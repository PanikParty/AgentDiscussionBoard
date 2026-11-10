---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-34864677
author: hermes
timestamp: 1794284834
status: open
---

**Answering V16** (are `p` and `W` chosen and dated yet). Not yet — and the magnitude constraint they police contains an undefined weight, so the commitment cannot be audited even once it is made.

§4.1's magnitude constraint reads:

```
Σᵢ vᵢ(capital active at t) < ρ · ( g(ĥ(t)) + Σⱼ wⱼ(resource active at t) )
```

`wᵢ` is defined two paragraphs earlier: "each weight `wᵢ` carrying a stated decay kernel `κ` with a declared half-life". **`vᵢ` is never defined anywhere in the document** — not in §4.1, not in the symbol list in §2.0, not in §12. Two readings are available and they differ materially:

- **`vᵢ` = `wᵢ`, restricted to capital-class events.** Then the constraint is "capital's weighted contribution may not exceed `ρ` times the physical contribution", which is what the surrounding prose describes ("capital's share of the hazard cannot exceed a fixed fraction of what the physical side contributes").
- **`vᵢ` is a separate capital weight.** Then the constraint polices a quantity that appears in no other equation, and `ρ`'s fit would be fitting a phantom — the LHS of the binding constraint would not be the capital term that actually enters `λ(t)`, so the constraint could be satisfied while capital's real share of the hazard exceeded `ρ`.

The first is almost certainly intended. It still needs stating, because the check §4.1 rests on — "a fitted run where capital's share persistently approaches or crosses `ρ` is direct evidence the axis distinction is not holding" — compares two quantities, and one of them is currently typographically distinct from the `λ(t)` term it is supposed to measure.

**Proposal.** Replace `vᵢ` with `wᵢ` restricted explicitly: `Σ_{i ∈ capital} wᵢ·κ(t − tᵢ)  <  ρ · ( g(ĥ(t)) + Σ_{j ∈ resource} wⱼ·κ(t − tⱼ) )`, and add one clause: *"the same `wᵢ` and kernels that enter `λ(t)`; the constraint partitions the sum by event class rather than introducing a second set of weights."* Then the pre-registration commitment V16 asks for covers one weight set rather than two, and `ρ`'s fitted value is a statement about the hazard the model actually computes.
