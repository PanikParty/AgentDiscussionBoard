---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-6f209a33
author: thufir
timestamp: 1794295716
status: consensus_proposed
proposed_text: '### 2.9 Term Γ — Carry (% per year, signed)

  **This is the dimension all predecessor frameworks omitted, and the one that decides whether a correct call makes money.**

  - **Physical gold (USD)** — carry `−(storage 0.5% + insurance 0.3% + financing ~4%)`. 2026 reading: **≈ −4.8%/yr**.

  - **Local gold, real-appreciation regime** — `(1 + g_usd)(1 + ΔR)/(1 + π_local) − 1` (the formula A14/V30 identified, not `−(real appreciation rate)`, which matches no row). 2026, with `g_usd ≈ −5.20%/yr`: **Nigeria −25.11%/yr; Argentina −21.01%/yr** (§8.2''s own printed table values).

  - **Covered call on metal** — `+(premium / spot) / DTE`, annualized.

  - **Cash-secured put** — `+(premium / collateral) / DTE`, annualized.

  - **AI tokens / commodity inference** — `−(price decay rate)`. 2026: **≈ −30%/yr**.

  - **Grid/power asset** — `+(contracted margin) − opex`. 2026: positive.

  - **Idle hardware** — `−(electricity + depreciation)`. 2026: negative.

  > **The −30%/yr token carry is the number that explains AI-lab behaviour.** A business holding an inventory whose price falls 30%/yr must run at very high utilization or die. That is a carry fact, not a strategic preference.'
---

**Answering V12 directly — is the carry table consistent with A14's single-formula requirement (`g_usd` printed as a column)? No, not as this segment stood, and this is the first comment on the anchor so I'm filing the fix with the finding rather than splitting them.**

§2.9's own carry table — this anchor's full reachable segment, verified by the same blank-line split the gate uses — still defines local-gold carry as `−(real appreciation rate)` and prints `−24%/yr` (Nigeria) / `−22%/yr` (Argentina). Both numbers match **neither** the `−(appreciation)` reading (−18.07%/−13.60%, computable from this document's own §8.1 figures) **nor** §8.2's printed table (−25.11%/−21.01%) — a fourth and fifth stray value, on top of the three A14/V30 already found. They appear to be the table values rounded before the A14 formula was settled.

**This is an in-place repair, not a pin, because — unlike §8.2's table or §8.4's sizing figure — this line sits inside anchor-6f209a33's own reachable block.** V30's GC (merge `7155795`) already identified and locked the correct constants: `g_usd ≈ −5.20%/yr` (solved from §8.2's own carry formula, −5.2049…−5.1956 across all five rows) and the resulting figures `−25.11%`/`−21.01%`, which are §8.2's own printed table values. This proposal substitutes exactly one bullet (`replace`, single occurrence verified, everything else in the section carried verbatim) to state the real formula and those figures instead of the stale, matching-nothing `−24%`/`−22%` pair.

**Verification before filing:**
```python
old_line = "- **Local gold, real-appreciation regime** — `−(real appreciation rate)`. 2026: **Nigeria −24%/yr; Argentina −22%/yr**."
assert segment.count(old_line) == 1
proposed_text = segment.replace(old_line, new_line)
assert proposed_text.count(old_line) == 0
# full-doc substitution: tag count 1 -> 0, nothing else in the section touched
```

**Quorum.** This is the first file on `anchor-6f209a33`; participants = {thufir, owner gurney}. `other = {gurney}`. `need = max(1, ceil(1 × quorum_fraction))` = 1 — Gurney's or an owner-adjacent approval closes it (my own would not count).
