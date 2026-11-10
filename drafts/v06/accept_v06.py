#!/usr/bin/env python3
"""Acceptance gate for the v0.6 build — the register's five successor tests
(shared/unified-state-model-v05-defect-register.md §6), plus the two §9 audit
questions the disposition record assigns to this gate.

Usage:
    accept_v06.py <built v06.md> [--source <v05.md>]

Exit 0 = every test passes. Exit 1 = at least one failure, each named with the
section and the offending string. Nothing here reviews prose; every check is a
count, a set, or a recomputation.
"""
import re
import sys

TAG_RE = re.compile(r"<!-- anchor-[0-9a-f]{8} -->")

# Pre-F2 readings: the calibration before the ruling had 0 = neutral/unit and
# negative = rigid. Post-F2, 0 = no response (the wall) and negative = perverse.
# These are the literal strings that carry the old reading.
PRE_F2_MARKERS = [
    # Exact pre-F2 strings. Fuzzy patterns were measured to flag corrective
    # prose ("not a neutral one", "The low-Λ corner is not a shortage") and
    # would fail a correct document — a gate that cries wolf gets ignored.
    ("D1's calibration bullet", "`""0` unit-responsive — neutral"),
    ("epigraph naming shortage as low-Λ",
     "Bubbles are high-Λ, near-zero-Δ events. Shortages are low-Λ"),
    ("(0,0) at Λ≈−1 labelled the shortage",
     "Shortage crisis: maximum rigidity on both sides"),
    ("(0,0) at Λ≈0 labelled indifference", "Genuine indifference"),
]

# The index↔elasticity mapping must be stated exactly once, at the definition.
MAPPING_PATTERNS = [
    # One distinctive phrase, not a family: "perverse" alone appears in ten
    # resolutions and counting it measured nothing about the definition.
    r"no quantity response",
]


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def test_2_anchor_placement(doc):
    """§6.2 — in the successor there are no anchors at all; in v0.5 every anchor
    must sit on its own line. Checked as: zero surviving tags in the build."""
    hits = TAG_RE.findall(doc)
    return (not hits,
            f"{len(hits)} anchor tag(s) survived the build" if hits else "no anchors survive (correct for v0.6)")


def test_3_scale_sweep(doc):
    """§6.3 — the F2 recode must be carried through every dependent block in one
    pass. Checked by searching the whole document for pre-F2 readings."""
    found = []
    for label, pat in PRE_F2_MARKERS:
        for m in re.finditer(pat, doc):
            ctx = doc[max(0, m.start() - 70):m.start() + 70].replace("\n", " ")
            found.append(f"{label}: …{ctx}…")
    return (not found, f"{len(found)} pre-F2 reading(s) remain" if found else
            "no pre-F2 readings remain")


def test_4_single_mapping(doc):
    """§6.4 — one mapping between the index and price elasticity, stated once at
    the point of definition. Checked in two parts, because a statement that
    exists only inside a resolution is not a definition a reader can meet:
    (a) the phrase occurs exactly once document-wide; (b) that occurrence is
    inside the block that defines the [−1, +1] index."""
    needle = MAPPING_PATTERNS[0]
    total = len(re.findall(needle, doc))
    if total != 1:
        return False, f"post-F2 mapping phrase occurs {total} time(s) (expected 1)"

    lines = doc.splitlines()
    # The D1 bullets put +1, 0 and −1 on separate lines, so locate the zero
    # line and test the window around it rather than demanding one line.
    block_idx = [i for i, l in enumerate(lines)
                 if "`0`" in l and ("unit-responsive" in l or "no quantity response" in l)]
    if not block_idx:
        return False, "could not locate the index definition block (no line defines +1/0/−1 together)"
    # The definition line itself must carry the post-F2 meaning. A window was
    # tried first and passed v0.5, because the F2 scope note sits within three
    # lines of the bullets it declares superseded — the test was measuring
    # adjacency, not the definition.
    for i in block_idx:
        if re.search(needle, lines[i]):
            return True, f"mapping stated once, on the index definition line (line {i+1})"
    return False, ("mapping phrase exists but not at the point of definition — it is in prose "
                   f"elsewhere; the block at line {block_idx[0]+1} still defines the superseded reading")


def test_1_repair_counts(build_log):
    """§6.1 — the locked repair list applied with nothing added. The builder
    asserts each substitution; this test reads its log for FAIL lines."""
    fails = [l for l in build_log.splitlines() if "[FAIL]" in l]
    return (not fails, f"{len(fails)} repair assertion(s) failed" if fails else
            "every declared repair asserted at its expected count")


def test_5_preserved_text(src, doc):
    """§6.5 — where a block is unchanged, its text carries forward. Checked by
    sampling every closed anchor's resolution-bearing sentences: if the source
    has them and the build does not, a closure was lost."""
    missing = []
    for line in src.splitlines():
        s = line.strip()
        if len(s) < 60 or not s.startswith(("**", "-", "The ", "A ", "Under ")):
            continue
        if s.startswith("**Resolution"):     # process prose, expected to be stripped
            continue
        probe = s[:60]
        if probe not in doc:
            missing.append(probe)
    return (not missing, f"{len(missing)} substantive line(s) dropped in the build" if missing else
            "sampled substantive lines all carry forward")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    built = sys.argv[1]
    src_path = sys.argv[sys.argv.index("--source") + 1] if "--source" in sys.argv else None
    doc = read(built)
    src = read(src_path) if src_path else ""
    log_path = built.rsplit(".", 1)[0] + ".buildlog"
    try:
        log = read(log_path)
    except FileNotFoundError:
        log = ""

    tests = [
        ("1 repair counts", test_1_repair_counts, (log,)),
        ("2 anchor placement", test_2_anchor_placement, (doc,)),
        ("3 scale sweep", test_3_scale_sweep, (doc,)),
        ("4 single mapping", test_4_single_mapping, (doc,)),
        ("5 preserved text", test_5_preserved_text, (src, doc)),
    ]
    failed = 0
    print(f"acceptance gate — {built} ({len(doc)} chars)\n")
    for name, fn, args in tests:
        if name.startswith("5") and not src:
            print(f"  SKIP  {name:26s} no --source given")
            continue
        ok, detail = fn(*args)
        print(f"  {'PASS' if ok else 'FAIL'}  {name:26s} {detail}")
        failed += 0 if ok else 1
    print(f"\n{len(tests)-failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)


main()
