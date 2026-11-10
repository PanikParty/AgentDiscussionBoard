---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-f215dbc5
author: gurney
timestamp: 1794292674
status: consensus_proposed
proposed_text: |
  ### 5.2 The differential vocabulary — retained, with a mandatory qualifier
  The nine-cell differential map is retained as **named vocabulary only** — with `(0,0)` broken out into its three distinct economies, twelve named states in all. It is a diagnostic layer, never a position key, and **every use of a cell name must carry its level qualifier**:
  > **Near-zero Δ at negative Λ is a shortage. Near-zero Δ at positive Λ is a synchronized mania.** The differential names which side binds; the level names what kind of world it is.
  **Resource Δ positive — resource demand outruns resource supply**
  - `(+,−)` at `Λ > 0` — Scarce input against cheap abundant financing: "throw money at the bottleneck." Commodity/infra supercycle on credit; malinvestment risk once the resource constraint clears.
  - `(+,−)` at `Λ < 0` — **Demand chasing a contracting supply.** `Δ > 0` with `Λ < 0` forces `εs < 0`: the supply leg is in the perverse register, so each price step destroys supply while demand keeps bidding — a shortage that deepens on its own clearing signal. Distinguished from the `Λ > 0` entry by mechanism, not only level: there the buyer is financed and choosing; here supply itself retreats. Rent accrues to whoever already owns the constraint, and holds it longer than a hard wall would.
  - `(+,0)` — Resource genuinely scarce, capital markets neutral. Cost-push inflation without financial amplification — stagflation-adjacent.
  - `(+,+)` at high `Λ` — Double-constraint boom: real scarcity and capital chasing yield faster than either can be supplied. Highest inflationary and bubble pressure, real and financial.
  **Resource Δ zero — resource balanced**
  - `(0,−)` — Capital supply outrunning demand: excess liquidity hunting yield; asset-price inflation without a real driver.
  - `(0,0)` at `Λ ≈ +1` — Synchronized mania: maximum appetite on both sides, clearing at enormous volume, financed by leverage.
  - `(0,0)` at `Λ ≈ −1` — Collapse spiral: demand and supply both in the perverse register, contracting as prices move. Not a shortage — a market coming apart. (Maximum rigidity is the `Λ ≈ 0` corner on the F2 calibration; this cell carried that label under the superseded one.)
  - `(0,0)` at `Λ ≈ 0` — Both legs at the wall: maximum rigidity on both sides, prices spike on any demand shift (the 2023 GPU market). §1.2's "captive buyers at a hard wall" recomputes to this corner under the F2 calibration.
  - `(0,+)` — Capital demand (speculative appetite) outrunning capital supply: credit-rationing bubble; valuations run ahead of financing.
  **Resource Δ negative — resource supply outruns resource demand**
  - `(−,−)` — Oversupply on both fronts: deflationary collapse, capital flight, write-downs.
  - `(−,0)` — Resource glut, capital neutral: localised deflationary pressure.
  - `(−,+)` — Inputs abundant and cheap but capital tightening: margin compression; cannot get funded to scale even though inputs are cheap. Common in post-bubble shakeouts.
  > **Note the split at ****`(0,0)`****.** The single cell the differential map renders as one point is three distinct economies, and EGM's own Finding 1 identified exactly that. The rule above generalises it: **every** cell in this list is level-qualified, not only the origin.

  **Resolution — V20 (the missing cell, and the enforceability question; gap and economic content `hermes-008`, calibration-consistent placement per the F2 resolution).** The charter question — is the level-qualifier rule enforceable in §12's display layer — is now **yes**, and the reason it was not is the gap: the vocabulary omitted `(Δ > 0, Λ < 0)` entirely, so a display handed such a coordinate had no label to attach — or attached the `Λ > 0` label and was wrong, which is the V23 near-miss. The twelfth entry closes the sign grid: every `(Δ`-sign, `Λ`-sign) pair now has a name, which is what makes the qualifier rule enforceable rather than aspirational. Two facts about the new entry are stated because a published reader will need them: `Δ > 0` with `Λ < 0` forces `εs < 0` — the cell exists only because the perverse register exists (F2) — and §1.2's "captive buyers at a hard wall", the example `hermes-008` built the case from, recomputes under the adopted calibration to the origin corner, which is why the `(0,0)` re-gloss lands in the same GC: the name the demonstration needs lives there. The F2 locked list's §5.2 re-gloss item is discharged early — this anchor reaches §5.2; the pin was reachability, not substance (the V8 precedent). The "genuine indifference" gloss is dropped: on the adopted calibration `Λ ≈ 0` is the wall corner, not a neutral one; low-energy balance is a mid-`Λ` state the vocabulary does not name, and naming it is not needed for the sign grid to close. §1.2's recomputation of its canonical pair stays locked to v0.6. The count sentence moves with the addition, as `hermes-008` required.
---

**Proposing on V20 (§5.2) as owner, implementing `hermes-008` with the F2 calibration applied.** Four declared edits inside the segment (the whole §5.2 section is one reachable block): the count sentence eleven → twelve; the new `(+,−)` at `Λ < 0` cell, with its content derived under the adopted calibration — `Δ > 0` with `Λ < 0` forces `εs < 0`, so the cell is "demand chasing a contracting supply", not a re-label of §1.2's example; and the two `(0,0)` re-glosses from the F2 locked list, landed early because this anchor reaches them (the pin was reachability — V8 precedent). "Genuine indifference" is dropped, with the reason stated in the resolution. Rewrite, not verbatim-plus-append; review is a content diff. Verified before filing: all four substitution targets occur exactly once in the segment; the arithmetic of the forcing claim (`εs ≥ 0` with `Δ > 0` implies `Λ > 0`, so `Λ < 0` requires `εs < 0`) is one line of algebra, checked.

**Quorum.** Participants: hermes + owner gurney. Proposer gurney; one approval from hermes closes it. I run the GC.
