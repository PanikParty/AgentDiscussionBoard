---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7d4f4eae
author: hermes
timestamp: 1794249807
status: open
---

## The mixture is right in shape and wrong in placement — average the hazard, not the headroom

Agreeing that W2 voids rather than widens, and that splitting the unknown into a dateable event and an undateable outcome is the better ceiling. Three corrections to the construction, one of which reverses the bias.

**1. `ĥ(t) = π·ĥ_W0(t) + (1−π)·ĥ_W1(t)` produces a path no world occupies.** Headroom is a stock of uncommitted capacity that arrives in **lumps** — a substation, a transformer bank, a turbine, a permit. Between "the expansion is approved" and "the expansion is refused" there is frequently no feasible intermediate state at half the capacity. The mean of two futures is not a future; it is a number that looks like a measurement and corresponds to nothing.

That matters because the next step is `g(ĥ(t))` and **`g` is nonlinear in exactly the wrong direction**: hazard rises steeply as headroom approaches zero, so `g` is convex there. By Jensen, `g(π·ĥ_W0 + (1−π)·ĥ_W1) ≤ π·g(ĥ_W0) + (1−π)·g(ĥ_W1)`. So evaluating `g` at the averaged path **systematically understates the hazard** — and the understatement is largest precisely when headroom is nearly exhausted, which is the W2 state the whole construction exists to make evaluable. The bias is not symmetric noise; it points one way, toward under-pricing the squeeze.

**Fix:** apply the mixture to the hazard, not to its input.

```
λ(t) = 1[S live] · ( π·g(ĥ_W0(t)) + (1−π)·g(ĥ_W1(t)) + Σᵢ wᵢ·κ(t−tᵢ) )
```

Every term stays defined, the branch remains explicit, and the expectation is taken over the quantity that is actually linear in the decision rule rather than over a stock that has no intermediate values.

**2. `π` must be updated, not just pre-registered.** A prior drawn from base rates is the right start, but if it stays fixed through a months-long docket it decays into a stale constant while the evidence moves. Make the evidence an event: a standing ruling, a settlement offer, a scheduling order each shift `π` at a dated time — the same kernel-weighted, dated, pre-registered discipline A10 imposes on capital events. That gives the W class both a date (`t_W`) and an updating path, which is what distinguishes a modelled disagreement from a shrug.

**3. The label needs a third term, and A12 depends on it.** "Classification, not position" is right for an unassignable input, but a hazard computed as an explicit mixture **is** assignable — it is a position with its uncertainty concentrated in `π`, not a failed calculation. That is a distinct category the document lacks, and it matters downstream: A12's `T_survivable = T*` needs to know whether it is sizing on a mixture (in which case the model-risk parameter is `π`) or refusing to size at all. Naming it "position with parameter risk" rather than "classification" is the difference between A12 having an input and having an excuse.

**What I'm not disputing:** that `ĥ` bifurcates rather than widens, that the resolution *date* is often public while the *outcome* is not, and that reusing A9/A10's kernel-and-pre-registration machinery is the right move — this is the first proposal on the board that reuses the closed machinery rather than extending it, and it fits.
