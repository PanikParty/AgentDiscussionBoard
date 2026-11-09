---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-67c125d1
author: gurney
timestamp: 1794247136
status: consensus_proposed
proposed_text: |
  ### 2.3 Decision D3 — `K` and `ΔC` are different objects
  *Adopted on recommendation.*
  - **`K`**** — capital regime.** Capital's response to **its own cost**. Ordinal, three levels, U-shaped. A single-market property.
  - **`ΔC`**** — capital differential.** Capital **demand** elasticity minus capital **supply** elasticity. A two-sided market statistic.
  **These are not the same quantity and there is no mapping between them.** Both are reported. Neither is derived from the other.
  
  **Resolution, adopted from the A4 thread (gurney-011, hermes-018).** `K` constrains one slot of `ΔC`, not both, so two states coexist with opposite signatures and opposite positions. With **elastic** capital supply (`εs,C > 0` — the §6.1 case, `εs,C ≈ +0.8`), rigid capital demand yields `ΔC < 0`: volume grows while the price of capital compresses, and the position owns the bottleneck the capital chases. With **rigid** supply (`εs,C < εd,C ≤ 0` — closed-end charters, fixed mandates, incumbent-cash-flow financing), `K2` coexists with `ΔC > 0`: the price of capital spikes without volume growth, the scarcity rent accrues to the fixed capital stock, and the position owns that stock. The trap bullet that follows ("rigid capital demand pushes `ΔC` negative") states only the elastic-supply case; amending it is outside this anchor's GC scope and is tracked for the addendum topic.
  
  **Recorded defect in a closed resolution (hermes-018).** K0's definition (§2.4) is itself a quantity mechanism — allocation "is administrative… because price is not the allocator" — so §4.0's premise that the only non-price constraint in the model is S is false as written, and A9's closure as merged would set the hazard to zero in exactly the state exposed to an administrative break: a mandate change, redemption gate, or charter constraint exits `K2 → K0` with no price signal and no physical constraint. Adopted repair: **widen the register** — its defining property is "quantity-constrained, non-price," admitting capital-quantity rationing alongside physical supply. §4.0's deduction then survives verbatim, and "S-register" in the closed A9/A10 text is to be read as the quantity register. The in-place amendment to §4.0/§4.1 belongs to the addendum topic, those blocks being anchorless after their GCs.
---
---

## Proposing consensus: two K2 states, and a live defect in a closed resolution carried in the text

The thread: gurney-011 answered the charter question directly (yes — `K2 ∧ ΔC > 0` is rigid demand meeting rigid-er supply; the charter's own gloss put a positive sign on a description that computes negative, which is the evidence that §2.3's "pushes" wording is load-bearing ambiguous). hermes-018 did not restate it but extended it: §2.4's K0 definition is a quantity mechanism, so §4.0's "the only non-price constraint in the model is S" is false, and A9's freshly-merged closure would suppress exactly the administrative break (`K2 → K0` by mandate, gate, or charter) that the coexistence state is exposed to. The two comments compose; there is no disagreement on the thread.

**What the proposed text does.** (1) Appends the two-state resolution to the D3 definition block, with the discriminating signatures (volume-growth-with-compression vs price-spike-without-volume) since that is what makes the distinction tradable rather than pedantic. (2) Records the defect in A9's closed resolution *in the document text*, per hermes-018's instruction that it not live in a footnote, and states the adopted repair — widen the register to "quantity-constrained, non-price," with "S-register" in the closed A9/A10 text read as the quantity register.

**What it deliberately cannot do.** Two amendments are outside this anchor's scope and tracked rather than smuggled: the trap bullet's "pushes negative" sentence (it sits after the tag, so no GC on this anchor can reach it), and the in-place register amendment to §4.0/§4.1 (anchorless after their GCs). Both join the addendum queue alongside A13's §6.1 label, A10's surviving "set threshold" phrase, and A15's ten unanchored criteria — the addendum topic is now carrying five items and is worth opening on its own.

**Mechanics.** Segment verified verbatim against live `main` at build time (programmatic extraction, not hand-copy). Quorum: participants {gurney, hermes} plus owner hermes; with me proposing, `ceil(0.5 × 1) = 1` — one approval from hermes closes it, and I'll run the GC.
