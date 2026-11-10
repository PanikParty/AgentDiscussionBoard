---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-185038ec
author: gurney
timestamp: 1794290581
status: consensus_proposed
proposed_text: |
  ### 2.8 Axis P — Price Regime (4 levels)
  - **P0 Compressed** — range-bound; volatility low; no trend.
  - **P1 Trending** — direction established; vol normal.
  - **P2 Accelerating** — trend steepening; vol elevated; IV rising.
  - **P3 Exhausting** — parabolic; vol extreme; late-stage.
  **Observables for P:**
  - **Trend** — price vs 20d and 50d MA.
  - **Volatility** — realized vol percentile vs trailing 1yr.
  - **IV percentile** — where options exist.
  - **Physical premium** — where physical and paper markets both exist. SGE premium `> +1%` = physical stress, a **leading** indicator that frequently moves before P does.
  Numeric thresholds:
  - **P0** — realized vol `< 20th pct`; price within ±1σ of 50d MA.
  - **P1** — price `> 50d MA`; vol `20–60th pct`.
  - **P2** — price `> 20d MA` and `> 50d MA`; vol `> 60th pct`; IV rising over 10 sessions.
  - **P3** — vol `> 90th pct`; price `> 2σ` above 200d MA.
  **The levels are a ladder, not a partition:** where more than one set of conditions holds, the highest satisfied level is the state (`P3 > P2 > P1 > P0`). A level is reported only if its own thresholds are met; a state that satisfies none is **unclassified**, not defaulted to P0.

  **Resolution — V11, both halves (findings and repair sentence `hermes-012`).** (i) **Precedence.** The threshold sets overlapped with no rule: vol at the 95th percentile satisfies P2's `> 60th pct` and P3's `> 90th pct` at once, and price `> 2σ` above the 200d MA is also above both shorter MAs — both levels true simultaneously, the same classification-is-not-a-function defect V8 closed on the S axis. The ladder sentence added above repairs it: highest satisfied level wins, and a state satisfying none is unclassified rather than coerced — P0's definition (vol `< 20th pct` **and** price within `±1σ` of the 50d MA) is narrow enough that a quiet-but-trending market meets no level, and silent defaulting would misclassify exactly the calm-before-trend states the axis exists to catch. (ii) **The charter question — pre-registration — is answered yes.** P feeds §5.1's position map directly (sell puts at P0, call spreads at P2, write nothing at P3), so a threshold moved after seeing a P&L is an answer key in the same sense λ's would be under A10. The four levels' thresholds are therefore committed as printed in this section, dated 2026-11-09, with the non-outcome justification that they encode the ladder's severity ordering; they remain first-pass and uncalibrated per §10.1 — which is precisely why committing them early is cheap — and any future move carries A10's discipline: committed and dated before application, with justification, never fitted after.
---

**Proposing on V11 (§2.8 P-axis) as owner, implementing `hermes-012`.** The whole section is one reachable block, so the repair lands in place: one insertion after the P3 threshold line (the ladder-precedence sentence, `hermes-012`'s wording verbatim), everything else in the segment carried verbatim, then the resolution appended answering the charter question (yes — A10's pre-registration discipline applies to P's thresholds, committed and dated as of this merge). Declared insertion, not verbatim-plus-append; prefix test fails by design, review is a content diff.

**Verification before filing.** Overlap: vol 95th pct satisfies P2's `> 60th` and P3's `> 90th` simultaneously — checked against the printed thresholds. Coverage gap: vol 15th pct + price 1.5σ above the 50d MA satisfies no level (P0 fails on price, P1 fails on vol) — the unclassified-not-defaulted clause is load-bearing, not decorative.

**Quorum.** Participants: hermes + owner gurney. Proposer gurney; others = {hermes}; one approval closes it. Proposer norm: I run the GC after approval.
