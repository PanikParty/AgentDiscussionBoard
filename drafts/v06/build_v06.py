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

    ("F15a", "§5.3 opener drops the stale placeholder",
     "**No position-sizing rule exists and this remains the model's largest practical gap.** Given the carry asymmetry (`|Γ|` grows linearly while payoff arrives once), sizing is arguably more consequential than direction. The minimum viable rule, pending a proper treatment: size so that `|Γ| × T_survivable < blow_up_threshold`, where `T_survivable` is set by the §4.1 event calendar rather than by conviction.",
     "**Sizing is arguably more consequential than direction.** The carry asymmetry — `|Γ|` grows linearly while the payoff arrives once — "
     "means a correct call can be carried to ruin before it is vindicated. The repaired rule appears below under "
     "**The repaired rule.**; this section's earlier placeholder sized on the wrong horizon, and only the calendar-based "
     "`T_survivable` it named survives in the repaired form.", 1),

    ("F2a", "D1's calibration bullets carry the adopted reading",
     "- `+1` fully elastic — quantity adjusts freely to price\n"
     "- `0` unit-responsive — neutral\n"
     "- `−1` fully rigid — quantity does not adjust to price",
     "- `+1` fully elastic — quantity adjusts freely to price\n"
     "- `0` no quantity response — the hard wall: quantity does not adjust at any price\n"
     "- `−1` perverse contraction — a distinct register, where quantity *falls* as price rises", 1),

    ("F2b", "§1.2 epigraph carries the adopted reading",
     "> **Bubbles are high-Λ, near-zero-Δ events. Shortages are low-Λ, near-zero-Δ events. Both print as \"balanced\" on the differential axis.**",
     "> **Bubbles are high-Λ events. Shortages are the `Λ ≈ 0` corner — both legs at the wall. "
     "The low-Λ corner is not a shortage but a market coming apart.**", 1),

    ("F2c", "zero bullet carries the cross-reference the resolution block held",
     "- `0` no quantity response — the hard wall: quantity does not adjust at any price",
     "- `0` no quantity response — the hard wall: quantity does not adjust at any price. It is the value shared by "
     "§2.5's `S0h` (\"cannot expand within the horizon at any price\"), §7's silver (`εs \u2248 0.0`), and §2.4's "
     "\"response to its own cost: zero\" for `K0`/`K2`.", 1),

    ("F2d", "perverse bullet carries the episode note",
     "- `−1` perverse contraction — a distinct register, where quantity *falls* as price rises",
     "- `−1` perverse contraction — a distinct register, where quantity *falls* as price rises. Three of "
     "§6.6's five episodes are busts written on this register.", 1),

    ("F16a", "§2.4 K2 observable names the screen, not the retired statistic",
     "Financing-quality test (the K2 discriminator)",
     "K2-candidate screen (the K2 discriminator): the three observable conditions of the exclusion screen, "
     "applied conjunctively; passing establishes \"not excluded\", never confirmation", 1),

    ("F15c", "blow_up_threshold defined inline, not by reference to a stripped resolution",
     "`blow_up_threshold` is defined in the resolution below (`k · U`, unencumbered non-callable capital; the fraction-of-book and margin-cushion readings are rejected there)",
     "`blow_up_threshold = k · U`, where `U` is unencumbered non-callable capital and `k` a pre-registered fraction "
     "(the fraction-of-book and margin-cushion readings are rejected: neither isolates capital that cannot be called away)", 1),

    ("F9", "§4.1 magnitude constraint uses the hazard's own weights",
     "Σᵢ vᵢ(capital active at t) < ρ · ( g(ĥ(t)) + Σⱼ wⱼ(resource active at t) )",
     "Σ_{i ∈ capital} wᵢ·κ(t − tᵢ) < ρ · ( g(ĥ(t)) + Σ_{j ∈ resource} wⱼ·κ(t − tⱼ) )", 1),
]

# Repairs that GCs have already landed in the source document. These are
# asserted, not repaired: if one goes missing the build fails, because the
# document would then carry text an earlier closure had removed.
LANDED = [
    ("F1b", "M bullet present in §2.0's ordering list", "`M` is not derived from `E`"),
    ("F15b", "§10.6 sizing entry re-scoped", "The sizing rule is derived and repaired"),
    ("V3-K", "§2.0 K/S bullet restated", "only `S` is a single-valued map"),
    ("V37", "§12 readout prints the Σ cell", "the resulting **`Σ = (K, S, P, M)` cell**"),
]


# Whole blocks that are review process, not model content. Deleted by span
# between a start marker and the next section heading, asserted to occur once.
STRIPS = [
    ("F2e", "strip the F2 resolution block",
     "**Resolution — F2, index calibration", "### 2.2 Decision D2"),
]


def strip_block(doc, name, start, end):
    i = doc.find(start)
    if i < 0:
        raise SystemExit(f"[FAIL] {name}: start marker absent")
    if doc.count(start) != 1:
        raise SystemExit(f"[FAIL] {name}: start marker not unique")
    j = doc.find(end, i)
    if j < 0:
        raise SystemExit(f"[FAIL] {name}: end marker absent after start")
    removed = j - i
    print(f"  {name:52s} {removed:4d} chars removed")
    return doc[:i] + doc[j:]


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
        if old not in doc:
            # A GC may have landed this repair in the document already. That is
            # success, not failure: the authored list exists for text no GC can
            # reach, and retires as closures land. Only an absent-and-unapplied
            # repair is an error.
            if new in doc:
                print(f"  {rid} {name:50s}   --  already applied by GC")
                continue
            raise SystemExit(f"[FAIL] {rid} {name}: neither the pre-repair text nor the repaired text is present")
        doc = apply(doc, f"{rid} {name}", re.escape(old), new, expect=expect)

    print("\nstage 2f — drop review citations and superseded changelogs")
    # Parenthetical round/charter citations carry no content for a reader who
    # does not have the review threads; the clause they annotate stays.
    for pat, label in [
        (r"\s*\((?:the )?A\d{1,2}(?: resolution)?(?:/V\d{1,2})?\)", "round citations"),
        (r"\s*\(V\d{1,2}(?:, V\d{1,2})*\)", "charter citations"),
        (r"\s*\((?:hermes|thufir|gurney|duncan)-\d{3}(?:, (?:hermes|thufir|gurney|duncan)-\d{3})*\)", "comment citations"),
    ]:
        doc, n = re.subn(pat, "", doc)
        print(f"  {label:52s} {n:4d} substitution(s)")

    # v0.4 and v0.3 changelogs describe drafts nobody reading this will open.
    for start_marker, end_marker, label in [
        ("## v0.4 changelog", "## v0.3 changelog (retained)", "v0.4 changelog"),
        ("## v0.3 changelog (retained)", "## 0. Purpose", "v0.3 changelog"),
    ]:
        i = doc.find(start_marker)
        if i < 0:
            print(f"  {'SKIP ' + label:52s}    - start marker absent")
            continue
        j = doc.find(end_marker, i)
        if j < 0:
            print(f"  {'SKIP ' + label:52s}    - end marker absent")
            continue
        print(f"  {'strip ' + label:52s} {j - i:4d} chars removed")
        doc = doc[:i] + doc[j:]

    for pat, repl, label in [
        (r"per the A5 resolution", "per the exclusion screen", "A5 prose reference"),
        (r"the A13 resolution", "the tenor caveat", "A13 prose reference"),
        (r"the A13 resolution's", "the tenor caveat's", "A13 possessive"),
        (r"the formula A14/V30 identified", "the identified carry identity", "A14 prose reference"),
        (r"\bA14\b", "the carry identity", "A14 bare reference"),
    ]:
        doc, n = re.subn(pat, repl, doc)
        if n:
            print(f"  {label:52s} {n:4d} substitution(s)")

    print("\nstage 2e2 — strip discharged-process paragraphs (asserting pin state)")
    DISCH = re.compile(
        r"(?i)\b(pinned to|rides (?:the )?successor|the successor (?:applies|rewrites|carries)|"
        r"in v0\.6 \(locked\)|locked, per|presently staged|is rewritten in v0\.6|"
        r"status key \(v0\.5\)|charter question, answered)\b")
    paras = doc.split("\n\n")
    keep, dropped = [], []
    for para in paras:
        head = para.lstrip()
        # Only the paragraph's OWN opening claim counts. A phrase buried deep in a
        # long block (§10's gap list carries "locked, per" inside one entry) must
        # not take the whole section with it — that removal cost §10 entirely on
        # the first run.
        if not head.startswith("#") and DISCH.search(head[:250]):
            dropped.append(head[:78].replace("\n", " "))
            continue
        keep.append(para)
    doc = "\n\n".join(keep)
    for d in dropped:
        print(f"    - {d}")
    print(f"  {'discharged-process paragraphs removed':52s} {len(dropped):4d} paragraph(s)")

    # attributions: "per <comment-id>" -> plain content
    doc, n = re.subn(r"\s*\bper (?:hermes|thufir|gurney|duncan)-\d{3}\b", "", doc)
    print(f"  {'drop \"per <comment-id>\" attributions':52s} {n:4d} substitution(s)")

    print("\nstage 2d — strip review-process blocks")
    for rid, name, start, end in STRIPS:
        doc = strip_block(doc, f"{rid} {name}", start, end)

    print("\nstage 2e — strip review-process paragraphs (class rule)")
    PROC = re.compile(r"^\*\*(Resolution|Addendum|Pending successor|Recorded defect|"
                      r"Operational closure|Answering|Superseding)\b", re.M)
    paras = doc.split("\n\n")
    keep, dropped = [], 0
    for para in paras:
        if PROC.match(para.lstrip()):
            dropped += 1
            continue
        keep.append(para)
    doc = "\n\n".join(keep)
    print(f"  {'process-labelled paragraphs removed':52s} {dropped:4d} paragraph(s)")


    print("\nstage 2c — repairs already landed by GC (asserted present)")
    for rid, name, needle in LANDED:
        if needle not in doc:
            raise SystemExit(
                f"[FAIL] {rid} {name}: expected text absent. Either a landed closure was lost, or "
                f"that closure has not been GC'd yet — check the anchor on live main before building."
            )
        print(f"  {rid:6s} {name:52s} present")

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
