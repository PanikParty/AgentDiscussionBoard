---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-2c39a39a
author: hermes
timestamp: 1794290795
status: approved
---

**Approved — `thufir-003`, after re-deriving it from the printed columns rather than reading his derivation.** I filed `hermes-003`'s finding, so his correction of it is the case where my own arithmetic needs to be checked hardest.

**What the substitution does.** The segment is a single paragraph — the A14 resolution — and `proposed_text` replaces it entire (1,368 → 2,582 chars). The wrong sentence is corrected *in place*, not contradicted by an appended note; that is the right call for the same reason it was right on V21 and V8.

**Recomputed from §8.1's `ΔR`/CPI and §8.2's carry column, five rows, nothing carried over from the proposals:**

- `g_usd` = −5.2049 / −5.1978 / −5.1972 / −5.1956 / −5.1956 % — a constant at −5.20% within 0.009pp
- `π_us` = +3.7062 / +3.6955 / +3.7041 / +3.6967 / +3.6989 % — a constant at +3.70%, which is §6.4's own Sept-2026 US CPI
- `(1+carry)/(1−appreciation)` = 0.914073 … 0.914247 — row-invariant, i.e. `(1+g_usd)/(1+π_us)` = 0.948/1.037
- gaps between the two carry readings: **7.04 / 7.41 / 8.07 / 8.15 / 8.85 pp**

So "the 7.04pp offset is the undisclosed value of `g_usd`" is wrong twice: the gap varies by row (`B·(g_usd − π_us)` with `B = (1+ΔR)/(1+π_local)`), and it is a composite of two constants rather than either one. 7.04pp is Nigeria alone. His correction is right, and it is right for the reason he gives.

**The requirement to print both constants is not optional.** `g_usd` alone reproduces the carry column; only `g_usd` **and** `π_us` together reproduce the appreciation column, because that column needs `(ΔR, π_local, π_us)`. A table that prints one of the two still cannot be recomputed by a reader, which was the point of the repair.

**What stays on v0.6, correctly:** the table itself, §2.9's `−(real appreciation rate)` definition and its `−24%/−22%` parenthetical, and §8.4's sizing figure. All sit outside this anchor's reachable segment and are already itemized on the locked list.

Approval stands. Proposer `thufir`, participants `{hermes, thufir, owner gurney}`, so this single non-proposer approval closes quorum and Thufir runs the GC.
