#!/usr/bin/python3
"""Apply the seven owner-specified corrections to the PUBLISHED v0.6 document.

Thufir filed and merged the NEW TOPIC (PR #210, 467b531) before Gurney's second
checklist round reported, so the corrections land against the published file
rather than the builder output. Every swap is asserted count-1; any miss aborts
before a byte is written.

Run from the repo root:  python3 /tmp/v06_fix7.py
"""

import sys

DOC = "shared/unified-state-model-v06.md"

EDITS = [
    # 1 — discharged process asserting a false present: (1)/(2) have both landed.
    (
        "1 V7 sequence asserts pending state",
        "**V7's answer, stated as a sequence rather than a single verdict.** The screen is run as soon "
        "as (1)/(2) above land \u2014 the tests are already specified and already described as the operative "
        "classification in this very resolution. Until then, the document's own `unscreened` label on the "
        "live AI capital pool (\u00a72.4's observables block) remains correct.",
        "**The screen has not yet been run against a live pool.** Its three tests are specified and are the "
        "operative classification; until a run exists, the document's `unscreened` label on the live AI "
        "capital pool (\u00a72.4's observables block) remains correct.",
    ),
    # 2 — v0.5-consolidation clause is discharged; "none currently does" is now false.
    (
        "2 v0.5 consolidation flag",
        "are flagged for the v0.5 consolidation \u2014 every block asserting over K2 must state its screen "
        "status (confirmed / candidate-not-excluded / excluded), and none currently does.",
        "are flagged in this revision \u2014 every block asserting over K2 states its screen status "
        "(confirmed / candidate-not-excluded / excluded).",
    ),
    # 2b — board jargon a published reader cannot resolve.
    (
        "2b GC jargon",
        "(consumed by their own GCs)", "(sitting in the review record)",
    ),
    # 3 — version tag in the amendment phrase.
    (
        "3 amendment version tag",
        "The trap bullet that follows now carries the amendment (v0.5): the elastic-supply assumption is "
        "stated in the text.",
        "The trap bullet that follows carries the stated elastic-supply assumption in the text.",
    ),
    # 4 — "charter" is board vocabulary.
    ("4 charter's choice", "The charter's choice", "The design choice"),
    # 5 — half review history, half redundant with the adjacent bullet.
    (
        "5 parenthetical review history",
        " (Maximum rigidity is the `\u039b \u2248 0` corner on the F2 calibration; this cell carried that "
        "label under the superseded one.)",
        " (Maximum rigidity is the `\u039b \u2248 0` corner.)",
    ),
    # 6 — calibration reference in a cell gloss.
    (
        "6 cell gloss calibration",
        "\u00a71.2's \"captive buyers at a hard wall\" recomputes to this corner under the F2 calibration.",
        "\u00a71.2's \"captive buyers at a hard wall\" reads at this corner.",
    ),
    # 7 — reviewer attribution; the coordinate itself stays dropped. The
    # "No in-domain replacement is printed here:" sentence a line later already
    # carries that half of the ruling, so this edit must not restate it.
    (
        "7 reviewer attribution",
        "The reviewer's first-pass corrected coordinate `(+0.5, \u22121.8)` is **dropped, not carried as an "
        "illustration**:",
        "The obvious correction `(+0.5, \u22121.8)` is **dropped, not carried as an illustration**:",
    ),
    (
        "7b calibration phrase",
        "under the F2 calibration (\u00a72.1 resolution)",
        "under the adopted calibration (\u00a72.1)",
    ),
]


def main():
    doc = open(DOC, encoding="utf-8").read()
    before = len(doc)
    for name, old, new in EDITS:
        n = doc.count(old)
        if n != 1:
            sys.exit(f"[FAIL] {name}: expected 1 occurrence, found {n}")
        doc = doc.replace(old, new)
        print(f"  {name:48s} 1 swap")
    open(DOC, "w", encoding="utf-8").write(doc)
    print(f"\n{before} -> {len(doc)} chars ({len(doc) - before:+d})")


if __name__ == "__main__":
    main()
