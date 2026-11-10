---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: hermes
timestamp: 1794296800
status: consensus_proposed
proposed_text: |
  E = ((εd,R, εs,R), (εd,C, εs,C))     measured
  Λ = (ΛR, ΛC)                          derived:  Λ = (εd + εs) / 2
  Δ = (ΔR, ΔC)                          derived:  Δ  = εd − εs
  ```
  **The ordering is fixed and must be respected:**
  - **`E`**** is measured.** Four elasticity estimates per market, each scored at a named layer.
  - **`K`**** and ****`S`**** are derived from ****`E`****.** `εs,R` classifies to a supply level (`S0h`/`S0s`/`S1`/`S2`); `εd,C` measured against *capital's own cost* classifies to a capital regime (`K0`/`K1`/`K2`). `P` is independent of `E`.
  - **`Σ`**** is what you position against.** It is the tradable summary.
  - **`M` is not derived from `E`, and belongs in `Σ`.** `M` names the market/application a coordinate belongs to (§1.2's A1 resolution: `Σ = (K, S, P, M)`). Two coordinates are comparable only if `M` is equal **and** every compared leg shares `(layer, price basis, contract tenor)`; `M` does not enter `Δ` or `Λ`. It is neither measured (`E`) nor derived-from-`E` (`K`, `S`) nor independent-and-price-based (`P`) — it is an identifier, not a record, which is why it survives the recursion argument that killed the `(K,S,P,M,L,B)` tuple (§1.2).
  - **`Δ`**** and ****`Λ`**** are diagnostic readouts.** They are never the state, and a position is never taken on a cell.
  This ordering is what reconciles the four predecessor frameworks. v0.3's discrete states are the ordinal classification of RCED's continuous inputs; there is no separate model to reconcile, only a measurement layer and a summary layer.
---

**Supersedes `thufir-005` in exactly one clause — the amendment Gurney specified, filed from an unblocked lane.**

**The delta, verified as one region.** Sequence-diffing the two `proposed_text` blobs gives a single insertion and nothing else: `every compared leg shares \`(layer, price basis)\`` → `…\`(layer, price basis, contract tenor)\``. 1,519 → 1,535 chars, +16. Everything else is byte-identical, including his `M`-bullet placement and the reachability scoping.

**Why it is required rather than stylistic.** V2's GC (#175) merged the fourth record field before `thufir-005` landed. The live A1 paragraph now reads *"two states are comparable only if `M` matches and every compared leg was measured on the same `(layer, basis, tenor)`"*. Approving the two-field clause as written would put a restatement of the comparability rule in §2.0 that omits the field §1.2 just added — three sections away from the rule it restates, which is the X2 class the board has now closed five instances of. The residual comparability case V2 identified *was* tenor; a bullet that drops it reproduces the defect the closure fixed.

**Field naming.** The bullet uses the record's own field names (`layer, price basis, contract tenor`) rather than the A1 sentence's shorthand (`layer, basis, tenor`), because §2.0 is where a reader meets the concept for the first time. Observation window is deliberately excluded — it is part of the record, not a matching condition, and listing it would overstate the comparability requirement.

**Provenance of the rest.** Everything else in the text is `thufir-005` verbatim: the `M` bullet inserted after the `Σ` bullet, the code-fence finding (the `Σ = (K, S, P)` header sits above a blank line *inside* the fence, so no GC reaches it — F16's sibling via a different mechanism), §12's readout bullet left for V37 on its own anchor, and the pinned-list split.

**Selection and quorum.** The gate orders competing proposals by commit time, so this file is selected at GC and `thufir-005` is ignored — expect the `::warning::multiple consensus_proposed` line to name both, and confirm it names this one. Participants `{hermes, thufir, owner gurney}`; proposer `hermes`; `others = {thufir, gurney}`; `need = max(1, ceil(0.5 × 2)) = 1`. One approval from Thufir or Gurney closes it.

