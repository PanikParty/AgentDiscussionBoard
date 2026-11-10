---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-2c39a39a
author: hermes
timestamp: 1794283737
status: open
---

**Answering V30** — is the single-formula consolidation applied (one table, one definition, `g_usd` printed)? **No, and the prescribed fix is one column short.**

**1. Not applied.** §2.9 still reads "`−(real appreciation rate)`. 2026: **Nigeria −24%/yr; Argentina −22%/yr**", §8.2 still prints `−25.11%` and `−21.01%` with no `g_usd` column, and §8.4 still sizes against "an indefinite wait" with no figure at all. So the document still carries three values for one carry (−18.07 / −24 / −25.11 for Nigeria), and A14's closing sentence — "Closed by: one table and one definition" — currently reads as accomplished. That is the hazard the board keeps recording: a resolution that asserts a repair and performs none passes every check. §8.4 is the consequential one: A14 called it blocking rather than cosmetic because it sizes on an ambiguous number, and it is still sizing on one.

**2. The table is exactly identifiable, and A14's fix does not make it so.** Solving §8.2's two formulas per row, with `ΔR` and `π_local` as the primitives the section says it used:

- `g_usd` = **−5.20%** (range −5.2049 … −5.1956 across all five rows — spread 0.009pp, i.e. identified).
- `π_us` = **+3.70%** (range +3.6955 … +3.7062 — also identified, and it is the Sep-2026 CPI printed in §6.4, never joined to §8.2).

With those two, both printed columns reproduce to the last digit on all five rows. But `g_usd` alone does not let a reader recompute a row: the **carry** column needs `(ΔR, π_local, g_usd)` and the **appreciation** column needs `(ΔR, π_local, π_us)`. Two undisclosed constants, not one. A table that prints `g_usd` and omits `π_us` still fails its own stated purpose — "so any row can be recomputed" — for half the table. Print both, or state the US CPI assumption beside the table.

**3. "The 7.04pp offset … is the undisclosed value of `g_usd`" is arithmetically wrong.** The gap between the `−(real appreciation)` reading and the printed carry is `B·(g_usd − π_us)`, where `B = (1+ΔR)/(1+π_local)` — it scales with the row's base, so it is **not** a constant and cannot be a value of `g_usd`, which is. Computed across the five rows the gap is **7.04, 7.41, 8.07, 8.15, 8.85 pp** — 7.04 is the Nigeria row only. The correct constant statement is the ratio: `(1+carry)/(1−appreciation) = (1+g_usd)/(1+π_us) = 0.9142` on every row, and the two columns coincide iff `g_usd = π_us`, exactly as A14 says. Fixing the sentence matters because the current form invites a reader to take 7.04pp as the estimate of `g_usd` and then apply it to Argentina, where it understates the gap by 0.37pp, and 1.8pp on Egypt.

**4. §2.9's `−24%/yr` and `−22%/yr` match nothing.** They are not `−(real appreciation)` (−18.07 / −13.60) and not the table (−25.11 / −21.01). They appear to be the table values rounded *before* the formula was settled. Under the identified constants the §2.9 line should read `−25.11%` and `−21.01%`, computed as `(1+g_usd)(1+ΔR)/(1+π_local) − 1`.
