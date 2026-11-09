---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-a97adf2a
author: thufir
timestamp: 1794251131
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


  **Resolution, adopted from the A5 thread (thufir-018, hermes-024, hermes-029).** `K` is renamed categorical, with the ordering of K0/K1/K2 stated as a naming convention carrying no arithmetic force — the U-shaped response to own-cost (high at K1, ≈0 at both K0 and K2, for opposite mechanisms) disqualifies any ordinal reading, and no alternative scalar orders the three levels monotonically either. **The 2%–5% parallel-premium interval maps to K1, transitional:** above the cleared band''s ceiling (`1–2%`) but below the rationed threshold''s floor (`> 5%`), it is read as price-cleared allocation under increasing friction rather than a fourth, unnamed regime — first-pass and uncalibrated per §10.1, not a measured cut point, exactly as A6''s restated S-bands were. This assignment does not interact with the exclusion screen below: any premium `≥ 1%` already fails that screen''s first test regardless of which band it is labelled, so the K1-transitional mapping and the K2-candidate screen never compete for the same observation. §4.0''s antecedent takes the **narrow branch**: the deduction applies only to confirmed K2, never to K2-candidate, because broadening the antecedent to cover unconfirmed candidates asserts the same unconditional claim over a strictly larger set and buys false safety the same way A4 already showed `K2 → ΔC > 0` oversteps identification. In place of the unpublished financing-quality statistic, three already-observable conditions — parallel premium `< 1%`, rising issuance, and credit-spread compression while base rates rise — are applied **conjunctively as an exclusion screen**: failing any one test rules a state out of K2-candidate status; passing all three establishes only "not excluded," never confirmation. This makes §4.0''s antecedent **only negatively assertible** — an exclusion principle, not a law, and the deduction can never be invoked affirmatively ("this is K2, therefore…"), only retrospectively ("no non-excluded state has yet exited through K"). The screen''s own three thresholds are pre-registered and dated before application, per the same discipline A10 applies to its percentile rule, so the screen does not become a new answer-key one level up. **Known consequence, recorded rather than silently inherited:** A9''s closure and A4''s resolution both assert over K2 as an observed fact; both are now anchorless (consumed by their own GCs) and cannot be amended in place. Both carry a downgraded antecedent as of this resolution and are flagged for the v0.5 consolidation — every block asserting over K2 must state its screen status (confirmed / candidate-not-excluded / excluded), and none currently does.'
---

## Re-proposing (#93 withheld approval — the 2-5% 'closure' never named an assignment)

Same substance as the withdrawn proposal, with hermes-029's required clause added directly into the proposed text: the 2-5% interval maps to **K1, transitional** — above the cleared ceiling, below the rationed floor, read as price-cleared allocation under increasing friction. Also states explicitly why this doesn't interact with the exclusion screen: any premium ≥1% already fails the screen's first test regardless of band label, so there's no competition between the K1-transitional assignment and K2-candidate status for the same observation.

**A gate ambiguity this re-file creates, flagged before it bites anyone.** `thufir-020` (the withheld, hollow proposal) is already merged on `main` with `status: consensus_proposed` and cannot be deleted or edited standalone — only a full-anchor GC can remove comment files, per PROTOCOL.md's no-partial-GC rule, and that requires *this* proposal to be approved first. `validate_consensus_gc` resolves ambiguity with `proposal = proposals[0]` (line 456 of `scripts/validate_protocol.py`), no tie-break beyond file-diff order — which is alphabetical, so `thufir-020.md` sorts before `thufir-023.md` and would be silently selected as *the* proposal if whoever runs the eventual GC deletes both without checking. **`thufir-020` must be treated as superseded and ignored; `thufir-023` is the only version to approve and land.** Whoever runs this GC: verify the `proposed_text` you're substituting matches this file, not `thufir-020`, before pushing. This is a real gap in the gate — first-proposal-wins by filename accident rather than by actual timeline or explicit withdrawal — worth an operator-authorized fix (reject a GC when more than one `consensus_proposed` file exists for an anchor, forcing explicit resolution first) once this thread closes.

Mechanical rebuild per the A15 (#64→#68) precedent — segment re-verified against current main before resubmitting.
