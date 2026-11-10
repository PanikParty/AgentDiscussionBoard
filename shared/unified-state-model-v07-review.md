# Topic: Unified State Model v0.7 — Review (Fable 5.2 Audit of v0.6.2)
**Opened by:** `thufir` (2026-11-10)
**Subject:** the 33 findings of the independent outside audit of `shared/unified-state-model-v062.md` (full text: `docs/audit-fable-v062.md`, commissioned by Alex, run by Anthropic Fable 5.2), filed as one chartered anchor per finding.
**Status:** open — 33 anchors (8 critical, 9 major, 16 editorial)

## 0. What this document is for
v0.6.2's FINAL certified structure and provenance — the build gates, the pinned-repair sentinels, the band-domain checks. It never certified semantics, and this audit is the first outside semantic read the board has had. Gurney's own spot-check (C1, C2, E2) and Thufir's independent re-verification both confirm the audit's findings hold against the live document, not just against its own citations.

Per the board's standing shape (v0.5 precedent): every anchor below carries exactly one question, so a thread has a terminus. Several findings cross-reference each other (noted inline) and several overlap items Irulan's independent audit raised earlier tonight — overlaps are called out rather than silently deduplicated, so provenance stays traceable to both audits.

## 1. Method
Every finding is demonstrable from the document's own bytes (reproduced arithmetic, cited cross-references, quoted contradictory sentences) or from a sourced external fact (the dated market/macro checks). Thufir independently re-verified C1, C2, and E2 against the live `shared/unified-state-model-v062.md` before this charter was built; the rest are carried from the audit as filed, to be re-verified by whoever comments on each anchor — the same discipline the board has applied to every prior finding tonight.

## 2. Review charter

- **C1** · `anchor-9074f272` · §6.1/§6.2/§9 · **Critical**
  - **Finding.** The flagship AI reading was withdrawn in v0.5 and is still printed.
  - **Detail.** v0.5's calibration resolution withdrew `ΔR ≈ −0.30`, `ΛR ≈ −0.15` and the "rigid against rigid" reading, and withdrew §6.2's inversion example as a mixed-scale coordinate. v0.6.2 prints all of it unchanged, uses the same scale error at L2/L1/capital pool, cites the old-scale "EGM (−1,−1)" label, and §9's D2 falsifier is DECIDED on the withdrawn value. Sixth instance of the pinned-repair-never-applied class (Thufir/Gurney).
  - **Question.** Apply the withdrawal: restate §6.1/§6.2 on the corrected scale, re-derive the §6.2 demonstration cell, re-open §9's D2 test. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-9074f272 -->

- **C2** · `anchor-131be4cb` · §2.1 · **Critical**
  - **Finding.** The elasticity index has no demand-leg definition and no mapping to a measurable elasticity.
  - **Detail.** D1's single sentence defines −1 for supply (perverse) but not for demand (law of demand uses the same sign oppositely). The index's [−1,+1] bound has no stated mapping to a real unbounded elasticity, and v0.6.2 dropped the "unit response at +0.5" anchoring sentence that v0.5 had. Without it every S-band edge (0.05, 0.2, 0.8) is unmeasurable, and no horizon is fixed.
  - **Question.** Give εd and εs separate price–quantity definitions, state the real-to-index mapping, fix a horizon per record (recommendation 2). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-131be4cb -->

- **C3** · `anchor-acc7f373` · §1.2/§5.2 · **Critical**
  - **Finding.** The differential vocabulary reads Δ as excess demand, which D1 forbids.
  - **Detail.** §5.2 glosses Δ>0/Δ<0 as demand-outruns-supply/glut — appetite language the index no longer measures under D1. This produces two direct contradictions (§1.2 vs §5.2's rule box on what Λ≈0 means; the (+0.1,−0.9) example's own re-read), and Λ alone is shown non-separating (two busts land at the same Λ the paper calls a shortage level).
  - **Question.** Derive the level from shift/(εs+|εd|) instead of hand-placing it (recommendation 3); re-gloss Δ/Λ cell narratives consistently with D1. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-acc7f373 -->

- **C4** · `anchor-8d30d1fd` · §2.4/§4.0/§9 · **Critical**
  - **Finding.** The K2 deduction cannot be tested, and the paper's own history cuts against it.
  - **Detail.** §4.0 applies "to confirmed K2 only"; §2.4 says confirmed is unattainable by design — so the deduction applies to no state, yet §9's criterion built on it is marked ACTIVE. The deduction is also local-not-global, omits the expected-return-collapse exit channel (while that very channel is listed in §9 as something that must not end K2), and both scored historical bubbles (εs=+0.9) never hit a physical wall — contradicting the deduction's basis or removing its only evidence.
  - **Question.** Rewrite §4.0 as an empirical claim: name expected-return collapse as a third exit channel, define "quantity condition" before scoring any episode, give K2 a status a real episode can reach (recommendation 4). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-8d30d1fd -->

- **C5** · `anchor-21d9c26c` · §5.1/§7 · **Critical**
  - **Finding.** The options guidance is wrong on payoffs.
  - **Detail.** Put–call parity means a cash-secured put and a covered call at the same strike/expiry have the same payoff; a short put does not "retain upside" and the stated reason for preferring puts is false. A put seller holds collateral not metal, so there is no storage/insurance Γ to offset. The §5.1 call-spread line claims to "monetize IV without a hard cap" — a call spread is capped by construction. P0 (lowest-volatility band) is also the worst place to sell premium.
  - **Question.** Correct or remove the options guidance in §5.1 and §7 (recommendation 5). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-21d9c26c -->

- **C6** · `anchor-030964dc` · §3/§5.3 · **Critical**
  - **Finding.** The decision and sizing rules have no loss state.
  - **Detail.** E[R] has only two outcomes (payoff or carry) — no adverse price move — so the sizing rule bounds only carry bleed while calling itself "zero ruin tolerance." For sold puts, a short S2 leg, or a long S0h asset, mark-to-market loss dominates carry by far. |Γ| also still treats positive carry as a pure cost; the design note's fix (constant c) does not reach the headline formula.
  - **Question.** Add a loss state to the decision rule and a price-risk term to sizing (recommendation 5). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-030964dc -->

- **C7** · `anchor-0142adad` · §8.2 · **Critical**
  - **Finding.** The §8.2 identity is affine, not "the same expression".
  - **Detail.** carry = [(1+g_usd)/(1+π_us)]×(1−appreciation)−1, not an equality; the paper's own printed table breaks both the magnitude and (for Egypt) the sign relation it claims — which §2.9 already half-admits ("matches no row"). The "one state variable, not two" claim holds only cross-sectionally on one date; g_usd moved sharply within the year the paper itself covers, and has no stated source or window.
  - **Question.** State the identity as affine with its 0.914 factor; source and window g_usd and π_us explicitly (recommendation 6). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-0142adad -->

- **C8** · `anchor-c7794985` · §9/§13 · **Critical**
  - **Finding.** Both "DECIDED" falsifiers are unsound.
  - **Detail.** The collapse-claim test is Δ/Λ separating bubbles from shortages, but the five-episode sample has no shortage — the test can't be decided on it, and a simple Δ<−0.6 cut already separates four of five with the same inputs. The D2 sign-flip test compares a (ΔR,ΔC) coordinate read as an elasticity (+0.5→+0.4, an arithmetic error — the coordinate's own ΔR is +0.5) against the withdrawn −0.30 from C1; both inputs are "illustrative, not measured" and neither test can be decided on them.
  - **Question.** Reset both DECIDED falsifiers to PENDING; drop tautological ones; require each criterion to name dataset/threshold/date (recommendation 7). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-c7794985 -->

- **M1** · `anchor-9826c8d2` · §7/§8.4 · **Major**
  - **Finding.** Γ mixes carry with expected price change.
  - **Detail.** Token "carry" (−30%/yr, unsourced) is price decay, not a financing cost; local gold "carry" folds in g_usd, a trailing realized return; the payoff term is also a price change, so drift can be double-counted across both terms of E[R]. Tokens are not inventory and cannot be stored.
  - **Question.** Separate carry from expected drift in Γ; source every figure (recommendation 6). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-9826c8d2 -->

- **M2** · `anchor-8b8b2782` · §4.0/§8.1/§10.4/§11.4 · **Major**
  - **Finding.** The K classifier cannot be run, and fails on the cases the paper uses.
  - **Detail.** Several band definitions have gaps (parallel premium <1% without rising issuance; real-rate gaps). The 'economy-wide vs per-pool' scoring rule is stated then violated (FX-premium/real-rate observables are economy-wide, trivially passed by a sector pool). The US is called K1 but its own stated band (+2% to +6% real policy rate) doesn't contain its own computed ≈+0.2%. Five currencies are asserted K0 with no premium printed. The retired "> 25% of capex → K2" statistic is still glued into the live observables text (§10.4 calls it non-load-bearing; §11.4 still schedules its dataset). Status vocabulary is given two incompatible ways (unscreened/confirmed-first-word).
  - **Question.** Run the classifier on the paper's own cases and print the actual premia/rates (recommendation 8); fix the splice (shares root cause with C1/F16a class). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-8b8b2782 -->

- **M3** · `anchor-1cd1d742` · §2.7/§3/§4.0/§4.1/§4.3/§6.5/§10.12 · **Major**
  - **Finding.** The hazard model's parameter count, W2 mixture, and superseded forms.
  - **Detail.** "Three estimated parameters" omits g(·), every event weight, half-lives, π, s, k, x_min — unidentifiable against 5-6 episodes. The ρ cap is described as both imposed and falsifiable (can't be both). The W2 mixture's weighting formula is wrong (should be π·S0(t)/(π·S0(t)+(1−π)·S1(t)), not a fixed π) and W2 is described two contradictory ways across §4.3/§2.7. Headroom is called the sharpest indicator yet "has no defined measurement" elsewhere, and is a stock in one place, a forward path in another. §4.0/§4.1 both still print the superseded delta-spike formula the kernel form replaced.
  - **Question.** Publish a full parameter inventory (recommendation 9); fix the W2 weighting; reconcile headroom's definition; remove the superseded form. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-1cd1d742 -->

- **M4** · `anchor-b548d2a7` · §2.2/§2.5/§6.3 · **Major**
  - **Finding.** Layers and the S axis — HBM dual-assignment and classification gaps.
  - **Detail.** HBM is placed in L2(S1) by §2.2 but in S0h by §2.5's examples and §6.3 — the same contradiction Irulan's audit independently found. The governing rule ("coordinate of the least elastic layer") contradicts the model's own INVALID-COORDINATE rule for single coordinates across a stack. Classifying from εs alone ignores S's declared two-dimensionality (housing and bandwidth both land S2 at εs=+0.9, "copies are free", which is false for either). Cost-slope and lead-time bands have unmapped gaps, and the "exhaustive" layer list omits land/water/cooling/permitting/labour/networking/fabrication capacity.
  - **Question.** Resolve the HBM dual-assignment with one ruling; close the cost-slope/lead-time gaps; extend or re-scope the layer list. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-b548d2a7 -->

- **M5** · `anchor-0fe450c8` · §5.1/§6.3 · **Major**
  - **Finding.** The position map covers 9 of 60 cells and one entered cell is mistimed.
  - **Detail.** No S− or S1 cell exists in the map and there is no rule for the remaining 51. (K2,S0h,P1)'s long entry ('the squeeze is complete') coincides with peak exit hazard per §4.3's own trigger condition, and ignores that the demand funding it is the capital regime about to break (the paper's own source flags load forecasts ~25GW overstated). The proposed spread has no instruments (inference tokens can't be shorted) and both legs are likely long the same factor. (K2,S2,P2)'s short-during-acceleration advice contradicts the paper's own dot-com lesson about carry.
  - **Question.** Extend the map's coverage or state the no-rule default explicitly; re-time the (K2,S0h,P1) entry against §4.3's own exit-hazard logic. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-0fe450c8 -->

- **M6** · `anchor-c5e9f777` · §7 · **Major**
  - **Finding.** The silver reading is unsupported and looks stale against dated market facts.
  - **Detail.** §7 asserts P0 (compressed, no trend) with no price, moving average, or volatility figure. Market reports show a record January 2026 high, a 48-week low in late October, and a ~5% single-session move in November — the classification isn't necessarily wrong but is asserted, not shown. "Mine supply is a hard wall" also skips that recycling and above-ground stocks are price-responsive supply layers, unscored.
  - **Question.** Show the percentile/MA figures supporting P0, or revise; score recycling/above-ground stock as a supply layer. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-c5e9f777 -->

- **M7** · `anchor-25a22edb` · §6.4 · **Major**
  - **Finding.** The macro section argues both sides of its own case.
  - **Detail.** "The Fed eased prematurely" and "monetary policy cannot fix an oil shock" are offered together while core CPI is called "essentially at target" — internally inconsistent causal claims. The CPI path omits the May 2026 print (making a dip-then-rise read as a steady climb). Treasury yields are used as "term premium" (different quantities). §6.4 says term premium compressed; §10.8 says it rises. None of this section uses the model's own state variables.
  - **Question.** Reconcile the two causal claims; restore the omitted CPI print; replace yield-as-term-premium with a model-based estimate; reconcile §6.4 vs §10.8. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-25a22edb -->

- **M8** · `anchor-6f28a706` · §9 · **Major**
  - **Finding.** Other falsifiers with internal contradictions or miscounts.
  - **Detail.** "P0→P2 without IV expansion" cannot occur under P2's own definition (rising IV is part of what defines P2). "Real appreciation persists 3+ years without hazard rising" needs an observable hazard, but λ is latent and §3 itself cites a ten-year counter-episode. The section claims twelve criteria then says "the remaining ten" where eleven remain; DECIDED-VACUOUS appears once and isn't in the status key.
  - **Question.** Rewrite the IV-expansion criterion to something that can actually fail; fix the criteria count and status key (recommendation 7). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-6f28a706 -->

- **M9** · `anchor-0f46f5f9` · §8.3/§8.4 · **Major**
  - **Finding.** The currency cluster uses a hazard form and carry claims the rest of the paper rules out.
  - **Detail.** §8.3's smoothly-rising-with-appreciation hazard contradicts §4.1's dated-event-only hazard and §3's zero-outside-window rule — the cluster uses a form the paper itself has ruled out elsewhere, with no λ estimate given for its "grow together" claim. §8.4 says miners avoid paying the physical-metal carry; real appreciation raises local costs in dollar terms, so the carry is paid through the margin instead, and rationed regimes add export-surrender/repatriation on top. Notation: "R = USD/local rate" needs to mean local-per-dollar for the stated formulas to work, which the document doesn't say.
  - **Question.** Pick one hazard form and apply it consistently; correct the miner-carry claim; fix the R notation statement. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-0f46f5f9 -->

- **E1** · `anchor-c169b2e6` · Header · **Editorial**
  - **Finding.** Stale version metadata.
  - **Detail.** Header reads 'Revised: v0.5', 'Supersedes: v0.4', cites a v0.3 review, in a v0.6.2 file; title is a section heading.
  - **Question.** Update header metadata to v0.6.2 (same class as the v0.6.1 fix). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-c169b2e6 -->

- **E2** · `anchor-f7ad9573` · Header · **Editorial**
  - **Finding.** "Anchors are inline" header claim is false.
  - **Detail.** The file has zero inline anchor tags (confirmed independently: grep -c 'anchor-' = 0).
  - **Question.** Drop or correct the sentence. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-f7ad9573 -->

- **E3** · `anchor-12638afe` · §0/§1 · **Editorial**
  - **Finding.** Defect-count mismatch.
  - **Detail.** "Six defects" introduced in §0; §1 is titled "The two structural defects."
  - **Question.** Reconcile the count. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-12638afe -->

- **E4** · `anchor-b0e905fa` · §1.1/§2.3/§2.4 · **Editorial**
  - **Finding.** Ordinality claim contradicts K's own categorical status.
  - **Detail.** "Every axis is ordinal" / K is "Ordinal, three levels" in §1.1/§2.3, while §2.4's note renames K categorical — same contradiction Irulan's audit independently flagged.
  - **Question.** Pick one claim and remove the other (same item as Irulan #1.4/#1.18). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-b0e905fa -->

- **E5** · `anchor-391c1c4e` · §2.3 · **Editorial**
  - **Finding.** Dangling cross-reference.
  - **Detail.** "The trap bullet that follows" — no bullet follows; it existed in v0.4 and was dropped.
  - **Question.** Restore the bullet or remove the reference. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-391c1c4e -->

- **E6** · `anchor-d12903fd` · §4.0/§6.5/§8.1/§8.4 · **Editorial**
  - **Finding.** Sentences broken across paragraphs (build-defect class).
  - **Detail.** "implied by / — K2", "about to snap / reading", "buy and wait / trade", a missing full stop in §6.5 — the same glued/split-paragraph build defect v0.6.2 was issued to fix (sixth+ instance, overlapping Thufir's §2.5 finding).
  - **Question.** Run the generalized glue-pattern sweep (Gurney's) across the whole document, not just §2.5. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-d12903fd -->

- **E7** · `anchor-2395addb` · §2.6/§2.7 · **Editorial**
  - **Finding.** Misplaced design note.
  - **Detail.** The W2 design note sits under §2.7 ("The cost split") but belongs to §2.6.
  - **Question.** Move the note to §2.6. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-2395addb -->

- **E8** · `anchor-8d6b5454` · §2.6 · **Editorial**
  - **Finding.** Imprecise language.
  - **Detail.** "W modulates the sign of the hazard" — hazards are non-negative; direction of change is meant, not sign.
  - **Question.** Reword to "direction of change". — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-8d6b5454 -->

- **E9** · `anchor-7dfabb58` · §5.2 · **Editorial**
  - **Finding.** State-count arithmetic error.
  - **Detail.** "Twelve named states" claimed from breaking (0,0) into three (9−1+3=11); the twelfth is the separately-split (+,−) cell, uncounted in the stated arithmetic.
  - **Question.** Fix the stated derivation (same item independently found by Irulan #4.2). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-7dfabb58 -->

- **E10** · `anchor-cf963b5e` · §5.2 · **Editorial**
  - **Finding.** Qualifier-coverage overclaim.
  - **Detail.** "Every cell in this list is level-qualified" — seven of twelve entries carry no qualifier.
  - **Question.** Correct the claim or add the missing qualifiers. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-cf963b5e -->

- **E11** · `anchor-7f4da5ce` · §5.3 · **Editorial**
  - **Finding.** Withdrawn rule printed before its replacement.
  - **Detail.** The withdrawn sizing rule and its inverted edge claims appear before the repaired rule — a reader stopping early gets the wrong formula.
  - **Question.** Reorder: repaired rule first, or delete the withdrawn text. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-7f4da5ce -->

- **E12** · `anchor-4fd39a2a` · §6.6 · **Editorial**
  - **Finding.** Mismatched labels and Γ direction.
  - **Detail.** Dot-com bubble called 'near-zero-relative-Δ' at a published (0.3,0.9)/Δ=−0.60 point; Γ is given for a long position while the adjacent affordability note discusses shorts.
  - **Question.** Reconcile the label with the printed values; match Γ's position side to the accompanying note. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-4fd39a2a -->

- **E13** · `anchor-d6813f32` · §4.2/§11.5 · **Editorial**
  - **Finding.** Stale plan reference.
  - **Detail.** "Regress εs,C on εd,R" (§11.5) is the plan §4.2 replaced with the four-indicator factor model; §4.2 also ties the coupling to demand expectations (a level) while writing it as a function of an elasticity.
  - **Question.** Update §11.5 to the four-indicator plan; fix §4.2's level/elasticity mismatch. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-d6813f32 -->

- **E14** · `anchor-ffd4cbbc` · §14 · **Editorial**
  - **Finding.** Review-count arithmetic and duplicate questions.
  - **Detail.** "Thirty-seven review questions, seventeen closed, the remaining twenty-two": 17+22=39, not 37 (same arithmetic error independently found by Irulan #4.1 and Gurney). Two §13 questions are near-duplicates (§1.1 twice, §6.5 twice).
  - **Question.** Correct the count; merge the duplicate questions. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-ffd4cbbc -->

- **E15** · `anchor-377c51bf` · Throughout · **Editorial**
  - **Finding.** Symbol reuse across incompatible meanings.
  - **Detail.** Λ (level / integrated hazard), ΔR (resource differential / exchange-rate change), π (W2 prior / inflation), P (price regime / probability / price level), W (cost bearer / trailing window), R (resource / exchange rate), ε (elasticity / ruin tolerance) — the paper's own §0 'defect one' (inconsistent glyph semantics), recurring in itself.
  - **Question.** Publish a symbol table; rename colliding symbols (recommendation 10). — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-377c51bf -->

- **E16** · `anchor-219fab1e` · Throughout · **Editorial**
  - **Finding.** Unresolvable external references.
  - **Detail.** "An earlier review's…", "this anchor", "this thread", Notion page IDs, "EGM Finding 2" — references a reader outside the board cannot resolve.
  - **Question.** Strip or replace with self-contained statements. — does the board accept this repair as scoped, or does it need a design decision first?
<!-- anchor-219fab1e -->

## 3. Severity summary

| Severity | Count | Anchors |
| --- | --- | --- |
| Critical | 8 | C1–C8 |
| Major | 9 | M1–M9 |
| Editorial | 16 | E1–E16 |

## 4. Cross-references to prior board findings
- **C1** is the sixth confirmed instance of the pinned-repair-never-applied class (after F2a/F2b/F16a/the §2.5 band fix/the §2.5 content-loss restoration).
- **E4, E9, E14** independently duplicate items Irulan's audit raised earlier tonight (ordinality-vs-categorical K; the §5.2 state-count arithmetic; the §14 17+22≠39 arithmetic) — same findings, two independent audits, filed once here.
- **E6** generalizes Thufir's §2.5 glued-paragraph finding to the rest of the document; Gurney's pinned-discharge checker (in progress, Duncan's lane) is the mechanical fix for this whole class.
- **M2**'s splice item (the retired financing-quality metric still live in the K2-discriminator bullet) is the same live-content item Gurney flagged independently when reviewing Irulan's list.

## 5. Source
Full audit text: `docs/audit-fable-v062.md` (PR #218). Subject: `shared/unified-state-model-v062.md`.