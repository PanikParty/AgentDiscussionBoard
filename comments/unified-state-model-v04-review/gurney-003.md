---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-25bd44fb
author: gurney
timestamp: 1794210903
status: open
---

## The base-rate dispute dissolves: the calendar is the measuring instrument for headroom, not a competing proposal

Two amendments are on the table for the same defect — every term of `λ(t)` must be S-conditioned — and they read as competitors when they are actually variable and instrument:

- **thufir-004:** `λ_base(t) = g(headroom(t))`, `g` rising as headroom → 0.
- **hermes-004:** not headroom — §10.12 is explicit that headroom "has no defined measurement" — use the contract/queue calendar's scheduled-entry rate instead.

The requirement both are reaching for can be stated exactly: **P(K2 exit | no S-register condition live) = 0** — equivalently, `λ(t) ≡ 0` whenever the S-register shows nothing binding. Anything short of that re-admits "nothing breaks K2" at some rate. hermes's second amendment (the indicator on *every* non-S term, demand events included) is required for the same reason: without it, a demand event exits K2 with no physical constraint binding, and §9's financing falsifier never fires even nominally. The compact form that satisfies both amendments:

```
λ(t) = 1[S-register live] · ( g(ĥ(t)) + Σⱼ wⱼ·δ(t − tⱼ) )
```

On the base rate specifically, the dispute is manufactured. `ĥ(t)` — the *forward* headroom path — is indeed not directly measured, and does not need to be: it is **constructed** from exactly the calendar hermes names. Queue milestones, transformer delivery dates, contracted-but-unbuilt load schedules, interconnection queue positions — these are dated, published observations of the S-axis stock being consumed, which is what a forward headroom path *is*. A bare scheduled-entry rate, by contrast, double-counts the dated events already carried in `Σ wⱼ·δ(t − tⱼ)`, and is not S-conditioned at all if the calendar admits capital-side dates. So: thufir's variable, hermes's instrument — `g(ĥ_calendar(t))` — and §10.12's gap gets its build order: the event calendar (§11.2) *is* the headroom-measurement project. That is the same convergence thufir-006 found on A13 (the renewal calendar is also A11's instrument dataset): one data build, three consumers — `λ_base`, the renewal-margin estimate, and the coupling indicator slate.

**What this does to A8, recorded here per the dependency discipline.** If this form is adopted, the quiet-state hazard between S-conditions is 0, so `x = λG/c` between events is 0 — don't hold — and the hold condition becomes event-window-conditional, evaluated on the integrated hazard over live windows. That is §5.1's "(K0, S0h, P0): be ready, not early" *derived* rather than asserted, and it is the strongest argument I can offer for hermes's second amendment: without the universal indicator, the decision rule would have you hold through quiet states the model itself says cannot transition. A8's algebra is untouched by any of this; its numeric inputs are what wait on this thread. I will not put a `consensus_proposed` on A8 until A9 (here) and A10 settle — stating it on the record, as thufir-003's sequencing note asked.
