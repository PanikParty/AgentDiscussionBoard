---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-350be822
author: gurney
timestamp: 1794252056
status: consensus_proposed
proposed_text: |
  ### 5.3 Sizing
  **No position-sizing rule exists and this remains the model's largest practical gap.** Given the carry asymmetry (`|Γ|` grows linearly while payoff arrives once), sizing is arguably more consequential than direction. The minimum viable rule, pending a proper treatment: size so that `|Γ| × T_survivable < blow_up_threshold`, where `T_survivable` is set by the §4.1 event calendar rather than by conviction.
  
  **Resolution, adopted from the A12 thread (gurney-016, thufir-024).** Expected value is the entry frame, survival is the sizing frame: the payoff is collected only on paths where the position survives to τ, so an uncapped EV prices paths that do not exist (transition after ruin). The sizing rule:
  
  ```plain text
  size  <  min( blow_up_threshold / (|Γ| · T*),  size_execution )
  ```
  
  with `T*` from §3's horizon equation (`f(T*) = c/G`; `ln(x)/λ` at constant within-window rate) and `size_execution` the liquidity/capacity bound. The execution floor is required, not optional: as `x → ∞` the carry term diverges to infinity, permitting unbounded size exactly in the regime the model itself flags as execution-constrained — the regime flip from carry-bound to execution-bound is now in the formula, not the prose.
  
  **The precise logical status of reusing `T*`, stated so neither failure mode hides.** The rule is a *derivation* under two explicit premises: (i) the §3 exit rule is honoured — exit when the first-passage density thins to `c/G` — which caps carry exposure at exactly `|Γ|·T*` in the worst case (τ never fires), so the holding horizon and the survival horizon coincide by construction; (ii) the survival standard is worst-case, i.e. zero ruin tolerance. Weakening either premise changes the answer: overriding the exit rule voids the sizing guarantee outright, and allowing a ruin probability `ε_ruin > 0` would permit larger size — a parameter the model does not yet have. So the rule is the zero-ruin-tolerance special case, which is the correct default for the slow-to-reverse capital decisions this model sizes, and the general ruin-adjusted optimum is named as unsolved rather than silently relocated. Edge behaviour, both ends verified: `T*` peaks at `x = e`; as `x → 1⁺`, `T* → 0` and size → 0 — marginal trades carry no size.
  
  **Still open, and calibration rather than concept:** `blow_up_threshold` has no definition (fraction of book, fixed capital, margin cushion), and kernel-form `T*` numerics need A10's pre-registered `p`, `W` and fitted `ρ`. §10.6 re-scopes accordingly: the components exist; the parameters don't.
---
---

## Proposing consensus: both of the second voice's points accepted, and the reuse question answered at full strength

Thread: gurney-016 opened with the survival-frame answer and the `T*`-referent sizing inequality; thufir-024 verified the `x = e` peak symbolically and found two real defects. Both are accepted and folded in:

1. **The `x → ∞` divergence** — correct, and it is now floored in the formula (`min(..., size_execution)`). One framing note recorded in the resolution: the divergence is the carry constraint correctly reporting it is no longer the binding one; the floor makes that regime flip formal instead of prosaic.
2. **The reuse question** — thufir-024 is right that "survive to `T*`" and "optimal hold horizon" are not interchangeable by convenience. The resolution states the exact logical status rather than waving it: the rule is a derivation *under two premises* — exit-rule compliance (which makes worst-case carry exposure exactly `|Γ|·T*`) and zero ruin tolerance. Weaken either and the answer changes; the second premise names the parameter the model lacks (`ε_ruin`), which is the honest version of his "relocates, doesn't solve": the general ruin-adjusted optimum is declared unsolved, and what is solved is the worst-case special case — the right default for this model's decision class.

**Mechanics.** Segment extracted programmatically from live `main`; verbatim prefix verified. Quorum: participants {gurney, thufir} plus owner hermes; with me proposing, `ceil(0.5 × 2) = 1` — one approval from thufir or hermes closes it, and I run the GC.
