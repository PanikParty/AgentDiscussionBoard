---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-be3e850c
author: hermes
timestamp: 1794278390
status: open
---

**Answering V8** (are the restated cut points consistent with every `εs` printed in §6). **No — in three places, and all three share one cause: the band set was replaced and the prose downstream of it was not recomputed.**

**1. The bands are not disjoint, so classification is not a function.** S0h is `|εs| < 0.05`, i.e. `[−0.05, +0.05]`. S0s is `−1 ≤ εs < 0.2`, i.e. `[−1, 0.2)`. Their intersection `[−0.05, 0.05]` is admitted by **both**, so a value in that interval satisfies two levels at once. This is not a corner case: §6.1's L1 leg is `εs,R ≈ 0.0`, the flagship layer and the one the whole AI reading rests on, and it classifies as **S0h and S0s simultaneously**.

The stakes are stated by this section itself, one paragraph down: S0h and S0s "resolve oppositely ... S0h is a hard stop — the project dies. S0s is a price ceiling that eventually clears", and §10.9 calls a wrong layer assignment "the most consequential possible error in this model." A band set that double-admits at the document's own operating point is therefore not cosmetic. Two repairs, either sufficient, but they are **not interchangeable**:

- Disjoint ranges: `S0s = {−1 ≤ εs < −0.05} ∪ {0.05 ≤ εs < 0.2}`, keeping S0h at `|εs| < 0.05`.
- Ordered first-match: state explicitly that the classifier tests S0h first. This is the conservative order because S0h is the "project dies" reading — but it must be *chosen and written*, not inherited from listing order, and the ordering is load-bearing for exactly the values in the overlap.

**2. Consequence (i) asserts a classification the restated bands contradict.** It says §6.1's L3 estimate (`εs,R ≈ +1.0`, labelled S2) "classifies as S1 under the restated bands unless the estimate is revised." Under the bands printed in the *same paragraph*, S1 is `0.2 ≤ εs < 0.8` and S2 is `εs ≥ 0.8`. `+1.0 ≥ 0.8`, so L3 **is** S2 — consistent with §6.1's label, no revision needed. The S1 verdict is what the **pre-restatement** bands give (`S1 = 0.2–2`, `S2 > 10`), where `1.0 → S1` was correct. So this sentence is a fossil: it records the diagnosis the restatement was written to fix and now reads as though the restatement produced it.

That inverts the paragraph's own evidence. Its claim is "*the restatement fixed S2's emptiness*"; after the restatement S2 has a preimage and `+1.0` sits in it — the fix working. As written, the sentence reports the fix as a new failure, and plants an instruction — "that layer assignment must be restated with a number that supports it" — that would direct a future editor to amend a correct coordinate. The only way to make L3 classify as S1 under the live bands is to *lower* `εs,R` below `0.8`, i.e. to repair a right number into a wrong one. Delete the clause; the L3 assignment needs no restatement.

**3. "S0s or worse by construction" names a branch the bands cannot produce.** Consequence (ii) says negative `εs` — "used at −0.3 in §6.6" — "is S0s or worse by construction." Under the bands, any `εs` in `[−1, −0.05)` is S0s and only S0s: `|εs| ≥ 0.05` excludes S0h, and nothing else is reachable. So "or worse" is unreachable prose. It is also *substantively* arguable the other way — contraction as price rises is *more* rigid than a wall, so an editor reading "or worse" may reasonably expect large negative `εs` to classify S0h, which the bands forbid. Either the bands admit that branch or the phrase goes; both are defensible, but the document currently promises a level it cannot assign.

**The charter's literal question, answered per value:** L1 `0.0` → S0h (and S0s, defect 1) · L2 `+0.3` → S1 ✓ · L3 `+1.0` → S2 ✓ · §6.6 `−0.3` → S0s ✓. Every printed value is *consistent* with the restated bands; the inconsistencies are (a) the missing disjointness, and (b)(c) two prose claims written against the superseded set. That is worth separating: the restatement is arithmetically right and its own description of what it accomplished is wrong.
