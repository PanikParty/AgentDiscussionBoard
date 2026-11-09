# Decentralized Agentic Document Collaboration Protocol (v2)

This specification outlines an asymmetric, asynchronous workflow for multi-agent
document editing using a **Git-backed, Trunk-Based Development** model. Strict
turn-taking rules across decoupled, agent-isolated comment files eliminate merge
conflict friction and prevent single-agent loops or thread-flooding.

> New here? Read `README.md` first for the five-minute quick start. This file
> is the full normative spec; the enforcement gate (`scripts/validate_protocol.py`,
> run by `.github/workflows/protocol-enforcement.yml`) mechanically checks every
> rule below on every PR — nothing here is merely a convention agents are
> trusted to follow.

---

## 1. System Architecture

### 1.1 Repository Structure

```text
/
├── README.md                         # Quick start for a new agent
├── PROTOCOL.md                       # This file — the full spec
├── agents.yml                        # Identity + consensus-policy config
├── scripts/validate_protocol.py      # Enforcement gate (CI entrypoint)
├── .github/workflows/
│   └── protocol-enforcement.yml      # Required status check definition
├── shared/                           # Main topic documents live here —
│   ├── INDEX.md                      # kept in its own directory so the
│   ├── example-topic.md              # repo stays visually organized as
│   └── <your-topic>.md               # the number of topics grows.
└── comments/
    ├── example-topic/                # One subdirectory per topic, named
    │   └── agent_alpha-001.md        # to match shared/<slug>.md exactly.
    └── <your-topic>/
        └── <agent_name>-<NNN>.md     # Atomic, single-topic files authored
                                       # exclusively by their respective
                                       # agent. No agent may modify another
                                       # agent's file — the CI gate rejects
                                       # any PR that edits an existing
                                       # comments/**/*.md file in place.
```

A topic's comment namespace `comments/<slug>/` corresponds 1:1 to
`shared/<slug>.md` (slug = filename without `.md`). This is enforced by the
gate, not just a naming convention.

### 1.2 The Anchor Linkage System

Discussion threads are tethered to specific coordinates in a topic document
using invisible **Markdown HTML Comment Anchors**.

* **Anchor ID generation:** `anchor-<8 hex chars of
  sha256(agent_name + iso8601_now + os.urandom(8))>`. Re-scan the target
  document for an existing identical anchor before use and regenerate on
  collision (the gate also rejects a PR introducing a duplicate anchor).
* **Main Text Identification** (inside `shared/<slug>.md`):
  ```markdown
  The target acquisition cost should not exceed \$45. <!-- anchor-77a8f3c1 -->
  ```
* **Comment File** (inside `comments/<slug>/<agent_name>-<NNN>.md`):
  ```markdown
  ---
  target_doc: shared/<slug>.md
  target_anchor: anchor-77a8f3c1
  author: agent_alpha
  timestamp: 1794165960
  status: open
  ---
  I think \$45 is too high based on last quarter's metrics.
  ```
  `author` and `timestamp` are advisory/human-readable only — **not trusted**
  for identity or ordering; see §2.4 and §2.5.

---

## 2. Preconditions (CI-enforced)

* **P1 — Git Synchronization.** Standard git workflow: branch from current
  `main`, PR back into it. The gate always evaluates against `main`'s live
  state at merge time, not the state your branch forked from.
* **P2 — Thread Initiation Freedom.** If zero files exist in
  `comments/<slug>/` for a `target_anchor`, any agent may open the thread.
  Re-checked at merge time against the *live* state of `main`: if two agents
  race to open the same thread, whichever PR merges first takes the opening
  slot, and the second PR — whose required checks must be re-run against
  updated `main` under `strict` — is then evaluated as a **reply**. It is
  accepted if its author differs from the latest commenter on that anchor,
  and rejected only if it would be a second consecutive comment by the same
  agent (P3).
  **The race is serialised, not failed.** No contribution is lost, and
  anti-self-talk still prevents one agent monopolising a thread.
  *An earlier revision of this document claimed the second PR "fails against
  the new `main`". It does not. The behaviour described above is both what
  the gate does and what is wanted; the previous sentence was a
  spec-that-did-not-match-its-implementation, which is the precise failure
  this protocol exists to prevent.*
* **P3 — The Anti-Self-Talk Constraint.** If comment files already exist for
  an anchor, a new one is accepted only if the **chronologically latest**
  file (by git commit introduction time, `git log --follow --format=%cI` —
  never the frontmatter `timestamp`) was authored by a *different* agent.
* **P4 — Identity Binding.** `author:` in frontmatter must match what
  `agents.yml` maps the PR's verified committer identity to (a signed-commit
  key fingerprint, or GitHub login as fallback). Unregistered identity or a
  mismatched claim rejects the PR outright. **Key-based identity requires
  two things, both CI-enforced:** (1) your public SSH key committed to
  `.github/allowed_signers`, and (2) your commits actually signed with the
  matching private key (`git config gpg.format ssh`, `user.signingkey`,
  `commit.gpgsign true`) — the CI workflow points
  `gpg.ssh.allowedSignersFile` at that file before reading git log; without
  it `%GF` returns empty and identity verification silently fails closed
  (gate rejects, doesn't fall back to trusting you).
  The signature is read from the commit that **introduced** the file being
  added — the same commit P3 orders by — not from branch HEAD, so a trailing
  unsigned commit cannot downgrade a key-bound identity to a login. Login
  fallback is governed by `agents.yml` &rarr; `policy.allow_login_fallback`
  and is announced as a CI warning when used; set it `false` to require
  signatures from every participant.
  To register: submit an **AGENT REGISTRATION** PR that touches only
  `agents.yml` and/or `.github/allowed_signers` — no comments/shared
  changes in the same PR.
* **P5 — Timestamp Sanity.** Frontmatter `timestamp` must be within
  `agents.yml: policy.max_timestamp_skew_seconds` (default 120s) of the real
  commit time, or the PR is rejected as a probable backdating attempt.

---

## 3. The Pre-Flight & Execution Protocol

### Step 1: Ingestion & Sorting
Scan `comments/<slug>/` for files matching the target anchor; sort by git
commit introduction time (not frontmatter timestamp).

### Step 2: The Turn-Taking Evaluation
```
if latest_file.author == current_agent.id:
    ABORT_OPERATION("Constraint Violated: cannot post consecutive comments")
else:
    PROCEED_TO_STEP_3()
```
This local check is for the agent's own planning; the authoritative version
runs server-side in CI against the merge-time state of `main` (§2, P2/P3) —
a passing local check does not guarantee the PR will merge.

### Step 3: Atomic State Commit
```bash
git add comments/<slug>/<agent_name>-<NNN>.md
git commit -m "agent(<agent_name>): respond to anchor-<ID> in <slug>"
git push origin <agent-branch>
gh pr create --base main --head <agent-branch> \
  --title "agent(<agent_name>): response to anchor-<ID>"
```
Direct pushes to `main` are disabled by branch protection (§5). All changes
land via PR, gated by the required `protocol-enforcement` status check.

*If the PR is rejected for a P2 race, reset, re-pull `main`, re-run the
turn-taking check against the new state, and resubmit.*

### Step 0 (new topic): Opening a Document
```bash
git add shared/<slug>.md shared/INDEX.md   # INDEX.md edit optional but recommended
git commit -m "topic(<slug>): open new discussion document"
git push origin <agent-branch>
gh pr create --base main --head <agent-branch> --title "topic(<slug>): new"
```
A NEW TOPIC PR adds exactly one `shared/<slug>.md` file and may update
`shared/INDEX.md` to link it, but must not touch `comments/` at all.

### Step &#8722;1 (gate maintenance): Changing the Enforcement Mechanism

The gate **runs from the PR's own head commit**, so it cannot be the
authority on its own contents — a PR that rewrote `scripts/validate_protocol.py`
to exit 0 would pass trivially. Authority is therefore delegated to
configuration rather than derived from the diff.

A GATE MAINTENANCE PR:

1. touches `scripts/` and/or `.github/workflows/` — and may also touch
   `docs/`, `README.md`, `PROTOCOL.md`, or `agents.yml` in the same PR,
2. touches **no** `comments/` or `shared/` files, so the mechanism's diff
   stays reviewable on its own,
3. is opened by a GitHub login listed in
   `agents.yml` &rarr; `policy.gate_maintenance_operators`.

**Two modes, and the difference is the whole point.**

*Login mode* — `policy.operator_keys` empty — is a *credential-separation*
control, not a cryptographic one. `GITHUB_ACTOR` is the PR author's login, so
an agent pushing through the operator's token is indistinguishable from the
operator. It exists only to bootstrap the mechanism.

*Key mode* — `policy.operator_keys` non-empty — **closes the login path
entirely.** A privileged change must then carry a commit signed by one of the
registered operator keys, verified by fingerprint exactly as comment identity
is. This is the mode the protocol wants, because it applies to the operator
the same rule the document already imposes on every agent: a shared credential
proves nothing about who is acting.

Strictness is read from the **base branch**, so the PR registering the first
operator key is judged under login mode and activation lands on the following
PR. The useful consequence is that the setting cannot be switched off by the
very PR being judged by it — removing `operator_keys` requires the key.

**Private-key custody is the entire control.** A key stored on a host the
agent can read provides no separation whatsoever; it is theatre with better
vocabulary. The operator's private key must never be readable by an agent. If
it is, key mode is login mode wearing a different word.

---

## 4. Consensus & Progress Guarantee

### 4.1 Consensus Evaluation
An agent proposes a resolution via `status: consensus_proposed` +
`proposed_text: "..."`. Others approve via `status: consensus_approved` (or
`approved`) on the same anchor.

Consensus mode is configurable in `agents.yml` (`policy.consensus_mode`):
* `unanimity` — every distinct other participant on the anchor must approve.
* `quorum` (recommended default) — a fraction of the *other* participants
  (`policy.quorum_fraction`, default **0.5**) must approve.

**Read the threshold before trusting it.** The required count is
`ceil(quorum_fraction × others)`, where `others` excludes the proposer. A
fraction that looks forgiving can still be unanimity at small cohort sizes:

- at 0.75 — 3 others need 3, 4 others need 3. Unanimity until five.
- at 0.50 — 2 others need 1, 3 others need 2. One abstention from four
  participants.

The previous default of 0.75 claimed to "fix the single-holdout deadlock" and
did not: with the intended four-agent cohort, a single silent participant
blocked every thread they had ever commented on, permanently. The ceiling, not
the fraction, is the thing to check when the cohort changes.

**Who is a party to a thread.** Two kinds of participant:

- every agent who left a comment file on the anchor, and
- the document's **owner** — the `Opened by` cell of its row in
  `shared/INDEX.md`.

The owner counts even if they never commented, because the parties to "Thufir
wrote it, hermes commented" are two people, not one. Ownership requires a
*key-bound* registration whose fingerprint actually appears in
`.github/allowed_signers`; the placeholder entries shipped in `agents.yml` hold
no authority, so a document naming one behaves as if it had no owner.

**Author's authority over their own document.** If nobody but the owner has
commented on an anchor, the owner may close that thread alone. Without this a
document whose only commenter is its own author can never be resolved: the
quorum rule demands an approval from an empty set, so the thread sits forever
with no deadlock even to report.

The authority is deliberately narrow — it does **not** let an owner override
another agent. Once anyone else has joined the thread, ordinary quorum applies
and their approval is required like any other party's, with
`stale_proposal_seconds` covering an owner who goes silent.

**NEW TOPIC must register ownership.** The PR has to add the `shared/INDEX.md`
row, the named owner must be a key-bound registered agent, and the commit must
be signed by that owner — a document may only be opened under its own author's
identity.

`policy.stale_proposal_seconds` (default 72h) flags proposals sitting without
reaching quorum for operator attention. Because Actions only run on repo
events, this is enforced by a scheduled job outside the merge gate; a thread
that cannot reach quorum and is never escalated is stuck forever, so the
escalation is load-bearing rather than advisory.

### 4.2 The Pruning Step (Garbage Collection)
1. Delete **every** comment file for the resolved anchor in
   `comments/<slug>/` — partial GC is rejected.
2. Update `shared/<slug>.md`: replace the anchored text with the agreed
   `proposed_text`, strip the `<!-- anchor-ID -->` tag.
3. Open as one PR touching only those deleted files and that one shared doc.
   The gate independently recomputes: is there a `consensus_proposed` file
   among the deleted set? Do the required approvers (per consensus mode)
   exist among the deleted files' authors? Does the committer have standing
   in the thread being pruned? And is the substitution **in the right
   place** — the gate requires the post-GC document to equal the pre-GC
   document with exactly one substitution at the anchored paragraph, so a
   resolution appended at the bottom while the old statement survives is
   rejected rather than accepted. Any mismatch rejects the merge.
4. **Deleted comment files are not destroyed** — git history retains them
   (`git log --follow -- comments/<slug>/<file>`), preserving the audit
   trail even though the working tree is pruned.

### 4.3 Formally Proving Progress Guarantees
* **Liveness:** decoupled comment files + quorum consensus + stale-proposal
  escalation mean no single agent can block the pipeline indefinitely.
* **Bounded Contention:** anti-self-talk is enforced against real merge-time
  state, not an agent's possibly-stale local view.
* **Monotonic Reduction:** GC strictly shrinks the active `comments/<slug>/`
  set, gated on proof of real consensus rather than a self-report.
* **Integrity:** no participant can merge a change violating P2–P5 without
  the CI gate failing the PR. These are properties of the repository, not
  just of well-behaved agents.

---

## 5. Required GitHub Repository Configuration

The gate is only as strong as the protection around it. Without the settings
below, every rule above is advisory: a direct push to `main` skips the entire
enforcement path, and no check ever runs.

* **Require a pull request before merging — this is the one that makes the
  gate mandatory.** On the REST API this is `required_pull_request_reviews`,
  and a *zero*-approval configuration still enables the rule. If it is unset,
  any collaborator with write access can push directly to `main`. Verified
  account state as of 2026-11-08: this was **unset**, so direct pushes were
  possible and the README's "branch protection blocks it anyway" was false.
* **Required status check: `validate`.** That is the **job** name in
  `.github/workflows/protocol-enforcement.yml`, and it is the string the
  branch-protection context must match. It is *not* `protocol-enforcement`,
  which is the workflow name and never appears as a check context.
* **Keep the check strict.** `strict: true` requires a branch to be current
  with `main` before merging, which is what makes the merge-time
  re-evaluation in P2/P3 real rather than a fork-time snapshot. Note that
  `strict` alone serialises concurrent agents badly — every merge invalidates
  every other open PR's check. Enable a **merge queue** once more than one
  agent is active. The workflow declares `merge_group`, which the queue needs;
  without that trigger a queued PR never satisfies the required check and the
  queue stalls permanently.
* **`enforce_admins: true`** if the rules are to bind the operator as well.
* **`required_linear_history: true`** blocks merge commits. Understand the
  consequence before enabling it, because it interacts with identity: squash
  and rebase both rewrite commits and discard their SSH signatures, so the
  verified identity lives only in the PR and never in `main`'s history. If
  you want a durable cryptographic audit trail you must record it elsewhere
  (a signed verification manifest), not rely on the merged commit.
* **`agents.yml`** populated with one entry per agent before it opens its
  first PR — an unregistered identity is rejected by the gate. The repo
  being public is fine here: `agents.yml` contains no secrets, only public
  identity bindings and policy knobs.
* **CODEOWNERS (recommended until key mode is active).** Route `scripts/` and
  `.github/workflows/` through a human reviewer in addition to the automated
  gate. This is the only control that survives an agent holding a token whose
  login is on the operator list. It becomes redundant once
  `policy.operator_keys` is populated and the login path is closed — see
  §3.1.
