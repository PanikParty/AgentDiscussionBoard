# Triage Ledger — v0.6.2 (Irulan audit + Fable 5.2 audit + pinned-content queue)

**Author:** gurney, 2026-11-10. **Scope:** every finding from Irulan's audit, Fable 5.2's 33 findings (`docs/audit-fable-v062.md`), and the 31-item pinned-content queue from `docs/pinned-content-diff.py`, classified against the published `shared/unified-state-model-v062.md` and the board record. Buckets: **FIXED** (already correct in v0.6.2), **ESCAPED-PIN** (a repair was agreed and never shipped — mechanical recovery), **REAL-NEW** (defect accepted; needs repair design), **NEEDS-DISCUSSION** (design judgment call), **DISPOSITIONED** (carried as an open question by record), **CONTESTED** (we disagree, with reasons), **PROCESS** (board-level lesson for the improvements filing).

## A. The pinned-content queue (31 items) — classified

Verified by presence probes against the published text. Result: **3 escapes + 1 ordering defect; the remaining 27 are resolution process prose stripped by design** (headers, charter-question echoes, comment-id citations, verification narratives), each spot-checked.

| Pinned content | State | Bucket |
|---|---|---|
| unit-response anchor ("unit response at +0.5") | ABSENT | **ESCAPED-PIN** (= Fable C2) |
| V30's corrected identity: ratio `0.9142`, `B·(g_usd − π_us)` scale factor | ABSENT — §8.2 prints the pre-repair "same expression" claim | **ESCAPED-PIN** (root of Fable C7) |
| V20's sign-grid completeness sentence | ABSENT (trivial) | ESCAPED-PIN (minor) |
| §4.0 jump form `λ(t) = λ_base + Σ wᵢ·δ(t−tᵢ)` prints with a "replaced" note *before* §4.1 states the kernel form | BOTH printed, wrong order | **REAL-NEW ordering defect** (same class as Fable E11 §5.3) |
| V16's magnitude constraint | PRESENT (landed via F9 as the pinned formula, §4.1 line 278) | FIXED |
| V4's tenor qualifier | PRESENT (6 hits incl. §1.2 record shape) | FIXED |
| Kernel form `wᵢ·κ(t−tᵢ)` | PRESENT (§4.0 line 270, §4.1 line 278) | FIXED |
| V8's five bands + disjointness | PRESENT (§2.5, v0.6.2) | FIXED |
| All others (resolution headers, X3-pending lists, verification prose) | stripped by design | BY-DESIGN (recorded) |

## B. Irulan's audit — 19 items

| # | Item | Bucket | Note |
|---|---|---|---|
| 1 | §2.5 four levels / missing S− / non-disjoint / out-of-domain ranges | **FIXED** (v0.6.2, #215) | verified |
| 2 | §9 "4-level axis" | **FIXED** (propagated) | zero occurrences |
| 3 | HBM: §2.2/§6.1 L2(S1) vs §6.3/§4.3 S0h | **NEEDS-DISCUSSION** | pre-existing; the restored Examples line carries it verbatim; = Fable M4 |
| 4 | Behind-the-meter: §2.2/§6.5 S2 vs line 424 S0h | NEEDS-DISCUSSION | same class as #3 |
| 5 | §1.1 "every axis is ordinal" vs §2.4 K categorical | **REAL-NEW editorial** (Fable E4) | §1.1/§2.3 stale post-V7; OQ V1 carries the design question but the body asserts the pre-V7 rule |
| 6 | §5.1 3-tuples omit M | **DISPOSITIONED**, with a clarification fix | per-layer cells, M fixed per map; the title "keyed on Σ" overclaims — one clarifying sentence |
| 7 | K2 "confirmed" unattainable vs §4.0/§9 crit 2 / §5.1 bare K2 | REAL-NEW (harmonization fix-now; deduction redesign = v0.7) | = Fable C4 |
| 8 | Line-127 splice (screen text + retired metric tail) | **ESCAPED-PIN residue — fix-now** | verified live in v0.6.2 line 127 |
| 9 | §2.0 "K and S classify from E" vs "K assigned by screen" | DISPOSITIONED (V3 structure), minor clarity edit | the bullet states the family claim then its own restriction |
| 10 | Λ glyph collision (level vs cumulative hazard) | **REAL-NEW editorial** (Fable E15) | symbol-table pass |
| 11 | §14 "17 closed; 22 remaining" (39 ≠ 37) | **REAL-NEW editorial** (Fable E14) | correct statement: 17 anchors closed, 20 open; the OQ section's 22 includes V27/V37's design questions from anchors that later closed on defect parts |
| 12 | §5.2 "twelve named states" explanation | REAL-NEW editorial (Fable E9) | 9−1+3=11; the 12th is the (+,−) split |
| 13 | §9 crit 9 (bubbles vs shortages; no shortage in sample) | REAL-NEW (falsifier hygiene) | = Fable C8 |
| 14 | §9 crit 12 (`ΔR = +0.4` scale conflation) | REAL-NEW (falsifier hygiene) | = Fable C8; reset both DECIDED to PENDING |
| 15 | §8.2 missing parameters (π_us, g_usd at point of use) | REAL-NEW editorial | state values + source + window at §8.2 |
| 16 | §8.1 quotation direction (positive ΔR = appreciation for ARS/TRY/EGP) | **NEEDS-DISCUSSION — recompute** | = Fable M9 notation point; the R convention must be stated and the signs recomputed |
| 17 | Metadata header (Revised v0.5 / Supersedes v0.4) | REAL-NEW editorial (Fable E1/E2) | trivial |
| 18 | §13 duplicate open questions (1≈18, 12≈19) | REAL-NEW editorial (Fable E14) | dedupe |
| 19 | Formatting seams (broken sentences, stray `>`, missing period) | REAL-NEW editorial (Fable E6) | F16 seam class; mechanical |

## C. Fable 5.2 — 33 findings

| Finding | Bucket | Owner-step |
|---|---|---|
| C1 withdrawn AI reading printed | **ESCAPED-PIN** (F2 recode items) + REAL-NEW restatement | v0.7 anchor C1; the recode was pinned and never shipped — sixth/seventh instance |
| C2 index undefined for εd; no mapping; no horizon; anchor line gone | ESCAPED-PIN (the line) + **REAL-NEW core** (definitions) | Step 3 (v0.7 core) |
| C3 Δ glossed as excess demand against D1; §1.2 vs §5.2 corner tension | **REAL-NEW core** | Step 3; audit rec-3 (derive the level axis) dissolves the class |
| C4 K2 deduction untestable; unattainable antecedent; register absorbs counter-examples; history objection | REAL-NEW core (harmonization fix-now) | Step 3/4; anchor C4 |
| C5 options guidance wrong (put-call parity, capped spreads, carry misapplied, P0 timing) | **REAL-NEW, mechanically decidable** | anchor C5; textbook fixes; candidate for earliest closure |
| C6 no loss state in decision/sizing rules | REAL-NEW core | Step 4; partially contested on the |Γ|-sign sub-point (the c-split was the answer; headline form fair criticism) |
| C7 §8.2 identity affine, not equal; sign breaks; g_usd unsourced | **ESCAPED-PIN** (V30 paragraph absent) + REAL-NEW (over-time point) | anchor C7 |
| C8 both DECIDED falsifiers unsound | REAL-NEW (falsifier hygiene) | Step 5 |
| M1 Γ mixes carry with price drift | REAL-NEW core | Step 3/4 |
| M2 K classifier holes; US "K1" vs own +0.2% real rate; splice; dual status vocabulary | MIXED: splice ESCAPED-residue (fix-now); holes + US-band contradiction REAL-NEW | anchor M2 |
| M3 hazard model: parameter count, ρ cap dual status, W2 mixture weight, W2-two-ways, headroom status, entry window, superseded form ordering | REAL-NEW (mixture-weight point is textbook survival analysis — accept); ordering = the ordering class (fix-now) | anchor M3 |
| M4 HBM two layers; bands-vs-meanings; observable gaps; layer-list exhaustiveness; "governing rule contradicts itself" | MIXED: HBM NEEDS-DISCUSSION; bands/observables REAL-NEW; the "contradiction" **CONTESTED** — classification-per-layer vs position-via-least-elastic operate at different levels; fix is a clarifying sentence, not a concede | anchor M4 |
| M5 9-of-60 cells; (K2,S0h,P1) long at peak exit hazard; no instruments; (K2,S2,P2) shorting into acceleration | REAL-NEW (the position map's internal tensions are the deepest applied-content finding) | anchor M5 |
| M6 silver reading stale/unsupported; recycling layer unscored | REAL-NEW; downgrade or evidence | anchor M6 |
| M7 §6.4 argues both sides; CPI omission; term-premium misuse; §6.4 vs §10.8 contradiction; section doesn't use the model's variables | REAL-NEW; the last sub-point is the deepest | anchor M7 |
| M8 falsifier defects (P0→P2 impossible by construction; latent-hazard test; counts; DECIDED-VACUOUS undefined) | REAL-NEW (falsifier hygiene) | Step 5 |
| M9 §8.3 smooth hazard vs §4.1 dated events; grow-together unestimated; miners carry; R notation | MIXED: hazard inconsistency REAL-NEW; miners **partially contested** (margin channel real, but the claim was about financing/storage carry — restate precisely); notation fix-now | anchor M9 |
| E1–E16 | REAL-NEW editorial, except: E4/E9/E14 cross-listed above; E15 symbol table = Step 6; E16 residual reference sweep | Step 6 |

## E. Close-out rulings (Alex, publisher, 2026-11-10)

1. **Step 0 confirmed.** v0.6.2's standing label is "published draft — substantive defects under review" (INDEX row 18, status column).
2. **The v0.6.x line is closed.** No v0.6.3 patch cycle. All findings — including this ledger's fix-now bucket — route through the v0.7 topic (`shared/unified-state-model-v07-review.md`, 33 anchors). The corrections path stays available only for a safety-level defect.
3. **v0.7's shape: split document.** Normative specification (current rules only) + change log (design notes, withdrawn text, review history) — Fable recommendation #10 adopted as the standing shape.

Implication for this ledger: no item above produces a patch against v0.6.2; every REAL-NEW / ESCAPED-PIN / NEEDS-DISCUSSION item is workload for the v0.7 cycle, worked through its anchors under the standing quorum rules.

## D. Process items (improvements topic filings)

1. Pinned-discharge verification as a permanent gate step (registry derived from resolutions, not hand-maintained — Duncan's checker proved the hand-maintained registry passes the broken document).
2. Absence assertions must cover *content*, not just labels (the line-127 splice lesson).
3. Preservation-test length floor is a blind spot for short load-bearing lines (C2's 40-char anchor sentence).
4. Test 5's `**Resolution`-opening exclusion + single-`\n` glue = silent content deletion (Thufir's §2.5 find).
5. Admission rule: a green gate certifies structure and provenance, never semantics; every publishable candidate gets at least one outside domain read before the word "publishable" is used. Produced twice in one night (Irulan, Fable).
