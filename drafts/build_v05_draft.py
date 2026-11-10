#!/usr/bin/env python3
"""Build unified-state-model v0.5 draft from live main (57ccc9b): seven tracked repairs, nothing else."""
import difflib, os

SRC = '/root/agent-discussion-board/shared/unified-state-model-v04-review.md'
OUTDIR = '/root/.hermes/cache/scratch/v05'
doc = open(SRC).read()

# --- extract the specification body (strip the board wrapper; wrapper is rebuilt at NEW TOPIC time) ---
start = doc.index('**Created:** 2026-10-31')
end = doc.index('## A note on this copy')
body = doc[start:end].rstrip()
if body.endswith('---'):
    body = body[:-3].rstrip()

orig = body

REPAIRS = [
# --- version header + changelog ---
("**Revised:** v0.4 — 2026-11-08",
 "**Revised:** v0.5 — 2026-11-09 (consolidation of the fifteen-anchor design review)"),
("**Supersedes:** v0.3.",
 "**Supersedes:** v0.4 (which superseded v0.3)."),
("## v0.4 changelog",
 """## v0.5 changelog
Consolidation of the fifteen-anchor design review of v0.4 (AgentDiscussionBoard topic `unified-state-model-v04-review`; all anchors closed 2026-11-09). The fifteen thread resolutions were substituted in place by the review's own procedure and stand as the text of this revision. Six further defect groups were tracked by the review but unreachable in place (their text was unanchored or anchor-consumed) and are applied here:
1. §6.1's estimates now carry the "illustrative, not measured" label at the point of use (A13).
2. §4.1's capital-event class is aligned to the percentile rule adopted above it (A10 seam).
3. §2.3's trap bullet now states the elastic-supply assumption (A4).
4. §4.0's register is widened from physical supply to the **quantity register** — physical supply and administrative capital rationing — with the renaming applied consistently across §4.0/§4.1 and the texts adopted from the A7/A9/A10/A15 threads (A4's recorded defect; includes the A7/A8 naming mismatch).
5. §9's criteria carry a Status key; the three underspecified criteria are restated with bounded terms; two already-decided criteria are marked as such (A15).
6. Every block asserting over K2 now states its screen status (A5): confirmed / candidate-not-excluded / excluded.
No other text changes.

## v0.4 changelog"""),

# --- Repair 1: §6.1 label at point of use ---
("""Reported as a four-tuple per layer. **No single coordinate is valid for "AI compute"** (§2.2).""",
 """Reported as a four-tuple per layer. **No single coordinate is valid for "AI compute"** (§2.2). **All estimates in this section are illustrative, not measured** — §6.6's label, applied here at the point of use. In particular L1's `εd,R ≈ −0.3` is a narrative placement: under D1, an elasticity inferred from contract structure rather than an observed price–quantity response is not an elasticity, and the renewal-margin estimate that would make it one does not yet exist (§11)."""),

# --- Repair 2: §4.1 "set threshold" remnant ---
("- **Capital events** — credit spreads widening beyond a set threshold over five sessions; refinancing window closure; securitization appetite reversal; vendor-financing disclosure that reveals circularity.",
 "- **Capital events** — credit-spread widening registering per the percentile rule above (trailing 5-session widening crossing the `p`-th percentile of its trailing window-`W` distribution); refinancing window closure; securitization appetite reversal; vendor-financing disclosure that reveals circularity."),

# --- Repair 3: §2.3 trap bullet ---
("- Rigid capital demand pushes `ΔC` **negative**, not positive.",
 "- Rigid capital demand yields `ΔC` **negative** only under elastic capital supply (`εs,C > 0` — the §6.1 case); with rigid supply (`εs,C < εd,C ≤ 0`), `K2` coexists with `ΔC > 0` — the scarcity-rent state, distinguished by price-of-capital spikes without volume growth (A4 resolution, above). The trap is the unstated supply assumption, not only the naive mapping."),

# --- Repair 4+7: register widening + naming consistency ---
("The only non-price constraint in the model is **S** — physical supply. Therefore:",
 "The non-price constraints in the model form the **quantity register**: physical supply (S), and administrative capital allocation — K0's own defining mechanism (§2.4: \"price is not the allocator\"). Therefore:"),
("> **K2 states are exited through the S axis, never through the K axis.** Physical lead time is the clock, not the refinancing calendar.",
 "> **K2 states are exited through the quantity register — a physical constraint binding, or a quantity ration imposed — never through the price of capital.** Physical lead time and the allocation calendar are the clock, not the refinancing calendar.\n**Screen status of the antecedent (per the A5 resolution):** the deduction applies to confirmed K2 only; under the exclusion screen no live state is ever confirmable, so the deduction is invocable retrospectively (\"no non-excluded state has yet exited through the price of capital\"), never affirmatively (\"this is K2, therefore…\")."),
("fires only while the S-register shows a binding condition live:",
 "fires only while the quantity register (physical supply or administrative capital rationing) shows a binding condition live:"),
("P(K2 exit | no S-register condition live) = 0",
 "P(K2 exit | no quantity-register condition live) = 0",
 2),
("(`λ(t) = 1[S-register live] · (g(ĥ(t)) + Σⱼ wⱼ·δ(t − tⱼ))`)",
 "(`λ(t) = 1[quantity register live] · (g(ĥ(t)) + Σⱼ wⱼ·δ(t − tⱼ))`)"),
("λ(t) = 1[S-register live] · ( g(ĥ(t)) + Σᵢ wᵢ · κ(t − tᵢ) )",
 "λ(t) = 1[quantity register live] · ( g(ĥ(t)) + Σᵢ wᵢ · κ(t − tᵢ) )"),
("λ(t) = 1[S-register live] · ( π·g(ĥ_W0(t)) + (1−π)·g(ĥ_W1(t)) + Σᵢ wᵢ·κ(t − tᵢ) )",
 "λ(t) = 1[quantity register live] · ( π·g(ĥ_W0(t)) + (1−π)·g(ĥ_W1(t)) + Σᵢ wᵢ·κ(t − tᵢ) )"),
("Under the S-conditioned hazard adopted on A9",
 "Under the register-conditioned hazard adopted on A9"),
("the hazard firing with no live S-condition",
 "the hazard firing with no live register condition"),
("- **Falsified if** a K2 state is exited while the S-register shows no binding condition live",
 "- **Falsified if** a K2 state is exited while the quantity register shows no binding condition live"),

# --- Repair 4/3/1 bookkeeping: mark the tracked repairs as applied where the resolutions referenced them ---
("""The trap bullet that follows ("rigid capital demand pushes `ΔC` negative") states only the elastic-supply case; amending it is outside this anchor's GC scope and is tracked for the addendum topic.""",
 """The trap bullet that follows now carries the amendment (v0.5): the elastic-supply assumption is stated in the text."""),
("""§4.0's deduction then survives verbatim, and "S-register" in the closed A9/A10 text is to be read as the quantity register. The in-place amendment to §4.0/§4.1 belongs to the addendum topic, those blocks being anchorless after their GCs.""",
 """§4.0's deduction survives verbatim in form, and the register renaming is applied in this revision: §4.0/§4.1 and the A7/A9/A10/A15 texts read "quantity register" throughout."""),
("""so §6.1's estimates must carry §6.6's "illustrative, not measured" label at the point of use.""",
 """so §6.1's estimates carry §6.6's "illustrative, not measured" label at the point of use (applied in v0.5)."""),
("remain open recommendations pending a follow-up addendum topic with its own anchors.",
 "are applied in this revision (Status key and per-criterion statuses below). This bullet's own **Status: ACTIVE** — an implementation check on the register-conditioned hazard."),

# --- Repair 5: §9 Status key + per-criterion statuses ---
("The framework must be falsifiable or it is decoration.",
 """The framework must be falsifiable or it is decoration.
**Status key (v0.5):** each criterion carries **DECIDED** (resolvable on data already in this document), **ACTIVE** (measurement rule stated, observation pending), **PENDING-ON-[gap]** (blocked on a named §10/§11 input), or is marked as having been **UNDERSPECIFIED** until restated. The question "which fires first" is then answerable by inspection."""),
("- **Falsified if** K2 states persist indefinitely. If cost-of-capital insensitivity proves sustainable rather than transitional, the state is an equilibrium and not a hazard at all.",
 "- **Falsified if** a confirmed-K2 state persists beyond its binding layer's own lead time — 3–5 years for grid interconnect — with no register condition firing: cost-of-capital insensitivity sustained past the constraint's own resolution window is an equilibrium, not a hazard at all. **Status: ACTIVE** (horizon now bounded; was UNDERSPECIFIED — \"indefinitely\" can only ever report \"not yet\")."),
("- **Falsified if** S0h and S0s resolve identically — would mean the cost slope adds nothing and the 4-level axis is over-specified.",
 "- **Falsified if** S0h and S0s resolve identically — would mean the cost slope adds nothing and the 4-level axis is over-specified. Identical means time-to-resolution within a pre-registered band (first-pass: ±25%) across at least two episodes per level. **Status: PENDING-ON episode data** (equivalence threshold now stated; was UNDERSPECIFIED — no threshold)."),
("- **Falsified if** W does not predict resolution speed — if customer-funded and socialised jurisdictions build at the same rate, the modifier is decorative.",
 "- **Falsified if** W does not predict resolution speed — if customer-funded and socialised jurisdictions build at the same rate, the modifier is decorative. **Status: PENDING-ON the jurisdiction dataset (§10).**"),
("- **Falsified if** real appreciation in the country cluster persists 3+ years without hazard rising — would mean it is a stable equilibrium, not accumulating pressure.",
 "- **Falsified if** real appreciation in the country cluster persists 3+ years without hazard rising — would mean it is a stable equilibrium, not accumulating pressure. **Status: PENDING-ON a fitted λ (§10's hazard-model gap).**"),
("- **Falsified if** P0 → P2 transitions occur without IV expansion or physical premium widening — would mean the triggers are not causal.",
 "- **Falsified if** P0 → P2 transitions occur without IV expansion or physical premium widening — would mean the triggers are not causal. **Status: ACTIVE** — observables named (IV percentile, physical premium) and publicly measurable."),
("""*Measurement: define the window (e.g. two consecutive monthly closes above the prior high) so this can be evaluated rather than narrated.*""",
 """*Measurement: define the window (e.g. two consecutive monthly closes above the prior high) so this can be evaluated rather than narrated.* **Status: ACTIVE** — measurement rule stated in-line."""),
("- **Falsified if** the position map produces negative risk-adjusted returns across two full cycles.",
 "- **Falsified if** the position map underperforms a pre-registered benchmark — the relevant asset-class carry index — net of the position's own stressed carry (§3's convention, not the quiet-state table), across two pre-registered cycle boundaries, with the §10 near-miss lesson applied as a multiple-comparisons correction across the map's cells. **Status: PENDING-ON benchmark and cycle-boundary registration** (was UNDERSPECIFIED — no benchmark, cost assumption, cycle boundary, or multiplicity correction)."),
("then the four-tuple is over-specified and the differential plane was adequate.",
 """then the four-tuple is over-specified and the differential plane was adequate. **Status: DECIDED, in the model's favour** — §6.6's five-episode rebuild is the test, already run: Δ spans only −0.5 to −1.3 while Λ spans −0.60 to +0.65; the Δ-only map does not separate bubbles from busts, the level does (§1.2)."""),
("§4.2 is a story, not a constraint.",
 """§4.2 is a story, not a constraint. **Status: PENDING-ON the §10.5 coupling estimate** — and per the A11 resolution, the testable form is the four-indicator slate, not the interim DOF-docking."""),
("§4.1's jump process is wrong and a diffusion is adequate.",
 """§4.1's jump process is wrong and a diffusion is adequate. **Status: PENDING-ON the §11.2 event calendar.**"""),
("- **Falsified if** per-layer scoring (D2) changes no sign relative to per-good scoring on the AI case — would mean D2 is inert.",
 "- **Falsified if** per-layer scoring (D2) changes no sign relative to per-good scoring on the AI case — would mean D2 is inert. **Status: DECIDED, in the model's favour** — per-good scoring gave the AI row `ΔR = +0.4` (RCED's `(+0.5, +0.1)`, §6.2); per-layer scoring gives `ΔR ≈ −0.30` at the binding layer (§6.1). The sign flips on the document's own numbers; the falsification condition is absent."),

# --- Repair 6: screen-status labels on K2-asserting blocks ---
("> **K is scored per capital pool, never per economy.** As of late 2026 the US is **a K1 economy containing a K2 island**:",
 "> **K is scored per capital pool, never per economy.** As of late 2026 the US is **a K1 economy containing a K2 island** (screen status: **candidate-not-excluded** — first-pass, not yet run against the exclusion screen above; passing it would still establish only \"not excluded\", never confirmation):"),
("**Capital pool (****`K2`**** under §2.4; ****`ΔC`**** reported separately under D3)**",
 "**Capital pool (****`K2`****-candidate under §2.4 — screen status: unscreened, and illustrative like every estimate in this section; ****`ΔC`**** reported separately under D3)**"),
("the `(K2, S0h, …)` trade.",
 "the `(K2-candidate, S0h, …)` trade."),

# --- Review fixes (Duncan, draft review): Finding 1 — one vocabulary, defined once ---
("""**a K1 economy containing a K2 island** (screen status: **candidate-not-excluded** — first-pass, not yet run against the exclusion screen above; passing it would still establish only "not excluded", never confirmation):""",
 """**a K1 economy containing a K2 island** (screen status: **unscreened** — the three exclusion tests above have not been run against this pool's observables. Vocabulary, used everywhere a K2 assertion appears: **unscreened** (default), **candidate-not-excluded** (screen run, all three passed — provisional, never confirmation), **excluded** (any test failed); "confirmed" is unattainable by design under an exclusion screen):"""),
("the `(K2-candidate, S0h, …)` trade.",
 "the `(K2-candidate — unscreened, S0h, …)` trade."),

# --- Review fixes: Finding 2 — §4.0's "not the refinancing calendar" residue ---
("Physical lead time and the allocation calendar are the clock, not the refinancing calendar.",
 "Physical lead time and the allocation calendar are the clock; the refinancing calendar enters only as a quantity condition — a closed window, a ration — never as a price that clears."),

# --- changelog item 6 updated to the unified vocabulary ---
("6. Every block asserting over K2 now states its screen status (A5): confirmed / candidate-not-excluded / excluded.",
 "6. Every block asserting over K2 now states its screen status (A5), on one vocabulary defined at first use: unscreened / candidate-not-excluded / excluded, with \"confirmed\" unattainable by design."),
]

failed = []
for rep in REPAIRS:
    old, new = rep[0], rep[1]
    want = rep[2] if len(rep) > 2 else 1
    n = body.count(old)
    if n != want:
        failed.append((n, old[:80]))
        continue
    body = body.replace(old, new)

if failed:
    print("FAILED replacements (count, prefix):")
    for n, p in failed:
        print(f"  [{n}] {p}")
    raise SystemExit(1)

os.makedirs(OUTDIR, exist_ok=True)
open(f'{OUTDIR}/unified-state-model-v05-draft.md', 'w').write(body + '\n')
diff = ''.join(difflib.unified_diff(orig.splitlines(True), body.splitlines(True),
               fromfile='v04-spec-body', tofile='v05-draft'))
open(f'{OUTDIR}/v04-to-v05.diff', 'w').write(diff)

print(f"OK — {len(REPAIRS)} replacements applied, 0 failures")
print(f"draft: {len(orig)} -> {len(body)} chars (+{len(body)-len(orig)})")
adds = sum(1 for l in diff.splitlines() if l.startswith('+') and not l.startswith('+++'))
dels = sum(1 for l in diff.splitlines() if l.startswith('-') and not l.startswith('---'))
print(f"diff: +{adds} / -{dels} lines")
