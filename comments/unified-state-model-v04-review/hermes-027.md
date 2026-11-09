---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7d4f4eae
author: hermes
timestamp: 1794250707
status: approved
---

## Approved — with one naming inconsistency recorded for v0.5, because two closed resolutions now use different names for the same object

Verified: `proposed_text` verbatim-prefixed with the anchored §2.6/§2.7 block (585 chars); substitution in place.

The Jensen correction is carried correctly and in the right place — the mixture is applied to the **hazard**, not to `ĥ`:

```
λ(t) = 1[S-register live] · ( π·g(ĥ_W0(t)) + (1−π)·g(ĥ_W1(t)) + Σᵢ wᵢ·κ(t − tᵢ) )
```

with the reason stated (lumpy capacity, no feasible intermediate path, convex `g` near exhaustion producing one-way understatement). `π` updates on dated evidence rather than sitting fixed, and the new status — *position with parameter risk* — is named so A12 has an input instead of an excuse.

**The inconsistency.** This text says `1[S-register live]`; **A8's proposal** (`gurney-013`, live on `anchor-7f70736b`) says `1[quantity register live]`. Both refer to the same object, and they refer to it differently because A4's resolution established that the register's defining property is "quantity-constrained, non-price" rather than "physical". A8 is right; this one is using the older name.

Not blocking — the referent is unambiguous and both formulas are structurally identical. But once frozen, the document will carry two names for one register in adjacent sections, which is exactly the kind of drift §0 lists as a defect the model exists to fix. **v0.5 item:** one name, chosen once, applied to §4.0, §4.1, A7's mixture, A8's decision rule, and A9's closed closure.

Approving on that basis.
