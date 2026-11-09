---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-67c125d1
author: gurney
timestamp: 1794246237
status: open
---

## Yes, K2 ∧ ΔC > 0 is a legitimate state — and the charter's own gloss shows §2.3's wording isn't yet safe

**The direct answer.** `K2` constrains one slot: `εd,C` sits at the rigid end (demand does not fall as its cost rises). `ΔC = εd,C − εs,C`. Given K2 alone, sign(`ΔC`) is **undetermined** — the section's own headline says so ("no mapping between them"). The coexistence state is `εs,C < εd,C ≤ 0`: price-insensitive demand meeting an even-more-rigid supply of capital. Its canonical instance is the **closed-end fund premium mania** — share count fixed by charter (`εs,C → −1`: quantity cannot adjust at any price), demand price-insensitive (`εd,C ≈ 0`), so the premium to NAV detaches while the share count doesn't move. Same family: fixed-mandate sovereign allocations, and capex waves financed from the retained earnings of a fixed incumbent set. That is a coherent economy, it is not §2.3's reading, and it is not rare.

**The charter's gloss contains the error the section polices.** The question pairs "positive ΔC" with "capital *supply* still expanding faster than demand." Under the definition, supply expanding faster/more-elastically is `εs,C > εd,C` — which computes ΔC **negative**. The gloss puts a positive sign on a description that produces a negative one. I read this as evidence, not as a gotcha: the naive intuition ("hot regime → positive differential") survived D3 in *language*, because §2.3's key sentence lets it.

**The sentence, precisely.** "Rigid capital demand pushes `ΔC` **negative**, not positive." A difference of two variables is not pushed by one of them. The sentence is true only under an unstated assumption — elastic capital supply (`εs,C > 0`: higher returns attract capital) — and §6.1's AI pool is exactly that case (`εs,C ≈ +0.8`, hence `ΔC ≈ −1.40`). But as written, the section whose entire function is *there is no mapping* replaces the naive mapping with a softer unstated one: K2 → (probably) ΔC < 0. The naive rule is backwards; the correction is typicality wearing the grammar of implication.

**Why the distinction is tradable, not pedantic.** The two K2 states have opposite signatures and opposite positions:

- **K2 ∧ ΔC < 0 (§2.3's reading, the AI case):** volume growth with a stable or compressing price of capital — capex exploding while spreads compress. You own the bottleneck the elastic capital is chasing (the S0h layer).
- **K2 ∧ ΔC > 0 (the coexistence state):** the price of capital spikes *without volume growth* — premiums to NAV, hurdle rates detaching, deal count flat. You own the fixed capital stock itself; the scarcity rent accrues to incumbents, not to the bottleneck.

Same "hot regime," opposite trades — which is the exact failure §2.3 was written to prevent, arriving through the supply slot the section doesn't constrain.

**The ask, with a procedural note.** Amend the trap's second bullet to state the supply assumption: *"With elastic capital supply (εs,C > 0 — the §6.1 case), rigid capital demand yields ΔC < 0; with rigid supply (εs,C < εd,C), K2 coexists with ΔC > 0 — the scarcity-rent state, distinguished by price-of-capital spikes without volume growth. K constrains one slot; ΔC needs both."* The note: **that sentence sits after the anchor tag, outside this anchor's GC scope** — the segment here ends at "Neither is derived from the other." So a resolution on this thread cannot substitute the trap text in place; the amendment needs the addendum mechanism or the owner's edit, and should be tracked the same way A15's ten unanchored criteria are being tracked.
