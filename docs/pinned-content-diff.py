#!/usr/bin/python3
"""Step 1, second half: pinned-content diff.

The registry-based checker (pinned_discharge_check.py) can only verify repairs
someone remembered to register. Twice tonight the escape was in the registry
itself: the V8 band numbers and the C2 scale-anchoring sentence were pinned in
review prose and never became registry entries, so no amount of checking caught
them — an outside audit did.

This script inverts the direction. It walks the SOURCE document, pulls every
sentence that a resolution marks as operative (pinned / locked / rides the
successor / must be rewritten / must state), and asks whether that content —
its distinctive phrases, not its prose — survives in the published text.

Every hit is either a genuine loss or a deliberate rewrite; the output is a
review queue, not a verdict.

Usage: pinned_content_diff.py <source.md> <published.md>
"""

import re
import sys

PIN = re.compile(
    r"pinned|locked|rides the successor|must be rewritten|rewritten in|"
    r"must state|must carry|must be carried|is rewritten",
    re.I,
)

# Only content-bearing fragments are testable this way: a phrase with a code
# span, a number, or a technical term. Bare connectives ("and so on") match
# everywhere and mean nothing.
CONTENT = re.compile(r"`[^`]{3,}`|\d+(?:\.\d+)?%?|ε[ds]|[ΔΛΣΓ]|S[−\-0-9]|K[0-2]")

STOP = set("the a an and or of to in for on with that this it is are be by as at from".split())


def phrases(text):
    """Distinctive fragments: code spans and numeric/notation tokens, in order."""
    return re.findall(r"`([^`]{3,})`|\b(\d+(?:\.\d+)?%?)\b", text)


def norm(t):
    t = t.replace("`", "").replace("**", "")
    for a, b in (("−", "-"), ("–", "-"), ("—", "-"), ("’", "'")):
        t = t.replace(a, b)
    return re.sub(r"\s+", " ", t).strip()


def main(src_path, pub_path, min_len=25):
    src = open(src_path, encoding="utf-8").read()
    pub = norm(open(pub_path, encoding="utf-8").read())

    paras = [p for p in src.split("\n\n") if PIN.search(p)]
    print(f"source pin paragraphs: {len(paras)}")

    checked = missing = 0
    for para in paras:
        # sentence-ish split, keeping code spans intact
        for sent in re.split(r"(?<=[.;:])\s+(?=[A-Z`(])", para):
            s = sent.strip()
            if len(s) < min_len or not CONTENT.search(s):
                continue
            checked += 1
            # test the sentence's own code spans and numbers, not its prose
            frags = [f[0] or f[1] for f in phrases(s)]
            frags = [f for f in frags if len(f) >= 4 and f.lower() not in STOP]
            if not frags:
                continue
            hits = [f for f in frags if norm(f) not in pub]
            if hits:
                missing += 1
                print(f"\n  ABSENT  {hits[:3]}")
                print(f"    from: {s[:190]}")

    print(f"\nchecked {checked} pinned sentences; {missing} have content absent from the published text")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
