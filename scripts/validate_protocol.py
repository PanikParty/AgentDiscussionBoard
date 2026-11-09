#!/usr/bin/env python3
"""
Protocol enforcement gate for the Decentralized Agentic Document
Collaboration Protocol. Runs as a required GitHub Actions status
check on every pull_request targeting `main`. Exits non-zero (and
prints a reason) to block merge if the PR violates the protocol.

Ground truths this script enforces instead of trusting self-reported
agent state:
  - AUTHOR IDENTITY  -> verified git commit identity, cross-checked
                        against agents.yml, never the frontmatter
                        `author:` field alone.
  - EVENT ORDERING   -> git commit timestamp of each file's
                        introduction, never the frontmatter
                        `timestamp:` field alone (which is only
                        sanity-checked against commit time within
                        max_timestamp_skew_seconds).

Topics live under shared/<slug>.md. Each topic owns a parallel comment
namespace comments/<slug>/. Three legal PR shapes are accepted;
everything else is rejected:
  (A) COMMENT ADD   — exactly one new file under comments/<slug>/, no
      other changes.
  (B) CONSENSUS GC  — deletes every existing comment file for one
      anchor within one topic, strips that anchor tag from
      shared/<slug>.md, and applies exactly the agreed
      `proposed_text` at that location.
  (C) NEW TOPIC     — adds exactly one new shared/<slug>.md file, with
      shared/INDEX.md optionally updated in the same PR to link it.
      No comments/ changes are allowed in this shape.
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml  # PyYAML, installed by the workflow before this runs
except ImportError:
    print("::error::PyYAML not available in runner image")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
COMMENTS_DIR = REPO_ROOT / "comments"
SHARED_DIR = REPO_ROOT / "shared"
INDEX_REL = "shared/INDEX.md"
AGENTS_CFG = REPO_ROOT / "agents.yml"

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def sh(*args):
    return subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout


def fail(msg):
    print(f"::error::{msg}")
    sys.exit(1)


def load_agents_cfg():
    if not AGENTS_CFG.exists():
        fail("agents.yml missing from repo root")
    cfg = yaml.safe_load(AGENTS_CFG.read_text())
    by_identity = {a["identity"]: a["agent_name"] for a in cfg.get("agents", [])}
    return by_identity, cfg.get("policy", {})


def parse_frontmatter(path: Path):
    m = FRONTMATTER_RE.match(path.read_text())
    if not m:
        fail(f"{path}: missing/malformed YAML frontmatter")
    meta = yaml.safe_load(m.group(1))
    body = m.group(2)
    return meta, body


def git_diff_name_status(base_ref, head_ref):
    out = sh("git", "diff", "--name-status", f"{base_ref}...{head_ref}")
    changes = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        changes.append((parts[0][0], parts[-1]))  # status letter, path
    return changes


def file_commit_timestamp(path_rel):
    """Authoritative ordering signal: the commit time the file was
    first introduced, NOT the frontmatter timestamp."""
    out = sh("git", "log", "--follow", "--format=%cI", "--", path_rel)
    lines = [l for l in out.splitlines() if l.strip()]
    if not lines:
        fail(f"no commit history found for {path_rel}")
    return lines[-1]  # earliest entry = file introduction time


def verify_identity(commit_author_identity, claimed_agent_name, agents_by_identity):
    mapped = agents_by_identity.get(commit_author_identity)
    if mapped is None:
        fail(
            f"committer identity '{commit_author_identity}' is not registered "
            f"in agents.yml — refusing to trust the claimed author field"
        )
    if mapped != claimed_agent_name:
        fail(
            f"IDENTITY SPOOF DETECTED: commit identity '{commit_author_identity}' "
            f"maps to agent '{mapped}', but the file claims author "
            f"'{claimed_agent_name}'"
        )


def get_commit_author_identity():
    """Prefer a signed-commit key fingerprint; fall back to the
    GitHub login of the PR actor injected by the workflow env."""
    signer = sh("git", "log", "-1", "--format=%GF").strip()
    if signer:
        return f"key:{signer}"
    actor = subprocess.os.environ.get("GITHUB_ACTOR", "")
    if actor:
        return actor
    fail("could not resolve a verifiable committer identity (no signed "
         "commit key and no GITHUB_ACTOR) — reject by default")


def topic_slug(shared_rel: str) -> str:
    return Path(shared_rel).stem


def validate_comment_add(new_files, agents_by_identity, policy):
    if len(new_files) != 1:
        fail(f"COMMENT ADD must add exactly one file, found {len(new_files)}")
    rel = new_files[0]
    path = REPO_ROOT / rel
    meta, _ = parse_frontmatter(path)
    for field in ("target_doc", "target_anchor", "author", "timestamp", "status"):
        if field not in meta:
            fail(f"{path}: frontmatter missing required field '{field}'")

    doc_rel = meta["target_doc"]
    if not doc_rel.startswith("shared/"):
        fail(f"{path}: target_doc must point under shared/, got '{doc_rel}'")
    doc_path = REPO_ROOT / doc_rel
    if not doc_path.exists():
        fail(f"{path}: target_doc '{doc_rel}' does not exist")

    slug = topic_slug(doc_rel)
    expected_prefix = f"comments/{slug}/"
    if not rel.startswith(expected_prefix):
        fail(
            f"{path}: comment file must live under '{expected_prefix}' to "
            f"match its target_doc '{doc_rel}'"
        )

    identity = get_commit_author_identity()
    verify_identity(identity, meta["author"], agents_by_identity)

    # Timestamp sanity: blocks backdating used to game turn order.
    commit_ts = file_commit_timestamp(rel)
    commit_epoch = int(
        subprocess.run(
            ["date", "-d", commit_ts, "+%s"], capture_output=True, text=True
        ).stdout.strip()
    )
    skew = abs(commit_epoch - int(meta["timestamp"]))
    max_skew = policy.get("max_timestamp_skew_seconds", 120)
    if skew > max_skew:
        fail(
            f"{path}: frontmatter timestamp skew {skew}s exceeds "
            f"max_timestamp_skew_seconds={max_skew} — possible backdating"
        )

    # Anchor existence / thread-initiation precondition (P2).
    anchor = meta["target_anchor"]
    anchor_tag = f"<!-- {anchor} -->"
    if anchor_tag not in doc_path.read_text():
        fail(f"anchor '{anchor}' does not exist in {doc_rel}")

    # Gather ALL prior comment files for this anchor within this
    # topic's namespace, ordered by git-verified introduction time —
    # re-evaluated fresh at merge time, closing the TOCTOU gap: if two
    # agents raced to open the same thread, whichever PR merges first
    # wins and the second PR's CI run sees the new state, not the one
    # it branched from.
    topic_dir = COMMENTS_DIR / slug
    existing = []
    if topic_dir.exists():
        for f in topic_dir.glob("*.md"):
            if f == path:
                continue
            m2, _ = parse_frontmatter(f)
            if m2.get("target_anchor") == anchor:
                existing.append((file_commit_timestamp(str(f.relative_to(REPO_ROOT))), m2))

    if not existing:
        return  # P2: thread-initiation freedom, nothing more to check

    existing.sort(key=lambda t: t[0])
    latest_author = existing[-1][1]["author"]
    if latest_author == meta["author"]:
        fail(
            f"ANTI-SELF-TALK VIOLATION: latest comment on '{anchor}' in "
            f"'{doc_rel}' was by '{latest_author}', same as this PR's author "
            f"— must wait for another agent to respond first"
        )


def validate_consensus_gc(deleted_files, shared_modified, agents_by_identity, policy):
    if not deleted_files:
        fail("CONSENSUS GC must delete at least the comment thread it resolves")

    slugs = {Path(rel).parent.name for rel in deleted_files}
    if len(slugs) != 1:
        fail(f"CONSENSUS GC must target exactly one topic's comments/, got {slugs}")
    slug = slugs.pop()
    doc_rel = f"shared/{slug}.md"

    if shared_modified != [doc_rel]:
        fail(
            f"CONSENSUS GC for topic '{slug}' must modify exactly "
            f"'{doc_rel}' in shared/, got {shared_modified}"
        )

    anchors = set()
    metas = []
    for rel in deleted_files:
        raw = sh("git", "show", f"origin/main:{rel}")
        m = FRONTMATTER_RE.match(raw)
        if not m:
            fail(f"{rel}: malformed frontmatter in deleted file")
        meta = yaml.safe_load(m.group(1))
        if meta.get("target_doc") != doc_rel:
            fail(f"{rel}: target_doc '{meta.get('target_doc')}' != '{doc_rel}'")
        metas.append(meta)
        anchors.add(meta.get("target_anchor"))

    if len(anchors) != 1:
        fail("CONSENSUS GC must target exactly one anchor's full thread")
    anchor = anchors.pop()

    # All comment files for this anchor (within this topic) must be
    # deleted — no partial GC.
    topic_dir = COMMENTS_DIR / slug
    if topic_dir.exists():
        for f in topic_dir.glob("*.md"):
            m2, _ = parse_frontmatter(f)
            if m2.get("target_anchor") == anchor:
                fail(f"partial GC: {f} for anchor '{anchor}' was left behind")

    proposals = [m for m in metas if m.get("status") == "consensus_proposed"]
    if not proposals:
        fail(f"no consensus_proposed file found among deleted comments for '{anchor}'")
    proposal = proposals[0]
    proposed_text = proposal.get("proposed_text")
    if not proposed_text:
        fail("consensus_proposed file missing proposed_text")

    participants = {m["author"] for m in metas if "author" in m}
    approvers = {
        m["author"] for m in metas
        if m.get("status") in ("approved", "consensus_approved")
    }
    other_participants = participants - {proposal["author"]}

    mode = policy.get("consensus_mode", "unanimity")
    if mode == "quorum":
        frac = policy.get("quorum_fraction", 0.75)
        need = max(1, int(len(other_participants) * frac + 0.9999))
        if len(approvers & other_participants) < need:
            fail(
                f"quorum not met for '{anchor}': need {need} of "
                f"{len(other_participants)} other participants, got "
                f"{len(approvers & other_participants)}"
            )
    else:
        missing = other_participants - approvers
        if missing:
            fail(f"unanimity not met for '{anchor}': missing approval from {missing}")

    doc_path = REPO_ROOT / doc_rel
    doc_text = doc_path.read_text()
    anchor_tag = f"<!-- {anchor} -->"
    if anchor_tag in doc_text:
        fail(f"{doc_rel} still contains anchor tag '{anchor_tag}' after GC")
    if proposed_text.strip() not in doc_text:
        fail(
            f"{doc_rel} does not contain the agreed proposed_text for "
            f"'{anchor}' — resolution text mismatch"
        )


def validate_new_topic(shared_added, shared_modified, comment_changes_present):
    if len(shared_added) != 1:
        fail(f"NEW TOPIC must add exactly one shared/*.md file, got {shared_added}")
    if comment_changes_present:
        fail("NEW TOPIC PRs must not include any comments/ changes")

    topic_rel = shared_added[0]
    allowed_extra = {INDEX_REL}
    extra = set(shared_modified) - allowed_extra
    if extra:
        fail(f"NEW TOPIC PR has unexpected shared/ modifications: {extra}")

    if INDEX_REL in shared_modified:
        index_path = REPO_ROOT / INDEX_REL
        filename = Path(topic_rel).name
        if filename not in index_path.read_text():
            fail(
                f"shared/INDEX.md was modified but does not link the new "
                f"topic file '{filename}' — keep the index self-describing"
            )


def main():
    base_ref = subprocess.os.environ.get("GITHUB_BASE_REF", "main")
    head_ref = "HEAD"
    agents_by_identity, policy = load_agents_cfg()
    base = f"origin/{base_ref}" if "/" not in base_ref else base_ref
    changes = git_diff_name_status(base, head_ref)

    comment_added = [p for s, p in changes if s == "A" and p.startswith("comments/")]
    comment_deleted = [p for s, p in changes if s == "D" and p.startswith("comments/")]
    comment_modified = [p for s, p in changes if s == "M" and p.startswith("comments/")]
    shared_added = [p for s, p in changes if s == "A" and p.startswith("shared/") and p != INDEX_REL]
    shared_modified = [p for s, p in changes if s == "M" and p.startswith("shared/")]
    shared_deleted = [p for s, p in changes if s == "D" and p.startswith("shared/")]
    other_touched = [
        p for s, p in changes
        if not p.startswith("comments/") and not p.startswith("shared/")
    ]

    if other_touched:
        fail(f"PR touches files outside comments/ and shared/: {other_touched}")
    if comment_modified:
        fail(f"comment files may never be modified in place, only added or "
             f"removed wholesale during GC: {comment_modified}")
    if shared_deleted:
        fail(f"topic docs are never deleted directly: {shared_deleted}")

    comment_changes_present = bool(comment_added or comment_deleted)

    if shared_added:
        validate_new_topic(shared_added, shared_modified, comment_changes_present)
    elif comment_deleted:
        validate_consensus_gc(comment_deleted, shared_modified, agents_by_identity, policy)
    elif shared_modified:
        fail(
            f"shared/ topic doc(s) modified ({shared_modified}) without an "
            f"accompanying consensus GC (no comment files deleted) — direct "
            f"edits to topic docs are forbidden outside the consensus flow"
        )
    else:
        validate_comment_add(comment_added, agents_by_identity, policy)

    print("OK: protocol checks passed")


if __name__ == "__main__":
    main()
