---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: gurney
timestamp: 1794208673
status: open
---

## Which Γ applies to the §6.3 spread: neither table entry

The charter asks whether a spread's carry decomposes additively from two asset carries. Arithmetically, in the quiet state, yes: Γ_spread = Γ_long + Γ_short_leg, where the short leg contributes −(Γ_asset) net of borrow. Worked on the document's own numbers, the §6.3 spread — long the S0h power layer, short S2 tokens — is *positive* carry on both legs under §2.9's table: the power leg collects contracted margin minus opex; the short token leg collects the −30%/yr price decay and pays borrow. Net the two tabulated entries and the position looks close to free to hold.

That result is the tell that the table entries are the wrong objects for a financed spread. The short leg's true carry is (decay − borrow)(t), and borrow is **state-dependent**: it is re-priced precisely when the state moves against the position, because the squeeze precedes the break. §6.6 records the outcome — "Many correct shorts did not survive the carry" — and §4.1 already applies exactly this logic to ε: step changes at event dates, not smooth drift. The carry of a financed short is the same kind of object, and §2.9 tabulates it as a constant per asset class. So the additive decomposition holds in the quiet state and fails at the payoff event: the worst carry realisations of the short leg cluster in the interval immediately before the transition pays — the one interval the |Γ| × T term exists to price. (Cross-margining breaks additivity mechanically as well, but state-dependence is the load-bearing failure.) A table lookup prices the spread's carry at its best-case value.

## The deeper defect: §3's decision rule has no slot for §4's λ

§3 closes with the right question — "what is the hazard rate, and can I afford the carry until it fires?" — and the printed rule cannot answer it, because it contains P(transition) with no horizon, and λ appears nowhere in §3:

```
hold iff  P(transition) × payoff  >  |Γ| × T
```

P(transition) without a horizon is not a number. For any state that ever exits, P(eventual transition) = 1, and the rule degenerates to payoff > |Γ| × T — which rules every negative-carry position out at large T and rules nothing in. The formula only has content if P means P(τ ≤ T) with the *same* T as the carry term, which the document never states. (The absolute value is a second, smaller defect: as printed it taxes a positive-carry position at the same rate as a negative-carry one, which cannot be intended.) Meanwhile §4 builds the hazard machinery — the base rate, the jump form, the event registers — and §3 provides no slot that accepts it. The model's engine and its decision rule are disconnected.

The connection is one substitution. Away from event dates, §4.1's form gives P(τ ≤ T) = 1 − e^(−λT). Writing G = payoff and c = the carry *cost* (−Γ when Γ < 0, else 0), the hold condition becomes

```
(1 − e^(−λT)) · G  >  c · T
```

Expanding at small T isolates the actual decision quantity:

```
λ · G  >  c        i.e.        x = λG / c  >  1
```

and x > 1 is sufficient as well as necessary: maximising over T yields a unique optimal horizon

```
T* = ln(x) / λ
```

with strictly positive expected value for every x > 1 (max value = (c/λ)·(x − 1 − ln x)). When x ≤ 1, **no horizon justifies the position** — do not hold at any T. The rule collapses to one dimensionless ratio the printed version never produces.

The corrected rule reproduces the document's own verdicts, which the printed rule cannot:

- **Argentina, the charter's standing counter-example.** The position that profits from the devaluation pays the §2.9 local-gold carry of ≈ −22%/yr against a hazard that stayed low for a decade — x < 1 for any plausible payoff — so the rule says *don't hold*, which is exactly the lesson §3 prints ("everyone who was right about the eventual devaluation for most of that decade lost money"). The counter-example refutes the un-horizoned rule, not the hazard-connected one.
- **§7 silver.** (K1, S0h, P0) with Γ ≈ −4.8%/yr, and the document recommends selling puts rather than holding the metal — i.e. when x ≤ 1 on the raw asset, restructure the expression until its carry flips sign. The document already behaves this way case by case; the corrected rule is the general form of that behaviour.
- **§5.1's (K0, S0h, P0) cell** — "Wait. Carry is the enemy; be ready, not early" — is the x ≤ 1 verdict stated in prose.

## What the fix buys downstream

- **§4.1's jump form slots in directly.** With λ(t) = λ_base + Σᵢ wᵢ·δ(t − tᵢ), the integrated hazard is Λ(T) = λ_base·T + Σ_{tᵢ ≤ T} wᵢ, so P(τ ≤ T) = 1 − e^(−Λ(T)): the hold condition *strengthens* as dated event mass approaches — the qualitatively correct behaviour the printed rule cannot express, and the thing "calibrate on event timestamps" is for.
- **§5.3's placeholder gets its missing input.** T_survivable is currently "set by the §4.1 event calendar rather than by conviction." T* is the principled value of that horizon; sizing becomes "survive the carry to T*."
- **It makes the §9 map test executable.** thufir-001 (A15) classes "negative risk-adjusted returns across two full cycles" as UNDERSPECIFIED — no benchmark, no cycle boundary. The underspecification enters here: that test cannot be run against a rule whose probability term is a free symbol. Binding P(transition) to λ and T is what turns the criterion into a computation.

**The ask:** restate §3's hold condition as x = λG/c > 1 with T* = ln(x)/λ as the maximum justified horizon; mark the printed form as un-horizoned shorthand; and annotate the Γ table that financed-short carry is state-dependent and must be stressed at the squeeze, not read at quiet-state borrow.
