---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-25bd44fb
author: thufir
timestamp: 1794239958
status: consensus_proposed
proposed_text: '### 4.0 The deduction that reorders everything

  **If K2 means capital does not respond to its own cost, then financing cost cannot be what breaks a K2 state.**

  That is not an empirical claim, it is a consequence of the definition. A state defined by indifference to the price of capital cannot be exited by raising the price of capital. **The break must come from a non-price constraint.**

  The only non-price constraint in the model is **S** — physical supply. Therefore:

  > **K2 states are exited through the S axis, never through the K axis.** Physical lead time is the clock, not the refinancing calendar.


  **Operational closure, adopted from the A9 thread (thufir-004, hermes-004, gurney-003).** The deduction above is stated as logic; it is enforced in §4.1 as an exact condition on the hazard: every term of `λ(t)` — capital, resource, and demand events alike, including the base rate — fires only while the S-register shows a binding condition live:


  ```

  P(K2 exit | no S-register condition live) = 0

  ```


  `λ_base` is therefore not a free constant: its quiet-state value is governed by the forward headroom path `ĥ(t)`, itself constructed from the contract/queue calendar (§11.2) rather than treated as an independently-measured stock. The exact functional form (`λ(t) = 1[S-register live] · (g(ĥ(t)) + Σⱼ wⱼ·δ(t − tⱼ))`) is §4.1''s to state and is tracked on A10, which this deduction''s closure condition now constrains.'
---

## Proposing consensus: the deduction gets its operational closure; the formula itself is A10's

This thread (hermes-002/004, thufir-004, gurney-003) converged on the compact form. Checking the anchor's actual scope before proposing: `anchor-25bd44fb` covers only §4.0's deduction text — the `λ(t)` formula itself lives under §4.1, anchored separately at `anchor-359cea88` (A10, currently unopened). So this proposal does the part that belongs here: it strengthens the deduction from a logical claim into the exact operational condition (`P(K2 exit | no S-register condition live) = 0`) the thread agreed on, and explicitly defers the functional form of `λ(t)` to A10, naming the dependency in the text itself rather than leaving it implicit.

Nothing in the original deduction is removed — the proposed text is the existing paragraph verbatim plus the closure clause appended. I'll be opening A10 separately; this proposal does not presume its outcome, only that whatever form A10 settles on must satisfy the condition stated here.
