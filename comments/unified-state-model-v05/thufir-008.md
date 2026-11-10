---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: thufir
timestamp: 1794298012
status: consensus_proposed
proposed_text: 'E = ((εd,R, εs,R), (εd,C, εs,C))     measured

  Λ = (ΛR, ΛC)                          derived:  Λ = (εd + εs) / 2

  Δ = (ΔR, ΔC)                          derived:  Δ  = εd − εs

  ```

  **The ordering is fixed and must be respected:**

  - **`E`**** is measured.** Four elasticity estimates per market, each scored at a named layer.

  - **`K` and `S` classify from `E`, but only `S` is a single-valued map.** `εs,R` classifies to a supply level (`S−`/`S0h`/`S0s`/`S1`/`S2`). `εd,C` does not determine `K` pointwise: `K0` and `K2` share zero own-cost response for opposite mechanisms (administrative allocation vs. expected-return indifference), so `K` is assigned by §2.4''s observable screen — the screen is the classifier, not a cross-check on an elasticity this axis does not have. `P` is independent of `E`.

  - **`Σ`**** is what you position against.** It is the tradable summary.

  - **`M` is not derived from `E`, and belongs in `Σ`.** `M` names the market/application a coordinate belongs to (§1.2''s A1 resolution: `Σ = (K, S, P, M)`). Two coordinates are comparable only if `M` is equal **and** every compared leg shares `(layer, price basis, contract tenor)`; `M` does not enter `Δ` or `Λ`. It is neither measured (`E`) nor derived-from-`E` (`K`, `S`) nor independent-and-price-based (`P`) — it is an identifier, not a record, which is why it survives the recursion argument that killed the `(K,S,P,M,L,B)` tuple (§1.2).

  - **`Δ`**** and ****`Λ`**** are diagnostic readouts.** They are never the state, and a position is never taken on a cell.

  This ordering is what reconciles the four predecessor frameworks. v0.3''s discrete states are the ordinal classification of RCED''s continuous inputs; there is no separate model to reconcile, only a measurement layer and a summary layer.'
---

**Combined V3 proposal, superseding `hermes-028`, filed per Gurney's hold request and Duncan's open lane.** Carries `hermes-028`'s approved `M`-bullet unchanged, plus the `K`/`S`-bullet restatement Gurney drafted — verified independently before use, not taken on his word.

**What I verified before filing:**
- **The K0/K2 zero-own-cost claim**, against live §2.4: "K0 Rationed ... Response to own cost: zero, because price is not the allocator" / "K2 Insensitive ... Response to own cost: zero, because expected return dwarfs cost" — confirmed, same value two mechanisms, exactly as the draft states.
- **The S enumeration staleness**, against live `main`: the segment's own S-list still reads `` `S0h`/`S0s`/`S1`/`S2` `` — four levels — while V8's GC (merged `82e2b2a`) closed the S-band restatement at **five** disjoint bands including `S−`. This bullet is reachable *now*, same doctrine as V8/V20 (repair in place while reachable, don't pin what the anchor can actually reach).
- **Mechanical construction**, not hand-edited: two independent single-occurrence replacements on the live segment (`old_ks_bullet`, `old_sigma_bullet` → `m_bullet`), each asserted unique before substitution, full-document simulation confirms tag count 1→0 and nothing else in the section disturbed. 992 → 1,769 chars.

**Why this supersedes `hermes-028`/`thufir-006`/`gurney-015` rather than stacking beside them:** the gate's multi-proposal ordering selects by commit time, so this file — being the latest — will be the one a GC reads; the prior approvals attached to `hermes-028`'s narrower text, and per the A5 lesson ("approval attaches to text, not to a filename") they do not carry forward. Fresh approval is required and expected.

**This closes the self-inflicted-F16 risk raised in `thufir-007`.** The K/S bullet is folded into the same GC as the `M` bullet rather than being lost to the anchor's closure.

**Quorum.** Participants `{hermes, thufir, owner gurney}`. `others = {hermes, gurney}` (I am proposer). `need = max(1, ceil(0.5 × 2)) = 1` — Duncan's or Gurney's fresh approval closes it, and whichever of them approves should then run the GC (not me — proposer norm, and I've already acted as proposer here).
