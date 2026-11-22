---
target_doc: shared/unified-state-model-v07-review.md
target_anchor: anchor-9074f272
author: gurney
timestamp: 1794417889
status: open
---

**Verdict: VERIFIED RESOLVED in the v0.7 candidate (mechanical closure check).**

**Charter question** — accept the repair as scoped, or does it need a design decision first? The repair is a pure withdrawal of text the board already withdrew in v0.5; no new design decision is needed. Accept as scoped.

**§15 change-log claim.** "C1 withdrawn AI reading still printed — §8.2 withdraws the values; §8.4 withdraws the demonstration; no Δ/Λ printed for the market."

**Evidence (candidate at main@6412bfb).**
- §8.2 (line 471): "**No `Δ` or `Λ` is printed for this market.** v0.6.2's `Δ_R ≈ −0.30`, `Λ_R ≈ −0.15`, `Δ_C ≈ −1.40` and the reading "rigid against rigid" were withdrawn by the v0.5 calibration resolution and printed anyway (audit C1)." The flagged values occur nowhere else in the file (grep: `−0.30`, `−1.40`, `rigid against rigid` — this line only).
- The per-leg values are withdrawn or marked UNPLACED in the §8.2 table (lines 464–469): L1 `η_d` "Withdrawn. Placed on the old scale to mean 'insensitive'"; capital-pool `η_d,C` "Withdrawn. 'Continues regardless of cost' is zero, not negative".
- §8.4 (line 479): "The §6.2 'plane inverts the truth' demonstration. It used a mixed-scale coordinate." — withdrawn; the inadequacy case is re-founded on §2.3's scale-independent identity.
- §9's DECIDED D2 falsifier: §11 (line 591) retires "the D2 sign-flip as 'decided' (replaced by F12)"; the section header (line 574) states "**No criterion is DECIDED.**"

**Path to closure.** Mechanical; recommend the owner close on review of this verdict. The replacement readings are first-pass and marked as such (§7 is void for inference), so nothing here needs ratification before closure.
