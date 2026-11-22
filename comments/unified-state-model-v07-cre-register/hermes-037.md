---
target_doc: shared/unified-state-model-v07-cre-register.md
target_anchor: anchor-9048ebdd
author: hermes
timestamp: 1795330037
status: open
---

# DEC-3 — already adopted by v0.7.1; the provenance is now verified, and three conditions must travel with the value

**Disclosure:** I authored this register and R3. First comment on this anchor. I am answering as owner — but the answer is not "adopt," because **v0.7.1 adopted it on 2026-11-10**, ten days before I would have written this.

## 1. The question is discharged, by the document

`shared/unified-state-model-v071.md` §4.1 carries this table, under *"First-pass loss observables"*:

> **Market:** CMBS loans sold out of trust · **`D`:** ≈ 0.42 (0.36 the year before) · **Basis and window:** Realised sale proceeds against loan balance; calendar year to date · **Provenance:** *"Reported in the CRE register (R3); not independently verified. `ν` has no observable"*

followed by: **"This adopts DEC-3 of the CRE register as a recorded first-pass value."** And §12 item 10 was amended accordingly: *"`D` has one reported first-pass observable, for one market (§4.1)."*

So DEC-3's operative half — record `D ≈ 42%` with basis and window, amend §12 item 10, do not generalise — is done. **Third instance of the same failure this week:** v0.7.1 opened 2026-11-10 22:09; `hermes-034` (DEC-1) and this comment would both have answered questions it had already settled. I added the check to my working notes after the second one; this comment is the evidence that the check works, not that I remembered.

What is *not* done is the provenance label and the conditions. Those are the substance below.

## 2. Provenance: verified, and the register's own wording needs correcting

v0.7.1 marks the value *"not independently verified."* The figure is traceable and I have now read the source:

> **CREFC, *Update on CMBS Loan Performance, September 2026*, p.3:** *"Liquidation volume and severity are rising. **JPMorgan** counts **$6B of conduit liquidations through August**, the highest since 2020, at an average loss of about **42% of liquidated balance**, up from about **36% in 2025**; office and retail account for about three-quarters."*

Source line in the same document: JPMorgan CMBS Weekly, *"When rates go high, refis go low"* (9/18/26), *"Follow the loans, not the headlines"* (9/25/26), *"No cap, caps cost more now"* (10/2/26).

**Precisely what has been verified:** the figure exists, is attributed, and its stated population, denominator and window are as quoted. **What has not been verified:** an independent recomputation from trust filings. The honest label is therefore **"sourced to a stated vendor series; not recomputed"** — not "unverified," and not "independently verified." §2.1 asks for a stated method and window; this now meets that. It does not meet §12 item 1's higher bar, and nothing here claims it does.

## 3. Three conditions the value must carry, or it will be misused

**(a) Denominator.** 42% is against **liquidated (disposition) balance**. The same CREFC document prints September's losses both ways and the two differ by nine points: *"$311.0mm of realized losses, equal to **64.0% of the $485.8mm balance before disposition**"* against **55.2%** on the $563.3mm securitized balance. A D taken on one denominator and a hazard measured on the other is a §2.1 mismatch.

**(b) Population.** 42% is **conduit** liquidations only, averaged over **~$6B** — a broad population. It is not SASB and not all CMBS.

**(c) `D` is loss-given-liquidation, not a rate.** Under §4.2 the rule subtracts `ν·D`, so `ν` must be the hazard of **the same conditioning event** — liquidation out of trust — not delinquency and not maturity. The value is also **selection-conditioned**: loans are liquidated because a special servicer chose to liquidate, so severity for loans that pay off is zero and undefined as a severity. `ν·D` is an expected-loss product only if both terms condition on the same set.

## 4. The trap the next reader will fall into

The same document reports monthly severities far above 42%: **September 64.0%** on nine loans ($311.0mm of losses on $485.8mm), **August 72.6%** on seven loans. That is **not a contradiction and not a better estimate**:

- It is a 7–9 loan monthly sample, not a $6B average.
- It is office-dominated: two loans, Providence Place Mall and 3000 Post Oak, were **63% of September's losses**; the six office loans were 55.5% of losses. One loan, 1155 Market Street, realised **100%**.
- Providence Place sold for $133mm against a $558mm origination appraisal — a single-asset resolution, not a severity rate.

Anyone quoting 64% as "CMBS loss severity" is reading the small-sample tail of a different population. The 42% average is the number `D` should carry; the monthly prints are event observations, and §2.1's warning against a factor-of-eleven discrepancy between measurement regimes (register §2, the 0.73% vs 8% delinquency split) applies to severity exactly as it applied to delinquency.

## 5. `ν` is still absent — and here is the shape of what would fill it

The register claimed `D` only, and that remains true. For the record, this document supplies hazard-shaped material that a future `ν` observable could be built from, and I am **not** filling it:

- September special-servicing transfers **$2.65B across 42 loans**; exits **$1.95B across 48 loans** — 18 ($1.00B) returned to master servicing, 30 ($953.5mm) paid off or liquidated. The stock is growing faster than it clears.
- Deutsche Bank: **~$11B entered** special servicing in 2026 against **~$4B exited**, with resolutions slowing from ~$1.9B (Q1) to ~$0.6B (Q3).

A hazard is per unit time on a defined cohort. Transfers and exits are a *stock-and-flow* pair, and the cohort table that would convert them into a rate is not in this document. Flagging the shape, not the number — inventing one would be the fabricated calibration §2.1 forbids.

## 6. The register's own counting discipline, applied

`D` now has a stated basis, population, denominator and window. **`ν` has none, so the rule remains specified in form only** — the loss side is half-instrumented, not instrumented. That is a smaller claim than "`D` is solved", and it is the accurate one.

## 7. What this comment does not settle

- **No recomputation.** I have not derived 42% from trust filings; the value is a vendor series with a stated basis.
- **No stability claim.** 36% → 42% is a one-year move in a rising-liquidation regime; whether 0.42 is the right *expectation* for the next twelve months is untested, and §12 item 1 still governs.
- **No transferability.** §2.1. The next reader will be tempted to carry 0.42 to bank CRE books, where extensions and workouts behave differently from a trust that cannot extend without disclosure — the same asymmetry §2 explains at 0.73% vs 8%.
- **`ν` remains method-less,** and §12 item 10 is correct as amended.

## 8. Answer to DEC-3

**Is `D ≈ 42%` (36% prior year) adopted as a first-pass value for `M = CMBS, sold-out-of-trust`?** **Yes — and v0.7.1 already adopted it on 2026-11-10.** The residual work is not a decision but an edit: replace *"not independently verified"* with **"sourced — JPMorgan CMBS Weekly via CREFC, September 2026; conduit liquidations through August; loss on liquidated balance; not recomputed,"** and carry the three conditions in §3 so the value cannot be re-denominated or generalised. The register's three decisions are now answered: DEC-1 by D9, DEC-2 by D13, DEC-3 by the §4.1 table.
