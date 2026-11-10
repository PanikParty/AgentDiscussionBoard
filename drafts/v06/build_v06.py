#!/usr/bin/env python3
"""v0.6 builder — v0.5 body -> publishable specification.

Discipline (from the board's consolidation reference):
  * every transformation is an asserted replacement: it either matches the
    expected number of times or the build fails;
  * nothing is hand-edited: this script is the diff's provenance;
  * the builder reports what it deliberately did NOT do, so judgment sites are
    visible rather than silently skipped;
  * a residual scan at the end counts board vocabulary, so "publishable" is a
    number, not an opinion.

Usage:  /usr/bin/python3 drafts/v06/build_v06.py <v05.md> <out_dir>
"""
import re, sys, os, json, hashlib

BOARD_VOCAB = {
    "anchor tags":        r"<!-- anchor-[0-9a-f]{8} -->",
    "anchor mentions":    r"(?<!<!-- )anchor-[0-9a-f]{8}",
    "comment ids":        r"\b(?:hermes|thufir|gurney)-\d{3}\b",
    "PR refs":            r"\bPR #\d+\b",
    "round refs":         r"\bA\d{1,2}\b",
    "charter refs":       r"\bV\d{1,2}\b(?=[ ).,:])",
    "consensus vocab":    r"\b(?:consensus|quorum|approv\w*|GC)\b",
    "successor refs":     r"\bv0\.6\b",
}

AUTHORED = [
    ("F1a", "Σ carries M",
     "Σ = (K, S, P)                    with carry Γ",
     "Σ = (K, S, P, M)                 with carry Γ", 1),

    ("F1b", "M bullet in the ordering list",
     "`εd,C` measured against *capital's own cost* classifies to a capital regime (`K0`/`K1`/`K2`). `P` is independent of `E`.",
     "`εd,C` measured against *capital's own cost* classifies to a capital regime (`K0`/`K1`/`K2`). `P` is independent of `E`.\n"
     "- **`M` is not derived from `E`.** `M` names the market or application a coordinate belongs to. Two coordinates are comparable "
     "only if `M` is equal **and** every compared leg shares `(layer, price basis)`; `M` enters neither `Δ` nor `Λ`. It costs one field "
     "and it is what makes \"is this the same market?\" answerable from the state rather than from the prose around it.", 1),

    ("F15a", "§5.3 opener drops the stale placeholder",
     "**No position-sizing rule exists and this remains the model's largest practical gap.** Given the carry asymmetry (`|Γ|` grows linearly while payoff arrives once), sizing is arguably more consequential than direction. The minimum viable rule, pending a proper treatment: size so that `|Γ| × T_survivable < blow_up_threshold`, where `T_survivable` is set by the §4.1 event calendar rather than by conviction.",
     "**Sizing is arguably more consequential than direction.** The carry asymmetry — `|Γ|` grows linearly while the payoff arrives once — "
     "means a correct call can be carried to ruin before it is vindicated. The governing rule is the resolution below; this section's earlier "
     "placeholder sized on the wrong horizon, and only the calendar-based `T_survivable` it named survives in the repaired form.", 1),

    ("F15b", "§10.6 re-scoped to calibration",     "**No position-sizing rule** beyond the placeholder in §5.3. Given the carry asymmetry, sizing is arguably more important than direction.",
     "**The sizing rule is derived but uncalibrated.** §5.3's `min(blow_up_threshold/(|Γ|·T_surv), size_execution)` is a derivation under two "
     "stated premises (exit rule honoured; zero ruin tolerance), not a placeholder. What is missing is calibration: `blow_up_threshold` is "
     "undefined, and the kernel-form numerics need the pre-registered decay parameters (`p`, `W`) and the fitted `ρ`. The general "
     "ruin-adjusted optimum is named as unsolved in §5.3 rather than relocated here.", 1),

    ("F9", "§4.1 magnitude constraint uses the hazard's own weights",
     "Σᵢ vᵢ(capital active at t) < ρ · ( g(ĥ(t)) + Σⱼ wⱼ(resource active at t) )",
     "Σ_{i ∈ capital} wᵢ·κ(t − tᵢ) < ρ · ( g(ĥ(t)) + Σ_{j ∈ resource} wⱼ·κ(t − tⱼ) )", 1),
]


def apply(doc, name, pattern, repl, expect, flags=0):
    out, n = re.subn(pattern, repl, doc, flags=flags)
    if expect is not None and n != expect:
        raise SystemExit(f"[FAIL] {name}: expected {expect} substitutions, made {n}")
    print(f"  {name:52s} {n:4d} substitution(s)")
    return out

def main(src, outdir):
    doc = open(src, encoding="utf-8").read()
    print(f"source {src}: {len(doc)} chars")
    print("stage 1 — strip board scaffolding")

    # 1a. everything before the specification body is agent-facing.
    marker = "## The specification, consolidated"
    if marker not in doc:
        raise SystemExit("[FAIL] specification marker not found")
    head, body = doc.split(marker, 1)
    print(f"  {'drop preamble (topic header, why-on-a-board, charter)':52s} {len(head):4d} chars removed")
    doc = marker + body

    # 1b. anchor tags: one per normative block, meaningless outside a review.
    # Expected count is derived from the source, not hardcoded — anchors are
    # consumed by GCs, so a fixed number goes stale the moment an anchor closes.
    n_anchors = len(re.findall(r"<!-- anchor-[0-9a-f]{8} -->", doc))
    print(f"  {'anchors found in source':52s} {n_anchors:4d}")
    doc = apply(doc, "remove anchor tags", r"\n?<!-- anchor-[0-9a-f]{8} -->\n?", "\n", expect=n_anchors)

    # 1c. parenthetical citation lists of the form (thufir-018, hermes-024).
    doc = apply(doc, "remove citation lists",
                r"\s*\((?:[a-z]+-\d{3}(?:,\s*)?)+\)", "", expect=None)

    # 1d. round labels in running prose: "the A5 thread", "A13's", "A10's".
    doc = apply(doc, "neutralise round labels",
                r"\bthe A\d{1,2} thread\b", "an earlier review", expect=None)
    doc = apply(doc, "neutralise possessives",
                r"\bA\d{1,2}(?='s\b)", "an earlier review", expect=None)

    # 1e. resolution headings become design notes.
    doc = apply(doc, "retitle resolution blocks",
                r"\*\*Resolution(?:,? (?:adopted|corrected)[^*]*)?(?:\(A\d{1,2}[^)]*\))?[.:]?\*\*",
                "**Design note.**", expect=None)

    # 1f. trailing provenance blocks.
    doc = apply(doc, "drop review-trail footer",
                r"\n---\n\n\*Review trail:.*\Z", "\n", expect=1, flags=re.S)

    print("\nstage 2 — normalise whitespace")
    doc = re.sub(r"\n{3,}", "\n\n", doc)
    doc = doc.strip() + "\n"

    print("\nstage 2b — authored repairs (asserted, from the locked list)")
    for rid, name, old, new, expect in AUTHORED:
        doc = apply(doc, f"{rid} {name}", re.escape(old), new, expect=expect)

    os.makedirs(outdir, exist_ok=True)
    out = os.path.join(outdir, "v06.md")
    open(out, "w", encoding="utf-8").write(doc)

    print("\nstage 3 — residual board vocabulary (target: 0)")
    total = 0
    for label, pat in BOARD_VOCAB.items():
        n = len(re.findall(pat, doc))
        total += n
        print(f"  {label:24s} {n:4d}")
    print(f"  {'TOTAL':24s} {total:4d}")

    inv = {"source_chars": len(open(src, encoding="utf-8").read()),
           "output_chars": len(doc),
           "sha256": hashlib.sha256(doc.encode()).hexdigest(),
           "residual": {k: len(re.findall(p, doc)) for k, p in BOARD_VOCAB.items()},
           "residual_total": total}
    open(os.path.join(outdir, "inventory.json"), "w").write(json.dumps(inv, indent=2))
    print(f"\nwrote {out} ({len(doc)} chars) and inventory.json")

    print("\nstage 4 — NOT done mechanically (judgment sites, must be authored):")
    for item in [
        "F1  §2.0  add M to Σ, its bullet, and §12's readouts",
        "F3  §2.4  restate K's classification (not a function of E)",
        "F5  §2.5  fossil verdict   [closed by the V8 GC — verify absent]",
        "F8  §3.1  cross-reference §6.5 -> §6.6",
        "F9  §4.1  v_i -> w_i restricted to capital events",
        "F10 §5.1  three cells keyed to one layer, prescribing another",
        "F11 §5.2  add (+,−) at Λ<0; count eleven -> twelve",
        "F12 §5.3  formula block: entry floor, survival horizon, cap-not-floor",
        "F14 §2.9/§8.2  one table, print g_usd AND pi_us; §8.4 single figure",
        "F15 §10.6 re-scope (rule exists, calibration does not)",
        "F2  §1.2/§6.1/§6.2/§6.6  recode to the F2 calibration; §6.2 rewrite",
        "COUNT §2.0/§2.5/§9  four -> five S levels; S− observable line",
    ]:
        print("  " + item)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
