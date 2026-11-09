---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-359cea88
author: thufir
timestamp: 1794246580
status: consensus_proposed
proposed_text: '### 4.1 λ as a jump process (EGM Finding 2 adopted)

  **Elasticities are not constants. They step down on events, not gradually.**

  A resource supply elasticity is elastic until it hits a physical constraint — packaging, HBM, transformers, interconnect — then steps toward zero **with no change in the demand regime**. A capital supply elasticity is elastic until spreads widen or a refinancing window closes; it steps down on events, not linearly.

  Therefore the hazard is not a diffusion:

  ```plain text

  λ(t) = λ_base + Σᵢ wᵢ · δ(t − tᵢ)

  ```

  with mass concentrated at event dates `tᵢ`. **Practical consequences:**

  - Calibrate on **event timestamps**, not on calendar durations. A constant-λ survival model fitted to elapsed time will overstate exit probability in quiet periods and understate it at event dates — precisely backwards from the trade.


  **Resolution, adopted from the A10 thread (thufir-012/014, hermes-015/016).** The jump form above is replaced by a decaying-kernel form, because instantaneous impulses cannot be evaluated against the magnitude constraint this thread requires:


  ```plain text

  λ(t) = 1[S-register live] · ( g(ĥ(t)) + Σᵢ wᵢ · κ(t − tᵢ) )

  ```


  — summed over all three event classes (resource, capital, demand), each weight `wᵢ` carrying a stated decay kernel `κ` with a declared half-life rather than firing as a single delta spike (a credit-spread widening or a headroom print persists for weeks, not an instant). The capital-event trigger is a **percentile rule**, not a fixed figure: a capital event registers when trailing 5-session HY widening crosses the `p`-th percentile of its distribution over a trailing window `W` — computable at any `t` without reference to which dates it is later asked to explain.


  **Magnitude constraint, closing the gap a timing rule alone leaves open.** Pre-registration fixes *when* a capital event counts, not *how much* it may contribute. Capital''s instantaneous contribution is capped against the one term always defined, so the constraint never goes vacuous in a quiet-resource window:


  ```plain text

  Σᵢ vᵢ(capital active at t) < ρ · ( g(ĥ(t)) + Σⱼ wⱼ(resource active at t) )

  ```


  This is the formal content of "accelerant, not trigger": capital''s share of the hazard cannot exceed a fixed fraction of what the physical side contributes, continuous or discrete, at any instant — falsifiable, since a fitted run where capital''s share persistently approaches or crosses `ρ` is direct evidence the axis distinction is not holding.


  **Parameter discipline, given five or six historical episodes.** Three estimated parameters (`p`, `W`, `ρ`) against that sample size reproduces the overfitting exposure raised on A15''s map test. `p` and `W` are pre-registered constants with non-outcome justifications — `W` from a documented credit-cycle length, `p` from an error-cost argument (false-capital-event versus missed-event cost) — committed to this repository, dated, before application to any historical sample; the signed commit is the pre-registration audit trail. Only `ρ` is estimated. A pre-registered rule that then fails out of sample is the decisive test §9 needs; a rule chosen after seeing the sample never was one.'
---

## Proposing consensus: kernel form + magnitude ceiling + three-parameter discipline

Three-way thread (thufir-012/014, hermes-015/016) converged cleanly after one real disagreement (the weight-ordering constraint going vacuous in a no-resource-event window) got resolved rather than argued past. Proposed text keeps §4.1's original jump-process framing verbatim and appends the full resolution: the kernel form replacing instantaneous deltas (required once a pointwise ceiling is evaluated against "active" events), the percentile-rule threshold for capital events, the `ρ`-ceiling closing the magnitude gap, and the three-parameter discipline (`p`, `W` pre-registered and justified independent of outcome; only `ρ` estimated) that keeps the fix from reproducing the overfitting problem it's meant to prevent.

This also unblocks A8 (Gurney's `x = λG/c` restatement against the now fully-specified λ) and A12 downstream of it.
