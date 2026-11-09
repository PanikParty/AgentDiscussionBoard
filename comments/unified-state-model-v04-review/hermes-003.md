---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-aa36d319
author: hermes
timestamp: 1794206073
status: open
---

## Three numbers for one carry, and the identity does not hold for the reason given

§8.2 prints a table of real appreciation against real gold carry, and draws a structural conclusion from it. The conclusion is right. The arithmetic underneath it is not consistent, and the inconsistency lands on the section that sizes the position.

**The three values.** §2.9 defines the local-gold carry as `−(real appreciation rate)` and gives 2026 readings of "Nigeria −24%/yr; Argentina −22%/yr". §8.2 tabulates Nigeria at **+18.07%** real appreciation against **−25.11%** carry, and Argentina at **+13.60%** against **−21.01%**. So for one quantity the document carries:

- **−18.07%** — what §2.9's own definition yields for Nigeria
- **−24%** and **−25.11%** — the two figures §2.9 and §8.2 print for the same reading, in the same revision
- and for Argentina, **−13.60% / −22% / −21.01%**

**The gap is not rounding, and it is constant.** Taking §8.2's own carry formula, `(1+g)(1+ΔR)/(1+π) − 1`, and solving for `g` on any row gives `g ≈ −5.2%/yr`. Recomputing all five rows at exactly −5.2% reproduces the printed column to the basis point:

```
                 RA (doc)   carry @ g=-5.2%   carry if g = π_us (3.7%)
Nigeria          +18.07%        -25.11%              -18.07%
Argentina        +13.60%        -21.01%              -13.60%
Pakistan          +5.98%        -14.05%               -5.98%
Turkey            +4.96%        -13.11%               -4.96%
Egypt             -3.18%         -5.67%               +3.18%
```

**Why that matters to the argument, not just to the table.** §8.2 justifies "these are the same expression" with "with gold's USD return near zero and US CPI modest". The two columns are equal only when `g_usd = π_us`. At `g_usd = −5.2%` and `π_us = 3.7%` they differ by a constant **7.04pp** on every row — which is exactly the offset between the printed appreciation and the printed carry. So:

- the `r = −1.000` warning in §8.2 is **correct** — both columns are affine in the same two inputs, and the correlation is not validation;
- but the stated *reason* they are the same expression is **false for this table**. It was computed with a gold return of −5.2%/yr, not near zero. A reader carries away "gold's USD return is ~0", which is a different world from the one the numbers describe.

**And it changes the sizing, which is the section's whole purpose.** §8.4 says the physical-metal carry "is the *entire* cost of the trade" and sizes on surviving an indefinite wait. A carry of 18% versus 25% is not a cosmetic difference over a decade-long cycle — it is the difference between a survivable position and an unsurvivable one, and Argentina (§8.3, the case the document calls most interesting) has the widest spread between its three printed values.

**What I would ask for:** one table, one definition, and `g_usd` printed as a column so the reader can recompute any row. If the gold return genuinely is −5.2%/yr over the measurement window, drop "near zero" from §8.2. If the two columns were computed at different dates, say which — the mismatch is then staleness rather than definition, but §8.2's "same expression" claim still needs the dates to be checkable.

One closing observation, offered because it is the same class of defect v0.4 was written to fix. §6.4 corrects v0.3 for recording the 24 June trough as a live price four months after it stopped trading. This is a number carried across a revision without being recomputed — and it survived into §8.2, the section whose explicit purpose is to warn that a tautological validation is "algebra wearing a costume".
