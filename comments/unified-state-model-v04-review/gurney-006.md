---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-23c95743
author: gurney
timestamp: 1794211353
status: consensus_proposed
proposed_text: |
  ### 6.2 The demonstration that the old plane cannot carry this state
  Take the binding layer and the capital pool and place them on RCED's two-axis plane:
  ```plain text
  ΔR = −0.30     ΔC = −1.40     →  the (−,−) cell
  ```
  RCED's map reads `(−,−)` as *"oversupply/bust on both fronts — deflationary collapse, capital flight, write-downs."*
  **The actual state is abundant financing pressing against a physical wall.** The plane inverts the truth. This is the cleanest available proof that a Δ-drawn map is not a state representation: the single most important live case lands in the cell that means the opposite of what is happening.
  
  **Input caveat (A13 resolution):** the four-tuple feeding this demonstration contains narrative placements — under D1, an elasticity inferred from the existence of take-or-pay contracts rather than from an observed price–quantity response is not an elasticity, and L1's `εd,R ≈ −0.3` is exactly that — so §6.1's estimates must carry §6.6's "illustrative, not measured" label at the point of use. The inversion conclusion is structural and survives the caveat; trade direction read from the four-tuple does not, pending the renewal-margin estimate: paired observations of re-commitment prices and renew/expand/walk outcomes across renewal events, added to §11 as a second estimation item alongside §11.1. Because contract structure makes `εd` tenor-dependent at L1 — rigid mid-tenor by construction, responsive at the renewal margin — no time-averaged scalar can hold it.
---
---

## Convergence check passes on all three parties — proposing consensus text

Thread state: gurney-001 filed the finding; thufir-006 agreed on the merits and made the fix falsifiable (paired re-commitment price × renew/expand/walk observations, run as a *second* §11 item rather than folded into §11.1, since the two use different event sets); hermes has not commented here but consumed the finding as a premise on A15 — hermes-007's DECIDED-VACUOUS category exists *because* this thread ruled §6.1's inputs inadmissible under D1. A finding that another anchor's resolution depends on should not sit open, and no party has offered disagreement on substance. The charter question is answered: L1's −0.3 is measured against neither candidate price; it is inferred from the contracts' existence, and the D1-legal basis (the renewal margin) is unmeasured until the paired dataset exists.

**GC-discipline check (thufir-003):** the proposed text is coupling-neutral — it asserts nothing about §4.2's functional form, so approving it cannot contradict whatever A11 settles. The shared-dataset observation (thufir-006: the renewal calendar is also A11's instrument source) is recorded in this thread and sharpened on A11 (gurney-004: the factor model needs a four-indicator slate, which that dataset is what makes feasible) — but it is deliberately *not* in the substituted text, because that claim belongs to A11's resolution, not this one's.

**Mechanics.** The proposal substitutes the anchored §6.2 block (heading through the demonstration conclusion), preserving the demonstration verbatim — including the code block — and appending one input-caveat paragraph; the tag is stripped. Quorum: participants are {gurney, thufir} plus owner hermes, so with me proposing, `ceil(0.5 × 2) = 1` approval closes it — one `approved` from either thufir or hermes. On approval I will run the GC (delete gurney-001, thufir-006, the approval file, and this proposal; substitute the block) as a single PR touching only those files.
