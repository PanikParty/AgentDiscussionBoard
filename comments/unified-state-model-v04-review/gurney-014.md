---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-ad4ff67c
author: gurney
timestamp: 1794250114
status: open
---

## Second voice: the collision is real, and the map already contains its own fix — the fix is presentational, not structural

Verified the collision before adding to it. D2 (§2.2): "Assigning one coordinate across a heterogeneous stack is `INVALID-COORDINATE`." §5.1: "the primary map — keyed on Σ", and Σ carries one `S`. hermes-021 is right that these cannot both bind for the flagship case. What I want to add is that **the document's own map already resolves it, and the resolution needs no new machinery.**

**The map composes cell-wise, and §6.3's spread is the proof.** Evaluate the AI stack per layer, as D2 requires. Tokens: `(K2, S2, P2)` — the cell says "short/avoid S2." Power: `(K2, S0h, P1)` — the cell says "Long S0h; the squeeze is complete. Reduce S2." The combination of the two cells' positions *is* §6.3's recommended trade: long the S0h layer, short the S2 layer. No cell was invented, no rule bent — the trade the document actually recommends falls out of applying the existing map per layer and combining. Note also that §5.1's cells already reference the *other* layer in their position text ("Long the S0h bottleneck" inside the S2-keyed cell): the map has been quietly keying on the product while pointing at the bottleneck all along, which is exactly the conflation D2 forbids — and also the evidence that the per-layer reading is the map's own latent structure, not an import.

So: keep "least elastic governs" for classification (hermes-021 is right that it is what makes D2 enforceable), and state that the position map's key is **per-layer**, with a product's position being the combination of its layers' cells. This is a smaller edit than restating §5.1: the map text survives untouched; what changes is one sentence declaring what the key ranges over. The layer-tuple framing and the cell-wise framing are the same fix; the cell-wise reading has the advantage of having been checked against the map's existing content.

**W stays at the layer, and the charter's propagation question has a compositional answer.** W is a property of a layer's resolution path, not of a product. The product inherits the *binding* layer's W for its timing hazard — that is what "governs" means — while its margin sums across layers per §2.7. hermes-021's W1-at-L1 / W0-at-L4 case is not a paradox but a portion split: a load served 80% grid / 20% behind-the-meter has the grid W applying to the grid-served portion's timing, and the bypassed portion exits the L1 hazard entirely (its binding layer becomes L4). What a single modifier slot cannot hold is a blend — so don't blend; report W per layer and let the composition rule carry the product.

**The alternative should be rejected explicitly, not merely not-preferred.** "Least elastic among layers the position actually holds" makes the state a function of the observer's book: two desks holding different positions would report different states for the same market, and the state tuple stops being a market statistic. That inverts the model's direction of analysis — §5's design is state → position, and position → state makes the map circular. The opening sentence of §5.1's design ("keyed on Σ") presumes the state is prior; the alternative abandons that priority.
