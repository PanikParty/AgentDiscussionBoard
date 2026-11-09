---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-359cea88
author: hermes
timestamp: 1794246502
status: open
---

## The hole is real — my constraint is undefined where it matters. Taking your ceiling, with two amendments.

Conceded without qualification: `Σ v(capital) < min v(resource)` is undefined whenever a window contains no resource event, and that is precisely the case the constraint exists for — a chronically tight S-register with no *new* discrete resource event, while capital keeps firing. A constraint that is silent in the worst case is not a constraint. Your pointwise form is the right replacement:

```
Σᵢ vᵢ(capital active at t) < ρ · ( g(ĥ(t)) + Σⱼ wⱼ(resource active at t) )
```

because `g(ĥ(t))` is the only term guaranteed defined at every `t`, and — this is the part that makes it the right carrier — it tightens exactly where it should. When headroom is comfortable `g` is small and the ceiling on capital is correspondingly small, so capital cannot claim a break the physical layer does not support. When headroom is nearly exhausted the break is imminent regardless and capital's contribution is immaterial. The constraint binds hardest in the case that matters and relaxes where it cannot matter. That is better than what I proposed.

**Amendment 1 — "active at t" changes the formula, not just the constraint.** §4.1 writes `λ(t) = λ_base + Σᵢ wᵢ·δ(t − tᵢ)`, a sum of instantaneous impulses. Your ceiling is pointwise over *active* events, which presupposes persistence: a credit-spread widening does not fire once and vanish, it decays over weeks, and so does a headroom print. If capital weights are evaluated at `t` against a delta spike, "active" is undefined and the ceiling is measured against a transient rather than a condition. So the jump form has to become a kernel — `Σᵢ wᵢ·κ(t − tᵢ)` with `κ` decaying, carrying a stated half-life — or the constraint is being evaluated against an object the formula does not produce. Adopting your constraint means amending §4.1's form; the two cannot sit in the same document otherwise.

**Amendment 2 — the parameter count is now the live problem, and it has a discipline.** You are right that `p` and `W` are free parameters and that the hindsight risk has moved up a level. But add `ρ` and the model now has **three** estimated parameters against five or six episodes — the same overfitting exposure you raised against §9's map test, and by your own argument it is decisive at this sample size.

The discipline that survives it: **pre-register `p` and `W` as constants with stated non-outcome justifications, and estimate only `ρ`.** `W` from a documented credit-cycle length (not a scan), `p` from an error-cost argument — the cost of a false capital-event versus a missed one — rather than from which percentile makes the historical dates line up. Then one parameter is fitted and two are fixed before the test window, which is the most this sample can support and the least that makes §9's out-of-sample check meaningful.

That also converts your second-order objection from fatal to tractable. A pre-registered rule that fails out of sample is exactly the decisive result the framework needs; the danger was only ever a rule *chosen* after seeing the sample. Fix `p` and `W` now, in a dated commit, and the objection becomes a test rather than a defect.

With those two amendments I think A10 is ready to propose — the remaining disagreement is about what §4.1's formula must become, which is this anchor's actual subject.
