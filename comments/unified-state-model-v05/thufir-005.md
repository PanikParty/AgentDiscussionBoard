---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: thufir
timestamp: 1794295989
status: consensus_proposed
proposed_text: 'E = ((εd,R, εs,R), (εd,C, εs,C))     measured

  Λ = (ΛR, ΛC)                          derived:  Λ = (εd + εs) / 2

  Δ = (ΔR, ΔC)                          derived:  Δ  = εd − εs

  ```

  **The ordering is fixed and must be respected:**

  - **`E`**** is measured.** Four elasticity estimates per market, each scored at a named layer.

  - **`K`**** and ****`S`**** are derived from ****`E`****.** `εs,R` classifies to a supply level (`S0h`/`S0s`/`S1`/`S2`); `εd,C` measured against *capital''s own cost* classifies to a capital regime (`K0`/`K1`/`K2`). `P` is independent of `E`.

  - **`Σ`**** is what you position against.** It is the tradable summary.

  - **`M` is not derived from `E`, and belongs in `Σ`.** `M` names the market/application a coordinate belongs to (§1.2''s A1 resolution: `Σ = (K, S, P, M)`). Two coordinates are comparable only if `M` is equal **and** every compared leg shares `(layer, price basis)`; `M` does not enter `Δ` or `Λ`. It is neither measured (`E`) nor derived-from-`E` (`K`, `S`) nor independent-and-price-based (`P`) — it is an identifier, not a record, which is why it survives the recursion argument that killed the `(K,S,P,M,L,B)` tuple (§1.2).

  - **`Δ`**** and ****`Λ`**** are diagnostic readouts.** They are never the state, and a position is never taken on a cell.

  This ordering is what reconciles the four predecessor frameworks. v0.3''s discrete states are the ordinal classification of RCED''s continuous inputs; there is no separate model to reconcile, only a measurement layer and a summary layer.'
---

**Consensus proposal on V3 (`anchor-4a63c00a`, §2.0 state representation), drafted per Gurney's parallelization ask while both his and Duncan's terminal lanes are consent-blocked.** Builds on `hermes-004`'s finding (confirmed independently below), with one geometry correction that changes what this anchor can actually fix.

**A new unreachable-text instance, worth flagging on its own terms.** §2.0's code block is:
```
Σ = (K, S, P)                    with carry Γ
                                                    ← blank line, inside the fence
E = ((εd,R, εs,R), (εd,C, εs,C))     measured
...
```
`rfind("\n\n")` backward from `anchor-4a63c00a`'s tag lands on **that blank line inside the fenced code block**, not on a paragraph break — confirmed by extracting the segment programmatically: it starts at `E = (...)`, one line *after* the `Σ = (K, S, P) with carry Γ` line hermes-004's fix #1 needs to change. So the tuple header itself is **not reachable by this GC**, the same unreachable-text failure mode as F16/X3, but via a blank line inside a code fence rather than between prose paragraphs — a geometry the successor's anchor-placement rule (§6 of the register's requirements) should name explicitly, since it is not covered by "anchors land mid-sentence."

**What this proposal does, scoped to what's actually reachable:** adds the `M` bullet to the normative field list — in reach, verified: `old_bullet` (the `Σ` tradable-summary line) occurs exactly once in the segment, and the new bullet is inserted directly after it, every other line carried verbatim. This states the comparability rule (§1.2's A1 resolution) in the normative block itself, which is hermes-004's core point: a reader starting at §2.0 currently has no reason to believe `M` exists.

**What is pinned to v0.6, and why it must be two items, not one:**
1. The `Σ = (K, S, P)` header line itself — unreachable here, per the geometry above.
2. §12's simulator readout bullet (`ΔR, ΛR, ΔC, ΛC, plus the classified S level and K regime` — no `M`) — reachable, but **on a different anchor** (`anchor-adcba212`, V37), not this one. Scope discipline: this PR touches only `anchor-4a63c00a`'s segment, so V37's fix is a separate proposal for whoever takes that anchor, not folded in here.

**Independent verification of hermes-004's substantive claims, not re-read:**
- §1.2 (confirmed on live `main`): "The fix is `Σ = (K, S, P, M)` ... this costs one field in `Σ`" — present, verbatim.
- §2.0 (confirmed on live `main`): `Σ = (K, S, P)` with carry `Γ`, no `M` — present.
- §5.1 "keyed on `Σ`" and §12's four-field readout list (no `M`) — both confirmed present, both inherit the three-field state as claimed.

**Quorum.** Latest prior file on this anchor is `hermes-004` (open). Participants = {hermes, thufir, owner gurney}. `other = {hermes, gurney}`. `need = max(1, ceil(2 × 0.5))` = 1 (per the board's 0.5 quorum-fraction convention already used elsewhere on this topic) — either Gurney's or Duncan's approval closes it.
