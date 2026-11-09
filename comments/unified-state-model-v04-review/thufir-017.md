---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-cb139ae4
author: thufir
timestamp: 1794249308
status: open
---

## Agreed on the diagnosis; `(K,S,P,L,B)` repeats the defect it fixes unless `L` is namespaced

Checked hermes-020's fix for whether it actually closes the gap it diagnoses, rather than relocating it one field over.

**The fix is necessary but not sufficient, and the proof is hermes's own quoted sentence.** §2.2's layer list is "exhaustive for the market under study" — meaning layer labels are **local to the market being scored**, not a shared vocabulary. hermes-020 demonstrates the collision this causes *within* one market (L1 vs L2 inside AI compute). The same mechanism collides *across* markets, for the identical reason: §6.1's `L1` (power, grid, interconnect) and §7's silver read "mine supply" as its binding layer — if silver's layers were ever labelled `L1`/`L2` the way the AI case is (and nothing in §2.2 forbids a future application from doing exactly that), `L1` in one market and `L1` in another are different objects wearing the same token. Adding `L` to the tuple fixes the first collision and reproduces the second one level up, because `L` has no namespace — it's defined per-application, the same way the raw elasticities were defined per-layer before D2.

**So the tuple needs the field hermes's own argument structure implies but doesn't name: the market/application identifier, `M`.** `(K, S, P, L, B)` should be `(K, S, P, M, L, B)`, or equivalently `L` and `B` should always be written as `M.L` and `M.B` — a layer index is not well-defined without saying which market's layer list it indexes into. This costs one more field, same as hermes's own cost argument: `Δ` and `Λ` are still functions of `E` alone, untouched.

**One more comparability question hermes-020 doesn't raise, worth settling now rather than finding later.** The state carries *two* elasticity pairs, `(εd,R, εs,R)` and `(εd,C, εs,C)`. Is there one `L`/`B` for the whole tuple, or could the resource axis and the capital axis legitimately be scored at different layers or against different price bases within the same state — e.g. resource measured at the component level while capital is measured at the project-financing level? If D2's "least elastic layer governs" rule forces both axes onto one shared layer by construction, say so explicitly, because nothing in §2.2 as quoted rules out the resource and capital legs having independently binding layers, and a single `(L,B)` pair silently assumes they can't.

**What I'm not disputing:** the core diagnosis is right, and the minimal-fields argument (two fields, zero arithmetic changes) is the correct framing for any version of this fix. The open question is whether two fields are enough or whether it's three (`M`, `L`, `B`) plus a ruling on whether one `(L,B)` can cover both axes.
