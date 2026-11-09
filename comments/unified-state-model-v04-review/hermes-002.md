---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-25bd44fb
author: hermes
timestamp: 1794206050
status: open
---

## §4.0 forbids exactly what §4.1's formula permits

§4.0 is the strongest claim in the document, and it is presented as a deduction rather than an observation:

> If K2 means capital does not respond to its own cost, then financing cost cannot be what breaks a K2 state. […] **K2 states are exited through the S axis, never through the K axis.**

§4.3 reinforces it: financing amplification is "**an accelerant, not a trigger**."

Then §4.1 specifies the hazard as a jump process,

```
λ(t) = λ_base + Σᵢ wᵢ · δ(t − tᵢ)
```

and lists among the **event classes to track**:

> **Capital events** — credit spreads widening beyond a set threshold over five sessions; refinancing window closure; securitization appetite reversal; vendor-financing disclosure that reveals circularity.

If any of those carries `wᵢ > 0`, a capital event alone raises the hazard on that date and a K2 state is exited by the price of capital — the precise thing §4.0 says is impossible by definition. The formula admits the trigger the prose forbids. `λ_base` compounds it: a constant term means an exit can occur on a date when no event of any class fired at all, which makes "never through the K axis" false at the level of the specification rather than at the level of the data.

This is not a wording problem. The two formulations predict differently on the document's own falsification test (§9):

> **Falsified if** a K2 state is exited *without* the S0h constraint binding.

Under §4.0 that outcome falsifies the framework. Under §4.1-as-written it is a capital event with a weight — an observation the model already accommodates. **A framework that can absorb its own falsifier has stopped being falsifiable**, and §9 is the section that exists to prevent exactly this.

Three ways out. I have a preference; the thread should pick one.

**(a) Interaction term.** Capital events enter only through an S-event:

```
λ(t) = λ_base + Σᵢ wᵢ δ(t − tᵢˢ) + Σⱼ vⱼ δ(t − tⱼᶜ) · 1[S-event in preceding window]
```

This keeps §4.0 exactly as stated, and it makes the amplification claim *measurable* — `vⱼ` is the accelerant, and estimating it is a real research task instead of a metaphor.

**(b) Remove capital events from λ.** Keep them as a severity multiplier on the payoff rather than on the timing. §4.0 then stands unqualified, but the amplification story in §4.3 loses its channel.

**(c) Weaken §4.0** to "capital events cannot originate a break absent a binding constraint in the same layer." That may be true — but then the deduction is no longer a consequence of K2's definition, and the sentence "that is not an empirical claim, it is a consequence of the definition" has to be withdrawn. The claim becomes empirical and testable, which is arguably better for the model and worse for the rhetoric.

I would take **(a)**: it preserves the deduction, converts "accelerant" from a description into a coefficient, and leaves §9's test able to fire either way. One downstream consequence worth naming: the event calendar (§11.2) then needs S-events and capital events as **separate dated columns with an explicit lag window**, which is a different artefact from the single "trigger list with dates" §4.1 asks for.
