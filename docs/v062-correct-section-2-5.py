#!/usr/bin/python3
"""v0.6.1 -> v0.6.2 correction: §2.5's supply taxonomy.

The five-band repair adopted in the V8 closure never landed in the body text.
It lived in resolution-labelled prose, which the v0.6 elimination pass strips by
design, and the §2.5 range update was pinned without an authored repair — the
same failure class as F2a/F2b/F16a, and the first one that reached a published
document.

Symptom in the published text: §2.5 headed "(4 levels)", listing
S1 = eps 0.2-2 and S2 = eps > 10, both outside the document's own [-1,+1]
domain, while §2.0 enumerates five levels and §14 claims the fifth. The
document's own S2 example (eps_s,R ~ +1.0) satisfies the adopted band (>= 0.8)
and violates the printed one (> 10).

Run from the repo root:  python3 docs/v062-correct-section-2-5.py <path>
"""

import sys

OLD_HEADING = "### 2.5 Axis S \u2014 Supply Regime (4 levels)"

OLD_BLOCK = """- **S0h Hard wall** \u2014 cannot expand within the horizon at any price (no capacity, no land, no permit, no queue position). `\u03b5s \u2248 0`. Cost slope undefined \u2014 no price clears.
- **S0s Steep** \u2014 expandable, but marginal cost rises more than 3x to do so. `\u03b5s < 0.2`. Cost slope `> 3x`.
- **S1 Elastic** \u2014 expandable at roughly linear cost. `\u03b5s 0.2\u20132`. Cost slope `1x\u20132x`.
- **S2 Unbounded** \u2014 near-zero marginal cost; copies are free. `\u03b5s > 10`. Cost slope `\u2248 0`."""

NEW_HEADING = "### 2.5 Axis S \u2014 Supply Regime (5 levels)"

NEW_BLOCK = """- **`S\u2212` Perverse** \u2014 `\u03b5s \u2264 \u22120.05`: quantity *contracts* as price rises \u2014 capacity is destroyed by the price signal (exit, cannibalisation, foreclosure). A distinct register, not a degree of rigidity; it is where the busts live. Cost slope undefined \u2014 the signal moves the wrong way.
- **`S0h` Hard wall** \u2014 `|\u03b5s| < 0.05`: cannot expand within the horizon at any price (no capacity, no land, no permit, no queue position). Cost slope undefined \u2014 no price clears.
- **`S0s` Steep** \u2014 `0.05 \u2264 \u03b5s < 0.2`: expandable, but marginal cost rises more than 3x to do so. Cost slope `> 3x`.
- **`S1` Elastic** \u2014 `0.2 \u2264 \u03b5s < 0.8`: expandable at roughly linear cost. Cost slope `1x\u20132x`.
- **`S2` Unbounded** \u2014 `\u03b5s \u2265 0.8` (the index maximum is `+1`): near-zero marginal cost; copies are free. Cost slope `\u2248 0`.

The five bands are disjoint and exhaustive over the index's `[\u22121, +1]` domain: `S\u2212` below `\u22120.05`, `S0h` the zero band, then three positive bands. Every `\u03b5s` classifies to exactly one level."""

EDITS = [
    ("2.5 heading level count", OLD_HEADING, NEW_HEADING),
    ("2.5 five-band list", OLD_BLOCK, NEW_BLOCK),
    ("\u00a79 criterion 3 axis arity", "the 4-level axis is over-specified", "the 5-level axis is over-specified"),
]


def main(path):
    doc = open(path, encoding="utf-8").read()
    before = len(doc)
    for name, old, new in EDITS:
        n = doc.count(old)
        if n != 1:
            sys.exit(f"[FAIL] {name}: expected 1 occurrence, found {n}")
        doc = doc.replace(old, new)
        print(f"  {name:40s} 1 swap")
    open(path, "w", encoding="utf-8").write(doc)
    print(f"\n{before} -> {len(doc)} chars ({len(doc) - before:+d})")


if __name__ == "__main__":
    main(sys.argv[1])
