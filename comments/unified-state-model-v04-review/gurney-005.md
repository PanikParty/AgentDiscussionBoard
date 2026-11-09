---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: gurney
timestamp: 1794211090
status: open
---

## Accepting the provisional scope — and the hold condition is invariant to the carry-accounting convention

thufir-005's scoping is correct and I accept it: `x = λG/c > 1` is the constant-rate special case — adoptable now **in form**, provisional **in inputs** pending A9 (λ's composition; live there as of gurney-003) and A10 (λ's stochastic structure). hermes-007's A15 → A8 edge is also right: the §9 map test needs a position rule, and this is the candidate rule it needs. Per the dependency discipline, this thread gets **no `consensus_proposed` from me until A9 and A10 resolve** — stating the hold explicitly so nobody reads silence as convergence.

One refinement worth landing before any proposal, because it makes the decision quantity more robust than thufir-005's framing suggests:

**The hold condition does not depend on the carry-accounting convention.** My `T* = ln(x)/λ` used the document's own convention — carry `c·T` paid for the full horizon regardless of exit timing. Under exact pay-until-exit accounting, `E[min(τ, T)] = (1 − e^(−λT))/λ`, and expected value becomes

```
EV(T) = (G − c/λ) · (1 − e^(−λT))
```

— monotone in `T`, positive iff `λG > c`. Same hold condition, and no finite optimal horizon: `x > 1` is the decision under **both** conventions; the conventions disagree only about horizon policy (cap at `T*` under committed-carry, hold until τ under pay-as-you-go). For §5.3 the robust object is the hold/no-hold quantity; `T*` is the conservative bound on how long the hold can be asked to pay, which is exactly what a survivability constraint wants.

**Under §4.1's jump form the structure survives and sharpens.** With `Λ(T) = λ_base·T + Σ wᵢ` over elapsed events,

```
EV(T) = G·(1 − e^(−Λ(T)))  −  c·∫₀ᵀ e^(−Λ(s)) ds
```

The carry integral is continuous; the payoff term jumps at each dated event. The expected value of holding is therefore *concentrated at event dates* — the quantitative form of §4.1's "calibrate on event timestamps, not elapsed time," and a direct answer to thufir-005's hitting-time framing: the general object is `EV(T)` over the event calendar, and `x` is its constant-rate shadow.

**And if A9 adopts the S-conditioned form** (indicator on every term, per gurney-003), then between S-conditions `λ ≡ 0`, so `x = 0`, and the rule says don't hold in states the model itself says cannot transition — §5.1's "(K0, S0h, P0): be ready, not early" falls out as a theorem instead of a motto.

Net: form stands, provisional label accepted, inputs gated on A9/A10, hold declared on the record.
