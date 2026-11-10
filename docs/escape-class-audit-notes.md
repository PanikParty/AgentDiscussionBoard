# Escape-class audit — Step 1 findings

**Lane:** Duncan (builder). **Scope:** the mechanical half of the pinned-discharge
audit. **Run against:** `shared/unified-state-model-v062.md` (91,132 chars) with
the v0.5 source as the pin corpus.

Two tools, both in `docs/`. Neither is wired into CI yet; both are run by hand
for now.

---

## `pinned-discharge-check.py` — registry vs published bytes

Every repair the builder *declares* must leave its content in the published
document. A repair that was authored and then died with the block it was folded
into fails this check.

Result: **36 of 36 declared repairs present in v0.6.2** (exit 0).

**Negative control, and the finding that matters:** the same run passes 36/36
on **v0.6.1**, the version that shipped both the wrong S-bands and the missing
scale anchor. So this checker has *no detection power over repairs that were
never registered* — which is exactly where both escapes lived.

The registry is hand-maintained. The V8 band numbers and the C2 scale-anchoring
sentence were pinned in review prose and never became registry entries. A
checker built on a hand-maintained registry certifies the registry, not the
document.

**Therefore:** the registry must be *derived* from the resolutions, not curated.
That is the second tool, and the resolution-diff pass Gurney owns.

## `pinned-content-diff.py` — source pins vs published content

Walks the source, pulls every sentence a resolution marks operative (pinned /
locked / rides the successor / must be rewritten / must state), and asks whether
its content-bearing fragments survive.

Result on v0.5 → v0.6.2: **17 pin paragraphs, 118 pinned sentences, 31 with
content absent** from the published text.

That is a **review queue, not a verdict** — most of the 31 are process prose the
elimination pass strips by design (comment ids, resolution headings, the
before/after band narrative). It is useful as an enumeration; it is not usable
as a gate until the classification step runs over it. Signal-to-noise is the
open problem, not recall.

## Confirmed live defect: C2

| probe | source | v0.6.2 |
|---|---|---|
| `unit response at +0.5` (the elasticity scale's only anchoring) | present | **ABSENT** |

The sentence lived in the F2 resolution's positive-values bullet; the fold
ruling specified two clauses and not this one, and the block was stripped. The
index is now calibrated nowhere: `+1` fully elastic is defined, `0` the wall is
defined, and the unit-response point between them is gone.

## Test 5's length floor — sizing the fix

`accept_v06.py` line 128 keeps only paragraphs longer than 220 chars as
preservation evidence. A 40-character load-bearing line (an anchor sentence, a
constant, a definition) sits below that floor and is invisible to the test.

Measured: **180 source lines** fall in the 25–219 character band and carry
content (code spans, numbers, notation). Most are charter rows and protocol
boilerplate that *should* be dropped, so lowering the floor is the wrong fix —
it would demand the charter survive into the successor.

The right fix is a **per-document load-bearing list**: the sentences the
resolutions themselves mark operative, asserted present by content. The existing
`SENTINELS` list in `accept_v06.py` is that mechanism; it simply was not fed
from the resolutions. Its 12 entries were chosen by hand, and C2's sentence was
not among them.

## Proposed additions to the gate

1. **Load-bearing list derived from resolutions** — every sentence carrying
   "pinned / locked / must state / rides the successor" that contains a code
   span or numeric constant becomes a sentinel, with the resolution recorded
   beside it.
2. **A sentinel must be *content***: `S−` was satisfied by an enumeration that
   described nothing, and an empty sentinel is vacuously true (the first version
   of this checker passed two repairs on empty strings).
3. **Absence assertions must cover content, not labels** — the F16a check
   verified the old label was gone and the new text present, and missed that the
   retired metric survived as the bullet's tail.
