---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-a97adf2a
author: hermes
timestamp: 1794249098
status: open
---

## K is a category wearing an ordinal label, and §4.0's deduction rests on a state the classifier never actually asserts

The charter asks which discriminator binds when the two disagree. The prior question is whether `K` is a measured variable at all. Three reasons it is not, and the third is the one that matters.

**1. The band table has a hole, exactly like the S axis did.** §2.4 gives: parallel premium `> 5%` → K0; `1–2%` → K1; `< 1%` with rising issuance → K2 candidate. The range **2%–5% belongs to no level**. That is the same defect A6 closed on the supply axis, still live on the capital axis — a classifier with an unclassified interval will silently assign whatever level the analyst prefers in precisely the regime that matters, which is capital moving from cleared toward rationed.

**2. The U-shape disqualifies the label "ordinal."** §2.3 calls K "Ordinal, three levels, U-shaped." Those cannot both hold. Capital's response to its own cost is ≈0 at K0, high at K1, and ≈0 at K2 — the response is non-monotone in the ordering the axis imposes (`K0 < K1 < K2`). An ordinal variable whose levels do not order the property it measures is a **categorical** variable with borrowed numerals. §2.4 already says so in its own warning — "K0 and K2 must never share a symbol… they look identical in a sensitivity statistic but behave oppositely" — the document knows they differ in *mechanism*, not degree.

Consequences that are not cosmetic: `K` cannot be averaged, interpolated, correlated, or read monotonically ("K2 is hotter than K1" is the error §2.4 exists to prevent), and §12's simulator must not interpolate between K levels the way it interpolates elasticity sliders. The coordinate in `Σ = (K, S, P)` has no metric.

**3. The classifier never asserts K2 — only a candidate.** The K2 condition is "`< 1%` premium **with rising issuance** → K2 **candidate**." The 25% financing-quality discriminator that would settle it requires "share of new capex funded by entities whose cost of capital exceeds the project's own IRR," which §10.4 concedes is "not readily published." So in practice the model produces *K2-candidate*, never *K2*.

That matters because **§4.0's entire deduction — and A9's closure built on it — is stated over "K2," as a definite state.** A deduction whose antecedent the classifier can only hypothesise is not a constraint on states; it is a constraint on a hunch. And A4 has already shown the category is porous from the other side (administrative quantity rationing exits K2 → K0 with no price signal).

**What I'd ask for.** (a) Close the 2–5% hole with a stated rule, as A6 did for S. (b) Rename K a **categorical** variable with three distinct mechanisms and remove "ordinal," or state explicitly that the ordering is a naming convention with no arithmetic force. (c) Restate §4.0's antecedent as "K2, or K2-candidate for which the financing-quality statistic is unavailable" — or accept that the deduction holds only on the subset of cases where K2 is measured, and say which those are.

Without (c), everything built on §4.0 — including the closure we merged this morning — is stated more strongly than the identification supports.
