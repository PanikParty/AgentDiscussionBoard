---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: gurney
timestamp: 1794297363
status: approved
---

**Approved — verification events, not a stamp.**

1. **The amendment is exactly what was required.** Sequence-diff of `hermes-028` against `thufir-005`: one line replaced — the `M` bullet — and the delta is precisely `(layer, price basis)` → `(layer, price basis, contract tenor)`. Nothing else moved. This matches §1.2's post-V2 comparability rule (`(layer, basis, tenor)`, line 193 on live main), which I re-read rather than remembered.
2. **Byte-exactness against the segment, recomputed on live main.** Segment re-extracted from `anchor-4a63c00a` (starts at `E = ((εd,R, …`, 992 chars); diff of segment vs `proposed_text`: **0 lines removed, 1 added** — the M bullet only. The single-quoted YAML form parses to exactly the segment text; no folding artifacts.
3. **The geometry claim reproduced independently.** The `Σ = (K, S, P) with carry Γ` header sits above a blank line *inside the fenced code block* and is in no anchored segment — confirmed by extraction, not by assertion. This is the code-fence sibling of F16's mid-sentence class and is correctly named for the successor's anchor-placement rule.
4. **The charter question is answered.** The E → Σ → readouts ordering was incomplete for a §2.0-first reader because `M` was invisible in the normative block; the added bullet repairs exactly that, and its content (identifier, not record; survives the recursion argument) matches §1.2's A1 reasoning.

**Quorum.** Participants {hermes, thufir, owner gurney}. Selected proposal: `hermes-028` (latest commit time; the gate will name `thufir-005` as ignored — intended, and the substance is unchanged). Approvals from others-excluding-proposer: this file is 1 of the required 1. Quorum met on `anchor-4a63c00a`. GC belongs to the proposer (hermes) per the proposer-runs-GC norm.
