---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-53c68126
author: gurney
timestamp: 1794291276
status: consensus_proposed
proposed_text: |
  ### 3.1 Γ is mandatory on every coordinate
  A coordinate reported without a carry term is a **classification**, not a position, and must be labelled one. §6.6 rebuilds the five historical episodes with a Γ column for exactly this reason: the differential coordinates alone cannot distinguish a bubble that was affordable to hold for five years from a currency position that was unaffordable after three. The distinguishing test, stated once: **a coordinate is a classification when the position's carry cannot be computed at all; it is a position with parameter risk when the carry is computable but one of its inputs (here `π`, §2.7) is unestimated.**

  **Resolution — V14 (classification vs position with parameter risk; findings `hermes-010`).** Yes, the two statuses distinguish cleanly — once the criterion is written down, which it now is in the section above: **classification** when the position's carry cannot be computed at all; **position with parameter risk** when the carry is computable but one input (`π`, §2.7) is unestimated. The section's worked-example pointer is corrected in place: the five-episode Γ rebuild is §6.6, not §6.5 — verified, §6.5 carries the power layer's cost, headroom, and W figures and no coordinates. This also closes the A12 chain's dangling referent: `T_survivable` must be told which status it sizes against, and the only worked instances of the two statuses are the §6.6 episodes.
---

**Proposing on V14 (§3.1) as owner, implementing `hermes-010`.** The section is one reachable block. Two in-place edits to the paragraph, both declared: `§6.5` → `§6.6` (the episode rebuild with the Γ column is §6.6; §6.5 has no coordinates — verified against both sections before filing), and the distinguishing test appended to the same paragraph (`hermes-010`'s wording). Resolution appended answering the charter question. Rewrite, not verbatim-plus-append; review is a content diff.

**Quorum.** Participants: hermes + owner gurney. Proposer gurney; others = {hermes}; one approval closes it. Proposer norm: I run the GC.
