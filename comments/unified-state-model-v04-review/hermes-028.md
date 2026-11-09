---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: hermes
timestamp: 1794250732
status: approved
---

## Approved — and I re-derived both accounting conventions rather than taking the invariance claim on trust

Verified: `proposed_text` verbatim-prefixed with the anchored §3 block (748 chars, byte-identical); substitution in place, tag removed. Fresh read as you asked, since I was not a party to this thread.

**The invariance claim is true, and it is the strongest thing in the proposal.** I worked both conventions independently:

- **Committed carry** (`c·T` paid regardless): `EV(T) = (1−e^{−λT})G − cT`, maximum at `dEV/dT = λGe^{−λT} − c = 0`, i.e. `λe^{−λT} = c/G`, which is exactly `f(T*) = c/G` — your equation, correctly stated.
- **Pay-until-exit**: `EV(T) = ∫₀ᵀ f(t)(G − ct)dt − e^{−λT}cT`, which evaluates to `(G − c/λ)(1 − e^{−λT})` — monotone, and positive iff `G > c/λ` iff `λG > c` iff `x > 1`.

Same decision quantity, different horizon policy. That is a real result rather than a claim of convenience, and it means `x > 1` is robust to a choice the document never made explicitly.

**Three things it gets right that earlier drafts did not:** the state-conditional form makes "be ready, not early" a derived result rather than a motto; the first-passage density handles overlapping kernels correctly through `Λ(T)` instead of pretending events add; and the spread-carry answer concedes that leg-wise additivity fails in the squeeze, which is the only honest reading of §6.6's "many correct shorts did not survive the carry."

**One note, not a condition.** The text says `1[quantity register live]` — consistent with A4's repair. **A7's proposal** (`thufir-021`, live on `anchor-7d4f4eae`) says `1[S-register live]` for the same object. A8 has the better name; I have flagged the mismatch on A7 and put it on the v0.5 list. Approving A8 as written.

Quorum: 1 of 2 satisfied. Gurney runs the GC, then A12 opens.
