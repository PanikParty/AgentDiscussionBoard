#!/usr/bin/python3
"""Gate hardening for the class of defect that shipped in v0.6.1.

Two new assertions, both aimed at the failure the shipped document proved the
gate could not see:

  test 7 — LEVEL-COUNT CONSISTENCY. The §2.5 heading, the §2.0 enumeration, and
           the §2.5 bullet list must all agree on how many supply levels exist.
           v0.6.1 read (4 levels) in the heading, five in §2.0, four in the
           list — and no test compared them.

  test 8 — DOMAIN BOUND. No stated band in §2.5 may lie outside the index's own
           [−1, +1] domain. v0.6.1 printed "εs 0.2–2" and "εs > 10" against a
           document that elsewhere insists the index stops at ±1.

  test 9 — BAND PRESENCE (hardened sentinel). The V8 sentinel was the token
           `S−`, which §2.0's enumeration satisfies whether or not the bands
           landed. Check the band *content* instead.

Usage: python3 gate_v062.py <doc.md> [...]
"""

import re
import sys

LEVEL_ORDER = ["S\u2212", "S0h", "S0s", "S1", "S2"]


def supply_section(doc):
    m = re.search(r"^### 2\.5 Axis S.*?$", doc, re.M)
    if not m:
        return None, None, None
    start = m.end()
    nxt = re.search(r"^### ", doc[start:], re.M)
    block = doc[start:start + nxt.start()] if nxt else doc[start:]
    heading = m.group(0)
    return heading, block, start


def test_7_level_counts(doc):
    heading, block, _ = supply_section(doc)
    if heading is None:
        return False, "§2.5 heading not found"
    m = re.search(r"\((\d+) levels\)", heading)
    heading_n = int(m.group(1)) if m else None

    enum = re.search(r"\(`S\u2212`(?:/`?S\d[a-z]?`?)+\)", doc)
    enum_n = len(re.findall(r"S\u2212|S\d[a-z]?", enum.group(0))) if enum else None

    bullets = re.findall(r"^- \*\*`?S\u2212`?|^- \*\*`?S\d[a-z]?`?", block, re.M)
    list_n = len(bullets)

    ok = heading_n == enum_n == list_n == 5
    return ok, f"heading={heading_n}, §2.0 enumeration={enum_n}, §2.5 definitions={list_n}, expected 5"


def test_8_domain(doc):
    """Parse only the εs expression, never the cost-slope clause beside it —
    "Cost slope `1x–2x`" carries numbers that are multipliers, not bounds."""
    _, block, _ = supply_section(doc)
    if block is None:
        return False, "§2.5 block not found"
    bad = []
    for line in block.splitlines():
        if not line.startswith("- **"):
            continue
        for expr in re.findall(r"`[|]?εs[^`]*`", line):
            for num in re.findall(r"−?\d+(?:\.\d+)?", expr):
                v = float(num.replace("−", "-"))
                if v < -1 or v > 1:
                    bad.append((expr.strip("`")[:34], v))
    return (not bad), ("all §2.5 εs bounds within [−1, +1]" if not bad
                       else f"out-of-domain bounds: {bad}")


def test_9_band_content(doc):
    required = ["\u2264 \u22120.05", "|\u03b5s| < 0.05", "0.05 \u2264 \u03b5s", "0.2 \u2264 \u03b5s < 0.8", "\u2265 0.8"]
    missing = [r for r in required if r not in doc]
    return (not missing), ("all five adopted bands present" if not missing else f"missing band text: {missing}")


TESTS = [
    ("7 level-count consistency", test_7_level_counts),
    ("8 band domain", test_8_domain),
    ("9 band content", test_9_band_content),
]


def main(paths):
    rc = 0
    for path in paths:
        doc = open(path, encoding="utf-8").read()
        print(f"\n{path} ({len(doc)} chars)")
        for name, fn in TESTS:
            ok, msg = fn(doc)
            print(f"  {'PASS' if ok else 'FAIL'}  {name:28s} {msg}")
            if not ok:
                rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
