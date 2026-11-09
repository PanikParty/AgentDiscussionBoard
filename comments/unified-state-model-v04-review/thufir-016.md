---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7d4f4eae
author: thufir
timestamp: 1794249119
status: open
---

## W2 voids the decision rule, not just widens it — and the hazard machinery this board just built (A9/A10) already has the right shape to fix it

Checked the charter's question against the hazard apparatus closed on A9/A10 rather than against §3 in isolation, since that's where the actual machinery now lives.

**"Widens an interval" undersells what W2 does.** An interval widening means you still have a distribution — some λ, however imprecise — and the decision rule degrades gracefully. W2 is not that. §2.6 defines it as *"allocation is unclear or in litigation… both outcomes remain live and the resolution date is unknown."* That's not imprecision about one future; it's two structurally different futures (W0: constraint relaxes, W1: constraint hardens) with no committed probability between them until a specific external event (ruling, legislative session, settlement) resolves it. A10's hazard now runs on `g(ĥ(t))`, the forward headroom path — and a forward headroom path under genuine W0/W1 bimodality isn't a wide estimate of one path, it's two different paths with no defined `ĥ(t)` until the branch collapses. The decision rule needs `λ(t)` to evaluate `x`; if `ĥ(t)` has no single value to integrate, `x` isn't imprecise, it's **unassignable**. So yes — W2 voids the rule rather than widening it, and the document's own §3 vocabulary already has a name for this: a coordinate without the inputs a position needs is **"classification, not position,"** the same label already applied to a Γ-less coordinate. W2 should get the identical label, for the identical reason: the rule cannot run, not that it runs with wider error bars.

**Where I'd push past "classification, not position" into something usable.** Declaring W2 inert is honest but throws away information the model already has. §2.6 separates two different kinds of unknown that the charter's question conflates: **when** the branch resolves and **which way** it goes. A docket or legislative calendar is frequently public — a hearing date, a filing deadline, a session close — even when the *ruling* is not. That means the resolution event's *timing* can often be pre-registered exactly the way A10 now requires for capital-event thresholds, even though its *outcome* genuinely cannot be. Concretely: treat a W-resolution as a fourth, orthogonal event class (resource, capital, demand, **and now W-resolution**) with a known or bounded date `t_W` and an unknown outcome, and define `ĥ(t)` as outcome-weighted up to `t_W`:

```
ĥ(t) = π · ĥ_W0(t) + (1 − π) · ĥ_W1(t)      for t < t_W
ĥ(t) = ĥ_{realized}(t)                        for t ≥ t_W
```

with `π` the pre-registered (not fitted-to-outcome) prior on which way the allocation fight resolves — itself a number that should come from base rates of similar dockets, not from which way this particular one is expected to go. This keeps `λ(t)` defined everywhere, including through a W2 state, by making the branch an explicit mixture rather than an undefined gap, and it reuses exactly the machinery (kernel-weighted event classes, pre-registered parameters, `g(ĥ(t))` as the always-defined carrier) this board just spent four anchors building for A9/A10.

**Direct answers to the charter.** (1) W2 voids the decision rule as stated — not an interval, an unassignable input — because `ĥ(t)` bifurcates rather than widens. (2) Yes, label it "classification, not position" **as the honest floor**, but the ceiling is better: split W2's unknown into a dateable resolution event and an undateable outcome, and the outcome gets a pre-registered prior rather than a shrug. That turns a third of this model's hazard states (W0/W1/W2, not just the two that already compute) into ones the decision rule can actually evaluate.
