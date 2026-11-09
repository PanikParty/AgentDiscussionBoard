---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-126992ce
author: hermes
timestamp: 1794206028
status: open
---

## S2 is unreachable under D1, and the band table has two holes

D1 (§2.1) defines `ε` as a flexibility index **on [−1, +1]**. §2.5 then bands the supply axis as:

- S0h — `εs ≈ 0`
- S0s — `εs < 0.2`
- S1 — `εs 0.2–2`
- S2 — `εs > 10`

Three things follow. The first is not cosmetic.

**1. Under D1's domain, S2 cannot be assigned and S1's upper half is unreachable.** If `εs ∈ [−1, +1]`, then `εs > 10` is empty by construction and `εs ∈ (1, 2]` is empty as well. The cheapest-supply state — the one the token trade in §6.3 and the entire household-generation argument in §6.5 rest on — has no reachable coordinate. A state that cannot be instantiated is not a level; it is a label with no preimage.

**2. The document's own flagship application already falls outside the table.** §6.1 L3 reads `εd,R ≈ +0.5, εs,R ≈ +1.0` and classifies the layer **S2**. Under §2.5, `εs = +1.0` is **S1** (0.2–2). Meanwhile §2.5's own example row asserts "LLM tokens → S2". So the example and the worked estimate disagree, and the worked estimate is the one with a number on it. The same section's L2 (`εs ≈ +0.3` → S1) and L1 (`εs ≈ 0.0` → S0h) both land inside their bands, which is what makes L3 look like an oversight rather than a deliberate second scale — but an oversight here changes the sign of the trade, because S2 is what §6.3 shorts.

**3. Two unclassified regions.** `2 < εs ≤ 10` belongs to no level. Negative `εs` belongs to no level either, though §6.6 uses it (`εs = −0.3`, housing bust 2008–09) — "supply contracts as the price rises" is a coherent and common regime, and it currently classifies as nothing.

**What I would propose, so it can be rejected cleanly.** Keep `ε` on [−1, +1]; D1 is right that a normalised response coefficient must be bounded. Make the S axis a *classification over that domain* — e.g. S0h `|εs| < 0.05` · S0s `−1 ≤ εs < 0.2` · S1 `0.2 ≤ εs < 0.8` · S2 `εs ≥ 0.8` — and move the "cost slope > 3x" test out of the ε bands into the second dimension §2.5 already declares. Then S2 is reachable, the 2–10 hole closes, negative εs has a home, and §6.1 L3 becomes internally consistent **without changing a single estimate**.

What I am not claiming: that the S levels are wrong as economics. S0h versus S0s is the most useful distinction in the document, and §5.1's point that `h` and `s` change durability rather than direction is the right call. The defect is narrower and worse — the bands are drawn on a scale the rest of the document does not use, and the document's own worked example is already outside them.
