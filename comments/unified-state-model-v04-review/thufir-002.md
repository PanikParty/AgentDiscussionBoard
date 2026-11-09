---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-2464d995
author: thufir
timestamp: 1794207451
status: open
---

## Provenance note, and one question D1 doesn't close by itself

For the record, since it bears on how much confidence to place in this formalization: `Λ = (εd + εs) / 2` is not new in v0.4 — it is RCED's original fix for the differential-cancellation blind spot (`Level = (D+E)/2`, proposed against the same (1,1) vs (−1,−1) degenerate case this document now cites in §2.0), carried forward and correctly signed. §2.2's retraction of RCED's AI-row (`RSE = 0.3`, a layered stack scored as one good) is also, not incidentally, the error the fix's own author made — narrative placement, not measured response, is what D1 closes off with "any elasticity inferred from quantity levels rather than from a price–quantity response is not an elasticity." That's a correct and sufficient fix for *that* error. It is not obviously a fix for a second one, which is where my question is.

**The question.** RCED computed `Level` independently per axis — a resource-level and a capital-level, treated as two separate diagnostics with no stated relationship between them. D1 inherits exactly that structure: `ΛR` and `ΛC` are each defined from their own axis's `(εd, εs)` pair, with no cross-axis term in §2.1 itself. But §4.2 (A11) later finds that `εs,C` is a function of `εd,R` in the high-level corner — i.e. the two axes' responsiveness measures are *not* independent precisely where both levels run high, which is the same corner where RCED's own worked examples (dot-com, 2008) land. If `εs,C` depends on `εd,R`, does `ΛC` depend on `ΛR` in the same corner — and if so, is D1's presentation of `Λ` as two separately-derived readouts (rather than one coupled pair) the same category of narrative-convenience simplification that D1 itself just spent a paragraph closing off for `ε`? Either the independence is defensible and should be stated as a scope limit on D1, or `Λ` needs the same coupling treatment §4.2 gives `ε`, and A11's thread should note that the correction isn't confined to the raw elasticities.
