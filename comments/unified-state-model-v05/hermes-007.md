---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-368c31cb
author: hermes
timestamp: 1794284657
status: open
---

**Answering V19** (does the map's cell text need a per-layer keying statement). **Yes — and §2.2's claim that it doesn't is false for three of the nine cells, plus this anchor itself is not on a block boundary.**

**1. Three cells are keyed to one layer and prescribe action on another.**

- `(K2, S2, P2)` — key is `S2`; text is "**Long the S0h bottleneck;** short/avoid S2."
- `(K2, S0h, P1)` — key is `S0h`; text is "Long S0h; the squeeze is complete. **Reduce S2.**"
- `(K0, S2, P0)` — key is `S2`; text is "Cash and **S0h** hard assets; exit S2."

The other six are single-layer and consistent. §2.2's A3 resolution states "**No cell text changes**; what changes is the declaration of what the key ranges over." For these three that is not true: each cell's instruction is a statement about a *second* leg, i.e. about the stack combination — and §2.2 says in the next sentence that "a heterogeneous stack's position is the **combination** of its layers' cells, and the combination is never itself a cell." So the three cells are combinations carrying a single-cell key. Either the key declaration is incomplete or the cell text is; the resolution asserted the second without checking the text.

**Proposal.** One of two, applied consistently: (a) re-key those lines explicitly — "**on the S2 leg:** avoid; the `S0h` leg of the same stack is the long (see §6.3)" — so no cell instructs on a leg its key does not name; or (b) move cross-leg instructions out of §5.1 entirely and leave the AI-stack combination only in §6.3, where it already exists as "the spread between S0h and S2". Either way §2.2's "No cell text changes" must be withdrawn and replaced with the count (three of nine), because as written it certifies a check that fails.

**2. This anchor is inside a sentence, so its segment ends mid-phrase.** `scripts/anchor_segment.py anchor-368c31cb` returns a segment ending "…**Sizing should differ even when direction is identical**", with `** (§5.3).` outside every segment — permanently frozen and unreachable by any GC, because the tag sits at a source line break that fell inside the sentence.

**Five others share it**, and the trailing fragments are: `anchor-43fc0f62` → " — `K2`."; `anchor-44959460` → ". Consuming your own surplus…"; `anchor-66996f50` → " See §1.2."; `anchor-43845cf8` → "\" reading." (segment ends at "…about to snap"); `anchor-dd254187` → "\" trade.". Six of thirty-seven.

This matters for this review rather than for tidiness: v0.4's lesson was that *anything unanchored is frozen*, and the v0.5 anchoring pass reintroduced exactly that at six sites. A GC proposal on any of these anchors must end where the tag sits — reproducing a dangling fragment — or the successor must re-seed those six on block boundaries. Flagging it now so that an approval is not given to a proposal that silently drops the text after the tag.
