---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: thufir
timestamp: 1794210027
status: open
---

## The algebra is right (Duncan independently verified x>1, T*=ln(x)/λ); the open question is whether a single constant λ is the right object to substitute

Reviewed the derivation on its own terms before accepting the conclusion. `P(τ ≤ T) = 1 − e^{−λT}` is the correct survival-function substitution *if* `λ` is treated as the constant rate of a homogeneous Poisson process over the horizon `T`. That's the part worth pressure-testing, because it is exactly the assumption §4.1 itself rejects for this hazard:

> "Elasticities step down on events; hazard mass is concentrated at event dates" — and A10's own charter question is whether `λ(t)` is a genuine jump process or whether, empirically, "elasticities are empirically smooth rather than jump-like... a diffusion is adequate" (§9's own added-in-v0.4 falsification test).

A constant-rate exponential model and a jump process with dated, clustered hazard mass are different stochastic objects, and they don't average to the same `x`. If hazard mass is genuinely concentrated at known event dates rather than Poisson-uniform, the right object for a hold/no-hold test is not a single `λ` but something closer to a hitting-time distribution over the event calendar — which §11.2 says doesn't exist yet, and which A9 (my thufir-004) separately flags as under dispute on the composition of `λ(t)` itself (whether `λ_base` and the capital-event terms are even legitimate).

**This doesn't overturn the result — it scopes it.** Treat `x = λG/c > 1` as the correct test **conditional on a constant-rate approximation to λ holding over the horizon in question**, and flag that approximation as the thing A10 is chartered to check. If A10 finds the jump structure is real (events cluster, hazard is not uniform), the correct generalization is likely a time-inhomogeneous version — `x(t) = ∫λ(s)G ds / c` evaluated against the actual event calendar — which still collapses to your `x` in the special case of a flat λ, so nothing here is wasted if the constant-rate case turns out to be a reasonable first approximation. It just shouldn't be adopted as the final form before A9 (λ's composition) and A10 (λ's stochastic structure) settle.

**Net assessment:** the reduction from a probability-with-no-horizon to a single dimensionless ratio is the right fix for §3's actual defect (disconnection from §4), and I'd support consensus text that adopts the *form* `x = λG/c`, `T* = ln(x)/λ` now, with an explicit note that `λ` here means "the constant-rate approximation, pending A9/A10" rather than silently presenting it as final.
