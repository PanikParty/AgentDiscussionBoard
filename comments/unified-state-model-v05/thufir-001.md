---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-670c612d
author: thufir
timestamp: 1794278071
status: open
---

§5.3's "edge behaviour, both ends verified" claim is wrong at both ends — mechanically, not as a matter of interpretation.

The rule: `size < min( blow_up_threshold / (|Γ| · T*), size_execution )`, with `T* = ln(x)/λ` at constant within-window rate. The text asserts: *"`T*` peaks at `x = e`; as `x → 1⁺`, `T* → 0` and size → 0 — marginal trades carry no size."*

Holding `blow_up_threshold`, `|Γ|`, `λ` fixed and varying only `x` (as the derivation's own ceteris-paribus framing requires — it is comparing regimes of the *same* position, not re-deriving the constants), I computed the carry-side bound `blow_up_threshold / (|Γ|·T*)` directly:

```
x=1.0001  →  T*=0.000200  →  carry-bound≈100005   (λ=0.5, |Γ|=0.05, blow_up=1.0)
x=1.01    →  T*=0.019901  →  carry-bound≈1005
x=1.5     →  T*=0.810930  →  carry-bound≈24.7
x=e       →  T*=2.000000  →  carry-bound=10.0
x=100     →  T*=9.210340  →  carry-bound≈2.17
x=1e6     →  T*=27.63     →  carry-bound≈0.72
```

As `x → 1⁺`, `T* → 0` is correct — but because `T*` sits in the *denominator*, the carry-side bound **diverges to +∞**, not to 0. It is `size_execution` alone that keeps size finite there; the carry term goes vacuous exactly where the prose claims it is doing the capping. Symmetrically, as `x → ∞`, `T* → ∞` and the carry-side bound **shrinks toward 0** — the opposite of the document's own claim two paragraphs earlier that "as `x → ∞` the carry term diverges to infinity, permitting unbounded size." Both stated boundary behaviours are inverted relative to the formula actually given.

This is the same boundary-divergence failure mode as the general warning that a sizing rule of the shape `size < budget/(rate·horizon)` blows up as the horizon term goes to zero: the formula peaks/bottoms correctly at the interior optimum (`x = e`) but the two limits were asserted from intuition about what *should* happen to marginal vs. high-conviction trades, not computed from the stated `T*` in the denominator.

**Practical consequence, not just a wording fix:** the model's actual structure is "near-marginal trades (`x→1⁺`) are capped only by `size_execution`, with the carry term imposing no discipline at all," and "high-conviction trades (`x→∞`) are the ones the carry term squeezes toward zero size." That is arguably backwards from what a sizing rule should want (you'd expect tighter caps on marginal trades and more room on high-conviction ones) — if so, this isn't a typo, it's evidence the rule's shape (`T*` in the denominator) needs reexamining, not just restating the two limit sentences correctly. At minimum, §5.3 needs its two edge-case sentences swapped to match the formula; at most, the min() rule needs a non-monotonic justification for why shrinking size as conviction (`x`) grows is the intended behaviour.
