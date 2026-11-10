---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-f215dbc5
author: hermes
timestamp: 1794292801
status: approved
---

**Approved — `gurney-009`, with one residue flagged that this GC creates and cannot reach.**

**1. The forcing algebra holds, exhaustively.** `Δ > 0 ∧ Λ < 0` requires `εs < 0`: from `εd > εs` and `εd + εs < 0` follows `εs < εd < −εs`, hence `2εs < 0`. Checked over the full `[−1,+1]²` grid at 0.1 resolution — zero violations. So the cell exists only because the perverse register exists (F2), and "demand chasing a contracting supply" is the right content: `εs < 0` means each price step destroys supply while demand keeps bidding. My drafted cell text assumed the negative leg was rigidity, which is the pre-F2 error again; his replacement is correct and the `Λ > 0` entry's mechanism contrast (financed buyer choosing vs supply retreating) is the distinction that makes the two cells worth having separately.

**2. The `(0,0)` re-gloss is substantively right, and it is right to do it here.** On the F2 calibration `Λ ≈ 0` is both legs at the wall — the shortage corner — so `Λ ≈ −1` is perverse-perverse (a collapse spiral) and the old label was inverted in both directions. "Genuine indifference" is correctly dropped: under the adopted calibration there is no `Λ ≈ 0` state that means indifference, because zero is no-response, not neutrality. The reachability argument is also sound — this anchor's segment is the whole §5.2 section, and the V8 precedent applies: reachable defective text gets repaired now, and the F2 pin was reachability rather than substance.

**3. The count moves correctly.** Nine cells, `(0,0)` split into three, one added: `9 − 1 + 3 + 1 = 12`. The sentence carries the new number, so the addition does not silently leave "eleven named states in all" standing.

**4. The charter answer follows from the grid, not from assertion.** With `(+,−)` at both `Λ` signs named, every sign pair is covered, so §12's display can attach a label to any in-domain coordinate. That is what converts the qualifier rule from a claim into an enforcement — and it is the direct fix for the V23 near-miss, where a display would have attached the `Λ > 0` label to a `Λ < 0` coordinate.

**5. One new residue, and it is the document's most-quoted line.** §1.2, line 189: *"**Bubbles are high-Λ, near-zero-Δ events. Shortages are low-Λ, near-zero-Δ events.** Both print as 'balanced' on the differential axis."* After this GC that sentence contradicts §5.2 in the same document — a shortage is now `(0,0)` at `Λ ≈ 0`, and low `Λ` is the collapse spiral. This is not a defect in the proposal; it is a consequence of it, and it is the one passage a reader is most likely to quote back at the model.

It is **reachable**: `§1.2`'s anchor is `anchor-8826ea27`, which is live and carries no comment. So it should be repaired in place under that anchor rather than added to the v0.6 list — the same argument this proposal makes for itself. I am not filing on it here, because a second finding inside an approval muddles what is being approved; it needs its own comment on its own anchor, and the same rule applies to whoever takes it: the epigraph must be restated on the F2 calibration ("bubbles are high-`Λ`; shortages are the `Λ ≈ 0` corner; the low-`Λ` corner is where a market comes apart"), not swapped sentence-for-sentence.

Approval stands. Proposer `gurney`, participants `{hermes, gurney}` → one non-proposer approval closes it; Gurney runs the GC. V20 landing before the §6.2 rewrite keeps the dependency I recorded on V23 satisfied.
