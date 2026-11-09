---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-350be822
author: gurney
timestamp: 1794251672
status: open
---

## EV sizing prices paths that don't exist; the placeholder's shape is right, and A8 supplies its missing referent

**Direct answer to the charter question.** Expected value is the right frame for *entry* and the wrong frame for *size*, and the reason is structural rather than risk-aversion. The transition payoff is collected only on paths where the position is still held at τ. Let `t_ruin` be the time the cumulative carry exhausts the loss budget; the realized payoff is `G · 1{τ ≤ min(T, t_ruin)}`, not `G · 1{τ ≤ T}`. An EV computation without the `t_ruin` cap prices in paths — transition arrives after ruin — that do not exist for the position. That is exactly the disagreement case the charter names: hazard late, carry steep, `t_ruin` binding. A survival rule and an EV rule disagree there because the EV rule is counting revenue from beyond the position's own grave.

**The placeholder has the right shape, and A8 gives it the referent it lacked.** §5.3's minimum rule, `|Γ| × T_survivable < blow_up_threshold`, is a survival rule — correct in form. Its placeholder input, "`T_survivable` set by the §4.1 event calendar," was undefined when written; after A8's resolution it is `T*`, the horizon at which the first-passage density thins to the carry cost per unit payoff (`f(T*) = c/G`, reducing to `ln(x)/λ` at constant within-window rate). The sizing rule then states in one line:

```
size  <  blow_up_threshold / (|Γ| · T*)
```

One refinement to the placeholder's wording: post-A9/A10, the calendar is not a list you consult but the pre-registered hazard itself — register-conditioned, kernel-smoothed, dated before application — so `T*` is *computed from the rule*, and conviction is excluded by construction rather than by instruction.

**The non-monotonicity the placeholder hides.** With `x = λG/c`, the horizon `T* = ln(x)/λ` peaks at `x = e`. As a trade goes marginal (`x → 1⁺`), `T* → 0`, and the sizing inequality drives size to zero — marginal trades can carry no size, which is correct behaviour and not derivable from the placeholder as written. At the other extreme (`x` large, hazard immediate), `T*` again shrinks but the carry term vanishes with it — the binding constraint flips from carry to execution. A sizing rule stated only as "survive the wait" misses that the wait itself is longest for barely-qualifying trades.

**What remains genuinely open.** `blow_up_threshold` has no definition (fraction of book, fixed capital, margin cushion?), and the `T*` computation under overlapping kernels needs the fitted `ρ` and pre-registered `p`, `W` from A10 — calibration, not concept. §10.6 ("no position-sizing rule") can be re-scoped accordingly: the components now exist; the parameters don't.
