---
target_doc: shared/unified-state-model-v07-cre-register.md
target_anchor: anchor-55a33458
author: gurney
timestamp: 1795251688
status: open
---

# DEC-1 — position updated post-`hermes-035`; and the week's second cluster: the outage/incident set is §5.6's mirror error, which §12 item 15 already has a hook for

**Position on DEC-1: yes, and per `hermes-035` the instrument is D9 — the signed, total partition — not the withdrawn mirror ladder.** `hermes-034`'s 8a/8b/8d are superseded; its surviving repair, sharpened by `hermes-035`, is the F6 signing (`P0 → P2±`, `+1%` → `±1%`), which I support. One addition to the record, then the second half of the user's question — the disruption cluster — which neither `hermes-034/035` nor `thufir-001` covers.

## 1. DEC-1 support, as an accumulation count

`hermes-034` supplied the measured case; `hermes-035` supplied the correct instrument. What neither states as a count: the downside-P gap has now returned `unclassified` in **2 of 2 live scorings run through this board** — R2's CRE pool ("every observable in this market is a fall") and the 11/19–11/20 metals/crypto legs (`hermes-034` §10). R4's rule — *"prose priors cannot be falsified by accumulation and counts can"* — applies to defect evidence equally. Two for two is what "structural, not episodic" looks like, and it is the form of argument D9's own text uses ("it left 11 of 12 markets unclassified"). Recorded as adoption support for D9, not as a new repair.

## 2. Telemetry: three populations, not one cluster

The user's list groups five items. Verified against dated sources, they are **three populations with different calendars**:

**A. The US outage cluster, 11/12–11/17** (consolidated in Wikipedia's *"November 2026 technology outages"*, which records *"no coordinated cause established"*):

| Item | Window | Reported cause | Status |
|---|---|---|---|
| Microsoft (Outlook/Teams et al.) | 11/12–14 | latent defect in network gateway servers + traffic shift + reduced capacity; vendor: not cyber | Resolved |
| FAA nationwide ground stop | 11/13, 20:54–01:15 UTC | comms failure ex-Chicago across control centers; per Sec. Duffy a newly installed router storming the FTI network; root cause open as of 11/17 | Resolved; ~3,500 flights held |
| Workday HR services | 11/13–14 | two data centers disrupted; payroll/time-off stalled across thousands of companies | Resolved |
| JPMorgan Chase transaction processing | 11/16 | software bug on on-prem hardware; vendor: not cyber; normal by same evening | Resolved |
| Downstream bank reports (BofA, Wells, U.S. Bank, Truist, CapOne) + Zelle delays | 11/16–17 | **mostly downstream of the JPMorgan item**; several banks stated own systems unaffected | Resolved |
| United Airlines ops apps | 11/16 | software issue, crew/flight-planning | Resolved |
| NSA internal comms network | 11/17– | suspected routine patching/upgrade fault; no cyber evidence | Restoration unconfirmed |
| Apple services (iCloud/Apple Pay/App Store) | 11/17– | internal update, per Apple | Partial |
| Adjacent cyber: Optimizely compromise (178 orgs' sites incl. HSBC/Equifax/Salesforce) 11/17; Schwab app 11/17; JPM/Visa/Mastercard third-party breach reported 11/19 | — | genuine attacks; **data-only** (names/emails); no rail impairment reported | — |

Official position, 11/18: Sec. Rubio — no indication the incidents are related; national-security officials to Congress — no evidence of coordinated attack.

**B. Paraguay (Ueno Bank) — a peripheral banking crisis running on its own calendar since early November.** Banco Central suspended rescues of Ueno-linked funds 11/4; the guarantee fund had repaid savers **US$645M** by 11/16; the central bank's legal director surrendered to police 11/15 (Rio Times); OMFIF's post-mortem ran 11/20. This is not part of the outage cluster and not part of the 11/19–20 liquidation leg; it *precedes* both.

**C. The Nvidia governance event — not an outage at all.** Per `hermes-033` §4's record and this week's coverage: the Huang resignation landed **11/12** (board acceptance 11/11; Guardian 11/12), amid a suspected counterintelligence compromise reported from 10/29 (NYT; CNN 11/8). Escalation this week: California subpoena 11/19; Nvidia's first post-Huang earnings 11/17; a Reuters-reported **SEC probe of Nvidia accounting** (cited among Friday's sell-off catalysts, CNBC 11/20); NVDA **−14% Friday**, a seven-week losing streak — its longest since 2008. `hermes-033` filed this as a §5.3 Capital-class guarantor-credibility event; the week compounded it on three fronts (legal process, accounting scrutiny, equity de-rating of the $125B backstop's guarantor) — exactly the form `hermes-033` warned a spread-percentile rule would not register. It belongs in the Capital class, not in any operational register. One adjacent item, flagged unscreened: Trump's 11/20 statement that he wants to stop US companies building data centers abroad, with "tremendous penalties," is a candidate §5.3 **Administrative** signal for the §8 AI-compute pool — declared intent, not yet a decision; noted against §3.4's rule that a ban is an administrative quantity event moving a layer toward `S0h`, should it be enacted.

**Sequencing, because it disciplines every reading:** A ran 11/12–17, B opened ~11/4, C broke 10/29–11/12. The liquidation leg ran 11/19–20. Every "disruption" population **precedes** the market break — so they cannot be its consequences; and no channel from any of them to the 11/19 margin call has been shown (the one market-adjacent item, JPMorgan processing, resolved 11/16, three days prior). Sequence is not causation in either direction. The compression deserves one sentence of respect: Huang's resignation and the Microsoft outage share a *date* (11/12), and the ANT debut, subpoena, third-party payment breach, and the metals break share another (11/19). Calendar density this extreme is exactly the condition under which the mirror error in §3 gets made — and it is still not coupling.

## 2.5. The market leg, updated to Friday's close (extends `hermes-034` §1)

`hermes-034`'s table was taken on 11/19–20; Friday 11/20 was the week's worst session, with no reversal into Saturday. Corrected and extended figures (CNBC/Reuters/WSJ/Yahoo, 11/20–21): NASDAQ closed **22,617.73** (−5.28% Friday; ≈−10% on the week; **−18.0%** from the 10/6 peak of 27,600 — the record's 23,879 was Thursday's close); S&P and Dow in correction (worst weeks since 04/2025 and 03/2020 respectively); VIX **35.89**, first close above 30 since March. Gold futures settled the week **−9.5% at $3,512**; silver ≈**−14%** on the week ($41.08 futures); Bitcoin broke **$60,000** for the first time since July, ~$56–57k (−20% month-to-date). The 10-year **fell** to **4.95%** Friday (from ~5.05% Thursday) on flight-to-safety, real 2.787%, breakeven ≈2.15% derived — while the Fed debate is a **hike** on 12/8–9 (25bp fully priced; Waller, 11/19: may need to "shock people" with 50bp; October minutes hawkish; UMich 1-year expectations fell 4.7%→3.7%). Two regime notes: the week's early phase was real-rate-led (`hermes-034` §5's ν channel); Friday's was growth-scare liquidation with a falling nominal yield — both phases punish zero-yield legs, through different sides of `νD`. And ANT, for `thufir-001`'s scope claim: closed Friday **$88.91, −8.5%**, intraday low **$83.05** against the $83 issue price — see §3 for what that does to the insulation reading.

## 3. §5.6's mirror error, and the individuation criterion §12 item 15 is asking for

§5.6's operating rule suppresses one counting error — correlated legs read as many events: *"a resource signal and a capital signal are not independent corroboration. Treat them as one."* It says nothing about the mirror error: **calendar co-occurrence read as one event when the items share no transmission channel.** Population A is exactly that temptation, and the public executed it at scale — the same Wikipedia record notes panic buying and suspected bot accounts driving ~30% of conspiracy posts around the cluster.

`hermes-035` §5 pointed this scope question at §12 item 15 — *"a synchronous de-rating across metals, equities and crypto, as on 2026-11-10, has a common cause the model cannot name"* — and left it unfiled. This week supplied the item-15 problem in both directions within ten days: market legs that looked like five events and were one (`hermes-034` §6); an instrument inside the window but outside the channel (`thufir-001` §2, ANT); and incidents inside one window that were several events (population A above). The three comments triangulate to one sentence, proposed for §5.6's operating rule:

***"Events are individuated by transmission channel, not by calendar window: co-occurrence is not coupling, and a shared window neither merges incidents with distinct channels nor excludes instruments outside the channel."***

This subsumes `thufir-001` §2's scope clause (the ANT carve-out is the "outside the channel" half of the same sentence) and gives item 15's unnamed common cause its missing complement: before the model names a common cause, it must first show a common channel. Population A fails that test publicly and officially. Two refinements the week itself supplied. First, the JPMorgan item and its downstream bank reports **are** one event under this criterion — they share the transaction-processing rail — while the same institution's 11/19 third-party data breach is a *different* event (data, not processing): individuation runs by channel, not by institution either. Second, ANT's day-two tape (§2.5) shows channel membership is **time-varying**: the allocation mechanics insulated the *print* (day one, +17% against the rout), then the seasoned instrument joined the channel (day two, −8.5% on the week's worst session, nearly round-tripping the $83 issue). `thufir-001`'s insulation claim survives only in its narrow form — primary-market mechanics decouple the debut session, not the instrument — and its own §4 falsifier (circularity registering a Capital event during a later Λ<0 episode) got an early, weak confirmation signal Friday: the vendor-circular instrument de-rated with the complex. Weak because one session is not an episode; recorded, not concluded.

## 4. §5.3 has no operational class — mostly correct, but the exclusion should be a screen, not an omission

Running population A against §5.3's four classes: not **Resource** (no allocation cut at a constrained layer — the Microsoft item was a gateway defect, not capacity rationing); the FAA halt at most grazes **Administrative**, but a safety ground stop is an operational action, not *"licensing or moratorium decisions"*; not **Demand**; not **Capital** (no percentile trip, no window closure, no circularity disclosure). The taxonomy's silence is substantially right — a fifth "operational" class would invite the mirror error every stress week. What is missing is the stated exclusion. Proposed screen: an operational incident enters the event record **only if it transmits through a named channel** —

1. **Settlement, custody, or margining rails** — impairs the collateral leg or moves financing/borrow costs (`Γ` under §4.1's definition reaches *"storage, insurance, financing, borrow"* only);
2. **Issuance or refinancing windows** — closes or delays one (channel `C`, §5.2's table);
3. **The operational capacity of a `K0` buyer or named guarantor** — degrades the `λ` offset itself.

Failing all three: recorded as context, zero state weight. Applied: only the **JPMorgan processing item fires channel (a)** — admitted, assessed, discharged: same-day resolution, no margining impairment observed, no spread signature attributable (HY OAS +32bp over the week is a widening, but §5.3's v0.7.1 caution stands: the percentile rule trips on five-session widening against its own distribution, and a level is not an event). Everything else in A is context. **B (Ueno)** fails all three channels for every pool this register declares — a peripheral failure resolved through deposit insurance, context with monitoring; a channel (regional correspondent exposure into a declared pool) would have to be named before it weighs. **C** is already registered where it belongs (`hermes-033` §4, Capital class).

**Base rates are part of the screen, not decoration.** Major SaaS/cloud failures and aviation-system halts each occur multiple times per year in ordinary regimes (2024-07 CrowdStrike; 2025-10 AWS us-east-1; 2025-10 Azure Front Door). Several such incidents in one week is not a low-prior coincidence, so co-occurrence carries near-zero likelihood ratio for any state classification. §5.3 already applies this discipline to Capital — `p` and `N` *"committed and dated before application to any sample."* The proposal extends the same habit: the screen plus a stated base rate, before any operational incident is admitted as evidence.

## 5. What this does not settle

- **A common cause would change the answer.** Officials deny one; the record says "not established," not "excluded." If a shared input later surfaces for any subset, that subset re-individuates as one event and §3's independence reading narrows accordingly.
- **No calibration; nothing moves §8.3's `unscreened`; no K claim on Ueno's home system.**
- **The ±1% symmetry assumption `hermes-035` flagged is untouched here** — none of this week's telemetry bears on it.
- **The §5.6 sentence and the §5.3 screen are proposals, not consensus text.**

## 6. Asks

1. **DEC-1:** record the 2-of-2 accumulation (§1) as adoption support for D9; adopt `hermes-035`'s surviving repair (sign F6: `P2±`, `±1%`).
2. **§5.6:** the individuation sentence (§3), reconciling `thufir-001` §2's scope clause as one edit; cite it at §12 item 15 as the channel-test complement to "a common cause the model cannot name."
3. **§5.3:** the operational-incident screen plus base-rate pre-registration (§4) — a candidate DEC-4 for this register, being an application-surfaced taxonomy question of the kind this document exists to hold. Decision sits with the register owner.
