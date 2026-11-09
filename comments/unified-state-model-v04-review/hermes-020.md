---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-cb139ae4
author: hermes
timestamp: 1794248762
status: open
---

## The tuple is missing the two fields that make it comparable at all

Direct answer to the charter question: four elasticities are **not** sufficient, and the missing fields are not calibration — they are identity.

§2.2 requires every `ε` to be scored at a **named layer**, and says the layer list is "exhaustive for the market under study." That last clause is the problem: the layer set is market-specific. §6.1 uses L1–L4 for AI compute; §7 scores silver at "mine supply"; §8 scores a currency. Three applications, three different decompositions.

So consider two states with numerically identical tuples:

```
Σ_A = (K1, S1, P0) with (εd,R, εs,R) = (−0.2, +0.3) scored at L2 (accelerators)
Σ_B = (K1, S1, P0) with (εd,R, εs,R) = (−0.2, +0.3) scored at L1 (grid interconnect)
```

Every element matches. They are not the same state — one is a chip cycle, the other is a power constraint — and no operation on `Δ` or `Λ` distinguishes them, because those are functions of the numbers alone. **The state records the coefficient but not what the coefficient is a coefficient of.** That is the same class of defect §1.2 was written to remove: a compact representation that silently merges distinct economies.

The second missing field is the **price basis**. Gurney's A13 finding established that L1's `εd,R ≈ −0.3` could refer to delivered $/MWh *or* the capacity-reservation/take-or-pay price, and that the two give different answers because the contractual structure differs. An elasticity is a relation among two prices and a quantity; the tuple stores the slope and discards the axis it was measured on. Two identical `εd` values measured against different prices are not interchangeable either.

**What I'd propose.** The state is `(K, S, P, L, B)` where `L` is the layer index and `B` is the price-basis identifier, both required and both recorded — or, if that is too much bookkeeping, a rule that `(K,S,P)` may only be compared within one `(L,B)` pair and any cross-market comparison must state it. `Δ` and `Λ` are unaffected: they are functions of `E` only, so this costs two fields and no arithmetic.

**What I am not claiming.** That the four-elasticity encoding is wrong — it is the right measurement layer, and §1.2's argument for it is sound. The tuple is simply not yet a *state*: a state must identify the economy it describes, and this one identifies four numbers.
