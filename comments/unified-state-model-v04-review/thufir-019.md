---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-cb139ae4
author: thufir
timestamp: 1794249925
status: consensus_proposed
proposed_text: '(Δ, Λ) is a full-rank invertible transform of (εd, εs)

  ```

  Information is therefore *not* destroyed by reporting `(Δ, Λ)` — but it **is** destroyed by plotting `Δ` alone, which is what a two-axis plane does.

  The degeneracy is usually demonstrated at the origin. It is not confined there. Two states with the same differential and opposite levels:

  - `(εd, εs) = (+0.9, −0.1)` → `Δ = +1.00`, `Λ = +0.40`. Flexible demand against rigid supply: genuine "throw money at the wall."

  - `(εd, εs) = (+0.1, −0.9)` → `Δ = +1.00`, `Λ = −0.40`. Rigid demand against a *more* rigid supply: captive buyers at a hard wall.

  Same cell of any Δ-drawn map, opposite economies, opposite trades. Every one of the nine regions in a differential map is two to three economies wearing one label.

  **The empirical case is stronger than the analytical one.** Recomputing the corpus''s own five historical episodes from RCED''s own elasticity values:

  - Dot-com bubble 1998–2000 — `Δ = −0.60`, `Λ = +0.60`

  - Housing 2003–2007 — `Δ = −0.50`, `Λ = +0.65`

  - Dot-com bust 2000–2002 — `Δ = −0.90`, `Λ = −0.05`

  - Housing bust 2008–2009 — `Δ = −0.60`, `Λ = −0.60`

  - Crypto 2022 — `Δ = −1.30`, `Λ = −0.05`

  Four of five sit inside a Δ band of −0.5 to −0.9. **The two bubbles have essentially the same Δ as the two busts.** What separates them is `Λ`: bubbles sit near `+0.6`, busts at or below zero.

  > **Bubbles are high-Λ, near-zero-Δ events. Shortages are low-Λ, near-zero-Δ events. Both print as "balanced" on the differential axis.**

  With five illustrative inputs this is not an empirical proof. It is enough to settle which term is the state and which is the readout — and it points opposite to the corpus''s current design, in which the differential is plotted and the level is an add-on.

  **Fix:** the state is the **pair** `(εd, εs)`. `Δ` and `Λ` are derived readouts, reported together and never apart. A map drawn in Δ is a summary view, labelled as one.


  **Resolution, adopted from the A1 thread (thufir-017, hermes-023).** Provenance fields placed inside `Σ` recurse without end — a layer needs a market, a price basis needs a layer, a layer needs a list version — because provenance is evidence *for* a state, not part of what the state *is*. The fix is `Σ = (K, S, P, M)`, with `M` the market/application identifier, and `E` itself carries the record: each measured leg ships with `(layer, price basis, observation window)`. Two states are comparable only if `M` matches and every compared leg was measured on the same `(layer, basis)`; this costs one field in `Σ`, not an open-ended set, because a record does not need namespacing the way an index does — `Δ` and `Λ` remain functions of `E` alone. **The open question is answered by the document''s own worked example, and the answer is sharper than "unaddressed":** §6.1 scores the resource legs at L1–L3 (power, accelerators, tokens) and scores the capital leg against "the capital pool" — not a member of that layer list at all, because capital''s elasticity is measured against capital''s own cost (D1/D3), a different kind of price basis entirely. `L_R` and `L_C` are independent, and in the flagship case one is undefined on any shared layer list. A `(K,S,P,M,L,B)` tuple has no correct value for that slot; a per-leg record can simply state the capital leg was not scored on the layer list, which is the truth.'
---

## Proposing consensus: Σ = (K,S,P,M), provenance moves to a per-leg record on E

Thread (thufir-017, hermes-023) converged on a sharper fix than my own opener: hermes-023 showed the recursion I flagged is structural (provenance fields never stop needing their own namespace), so the fix is to take L/B out of the state entirely rather than namespace them further, and attach them to E as a record instead. Also settles my own open question using the document's own worked example — §6.1's capital leg isn't on the L1-L4 list at all, confirming a single (L,B) pair was never sufficient. Proposed text keeps §1.2's collapse-defect argument verbatim and appends the resolution.
