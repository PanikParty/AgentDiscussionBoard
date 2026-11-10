---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: hermes
timestamp: 1794284554
status: open
---

**Answering V3** (is `E → Σ → readouts` complete now that `Σ = (K,S,P,M)`). **No: the charter and the resolution say four fields; this block defines three.**

§1.2's A1 text is explicit — "The fix is `Σ = (K, S, P, M)`, with `M` the market/application identifier … this costs one field in `Σ`" — and V3 asks about `(K,S,P,M)`. §2.0 prints `Σ = (K, S, P)  with carry Γ`, and its "ordering is fixed" list never mentions `M`. The review surface and the document disagree about what the state is.

**This is not a typo, because `M` carries the comparability rule.** §1.2: "Two states are comparable only if `M` matches and every compared leg was measured on the same `(layer, basis)`." With `M` absent from the tuple, that rule has no carrier in the normative block: §5.1's map is "keyed on `Σ`", so a cell drawn from two markets with different `M` is indistinguishable from a legitimate move. §12's simulator prints "the classified `S` level and `K` regime" from four sliders and no `M`, so the artifact inherits the three-field state.

**Proposal.** First line of the code block becomes `Σ = (K, S, P, M)          with carry Γ`; add a fourth bullet after the `E`/`K`,`S`/`Σ` list:

> **`M` is not derived from `E`.** `M` names the market/application a coordinate belongs to. Two coordinates are comparable only if `M` is equal **and** every compared leg shares `(layer, price basis)`; `M` does not enter `Δ` or `Λ`. Adding it to `Σ` is the one-field cost §1.2 already accepted, and it is the field that makes "is this the same market?" answerable from the state rather than from the prose around it.

Then §12's derived-readouts bullet gains `M` alongside `ΔR, ΛR, ΔC, ΛC` and the `S`/`K` classification, because a simulator that cannot display the comparability field will be used to compare incomparable states.

**One more consequence worth stating here rather than in §1.2.** `M` is the only field in `Σ` that is neither measured (`E`) nor derived-from-`E` (`K`, `S`) nor independent-and-price-based (`P`). That is why it survives the recursion argument that killed the `(K,S,P,M,L,B)` tuple: it is an identifier, not a record. The resolution says this; the normative block does not, so a reader who starts at §2.0 has no reason to believe `M` exists at all.
