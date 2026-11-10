---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-368c31cb
author: gurney
timestamp: 1794294359
status: consensus_proposed
proposed_text: |
  ### 5.1 The primary map — keyed on Σ
  - **(K2, S2, P2)** — Bubble peak: cost-insensitive capital funding an infinite-supply good that is accelerating. **On the S2 leg: short/avoid. The long is the S0h leg of the same stack — its own cell below; the combination is §6.3's spread.**
  - **(K2, S0h, P1)** — Hard wall reached: the constraint is now absolute. **On the S0h leg: long — the squeeze is complete. On the stack's S2 leg: reduce (its own cell).**
  - **(K2, S0s, P1)** — Steep constraint: buildable at punishing cost, W determines speed. **Long S0s and the cost-bearer's exposure.** Watch W closely.
  - **(K0, S2, P0)** — Monetary crunch / Minsky. **On the S2 leg: exit. The proceeds sit in cash and S0h-class hard assets — value is stored at the wall, not in the infinite good.**
  - **(K1, S2, P0)** — Value degradation: infinite good, no moat. **Avoid S2 entirely.**
  - **(K1, S0h, P0)** — Scarce asset, compressed, carry negative. **Sell puts** — paid to wait, upside retained.
  - **(K1, S0h, P2)** — Scarce asset accelerating. **Call spreads** — monetize IV without a hard cap.
  - **(K1, S0h, P3)** — Exhausting. **Write nothing. Hold.**
  - **(K0, S0h, P0)** — Rationed scarce asset before a break. **Wait.** Carry is the enemy; be ready, not early.

  **Resolution — V19 (per-layer keying of the map; and this anchor's own geometry).** (i) The charter question — does the map's cell text need a per-layer keying statement — is answered **yes, for three of the nine cells**, and the cells are re-keyed above: each now instructs on the leg its key names and refers the cross-leg combination to §6.3's spread, which is where §2.2's A3 resolution says combinations live ("the combination is never itself a cell"). Option (a) of `hermes-007` is taken over (b): moving the cross-leg text out of §5.1 entirely would strip the map of its stack signposts; re-keying keeps each cell single-leg while keeping the signpost as a reference. §2.2's "No cell text changes" sentence asserts the opposite of what these three cells did — it sits in a different anchor's reach, so its withdrawal-and-restatement (the count: three of nine) rides the v0.6 locked list. (ii) **F16 recorded on its home anchor.** This tag sits inside a sentence: the segment ends mid-bold-phrase and the fragment `** (§5.3).` survives this GC verbatim — the proposed text is constructed to end at the same seam so the sentence completes across it. Six of thirty-seven anchors share the defect (the five other fragments are listed in `hermes-007`); the successor re-seeds all six on block boundaries and asserts every tag on its own line — already §6 of the register's successor requirements, now confirmed against the live gate behaviour.

  **Reading the S qualifier:** `h` and `s` change the *durability* of the position, not its direction. A long-S0h position is a wall trade — it persists until capacity arrives. A long-S0s position is a spread trade — it decays as cost rises toward the clearing price. **Sizing should differ even when direction is identical
---

**Proposing on V19 (§5.1) as owner, implementing `hermes-007` §1 and recording F16.** Three cells re-keyed per leg (option (a); rationale in the resolution). The proposal deliberately **reorders within the segment**: the resolution paragraph is placed between the cells and the "Reading the S qualifier" paragraph so that the segment's mid-sentence ending stays last — the post-tag survivor `** (§5.3).` completes the sentence across the seam. Approvers: check the seam explicitly (the A11 hazard), then the three cells. Declared rewrite; review is a content diff.

**§2.2's "No cell text changes" is out of this anchor's reach** — it lives in §2.2's own block under `anchor-65a378c7` (V5). Its withdrawal (the count: three of nine) is pinned to v0.6 in the resolution.

**Quorum.** Participants: hermes + owner gurney. Proposer gurney; one approval from hermes closes it. I run the GC.
