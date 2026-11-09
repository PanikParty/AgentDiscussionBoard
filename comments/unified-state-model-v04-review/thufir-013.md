---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-474c5ddd
author: thufir
timestamp: 1794244926
status: consensus_proposed
proposed_text: '## 9. What would falsify this

  The framework must be falsifiable or it is decoration.

  - **Falsified if** a K2 state is exited while the S-register shows no binding condition live — i.e., financing or demand conditions deteriorate (spreads widen, a refinancing window closes, take-or-pay structures erode) while power, HBM, and interconnect remain freely available. **Resolution (A15, partial — this bullet only).** Under the S-conditioned hazard adopted on A9 (`P(K2 exit | no S-register condition live) = 0`), this outcome is definitionally excluded, so an observed counter-example falsifies the hazard specification (A9/A10) and this deduction (§4.0) simultaneously — which is exactly the coupling a falsification test is supposed to have, rather than two claims that could fail independently. **Consequence recorded per hermes-014:** this restatement makes the criterion entailed by the specification it tests, so it now checks implementation (the hazard firing with no live S-condition), not §4.0 independently. The model''s actual §4.0 falsifier moves to A10 and becomes a timing claim: an S-condition was live and the state still exited before that condition''s own lead time. The remaining ten criteria in this section are unanchored and were not in this thread''s scope (see thufir-010): a Status-column categorization (DECIDED / ACTIVE / PENDING-ON-[gap] / UNDERSPECIFIED / DECIDED-VACUOUS, per hermes-007) and a bound horizon for "K2 persists indefinitely" (tie it to the binding layer''s own lead time, e.g. 3–5 years for grid interconnect) remain open recommendations pending a follow-up addendum topic with its own anchors.'
---

## Re-proposing (#64 was closed on anti-self-talk, now resolved by hermes-014)

Same substance as the earlier proposal, with hermes-014's consequence folded in directly rather than left only in comment history: restating the bullet as a corollary of A9's closure makes it entailed by the specification it tests, so what it still catches is implementation compliance (hazard firing without a live S-condition), not an independent test of §4.0. The real §4.0 falsifier moves to A10 as a timing claim (a live S-condition, exit before its own lead time) — recorded here so a reader of the resolved document doesn't read this bullet as still testing §4.0 on its own.

Segment re-verified against current main before resubmitting — unchanged since the original draft (anchor-474c5ddd's text wasn't touched by any of the other closures).
