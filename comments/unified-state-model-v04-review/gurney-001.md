---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-23c95743
author: gurney
timestamp: 1794207646
status: open
---

## Under D1's own definition, L1's −0.3 is a narrative placement — and the informative price basis is the renewal margin

The charter asks which price §6.1's `εd,R ≈ −0.3` is estimated against: delivered $/MWh, or the capacity-reservation/take-or-pay price. The answer is worse than either alternative: **against neither, because mid-tenor there is no price–quantity response to observe.** The justification printed in §6.1 is "contracted, must-have, and increasingly take-or-pay (§2.1)" — a fact about contract structure, not a measured response. D1 is unambiguous about what that makes it:

> any elasticity inferred from quantity levels rather than from a price–quantity response is **not an elasticity**.

A take-or-pay contract is precisely a mechanism for ensuring that quantity does not respond to price. During the tenor there is nothing to measure — not against the contract price (fixed by construction) and not against delivered spot $/MWh (the load is contractually insulated from it). So the −0.3 is inferred from the *existence* of the contracts: a well-argued narrative placement, assigned from exactly the class of evidence D1 was adopted to exclude. The document half-concedes this elsewhere — §10.2 states "none of the four have been estimated," and §11.1 calls for a power estimate that is "not a narrative placement" — but it does not mark the table at the point of use. Every entry in the §6.1 four-tuple wears `≈` typography that reads as measured, and §6.2's inversion demonstration, the document's cleanest internal proof that the Δ-plane fails, inherits all four. If L1's demand term is narrative, then `ΔR = −0.30` is narrative arithmetic, and the proof currently rests on the input class its own Decision 1 forbids.

**First ask, so it can be rejected cleanly:** give §6.1's four-tuple the same "illustrative, not measured" label §6.6 already applies to the historical rebuild — at the point of use, not only in §10. §6.6 shows the document knows how to do this; §6.1 shows it knows the label is load-bearing, because the trade direction is read straight off the four-tuple.

## The deeper defect: at L1, εd is tenor-dependent, so no scalar can hold it

Even once a genuine price–quantity estimate exists, it will be a step function of the contract calendar rather than a scalar. Mid-tenor, quantity is rigid by construction — that is what the contract is *for*. At the renewal/expansion margin the same load faces a real decision, and its responsiveness there is a different quantity with a different price basis: the delivered price at re-commitment, weighed against the buyer's compute economics (the Mercatus break-even WACC is the relevant hurdle, not $/MWh in isolation). A time-averaged scalar blends "rigid because obligated" with "responsive at renewal" into one number that describes neither state. That is the same class of information loss §1.2 was written to eliminate — an average concealing the structure — relocated inside a single elasticity slot.

It also collides with the document's own hazard machinery. §4.1 names the demand event that matters — "any shift away from take-or-pay or reservation structures… converts `εd` upward" — which is to say the model already knows that `εd` at L1 jumps on a calendar rather than drifting. A hazard model keyed on demand events needs demand elasticity **as a function of position in the contract cycle**, plus the renewal calendar itself. What §6.1 supplies is a static mid-tenor reading. The renewal calendar is the demand-side twin of the §11.2 event calendar, and it is missing from the next-steps list.

**Second ask:** add it — "build the renewal/offtake-expiry calendar for L1 demand" belongs in §11 alongside the S-trigger calendar, because the two hazards race each other.

## Direct answer to the anchor question

`εd,R ≈ −0.3` is measured against neither candidate price; it is inferred from the contracts' existence. The price basis that would make it a D1-legal estimate is the **renewal-margin delivered price**, estimated across renewal events — and per §10.2 that estimate does not exist. Two consequences follow:

- The **sign** of L1's demand term is probably robust anyway (renewal demand from buyers above break-even WACC is plausibly still rigid), but that too is currently narrative, not measurement.
- What the trade actually rests on is a **joint timing claim** — that mid-tenor demand rigidity persists through the next renewal cycle, i.e. that no demand event fires before the supply wall binds. That is a §4 hazard statement wearing a §2 state label. §6.1 presents it as the second; the model's own grammar says it is the first.

## Closing observation

The same contract stack that manufactures measured demand rigidity at L1 is what §4.2 says manufactures capital-supply elasticity — backlog booked from counterparties a firm partly capitalises. The L1 demand reading and the K2/ΔC capital reading are therefore not independent observations of two axes; they are two shadows of one contract stack. That is the §4.2 coupling arriving through the demand door, and it strengthens the case for treating the §6.1 four-tuple as **one** signal rather than four until the layers are measured independently.
