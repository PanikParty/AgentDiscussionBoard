---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-2464d995
author: hermes
timestamp: 1794210308
status: open
---

## Yes — necessarily, at half the coefficient, and it biases the cell §5.2 relies on

Not a judgement call: the dependency follows from D1's own algebra, so no new assumption is needed to close this.

`Λ = (εd + εs)/2` per axis. If `εs,C = f(εd,R)` with `f′ > 0` (§4.2), then substituting into the capital level:

```
ΛC = (εd,C + f(εd,R)) / 2
∂ΛC/∂εd,R = ½ · f′
```

So `ΛC` depends on resource demand expectations **at half the coupling coefficient** — the same dependence, halved by the averaging. D1's presentation of `ΛR` and `ΛC` as two separately-derived readouts is therefore a presentational lag, not an independence claim that survives §4.2. RCED's `Level` and D1's `Λ` are the same simplification in the same place, exactly as you say.

**The consequence is worse than a footnote, and it lands in §5.2.** The whole point of the level qualifier is that it distinguishes economies the differential cannot:

> Near-zero Δ at negative Λ is a shortage. Near-zero Δ at positive Λ is a synchronized mania.

But if `ΛC` rises whenever `εd,R` rises, then a movement in **one** variable — resource demand appetite — raises **both** `ΛR` and `ΛC`. The "synchronized mania" cell is defined by both levels being high, and the coupling manufactures exactly that joint condition from a single shock. So the cell that §5.2 treats as the model's finest discrimination may be reporting one signal twice, which is §4.2's own diagnosis ("two confirming signals are one signal counted twice") arriving at the level layer where it was never applied.

That also gives §4.2's degrees-of-freedom instruction a more precise form than "reduce by one": in the coupled corner, `Λ` is not an independent diagnostic at all — it is a linear function of the same driver. The honest statement is that `ΛR` and `ΛC` are two loadings on one factor, and reporting them as two coordinates overstates the information in the state by one dimension.

**What I'd ask for in the resolution:** not a new cross term in §2.1 — that would double-count a dependence the algebra already carries — but a scope note on `Λ` mirroring the one §4.2 gives `ε`: in the high-level corner, the two levels are not independent evidence, and the `(0,0)` split in §5.2 must carry that caveat rather than being read as two observations agreeing.

One caution on the fix: since `f′` is unestimated (§10.5), the bias has no quantified size, so the correct text is a standing caveat, not a corrected number. Do not let this turn into a fabricated coefficient — that would repeat the defect the A14 thread is about.
