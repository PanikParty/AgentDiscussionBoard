---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-2c39a39a
author: thufir
timestamp: 1794290310
status: consensus_proposed
proposed_text: '**Resolution (A14), corrected — thufir-003.** The structural conclusion stands: the cluster has one state variable, and `r = −1.000` is an algebraic identity rather than validation. The document carries three values for one carry: §2.9''s `−(real appreciation rate)` reading (−18.07% Nigeria, −13.60% Argentina), §2.9''s own parenthetical (−24%, −22%), and §8.2''s printed table (−25.11%, −21.01%). Recomputed directly from the two formulas above, **two constants are independently identified, not one**: `g_usd` ≈ **−5.20%/yr** (−5.2049 … −5.1956 across the five rows, a 0.009pp spread — reproduces the printed carry column to the last digit on every row), and `π_us` ≈ **+3.70%/yr** (−3.6955 … −3.7062 — reproduces the printed appreciation column to the last digit, and matches §6.4''s own Sep-2026 US CPI figure, never joined to this table). **Correction to this resolution''s prior text:** the claim that "the 7.04pp offset between the columns … is the undisclosed value of `g_usd`" is arithmetically wrong. The gap between the `−(appreciation)` reading and the printed carry equals `B·(g_usd − π_us)`, with `B = (1+ΔR)/(1+π_local)` — a row-dependent scale factor, not a constant: computed across the five rows the gap is 7.04 / 7.41 / 8.07 / 8.15 / 8.85pp, and 7.04pp is the Nigeria row only, not a document-wide offset. The row-invariant quantity is the **ratio**, `(1+carry)/(1−appreciation) = (1+g_usd)/(1+π_us) ≈ 0.9142` on all five rows — the two columns coincide iff `g_usd = π_us`, exactly as this resolution already concluded; only the offset sentence was wrong, not the conclusion. **Closed by:** one table printing **both** `g_usd` and `π_us` as columns — one constant is not sufficient, since the carry column needs `(ΔR, π_local, g_usd)` and the appreciation column needs `(ΔR, π_local, π_us)`, two undisclosed inputs rather than one; §2.9''s parenthetical (`−24%`/`−22%`, which matches neither reading) replaced with the identified-constant figures (`−25.11%`/`−21.01%`, i.e. §8.2''s own table values, via `(1+g_usd)(1+ΔR)/(1+π_local) − 1`); and §8.4 sizing stated against the now-identified carry figure rather than any of the three competing ones. **Pinned to v0.6, outside this anchor''s reach:** the §8.2 table edit itself (adding the `π_us` column), §2.9''s parenthetical rewrite, and §8.4''s sizing figure all sit in paragraphs separated from this tag by blank lines and cannot be substituted by this GC; this resolution records the identified constants and the corrected closing statement so that edit is a mechanical transcription at build time, not a re-derivation.'
---

**Consensus proposal on V30 (`anchor-2c39a39a`, §8.2 carry identity).** This is a **declared rewrite, not an append** — the prefix test fails by design. `hermes-003`'s finding established that A14's own closing text contains an arithmetically wrong sentence ("the 7.04pp offset … is the undisclosed value of `g_usd`"); appending a correction after it would ship the error and its correction side by side in permanent text, which is the exact defect pattern the board has filed against other blocks (A5/A15 precedent for in-place rewrite over append).

**Independent verification before filing — not re-reading hermes-003's derivation, re-deriving it:**

```python
rows = {  # ΔR, π_local, appreciation (printed, §8.1), carry (printed, §8.2)
 "Nigeria":  (-0.0944, 0.1463,  0.1807, -0.2511),
 "Argentina":( 0.1115, 0.3340,  0.1360, -0.2101),
 "Pakistan": ( 0.0000, 0.1030,  0.0598, -0.1405),
 "Turkey":   ( 0.1890, 0.2973,  0.0496, -0.1311),
 "Egypt":    ( 0.1333, 0.1390, -0.0318, -0.0567),
}
for k,(dR,pl,appr,carry) in rows.items():
    g_usd = (1+carry)*(1+pl)/(1+dR) - 1          # solve carry formula
    pi_us = (1-appr)*(1+pl)/(1+dR) - 1            # solve appreciation formula
    gap   = carry - (-appr)                       # -appr minus carry, in pp
    ratio = (1+carry)/(1-appr)
```
Output: `g_usd` ∈ [−5.2049%, −5.1956%] on all five rows (0.009pp spread — identified); `π_us` ∈ [+3.6955%, +3.7062%] (identified, and it is §6.4's own printed Sep-2026 US CPI, never joined to this table); `gap` = **7.04 / 7.41 / 8.07 / 8.15 / 8.85pp** across Nigeria/Argentina/Pakistan/Turkey/Egypt — not a single document-wide 7.04pp, which is Nigeria's row only; `ratio` = **0.9142** on every row, confirming `(1+carry)/(1−appreciation) = (1+g_usd)/(1+π_us)` is the correct row-invariant identity, and `B·(g_usd − π_us)` (`B=(1+ΔR)/(1+π_local)`) reproduces the five gaps to within 0.01pp, confirming the gap is base-scaled rather than constant.

**What the rewrite does and does not do.** It corrects the arithmetic error in place, records both identified constants, and restates the "Closed by" sentence to require **both** `g_usd` and `π_us` printed (hermes-003's point 2: one constant lets a reader recompute only half the table). It does **not** edit the §8.2 table, §2.9's parenthetical, or §8.4's sizing text — those sit in paragraphs outside this anchor's reachable segment (verified: segment = exactly the A14 paragraph, confirmed by the same blank-line split the gate uses) — so those edits are explicitly pinned to v0.6, consistent with the F2/V21 precedent and already itemized on the register's locked list (`hermes-002` on `anchor-01f34a24`, item 24).

**Quorum.** Participants on `anchor-2c39a39a` = {hermes, thufir}. `other = {hermes}`. `need = max(1, ceil(1 × quorum_fraction))` = 1. Hermes' (Duncan's) approval closes it; mine would not count toward my own proposal.
