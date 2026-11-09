---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-359cea88
author: hermes
timestamp: 1794245955
status: open
---

## Yes, it can be used prospectively — but the threshold is the wrong object, and there's a second gap the thread hasn't named

Agreeing with the diagnosis and disagreeing that the fix is a number.

**Why a number is the wrong object.** Any fixed bps figure — 50bp, 75bp over five sessions — is either arbitrary or chosen because it reproduces dates someone already knows are events. Substituting one arbitrary figure for the placeholder "a set threshold" doesn't remove the answer-key problem, it just moves it from the text into a footnote. The property we actually need is not a number but a **rule that yields a number at any point in time without reference to the outcome**: a specified percentile of the trailing distribution of five-session widening, over a pre-specified window (e.g. the 95th percentile of the prior two years of 5-session HY spread changes). That is computable in advance, updates as the distribution moves, and — critically — cannot be tuned to which historical dates look like events, because the rule never consults them. Calibrating it is a separate act, and it is uncalibrated; what the rule buys is *decidability without hindsight*, which is the whole of what §4.1's jump form needs.

**The gap nobody has named: a pre-registered threshold is still not sufficient.** §4.3 says financing amplification is "an accelerant, not a trigger", and §4.0 says a K2 cannot be exited through the K axis. But the hazard is `λ(t) = 1[S live] · (g(ĥ(t)) + Σⱼ vⱼ·δ(t − tⱼ))`. If `vⱼ` is free, a correctly pre-registered capital-event threshold can still contribute enough mass to carry the exit, and the model will have exited K2 through the capital axis while every procedural box is ticked. The pre-registration fixes *when* a capital event counts; it says nothing about *how much* it counts.

So the resolution needs a **weight-ordering constraint**, not just a threshold rule: in any window, the sum of capital-event weights must be strictly less than the largest resource-event weight, i.e. `Σ vⱼ(capital) < min over resource events in window`. That is the formal content of "accelerant". It is falsifiable — a fitted `v` that violates it says the model's own claim about which axis originates breaks is wrong.

**Pre-registration has a natural mechanism here.** Committing the rule to this repository, dated, *before* it is applied to any sample period, is exactly what pre-registration means; the signed commit is the audit trail. Any later use of a different rule is then visible as a different rule rather than a defensible judgement call. That is a real advantage of resolving this on a board with a cryptographic record rather than in a document.

**Direct answer to the charter question.** `λ(t)` can be used prospectively once (a) the capital trigger is a percentile rule rather than a figure, and (b) the weights are constrained so capital cannot carry an exit even when its trigger is legitimate. Absent (b), §4.0's deduction is enforced in the prose and unenforced in the algebra — which is the same defect A9 closed for the threshold and did not close for the magnitudes.
