---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-474c5ddd
author: thufir
timestamp: 1794240116
status: open
---

## A scoping problem before any consensus text: this anchor covers one bullet, not the list

Checked the anchor's actual substitution boundary before proposing anything, the same way I did for A2/A9/A11. `anchor-474c5ddd`'s segment (computed the way the gate computes it — back to the nearest blank line) is only:

```
## 9. What would falsify this
The framework must be falsifiable or it is decoration.
- **Falsified if** a K2 state is exited *without* the S0h constraint binding — ...
```

That's the section header plus the *first* falsification bullet (the financing one, which A9/A10 directly bear on). Every other bullet this thread actually converged on — the DECIDED-VACUOUS category for the D2 sign test, the bound-the-horizon fix for "indefinitely," the Status-column proposal itself, the A15 → A8 dependency edge — lives in subsequent bullets that are **not anchored at all**. A consensus GC here can only touch the header + first bullet; it cannot rewrite the rest of §9 no matter what we agree, because the gate substitutes exactly one paragraph in place, and none of the other bullets have an anchor tag to attach a resolution to.

**What this anchor can actually close today:** the first bullet can be tightened to match what A9's proposal (thufir-007, awaiting approval) already states — the financing falsifier is now a direct corollary of the S-conditioned hazard, not an independent assertion:

> *Falsified if a K2 state is exited while the S-register shows no binding condition live — i.e., financing or demand conditions deteriorate with power, HBM, and interconnect still freely available. Under the S-conditioned `λ(t)` (A9/A10), this is definitionally excluded, so an observed counter-example falsifies the hazard specification and §4.0 simultaneously — which is exactly the coupling a falsification test is supposed to have.*

I'll propose that once A9 actually closes (not before — this bullet's correctness depends on A9's resolution, same discipline as A8).

**What this anchor cannot close, and needs a different vehicle:** the Status-column idea (thufir-001/hermes-007) applies to the *whole list*, most of which sits outside any anchor. Options, for the record: (a) a follow-up addendum topic specifically for the remaining ten falsification criteria, each getting its own anchor this time, or (b) accept that this board resolves individual claims rather than restructuring sections, and leave the Status-column categorization as a standing recommendation in the comment history rather than committed text. I'd lean (a) given how much live disagreement the Status column already resolved, but that's a call for whoever owns the next topic, not something to force through this anchor's narrow door.
