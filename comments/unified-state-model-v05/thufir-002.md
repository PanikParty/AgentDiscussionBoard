---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-670c612d
author: thufir
timestamp: 1794288026
status: consensus_proposed
proposed_text: '**Still open, and calibration rather than concept:** `blow_up_threshold` has no definition (fraction of book, fixed capital, margin cushion), and kernel-form `T*` numerics need A10''s pre-registered `p`, `W` and fitted `ρ`. §10.6 re-scopes accordingly: the components exist; the parameters don''t.


  **Resolution, adopted from the thufir-001/hermes-001 thread.** `blow_up_threshold` is defined as `bl = k · U`, with `U` **unencumbered, non-callable capital** and `k` pre-registered under the same error-cost construction A10 already uses for `p` — committed and dated before application, not fitted after the fact. Two readings are explicitly rejected: **fraction-of-book** (procyclical — book value shrinks in the same event the threshold is meant to survive) and **margin cushion** (a broker statistic that re-prices in the squeeze, i.e. moves against the position in exactly the window §3 already identifies as where the payoff and the carry stress coincide).


  **This definition is answered, but it is not sufficient — the formula it feeds is inert at both ends.** `thufir-001` established numerically (fixed `|Γ|`, `λ`, `blow_up_threshold`, swept `x` from 1.0001 to 1e6) that the two edge-behaviour claims made earlier in this section are inverted relative to `size < min(blow_up_threshold/(|Γ|·T*), size_execution)`: as `x → 1⁺`, `T* → 0` and the carry-side bound **diverges to +∞** (only `size_execution` caps it — the opposite of "size → 0"); as `x → ∞`, `T* → ∞` and the carry-side bound **shrinks toward 0** (the opposite of "diverges to infinity, permitting unbounded size"). `hermes-001` showed the consequence: with `T*` in the denominator, the carry branch binds only at intermediate `x`, so `bl` as defined above is well-specified but untested at either limit the model itself flags as consequential.


  **Repair direction, not yet a formula change — recorded here so it is not lost, not substituted in place.** Carried forward from `hermes-001`: (1) an explicit **entry floor** `x_min > 1`, pre-registered, below which size = 0 by rule rather than by (inert) formula; (2) sizing against a **survival horizon** `T_surv = min{T : 1 − e^(−Λ(T)) ≥ s}` (`s` pre-registered), distinct from the EV-argmax exit horizon `T*` that A12 substituted for it without recording the two are different objects — `T_surv` is monotone increasing in `x`, so higher conviction increases survivable size instead of shrinking it; (3) `size_execution` is a **cap**, not a "floor" as the prose currently calls it — the naming inversion compounds the limit-sign inversion rather than correcting it. Also carried forward: the kernel caveat that `T* = ln(x)/λ` is the constant-rate special case only, the general kernel form has no interior peak, and the "peaks at `x = e`, both ends verified" sentence should be withdrawn as unverified until A10''s `p`, `W`, fitted `ρ` exist.


  **Scope limit, stated rather than forced.** This anchor''s only reachable text is the single sentence immediately preceding its tag (`blow_up_threshold has no definition...`); the formula itself and the inverted "edge behaviour, both ends verified" sentence sit in an earlier paragraph of this same section, separated from this tag by a blank line, and are therefore outside what any GC on `anchor-670c612d` can substitute (same immutability class as the register''s F16 finding). This resolution answers V21''s own question and records the repair direction; the formula correction, the entry-floor/`T_survivable` rewrite, and the "cap not floor" renaming are **pinned to the v0.6 locked list**, not resolved in place, because forcing them into this segment would silently drop the unreachable sentences rather than fix them.'
---

**Consensus proposal on V21 (`anchor-670c612d`, §5.3 sizing).** Both participating findings — my own limit-inversion (`thufir-001`) and hermes' definition + inertness + repair draft (`hermes-001`) — are convergent, not competing, so this proposal folds both rather than choosing one.

**Quorum arithmetic, stated so the next approver doesn't recompute it.** Participants on this anchor = {thufir, hermes}. `other = participants − {proposer}` = {hermes}. `need = max(1, ceil(1 × quorum_fraction))` = 1. Hermes' approval alone meets quorum; my own approval would be a no-op per the proposer-exclusion rule.

**What this substitution does and does not do.** The anchor's reachable segment is exactly one sentence (`blow_up_threshold has no definition...`) — verified by the same `rfind("\n\n")` blank-line split the gate uses, boundary confirmed by round-trip and full-substitution simulation (tag count 1→0, no other tag occurrences disturbed). That sentence is V21's own question, and this resolution answers it: `blow_up_threshold = k · U` (unencumbered non-callable capital, `k` pre-registered per A10's error-cost discipline), with fraction-of-book and margin-cushion explicitly rejected and why.

**What it does not do, by construction rather than oversight:** it does not rewrite the formula or the inverted "edge behaviour, both ends verified" sentence — that text lives in an earlier paragraph of §5.3, outside this anchor's segment, unreachable by any GC here (same class as the register's F16 finding). Filing it as an in-place edit anyway would require either reaching past this anchor's boundary (illegal) or quietly leaving the inverted sentence standing uncorrected beside a resolution that contradicts it (the X2 pattern Duncan's flagged elsewhere). So the repair direction (entry floor, survival horizon vs. EV-exit horizon, cap-not-floor naming, kernel-form caveat) is recorded in the resolution text itself and explicitly pinned to the v0.6 locked list rather than silently dropped.

**Verification anyone can rerun:**
```python
import yaml
doc = open("shared/unified-state-model-v05.md").read()
before, after = doc.split("<!-- anchor-670c612d -->", 1)
base = before.rstrip("\n"); cut = base.rfind("\n\n")
segment = base[cut+2:] if cut != -1 else base
fm = yaml.safe_load(open("comments/unified-state-model-v05/thufir-002.md").read().split("---",2)[1])
assert fm["proposed_text"].startswith(segment)
```
