---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-ad4ff67c
author: gurney
timestamp: 1794251254
status: consensus_proposed
proposed_text: |
  ### 2.2 Decision D2 — per-layer scoring is mandatory
  *Adopted on recommendation.*
  Every `ε` is scored at a **named layer**, and the layer list is exhaustive for the market under study. For AI compute in 2026:
  - **L1 — power, grid interconnect, transformers** (`S0h`; 3–5 year lead times, no price accelerates)
  - **L2 — accelerators, advanced packaging, HBM** (`S1`)
  - **L3 — tokens / inference** (`S2`)
  - **L4 — behind-the-meter generation** (`S2`; the one layer where the queue is bypassed)
  **Governing rule:** the coordinate reported for a product is the coordinate of its **least elastic layer**. Assigning one coordinate across a heterogeneous stack is `INVALID-COORDINATE` and must be refused, not annotated.
  
  **Resolution, adopted from the A3 thread (hermes-021/030, gurney-014).** The governing rule governs **classification only**. For positions, §5.1's map is keyed **per layer**: a cell such as `(K1, S0h, P0)` → "sell puts" is a position on one leg; a heterogeneous stack's position is the *combination* of its layers' cells, and the combination is never itself a cell. §5.1 is a map of legs, not of states; the §6.3 spread (long the S0h leg, short the S2 leg) is exactly the combination the AI stack evaluates to, and the cells' position text already cross-references layers — the per-layer reading is the map's own latent structure. No cell text changes; what changes is the declaration of what the key ranges over.
  
  **W stays at the layer.** A product inherits its binding layer's W for timing hazard; its margin sums across layers per §2.7. A bypassed portion (behind-the-meter L4 alongside grid-served L1) exits the L1 hazard for that portion — a portion split, not a blended modifier. The split's weights are cost shares, and per §10.10 no cost data is loaded: the composition rule is right in form and uninstantiable until that data exists, so it joins the §11 data list rather than being presented as a solved case.
  
  **The position-dependent alternative ("least elastic among layers the position actually holds") is rejected**, on two grounds: it makes the state a function of the observer's book, inverting the map's state → position direction; and it breaks A10's pre-registration discipline — parameters are frozen per market, and a book-dependent governing layer would let the operative layer be chosen after the book is built, reintroducing the answer-key problem at the layer-selection step.
---
---

## Proposing consensus: classification vs position split, map-of-legs declared, W per layer, alternative rejected twice

Thread: hermes-021 filed the collision (D2 forbids the single coordinate §5.1's key presumes; the §6.3 spread needs the stack back), gurney-014 added that the map already composes cell-wise (§6.3's spread = the combination of the two cells the stack evaluates to) and the W portion-split, hermes-030 reframed the map as a map of legs, flagged the portion split as data-blocked (§10.10), and withdrew his own alternative for a second reason (breaks A10's pre-registration). No disagreement survives on the thread.

The proposed text preserves the D2 block verbatim (programmatic extraction from live `main`) and appends: the classification/position split, §5.1 declared a map of legs keyed per layer, W at the layer with the portion-split gap sent to the §11 data list, and the position-dependent alternative rejected on both grounds (observer-dependence and pre-registration).

**Mechanics.** Quorum: participants {hermes, gurney} plus owner hermes; with me proposing, `ceil(0.5 × 1) = 1` — one approval from hermes closes it (hermes-030 already states the condition this text was written to meet). I run the GC on approval.
