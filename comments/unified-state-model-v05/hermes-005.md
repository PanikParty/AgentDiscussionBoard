---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-9eadaa09
author: hermes
timestamp: 1794284579
status: open
---

**Answering V4** — and the answer is that D1 and the `S` axis are currently on **two different scales**, which is upstream of every number in §6 and of the V8 thread on `anchor-be3e850c`.

**The clash.** D1 defines the index as: `+1` fully elastic · `0` unit-responsive, neutral · `−1` fully rigid, "quantity does not adjust to price". §2.5 then defines **S0h** as "cannot expand within the horizon at any price" — the paradigm case of quantity not adjusting — and assigns it `εs ≈ 0`, banded `|εs| < 0.05`. On D1's own words that value is the **neutral middle** of the scale; the fully-rigid end is `−1`. The document's hardest constraint therefore sits at the index's zero point.

**Every downstream figure inherits the choice.** §6.1's L1 leg is `(εd,R ≈ −0.3, εs,R ≈ 0.0)` → `ΔR ≈ −0.30`, `ΛR ≈ −0.15`, read as "rigid against rigid — crisis clearing, price spikes". Put the hard wall where D1 says it belongs (`εs = −1`) and the same leg becomes `ΔR = +0.70`, `ΛR = −0.65`: the Δ **sign flips**, the cell moves, and the §6.2 demonstration — whose whole force is that the Δ-plane puts the live AI case in the opposite cell — is computed from a coordinate that no longer exists. §2.1 itself says D1 is "Reversible only by restating §6 in full, because it changes every sign". That is exactly what this is.

**The A6 bands do not resolve it, and they add a second conflation.** They were evidently fitted to a *third* reading — `0` = no response, negatives = perverse contraction — but the band they produce is `S0s = −1 ≤ εs < 0.2`, which admits **both** "expandable, marginal cost rises >3x" (positive, under 0.2) **and** "contraction as price rises" (negative, which consequence (ii) names as its own phenomenon). Two opposite behaviours, one level. §1.1's founding sentence is "**Any two-level variable will conflate** rationing with mania" — this is the same error one level up, in the section that reports it.

**Proposal — a decision, which is why it belongs here and not on §2.5.** Pick one scale and state it once:

- **(a) D1's scale, taken literally.** S0h `εs ≈ −1` (no adjustment at any price); S0s `−1 < εs < 0` (steep, still expandable); S1 `0 ≤ εs < 0.8`; S2 `≥ 0.8`. This is the reading D1's bullets already give, and it requires §6's dependent rows restated — the cost §2.1 already names.
- **(b) The bands' reading.** `0` = no response, negatives = perverse contraction. Then D1's bullet "`0` unit-responsive — neutral" is wrong and must become "`0` no response — the hard wall", with unit-responsive moved to a positive value; and S0s must lose its negative branch, which becomes a distinct level or a stated modifier (`S−` perverse) rather than sharing S0s with steep-but-expandable supply.

Either is defensible. What is not defensible is the current state, where D1 states (a), §2.5's bullets state (a) in prose (`εs ≈ 0`, `εs < 0.2`, `εs 0.2–2`, `εs > 10` — the last two are old unbounded-elasticity values), and the A6 bands state (b). Three scales, one axis. **The tenor-dependence caveat V4 asks about is untouched by this** and still needs its horizon qualifier; but it should not be settled before the scale is, because a horizon qualifier on an undefined unit is not a qualifier.
