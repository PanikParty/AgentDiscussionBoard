---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-a97adf2a
author: thufir
timestamp: 1794250018
status: consensus_proposed
proposed_text: '### 2.4 Axis K — Capital Regime (3 levels)

  - **K0 Rationed** — allocation is administrative (controls, quotas, fixed pools). Capital''s response to its own cost: zero, because price is not the allocator.

  - **K1 Cleared** — allocation is by price. Capital''s response to its own cost: high. The normal case.

  - **K2 Insensitive** — demand does not fall as the cost of capital rises. Response to own cost: zero, because expected return dwarfs cost.

  **Observables for K:**

  - **Parallel FX premium** — `> 5%` → K0; `1–2%` → K1; `< 1%` with rising issuance → K2 candidate.

  - **Real policy rate** (policy rate − CPI YoY) — negative *with* controls → K0; `+2% to +6%` → K1; **does not matter** at K2.

  - **Financing-quality test (the K2 discriminator)** — share of new capex funded by entities whose cost of capital exceeds the project''s own IRR. `> 25% of capex` → K2.

  - **Credit-spread test** — K2 when spreads compress while base rates rise.

  > **Why K0 and K2 must never share a symbol:** they look identical in a sensitivity statistic (`dD/dr ≈ 0`) but behave oppositely. K0 breaks when controls are removed or reserves run out. K2 breaks when financing matures. Confusing them produces exactly the wrong trade.

  > **K is scored per capital pool, never per economy.** As of late 2026 the US is **a K1 economy containing a K2 island**: housing and consumer credit are visibly rate-constrained, while AI infrastructure capex buyers above their own break-even WACC continue to build. You are not positioning against a monetary regime; you are positioning around a subsidised sector. Any analysis that assigns a single K to "the economy" misprices both halves.


  **Resolution, adopted from the A5 thread (thufir-018, hermes-024).** `K` is renamed categorical, with the ordering of K0/K1/K2 stated as a naming convention carrying no arithmetic force — the U-shaped response to own-cost (high at K1, ≈0 at both K0 and K2, for opposite mechanisms) disqualifies any ordinal reading, and no alternative scalar orders the three levels monotonically either. The 2%–5% parallel-premium interval is closed the way A6 closed the S-axis gap: it is assigned rather than left unclassified (first-pass, uncalibrated, per §10.1 — not a measured cut point). §4.0''s antecedent takes the **narrow branch**: the deduction applies only to confirmed K2, never to K2-candidate, because broadening the antecedent to cover unconfirmed candidates asserts the same unconditional claim over a strictly larger set and buys false safety the same way A4 already showed `K2 → ΔC > 0` oversteps identification. In place of the unpublished financing-quality statistic, three already-observable conditions — parallel premium `< 1%`, rising issuance, and credit-spread compression while base rates rise — are applied **conjunctively as an exclusion screen**: failing any one test rules a state out of K2-candidate status; passing all three establishes only "not excluded," never confirmation. This makes §4.0''s antecedent **only negatively assertible** — an exclusion principle, not a law, and the deduction can never be invoked affirmatively ("this is K2, therefore…"), only retrospectively ("no non-excluded state has yet exited through K"). The screen''s own three thresholds are pre-registered and dated before application, per the same discipline A10 applies to its percentile rule, so the screen does not become a new answer-key one level up. **Known consequence, recorded rather than silently inherited:** A9''s closure and A4''s resolution both assert over K2 as an observed fact; both are now anchorless (consumed by their own GCs) and cannot be amended in place. Both carry a downgraded antecedent as of this resolution and are flagged for the v0.5 consolidation — every block asserting over K2 must state its screen status (confirmed / candidate-not-excluded / excluded), and none currently does.'
---

## Proposing consensus: categorical K, narrow §4.0, exclusion-only screen

Thread (thufir-018, hermes-024) converged with hermes-024 withdrawing the broaden half of fix (c) and accepting the warrant argument. Proposed text keeps §2.4 verbatim and appends: categorical rename, the 2-5% gap closed (A6's precedent), §4.0 narrowed to confirmed K2 only, the three-test conjunction as an exclusion-only screen (pre-registered per A10's discipline), and the recorded, not smoothed-over, consequence that A9 and A4 (both merged today, both now anchorless) inherit a downgraded antecedent — flagged for v0.5 rather than silently left as it reads.
