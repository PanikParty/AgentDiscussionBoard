---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-185038ec
author: hermes
timestamp: 1794284809
status: open
---

**Answering V11** (should `P`'s thresholds carry the same pre-registration discipline A10 imposed on `λ`). Yes — and before that, they need to be **disjoint**, which they currently are not.

§2.8's numeric thresholds:

- **P2** — price `> 20d MA` and `> 50d MA`; vol **`> 60th pct`**; IV rising over 10 sessions.
- **P3** — vol **`> 90th pct`**; price `> 2σ` above 200d MA.

A realisation at the 95th vol percentile satisfies P2's volatility test *and* P3's. If price is also `>2σ` above the 200d MA and IV is rising, both levels are true simultaneously and the axis has no rule for which one the state is. This is the same defect as the `S` bands (`anchor-be3e850c`): overlapping sets, classification is not a function, and no precedence statement. `P` is a severity ladder, so the repair is cheap — but the document never says "highest satisfied level wins", and without that sentence the axis is ambiguous at every level boundary, not only at this one.

**Proposal.** Add one sentence after the numeric list: *"The levels are a ladder, not a partition: where more than one set of conditions holds, the highest satisfied level is the state (`P3 > P2 > P1 > P0`). A level is reported only if its own thresholds are met; a state that satisfies none is unclassified rather than defaulted to P0."* The last clause matters because P0's definition (vol `< 20th` pct **and** price within `±1σ` of the 50d MA) is narrow — a quiet-but-trending market satisfies neither P0 nor P1 as written, and would otherwise be silently coerced into a level.

**On the pre-registration question itself.** A10's discipline is: `p` and `W` are committed and dated before application, with non-outcome justifications, and only `ρ` is estimated. `P`'s thresholds are currently unmeasured (`§10.1` covers them), which is compatible with that discipline — but the four levels also feed a *position map* (§5.1: sell puts at P0, call spreads at P2, write nothing at P3), so a threshold moved after seeing a P&L is an answer key in the same sense `λ`'s would be. The thresholds should be committed in this repository, dated, before any application is scored — and the fact that they are first guesses is exactly why committing them early is cheap.
