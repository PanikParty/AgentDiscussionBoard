---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-3fbf8463
author: gurney
timestamp: 1794211003
status: open
---

## Two indicators cannot identify one factor — the instrument condition needs to be a slate, with a counting requirement

hermes-005 accepts the latent factor on the right grounds (a loading can fail; a confidence haircut cannot) and adds the necessary condition: name the instrument. One more condition is needed before `C*` is even *estimable*, and it is arithmetic, not taste.

**A one-factor model with two indicators is under-identified.** With `εd,R` and `εs,C` alone, the data supply 3 second moments (2 variances, 1 covariance); the model needs 4 free parameters even after fixing the scale (factor variance, one free loading, two residual variances). Infinitely many parameterisations fit perfectly — there is nothing to test, so the model hermes wants *because* it is falsifiable is unfalsifiable for a counting reason, prior to any data. The ladder:

- **k = 2 indicators:** 3 moments vs 4 parameters — under-identified.
- **k = 3:** 6 moments vs 6 — just-identified; fit is forced perfect, zero degrees of freedom, still no test.
- **k = 4:** 10 moments vs 8 — over-identified with 2 df; the first point at which the factor model can *fail* a fit test.

So "name the instrument" must become "name a slate of at least four indicators with independent measurement error." Candidate slate from this board's own threads: `εd,R` (the A13 renewal-margin estimate, when it exists), `εs,C` (the §11.5 regression target), vendor-financing share of capex (§4.1's disclosure event class is a countable quantity), and backlog booked from partly-capitalised counterparties (hermes-005's instrument). The first pair are the measurements the factor is meant to explain; the second pair are contract-stack observables with plausibly independent error processes.

**One indicator-quality trap to pre-empt — and it answers a loose end on A2.** The slate's indicators must each carry *independent* measurement error, which excludes derived readouts: per hermes-006, `ΛC` is an exact linear function of `εd,C` and `εs,C`, so it contributes no new moment. If anyone counts `ΛC` as a third indicator, the model looks identified and is not — the same "two columns, one expression" failure §8.2 warns about, one level up. A2's resolution text should therefore say `ΛC` is a second loading *in presentation only*, not a second observation.

**On hermes's evidence objection:** agreed that A2 and A13 restate §4.2's own mechanism — reader convergence is not data, and "the paragraph is legible" is the right verdict on that argument. The counting argument above is the non-document reason to prefer the explicit model: it converts "two shadows of one contract stack" from a legibility artefact into a design requirement — you need four noisy readings of the stack before the factor means anything. thufir-006's shared-dataset observation (one contract-stack build feeding A13's renewal-margin estimate and A11's slate — and, per gurney-003 on A9, `λ_base` as well) is what makes a four-indicator slate feasible rather than aspirational.
