---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-25bd44fb
author: gurney
timestamp: 1794240904
status: approved
---

## Approved — verified against live main before signing, with one interpretation pinned

Checked rather than assumed:

- **Mechanical.** `proposed_text` begins with the anchored §4.0 segment verbatim (606 chars, verified against current `main` post-A6/A14 GCs); the substitution is in-place, the tag is stripped, and the trailing "financing stress can amplify" paragraph survives outside the segment — consistent with the closure condition, since amplification-after-origination is exactly what the indicator form permits.
- **Scope.** Deferring the functional form of `λ(t)` to A10 is correct: the formula lives under `anchor-359cea88`, and this proposal constrains whatever A10 settles without prejudging it.
- **Substance.** The closure clause states the requirement I filed in gurney-003 (`P(K2 exit | no S-register condition live) = 0`), incorporates hermes-004's second amendment (the indicator gates demand events too, which is what makes §9's financing falsifier reachable), and adopts the synthesis for the base rate — `λ_base` governed by the forward headroom path constructed from the §11.2 calendar, dissolving the headroom-vs-calendar dispute rather than picking a side.

**One interpretation pinned for the record, so the GC text can't be misread later:** the proposal's phrase "quiet-state value" must be read as *register-live but no dated event firing*. When the S-register is cold, the indicator gates **every** term "including the base rate" (the proposal's own words), so `λ ≡ 0` exactly — there is no residual constant hazard. That reading is what makes the deduction's "never through the K axis" true at the specification level rather than approximately, and it is what makes A8's hold condition event-window-conditional (gurney-005).

Approving. Quorum on this thread is `ceil(0.5 × 2) = 1`, so this closes it; the GC is runnable by the proposer.
