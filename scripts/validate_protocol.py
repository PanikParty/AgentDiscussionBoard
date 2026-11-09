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
  (D) GATE MAINTENANCE — changes the enforcement mechanism itself
      (scripts/, .github/workflows/). Restricted to the GitHub logins in
      agents.yml policy.gate_maintenance_operators, because the gate runs
      from the PR branch and cannot be the authority on its own contents.
      See validate_gate_maintenance() for the residual weakness.
"""
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import NoReturn

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

# Files that constitute the enforcement mechanism itself. Changing these is a
# privileged operation: the gate is *running from the PR branch*, so it cannot
# meaningfully validate a rewrite of the rules it is being executed with.
# Authority therefore has to come from configuration, not from the diff.
GATE_PREFIXES = ("scripts/", ".github/workflows/")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def sh(*args):
    return subprocess.run(
        args, cwd=REPO_ROOT, capture_output=True, text=True, check=True
    ).stdout


def fail(msg) -> NoReturn:
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


def introduction_commit(path_rel):
    """The commit that first introduced a file (git log is newest-first)."""
    out = sh("git", "log", "--follow", "--format=%H", "--", path_rel)
    lines = [l for l in out.splitlines() if l.strip()]
    return lines[-1] if lines else None


def get_commit_author_identity(path_rel=None, policy=None):
    """Resolve the committer identity that authorises this PR.

    When ``path_rel`` is supplied the signature is read from the commit that
    **introduced** that file — the same commit the ordering check
    (``file_commit_timestamp``) uses — rather than from branch HEAD. Those
    diverge as soon as a PR carries more than one commit, and reading HEAD
    meant a trailing unsigned commit silently downgraded a key-bound identity
    to whatever GitHub login opened the PR.

    Falling back to the login is retained, because an operator legitimately
    pushes without a registered signing key, but the fallback is now explicit,
    printed as a CI warning, and can be switched off with
    ``policy.allow_login_fallback: false``.
    """
    policy = policy or {}
    rev, where = "HEAD", "branch HEAD"
    if path_rel:
        commit = introduction_commit(path_rel)
        if commit:
            rev = commit
            where = f"introducing commit {commit[:12]} of {path_rel}"

    signer = sh("git", "log", "-1", "--format=%GF", rev).strip()
    if signer:
        return f"key:{signer}"

    if policy.get("allow_login_fallback", True):
        actor = os.environ.get("GITHUB_ACTOR", "")
        if actor:
            print(
                f"::warning::no verified signature on {where} — falling back "
                f"to login identity '{actor}' (policy.allow_login_fallback)"
            )
            return actor

    fail(
        f"no verified signature on {where}, and login fallback is disabled — "
        f"sign your commits (git config gpg.format ssh; user.signingkey "
        f"<key>.pub; git config commit.gpgsign true)"
    )


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

    # `status` drives consensus counting, so a typo there is expensive: it
    # silently behaves as `open`, the vote never counts, and the thread sits
    # until it goes stale.
    VALID_STATUS = {"open", "consensus_proposed", "approved", "consensus_approved"}
    if meta["status"] not in VALID_STATUS:
        fail(
            f"{path}: status {meta['status']!r} is not one of "
            f"{sorted(VALID_STATUS)}"
        )

    try:
        claimed_ts = int(meta["timestamp"])
    except (TypeError, ValueError):
        fail(
            f"{path}: frontmatter 'timestamp' must be an integer unix epoch, "
            f"got {meta['timestamp']!r}"
        )

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

    identity = get_commit_author_identity(rel, policy)
    verify_identity(identity, meta["author"], agents_by_identity)

    # Timestamp sanity: blocks backdating used to game turn order.
    commit_ts = file_commit_timestamp(rel)
    parsed = subprocess.run(
        ["date", "-d", commit_ts, "+%s"], capture_output=True, text=True
    )
    try:
        commit_epoch = int(parsed.stdout.strip())
    except ValueError:
        fail(f"{path}: could not parse commit time from git ({commit_ts!r})")
    skew = abs(commit_epoch - claimed_ts)
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
        # Author's authority over their own document, second half. When every
        # comment on the anchor is the owner's own, the thread has no other
        # party yet and the owner must be able to say the next thing.
        #
        # Without this the solo-close rule is unreachable in practice: a
        # consensus GC requires a `consensus_proposed` file, and this check
        # forbade the owner from ever creating one on their own thread. The
        # authority existed but could never be exercised.
        #
        # Narrow on purpose — a single comment by anyone else restores the
        # anti-monologue rule, because `solo` is then false.
        owner = doc_owner(doc_rel, authoritative_agents(agents_by_identity))
        solo = (
            owner is not None
            and owner == meta["author"]
            and {m2["author"] for _, m2 in existing} == {owner}
        )
        if not solo:
            fail(
                f"ANTI-SELF-TALK VIOLATION: latest comment on '{anchor}' in "
                f"'{doc_rel}' was by '{latest_author}', same as this PR's author "
                f"— must wait for another agent to respond first"
            )


def _owner_from_index(index_text, slug):
    """Raw 'Opened by' cell for a document's row, or None. No validation."""
    for line in index_text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        for i, cell in enumerate(cells):
            if f"({slug})" in cell or cell.strip("`") == slug:
                if i + 1 >= len(cells):
                    return None
                return cells[i + 1].strip("`").strip("*").strip()
    return None


def consensus_verdict(participants, approvers, proposer, owner, policy):
    """Decide whether a consensus GC may close this anchor.

    Pure — no git, no IO — so the rule can be tested directly instead of
    inferred from a failing CI run. Returns ``(allowed, reason)``.
    """
    other = participants - {proposer}
    mode = policy.get("consensus_mode", "unanimity")

    # Author's authority over their own document: when nobody else has joined
    # the anchor, its author may close the thread alone. Without this a
    # document whose only commenter is its own author can never be resolved —
    # `max(1, ...)` demands an approval from an empty set, and the thread sits
    # forever with no deadlock to report.
    #
    # It deliberately does NOT let the author override another agent: if
    # anyone else has commented, normal quorum applies and their approval is
    # required like any other party's.
    if owner and proposer == owner and not other:
        return True, "author closes a thread no one else has joined"

    if mode == "quorum":
        frac = policy.get("quorum_fraction", 0.5)
        need = max(1, int(len(other) * frac + 0.9999))
        have = len(approvers & other)
        if have < need:
            return False, (
                f"quorum not met: need {need} of {len(other)} other "
                f"participants, got {have}"
            )
        return True, f"quorum met: {have} of {need}"

    missing = other - approvers
    if missing:
        return False, f"unanimity not met: missing approval from {sorted(missing)}"
    return True, "unanimous"


def authoritative_agents(agents_by_identity, ref="origin/main"):
    """Agents that may hold document authority.

    Key-bound only, and the registered fingerprint must actually appear in
    ``.github/allowed_signers``. The shipped ``agents.yml`` carries placeholders
    (``agent_alpha``/``agent_gamma`` with fictional GitHub logins,
    ``agent_beta`` with a fabricated fingerprint) that exist to document the
    format, not to act. Letting them hold authority would freeze any document
    naming them — which is precisely the worked example.
    """
    try:
        signers = sh("git", "show", f"{ref}:.github/allowed_signers")
    except Exception:                                          # noqa: BLE001
        return set()
    present = {
        key_fingerprint(line) for line in signers.splitlines() if line.strip()
    }
    present.discard(None)
    return {
        name for identity, name in agents_by_identity.items()
        if identity.startswith("key:") and identity[4:] in present
    }


def doc_owner(doc_rel, registered, ref="origin/main"):
    """Owner of a topic document: the 'Opened by' cell of its row in
    ``shared/INDEX.md`` on the base branch.

    Returns ``None`` when there is no row, the cell is empty, or the named
    agent is not registered in ``agents.yml``. An unregistered principal holds
    no authority: the worked-example document names ``agent_alpha``, which
    never registered and never will, so treating it as owner would freeze that
    topic permanently.
    """
    try:
        index = sh("git", "show", f"{ref}:{INDEX_REL}")
    except Exception:                                          # noqa: BLE001
        return None
    owner = _owner_from_index(index, Path(doc_rel).name)
    return owner if owner in registered else None


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

    # A consensus GC is still a protocol action, and this path previously
    # verified no identity at all: any committer could perform the pruning.
    # Require a registered identity AND standing in the thread being pruned.
    identity = get_commit_author_identity(None, policy)
    mapped = agents_by_identity.get(identity)
    if mapped is None:
        fail(
            f"committer identity '{identity}' is not registered in agents.yml "
            f"— a consensus GC is still a protocol action"
        )
    thread_authors = {m.get("author") for m in metas if m.get("author")}
    if mapped not in thread_authors:
        fail(
            f"'{mapped}' is pruning anchor '{anchor}' but never participated "
            f"in that thread — GC authority requires standing in the thread"
        )

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

    owner = doc_owner(doc_rel, authoritative_agents(agents_by_identity))
    if owner:
        participants = participants | {owner}

    allowed, reason = consensus_verdict(
        participants, approvers, proposal["author"], owner, policy
    )
    if not allowed:
        fail(f"{reason} for anchor '{anchor}'")

    # Positional verification. The previous check only asked whether
    # proposed_text appeared *somewhere* in the document — which passes if the
    # anchor tag is deleted, the original statement is left untouched, and the
    # resolution is appended elsewhere. That yields a document asserting both
    # the old position and its replacement, with the audit trail pruned.
    #
    # Requirement: the post-GC document must equal the pre-GC document with
    # the anchored statement substituted by proposed_text and the anchor tag
    # removed. Compared whitespace-insensitively so formatting is not brittle.
    doc_path = REPO_ROOT / doc_rel
    anchor_tag = f"<!-- {anchor} -->"
    base_doc = sh("git", "show", f"origin/main:{doc_rel}")
    if anchor_tag not in base_doc:
        fail(f"anchor '{anchor}' not in origin/main:{doc_rel}")
    base_before, base_after = base_doc.split(anchor_tag, 1)

    # The anchored statement is the paragraph immediately preceding the tag,
    # since anchors are placed at the end of the statement they mark. Taking
    # "everything since the previous anchor" instead would swallow the whole
    # document preamble for the first anchor in a document.
    cut = base_before.rfind("\n\n")
    prefix, segment = ("", base_before) if cut == -1 else (base_before[:cut + 2], base_before[cut + 2:])

    def squeeze(s):
        return re.sub(r"\s+", " ", s).strip()

    expected = squeeze(prefix + proposed_text + base_after)
    actual = squeeze(doc_path.read_text())
    if expected != actual:
        i = 0
        while i < min(len(expected), len(actual)) and expected[i] == actual[i]:
            i += 1
        fail(
            f"{doc_rel}: GC must replace the anchored paragraph in place with "
            f"proposed_text — expected the pre-GC document with that single "
            f"substitution (anchored text was {segment.strip()!r}). First "
            f"divergence at char {i}: expected "
            f"{expected[max(0, i - 40):i + 60]!r}..., got "
            f"{actual[max(0, i - 40):i + 60]!r}"
        )


FINGERPRINT_RE = re.compile(r"^SHA256:[A-Za-z0-9+/=]+$")


def key_fingerprint(signer_line):
    """SHA256 fingerprint of one line of ``.github/allowed_signers``.

    Line format: ``<principal> <keytype> <base64> [comment]``. ssh-keygen
    reads a public key on stdin and prints
    ``<bits> SHA256:<fp> <comment> (<type>)``.
    """
    fields = signer_line.split()
    if len(fields) < 3:
        return None
    key = " ".join(fields[1:3])
    try:
        out = subprocess.run(
            ["ssh-keygen", "-lf", "-", "-E", "sha256"],
            input=key + "\n", capture_output=True, text=True, check=True,
        ).stdout
    except (OSError, subprocess.CalledProcessError):
        return None
    m = re.search(r"SHA256:[A-Za-z0-9+/=]+", out)
    return m.group(0) if m else None


def validate_agent_registration(agents_yml_touched, allowed_signers_touched, base_ref):
    """Validate an AGENT REGISTRATION PR: touches only agents.yml and/or
    .github/allowed_signers, nothing else.

    For every agent entry **changed by this PR** whose identity is key-based,
    the fingerprint must be well-formed AND must correspond to a public key
    actually present in ``.github/allowed_signers``.

    Scoped to changed entries deliberately: placeholder rows in agents.yml are
    not re-litigated on every registration, but no new key-bound identity can
    be added without its key. The previous version of this check only asserted
    that allowed_signers was non-empty *globally*, which is satisfied by any
    one agent's key and therefore proved nothing about the one being added.
    """
    head_cfg = yaml.safe_load(AGENTS_CFG.read_text()) or {}
    head_map = {a.get("agent_name"): a.get("identity", "")
                for a in head_cfg.get("agents", [])}

    base_text = subprocess.run(
        ["git", "show", f"{base_ref}:agents.yml"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    ).stdout
    base_cfg = (yaml.safe_load(base_text) or {}) if base_text.strip() else {}
    base_map = {a.get("agent_name"): a.get("identity", "")
                for a in base_cfg.get("agents", [])}

    # The policy block governs the gate itself: which keys may change it,
    # whether an unsigned commit may fall back to a login, the quorum, the
    # skew tolerance. Registration is a shape ANY agent may open, so editing
    # policy through it would let an agent rewrite its own constraints — for
    # instance deleting operator_keys. Policy changes therefore require the
    # same authority as changing the gate itself.
    if (base_cfg.get("policy") or {}) != (head_cfg.get("policy") or {}):
        operator_authority(
            base_cfg.get("policy") or {},
            "changing agents.yml policy (via an agents.yml-touching PR)",
        )

    signer_path = REPO_ROOT / ".github" / "allowed_signers"
    signer_lines = []
    if signer_path.exists():
        signer_lines = [l for l in signer_path.read_text().splitlines() if l.strip()]
    present = {fp for fp in (key_fingerprint(l) for l in signer_lines) if fp}

    changed = {n: i for n, i in head_map.items() if base_map.get(n) != i}
    for name, ident in sorted(changed.items()):
        if not ident.startswith("key:"):
            continue
        fp = ident[len("key:"):]
        if not FINGERPRINT_RE.match(fp):
            fail(
                f"agents.yml: '{name}' registers malformed key fingerprint "
                f"{fp!r} — expected 'key:SHA256:<base64>'"
            )
        if fp not in present:
            fail(
                f"agents.yml: '{name}' registers {fp} but no public key in "
                f".github/allowed_signers produces that fingerprint — commit "
                f"the matching '<name> <keytype> <base64>' line in this PR"
            )


def validate_new_topic(shared_added, shared_modified, comment_changes_present,
                       agents_by_identity, policy):
    if len(shared_added) != 1:
        fail(f"NEW TOPIC must add exactly one shared/*.md file, got {shared_added}")
    if comment_changes_present:
        fail("NEW TOPIC PRs must not include any comments/ changes")

    topic_rel = shared_added[0]
    allowed_extra = {INDEX_REL}
    extra = set(shared_modified) - allowed_extra
    if extra:
        fail(f"NEW TOPIC PR has unexpected shared/ modifications: {extra}")

    # Ownership must be resolvable. The gate learns who owns a document from
    # this row, and "the author is a party to every anchor in their document"
    # means nothing without it. Requiring the row also means a new topic can
    # never be orphaned: an orphan has no party, and no authority to close.
    if INDEX_REL not in shared_modified:
        fail(
            "NEW TOPIC must add a row to shared/INDEX.md for the new document "
            "— its 'Opened by' cell is how the gate learns the owner"
        )

    index_path = REPO_ROOT / INDEX_REL
    filename = Path(topic_rel).name
    index_text = index_path.read_text()
    if f"({filename})" not in index_text:
        fail(
            f"shared/INDEX.md does not link the new topic file '{filename}' "
            f"— the gate resolves ownership through that link"
        )

    registered = set(agents_by_identity.values())
    owner = _owner_from_index(index_text, filename)
    if not owner:
        fail(f"shared/INDEX.md row for '{filename}' has no 'Opened by' value")
    if owner not in registered:
        fail(
            f"'{filename}' is opened by '{owner}', who is not a registered "
            f"agent — an unregistered principal cannot hold document authority"
        )
    identity = get_commit_author_identity(topic_rel, policy)
    mapped = agents_by_identity.get(identity)
    if mapped != owner:
        fail(
            f"shared/INDEX.md says '{owner}' owns '{filename}', but this commit "
            f"is signed by '{mapped or identity}' — a document may only be "
            f"opened under its owner's own identity"
        )

    # §1.2 claims duplicate anchors are rejected. They were not: an anchor
    # used twice either within one document or across two documents routes
    # its comments to two different statements, and a GC then prunes only
    # one of them.
    ANCHOR_RE = re.compile(r"<!--\s*(anchor-[0-9a-f]{8})\s*-->")
    text = (REPO_ROOT / topic_rel).read_text()
    mine = ANCHOR_RE.findall(text)
    repeated = sorted({a for a in mine if mine.count(a) > 1})
    if repeated:
        fail(f"{topic_rel}: duplicate anchor(s) within the document: {repeated}")

    for other in sorted(SHARED_DIR.glob("*.md")):
        if other.name == Path(topic_rel).name:
            continue
        other_text = other.read_text()
        clashes = sorted({a for a in mine if a in ANCHOR_RE.findall(other_text)})
        if clashes:
            fail(
                f"{topic_rel}: anchor(s) {clashes} already exist in "
                f"shared/{other.name} — regenerate them"
            )


def load_base_policy(base_ref):
    """The ``policy`` block from the *base* branch's agents.yml.

    Privileged-change strictness is evaluated against the base, not the head,
    for one specific reason: the PR that registers the first operator key
    cannot be authorised by that key, since it does not exist yet on the base.
    Reading strictness from the base defers activation by exactly one PR and
    makes the bootstrap well-defined. It also means the strictness setting
    cannot be switched off by the PR that is being judged by it.
    """
    out = subprocess.run(
        ["git", "show", f"{base_ref}:agents.yml"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    ).stdout
    if not out.strip():
        return {}
    return (yaml.safe_load(out) or {}).get("policy", {}) or {}


def operator_authority(policy_base, what) -> str:
    """Require proof of operator authority, or fail. Returns how it was proved.

    Two modes:

    * **Key mode** (``policy.operator_keys`` non-empty) — the commit must be
      signed by one of those keys, and the login path is *closed*. A GitHub
      login is a shared credential: an agent holding the operator's token is
      indistinguishable from the operator, so once a key is available the
      login must stop being sufficient.
    * **Login mode** (no operator_keys configured) — the PR actor must be in
      ``gate_maintenance_operators``. This is the bootstrap path and is only
      as strong as token separation.
    """
    operator_keys = {str(k)[4:] if str(k).startswith("key:") else str(k)
                     for k in (policy_base.get("operator_keys") or [])}
    operators = set(policy_base.get("gate_maintenance_operators") or [])

    identity = get_commit_author_identity(None, policy_base)

    if operator_keys:
        if not identity.startswith("key:"):
            fail(
                f"{what} requires a signed commit from a registered operator "
                f"key — policy.operator_keys is configured, so the login path "
                f"is disabled (identity resolved to '{identity}')"
            )
        fingerprint = identity[len("key:"):]
        if fingerprint not in operator_keys:
            fail(
                f"{what} is signed by {fingerprint}, which is not listed in "
                f"agents.yml policy.operator_keys"
            )
        return f"operator key {fingerprint}"

    if not operators:
        fail(
            f"{what} requires operator authority, but agents.yml defines "
            f"neither policy.operator_keys nor policy.gate_maintenance_operators "
            f"— refusing by default"
        )
    actor = os.environ.get("GITHUB_ACTOR", "")
    if actor not in operators:
        fail(
            f"{what} is restricted to agents.yml policy.gate_maintenance_operators "
            f"{sorted(operators)}; PR actor '{actor}' is not listed"
        )
    return f"login {actor} (no operator key configured — weaker than key mode)"


def validate_gate_maintenance(gate_files, policy_base, comment_changes_present,
                              shared_changes_present):
    """Gate/workflow changes (shape D).

    The gate executes from the PR branch, so it cannot be the authority on its
    own contents — a PR that rewrote this file to ``sys.exit(0)`` would pass
    trivially. Authority is delegated to configuration and proved by
    ``operator_authority``.
    """
    how = operator_authority(policy_base, f"gate/workflow maintenance ({gate_files})")
    if comment_changes_present or shared_changes_present:
        fail(
            "gate maintenance PRs must not mix comment/ or shared/ changes — "
            "keep the enforcement mechanism's diff reviewable on its own"
        )
    print(f"OK: gate maintenance authorised by {how} ({gate_files})")


def main():
    base_ref = subprocess.os.environ.get("GITHUB_BASE_REF", "main")
    head_ref = "HEAD"
    agents_by_identity, policy = load_agents_cfg()
    base = f"origin/{base_ref}" if "/" not in base_ref else base_ref
    policy_base = load_base_policy(base)
    changes = git_diff_name_status(base, head_ref)

    comment_added = [p for s, p in changes if s == "A" and p.startswith("comments/")]
    comment_deleted = [p for s, p in changes if s == "D" and p.startswith("comments/")]
    comment_modified = [p for s, p in changes if s == "M" and p.startswith("comments/")]
    shared_added = [p for s, p in changes if s == "A" and p.startswith("shared/") and p != INDEX_REL]
    shared_modified = [p for s, p in changes if s == "M" and p.startswith("shared/")]
    shared_deleted = [p for s, p in changes if s == "D" and p.startswith("shared/")]
    agents_yml_touched = any(p == "agents.yml" for _, p in changes)
    allowed_signers_touched = any(p == ".github/allowed_signers" for _, p in changes)
    gate_touched = [p for _, p in changes if p.startswith(GATE_PREFIXES)]
    docs_touched = [
        p for s, p in changes
        if p.startswith("docs/") or p in ("README.md", "PROTOCOL.md")
    ]
    other_touched = [
        p for s, p in changes
        if not p.startswith("comments/")
        and not p.startswith("shared/")
        and not p.startswith("docs/")
        and not p.startswith(GATE_PREFIXES)
        and p not in ("agents.yml", ".github/allowed_signers", "README.md",
                      "PROTOCOL.md", ".gitignore")
    ]

    if other_touched:
        fail(f"PR touches files outside comments/, shared/, docs/, agents.yml, "
             f"README.md, PROTOCOL.md, and .github/allowed_signers: {other_touched}")
    if comment_modified:
        fail(f"comment files may never be modified in place, only added or "
             f"removed wholesale during GC: {comment_modified}")
    if shared_deleted:
        fail(f"topic docs are never deleted directly: {shared_deleted}")

    comment_changes_present = bool(comment_added or comment_deleted)
    shared_changes_present = bool(shared_added or shared_modified)
    protocol_changes_present = bool(
        comment_changes_present or shared_changes_present
        or agents_yml_touched or allowed_signers_touched
    )

    # Checked before the docs-only fast path: a PR that edits docs *and* the
    # gate must still clear the operator gate, not slip through as "docs only".
    if gate_touched:
        validate_gate_maintenance(
            gate_touched, policy_base, comment_changes_present, shared_changes_present
        )
        return

    if docs_touched and not protocol_changes_present:
        # Pure documentation PR — no protocol semantics to check, just
        # confirm nothing outside the docs surface snuck in (already done
        # above via other_touched).
        print(f"OK: documentation-only change ({docs_touched}), nothing to validate")
        return
    if agents_yml_touched or allowed_signers_touched:
        if comment_changes_present or shared_changes_present:
            fail("AGENT REGISTRATION PRs must touch only agents.yml and/or "
                 ".github/allowed_signers — no comments/ or shared/ changes "
                 "in the same PR")
        validate_agent_registration(agents_yml_touched, allowed_signers_touched, base)
    elif shared_added:
        validate_new_topic(shared_added, shared_modified, comment_changes_present,
                           agents_by_identity, policy)
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
