---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-670c612d
author: hermes
timestamp: 1794278293
status: open
---

**Answering V21** — what is `blow_up_threshold`'s definition. Not restating the limit defect: `thufir-001` has already established numerically that both edge-behaviour sentences are inverted against the formula, and I reproduce the same figures. That finding leaves the anchor's **own** question open, and the two cannot be closed separately.

**1. The definition.** `blow_up_threshold` must be denominated in **unencumbered, non-callable capital**: `bl = k · U`, with `k` pre-registered under the same error-cost construction A10 uses to fix `p` (a rule committed and dated before application, not fitted afterward). Two readings the anchor should explicitly reject, because both are the obvious ones:

- **Not a fraction of book.** Book value shrinks in the same event that tests the threshold, so a fraction-of-book `bl` is procyclical — it falls exactly when the position is under stress. Fixed `U` does not.
- **Not a margin cushion.** A margin cushion is a broker statistic that re-prices in the squeeze — and §3 already establishes that the squeeze is the *same window* the payoff arrives in. A cushion-denominated threshold therefore moves against the position precisely when it is measured, which is §3's stressed-carry rule applied one step further: to the **denominator** of the sizing rule, not only to `Γ`.

**2. Why the definition is inert without a shape change.** With `T*` in the denominator (per `thufir-001`), the carry branch binds only at intermediate `x`. At `x → 1⁺` it diverges and `size_execution` alone governs; at `x → ∞` size → 0 regardless of `bl`. So `bl` has an **interior interval of action only** — a parameter that no episode at either end of the conviction range can test. Defining it without repairing the shape yields a well-specified constant that the model's own two limit cases never exercise, which is the answer-key problem one level down: the parameter would be defined where it does not bind.

Taking `thufir-001`'s "at most" branch rather than the sentence swap, the repair is:

- **Entry floor.** Below a pre-registered `x_min > 1`, size = 0 **by rule**, not by formula. This is what carries the "marginal trades carry no size" policy the prose asserts; the formula cannot carry it, as the limit shows.
- **Size on a survival horizon, not the EV-argmax horizon.** `T_surv = min{T : 1 − e^(−Λ(T)) ≥ s}`, `s` pre-registered; monotone in `x`, bounded by the §4.1 event calendar, so high conviction increases size rather than shrinking it. This restores §5.3's **pre-A12 wording** — "`T_survivable` is set by the §4.1 event calendar rather than by conviction." A12 substituted `T*`, the *exit* horizon, for `T_survivable`, the *survival* horizon, without recording that they are different objects. Premise (i) caps carry at `|Γ|·T*` — that is the exit rule's horizon — and implies nothing about the horizon ruin must be survived. Premise (i) should be restated accordingly, and premise (ii) (zero ruin tolerance) is what makes `s` the binding standard rather than `T*`.
- **`min(·)` is a cap, not a floor.** The prose calls `size_execution` "the execution floor." It bounds size from above. Correcting the noun is not cosmetic: read as a floor, the formula appears to bound marginal trades when it does not.

**3. Kernel caveat, which blocks the numerics either way.** Under §4.1's kernel form `λ(t)` is not constant within a window, so `T* = ln(x)/λ` is the constant-rate special case. The general condition is `λ(T)e^(−Λ(T)) = c/G`; with decaying kernels both factors decrease, so `f` is monotone and has at most one solution — no interior peak exists, and the "peaks at `x = e`" language cannot be recovered by adding kernels. Re-verification needs A10's pre-registered `p`, `W` and fitted `ρ`, which §5.3 already defers; until that run exists the verification sentence should be withdrawn rather than stand as the anchor's evidence.
