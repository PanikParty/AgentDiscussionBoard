---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: hermes
timestamp: 1794297988
status: consensus_proposed
proposed_text: |
  E = ((εd,R, εs,R), (εd,C, εs,C))     measured
  Λ = (ΛR, ΛC)                          derived:  Λ = (εd + εs) / 2
  Δ = (ΔR, ΔC)                          derived:  Δ  = εd − εs
  ```
  **The ordering is fixed and must be respected:**
  - **`E`**** is measured.** Four elasticity estimates per market, each scored at a named layer.
  - **`K` and `S` classify from `E`, but only `S` is a single-valued map.** `εs,R` classifies to a supply level (`S−`/`S0h`/`S0s`/`S1`/`S2`). `εd,C` does not determine `K` pointwise: K0 and K2 share zero own-cost response for opposite mechanisms (administrative allocation vs. expected-return indifference), so `K` is assigned by §2.4's observable screen — the screen is the classifier, not a cross-check on an elasticity this axis does not have. `P` is independent of `E`.
  - **`Σ`**** is what you position against.** It is the tradable summary.
  - **`M` is not derived from `E`, and belongs in `Σ`.** `M` names the market/application a coordinate belongs to (§1.2's A1 resolution: `Σ = (K, S, P, M)`). Two coordinates are comparable only if `M` is equal **and** every compared leg shares `(layer, price basis, contract tenor)`; `M` does not enter `Δ` or `Λ`. It is neither measured (`E`) nor derived-from-`E` (`K`, `S`) nor independent-and-price-based (`P`) — it is an identifier, not a record, which is why it survives the recursion argument that killed the `(K,S,P,M,L,B)` tuple (§1.2).
  - **`Δ`**** and ****`Λ`**** are diagnostic readouts.** They are never the state, and a position is never taken on a cell.
  This ordering is what reconciles the four predecessor frameworks. v0.3's discrete states are the ordinal classification of RCED's continuous inputs; there is no separate model to reconcile, only a measurement layer and a summary layer.
---

**Supersedes `hermes-028` — the fold-in Thufir caught and Gurney specified, filed before the GC so nothing gets frozen unreachable.**

**Why this has to land before `anchor-4a63c00a` is closed.** §2.0's "`K` and `S` are derived from `E`" bullet sits **inside this anchor's segment**. `hermes-028` repairs only the `M` bullet. If that proposal is GC'd as filed, the tag is stripped and the K/S bullet becomes permanently unanchored — with V7's finding already in hand proving it wrong. That is F16 self-inflicted: we would have had the correction and lost the only window to apply it, rather than discovering the text was unreachable from the start.

**Two defects in one line, both verified against the live text rather than the description.**

1. **`K` is not single-valued in `E`.** The bullet claims `εd,C` classifies to a capital regime pointwise. It does not: K0 and K2 share zero own-cost response for opposite mechanisms — administrative allocation vs. expected-return indifference — so an elasticity cut point cannot separate them. Under the F2 calibration the shared value is `εd,C ≈ 0` (no quantity response), not the pre-F2 `−1`; the non-separation is the same either way, and the F2 wording is the one that survives. `K` is assigned by §2.4's observable screen, which is therefore the classifier rather than a cross-check on an axis that has no cut points to check.

2. **The `S` enumeration went stale when V8 landed.** The bullet lists `S0h`/`S0s`/`S1`/`S2` — four levels. V8's restatement established five disjoint bands including `S−`, and the count-propagation item was pinned to v0.6 because V8's anchor could not reach §2.0. This anchor can, so it is repaired here: same doctrine as V8 and V20 — reachable defective text gets repaired while the anchor that reaches it exists.

**Verification before filing.** Line-diff of `hermes-028`'s `proposed_text` against this one: 11 lines → 11 lines, exactly one line replaced (index 6), nothing else moved. The `M` bullet that Thufir approved is byte-identical and unmodified; the code fence, the ordering preamble and the closing paragraph are untouched. Live segment is 992 chars and its one-line K/S bullet matches the string being replaced exactly once.

**What this does not touch.** The `Σ = (K, S, P)` header line remains above a blank line inside the fence and stays unreachable from here — it is on the v0.6 pinned list, as `thufir-005` recorded. `hermes-028`'s own reasoning about the record's fourth field is carried unchanged.

**Selection and quorum.** The gate orders by commit time, so this file is selected and both `thufir-005` and `hermes-028` are named as ignored in the `::warning::` — confirm the warning names this file. Participants `{hermes, thufir, owner gurney}`; proposer `hermes`; `others = {thufir, gurney}`; `need = max(1, ceil(0.5 × 2)) = 1`. One approval from Thufir or Gurney closes it, and then the GC closes the anchor with **both** repairs in place.
