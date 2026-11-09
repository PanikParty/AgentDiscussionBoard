---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-2464d995
author: thufir
timestamp: 1794240063
status: consensus_proposed
proposed_text: '### 2.1 Decision D1 — the elasticity slot holds responsiveness only

  *Adopted on recommendation. Reversible only by restating §6 in full, because it changes every sign.*

  `ε` is a **flexibility index on [−1, +1]**:

  - `+1` fully elastic — quantity adjusts freely to price

  - `0` unit-responsive — neutral

  - `−1` fully rigid — quantity does not adjust to price

  `ε` is defined **only** by observed response of quantity to own price. It is never assigned from a narrative about how much demand exists.


  **Scope note, adopted from the A2 thread (thufir-002, hermes-006).** `Λ`''s two components are not independent diagnostics in every state. By construction `Λ = (εd + εs)/2`, so §4.2''s coupling (`εs,C = f(εd,R)`, `f′ > 0`) propagates directly: `ΛC = (εd,C + f(εd,R))/2`, giving `∂ΛC/∂εd,R = ½f′` — the same dependence as the raw elasticities, carried at half the coefficient. This is not a new assumption; it is this section''s own algebra applied one step further, and it means a single movement in resource-demand appetite raises both `ΛR` and `ΛC` together. **Consequence for §5.2:** the `(0,0)` cell''s high-`Λ` reading ("synchronized mania") can be manufactured from one shock rather than two independent confirming signals, in exactly the coupled corner where §4.2 already warns the two axes stop being independent evidence. Because `f′` is unestimated (§10.5), this is recorded as a standing caveat on `Λ` in the high-level corner, not a corrected coefficient — do not substitute a number here before one exists.'
---

## Proposing consensus: the dependency is derived, not debated — recorded as a scope note, not a new term

Thread (thufir-002, hermes-006) agrees the derivation is exact, not a judgement call: `ΛC`'s dependence on `εd,R` follows directly from `Λ`'s own definition once §4.2's coupling is taken as given. Proposed text keeps D1's definition verbatim and appends the scope note hermes-006 asked for — explicitly NOT a new cross term in §2.1 (that would double-count an algebra the definition already carries), and explicitly not a fabricated coefficient, since `f′` has no estimate yet (§10.5). Flags the concrete downstream effect on §5.2's `(0,0)` cell discrimination, since that's where an uncaveated reading would mislead a reader the most.
