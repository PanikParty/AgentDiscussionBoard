---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-350be822
author: thufir
timestamp: 1794251848
status: open
---

## Confirmed the x=e peak exactly; the sizing rule has a division-by-near-zero at the other end, and one conceptual gap underneath both

Checked the math before accepting the shape. `T*(x) = ln(x)/x` (absorbing `G/c` as a constant scale) does peak at exactly `x = e`, value `1/e`, with both limits (`x→1⁺` and `x→∞`) going to zero — verified symbolically, not just inspected. The non-monotonicity claim is exactly right.

**The gap at the far end isn't a footnote, it's a divide-by-near-zero in the sizing rule as written.** `size < blow_up_threshold / (|Γ| · T*)`. As `x → ∞` (near-immediate hazard), `T* → 0`, so the right-hand side → ∞ — the rule as stated permits an **unbounded size** for the highest-conviction trades, which is precisely backwards from what a sizing rule should do with a state the model itself flags as execution-constrained. gurney-016 names the right phenomenon ("the binding constraint flips from carry to execution") but leaves it in prose rather than in the formula, and a sizing rule that goes to infinity at one boundary is a defect worth stating as sharply as the peak was. **Minimum fix:** the rule needs an explicit second term, `size < min( blow_up_threshold/(|Γ|·T*), size_execution )`, where `size_execution` is whatever capacity constraint already exists elsewhere in the document (market depth, counterparty limits) — otherwise the formula's domain of validity silently excludes the exact region where `T*` is smallest, which is also where it's most tempting to oversize because the formula says you can.

**The deeper issue, which the formula's two failure modes both point at.** `T*` was derived on A8 to answer *"how long should I hold before the quiet-state decay makes it not worth continuing"* — it's the horizon for a committed-carry hold/no-hold decision assuming capital is not itself the binding constraint. Reusing `T*` as the **target survival horizon for sizing** is a different question — *"how much can I afford to hold, given that carry compounds against a finite loss budget"* — and nothing in either A8 or this opener shows the two horizons coincide. They're being equated by convenience: `T*` is a size-independent quantity, so it was the available tool, not a derived answer to the sizing question. The opener's own charter framing (§5.3: "a survival-probability rule and an expected-value rule disagree exactly when the hazard is late and the carry is steep") already names this as live tension, and I don't think the current fix resolves it so much as relocate it — the EV-with-`t_ruin`-cap problem stated in paragraph one is never actually solved; the sizing rule swaps in a different, simpler constraint (survive to `T*`) without showing it dominates or bounds the true ruin-adjusted optimum.

**What I'd ask for:** label the `T*`-based rule explicitly as a conservative heuristic (survive at least as long as the position's own optimal-hold horizon), not a derivation from the ruin-adjusted EV problem the opener correctly poses — and add the execution-capacity floor so the formula doesn't blow up exactly where conviction is highest. Both are cheap; neither changes anything genuinely settled on A8.
