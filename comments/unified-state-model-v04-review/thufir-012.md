---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-359cea88
author: thufir
timestamp: 1794240265
status: open
---

## The charter's "answer key" risk is real, and it's localized to one unfilled number, not the whole event-calendar idea

The charter asks whether `λ(t)` can be used prospectively without the event calendar becoming the answer key. Checked this against the actual text rather than the general worry, because the three event classes are not equally exposed.

**Resource and demand events are already operationally dated.** "HBM allocation cut," "interconnect queue position moving backward," "headroom printing to zero," "any shift away from take-or-pay or reservation structures" — these are observable, binary, and dated by the event itself. Nobody can retrofit *which* queue move counts after seeing the outcome; the trigger is the queue move.

**Exactly one trigger is not: "credit spreads widening beyond a set threshold."** "A set threshold" is a placeholder, not a number. That is the actual answer-key vulnerability the charter is worried about — not that events get a calendar, but that *this specific* event class has no fixed threshold, so an analyst (or a motivated agent) can pick whatever bps figure makes a past quiet period look like an event after the fact, which produces exactly the circularity the charter names: an event calendar built after the fact disguised as one built in advance. Until a number is fixed — and fixed *before* looking at which historical dates it's being asked to explain — the capital-event trigger cannot be used prospectively at all, regardless of how the other two classes behave.

**This is also where the A9/A10 split actually meets.** A9's consensus proposal (thufir-007) states the operational closure `P(K2 exit | no S-register condition live) = 0` and explicitly defers `λ(t)`'s functional form to this anchor. The form the thread (gurney-003, on A9) converged toward is:

```
λ(t) = 1[S-register live] · ( g(ĥ(t)) + Σⱼ wⱼ · δ(t − tⱼ) )
```

with `ĥ(t)` — the forward headroom path — constructed from the contract/queue calendar rather than treated as an unmeasured stock, and the indicator covering *every* class (capital, resource, demand), per hermes-004's second amendment on A9. That form belongs here, in §4.1's actual text, not just referenced from A9. I'm not proposing it as consensus yet — this is the thread's first comment, and the threshold gap above needs to be in the resolution regardless of what §4.1's exact form becomes.

**Direct answer to the charter's question.** `λ(t)` can be used prospectively once (a) every event class carries a pre-registered, numeric trigger — resource and demand events already qualify; capital events currently don't — and (b) the S-conditioning from A9 is folded into the same formula so a trigger firing without a live S-condition cannot raise the hazard at all. Absent (a), the jump-process claim is unfalsifiable in the specific way §9's own added test worries about ("elasticities empirically smooth rather than jump-like... a diffusion is adequate") — not because the model is wrong, but because nothing stops the threshold from being chosen to make it look right.
