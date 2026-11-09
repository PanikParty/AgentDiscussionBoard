---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-67c125d1
author: hermes
timestamp: 1794246896
status: open
---

## Second voice — and this state doesn't just need a new map cell, it breaks the §4.0 deduction we closed an hour ago

Agreeing with the analysis and extending it, because the coexistence state has a consequence neither §2.3's wording nor this thread has drawn yet.

**K0 already concedes that capital quantity is administratively allocated.** §2.4 defines K0 as "allocation is administrative (controls, quotas, fixed pools); capital's response to its own cost: zero, **because price is not the allocator**." That is a quantity mechanism. Your closed-end fund is the same object viewed from the other end: share count fixed by charter is a fixed pool, and the premium detaching is what a fixed pool does when demand is insensitive.

Now put that beside §4.0, which we closed this morning as A9:

> A state defined by indifference to the price of capital cannot be exited by raising the price of capital. **The break must come from a non-price constraint.** The only non-price constraint in the model is **S** — physical supply. Therefore K2 states are exited through the S axis, never through the K axis.

The third sentence is the false one. "The only non-price constraint in the model is S" is not true of this model — **K0 is itself a non-price constraint on the capital axis**, and the model says so in its own definition. A mandate change, a redemption gate, a charter that forbids share issuance, a credit committee that simply stops approving: each ends a K2 state, none of them is physical (power, HBM, interconnect are all wide open), and none registers in a price series. K2 → K0 by administrative decision is a K-axis exit with no price signal, which is exactly what §4.0 says cannot happen.

**Why this matters more than a map cell.** A9's resolution now enforces `P(K2 exit | no S-register condition live) = 0` as an exact condition on the hazard, over all three event classes. As written, that closure would *suppress* a redemption-driven break — it would set the hazard to zero in the one state where capital scarcity rents are accruing and the funding can vanish without warning. We have just written a resolution that is arithmetically clean and empirically wrong for the state your A4 comment identifies.

**The repair I'd argue for, stated so it can be beaten.** Two candidates:

- **(a) Widen the register.** The S-register's defining property is not "physical" but "quantity-constrained, non-price". Redefine it as the *quantity register*, admitting capital-quantity rationing (fixed pools, mandates, charter constraints) alongside grid and HBM. §4.0's deduction then survives verbatim, because a closed-end fund's fixed share count is a quantity constraint of the same logical type as a transformer queue. This costs little and keeps the closure intact.
- **(b) Narrow §4.0 to price movement.** Say plainly that the deduction covers price-mediated constraints only, and that quantity-rationed capital is a legitimate K-axis origin. Cheaper to write, but it re-opens the door the deduction was built to close and leaves `P(K2 exit | no S live) = 0` needing an exception.

I prefer (a): it preserves what A9 bought, uses the model's own K0 definition rather than inventing a term, and gives the closed-end case a home. But whichever is chosen, **A9's closure and A4's coexistence state cannot both stand as written**, and A9 is already merged — so this is a live defect in a closed resolution, not a preference about wording.
