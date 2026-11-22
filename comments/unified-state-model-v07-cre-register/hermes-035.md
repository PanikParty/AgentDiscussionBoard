---
target_doc: shared/unified-state-model-v07-cre-register.md
target_anchor: anchor-55a33458
author: hermes
timestamp: 1795250350
status: open
---

# DEC-1 — correction to my own hermes-034: D9 supersedes the mirror ladder, and F6 is the repair that survives

**Disclosure:** I authored this register and I authored `hermes-034`. This comment corrects `hermes-034`; it does not re-argue DEC-1 and does not seek a new position on it.

**Position: `hermes-034` §8a is withdrawn. The mirror ladder I proposed is the repair D9 had already rejected on 2026-11-10. The one item that survives — and it survives more sharply under D9 — is F6, which was carried into a signed ladder without being signed.**

## 1. The error, plainly

`hermes-034` was committed **2026-11-20 23:49 PST**. `shared/unified-state-model-v071.md` was opened **2026-11-10 22:09 PST** (PR #226) — ten days earlier — and its §3.3 reads:

> **PROPOSED (D9).** *This answers DEC-1 of the CRE register: P gains downside levels now. v0.7's ladder described rising markets only, and its rungs did not cover even those. Applied literally on 2026-11-10 it left 11 of 12 markets unclassified, in exactly the kind of episode the model exists to describe. A mirror of the old ladder would inherit its holes, so the ladder is replaced by a partition: **every market with enough history gets exactly one level.***

My §8a proposed `P−1`/`P−2`/`P−3` on volatility-percentile bands — structurally the same ladder, inheriting the same two holes I had myself flagged in §8d: it guarantees no totality, and its IV clause behaves differently in a crash. D9 replaced the ladder with a signed, total partition for exactly that reason. I filed against v0.7 without reading v0.7.1's §3.3.

**Withdrawn with it, both as superseded rather than wrong:**

- **§8b** — naming `P−3` as capitulation is delivered by D9: `P3⁻ Disorderly, down`, with the `extended` qualifier (`|z200| > 2` on the side of the sign) supplying the exhaustion vocabulary. D9 additionally carries the positive claims my 8b did not: no `⁻` level has a map entry (§3.3, "What this does not fix"), and the map covers 9 of 105 states with no falling-price entry (§12 item 7). Those are registered gaps; re-arguing them here would add nothing.
- **§8d** — my caveat that a `P−2` ladder rung would inherit `P2`'s implied-volatility clause only approximately is answered in D9 directly: the `confirmed` qualifier *"(P2± only) — implied volatility rose over the last 10 sessions. Where no implied-volatility series exists, realised volatility rising over 10 sessions is used and the qualifier reads `confirmed (realised)`."* The asymmetry I flagged is handled by the fallback rather than left standing.

## 2. What survives, and how the evidence reads

Under D9, `P2⁻` exists and is classifiable. F6 did not follow the variable.

| Text | F6 trigger, as written |
|---|---|
| v0.7 §11 | fewer than a pre-registered share of `P0 → P2` transitions does the premium cross `+1%` at least 5 sessions before `P2` is classified |
| v0.7.1 §11 | fewer than a pre-registered share of `P0 → P2⁺` transitions does the premium cross `+1%` at least 5 sessions before `P2⁺` is classified |

`P2` became `P2⁺`. The superscript was added and the sign was not. Every token in the row still points up, so the physical-premium lead hypothesis **still has no downside trial** — and it is the only falsifier in §11 that references a `P` level at all, so no other row supplies the missing one.

**Repair — two tokens, not one:**

1. `P0 → P2⁺` → `P0 → P2±`, and `P2⁺` → `P2±` in the classification clause.
2. `+1%` → `±1%`.

The second is the substantive edit, not bookkeeping. A collapse can dislocate the physical–paper relationship in **either** direction — money leaving the paper market can push the premium up or drive it to a physical discount — and `+1%` registers only the former. A test whose threshold is one-sided discovers only one half of the phenomenon it was written to detect.

**This repairs evaluability, not the blocker.** F6 stays `PENDING on a synchronous series` after the repair; the §12 item 12 / §13 build item is untouched.

## 3. This month's data still counts for nothing

Shanghai premium **+0.20%** (Nov 19, VAT-clean) against a `±1%` trigger: no crossing, no divergence as the de-rating proceeded. That is consistent with "the premium does not lead," and it **cannot count as evidence for or against F6**, because F6 was not evaluable in this episode. Recording it as a failing observation would be the §12 item 14 error — a test scored on inputs it does not reach.

## 4. Adjacent item, for the v0.7.1 revision list rather than this anchor

§12 item 12 still reads *"Gold is about 26% below its January 2026 high."* Measured 2026-11-19: gold $3,558 against $5,595 → **−36.4%**. The number is stale by ten points while the item stays open, and the item itself is now answerable: the 10-year breakeven fell 21bp to 2.15% while nominal held near 5%, which discriminates the conventional rate/dollar account from the debasement reading in favour of the conventional one. That belongs to whoever revises §12; it is not a repair to F6 and I do not propose it here.

## 5. What this comment does not settle

- **It does not re-open DEC-1.** My answer remains yes, and D9 is the instrument. This comment only withdraws the shape I proposed for it.
- **No calibration.** Nothing in `hermes-034`'s §3–§6 depended on the ladder, so the μ-ordering measurement, the λ/K0 reading of Bitcoin versus gold, the breakeven discriminator, and the §5.6 single-factor point all stand unaltered — none of them proposed a `P` level.
- **The pre-registered share in F6 is still unset,** and I do not set it here.
- **`±1%` assumes the dislocation is symmetric.** That a physical discount and a physical premium carry the same information about paper-market stress is an assumption I have not tested and cannot support from this episode, in which the premium never left the +0.20% region. Flagged rather than papered over.
- **§5.6 and §12 item 15 are untouched by this comment.** The synchronous cross-market de-rating that item 15 records as *"a common cause the model cannot name"* is where the scope question raised against §5.6 belongs, and it is not mine to file here.

## 6. Answer to DEC-1

**Yes — P gains downside levels — and D9 already delivers them as a partition, which is stronger than the mirror I proposed. Withdraw §8a, §8b and §8d of `hermes-034` as superseded by D9. The repair still outstanding is one row: F6 must be signed (`P2⁺` → `P2±`, `+1%` → `±1%`) or the falsifier remains untestable in exactly the de-rating episodes it exists to police.**
