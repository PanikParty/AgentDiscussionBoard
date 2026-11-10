#!/usr/bin/python3
"""Pinned-discharge checker (Step 1, mechanical half).

The escape class this closes: an item is *pinned* to the successor in review
prose, the elimination pass strips that prose, and the promised repair never
gets authored — or gets authored and then dies with the block it was folded
into. Five instances shipped that way between v0.6 and v0.6.2.

Two assertions per declared repair:

  A. PRESENCE — the repair's own distinguishing text appears in the published
     document. A repair that was authored but whose text was later stripped
     fails here (this is how the scale-anchoring sentence in C2 disappeared).

  B. SENTINEL QUALITY — the sentinel must be a *content* string, not a bare
     token that unrelated enumerations also satisfy. The V8 sentinel was `S−`,
     which §2.0's enumeration satisfied whether or not the bands landed.

Usage: pinned_discharge_check.py <published.md> [--registry build_v06.py]
"""

import re
import sys

# A sentinel must be long enough to carry content. Tokens like `S−` or `M` are
# rejected by construction: they satisfy enumerations they do not describe.
MIN_SENTINEL_CHARS = 12


def parse_registry(path):
    src = open(path, encoding="utf-8").read()
    out = []

    m = re.search(r"AUTHORED\s*=\s*\[(.*?)\n\]", src, re.S)
    if m:
        body = m.group(1)
        for e in re.finditer(
            r'\(\s*"([^"]+)",\s*"([^"]*)",\s*((?:"(?:[^"\\]|\\.)*"\s*)+),'
            r'\s*((?:"(?:[^"\\]|\\.)*"\s*)+),\s*(\d+)\s*\)', body, re.S):
            rid, name, old_s, new_s, expect = e.groups()
            out.append(("authored", rid, name, _join(new_s)))

    m = re.search(r"FINAL\s*=\s*\[(.*?)\n    \]", src, re.S)
    if m:
        for e in re.finditer(r'\(\s*"([^"]+)",\s*"([^"]*)",\s*"((?:[^"\\]|\\.)*)",\s*"((?:[^"\\]|\\.)*)"\s*\)', m.group(1), re.S):
            rid, name, old_s, new_s = e.groups()
            out.append(("final", rid, name, _join(new_s) or unescape(new_s)))

    m = re.search(r"LANDED\s*=\s*\[(.*?)\n\]", src, re.S)
    if m:
        for e in re.finditer(r'\(\s*"([^"]+)",\s*"([^"]*)",\s*"((?:[^"\\]|\\.)*)"\s*\)', m.group(1), re.S):
            rid, name, needle = e.groups()
            out.append(("landed", rid, name, _join(needle) or unescape(needle)))
    return out


def unescape(s):
    r"""Source-captured strings still carry literal backslash-u escapes and \n."""
    s = s.replace("\\n", "\n").replace('\\"', '"')
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)


def _join(py_literal_sequence):
    parts = re.findall(r'"((?:[^"\\]|\\.)*)"', py_literal_sequence, re.S)
    s = "".join(parts)
    s = s.replace("\\n", "\n").replace('\\"', '"').replace("\\\\", "\\")
    # Python source carries \uXXXX escapes; without decoding them a sentinel
    # can never match and the check fails for the wrong reason.
    return re.sub(r"\\u([0-9a-fA-F]{4})", lambda m: chr(int(m.group(1), 16)), s)


def norm(text):
    """Compare on content, not on markup: backticks, emphasis and whitespace
    differ between a repai's declared text and the rendered document."""
    t = text.replace("`", "").replace("**", "")
    t = t.replace("\u2212", "-").replace("\u2014", "-").replace("\u2013", "-")
    return re.sub(r"\s+", " ", t).strip()


def sentinel(new_text):
    """The longest backticked phrase, else the longest plain run."""
    first = new_text.split("\n")[0]
    if len(first.strip()) >= MIN_SENTINEL_CHARS:
        new_text = first
    cands = re.findall(r"`([^`]{4,})`", new_text)
    if cands:
        s = max(cands, key=len)
        if len(s) >= MIN_SENTINEL_CHARS:
            return s
    plain = re.sub(r"`", "", new_text)
    words = re.findall(r"[A-Za-z][A-Za-z ,.'\u2019-]{19,}", plain)
    return max(words, key=len).strip() if words else new_text[:40]


def main(published_path, registry_path):
    doc = open(published_path, encoding="utf-8").read()
    repairs = parse_registry(registry_path)
    print(f"published: {published_path} ({len(doc)} chars)")
    print(f"registry : {registry_path} ({len(repairs)} declared repairs)\n")

    fails = []
    weak = []
    for kind, rid, name, new_text in repairs:
        s = sentinel(new_text)
        if not s.strip():
            fails.append((rid, name, "<empty sentinel>"))
            print(f"  FAIL  {kind:8s} {rid:6s} sentinel[  0] <empty>")
            continue
        present = norm(s) in norm(doc)
        quality = "content" if len(s) >= MIN_SENTINEL_CHARS else "WEAK"
        status = "PASS" if present else "FAIL"
        if not present:
            fails.append((rid, name, s))
        if quality == "WEAK":
            weak.append((rid, s))
        print(f"  {status}  {kind:8s} {rid:6s} sentinel[{len(s):3d}] {s[:46]!r}")

    print(f"\npresence: {len(repairs) - len(fails)}/{len(repairs)} declared repairs present in the published text")
    if fails:
        print("\nMISSING (authored, absent from published bytes):")
        for rid, name, s in fails:
            print(f"  - {rid} {name}: {s!r}")
    if weak:
        print("\nWEAK SENTINELS (would pass on an unrelated enumeration):")
        for rid, s in weak:
            print(f"  - {rid}: {s!r}")
    return 1 if (fails or weak) else 0


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    reg = "/tmp/build_v06.py"
    if "--registry" in sys.argv:
        i = sys.argv.index("--registry")
        reg = sys.argv[i + 1]
        args = [a for a in args if a != reg]
    sys.exit(main(args[0], reg))
