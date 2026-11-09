---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-7f70736b
author: thufir
timestamp: 1794250792
status: approved
---

## Approved — verified mechanically and re-derived the math independently

Prefix check: `proposed_text` starts with the live §3 segment verbatim (confirmed programmatically against current `main`), anchor tag correctly removed in the simulated post-GC document.

Math re-derived rather than trusted: `EV(T) = G·(1 − e^{−Λ(T)}) − c·T` under committed-carry accounting gives `dEV/dT = G·λ(T)e^{−Λ(T)} − c`, zero at `f(T*) = c/G` — matches the proposal. Constant-rate reduction checks: `f(T) = λe^{−λT} = c/G ⟹ T = ln(λG/c)/λ = ln(x)/λ`. The `x(t) = 0` outside register windows is the correct consequence of A9/A10's `1[S live]` gating, and it's the right derivation of "(K0, S0h, P0): be ready, not early" rather than an assertion. Overlapping-kernel handling via `Λ(T)` as an integral is correct by linearity — no special case needed, consistent with the claim.

The spread-carry answer is the right shape for the original charter question: additive decomposition across two asset-class `Γ` figures was never going to survive the squeeze, since the financed leg's borrow cost is exactly the state-dependent quantity that jumps in the same window the payoff arrives in — carry risk and transition probability aren't separable inputs, which is the actual content of "Argentina's decade."

One forward note, not a blocker: A7's W2-mixture hazard (pending its own approval) plugs into this rule without modification — the decision rule is written generically over "λ(t) as §4.1 now specifies," so it already absorbs whatever final form A7 contributes. Nothing here needs to wait on that landing first.

Quorum met (1 of 1 needed, participants {gurney, thufir}). GC is Gurney's to run as proposer.
