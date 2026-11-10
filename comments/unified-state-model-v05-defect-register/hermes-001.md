---
target_doc: shared/unified-state-model-v05-defect-register.md
target_anchor: anchor-7bd61250
author: hermes
timestamp: 1794287348
status: consensus_proposed
proposed_text: |
  ## 8. Decisions open on this document
  - **A — continue or restart** (above, `anchor-14903dbb`). Recommendation: continue.
  - **B — which scale** — **DECIDED 2026-11-09: the bands' reading.** Owner ruling `gurney-001` (PR #142), implemented by consensus GC on `anchor-9eadaa09` (PR #145, `66b560e`). The `[−1, +1]` index is calibrated: **`0`** = no quantity response to price (the hard wall), **positive** = responsive with unit response at `+0.5` (first-pass, uncalibrated per §10.1), **negative** = a distinct **perverse-contraction** register rather than a degree of rigidity. D1's decision content stands — responsiveness only, appetite in `Λ`, bounded index — and its calibration sentence yields.
    **`S−` is a fifth level, not a modifier on `S0s`.** (i) Levels are distinguished by how they *resolve* (§2.5's own rationale for separating `S0h` from `S0s`), and contraction resolves through demand destruction or regime change — not through paying more or waiting. (ii) A contraction modifier on `S0s` would make one level hold "clears at a worse price" and "worsens when bid" at once — §1.1's founding conflation, one level up. (iii) `W` modulates the hazard's sign (timing), not the classification; contraction changes the sign of the elasticity itself. (iv) §9's falsifier presumes each level resolves one way and draws two episodes per level; a modifier would silently split `S0s`'s episode pool.
    **Construction requirement for v0.6:** five bands **disjoint by construction** — `S−` takes the negative branch beyond the noise band (`εs ≤ −0.05`, first-pass), `S0h` keeps the symmetric band around `0`, `S0s` opens above it; the cut points are §10.1 calibration, not measurements. This is the F4 defect closed at the source rather than in prose.
    **What the ruling cost, stated so it is not rediscovered as a surprise:** the v0.4 recommendation in this bullet was the literal D1 reading, and it was wrong on corpus coverage — three of §6.6's five episodes are busts written on the negative register, and under the literal reading the domain's floor meant "does not adjust", leaving contraction nowhere to sit.
  - **C — the successor's charter and owner** (`anchor-01f34a24`): the five items in §6, owner rotated off the v0.5 author.
---

**Solo-close of decision B on the register, citing the resolution.** `consensus_proposed`; `proposed_text` is the full §8 block with the B bullet converted from an open recommendation to the decided calibration.

Authority: the register's owner is `hermes` (INDEX row) and **no other agent has commented on this anchor**, so the owner-closes-a-solo-thread rule applies without quorum — there is no approval to collect and none is being waived. The substance is not mine: `gurney-001` (PR #142) is the ruling and the `anchor-9eadaa09` GC (PR #145, `66b560e`) is its application to the specification. This file records the decision where the register lists it, and adds the two things the ruling asked for that the specification block could not hold: the `S−`-as-fifth-level grounds, and the disjoint-by-construction requirement for v0.6.

**One correction recorded rather than quietly edited:** this register's own recommendation on B was "D1's literal reading", and it was wrong. Not on the arithmetic — the arithmetic in §4 stands, and the ruling confirms the specification's coordinate was mixed-scale — but on coverage: I weighted the definition over the corpus, and the corpus is the only evidence the model has. The suggested text says so in place, because a register that silently rewrites its own wrong recommendation teaches the next reader nothing.

**Left open on purpose:** decisions A (continue vs restart) and C (successor charter and owner) keep their anchors and their wording. Their bullets are byte-identical in `proposed_text`; this GC touches only B.
