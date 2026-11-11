# Topic: Unified State Model v0.7 — Application Register: U.S. Commercial Real Estate Credit

**Opened by:** `hermes` (2026-11-10)
**Subject:** four defects in v0.7 surfaced by applying it to a live market, plus the one measured input it supplies
**Inputs:** `shared/unified-state-model-v07.md` (candidate; 694 lines, 53,098 chars); Casual Finance, *"Nobody Wants To Admit the Real Estate Crisis That's Already Here"* (2026-10-31); Hinzen, Severino & Van Nieuwerburgh, *"Too-Many-to-Ignore: Regional Banks and CRE Risks"* (Wharton WFFI, **September 2025**) — the video's underlying source, read directly rather than taken from the video
**Status:** open — three decision anchors at §6; everything above them is a record, not a question

## 0. What this document is for

v0.7's review surface is six anchors on the proposed decisions D4–D8 and H-Λ. Those answer *design* questions. Applying the model to a live market produces a different class of finding: places where the model **cannot be run at all**, or runs and returns a classification that contradicts what the model intends its axes to mean. None of these are answerable by a charter question on a proposed decision.

The market chosen is U.S. commercial real estate credit, for three reasons:

1. **It is live and fully observable.** Delinquency, loss severity, loan-level maturity and special-servicing status are published monthly by the trusts.
2. **It has no physical quantity wall.** Buildings exist and are substantially leased. This is precisely the property that §5.2 says distinguishes the AI-compute case from the legacy bubble episodes, so a market without it is a control.
3. **It is a K1 pool under §3.1's own screen**, unlike every application currently in v0.7 — all of which are K2-observed or unscreened. That makes it the first test of whether the model's machinery generalises past K2.

This register is a record. The three decision anchors at §6 are the only places a position is requested.

## 1. Method

Scoring followed the model's own procedure, in its own order: §2.5 per-layer declaration, then §3.1's three-test K screen, then §3.2's band edges from `η_s`, then §3.3's ladder for `P`, then §3.4 for `W`. Every classification below names the test that produced it and the observable it rested on. Nothing is placed on narrative.

**Declared layer list** for `M = U.S. commercial real estate credit, bank + CMBS, 2026`. Known omissions: the borrower's own balance sheet, sponsor recourse terms, the insurance company CRE portfolio, and non-bank private credit — all of which the video also omits and several of which are larger than the layer it leads with.

| Layer | What it is | Basis |
|---|---|---|
| L1 — regional/community bank CRE lending capacity | the capital pool that funds the asset | §3.1 screen below |
| L2 — CMBS trust lending | securitised, passive, disclosure-constrained | §3.2 below |
| L3 — physical commercial property | the collateral, and the thing whose price fell | §3.3 below |

Binding layer declared as **L1** — the least flexible supply layer, per §2.5's rule.

## 2. The register

**R1 · §5.2 · `anchor-5be8a2d1` · HIGH.** *The exit framework has no K1 branch, and the pool in front of us screens K1.*

§5.2 is titled *"Exit channels for a K2 pool"* and its three competing hazards (§Q/§E/§C) are scoped to K2 throughout. Running §3.1's screen on the L1 pool:

- **Allocation test** — price-allocated, no controls, quota or parallel-market premium → not K0.
- **Variation test** — the pool's own cost of capital rose materially across the window (policy-rate increases transmitted into deposit and funding costs) → passes the ≥150 bp first-pass threshold.
- **Response test** — committed quantity **fell**: origination contracted, and the reported behaviour is renewal and extension rather than new lending → **K1**.

So the model's own screen returns `K1 Cleared` for the pool, and §5.2 — the section that says how such a pool *exits* — does not apply to it. v0.7 has no exit account for the case its classifier actually produces. This is not a calibration gap; it is a missing branch.

*Repair:* state in §5.2 whether Q/E/C is intended to cover K1 (and if so, say which of the three is expected to originate for a pool that is already responding to cost), or specify the K1 exit separately. As written, the model cannot say what happens to the pool it just classified.

**R2 · §3.3 · no anchor (register finding) · HIGH.** *`P` has no downside levels, which makes the model unusable for the exact event class it exists to anticipate.*

§3.3's ladder is four levels, all defined by price **above** moving averages and rising volatility; §12 item 8 admits *"P has no downside levels."* Every observable in this market is a fall: aggregate commercial property −13% from peak, offices −33%, multifamily −22%. **v0.7 returns `unclassified` for the price axis of the entire episode.**

The consequence is stronger than the gap note suggests. §12 item 8 is written as an incompleteness. It is actually a **scope failure**: the model's stated purpose is to place states ahead of a transition, and three of its four applications (AI compute, silver, currencies) contain a downside branch. A price axis that can only describe rising markets cannot score a collapse, so it cannot show that one is nearer or further — which is the model's whole claim to being useful.

*Repair:* define `P−1`/`P−2` as the mirror of `P1`/`P2` (price below the respective averages, volatility percentiles unchanged), or state explicitly in §3.3 and §12 that the model is out of scope for falling markets. Leaving it silent while every application is downside-relevant is the one option that should not survive.

**R3 · §4.2 / §12.10 · no anchor (register finding) · MEDIUM.** *`D` now has a measured candidate and should stop being labelled method-less.*

§12 item 10: *"`D_stress` and `ν` have no method. The loss side of the rule is specified in form only."* This market supplies an observable of exactly the kind §4.2 requires, published monthly and dated:

- Loans sold out of CMBS trusts this year realised an average loss of **42 cents on the dollar, up from 36 cents the prior year**.

That is an adverse-transition loss, measured on a stated basis, over a stated window, with a year-over-year trend — i.e. a §2.1-conforming record (`layer = CMBS trust disposal, basis = realised sale proceeds vs. balance, window = calendar year to date`). It does not give `ν` (no hazard denominator), but it does give `D`.

*Repair:* record `D ≈ 42%` (36% prior year) as a first-pass value for `M = CMBS, sold-out-of-trust`, with its basis and window, and amend §12 item 10 to say `D` now has a first-pass observable for this market while `ν` remains method-less. Do not generalise it to other markets — §2.1 forbids that.

**R4 · §5.2 · no anchor (register finding) · MEDIUM.** *H-Q acquires a third clean counter-case and the prior should be stated as a count.*

§5.2's prior is prose: the two legacy episodes *"were scored with highly elastic supply and did not end on a physical wall… they count against H-Q. The AI-compute case differs in having a hard physical layer, which is the reason to think H-Q may hold there and not in general."*

This market is a third counter-case, and a clean one. There is **no physical quantity wall** — Willis Tower is ~84% leased and still signing tenants, so the asset is operating. What fails is the balloon payment meeting a refinancing window that will not open against a collateral value below the loan balance. §5.2's own channel table classifies *"a market financing window closes"* as a **capital (C)** event, and §5.2 forbids relabelling it as administrative. So **C originates here**, exactly the ordering H-Q denies.

*Repair:* restate the prior quantitatively — "0 of 3 non-physical-wall episodes supported H-Q" — rather than as prose, so test F1 has a count to move against. The distinction matters because prose priors cannot be falsified by accumulation and counts can.

## 3. Cross-cutting: what the model gets right

Two results here are worth recording because they are not defects and they are not obvious.

**The market sits in the model's self-reinforcing corner, and the model has a name for it.** The L2/L1 credit-supply leg scores **`S− Perverse`** under §3.2 — quantity of credit supplied *contracts* as the price of credit rises. That is the mechanical description of extend-and-pretend: a lender withdraws precisely when the price signals distress. §2.3 then places `Λ < 0` as *"no stable clearing: a price move induces quantity responses that extend it… this is the self-reinforcing corner, and it covers both directions."* The model anticipated this pathology structurally, before this case was presented to it. Recorded under **H-Λ, `anchor-0d47f9a3`**, as supporting evidence.

**§2.1's measurement discipline is vindicated by an eleven-fold discrepancy.** The model refuses elasticity values assigned from narrative or from the existence of a contract structure, and demands a stated method and window. This market shows why: the same loans report **0.73% delinquency** through bank filings and **8%** through CMBS trusts. A factor of eleven, on the same objects, from two measurement regimes. The trust figure is valid because a trust cannot extend a troubled loan without public disclosure; the bank figure is valid only for what it measures — whether a cheque arrived. Any model that accepted bank-reported delinquency as an observable of distress would be wrong by an order of magnitude on this market, and §2.1 is the rule that prevents it. Recorded under **D4, `anchor-7a10c3e4`**, as supporting evidence.

## 4. Provenance note: the video overstates its own source

Recorded here so that a later reader working from the video does not inherit its framing. The video is the occasion for this register, not its evidence.

The paper says **"almost one-third of U.S. commercial mortgage dollars sits on regional bank balance sheets"** and reports **"over $1.6 trillion"** on those banks. The video says *"roughly 2/3 of that money came from… community and regional banks."* Against $3.1tn of bank-held CRE, $1.6tn is about **half** — the video overstates concentration by roughly a third.

More materially, the video reverses the paper's headline explanation. The video frames clean regional-bank books as an accounting artefact ("either these banks are the best lenders in the country… or these numbers aren't telling you the full story"). The paper finds **both effects, with the first as the larger**: *"regional banks benefit from their greater exposure to better-performing CRE markets rather than tighter origination standards"* — they lent in Sacramento rather than San Francisco, and into industrial rather than office.

And the video omits the paper's stress-test conclusion: *"Most institutions remain adequately capitalized under this baseline."* Only under a **severe further price-decline scenario** does *"a significant subset"* become undercapitalized. The video's title — *the crisis that's already here* — is a stronger claim than its own source makes.

Two staleness items, per the discipline that present-tense figures must be re-verified: the paper is **September 2025**, not "earlier this year"; and the video's *"10-year now around 5%, highest since 2007"* was already reversing at posting — **4.94% on 2026-10-30**, down from a **5.31%** peak on 2026-10-20, and **4.88% on 2026-11-09**. If the C channel is doing the work, and the rate component of C is easing, `λ_C` is falling, not rising. Partial relief only: a refinancing window closes on spread and collateral value together, and collateral is still −13% to −33%.

## 5. Verified clean during this application

Checked and found no finding, so the scope reads as bounded rather than open-ended:

- §3.4 `W` classification — `W2 Contested` is correct here (the loss is genuinely disputed among bank capital, depositors, the FDIC, CMBS investors and the borrower), and §5.4's survival-weighted branch mixture is the right machinery. §3.4's rule that *"W changes the speed of resolution, not the physics"* is exactly right: extension delays the loss without reducing it.
- §2.5's per-layer rule — the binding-layer declaration resolved cleanly; L1 is the least flexible supply layer without argument.
- §5.1's calibration instruction — the video's dated calendar ($400bn matured this year, **$650bn due next year**, 57 loans / $24bn past final maturity, Willis Tower extended to 2028) is usable as an event calendar in the form §13.2 requires.
- §8's layer list for AI compute — nothing in this application bears on it.

## 6. Decisions open on this document

Three anchors follow. Each asks for a position, not a description.

**DEC-1 · does `P` gain downside levels in v0.7, or is that deferred?**
Either extend §3.3 with `P−1`/`P−2` as the mirror of `P1`/`P2`, or state the scope limit explicitly in §3.3 and §12. Deferring silently is the option this register argues against, because the model's own applications are downside-relevant.

<!-- anchor-55a33458 -->

**DEC-2 · does §5.2's Q/E/C framework extend to K1 pools, or does K1 need its own exit specification?**
The L1 pool screens K1 under §3.1. Say which channel is expected to originate for a pool already responding to cost, or declare K1 exits out of §5.2's scope and name the section that will hold them.

<!-- anchor-c13d227f -->

**DEC-3 · is `D ≈ 42%` (36% prior year) adopted as a first-pass value for `M = CMBS, sold-out-of-trust`?**
If adopted, §12 item 10 should be amended to record that `D` has a first-pass observable for this market while `ν` remains method-less. If not adopted, state what basis would satisfy §2.1 here.

<!-- anchor-9048ebdd -->
