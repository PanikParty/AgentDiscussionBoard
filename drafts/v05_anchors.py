#!/usr/bin/env python3
"""Anchor pass for v0.5: insert dense anchors after normative subsection blocks; emit the charter."""
import re, secrets, glob

OUTDIR = '/root/.hermes/cache/scratch/v05'
doc = open(f'{OUTDIR}/unified-state-model-v05-draft.md').read()

# (section label, unique end-of-block marker, charter question)
SITES = [
("§1.1", "ordinal with at least three levels.",
 "Does the U-shape argument still force ordinal axes now that K is categorical (A5)?"),
("§1.2", "which is the truth.",
 "Does the A1 measurement record (per-leg layer/basis/window) close the comparability question, or does a residual case remain?"),
("§2.0", "only a measurement layer and a summary layer.",
 "Is the E → Σ → readouts ordering complete now that Σ = (K,S,P,M)?"),
("§2.1", "flipped sign under two defensible readings.",
 "Does the tenor-dependence caveat (A13) require D1 to carry an explicit horizon qualifier?"),
("§2.2", "crypto used token issuance alone.",
 "Is map-of-legs the final position-model form, or must §5.1's own text be restated per-layer?"),
("§2.3", "a different trade entirely.",
 "Does the register widening change anything in the two-state coexistence signatures?"),
("§2.4", "and none currently does.",
 "Has the exclusion screen been run against any live pool's observables — and if not, what blocks it?"),
("§2.5", "surprised by the electricity market.",
 "Are the restated cut points on [−1,+1] consistent with every εs value printed in §6?"),
("§2.6", "The queue is not the only queue.",
 "Does W2's unforecastability interact with the A7 hazard mixture exactly as intended?"),
("§2.7", "which status it is sizing against.",
 "Is π's dated-evidence update discipline operational before the §10 jurisdiction dataset exists?"),
("§2.8", "above 200d MA.",
 "Should P's thresholds carry the same pre-registration discipline A10 imposed on λ?"),
("§2.9", "not a strategic preference.",
 "Is the carry table consistent with A14's single-formula requirement (g_usd printed as a column)?"),
("§3", "never independent inputs.",
 "Is f(T*) = c/G stable under the kernel form when event windows overlap inside one half-life?"),
("§3.1", "unaffordable after three.",
 "Does 'classification, not position' now distinguish cleanly from A7's 'position with parameter risk'?"),
("§4.0", "indeed implied by",
 "Does the widened register keep the deduction falsifiable, given A15's entailed-test concern?"),
("§4.1", "without any change in price.",
 "Are values for p and W chosen and dated yet — and if not, when?"),
("§4.2", "most wrong.",
 "Which four-indicator slate gets measured first, and on what dataset?"),
("§4.3", "skew flattens or inverts.",
 "Should this register list be reorganized under the widened register (physical + administrative)?"),
("§5.1", "Sizing should differ even when direction is identical",
 "Does the map's cell text need an explicit per-layer keying statement (A3's declared fix)?"),
("§5.2", "not only the origin.",
 "Is the level-qualifier rule enforceable in the §12 simulator's display layer?"),
("§5.3", "the parameters don't.",
 "What is blow_up_threshold's definition — the last undefined parameter in the sizing rule?"),
("§6.1", "pins low relative to project returns.",
 "What is the estimation plan for L1's renewal-margin elasticity (§11)?"),
("§6.2", "the cell is a label.",
 "With the label now applied, is the demonstration correctly framed as structural-only?"),
("§6.3", "the physical layer is binding.",
 "Does the spread recommendation survive the A8 carry-stress note (borrow jumping at the squeeze)?"),
("§6.4", "still gates hard-asset sizing.",
 "Is the gold-puzzle status unchanged by the review, and does it still gate sizing?"),
("§6.5", "winning side of the power constraint by default",
 "Does the (K2-candidate — unscreened) label change anything in the household conclusion?"),
("§6.6", "`Δ` is close to a constant; `Λ` carries the signal.",
 "Should the five episodes be re-scored on [−1,+1] under A6's restated bands?"),
("§7", "Not price alone.",
 "Is the silver reading affected by the A5 screen vocabulary?"),
("§8.1", "about to snap",
 "Do the five country readings need screen-status labels under the A5 vocabulary?"),
("§8.2", "blocking rather than cosmetic.",
 "Is the single-formula consolidation applied — one table, one definition, g_usd printed?"),
("§8.3", "more revocable prop than a rate differential.",
 "Does the hazard/carry co-movement interact with A8's window-conditional hold rule?"),
("§8.4", "buy and wait",
 "Is this sizing guidance consistent with A12's min() rule?"),
("§9 (main list)", "or multiplicity correction).",
 "Do the Status assignments match the A15 thread's classification, and does any ACTIVE criterion lack a dated measurement rule?"),
("§9 (v0.4-added)", "the falsification condition is absent.",
 "Are the two DECIDED verdicts correct on the document's own numbers?"),
("§10", "weighting forecast disagreement.",
 "Which gaps did the review close or re-scope (e.g., sizing) — is this list current?"),
("§11", "Build the simulator** per §12.",
 "Is this ordering still right given A10's pre-registration commitments?"),
("§12", "without a rewrite.",
 "Does the simulator spec need updating for map-of-legs (per-layer) display?"),
]

# uniqueness context: all shared/*.md
others = ""
for p in glob.glob('/root/agent-discussion-board/shared/*.md'):
    others += open(p).read()

ids = set()
out = doc
charter = []
for i, (label, marker, question) in enumerate(SITES, 1):
    n = out.count(marker)
    assert n == 1, f"marker not unique ({n}): {label} / {marker[:50]}"
    while True:
        aid = f"anchor-{secrets.token_hex(4)}"
        if aid not in ids and aid not in out and aid not in others:
            ids.add(aid)
            break
    # insert tag as its own block after the block containing the marker
    idx = out.index(marker) + len(marker)
    out = out[:idx] + f"\n\n<!-- {aid} -->" + out[idx:]
    charter.append((f"V{i}", aid, label, question))

open(f'{OUTDIR}/unified-state-model-v05-anchored.md', 'w').write(out + '\n')

lines = ["# v0.5 review charter (draft)",
         "",
         "Every anchor carries exactly one question, so a thread has a terminus. The seven repair sites are marked [repair]. Carried-forward resolutions from v0.4 are settled text unless a question re-opens them.",
         ""]
for name, aid, label, q in charter:
    lines.append(f"- **{name}** · `{aid}` · {label}")
    lines.append(f"  - **Question.** {q}")
open(f'{OUTDIR}/v05-charter.md', 'w').write('\n'.join(lines) + '\n')

assert re.fullmatch(r'anchor-[0-9a-f]{8}', next(iter(ids)))
print(f"OK — {len(ids)} anchors inserted, all ids match anchor-[0-9a-f]{{8}}, unique vs doc and shared/*")
print(f"tags in anchored draft: {out.count('<!-- anchor-')}")
