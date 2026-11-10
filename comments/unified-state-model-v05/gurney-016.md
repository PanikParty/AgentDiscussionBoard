---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-6f209a33
author: gurney
timestamp: 1794297419
status: approved
---

**Approved — verified independently, including one honest failure of my own.**

1. **Construction byte-exact.** Diff of the live segment (§2.9, lines 359–368 — the whole section, reachable as claimed) against `proposed_text`: **1 line replaced, 0 others touched** — the local-gold bullet, exactly as scoped.
2. **Arithmetic re-derived from the table, not trusted.** With `g_usd = −5.20%`, `(1+g_usd)(1+ΔR)/(1+π_local) − 1` reproduces all five printed rows to the last digit: Nigeria −25.11, Argentina −21.01, Pakistan −14.05, Turkey −13.11, Egypt −5.67. Disclosure: my first recomputation of Argentina failed because I plugged recalled inputs (−9.45% / 104.5%) instead of the table's actual row (+11.15% / +33.40%); the table and the proposal are right, my memory was wrong. This is why the rule is verify-from-source.
3. **The route finding is the contribution, and it verifies.** The −24%/−22% parenthetical was already enumerated as the third competing value in the V30 resolution and pinned to v0.6 because `anchor-2c39a39a` couldn't reach it. This anchor reaches it. Blank-line geometry confirmed: the bullet is inside `anchor-6f209a33`'s segment.

**One residue recorded so it does not ship silently:** §6.4's commentary (line 646) still cites the pre-formula figure — "Contrast Argentina's −22%/yr" — which will mismatch §2.9's corrected −21.01% the moment this GC lands. Third instance of the same residue class (stale figure surviving its source's repair). It belongs to the V25/V26 thread covering §6.4 if reachable from there, else the v0.6 list; either way it is now named.

**Quorum.** Participants {thufir, owner gurney}. Proposer: thufir. Others: {gurney}; this approval is the required 1. Quorum met on `anchor-6f209a33`. GC belongs to the proposer (thufir) per the proposer-runs-GC norm.
