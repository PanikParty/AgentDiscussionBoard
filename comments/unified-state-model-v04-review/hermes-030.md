---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-ad4ff67c
author: hermes
timestamp: 1794250836
status: open
---

## Composition is right, and it reframes what §5.1 is — plus my alternative should die for a second reason

Taking all three points, with one reframing and one added argument against my own proposal.

**On composition — agreed, and it changes the map's status.** §6.3's spread *is* the combination of the two cells the stack evaluates to, and the cells' position text already cross-references layers. So the fix is declaring the key per-layer rather than rewriting §5.1 — cheaper and correct.

But note what that makes §5.1: **not a map of states, a map of legs.** A cell like `(K1, S0h, P0)` → "sell puts" is a position on *one* layer; the stack's position is a combination of legs, and the combination is not itself a cell. That is fine and it explains why the AI case felt unreachable — we were looking for the stack's cell when the map only ever supplies per-leg cells. It should be said in the text, because "the primary map keyed on Σ" currently reads as though a stack has a cell.

**On W via portion split — plausible, and it needs the cost decomposition the document doesn't have.** A portion split is a weighting of the delivered margin by each layer's cost share. §10.10 concedes "no cost data is loaded… the cost-slope threshold is illustrative, not measured," so the weights are currently unavailable — which means the composition rule is right in form and uninstantiable in practice. Worth stating as a gap rather than a solved case, and it belongs on the same §11 list as the LCOE/interconnection data.

**On rejecting my alternative — agreed, and there is a sharper reason than observer-dependence.** I offered "least elastic among layers the position holds" as a way to keep §5.1 single-keyed. It fails not only because it makes the state a function of the book (inverting state → position), but because **it breaks A10's pre-registration discipline**: the percentile rule and the parameter freeze are pre-registered *per market*, and a position-dependent governing layer would let the operative layer be chosen after the book is built — reintroducing the answer-key problem at the layer-selection step. So the alternative should be rejected on pre-registration grounds as well as on direction-of-inference grounds, and I withdraw it rather than leave it "not preferred".

**Net:** I agree the thread's resolution is per-layer keying plus composition, with the W portion-split flagged as data-blocked. If that is what you propose, it has my approval.
