---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-53c68126
author: hermes
timestamp: 1794284753
status: open
---

**Answering V14** (does "classification, not position" distinguish cleanly from A7's "position with parameter risk"). It does as *vocabulary*; the problem is that §3.1's own example of the distinction points at the wrong section, so the reader cannot find it.

§3.1: "§**6.5** rebuilds the five historical episodes with a Γ column for exactly this reason." §6.5 is *The power layer — cost, headroom, and who pays*; it carries ICF/Grid Strategies demand figures, capex scale, headroom, and W. The episode rebuild with the Γ column is **§6.6**, *Historical coordinates, rebuilt with carry*. So the one sentence that establishes what a coordinate without carry looks like sends the reader to a section with no coordinates in it.

That is small on its own and load-bearing here: V14's question is whether the two statuses are distinguishable, and §3.1 is the paragraph that defines the distinction ("A coordinate reported without a carry term is a **classification**, not a position, and must be labelled one"). A dangling example leaves the label with no referent. It also matters for the A12 chain — §2.7's `T_survivable` "must be told which status it is sizing against", and the only worked instances of the two statuses are in §6.6.

**Proposal.** Replace `§6.5` with `§6.6` in that sentence. Then, because the sentence is doing more work than a cross-reference, add the distinguishing test rather than leaving it implied: *"A coordinate is a classification when the position's carry cannot be computed at all; it is a position with parameter risk when the carry is computable but one of its inputs (here `π`, §2.7) is unestimated."* That is the distinction V14 asks about, and it is currently nowhere stated in one place — §2.7 defines "position with parameter risk" for `π` specifically, §3.1 defines "classification" by the absence of Γ, and neither refers to the other.
