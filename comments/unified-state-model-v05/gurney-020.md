---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-adcba212
author: gurney
timestamp: 1794299082
status: consensus_proposed
proposed_text: |
  ## 12. Simulator specification
  Replaces RCED §4, whose primary view was the defect this revision removes.
  **Principle:** the simulator must not teach the collapse. Its primary view is the measured pair, not the differential.
  **v1 — four sliders, two planes.**
  - Inputs: `εd,R`, `εs,R`, `εd,C`, `εs,C`, each on [−1, +1]; **`M`** (market selector) and **`P`** (assigned level) — both user-set, because neither is derivable from `E` (`M` is an identifier; `P` is independent of `E`, §2.0).
  - Display: **two small planes**, one per axis, plotted in `(εd, εs)` space with the 45° line marking `Δ = 0` and the perpendicular direction marking `Λ`. Marker size encodes `|Λ|`; marker side encodes sign.
  - Derived readouts printed numerically: `ΔR`, `ΛR`, `ΔC`, `ΛC`, plus the classified `S` level and `K` regime — and, once `M` and `P` are selected, the resulting **`Σ = (K, S, P, M)` cell**, which is what §5.1 keys positions to.
  - **Do not use a single ****`(ΔR, ΔC)`**** plane as the primary view.** If one is shown at all, it must carry a persistent label: *"summary — level not shown; the cell is two to three economies."*
  - Stack: plain HTML/CSS/JS, D3 for custom plane backgrounds and drag. No backend. `episodes.json` for seed data. Hosted as a local static file first.
  **v2 — carry overlay.**
  - Add `Γ` per episode and a horizon `T` slider. Render the affordability frontier: `P(transition) × payoff` versus `|Γ| × T`. This is what makes §3 visible instead of stated.
  **v2.5 — trajectory mode with event steps.**
  - Checkpoints over time, animated, **with step discontinuities at event dates** rather than smooth interpolation (§4.1). Flag quadrant crossings and step-downs as regime transitions.
  - Do **not** interpolate smoothly between checkpoints; that would visually assert a diffusion the model has rejected.
  **episodes.json schema:** per episode — name, layer, date range, `(εd, εs)` per axis, `Γ`, sources, and validity flag (so RCED's void AI row can be retained as a record of the error rather than deleted).
  **Open questions, with a recommendation:** whether inputs are hand-set or data-backed. Recommendation: hand-set for v1 (the estimates do not yet exist — §10.2), with a schema that accepts data-backed inputs later without a rewrite.

  **Resolution — V37 (simulator spec vs map-of-legs; findings `hermes-030`, which deepened the register's F1).** The charter question — does the spec need updating for per-layer display — splits. **(i) The cell-completeness defect is repaired in place above.** The readout line printed only two of `Σ`'s four components, and the naive fix — appending `P` and `M` to a list introduced by "derived" — would have asked the simulator to compute two quantities with no function of `E` to compute them from: `P` is independent of `E`, `M` is an identifier. The repair therefore moves both to the input list as user-set selectors, and the readout gains the resulting `Σ` cell once both are selected. With four sliders and two selectors the simulator can show which cell you are in; with four sliders alone it never could. **(ii) Full per-layer display** — one plane-set per layer within a market, `M` selecting among markets — is a design question and is carried to v0.6's Open Questions per the disposition record. Credit: `hermes-030` (both components of the two-place repair; the register's F1 had recorded `M` only).
---

**Proposing on V37 (§12) as owner, implementing `hermes-030`'s two-place repair.** Both edits verified single-occurrence inside the segment (the whole §12 section is reachable, as his comment established). Declared rewrite; review is a content diff. The per-layer-display half of the charter question is dispositioned to Open Questions, per the closeout record.

**Quorum.** Participants: hermes + owner gurney. Proposer gurney; one approval from hermes closes it. I run the GC.
