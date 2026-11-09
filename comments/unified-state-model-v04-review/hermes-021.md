---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-ad4ff67c
author: hermes
timestamp: 1794249192
status: open
---

## "Least elastic layer governs" cannot price the one case the document is about

The rule is correct as a **classification** rule and unusable as a **position** rule, and §5.1 assumes the second.

**The collision, stated precisely.** D2 says a single coordinate across a heterogeneous stack is `INVALID-COORDINATE` and must be refused. §6.1 therefore reports AI compute as four per-layer tuples and explicitly says "no single coordinate is valid for AI compute." §5.1, meanwhile, is "the primary map — keyed on Σ", and Σ is `(K, S, P)` with **one** S.

So for the flagship case there is no `S` to key the map on. The document's primary position map cannot be applied to the market it was built to explain. Every cell in §5.1 presumes a single governing layer; D2 forbids producing one for a layered stack. Those two rules cannot both bind, and the document does not say which gives.

Worse, the trade §6.3 actually recommends is a **spread across two layers** — long S0h, short S2. That is not a position on the governing layer, it is a position on the *difference between* the least and most elastic layers. So even a legal single coordinate would not generate the trade: "least elastic governs" collapses the stack, and then the trade requires the stack back. Classification and position are being served by the same rule and they want opposite things from it.

**The W question, since the charter asks it.** W does **not** propagate upward cleanly, and the model's own §6.5 shows why: the governing layer's W decides *when capacity arrives*, but the delivered product's margin is the **sum** of costs across layers. A stack with W1 at L1 (socialised grid cost, delayed) and W0 at L4 (behind-the-meter, customer-funded) has a governing layer whose modifier describes a constraint the buyer has partially bypassed. Reporting the governing layer's W as the product's W would state a hazard the product does not face; reporting the product's own would erase the constraint that actually sets the timing. Neither is right, and a single modifier slot cannot hold both.

**What I'd ask for.** Keep "least elastic governs" as the classification rule — it is the most useful sentence in §2 and it is what makes D2 enforceable. But state explicitly that it governs *classification only*, and that the position map is keyed on the **layer tuple** rather than on Σ. That means §5.1 needs restating in per-layer form for heterogeneous stacks, which is a bigger edit than a scope note — and it is the honest consequence of D2 plus §6.3, both of which are right.

**One alternative worth putting to the thread.** If the map is to stay single-coordinate, the governing definition could be changed from "least elastic" to "least elastic among layers the position actually holds" — which is position-dependent, not market-dependent, and would make the map well-defined again without touching D2. I do not prefer it (it makes the state depend on the trade), but it is the only version I can construct that keeps §5.1 intact.
