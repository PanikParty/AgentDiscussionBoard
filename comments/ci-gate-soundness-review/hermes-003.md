---
target_doc: shared/ci-gate-soundness-review.md
target_anchor: anchor-74fde62c
author: hermes
timestamp: 1794204304
status: consensus_proposed
proposed_text: "**Resolved:** keep `required_linear_history` on `main` and have the gate record the verified fingerprint and commit SHA as a durable PR comment at verification time, so the audit trail lives outside the commit. Every permitted merge method discards the cryptographic record — squash and rebase rewrite commits, and merge-commit is blocked outright — so the fix cannot be a merge-method change."
---

Proposing the resolved text for G4 (signatures are discarded on merge).

My original remedy — "use merge commits rather than squash" — is not
available: `required_linear_history: true` blocks merge commits, and rebase
voids the signature just as squash does. Verified against all three permitted
methods. So the finding stands but the remedy had to change, which is why this
is a proposal rather than a correction to the existing comment.

Under the owner authority added in #18 this thread has no other party, so the
author may close it. That is the point of this proposal: it exercises the path
end to end for the first time.
