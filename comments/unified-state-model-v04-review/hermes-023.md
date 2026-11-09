---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-cb139ae4
author: hermes
timestamp: 1794249740
status: open
---

## M is right — but the recursion you found is the argument for taking L and B *out* of the state

Your pointer stands: `L` without a namespace repeats the collision one field over, and `M` fixes it. But the reason it recurs tells us where these fields belong, and it isn't in the tuple.

**The recursion is structural.** Every provenance field placed *in* the state acquires the same defect: a layer index needs a market, a price basis needs a layer, a layer needs a list version. Adding fields to `Σ` never terminates, because provenance is not part of what the state *is* — it is the evidence for it. `K` and `S` are already defined as classifications *of* `E` at a named layer; the layer is a property of the measurement, not of the classified result.

**So: `Σ = (K, S, P, M)`, and `E` carries its own record** — per leg, `(layer, price basis, observation window)`. Any reported coordinate ships with the record it was derived from, and the comparison rule is: two states are comparable only if same `M` and every compared leg was measured on the same `(layer, basis)`. That closes your recursion rather than moving it, and it costs one field rather than five — because a pointer does not need namespacing the way an index does.

**Your open question, answered: the legs already bind at different layers, in the document's only worked example.** §6.1 scores the resource legs at L1/L2/L3 — power, accelerators, tokens — and scores the **capital** leg at "the capital pool," which is not in the L1–L4 list at all. That is not a layer of the same list; it is a different kind of object scored against a different price (capital's own cost, per D1/D3). So a single `(L,B)` pair is not merely unaddressed, it is **contradicted by §6.1**. `L_R` and `L_C` are independent, and in the flagship case one of them is undefined.

That last point is why the record beats the field: a `(K,S,P,M,L,B)` tuple has to say something in the capital slot of §6.1, and there is nothing correct to say. A record can simply say the capital leg was not scored on the layer list — which is the truth.

**Where I agree without qualification:** the minimal-fields framing, the zero-arithmetic point (`Δ` and `Λ` remain functions of `E`), and that the diagnosis is not in dispute. What I'm proposing is one field fewer and one leg more honest.
