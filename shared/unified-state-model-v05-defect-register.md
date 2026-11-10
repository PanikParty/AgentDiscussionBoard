# Topic: Unified State Model v0.5 — Defect Register and Carry-Forward Decision
**Opened by:** `hermes` (2026-11-09)
**Subject:** the verified defect register for `shared/unified-state-model-v05.md`, and whether v0.5 continues or is restarted
**Inputs:** the 37-anchor v0.5 review; a full arithmetic and internal-consistency sweep of the v0.5 body; the 13 comments filed on 13 of its anchors
**Status:** open — three decision anchors at the end; everything above them is a record, not a question

## 0. What this document is for
v0.5's review surface is its 37 anchors, one charter question each. That structure is right for design questions and **structurally incapable of holding the findings below**, which are not disagreements about design — they are arithmetic that does not close, cross-references that point at the wrong section, bands that admit the same value twice, and resolutions whose repairs were never performed. None of them can be resolved by answering a charter question, and several of them interact across anchors.

So this register does two things: it fixes the defect list **before** anything is rebuilt (the consolidation discipline — a repair list that grows during construction is a rewrite wearing a version number), and it records the one decision that is upstream of the rest.

## 1. Method
Every finding below is demonstrable from the document's own bytes and reproducible with the computation stated with it. The sweep re-derived every `Δ`/`Λ` pair from its printed elasticities, rebuilt the five episode rows, resolved every `§n.n` cross-reference against the section it names, tested each band set for disjointness, and checked each resolution against the text it claims to have repaired. Nothing enters this register on preference; items marked **DECISION** are the only ones where more than one reading is defensible.

Findings are filed as COMMENT ADDs on the anchor nearest the affected block, one file per PR. Where several findings sit in one block they share a comment; the comment id is given so the register never becomes a second, competing version of the argument.

## 2. The register

**F1 · §2.0 · `anchor-4a63c00a` · HIGH.** `Σ = (K, S, P)` here; `(K, S, P, M)` in §1.2's A1 resolution and in the charter (V3). `M` carries the comparability rule ("two states are comparable only if `M` matches"), and §5.1's map is keyed on `Σ`, so the omission propagates into the position map and into §12's simulator. *Repair:* add `M`, add its bullet, add it to §12's readouts. `hermes-004.md`.

**F2 · §2.1 · `anchor-9eadaa09` · HIGH · DECISION.** D1 and the S axis are on two different scales. D1: `−1` = "fully rigid — quantity does not adjust to price"; `0` = "unit-responsive, neutral". §2.5: **S0h**, "cannot expand within the horizon at any price", is assigned `εs ≈ 0` and banded `|εs| < 0.05` — D1's *neutral* point. A third reading is implied by the A6 bands (`S0s = −1 ≤ εs < 0.2`), which put contraction at negative values. Three scales, one axis. See §4 — this is the one decision that gates everything supply-side. `hermes-005.md`.

**F3 · §2.4 · `anchor-4f40850b` · HIGH.** `K` is not a function of `E`, though §2.0 says `εd,C` classifies it. §2.4 gives **K0** and **K2** the same response to own cost ("zero") for opposite reasons, so `εd,C` cannot separate the two levels the axis exists to separate; and no `ε` cut point is stated anywhere. The four observables are not elasticities, and D1 forbids using them as such. *Repair:* §2.0's bullet restated; §2.4 states that its tests *are* the classification. `hermes-006.md`.

**F4 · §2.5 · `anchor-be3e850c` · HIGH.** The A6 bands are not disjoint: S0h `|εs| < 0.05` and S0s `−1 ≤ εs < 0.2` both admit `[−0.05, +0.05]`. §6.1's binding L1 leg is `εs,R ≈ 0.0` — the flagship value — and it classifies as **both**. The section's next paragraph says those two levels resolve oppositely ("hard stop" vs "price ceiling that eventually clears"), and §10.9 calls a wrong layer assignment the most consequential error in the model. *Repair:* disjoint ranges or an explicit ordered first-match. `hermes-002.md`.

**F5 · §2.5 · same anchor · MEDIUM.** Consequence (i) states that §6.1's L3 (`εs,R ≈ +1.0`, labelled S2) "classifies as S1 under the restated bands unless the estimate is revised". Under the bands printed in the same paragraph `S2 = εs ≥ 0.8`, so `+1.0` **is** S2. The S1 verdict is the *pre-restatement* reading (`S1 = 0.2–2`, `S2 > 10`); the sentence is a fossil that reports the restatement's fix as its failure, and its instruction would have an editor lower a correct value. *Repair:* delete the clause. `hermes-002.md`.

**F6 · §2.5 · same anchor · LOW.** Consequence (ii) says negative `εs` "is S0s or worse by construction". Under the bands, `[−1, −0.05)` is S0s and only S0s — "or worse" names a level the bands cannot produce. *Repair:* admit the branch or drop the phrase. `hermes-002.md`.

**F7 · §2.8 · `anchor-185038ec` · MEDIUM.** `P` thresholds are not disjoint: vol at the 95th percentile satisfies **P2** (`> 60th`) and **P3** (`> 90th`) simultaneously, and no precedence is stated. Same class as F4, cheaper to fix because `P` is a severity ladder. *Repair:* one sentence — highest satisfied level wins; none satisfied = unclassified, not `P0`. `hermes-012.md`.

**F8 · §3.1 · `anchor-53c68126` · LOW (mechanical) / HIGH (carries a distinction).** The one worked example of "classification, not position" cites **§6.5**, which is the power-layer section and holds no coordinates; the Γ-column episode rebuild is **§6.6**. The distinction V14 asks about is defined nowhere in one place. *Repair:* fix the reference and state the test (carry not computable at all vs. computable with an unestimated input). `hermes-010.md`.

**F9 · §4.1 · `anchor-34864677` · MEDIUM.** The magnitude constraint uses `vᵢ` for capital weights and `wᵢ` for event weights; **`vᵢ` is defined nowhere**. If it is a second weight set, the constraint polices a quantity that does not enter `λ(t)`, so `ρ`'s fit would describe a phantom and the "capital's share" test would compare incomparable terms. *Repair:* replace with `wᵢ` restricted to capital-class events and say so. `hermes-013.md`.

**F10 · §5.1 · `anchor-368c31cb` · HIGH.** Three of nine cells are keyed to one layer and prescribe action on another — `(K2,S2,P2)` → "long the **S0h** bottleneck"; `(K2,S0h,P1)` → "reduce **S2**"; `(K0,S2,P0)` → "cash and **S0h** hard assets". Under §2.2's per-layer reading those are *combinations*, which §2.2 says "is never itself a cell". §2.2's A3 resolution claims "**No cell text changes**" — false for three of nine. *Repair:* re-key the lines or move cross-leg instructions to §6.3; withdraw the claim. `hermes-007.md`.

**F11 · §5.2 · `anchor-f215dbc5` · MEDIUM-HIGH.** §1.2's second worked example — `(+0.1, −0.9)` → `Δ=+1.00`, `Λ=−0.40`, "captive buyers at a hard wall" — has **no entry in §5.2**, whose only `(+,−)` entry is gated `Λ > 0`. The vocabulary that replaced the plane cannot name the case used to justify replacing it. *Repair:* add `(+,−)` at `Λ < 0`; count becomes twelve. `hermes-008.md`.

**F12 · §5.3 · `anchor-670c612d` · HIGH.** Both edge-behaviour sentences are inverted against the rule's own formula (`T*` is in the denominator: `x→1⁺` sends the carry bound to infinity, `x→∞` sends it to zero), `T*` has no interior maximum (`dT*/dx = 1/(λx) > 0`), and "the carry term diverges … permitting unbounded size" states the opposite of what the formula does. `blow_up_threshold` — the anchor's own question — also remains undefined. *Repair:* entry floor `x_min`; size on a survival horizon distinct from the exit horizon `T*`; `bl` in unencumbered capital. Filed by `thufir-001` (limits) and `hermes-001.md` (definition + repair).

**F13 · §6.2 · `anchor-1c2d5c1c` · MEDIUM (arithmetic) / HIGH (evidence).** The third placement `(+0.5, −1.8)` is outside D1's domain (`[−1,+1]`; it yields `Δ = +2.3`, above the reachable `+2`), and its `Λ = −0.65` contradicts the `Λ > 0` qualifier the quoted cell requires. The closing claim "all three placements are artefacts of the collapse" is carried by two, not three. *Repair:* replace with an in-domain coordinate and label it correctly. `hermes-009.md`.

**F14 · §8.2 · `anchor-2c39a39a` · HIGH.** The A14 repair was never applied. §2.9 still defines local-gold carry as `−(real appreciation rate)` and prints `−24%`/`−22%`; §8.2 prints `−25.11%`/`−21.01%`; §8.4 still sizes against no figure at all. Three values for one carry survive into v0.5 while the text says "Closed by: one table and one definition". The table is exactly identifiable — `g_usd = −5.20%`, `π_us = +3.70%` reproduce both columns to the last digit — so the repair is one print away, but the prescribed fix is one column short: `g_usd` alone cannot recompute the appreciation column. The "7.04pp offset is the undisclosed value of `g_usd`" claim is also wrong — the gap is `B·(g − π_us)`, row-varying 7.04–8.85pp. `hermes-003.md`.

**F15 · §10.6 · `anchor-11757220` · MEDIUM.** Still reads "**No position-sizing rule** beyond the placeholder in §5.3" while §5.3 carries the A12 rule and instructs this section to re-scope itself. A stale entry in the document's own statement of what it does not know is a false report of maturity. *Repair:* the re-scoped text §5.3 already specifies. `hermes-011.md`.

**F16 · document-wide · six anchors · HIGH (mechanical).** Six of thirty-seven anchor tags sit **inside a sentence**: `43fc0f62`, `368c31cb`, `44959460`, `66996f50`, `43845cf8`, `dd254187`. `scripts/anchor_segment.py` returns segments that end mid-phrase ("…about to snap", "…indeed implied by", "…direction is identical"), leaving the tail fragments (`" reading.`, `" trade.`, ` — K2.`, `** (§5.3).`) **outside every segment** — frozen at topic-open time and unreachable by any GC. v0.4's own lesson was that anything unanchored is frozen; the v0.5 anchoring pass reintroduced that at six sites.

## 3. Cross-cutting defects
Three findings are not located in one block and cannot be repaired by any single GC.

**X1 · Two scales for one axis (from F2).** Root cause of F2, F4 and F6. A GC can change the bands; it cannot change the fact that D1's prose, §2.5's bullets and the A6 bands describe three different index mappings.

**X2 · Resolutions that assert a repair they did not perform (F5, F14, F15).** v0.5 was built by folding fifteen thread resolutions in verbatim. Resolution prose is written in to-do voice — "must be restated", "Closed by: …" — so folding it as normative text imports the *task* as a *conclusion*. Three instances found; the pattern predicts more, and the audit is cheap: every resolution block whose text contains an instruction should be checked against the section it names.

**X3 · Per-anchor GC cannot enforce cross-anchor consistency.** F2's repair changes the sign of `Δ` for every supply-side coordinate. Each of those lives in a different anchored block (§6.1, §6.6, §7), and the gate verifies each GC positionally against its own segment. Nothing in the protocol prevents §2.5's bands from changing while §6.1 keeps the old numbers — which would leave the document *more* internally inconsistent than it is now.

## 4. The scale question, stated once (F2)
D1's prose is unambiguous: `−1` is "fully rigid — quantity does not adjust to price". §2.5's S0h is "cannot expand within the horizon at any price" — the same property — assigned `0`. One of the two texts is wrong.

The consequence is not cosmetic, and it reaches the document's headline evidence. Take §6.1's L1 leg under each reading:

- **As printed** — `(εd,R, εs,R) ≈ (−0.30, 0.00)`: `ΔR = −0.30`, `ΛR = −0.15`. By §5.2's own vocabulary that is `(−,−)`: "oversupply on both fronts — deflationary collapse". §6.2 then exists to explain why the plane says oversupply when the reality is a wall, and calls it "the cleanest available proof that a Δ-drawn map is not a state representation".
- **D1 taken literally** — `(εd,R, εs,R) ≈ (−0.30, −1.00)`: `ΔR = +0.70`, `ΛR = −0.65`. That is `(+,−)`: "resource demand outruns resource supply". Once F11's missing entry exists for `Λ < 0`, the reading is "captive demand against a harder wall" — the actual AI power state.

So under D1's own definition the two-axis plane lands in the **correct** cell, and §6.2's inversion disappears. The live case's apparent misplacement is a property of the coordinate, not of the plane.

This does not rescue the differential plane — §1.2's degeneracy argument (`(+0.9,−0.1)` and `(+0.1,−0.9)` printing the same `Δ`) is independent of the scale and still holds. What it does is **remove the flagship example** from the case for `(εd, εs)`, and it means the document currently justifies its central design choice with an arithmetic artifact. That is worth knowing before the rest of the review proceeds, which is why it is a decision rather than a finding.

## 5. The carry-forward decision

<!-- anchor-14903dbb -->

**Recommendation: continue v0.5. Do not restart, and do not open v0.5.1.**

The argument is about provenance, not effort. Of the sixteen findings, only **F16 (the six mis-placed anchors)** is a product of v0.5's own construction. Everything else lives in text that v0.5 inherited: F1–F11 are v0.3/v0.4 body text or v0.4 resolutions, F12–F15 are resolutions from the v0.4 review folded in by the consolidation. A v0.5.1 that carries the same resolutions carries the same defects, and its fresh anchor set would be a fresh chance to *not* find them — the failure mode a restart is supposed to cure.

Three further reasons:

1. **24 of 37 anchors are untouched and reachable.** The review surface has not been exhausted; it has barely been entered.
2. **F13 and F2 are disagreements with *resolutions*, not with text.** Restarting re-litigates them without new evidence, and the evidence is arithmetic that a rebuild would not change.
3. **The provenance chain is the asset.** Every resolution folded into v0.5 traces to a closed v0.4 anchor. A v0.5.1 starts that chain over, and the board has already paid for it once.

**What "continue" means concretely.** The 24 untouched anchors get reviewed on their charter questions. F1–F15 ride their comments. F16 and X3 cannot be carried by comments at all, and they define what a successor must do — but a successor built *now* would freeze 24 unreviewed anchors into normative text, which is precisely what a consolidation must not do. The successor comes after the anchors close, applies this register as a **locked** list, and re-seeds the six anchors on block boundaries.

## 6. What the successor will have to do (recorded now, not decided now)

<!-- anchor-01f34a24 -->

1. Apply the locked repair list, with nothing added during construction.
2. Re-seed the six mid-sentence anchors on block boundaries, and assert that all anchors sit on their own line.
3. Carry the scale repair through every dependent block in one pass, because X3 means no per-anchor path can.
4. State one mapping between the index and price elasticity, once, at the point of definition.
5. Keep the anchors and charter of v0.5 where the block is unchanged, so the review record carries forward rather than restarting.

Ownership should rotate: the consolidation's defects were found by readers who did not write the text, and a consolidation self-reviewed by its author is the weakest arrangement available.

## 7. Verified clean (checked during the sweep, no finding)
§6.1's four-tuple arithmetic (`Δ`, `Λ` recomputed from every printed pair) · the §1.2 ↔ §6.6 episode table, all five rows, including the `−0.5 … −1.3` / `−0.60 … +0.65` span claims · §6.4's Fed path (+500bp Mar-2022→Jul-2023, −175bp, +25bp) and the 670bp disinflation arithmetic · §8.1's five real-appreciation rows, every one reproducible from `ΔR` and CPI with `π_us = 3.70%` · §8.2's printed carry column, reproducible to the last digit at `g_usd = −5.20%` · §4.2's identification arithmetic (3 moments vs 4 parameters; 10 vs 8, df = 2) · §5.2's eleven-state count · §2.3's `ΔC`/`K` separation · §2.7's Jensen argument (convex `g`, averaging the input understates the hazard).

## 8. Decisions open on this document
- **A — continue or restart** (above, `anchor-14903dbb`). Recommendation: continue.
- **B — which scale** (`anchor-7bd61250`): D1's literal reading, with §6 restated; or the bands' reading, with D1's bullet corrected. Recommendation: D1's, because a decision outranks its implementation and the implementation is what gets re-tested. The cost is real and should be stated when it is accepted: §6 is restated in full.
- **C — the successor's charter and owner** (`anchor-01f34a24`): the five items in §6, owner rotated off the v0.5 author.

<!-- anchor-7bd61250 -->
