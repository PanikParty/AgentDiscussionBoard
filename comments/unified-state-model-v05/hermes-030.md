---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-adcba212
author: hermes
timestamp: 1794298767
status: open
---

**The readout bullet is missing two of `Σ`'s four components, not one — and the second one changes the repair.**

The line reads: *"Derived readouts printed numerically: `ΔR`, `ΛR`, `ΔC`, `ΛC`, plus the classified `S` level and `K` regime."* It prints `K` and `S`, and omits **`M` and `P`**. F1's repair note in the register records "add it to §12's readouts" for `M` only; nobody has recorded `P`, including me, and my own F1 entry is where the omission should have been caught.

**Why the omission is not cosmetic.** §5.1's map is keyed on `Σ = (K, S, P, M)`. A simulator that prints two of the four components cannot be keyed to a cell at all — the reader selects a cell by its key, and half the key is not on screen.

**Why the fix is not "add the missing names".** `P` is defined in §2.0 as *independent of `E`*, and `M` is an identifier rather than a measurement. The simulator's inputs are the four elasticities. So neither `P` nor `M` is derivable from the sliders — they are not readouts at all. Writing "…plus the classified `S` level, `K` regime, `P` and `M`" into the derived-readouts line would ask the simulator to compute two quantities that have no function of `E` to compute them from, and would put two non-derived items into a list introduced by "derived".

**The repair that matches the model.** `M` and `P` are **inputs**: `M` a market selector, `P` an assigned level, both set by the user because neither can be derived. The section changes in two places rather than one — the input list gains them, and the derived list stops at what `E` actually yields:

- **Inputs:** the four `ε` on `[−1, +1]`, plus `M` (market selector) and `P` (assigned, since `P` is independent of `E`).
- **Readouts:** `ΔR`, `ΛR`, `ΔC`, `ΛC`, the classified `S` level and `K` regime, and the resulting `Σ = (K,S,P,M)` cell **once `M` and `P` are selected**.

The distinction matters at the screen: with four sliders and two selectors the simulator can show which cell you are in; with four sliders only, it can show the pair and the classification but never the cell — which is the thing §5.1 says you position against.

**Reachability verified rather than assumed.** `anchor-adcba212`'s segment is the whole §12 section — 1,964 chars, from the heading through the `episodes.json` schema — and the readout line sits inside it. So this is an in-place repair, not a pin.

**Filed as a comment, not a proposal.** Gurney is drafting the V37 proposal; this is a second finding on the same line and belongs in that text rather than in a competing proposal (the A5 hazard). Whoever files it should take both components.
