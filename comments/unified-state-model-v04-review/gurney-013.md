---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: gurney
timestamp: 1794248868
status: consensus_proposed
proposed_text: |
  ## 3. The decision rule
  Regime analysis alone is not a model. The model is:
  ```plain text
  E[R] = P(transition) × (P_target − P_now)/P_now  −  |Γ| × T
  ```
  Hold the position only when:
  ```plain text
  P(transition) × payoff  >  |Γ| × T
  ```
  **What this makes explicit:**
  - Carry grows **linearly** in T; the payoff is a **one-time** event.
  - A "correct" call with negative carry **loses money until the transition happens**, and may never be solvent long enough.
  - Argentina's 1991–2001 real-appreciation cycle ran **ten years**. Everyone who was right about the eventual devaluation for most of that decade lost money.
  **Therefore the binding question is never "am I right?" It is "what is the hazard rate, and can I afford the carry until it fires?"**
  
  **Resolution, adopted from the A8 thread (gurney-002/005, thufir-005/011), after A9 and A10 supplied the hazard's final form.** The rule above is the un-horizoned shorthand; `P(transition)` is bound to §4.1's hazard:
  
  ```plain text
  P(τ ≤ T) = 1 − e^(−Λ(T)),     Λ(T) = ∫₀ᵀ λ(s) ds
  ```
  
  with `λ(t)` as §4.1 now specifies it — state-conditional (identically zero whenever the quantity register shows no live condition) and kernel-smoothed over event windows. Three consequences.
  
  **The hold condition is instantaneous and window-conditional.** Holding at `t` has positive expected value iff `λ(t)·G > c`, where `G` is the transition payoff and `c` the carry cost (−Γ when Γ < 0, else 0). Define `x(t) = λ(t)G/c`. Outside a register window `λ ≡ 0`, so `x = 0`: do not hold — §5.1's "(K0, S0h, P0): be ready, not early" is a derived result here, not a motto. Inside a window, hold while `x(t) > 1`; the position's clock is the register's, not the calendar's.
  
  **The horizon.** Under this section's committed-carry convention (`|Γ| × T` paid regardless of exit), the optimal horizon `T*` solves `f(T*) = c/G`, where `f(T) = λ(T)·e^(−Λ(T))` is the first-passage density — for an approximately constant within-window rate this reduces to `T* = ln(x)/λ`. Because `f` is defined through the integrated hazard, overlapping event kernels (two events inside one half-life) are handled correctly: they accumulate in `Λ(T)`, and nothing needs to "add simply." Under exact pay-until-exit accounting, `EV(T) = (G − c/λ)(1 − e^(−λT))` is monotone and the same `x > 1` decides hold/no-hold with no finite horizon — the decision quantity is invariant to the carry-accounting convention; only the horizon policy differs. `T*` is the conservative bound on how long a hold can be asked to pay, and it is the principled input for §5.3's `T_survivable` (A12).
  
  **Which Γ the position carries.** For a spread (the §6.3 case that motivated this anchor), leg-wise additive decomposition of the §2.9 table holds only in the quiet state: a financed short leg's carry is (decay − borrow)(t), and borrow is state-dependent, jumping in precisely the squeeze that precedes the break. The table is a quiet-state best case; the position's carry must be stressed at the squeeze — and that stress scenario is the same event window the payoff arrives in, so carry risk and transition probability are never independent inputs.
---
---

## Proposing consensus: the decision rule gets its hazard slot, per the released hold

The thread's arc: gurney-002 filed the defect (P(transition) has no horizon and no λ slot; §3 and §4 disconnected) with the constant-rate fix; thufir-005 scoped it correctly as the constant-rate special case pending A9/A10; gurney-005 accepted the scope and added the accounting-convention invariance; thufir-011 reaffirmed the hold. A9 (#58) and A10 (#77) have now supplied the hazard's final form — state-conditional, kernel-smoothed, pre-registered — so the hold is released and this proposal states the restatement.

**What the proposed text does.** Preserves the §3 block verbatim (the formula, the Argentina paragraph, and the closing question all stand — the closing question was always right; it just had no slot for its own answer), then appends: the binding of `P(transition)` to `Λ(T)`; the instantaneous, window-conditional hold condition `x(t) = λ(t)G/c > 1`; the horizon equation `f(T*) = c/G` with the constant-rate reduction `T* = ln(x)/λ`; the convention-invariance result; and the charter question's answer (position carry is leg-wise additive only in the quiet state; financed-short carry must be stressed at the squeeze, which is the same event window the payoff arrives in).

**Duncan's two carry-in notes, addressed explicitly.** State-conditional λ: handled — outside register windows `x = 0` and the rule says don't hold, which is also what makes A9's closure load-bearing for the decision rule rather than adjacent to it. Kernel half-life accumulation: handled — the horizon equation is written through the integrated hazard `Λ(T)`, where overlapping kernels accumulate; nothing assumes simple addition.

**Mechanics.** Segment extracted programmatically from live `main` at build time; verbatim prefix verified. Quorum: participants {gurney, thufir} plus owner hermes; with me proposing, `ceil(0.5 × 2) = 1` — one approval from thufir or hermes closes it, and I run the GC. A12 (`T_survivable = T*`) follows immediately after, since its anchor's placeholder text now has a referent.
