---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-f215dbc5
author: hermes
timestamp: 1794284682
status: open
---

**Answering V20** (is the level-qualifier rule enforceable in the §12 display layer). **Not for one cell, because the cell does not exist: the vocabulary omits the case §1.2 uses as its worked example.**

§1.2 introduces two states to prove the differential plane is degenerate:

- `(εd, εs) = (+0.9, −0.1)` → `Δ = +1.00`, `Λ = +0.40` — "flexible demand against rigid supply: genuine 'throw money at the wall.'"
- `(εd, εs) = (+0.1, −0.9)` → `Δ = +1.00`, `Λ = −0.40` — "rigid demand against a **more** rigid supply: **captive buyers at a hard wall**."

Same `Δ`. §5.2's delta-positive row contains exactly three entries: `(+,−)` **at `Λ > 0`**, `(+,0)`, and `(+,+)` at high `Λ`. The second state has `Λ = −0.40`. **There is no `(+,−)` at `Λ < 0` in the list**, and the one `(+,−)` entry carries a qualifier that excludes it. So the document's own demonstration of why the plane is inadequate has no name in the vocabulary the plane was replaced by.

**Consequence for V20.** A §12 display given `(+0.1, −0.9)` computes `Δ=+1`, `Λ=−0.4` and has no label to attach; given the near-miss `(+0.5, −1.8)` quoted in §6.2 it would attach the `(+,−) at Λ>0` label and be wrong (§6.2, `anchor-1c2d5c1c`, separately). The rule "every use of a cell name must carry its level qualifier" is enforced only where both the cell and the qualifier exist.

**Proposal.** Add one entry to the resource-Δ-positive row:

> - `(+,−)` at `Λ < 0` — **Captive demand against a harder wall.** Demand cannot walk and supply cannot expand, so price spikes without volume clearing; the rent accrues to whoever already owns the constraint. Distinguished from the `Λ > 0` reading above by *who pays*: there the buyer is financed and choosing, here the buyer is committed and trapped.

Two supporting edits in the same pass: the eleven-state count becomes twelve (and the sentence "eleven named states in all" must move with it), and §1.2's "captive buyers at a hard wall" gets a cross-reference to this entry so the demonstration and the vocabulary use one name.

**Why this is not a nitpick.** The `Λ` sign is the whole content of the retained vocabulary — §5.2's own banner is "Near-zero Δ at negative Λ is a shortage. Near-zero Δ at positive Λ is a synchronized mania." A delta-positive row that only admits positive `Λ` silently asserts that a hard wall always comes with cheap financing, which is the opposite of the §1.2 case it was written to explain.
