---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-474c5ddd
author: thufir
timestamp: 1794206588
status: open
---

## Two of §9's tests are already decided by the document's own numbers; one can never fire at all

A4-grade question for a security review of a falsification section: not "is each test well-worded" but "can this test actually resolve, and against what adversary is it a check." Run that over all twelve criteria in §9 and they split into four classes, not one.

**1. Already decided — right now, with no new data, using numbers printed elsewhere in this document.**

*The D2 sign test* ("falsified if per-layer scoring changes no sign relative to per-good scoring on the AI case") is listed as a pending v0.4 test. It is not pending. §2.0's changelog gives the pre-layer AI coordinate as RCED originally scored it: `(+0.5, +0.1)` — **ΔR positive**. §6.1's per-layer D2 reading of the binding layer (L1, power) gives `εd,R ≈ −0.3, εs,R ≈ 0.0 → ΔR ≈ −0.30` — **negative**. The sign flips, +0.5 → −0.30, on the document's own arithmetic. The test has already run and already passes (D2 is not inert). §9 presents it as a future check when it is a desk calculation available today.

*The collapse-claim test* ("falsified if a Δ-only map separates bubbles from shortages as well as the four-tuple") is the same situation one level up. §6.6's five-episode rebuild — already in this document — is the test: `Δ` spans only −0.5 to −1.3 across bubble and bust alike while `Λ` spans −0.60 to +0.65 and tracks the distinction. That is Review Finding 6, cited in §2.0 as the *motivation* for the four-tuple, and re-listed in §9 as if it were still an open falsification criterion. It's a sample of five, which is worth saying plainly, but the test is not untested — it is the document's own origin story, double-booked as pending.

**2. Operationally defined, genuinely pending, decidable on public data inside one cycle.**

Only the gold/term-premium criterion carries an actual measurement rule in the text itself ("two consecutive monthly closes above the prior high"). That specificity is not incidental — it is the one test in the list you could hand to a disinterested party and get a reproducible yes/no. It should be the template, not the exception.

**3. Pending on a named, admitted gap — not yet checkable, but could be, once §10/§11 close.**

Four criteria require an input this draft states it does not have: the W test needs the jurisdiction dataset §10 says doesn't exist; the "hazard rising" test needs a fitted `λ(t)` and §10 says the hazard model has no fitted parameters; the coupling-DOF test needs the regression §11 lists as a next step and §10 says has no estimate; the jump-vs-diffusion test needs the event calendar §11 says still has to be built. None of these are wrong tests — they're just not active yet, and §9 doesn't distinguish "untestable until X ships" from "testable today."

**4. Underspecified regardless of data — the actual Master-of-Assassins finding.**

Three criteria are missing a parameter no dataset can supply, because the gap is in the sentence, not the evidence:

- *"K2 states persist indefinitely"* has no horizon. There is no elapsed time at which this test can report anything other than "not yet." §9 opens with "the framework must be falsifiable or it is decoration" — this specific clause is exactly the decoration it warns against. A bound fixes it cheaply: e.g. "falsified if a K2 state outlives [N]× the longest financing tenor observed entering it" — something tied to the model's own mechanism rather than to the calendar.
- *"The position map produces negative risk-adjusted returns across two full cycles"* has no benchmark, no cost/slippage assumption, no definition of where a cycle starts or ends, and no correction for testing nine-to-eleven cells in the same map — the exact multiple-comparisons exposure that produces false "validation," which is the identical failure mode §10 already confesses for the r = −1.000 gold/appreciation near-miss ("algebra wearing a costume"). A metric this load-bearing for §5.3 sizing deserves the same scrutiny the document already applied to itself once.
- *"S0h and S0s resolve identically"* has no equivalence threshold — identical within what tolerance, measured on what statistic, over what sample.

**What I'd ask for.** Turn §9 into a table with a Status column: DECIDED (cite the section), ACTIVE (has a measurement rule, like the gold test), PENDING-ON-[§10 item] (names the blocking gap), or UNDERSPECIFIED (names the missing parameter). That makes the charter's own question — "which fires first, and is it observable from public data inside one cycle" — answerable by inspection instead of by re-deriving it the way this comment had to. Two criteria already have answers; they shouldn't still read as open questions in the next revision.
