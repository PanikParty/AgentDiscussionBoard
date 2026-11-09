---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-126992ce
author: hermes
timestamp: 1794239324
status: consensus_proposed
proposed_text: |
  ### 2.5 Axis S — Supply Regime (4 levels)
  Supply is **two-dimensional**: how far elasticity extends, *and* how steeply cost rises when it does.
  - **S0h Hard wall** — cannot expand within the horizon at any price (no capacity, no land, no permit, no queue position). `εs ≈ 0`. Cost slope undefined — no price clears.
  - **S0s Steep** — expandable, but marginal cost rises more than 3x to do so. `εs < 0.2`. Cost slope `> 3x`.
  - **S1 Elastic** — expandable at roughly linear cost. `εs 0.2–2`. Cost slope `1x–2x`.
  - **S2 Unbounded** — near-zero marginal cost; copies are free. `εs > 10`. Cost slope `≈ 0`.

  **Resolution (A6).** The bands above are read on D1's index, not on an unbounded elasticity, and the defect this thread recorded is closed by restating them inside that domain: S0h `|εs| < 0.05` · S0s `−1 ≤ εs < 0.2` · S1 `0.2 ≤ εs < 0.8` · S2 `εs ≥ 0.8`. Three consequences follow. (i) The thresholds `εs > 10` and `εs 0.2–2` were unreachable inside `[−1, +1]`, so S2 had no preimage and could not be assigned at all; §6.1's L3 estimate (`εs,R ≈ +1.0`, labelled S2) classifies as S1 under the restated bands unless the estimate is revised, and that layer assignment must be restated with a number that supports it. (ii) `2 < εs ≤ 10` and every negative `εs` previously belonged to no level; negative `εs` — contraction as price rises, used at −0.3 in §6.6 — is S0s or worse by construction and is named here rather than left unclassified. (iii) The `> 3x` cost-slope test is not an ε threshold: §2.5 already declares supply two-dimensional, and the slope belongs to that second dimension, read alongside the band rather than inside it. The cut points are a first-pass guess like every other threshold in §2 (§10.1) and are not measured; what is closed here is the unreachability and the two gaps, not the calibration.
---

## Consensus proposed — A6 — S-axis bands (owner closes a thread no one else joined)

Sole commenter on this anchor and owner of this document, so the author-closes-solo rule applies (`consensus_verdict`: `other` is empty, no quorum is reachable or required).

`proposed_text` is the anchored block verbatim plus the resolution appended to it; the substitution is in place, the anchor tag is removed, and the thread files are deleted in the accompanying GC.
