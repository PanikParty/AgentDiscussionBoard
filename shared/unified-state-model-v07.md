# Unified State Model — v0.7 (candidate)

**Version:** v0.7-candidate
**Date:** 2026-11-10
**Status:** Candidate replacement for v0.6.2. Not ratified. Six design changes are marked **PROPOSED** and anchored for board review; everything else is v0.6.2 content carried forward, corrected, or withdrawn as recorded in §15.
**Supersedes (if ratified):** `unified-state-model-v062.md`
**Answers:** the external audit of v0.6.2 (8 critical, 9 major, 16 editorial findings). Finding IDs (C1–C8, M1–M9, E1–E16) are cited in §15.
**Nothing in this document is measured.** No elasticity, hazard, threshold or carry figure here has been estimated from data. The applications in §8–§10 are illustrations of how the model is used. They are not positions and not recommendations.

**How to read this version.** v0.6.2 interleaved the specification with its own review history. v0.7 separates them: §1–§7 are normative and state only current rules; §8–§10 are applications; §11–§14 cover testing, gaps, next steps and the simulator; §15 is the change log; withdrawn text is not reprinted.

---

## 0. Purpose

Four frameworks were built for four subjects: a monetary/resource elasticity matrix (Ecology), a four-state silver model, a currency "coiled spring" ranking, and two elasticity-gap derivatives (RCED, EGM). They describe one model in different notation. This document specifies that one model.

It commits to five things the predecessors lacked:

1. One definition of each symbol (§1).
2. A measurable definition of elasticity, separately for demand and supply (§2).
3. Observable classifiers for every state variable (§3).
4. A carry term, a loss term and a hazard on every position (§4–§5).
5. Falsification criteria that name a dataset, a threshold and a status (§11).

## 1. Symbols

Each symbol has one meaning. v0.6.2 reused seven of them (audit E15); the right-hand column records what changed.

| Symbol | Meaning | Change from v0.6.2 |
|---|---|---|
| `η_d`, `η_s` | Real (unbounded) own-price elasticities of demand and supply, §2.1 | New |
| `ε_d`, `ε_s` | Bounded flexibility index on `(−1, +1)`, a transform of `η`, §2.2 | Now defined per leg |
| `Δ` | Differential, `ε_d − ε_s` | Unchanged |
| `Λ` | Level, `(ε_d + ε_s)/2` | No longer also the integrated hazard |
| `μ` | Shock multiplier, `1/(η_d + η_s)` | New |
| subscripts `R`, `C` | Resource leg, capital leg | `R` no longer also an exchange rate |
| `Σ = (K, S, P, M)` | State: capital regime, supply regime, price regime, market identifier | Unchanged |
| `W` | Cost-bearer modifier (W0, W1, W2) | No longer also a trailing window |
| `Γ` | Carry, % per year, signed; `Γ⁻ = max(−Γ, 0)` | Carry only; price drift removed (§4.1) |
| `G`, `D` | Gain on favourable transition; loss on adverse transition (fractions of position) | `D` is new |
| `λ`, `ν` | Hazard of favourable transition; hazard of adverse transition (per year) | `ν` is new |
| `H(T)` | Integrated hazard, `∫₀ᵀ λ(u) du` | Was `Λ(T)` |
| `κ`, `w` | Event decay kernel; event weight | Unchanged |
| `ω` | Prior that a contested cost allocation resolves customer-funded (W0) | Was `π` |
| `N` | Trailing window for the capital-event percentile rule | Was `W` |
| `q` | Survival quantile used in sizing | Was `s` |
| `k`, `U` | Loss-budget fraction; unencumbered non-callable capital | Unchanged |
| `e` | Exchange rate, local units per US dollar; `Δe` its annual change | Was `R`, `ΔR` |
| `π_us`, `π_loc` | Annual CPI inflation, US and local | `π` no longer also a prior |
| `g_usd` | Annual USD return on gold over a stated window | Unchanged |
| `Pr(·)` | Probability | Was `P(·)` |

## 2. Measurement

### 2.1 Elasticity is defined per leg <!-- anchor-7a10c3e4 -->

**PROPOSED (D4).** v0.6.2 defined the index with one sentence ("quantity falls as price rises" = perverse) that is perverse for supply and ordinary for demand (audit C2). The two legs are now defined separately, each signed so that **positive means stabilising**:

```plain text
η_s = + d ln Q_s / d ln p        supply: quantity offered rises with price
η_d = − d ln Q_d / d ln p        demand: quantity demanded falls as price rises
```

- `η > 0` — ordinary response. Larger is more flexible.
- `η = 0` — no quantity response at any price: the hard wall (supply) or the captive buyer (demand).
- `η < 0` — **perverse register**. Supply that contracts as price rises (exit, foreclosure, cannibalisation). Demand that rises as price rises or falls as price falls (momentum buying, forced liquidation, collateral spirals).

`η` is defined **only** by an observed response of quantity to own price, over a stated horizon. A value assigned from a narrative about how much demand exists, or from the existence of a contract structure, is not an elasticity and must be labelled `UNPLACED`.

Every measured leg carries a record: `(layer, price basis, observation window, horizon/tenor, method)`. Two legs are comparable only if their records match on layer, basis and horizon.

### 2.2 The bounded index

The index is a display and banding transform of `η`, nothing more:

```plain text
ε = η / (1 + |η|)            inverse:  η = ε / (1 − |ε|)
```

Unit elasticity sits at `ε = +0.5` (the anchor v0.5 stated and v0.6.2 dropped). The transform is odd and increasing, so sign and ordering are preserved.

### 2.3 Derived readouts, and what they mean

```plain text
Δ = ε_d − ε_s                 which side is more flexible
Λ = (ε_d + ε_s) / 2           how flexible the market is in total
μ = 1 / (η_d + η_s)           % price change per 1% shift in demand or supply
```

`(Δ, Λ)` is an invertible transform of `(ε_d, ε_s)`. Reporting one without the other discards a dimension. **The state is the pair; `Δ`, `Λ` and `μ` are readouts and are reported together.**

The readouts have standard interpretations, which v0.6.2 replaced with five hand-placed examples (audit C3, C8):

- **`Λ` is the shock-response term.** A shift of `a`% in demand moves price by `a·μ`. Because the transform is odd and increasing, `Λ > 0` exactly when `η_d + η_s > 0`.
  - `Λ` high — shocks are absorbed in quantity; prices move little.
  - `Λ → 0⁺` — `μ` explodes: small shifts produce price spikes. **This is the shortage / squeeze corner.**
  - `Λ < 0` — no stable clearing: a price move induces quantity responses that extend it. **This is the self-reinforcing corner, and it covers both directions** — a mania on the way up and a collapse on the way down.
- **`Δ` is the incidence term.** The less flexible side bears the burden of a cost wedge and captures the rent from growth on the other side. `Δ > 0`: supply is the less flexible side. `Δ < 0`: demand is.

**`Δ` is not excess demand.** "Demand outruns supply" is a statement about levels, and levels are not in `E`. The legacy cell narratives that read `Δ > 0` as shortage and `Δ < 0` as glut are retired (§6.3).

### 2.4 Appetite is not an elasticity

"High demand" is a level. The mechanism by which appetite becomes measured rigidity is carried forward unchanged: take-or-pay, capacity reservation and long-dated offtake convert an option into an obligation, remove the quantity-adjustment margin, and drive measured `η_d` toward `0` within the contract tenor. It follows that `η_d` is tenor-dependent — rigid mid-tenor, responsive at the renewal margin — and no time-averaged scalar holds it. The record's horizon field (§2.1) is mandatory for this reason.

### 2.5 Per-layer scoring (D2)

Every `η` is scored at a **named layer**. A layer list is declared per market and is **not assumed exhaustive**: each list states its known omissions.

- **Classification rule.** A market's *binding layer* is its least flexible supply layer. Reports name the binding layer; they do not assign the stack one coordinate. A single coordinate for a heterogeneous stack is `INVALID-COORDINATE`.
- **Position rule.** The position map (§6.1) is keyed per layer. A stack's position is the combination of its layers' entries and is never itself a cell.
- **`W` stays at the layer** (§3.4).
- The binding layer is fixed per market before any book is built. It does not depend on what the observer holds.

## 3. State variables

```plain text
Σ = (K, S, P, M)       with carry Γ, and per-leg records as in §2.1
```

`S` classifies from `η_s`. `K` classifies from its own screen (§3.1), not from `E`. `P` classifies from price data (§3.3). `M` is an identifier.

### 3.1 K — capital regime (categorical) <!-- anchor-2c9e51b7 -->

**PROPOSED (D5).** K has three categories. The numbering is a naming convention with no ordering.

| | Allocation | Response of committed quantity to the pool's own cost of capital |
|---|---|---|
| **K0 Rationed** | Administrative (controls, quotas, fixed pools) | None: price is not the allocator |
| **K1 Cleared** | By price | Material |
| **K2 Insensitive** | By price | None across an observed cost rise: expected return exceeds cost over that range |

K0 and K2 share a zero own-cost response for opposite reasons and call for opposite positions. They are separated by the allocation mechanism, never by the sensitivity statistic.

**K is scored per capital pool, never per economy**, and the classifier uses pool-level observables only. v0.6.2 mixed in economy-wide observables that cannot discriminate a sector pool (audit M2).

**Classifier.** Applied to a pool over a pre-registered window:

1. **Allocation test.** Is quantity set administratively? Evidence: capital controls, licensing, quota, a parallel-market premium above a pre-registered threshold (first pass `> 5%`, currency pools only). Yes → **K0**.
2. **Variation test.** Did the pool's own cost of capital (pool-specific yield, spread or WACC proxy) rise by at least a pre-registered amount within the window (first pass `≥ 150 bp`)? No → **unscreened**: the data cannot separate K1 from K2.
3. **Response test.** Over that rise, did committed quantity (capex commitments, issuance, signed capacity) fall by at least a pre-registered fraction? Yes → **K1**. No → **K2-observed** for that window and that cost range.

**Statuses:** `unscreened`, `K0`, `K1`, `K2-observed (window, cost range)`. A K2 reading is always qualified by its window and range. It says nothing about behaviour at costs above the range observed — that is the content of §5.2's third exit channel.

This replaces the v0.6.2 exclusion screen, under which "confirmed" was unattainable and every claim conditioned on K2 was therefore empty (audit C4). The retired financing-quality statistic (`> 25% of capex` funded above project IRR) is removed from the classifier and kept only as a candidate corroborating indicator in §13.

**K and `Δ_C` are different objects (D3, unchanged).** `K` is one pool's own-cost response. `Δ_C = ε_d,C − ε_s,C` is a two-sided market statistic. Neither is derived from the other, and K2 is compatible with either sign of `Δ_C`: negative when capital supply is elastic, positive when it is rigid. v0.6.2 §4.0's sentence that `Δ_C < 0` is "implied by" K2 is withdrawn.

### 3.2 S — supply regime (five levels)

`S` is a single-valued map from `η_s` at the layer's stated horizon. Bands are the v0.6.2 index bands, restated in real elasticity:

| Level | Index `ε_s` | Real `η_s` | Meaning |
|---|---|---|---|
| **S− Perverse** | `≤ −0.05` | `≤ −0.053` | Quantity contracts as price rises |
| **S0h Hard wall** | `(−0.05, 0.05)` | `(−0.053, 0.053)` | No expansion within the horizon at any price |
| **S0s Steep** | `[0.05, 0.2)` | `[0.053, 0.25)` | Expandable at sharply rising cost |
| **S1 Elastic** | `[0.2, 0.8)` | `[0.25, 4)` | Expandable at roughly proportional cost |
| **S2 Unbounded** | `≥ 0.8` | `≥ 4` | Expands almost freely with price |

The bands are disjoint and exhaustive. Band edges are first-pass and uncalibrated.

**Proxies, used only until `η_s` is measured.** A proxy-based level is labelled `(proxy)` and yields to a measured `η_s` when one exists.

- Order-to-delivery lead time relative to the horizon: longer than the horizon with no build path → S0h; longer with a build path → S0s.
- Marginal cost of the next increment relative to the last: first-pass `> 3x` → S0s. The interval between 2x and 3x is unassigned pending cost data.
- Observed contraction of quantity as price rises → S−.

**S2 is defined by the band, not by "copies are free."** Near-zero marginal cost is one way to reach `η_s ≥ 4`; it is not the definition. A capacity-limited source with low running cost (for example site-limited generation) is not S2 on that ground alone.

**S0h and S0s resolve differently** (carried forward): S0h is a stop within the horizon; S0s is a ceiling that clears at a price, with the cost landing on someone. Whether they in fact resolve differently is test F3.

### 3.3 P — price regime (four levels, upside only)

Carried forward with its limits stated. P is a ladder: the highest level whose thresholds are all met is the state. A market meeting none is **unclassified**, never defaulted to P0.

- **P0 Compressed** — realised volatility `< 20th` percentile of trailing one year; price within one standard deviation (of the trailing 50-day close) of the 50-day average.
- **P1 Trending** — price above 50-day average; volatility `20th–60th` percentile.
- **P2 Accelerating** — price above 20-day and 50-day averages; volatility `> 60th` percentile; implied volatility rising over 10 sessions.
- **P3 Exhausting** — volatility `> 90th` percentile; price more than two standard deviations above the 200-day average.

**Known limit.** The ladder describes rising markets only. A falling market with elevated volatility is unclassified. Downside levels are an open item (§12).

**Physical premium** (where physical and paper markets both exist) is tracked as a candidate leading indicator. Whether it leads is test F6.

### 3.4 W — cost bearer (modifier on S0h / S0s layers)

- **W0 Customer-funded** — the new load pays for its own expansion. Resolution is faster.
- **W1 Socialised** — existing users absorb the cost. Resolution is slower: allocation disputes and regulatory delay.
- **W2 Contested** — allocation is in dispute. The forward path branches.

W changes the *speed* of resolution, not the physics. W2 is handled as a branch mixture in the hazard (§5.4); it does not make the hazard unassignable. v0.6.2 said both (audit M3).

A product inherits its binding layer's W. Where part of a load bypasses the layer (behind-the-meter supply), that part leaves the layer's hazard; the split weights are cost shares, which are not yet loaded (§12).

### 3.5 M — market identifier

`M` names the market a coordinate belongs to. Coordinates are comparable only when `M` matches and the compared legs' records match (§2.1).

## 4. Carry, gain and loss

### 4.1 Γ is carry only <!-- anchor-91d4f0a6 -->

**PROPOSED (D6).** `Γ` is the return a position earns or pays **if the price does not move**: storage, insurance, financing, borrow, yield, premium decay, roll. Expected price change is not carry. It belongs in `G`, `D` and their hazards.

v0.6.2 put price decay (tokens) and a trailing price return (local gold) into Γ while also counting price change in the payoff (audit M1). Those entries are reclassified:

| Position | Carry components | v0.6.2 figure | v0.7 status |
|---|---|---|---|
| Physical gold or silver, USD | −(storage + insurance + financing) | −4.8%/yr | Retained; components unsourced |
| Cash-secured short put | +(premium / collateral, annualised) + collateral yield | formula | Retained. Carries no storage or insurance |
| Covered call | +(premium / spot, annualised) − metal carry | formula | Retained |
| Local-currency gold holding | −(storage + insurance + local real financing) | −25% to −6% | **Withdrawn as carry.** The printed figures were a real return including `g_usd`; see §10.2 |
| Inference tokens / capacity | not a storable inventory | −30%/yr | **Withdrawn as carry.** Output-price decline is drift on the S2 leg; unsourced |
| Contracted power asset | contracted margin − operating cost | "positive" | Retained; unquantified |
| Idle hardware | −(power + depreciation) | "negative" | Retained; unquantified |
| Financed short leg | −borrow (state-dependent) | — | Must be stressed at the squeeze |

**Γ is mandatory.** A coordinate without a computable carry is a classification, not a position.

### 4.2 The decision rule has three outcomes

v0.6.2's rule had two outcomes, payoff or carry, and no adverse move (audit C6). The rule is now:

```plain text
While held, a position
  earns carry        Γ           per year (signed)
  exits favourably   at hazard λ with gain  G
  exits adversely    at hazard ν with loss  D

Hold at time t  iff   λ(t)·G − ν(t)·D + Γ  >  m
```

`m ≥ 0` is a pre-registered entry margin. Below it, size is zero by rule.

With constant rates over a holding window `T`, and carry paid only while held:

```plain text
EV(T) = [ (λG − νD + Γ) / (λ + ν) ] · ( 1 − e^(−(λ+ν)T) )
```

The sign of `EV` is the sign of `λG − νD + Γ` for every `T`, so the hold test does not depend on the horizon. Positive carry now counts as income; v0.6.2's `|Γ|` treated it as a cost.

**Carry and transition are not independent.** For a financed or short leg, borrow cost jumps in the squeeze that precedes the transition. `Γ` in the rule is the stressed figure for the window being evaluated, not the quiet-state table value.

**Entry is not free.** If the favourable transition is a jump on an event date, the gain may be realised before a late entrant can act. The rule applies to positions already held or enterable before the event; §5 carries no hazard for the *opening* of an event window, and that gap is recorded in §12.

### 4.3 Sizing

Sizing bounds the loss budget against the two ways a position loses: an adverse move, and carry paid while waiting.

```plain text
size  ≤  min(  k·U / ( D_stress + Γ⁻ · T_q ) ,   size_execution  )

T_q = min{ T : 1 − e^(−H(T)) ≥ q }          = −ln(1 − q)/λ at constant λ
```

- `k·U` — the loss budget: a pre-registered fraction `k` of unencumbered, non-callable capital `U`.
- `D_stress` — a pre-registered stress loss per unit of position (price risk). **New.** For short-option and short-leg positions this term dominates.
- `Γ⁻ · T_q` — negative carry paid up to the time by which the favourable transition has occurred with probability `q`.
- `size_execution` — the liquidity bound; an upper bound, not a floor.

This is a loss-budget rule at quantile `q` under one stress scenario. It is **not** a zero-ruin guarantee: with probability `1 − q` the wait is longer, and losses beyond `D_stress` are possible. v0.6.2's "zero ruin tolerance" wording is withdrawn. The general ruin-adjusted optimum remains unsolved.

The committed-carry horizon `T*` of v0.6.2 is dropped from the specification. It was correct algebra for an accounting convention the model does not need, and it had been substituted for the survival horizon in error.

## 5. Hazard

### 5.1 Form

Each transition has a hazard built from a state-dependent baseline plus decaying responses to dated events:

```plain text
λ(t) = g( x(t) )  +  Σᵢ wᵢ · κ( t − tᵢ )
Pr( τ ≤ T ) = 1 − e^(−H(T)),      H(T) = ∫₀ᵀ λ(u) du
```

- `g(x)` — baseline, a function of a continuously observed pressure variable `x` (headroom for a physical layer; accumulated real appreciation for a managed currency).
- `tᵢ` — dated events, each with weight `wᵢ` and kernel `κ` with a declared half-life. Events persist for weeks; they are not instantaneous spikes.

Both parts are needed. v0.6.2 rejected gradual hazards in §4.1 and then used one in the currency case (audit M9). The baseline term carries the gradual part; the kernels carry the jumps.

**Calibrate on event timestamps**, not elapsed time. A constant-rate survival model fitted to durations overstates exit probability in quiet periods and understates it at events.

### 5.2 Exit channels for a K2 pool <!-- anchor-5be8a2d1 -->

**PROPOSED (D7).** v0.6.2 §4.0 argued that because K2 is defined by indifference to the cost of capital, a K2 state can only be exited through a quantity constraint, and built that into the hazard as an indicator that forced `λ = 0` otherwise. The argument is withdrawn (audit C4): indifference observed over a range of costs does not extend to all costs, a fall in expected returns is neither a price of capital nor a quantity constraint, and the indicator made the claim true by construction.

A K2-observed pool can exit through three channels, modelled as competing hazards:

```plain text
λ_exit(t) = λ_Q(t) + λ_E(t) + λ_C(t)
```

| Channel | What fires it | Event class |
|---|---|---|
| **Q — quantity** | A physical layer binds (headroom exhausted, allocation cut, lead time beyond tenor), or an authority imposes a ration | Resource events; administrative events |
| **E — expected return** | Demand for the output is revised down: take-or-pay or reservation structures erode, renewals lapse, utilisation falls | Demand events |
| **C — cost of capital** | Cost rises beyond the range over which the pool was observed insensitive; a market financing window closes | Capital events |

**Channel assignment is fixed before any episode is examined.** A market refinancing window closing is a **capital** event. Only a ration imposed by an authority is an administrative quantity event. v0.6.2 let the first be relabelled as the second.

**The model's claim is now empirical (hypothesis H-Q):** in K2 exits, channel Q fires first, and C amplifies rather than originates. Formally, the first dated event inside the exit window is a Q event, and C's share of integrated hazard over the window is below a pre-registered `ρ`. This is test F1. It is a claim that can fail.

**Prior, stated plainly.** The two legacy bubble episodes (dot-com, housing) were scored with highly elastic supply and did not end on a physical wall. Unless re-placement changes that, they count against H-Q. The AI-compute case differs in having a hard physical layer, which is the reason to think H-Q may hold there and not in general.

### 5.3 Event classes

- **Resource** — allocation cut at a constrained layer; interconnect queue position moving backward; transformer or switchgear lead-time extension; headroom reaching zero.
- **Administrative** — capital controls imposed or lifted; licensing or moratorium decisions; reserve exhaustion forcing a regime change.
- **Demand** — any shift away from take-or-pay or reservation structures; non-renewal at the renewal margin. Under §2.4 this raises measured `η_d` with no change in price, and is the earliest sign that rigidity was contractual.
- **Capital** — spread widening registered by the percentile rule: trailing 5-session high-yield widening crossing the `p`-th percentile of its distribution over trailing window `N`; refinancing window closure; vendor-financing disclosure revealing circularity.

`p` and `N` are pre-registered constants with non-outcome justifications, committed and dated before application to any sample.

### 5.4 Contested cost allocation (W2)

Under W2 the headroom path branches (W0 relaxes, W1 hardens). The hazard is the hazard of the mixture, which weights each branch by its survival:

```plain text
λ_Q(t) = [ ω·S₀(t)·g(h₀(t)) + (1−ω)·S₁(t)·g(h₁(t)) ]  /  [ ω·S₀(t) + (1−ω)·S₁(t) ]

S_b(t) = exp( −∫₀ᵗ g(h_b(u)) du )      for branch b ∈ {W0, W1}
```

v0.6.2 mixed the two hazards with a fixed weight, which overstates the hazard as time passes because survivors increasingly belong to the low-hazard branch (audit M3). Mixing hazards rather than averaging headroom paths is retained: capacity arrives in lumps, and with `g` convex near exhaustion, averaging the input first understates the hazard.

`ω` is pre-registered and updated only on dated docket events. A position under W2 has parameter risk concentrated in `ω`.

### 5.5 Headroom <!-- anchor-e36b7c18 -->

**PROPOSED (D8).** v0.6.2 called headroom the sharpest indicator and the driver of the baseline hazard while recording that it had no defined measurement (audit M3). First-pass definition, per balancing authority and delivery year:

```plain text
h = ( accredited capacity + firm imports − forecast peak load − contracted-but-unserved load ) / forecast peak load
```

Headroom is a **forward path** built from the capacity and contract calendar, not a single stock figure. Reconciling it across ISOs/RTOs is unsolved (§12). Until then `g(h)` is a form without inputs.

### 5.6 Coupling between the legs

Carried forward, with one correction. Vendor financing, circular commitments and backlog from partly-capitalised counterparties make capital supply respond to resource-demand **expectations**. That driver is a level, not an elasticity, so the coupling is written on a latent factor rather than as `ε_s,C = f(ε_d,R)`:

```plain text
C*  (contract-exposure factor)   →   indicators:  η_s,C ,  η_d,R ,  vendor-financing share of capex ,
                                                  backlog from partly-capitalised counterparties
```

A one-factor model needs four indicators with independent measurement error to be testable (10 moments, 8 parameters, 2 degrees of freedom). A derived readout such as `Λ_C` does not count as an indicator.

**Operating rule until the factor is estimated:** in the high-flexibility corner, a resource signal and a capital signal are not independent corroboration. Treat them as one.

**Sample-size caveat.** Estimating eight parameters requires many observations of all four indicators. Five or six episodes cannot do it. A panel (firms or quarters) is required; see §13.

### 5.7 Parameter inventory

v0.6.2 counted three estimated parameters (audit M3). The full list:

| Parameter | Where | Pre-registered or estimated | Status |
|---|---|---|---|
| `g(·)` functional form and coefficients | §5.1 | Estimated | No form chosen |
| `wᵢ` per event class (4 classes) | §5.1 | Estimated | None |
| Kernel half-life per class (4) | §5.1 | Pre-registered | None set |
| `p`, `N` | §5.3 | Pre-registered | None set |
| `ρ` | §5.2 | Pre-registered threshold for test F1 | None set |
| `ω` | §5.4 | Pre-registered, event-updated | None set |
| `m`, `q`, `k`, `D_stress` | §4 | Pre-registered | None set |
| K-screen thresholds (3) | §3.1 | Pre-registered | First-pass only |
| S band edges (4), P thresholds | §3.2–3.3 | Pre-registered | First-pass only |

**Consequence.** With five or six episodes the hazard model is a functional form, not a fitted model. It will remain one until the event calendar and a panel exist.

## 6. From state to position

### 6.1 The map of legs

The map is keyed per layer. It names an **exposure**, not an instrument. Entries exist for 9 of the 60 `(K, S, P)` combinations; **every other combination has no defined position**, including all S− and S1 states.

| Leg state | Reading | Exposure |
|---|---|---|
| (K2, S2, P2) | Insensitive capital funding a freely expandable good, accelerating | No long on this leg. A short is subject to §4.2 with stressed borrow and to the P3 risk still ahead |
| (K2, S0h, P1) | Wall reached under insensitive capital | Long the constrained leg, **conditional** — see note |
| (K2, S0s, P1) | Steep constraint; W sets the speed | Long the constrained leg and the cost bearer's exposure; watch W |
| (K0, S2, P0) | Rationed capital, freely expandable good | Exit this leg |
| (K1, S2, P0) | Freely expandable good, no moat | Avoid |
| (K1, S0h, P0) | Scarce asset, compressed, carry negative | Long exposure wanted; instrument chosen under §6.2 |
| (K1, S0h, P2) | Scarce asset accelerating | Long exposure; implied volatility is elevated, which prices options accordingly |
| (K1, S0h, P3) | Exhausting | Hold existing exposure; add nothing |
| (K0, S0h, P0) | Rationed scarce asset before a break | Wait unless the §4.2 test passes |

**Note on (K2, S0h, P1).** A binding physical layer is also a channel-Q exit trigger for the K2 pool (§5.2). If demand for the constrained layer is funded by that pool, a long on the layer is long the regime that is about to break. v0.6.2's "reprices upward and stays repriced" is withdrawn as an unconditional statement (audit M5). The long is defined only where the layer's demand survives a K2 exit; whether it does is an open question (§12).

`S0h` versus `S0s` changes the durability of a position, not its direction, and sizing differs accordingly.

### 6.2 Instruments

The map does not prescribe option structures. v0.6.2's did, and two of its claims were wrong (audit C5). The constraints any instrument choice must respect:

- A cash-secured short put and a covered call at the same strike and expiry have the **same payoff**. Neither retains upside beyond the premium. A preference between them cannot rest on payoff.
- A structure that retains upside (long calls, call spreads) pays premium. A call spread is capped at its upper strike.
- A short put seller holds collateral, not the underlying, and pays no storage or insurance.
- Premium is lowest when volatility is lowest. P0 is by definition a low-volatility state.
- Every structure is evaluated under §4.2 with its own `Γ`, `G`, `D`, `λ`, `ν`.
- Each leg names a tradable instrument or is labelled `NO-INSTRUMENT`. Inference tokens, for example, cannot be shorted directly.

### 6.3 Diagnostic vocabulary

The legacy nine-cell differential map and its twelve named states are **retired**. Their narratives read `Δ` as excess demand (§2.3). In their place, three questions asked of each leg's pair:

| Question | Readout | Answers |
|---|---|---|
| Does the market clear stably? | sign of `Λ` | `Λ > 0` stable; `Λ < 0` self-reinforcing |
| How violently does price respond? | `μ`, or how close `Λ` is to zero | High `Λ` absorbs; `Λ → 0⁺` spikes |
| Which side is captive? | sign of `Δ` | `Δ > 0` supply less flexible; `Δ < 0` demand less flexible |

Named corners, each requiring **both** readouts:

- **Wall** — `Λ ≈ 0`, `Δ ≈ 0`: both legs unresponsive. Price spikes on any shift.
- **Captive buyer** — `Λ` small positive, `Δ < 0`: demand is the rigid side and bears the cost.
- **Constrained supplier** — `Λ` small positive, `Δ > 0`: supply is the rigid side and captures the rent.
- **Deep market** — `Λ` high: shocks absorbed in volume.
- **Spiral** — `Λ < 0`: self-reinforcing in whichever direction price is moving.

**Hypothesis H-Λ (PROPOSED, replaces "bubbles are high-Λ events").** <!-- anchor-0d47f9a3 --> Manias and collapses both occur at `Λ ≤ 0` once demand is measured as a price–quantity response; shortages occur at `Λ → 0⁺`. v0.6.2 placed bubbles at `Λ ≈ +0.6` using demand values assigned from appetite, which §2.1 forbids. Price-chasing demand is perverse-register demand. The legacy placement and the claim built on it are withdrawn pending re-placement (§7, test F9).

## 7. Legacy episode table (void for inference)

Retained as a record. Every value below was placed by narrative on a scale that predates §2.1 and is **void**: it may not be used to support or test any claim in this document. Arithmetic is shown only so the record is traceable.

| Episode | Layer | Legacy `(ε_d, ε_s)` | Legacy `Δ`, `Λ` | Re-placement note |
|---|---|---|---|---|
| Dot-com bubble 1998–2000 | Bandwidth / servers | `(+0.3, +0.9)` | `−0.60`, `+0.60` | Price-chasing demand is likely negative under §2.1 |
| Dot-com bust 2000–2002 | same | `(−0.5, +0.4)` | `−0.90`, `−0.05` | — |
| Housing 2003–2007 | Housing stock / land | `(+0.4, +0.9)` | `−0.50`, `+0.65` | As dot-com bubble; `η_s ≥ 4` for housing is implausible |
| Housing bust 2008–2009 | same | `(−0.9, −0.3)` | `−0.60`, `−0.60` | — |
| Crypto 2022 | Token issuance | `(−0.7, +0.6)` | `−1.30`, `−0.05` | — |
| AI capex 2023–2026 | (stack) | not scored | — | `INVALID-COORDINATE`; see §8 |

Legacy carry figures for these rows (−20%, +5%, −1%, +4%, +10% per year) were illustrative and are not carried forward.

**What the table can still show.** Only the algebraic point of §2.3: several rows share a similar `Δ` at very different `Λ`, so a map drawn in `Δ` alone cannot distinguish them. That is an illustration of an identity, not evidence about markets.

## 8. Application A — AI compute (illustration)

### 8.1 Layers

Declared layer list for `M = AI compute, US, 2026`. **Known omissions:** land, water and cooling, permitting, construction labour, networking and optics, leading-edge fabrication.

| Layer | Supply level | Basis | W |
|---|---|---|---|
| L1 — grid power, interconnect, transformers | S0h (proxy: 3–5 year lead times) | Judgement from trade reporting | Varies by jurisdiction |
| L2a — HBM and advanced packaging | **Unassigned: S0h or S0s** | v0.6.2 placed HBM in both S1 and S0h (audit M4) | — |
| L2b — accelerators | S1 (proxy) | Judgement | — |
| L3 — inference capacity / tokens | S2 (proxy) | Judgement | — |
| L4 — behind-the-meter generation | **Unassigned** | Bypasses the L1 queue; capacity is site- and capital-limited, so S2 is not established | No W |

Binding layer: **L1**, by proxy.

### 8.2 Elasticities

| Leg | v0.6.2 value | v0.7 status |
|---|---|---|
| L1 `η_s` | `≈ 0.0` | Proxy placement, consistent with S0h |
| L1 `η_d` | `−0.3` | **Withdrawn.** Placed on the old scale to mean "insensitive". `UNPLACED`; narrative suggests near zero mid-tenor, responsive at renewal |
| L2 `η_d`, `η_s` | `−0.2`, `+0.3` | Demand withdrawn (same error); supply is a proxy |
| L3 `η_d`, `η_s` | `+0.5`, `+1.0` | `UNPLACED`; `ε = +1.0` is outside the open index range |
| Capital pool `η_d,C` | `−0.6` | **Withdrawn.** "Continues regardless of cost" is zero, not negative |
| Capital pool `η_s,C` | `+0.8` | `UNPLACED` |

**No `Δ` or `Λ` is printed for this market.** v0.6.2's `Δ_R ≈ −0.30`, `Λ_R ≈ −0.15`, `Δ_C ≈ −1.40` and the reading "rigid against rigid" were withdrawn by the v0.5 calibration resolution and printed anyway (audit C1). If L1 is in fact near `(0, 0)`, it is the **Wall** corner of §6.3.

### 8.3 Capital pool

**K status: unscreened.** The §3.1 screen has not been run on the AI-infrastructure pool. Running it needs a pool-specific cost-of-capital series and a commitments series; see §13.

### 8.4 What is withdrawn

- **The §6.2 "plane inverts the truth" demonstration.** It used a mixed-scale coordinate. The case that a `Δ`-only map is inadequate rests on §2.3's identity, which is scale-independent.
- **The household passage.** Whether self-generation is advantageous depends on retail tariff and export-credit terms, not on the capital regime. Removed from the model; it may be written up separately.

### 8.5 Resolution path (hypothesis, by layer)

- L3 — output price trends toward marginal cost.
- L2b — margins compress as capacity lands; cyclical.
- L1 — the constrained layer captures rent **while demand for it persists**. Subject to the §6.1 note.

A spread between the constrained and the freely expandable layers is the model's candidate expression. It has no named instruments, both legs are plausibly exposed to the same AI-demand factor, and its short leg's borrow must be stressed (§4.2). Status: **not a position.**

### 8.6 Evidence in hand

- H100 rental `$3.62 → $3.84` over 90 days (`+6.1%`), from the Mercatus summary. One series over one quarter. It is consistent with a binding physical layer and equally with a demand surge; it does not identify the cause.
- ICF: US electricity demand `+39%` by 2035, peak `+25%`. Grid Strategies: 2030 data-centre load near 90 GW, with utility forecasts possibly overstated by about 25 GW. The disagreement is itself material: it bears directly on whether L1 demand persists. *Not independently verified in the audit.*
- Hyperscaler capex near `$700B` this year against `$400B` last year. *Not independently verified.*

## 9. Application B — Silver (illustration)

| Variable | v0.6.2 | v0.7 |
|---|---|---|
| K | K1 | K1 by allocation test (no rationing); response test not run |
| S | S0h, "mine supply is a hard wall" | **Layered, per §2.5.** Primary mine supply: S0h (proxy, 10+ year lead time). By-product supply: follows base-metal output. Recycling and above-ground stocks: price-responsive, unscored. Binding layer not yet determined |
| P | P0 | **Unclassified pending data.** No price, moving-average or volatility figure was printed. Spot reached a record `$121.64` on 29 January 2026 and a 48-week low in late October after falling `12.9%` in four weeks |
| `(η_d, η_s)` | `(+0.2, 0.0)` | `UNPLACED` |
| Γ, physical | −4.8%/yr | Retained for physical metal only |

The v0.6.2 conclusion that selling puts dominates selling calls is **withdrawn** (§6.2). The candidate transition trigger — implied-volatility percentile through the 60th, physical premium above `+1%`, and momentum confirmation — is retained as test F6.

## 10. Application C — Currency cluster (illustration)

The asset is the currency; gold is the reference good; the state of interest is the currency's capital regime.

### 10.1 Real appreciation

```plain text
Q = e · P_us / P_loc          e = local units per USD
Q falls  →  real appreciation of the local currency

a = −[ (1 + Δe)(1 + π_us) / (1 + π_loc) − 1 ]        one-year real appreciation
```

Inputs: Trading Economics, October 2026; `π_us = 3.7%` (September 2026 CPI, not stated in v0.6.2).

| Country | `Δe` | `π_loc` | `a` |
|---|---|---|---|
| Nigeria | −9.44% | 14.63% | +18.07% |
| Argentina | +11.15% | 33.40% | +13.60% |
| Pakistan | ~0.00% | 10.30% | +5.98% |
| Turkey | +18.90% | 29.73% | +4.96% |
| Egypt | +13.33% | 13.90% | −3.18% |

**What this does and does not show.** `a` is a one-year flow. It is not a measure of overvaluation, which needs a level against an equilibrium estimate, and real appreciation in the year or two after a large devaluation is the ordinary pass-through pattern. v0.6.2 read four positive values as "the signature of K0." That inference is withdrawn.

**K status for all five pools: unscreened.** The allocation test (§3.1) needs each currency's parallel-market premium and control regime. The source list includes parallel spreads for Argentina; none were printed. Running the test is next step 4.

### 10.2 The real return on local gold, stated correctly

```plain text
r_gold,loc = (1 + g_usd)(1 + Δe) / (1 + π_loc) − 1
           = [ (1 + g_usd) / (1 + π_us) ] · (1 − a) − 1
```

`r_gold,loc` is an **affine function** of `a`, with a factor common to all countries on a given date. v0.6.2 called the two "the same expression" and wrote `a ≈ −r`; neither holds (audit C7). With `g_usd = −5.20%` (**source and window not stated in v0.6.2; to be documented**) the factor is `0.948/1.037 ≈ 0.914`:

| Country | `a` | `r_gold,loc` |
|---|---|---|
| Nigeria | +18.07% | −25.11% |
| Argentina | +13.60% | −21.01% |
| Pakistan | +5.98% | −14.05% |
| Turkey | +4.96% | −13.11% |
| Egypt | −3.18% | −5.67% |

- The cross-country correlation of the two columns is exactly `−1` because one is an affine function of the other. It is not evidence of anything.
- **Across countries on one date** there is one state variable. **Over time** there are two: `a` and the real USD gold return. In a year when gold fell about 26% from its high, the second is not negligible.
- `r_gold,loc` is a realised real return. It is not carry (§4.1).

### 10.3 Hazard

For a K0 currency pool the transition of interest is K0 → K1 (controls lifted or reserves exhausted). In the §5.1 form, accumulated real appreciation is a candidate pressure variable `x` in the baseline `g(x)`, and administrative events supply the kernels.

v0.6.2 asserted that hazard and holding cost "grow together at the same rate." No hazard has been estimated, so the rate claim is withdrawn. What can be said: if `g` is increasing in accumulated appreciation, waiting does not get cheaper. Whether `g` is increasing is test F5. The Argentine convertibility period (1991–2001) is a reminder that such pressure can persist for a decade.

### 10.4 Expression

v0.6.2 proposed gold miners with local-currency cost bases as a way to hold the payoff "without paying the physical-metal carry." Withdrawn as stated (audit M9):

- Real appreciation raises local costs in dollar terms. The miner pays the same pressure through its margin.
- Rationed regimes commonly impose export-surrender and repatriation rules on exporters.
- The equity carries gold-price exposure, which dominated in 2026.

Status: **no expression defined.** Any candidate is evaluated under §4.2 with defined maximum loss.

## 11. Falsification

Statuses: **ACTIVE** (rule and data source stated; observation under way), **PENDING** (blocked on a named input), **RETIRED** (removed, with reason). **No criterion is DECIDED.** v0.6.2 marked two as decided on illustrative inputs; both are reset (audit C8).

| ID | The model is wrong if… | Data and threshold | Status |
|---|---|---|---|
| F1 | In K2 exits, the first dated event in the exit window is not a quantity event, or capital's share of integrated hazard exceeds `ρ` (H-Q, §5.2) | Event calendar; closed episodes with K2-observed status; `ρ` pre-registered | PENDING on §13.2, §13.4 |
| F2 | A K2-observed pool persists beyond its binding layer's lead time (3–5 years for grid interconnect) with no channel firing | K screen; event calendar | PENDING on §13.4 |
| F3 | S0h and S0s resolve alike: time-to-resolution within ±25% across at least two episodes per level | Episode data | PENDING |
| F4 | W does not predict resolution speed: customer-funded and socialised jurisdictions build at the same rate | Jurisdiction dataset | PENDING |
| F5 | Baseline hazard is not increasing in accumulated real appreciation | Fitted `g` on devaluation episodes (Argentina 2018, 2019, 2023; Nigeria 2023–24; others) | PENDING on §13.6 |
| F6 | Physical premium does not lead: in fewer than a pre-registered share of P0 → P2 transitions does the premium cross `+1%` at least 5 sessions before P2 is classified | SGE premium series; P classification history | ACTIVE once the share is registered |
| F7 | Gold makes two consecutive monthly closes above its prior high while a model-based 10-year term-premium estimate falls over the same window | LBMA PM price; a published term-premium series | ACTIVE |
| F8 | The map underperforms a pre-registered benchmark net of stressed carry across two pre-registered cycle boundaries, with a multiple-comparisons correction across map entries | Benchmark and boundaries to be registered | PENDING |
| F9 | On re-placed episodes, manias and collapses do not sit at `Λ ≤ 0`, or shortages do not sit at `Λ → 0⁺` (H-Λ, §6.3) | Measured `η` per episode | PENDING on §13.1 |
| F10 | Leg-coupling indicators are empirically independent in the high-flexibility corner | Four-indicator panel | PENDING on §13.5 |
| F11 | Elasticity estimates move smoothly, with no clustering at event dates | Event calendar; repeated `η` estimates | PENDING |
| F12 | Per-layer scoring changes no classification relative to per-good scoring on a measured case | Measured `η_s` per layer for one market | PENDING on §13.1 |

**Retired:** the v0.6.2 criterion that a K2 exit must not occur without a live quantity condition (true by construction under the old indicator); "P0 → P2 without IV expansion" (impossible by the definition of P2; replaced by F6); the collapse-claim test as "decided" (replaced by F9); the D2 sign-flip as "decided" (replaced by F12).

## 12. Known gaps

1. **Nothing is measured.** Every `η`, threshold, band edge and hazard parameter is first-pass or absent.
2. **The index needs estimates it does not have.** A valid `η` requires a price–quantity response at a stated horizon. None exists for any leg.
3. **The hazard model is a form** (§5.7).
4. **The K screen has not been run** on any pool, live or historical.
5. **Headroom is defined (§5.5) but not reconciled** across ISOs/RTOs.
6. **No cost data is loaded.** The cost-slope proxy, the W split weights and the generation-versus-delivered cost spread all wait on it.
7. **The position map covers 9 of 60 states** and names no instruments.
8. **P has no downside levels.**
9. **No hazard for the opening of an event window** (§4.2).
10. **`D_stress` and `ν` have no method.** The loss side of the rule is specified in form only.
11. **Demand forecasts are contested** and the model has no way to weight the disagreement.
12. **The gold question.** Gold is about 26% below its January 2026 high. v0.6.2 framed this as a puzzle for a debasement reading. The conventional account in market coverage — rate-hike expectations and a stronger dollar — has not been weighed against it. It gates any hard-asset illustration.
13. **Layer assignments are judgement**, and L2a and L4 are unassigned.
14. **A lesson retained.** An early check produced `r = −1.000` between two columns computed from the same inputs. Tests must use independently derived quantities. The same discipline now applies to any test run on values the authors placed by hand.

## 13. Next steps

Ordered by what unblocks the most.

1. **Estimate one real `η` at L1.** Method candidate: the renewal-margin estimate — paired observations of re-contracting prices and renew / expand / walk outcomes. Unblocks F9, F12, §8.2.
2. **Build the event calendar**: dated events in the four classes of §5.3. Unblocks F1, F2, F11.
3. **Pre-register and commit** `p`, `N`, `ρ`, kernel half-lives, `m`, `q`, `k`, and the K-screen thresholds, dated, before touching any sample.
4. **Run the K screen** on the AI-infrastructure pool and the five currency pools; publish inputs and resulting statuses. The financing-quality statistic (Mercatus plus credit-spread data) may be assembled as corroboration.
5. **Assemble the four-indicator panel** for the coupling factor. This replaces v0.6.2's plan to regress one elasticity on the other.
6. **Fit `g` for the currency case** on dated devaluation episodes.
7. **Document every Γ component and `g_usd`** with source and window.
8. **Load cost data**: LCOE by technology, interconnection cost per MW by ISO, transformer pricing.
9. **Re-place the legacy episodes** under §2.1, or retire them.
10. **Build the simulator** per §14, after steps 1–3.

## 14. Simulator specification

**Principle:** the simulator must not teach the collapse, and must not present unmeasured values as measured.

**v1 — the pair, per leg.**
- Inputs: `ε_d`, `ε_s` for the resource leg and the capital leg, each on `(−1, +1)`; the real `η` shown alongside via §2.2.
- **User-set, not derived:** `M`; `P` (with "unclassified" as an option); **`K` and its status**. v0.6.2 asked the tool to derive K from the sliders, which §3.1 rules out.
- Display: one plane per leg in `(ε_d, ε_s)` space. The anti-diagonal `ε_d + ε_s = 0` is drawn as the stability boundary, with contours of `Λ` (or `μ`) as the primary background. The diagonal marks `Δ = 0`. The negative-`Λ` region is shaded as self-reinforcing.
- Printed readouts: `Δ`, `Λ`, `μ`, the classified `S` level, the §6.3 corner name, and the §6.1 map entry **if one exists**; otherwise "no position defined".
- No single `(Δ_R, Δ_C)` plane as a primary view. If shown, it carries a persistent label: "summary — level not shown."
- Every marker shows its provenance: `measured`, `proxy`, `UNPLACED`, or `legacy (void)`.
- Stack: plain HTML/CSS/JS, D3 for plane backgrounds and drag. No backend. `episodes.json` for seed data.

**v2 — decision overlay.** `Γ`, `G`, `D`, `λ`, `ν` as user inputs, labelled *user-assumed*; plot `λG − νD + Γ` against `m` and the §4.3 size bound.

**v2.5 — trajectories.** Checkpoints over time with step changes at event dates. No smooth interpolation between checkpoints.

**Per-layer view.** One plane set per layer within a market, since the map is keyed per layer.

**`episodes.json` schema:** name, `M`, layer, date range, `(ε_d, ε_s)` per leg, **scale version**, **provenance**, the §2.1 record, `Γ` components with sources, validity flag. Legacy rows load as `legacy (void)` and render distinctly.

## 15. Change log from v0.6.2

| Audit finding | Change in v0.7 |
|---|---|
| C1 withdrawn AI reading still printed | §8.2 withdraws the values; §8.4 withdraws the demonstration; no `Δ`/`Λ` printed for the market |
| C2 index undefined for demand; no mapping | §2.1 per-leg definitions (D4); §2.2 transform with unit elasticity at `+0.5`; horizon in every record |
| C3 `Δ` read as excess demand; shortage contradiction | §2.3 interpretations; §6.3 retires the twelve-state vocabulary; shortage fixed at `Λ → 0⁺` |
| C4 K2 deduction untestable | §3.1 K2-observed status (D5); §5.2 three exit channels and empirical H-Q (D7); indicator removed |
| C5 options guidance wrong | §6.1 names exposures only; §6.2 states the payoff constraints; §9 withdraws the put conclusion |
| C6 no loss state | §4.2 three-outcome rule; §4.3 `D_stress` in sizing; "zero ruin" withdrawn |
| C7 §8.2 identity | §10.2 affine relation, cross-section versus time, `g_usd` flagged |
| C8 "DECIDED" falsifiers | §11 resets both; F9 and F12 replace them |
| M1 carry mixed with drift | §4.1 (D6) |
| M2 K classifier | §3.1 pool-level screen; §10.1 statuses set to unscreened; US "K1 economy" claim removed |
| M3 hazard model | §5.1 general form; §5.4 survival-weighted mixture; §5.5 headroom (D8); §5.7 inventory; `ρ` moved to a test threshold |
| M4 layers and S | §8.1 splits L2, declares omissions; §3.2 S2 defined by band; proxies labelled |
| M5 position map | §6.1 coverage stated, conditional note, instruments required |
| M6 silver | §9 P unclassified; supply layered |
| M7 macro section | Removed from the specification. Verified facts retained only where used (§10.1 `π_us`; §12.12) |
| M8 other falsifiers | §11 retirements; F6 restated as a lead test |
| M9 currency cluster | §10.1 inference withdrawn; §10.3 hazard form; §10.4 expression withdrawn; `e` defined |
| E1–E3 header, anchors, counts | New header; anchors on the six proposals; §0 restated |
| E4 ordinal versus categorical | §3.1: K categorical; S and P ordinal |
| E5–E8 dangling and misplaced text | Removed with the design notes |
| E9–E10 state counts | Vocabulary retired |
| E11 withdrawn rule printed first | §4.3 prints one rule |
| E12 episode commentary | §7 table without commentary; legacy carry dropped |
| E13 coupling plan | §5.6 and §13.5 aligned on the factor model |
| E14 provenance arithmetic | Not carried forward; see §16 |
| E15 symbol reuse | §1 |
| E16 unresolvable references | Review-thread references removed; predecessor names kept in §16 |

**Proposals needing ratification:** D4 (§2.1), D5 (§3.1), D6 (§4.1), D7 (§5.2), D8 (§5.5), H-Λ (§6.3).

**Open questions carried forward:** does the long on a constrained layer survive a K2 exit (§6.1 note); downside levels for P (§12.8); a hazard for window opening (§12.9); a method for `ν` and `D_stress` (§12.10); which coupling indicator is measured first and on what data (§13.5); whether the legacy episodes are re-placed or retired (§13.9).

## 16. Provenance

Predecessors: the Ecology matrix; the silver four-state model; the currency "coiled spring" ranking; `Resource/Capital Elasticity Differential Model` (RCED); `Elasticity Gap Model for AI Markets` (EGM). Earlier versions of this document: v0.3, v0.4 (fifteen-anchor review), v0.5 (consolidation and defect register), v0.6, v0.6.1, v0.6.2. Their full derivation history is in the board's git history under `shared/unified-state-model-*`.

v0.7-candidate was drafted from v0.6.2 and the external audit of 2026-11-10. It has not been through board review.

---

*Sources carried forward from v0.6.2, not independently verified unless marked: `notion-ecology-2026-10-31.md`; `Mercatus_GPU_ROI_Summary.md` (break-even WACC ~11%, H100 rental +6.1%/90d); Trading Economics FX and CPI series (Oct 2026); CBN NFEM rates; SGE premium tracking; Argentina BCRA/blue/MEP/CCL spreads (Oct 2026); ICF US electricity demand outlook; Grid Strategies National Load Growth Report.*

*Verified in the audit: BLS Consumer Price Index, September 2026 (all items 3.7%); World Gold Council Gold Mid-Year Outlook 2026 and press reports (gold high near $5,595 on 2026-01-29, dip below $4,000 in late June); press reports of spot silver at $121.64 on 2026-01-29; Trading Economics, 2026-10-29 (silver at a 48-week low, −12.89% over four weeks).*

*This document is a modelling specification. It is not investment advice.*
