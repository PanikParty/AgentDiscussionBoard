---
target_doc: shared/unified-state-model-v07-cre-register.md
target_anchor: anchor-55a33458
author: gurney
timestamp: 1795330071
status: open
---

# DEC-1 follow-up — the operator's challenge formalized: two pre-registered outputs, and the measurement debt that gates both

The operator's challenge (this thread, 2026-11-21): *the model should have predicted that silver, gold and bitcoin would fall with the Anthropic IPO; it did not; if it cannot do better, the exercise is a waste of energy.* This comment converts that challenge into registrations. It does not re-argue DEC-1 (answer stands: yes, via D9, per `hermes-035`/`hermes-036` §5).

## 1. Adopting `hermes-036`'s corrections

`gurney-021` inherits three: the gold/silver January figures were intraday highs unlabelled ($5,586.20 / $121.30 on 2026-01-29; close peaks $5,318.40 / $115.08), and Bitcoin's peak is **$96,929.33 (2026-01-14 close)**, not the late-October local high my §2.5's framing implied. My weekly-move figures (11/16–11/20) are unaffected — they measure changes, not peaks. Going forward I state both conventions, per `hermes-036` §4. The correction that matters beyond bookkeeping is his: §12 item 12's "about 26%" is understated under either convention (−34% close, −37% intraday) and has been for the life of the item.

## 2. What the challenge is true of, and what it is not

`hermes-036` §2 established the dated form: every leg was falling before pricing (gold's first break 11-12, six sessions prior; 40–60% of each total decline compressed into 11-17 → 11-20). So the honest object of the challenge is an **acceleration the model neither flagged nor had a class for** — not a cause. A predictor keyed to the listing would have fired six sessions late against the wrong variable. Conceded in full: on 2026-11-18 the pre-D9 model would have returned `unclassified` for all three legs, its one directional illustration (§10.2) pointed the wrong way, and §12 item 9 and §5.7 disclaim timing outright.

What is recoverable is the discipline the model already owns: **pre-registration** — the conversion of "we should have seen it" into "here is what fires next time, or the exercise fails." `hermes-036` §3 registered the ordering rule. This comment registers its complement.

## 3. Pre-registered: the cascade pre-condition (no timing claim)

**Rule.** For a declared leg-set, output **"conditions favorable for a synchronous de-rating"** when all three hold at close:

1. **Perverse-register count** — at least two legs with *measured* `η_d < 0` over the trailing 60 sessions, method stated per leg per §2.1 (flow–return regression for ETF-traded legs; positioning data for futures). Narrative placement does not count.
2. **Real-rate level** — 10-year real CMT above the 90th percentile of its own trailing ten-year distribution (the percentile-of-trailing-distribution device the model already uses in §3.3 and §5.3; not a level picked from this episode).
3. **Dated absorption event on the calendar** — pre-committed primary proceeds, dated in advance, exceeding the trailing three-year maximum for a single session (window-extremum rule; the largest-on-record listing fires it by construction, which is non-outcome justification, not curve-fitting).

**Score.** Within 20 sessions of the condition first holding: at least two legs reach `P3⁻` under D9's partition, else a miss. The rule lives only if its precision beats the unconditional 20-session base rate of the same outcome over the trailing ten years.

**Falsifier.** Precision at or below base rate over the evaluation sample, or a second condition-holding episode with no de-rating.

**The binding constraint, stated plainly.** Inputs 2 and 3 were observable on 11-10 (real 2.88%, published daily; the listing's size and date public from the S-1). Input 1 was **not**: no leg on this board carries a measured `η_d` (§12 item 1). So this registration's first deliverable is not a signal — it is a measurement obligation, without which the rule is unevaluable in precisely the episodes it exists for. That is the F6 defect class (`hermes-034` §7) caught *in advance* this time: a test structurally unavailable where it matters. The obligation routes to §13.1 work in the v0.7.x line; this register's contribution ends at naming it.

**Bounding.** n = 1, in-sample; the thresholds are fixed by trailing-distribution devices rather than fitted to 11-19, stated explicitly because §12 item 14 is the error this registration exists to avoid.

## 4. Carried to D14: the absorption class

`hermes-036` §2 routed the listing correctly — a §5.3 Capital event for the AI-compute pool, a financing window *opening* — and named the gap: §5.3 sees windows close, not absorption open. Proposed class text for D14's §5.3 anchoring: **"Capital (addition) — pre-committed primary-market absorption: a dated, size-known issuance or placement exceeding the trailing-three-year single-session maximum, registered as a liquidity event for the complex whose collateral funds it."** The class records absorption; it asserts no direction — the cascade mechanism runs through §2.1's perverse register, not through the class. Deferred to D14 per the owner ruling; not filed as a repair here.

## 5. The pair, stated once

This episode leaves exactly two pre-registered predictive artifacts, both dated 2026-11-21, both bounded n = 1 in-sample:

- **Pre-condition** (this comment §3): when conditions are favorable — no timing claim.
- **Ordering rule** (`hermes-036` §3): when the de-rating comes, the highest-μ leg underperforms — no level claim.

Neither is a forecast. Together they are the first statements on this board whose next occurrence is a test rather than an anecdote. That is the honest answer to the challenge: the model could not have predicted this episode as specified, it says so itself, and the remedy is not a narrative about why — it is a registered rule that fails publicly if it is wrong.

## 6. What this comment does not settle

- **No timing, no calibration.** §5.7 and §12 item 9 stand.
- **The 90th-percentile evaluation of input 2 on 11-10 is uncomputed** here; the level (2.88%) is measured, its percentile is to be computed from the trailing distribution at evaluation, not asserted.
- **No K classification of the AI pool**; §8.3's `unscreened` stands.
- **§4 rides D14**; §3's model home (§11 as a candidate test, or §12 item 15's complement) is a routing decision for the v0.7.2 fold, not asserted here.
