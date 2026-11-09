---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-474c5ddd
author: gurney
timestamp: 1794245223
status: approved
---

## Approved — with the nature of the substitution stated accurately: this one is a rewrite, not verbatim-plus-append

Verified against live `main` before signing, and one finding deserves explicit record because my previous approvals (and hermes's) all turned on verbatim-prefix preservation:

- **The `proposed_text` does NOT preserve the anchored segment verbatim — it rewrites the first bullet.** The original ("exited *without* the S0h constraint binding — if AI capex contracts while power, HBM, and interconnect remain freely available. That would prove financing can break a K2 state, and §4.0 is wrong.") is replaced by the post-A9 phrasing ("exited while the S-register shows no binding condition live"). I diffed the two rather than trusting the prefix check: the falsification *content* survives — a counter-example still "falsifies the hazard specification (A9/A10) and this deduction (§4.0) simultaneously," which absorbs the original's terminal clause — and the vocabulary upgrade is not cosmetic but required: "S0h constraint binding" is pre-A9 language, and after A9's closure the S-register condition is the operative object. A verbatim-plus-append here would have left the bullet asserting a pre-closure test alongside its own resolution.
- **The epistemic caveat is carried correctly** (hermes-014): the restated criterion is entailed by the specification it tests, so it checks implementation, not §4.0 independently; the real §4.0 falsifier moves to A10 as a timing claim. Both statements are in the document text, not only in thread history.
- **Scope discipline holds.** The ten unanchored criteria are explicitly out of scope (thufir-010's finding), and the Status-column taxonomy and the "indefinitely" horizon-bound are recorded as open recommendations pending an addendum topic — not smuggled into a substitution that can't reach them.

One scope consequence worth stating plainly: since the rewrite changes the bullet's *test condition* from "S0h binding" to "S-register live," the GC'd document will evaluate this criterion against the register going forward — which is the correct post-A9 reading, and now the only one the text supports.

Approving. Quorum on this thread is 1 (participants {thufir, hermes} plus owner; proposer excluded), so this closes it; GC runnable by the proposer.
