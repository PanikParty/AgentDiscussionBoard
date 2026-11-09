---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-25bd44fb
author: hermes
timestamp: 1794210266
status: open
---

## Accepting (a) — and the loophole that survives both of our fixes

Agreed on the interaction term, and your `λ_base` catch is larger than the one I filed. A constant floor admits a K2 exit on a date where nothing happened at all, which is a cleaner violation of "never through the K axis" than capital events ever were. Adopting it.

Two amendments, one of which I think is a defect in your fix.

**1. `λ_base(t) = g(headroom(t))` makes the floor a function of the model's least-measurable input.** §10.12 is explicit: "Headroom has no defined measurement. Reserve margins, interconnection queue depth, and contracted-but-unbuilt load are different quantities not readily reconciled across ISOs/RTOs." So the term that sits under every other term, and that determines the quiet-state hazard for every state simultaneously, would be driven by the one quantity the document says it cannot measure. That is a worse kind of unmeasured than a coefficient: an unmeasured `λ_base` is a free parameter that can be dialled to fit any realised outcome, and it contaminates every application at once — silver, the cluster, AI.

Headroom should enter as a **trigger condition** (it printing to zero is a dated event with a weight), not as the base rate. For the floor, use the only thing in the document with dated, published structure: the **contract and queue calendar**. §4.1 already commits to event-time calibration, and Gurney's A13 renewal/offtake-expiry calendar is the demand-side twin of it. `λ_base(t)` = the scheduled-entry rate of that calendar under the same accounting as the event list. That satisfies your requirement — every term needs an S-axis or contract condition to fire — without importing an unmeasured stock as a rate.

**2. The header still leaves one class free: demand events.** §4.1 lists three classes — capital, resource, demand. Your formulation makes *capital* terms conditional on an S-event. Nothing conditions the **demand** class, and a demand event ("any shift away from take-or-pay or reservation structures") can raise λ and exit a K2 state with no physical constraint binding at all.

That matters because of how §9 is worded. The falsifier is specifically about *financing*: "falsified if a K2 state is exited without the S0h constraint binding — if AI capex contracts while power, HBM, and interconnect remain freely available." A demand-side exit would not trigger that test as written, so the model could exit K2 through a non-S route, satisfy the interaction term for capital, and never face the criterion. The test would pass nominally while the claim it tests was false.

**Amendment:** the interaction condition belongs on *every* non-S term, not on capital alone — `1[S-condition in preceding window]` multiplying all three classes. Then "never through the K axis" means what it says, and the §9 falsifier becomes reachable, which is the point of the section.
