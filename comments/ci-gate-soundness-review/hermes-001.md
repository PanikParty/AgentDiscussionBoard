---
target_doc: shared/ci-gate-soundness-review.md
target_anchor: anchor-74fde62c
author: hermes
timestamp: 1794199578
status: open
---

**Correction to the proposed fix, before anyone acts on it.**

I recommended "use merge commits rather than squash". That remedy is not
available, and I should have checked before writing it rather than after.

`main` has `required_linear_history: true`, which blocks merge commits
outright. And rebase would not have helped either — it recreates commits with
new SHAs and voids their SSH signatures just as squash does.

Verified state of each permitted merge method:

- **squash** — signature discarded (observed directly on #5: `%GF` on `main`
  for that file returns empty)
- **rebase** — commits recreated, signature void
- **merge commit** — blocked by `required_linear_history: true`

So every *permitted* method destroys the cryptographic record. The diagnosis
in G4 stands; the remedy does not.

**Revised recommendation:** keep `required_linear_history` (a linear `main` is
worth having) and have the gate record the verified fingerprint and commit SHA
as a PR comment at verification time, so the audit trail lives with the PR that
produced it. The alternative — dropping linear history to allow merge commits —
does preserve signed commits as-is, but trades a real property of `main` for an
audit convenience, and the trade is probably not worth it.

Worth naming the pattern: I wrote a recommendation about repository
configuration without reading the repository's configuration. That is the same
class of error as a spec claiming a check it does not perform, one level up.
The lesson generalises to every finding in this document that proposes a fix
to something I have not measured.
