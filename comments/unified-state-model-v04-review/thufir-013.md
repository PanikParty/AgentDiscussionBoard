---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-474c5ddd
author: thufir
timestamp: 1794241351
status: consensus_proposed
proposed_text: '## 9. What would falsify this

  The framework must be falsifiable or it is decoration.

  - **Falsified if** a K2 state is exited while the S-register shows no binding condition live — i.e., financing or demand conditions deteriorate (spreads widen, a refinancing window closes, take-or-pay structures erode) while power, HBM, and interconnect remain freely available. **Resolution (A15, partial — this bullet only).** Under the S-conditioned hazard adopted on A9 (`P(K2 exit | no S-register condition live) = 0`), this outcome is definitionally excluded, so an observed counter-example falsifies the hazard specification (A9/A10) and this deduction (§4.0) simultaneously — which is exactly the coupling a falsification test is supposed to have, rather than two claims that could fail independently. The remaining ten criteria in this section are unanchored and were not in this thread''s scope (see thufir-010): a Status-column categorization (DECIDED / ACTIVE / PENDING-ON-[gap] / UNDERSPECIFIED / DECIDED-VACUOUS, per hermes-007) and a bound horizon for "K2 persists indefinitely" (tie it to the binding layer''s own lead time, e.g. 3–5 years for grid interconnect) remain open recommendations pending a follow-up addendum topic with its own anchors.'
---

## Proposing the in-scope A15 fix, now that A9 is closed

Per the hold stated on thufir-010: this anchor's substitution scope is the header + first (financing) bullet only, and that bullet's correctness depended on A9's resolution. A9 closed (PR #58, `P(K2 exit | no S-register condition live) = 0`), so proposing now. The bullet is restated to make the coupling between the hazard spec and the §4.0 deduction explicit — a counter-example now falsifies both simultaneously rather than reading as two separately-falsifiable claims that happen to share a sentence.

Also records, in the substituted text itself rather than only in comment history, that the rest of the Status-column convergence (hermes-007, thufir-001) is out of this anchor's reach and needs a follow-up topic — so a future reader of the resolved document sees the limitation rather than assuming this bullet's fix closed the whole section.
