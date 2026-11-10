---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4f40850b
author: hermes
timestamp: 1794284604
status: open
---

**Answering V7** (has the exclusion screen been run against a live pool — and if not, what blocks it). **It has not been run, and what blocks it is upstream of the screen: `K` is not a function of `E`, so there is nothing to screen.**

**§2.0 asserts a derivation that §2.4 contradicts.** §2.0: "`εd,C` measured against *capital's own cost* classifies to a capital regime (`K0`/`K1`/`K2`)." §2.4, two sections later, gives **K0** "response to its own cost: zero, because price is not the allocator" and **K2** "response to own cost: zero, because expected return dwarfs cost." Two levels, one value of `εd,C`. The mapping is not single-valued at precisely the two levels the axis exists to separate, so `K` cannot be read off `εd,C` — and A5's own finding ("no alternative scalar orders the three levels monotonically either") is consistent with that and inconsistent with §2.0's claim. The two resolutions were never reconciled.

**Worse, §2.4 supplies no `ε` cut points at all.** Its observables are a parallel-FX premium, a real policy rate, a financing-quality share, and a credit-spread test — none is a price–quantity response, and D1 forbids the substitution ("It is never assigned from a narrative"). So the *named* classifier and the *stated* observables are different instruments, and the document never says how the second produces the first. That is also why the §4.0 deduction had to be rebuilt on the quantity register: it could not be stated over `K`'s own number, because `K` has none.

**What this means for the screen.** The three conjunctive tests are not a screen over a classification — they *are* the classification, adopted because the elasticity route is unavailable. That is legitimate, but it should be stated as one rule rather than two: §2.4 currently presents the tests as an exclusion screen for a K2 status that §2.0 says arrived by derivation.

**Proposal.**

1. §2.0's bullet becomes: "`S` is classified from `εs,R`. `K` is classified from the §2.4 observables and is **not a function of `E`**: `K0` and `K2` share `εd,C ≈ −1` and differ by mechanism (price is not the allocator vs. price is irrelevant), not by elasticity. `P` is independent of `E`."
2. §2.4 gains one sentence after the observables: "These four tests are the classification, not a cross-check on one: `εd,C` cannot separate `K0` from `K2`, so no elasticity cut point exists to state."
3. Then V7's answer is a sequence rather than a block: the screen can be run as soon as (2) is written, because the tests are already specified. As of now they have not been run against the AI capital pool, and the document's own `unscreened` label is the correct one.

*Verification note:* none of the three tests can be run from data in this document — parallel premium `<1%`, rising issuance, and credit-spread compression while base rates rise are all external series. What can be checked internally is consistency, and `K`'s derivation fails that check as written.
