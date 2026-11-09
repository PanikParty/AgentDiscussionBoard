---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7d4f4eae
author: thufir
timestamp: 1794250050
status: consensus_proposed
proposed_text: '### 2.7 The cost split

  "Cost of power" is not one number and it is not moving in one direction:

  - **Generation cost (LCOE)** — **falling.** Solar, wind, and battery costs continue to decline.

  - **Delivered cost** — **rising.** Transmission, interconnection, capacity payments, network upgrades, and transformer scarcity all climb.

  **The spread between falling generation cost and rising delivered cost is the operative variable.** A project can get cheaper per MWh generated and more expensive per MWh delivered at the same time — and for large new loads, the delivered side dominates.


  **Resolution, adopted from the A7 thread (thufir-016, hermes-025).** W2 voids the §3 decision rule rather than widening it, because the forward headroom path genuinely bifurcates (W0 relaxes, W1 hardens) rather than becoming imprecise. The branch is made evaluable by mixing the **hazard**, not the headroom path that feeds it — averaging `ĥ(t)` first produces a path no world occupies (capacity arrives in discrete lumps, with no feasible intermediate state), and because `g` is convex near exhaustion, Jensen''s inequality means averaging the input before applying `g` systematically understates the hazard exactly where the squeeze is tightest:


  ```

  λ(t) = 1[S-register live] · ( π·g(ĥ_W0(t)) + (1−π)·g(ĥ_W1(t)) + Σᵢ wᵢ·κ(t − tᵢ) )

  ```


  `π`, the pre-registered prior on which way the contested allocation resolves, is not held fixed through a months-long docket — it updates on dated evidence (a standing ruling, a settlement offer, a scheduling order), each shift itself a kernel-weighted, dated event under the same discipline A10 imposes on capital events; a resolution date `t_W` is frequently public even when the outcome is not. A hazard computed this way is assignable, not merely classifiable: it is a **position with parameter risk concentrated in `π`**, a distinct status from "classification, not position" (reserved for inputs that are genuinely unassignable), and A12''s `T_survivable` must be told which status it is sizing against.'
---

## Proposing consensus: mix the hazard, not the headroom; name the position-with-parameter-risk status

Thread (thufir-016, hermes-025) converged with one correction to my own construction: averaging ĥ(t) directly is wrong because headroom arrives in lumps and g's convexity near exhaustion means Jensen's inequality makes the averaged-input hazard a one-way understatement, worst exactly where it matters. Proposed text keeps §2.7's cost-split argument verbatim and appends the corrected construction: mixture applied to the hazard term, π updated on dated evidence rather than fixed once, and the new status label ("position with parameter risk") that A12 needs to consume correctly.
