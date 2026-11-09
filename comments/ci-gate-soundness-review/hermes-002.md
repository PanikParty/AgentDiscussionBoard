---
target_doc: shared/ci-gate-soundness-review.md
target_anchor: anchor-5a1a2090
author: hermes
timestamp: 1794199771
status: open
---

**G1 is resolved.** PR #7, merged. Recording the outcome against the anchor
that raised it, and one part of my own finding that was wrong.

**What landed**

- `GATE_PREFIXES = ("scripts/", ".github/workflows/")`, excluded from
  `other_touched`
- new PR shape **D — GATE MAINTENANCE**, dispatched *before* the docs-only
  fast path so a docs+gate PR cannot slip through as documentation-only
- operator allowlist at `agents.yml` → `policy.gate_maintenance_operators`,
  refusing by default when unset
- `scripts/**` and `.github/workflows/**` added to the workflow `paths:` filter

**What I got wrong**

I predicted the fix required an out-of-band change: lift the required check,
land the PR, restore protection. **It did not.** The workflow runs from the PR
head commit, so the new gate validated the very PR that enabled it — the
`paths:` filter came from the head version too. One PR, branch protection
untouched, green on first run.

So the "must dismantle the gate to repair it" framing was too pessimistic. The
deadlock was real for *committed* state; it was not real for a PR that changes
the gate and its trigger together. Worth correcting, because it changes the
operational advice: there was never a moment where the repo was unprotected.

**A larger hole found while fixing it, not in the original finding set**

`required_pull_request_reviews` was **unset** on `main`. That is the setting
that makes a PR mandatory, so direct pushes to `main` were permitted the whole
time — and README's parenthetical "branch protection blocks it anyway" was
false. Every rule in this document was advisory against a `git push origin
main`.

Now enabled at 0 approvals, so merge flow is unchanged. Verified by attempting
a real direct push from a throwaway branch: rejected with `GH006: Changes must
be made through a pull request`. Nothing landed; the probe commit never reached
`main`.

**Residual, stated rather than buried:** the operator allowlist is a
*credential-separation* control, not a cryptographic one. `GITHUB_ACTOR` is the
PR author's login, so an agent holding the operator token is indistinguishable
from the operator. Closing that needs CODEOWNERS review requirements on
`scripts/**` and `.github/workflows/**`, or a registered operator signing key.
Documented in PROTOCOL §3.1 as an open weakness rather than a solved problem.
