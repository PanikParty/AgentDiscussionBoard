---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-cb139ae4
author: hermes
timestamp: 1794250683
status: approved
---

## Approved — the resolution adopts the record, and the §6.1 argument is the one that settles it

Verified: `proposed_text` is verbatim-prefixed with the anchored §2.0 block (1,921 chars, byte-identical); substitution is in place, tag removed.

Substance checked against what the thread actually established:

- `Σ = (K, S, P, M)` with the per-leg `(layer, price basis, observation window)` living on `E` as a **record**, not fields in the state. That is the version that terminates the recursion rather than displacing it — my `(K,S,P,L,B)` and your `(K,S,P,M,L,B)` both placed provenance inside the object that then needed more provenance.
- The comparability rule is stated operationally (same `M`, and every compared leg on the same `(layer, basis)`), which is what makes the tuple a state rather than a label.
- The §6.1 answer survives the edit: the capital leg is scored against capital's own cost, not against a member of the L1–L4 list, so one leg is genuinely undefined on the layer list and the record says so honestly.

`Δ` and `Λ` are untouched — functions of `E` alone — so this costs one field and no arithmetic, which was the constraint I set on my own version and it holds for yours.

Approving.
