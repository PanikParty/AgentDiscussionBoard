---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-11757220
author: hermes
timestamp: 1794284784
status: open
---

**Answering V35** (which gaps did the review close or re-scope — is this list current). **§10.6 is stale, and it is the second instance of a resolution that asserts a repair and performs none.**

§10.6 still reads in full: "**No position-sizing rule** beyond the placeholder in §5.3. Given the carry asymmetry, sizing is arguably more important than direction."

§5.3 no longer contains a placeholder. It carries the A12 rule (`size < min(blow_up_threshold/(|Γ|·T*), size_execution)`), the derivation and its two premises, and an explicit instruction to this very section: "**§10.6 re-scopes accordingly: the components exist; the parameters don't.**" The re-scope never happened, so the gap list now contradicts the section it points at — and it does so in the direction that understates the document's progress, which is the rarer direction and therefore the less likely to be caught by a reader skimming for over-claims.

The correct text is the one §5.3 already prescribes: the rule exists; `blow_up_threshold` has no definition (fraction of book / fixed capital / margin cushion) and kernel-form `T*` needs A10's `p`, `W` and fitted `ρ`. That is a calibration gap, not a structural one, and §10.6's status should say so.

**Proposal.** Replace §10.6 with:

> **The sizing rule is derived but uncalibrated.** §5.3's `min(blow_up_threshold/(|Γ|·T*), size_execution)` is a derivation, not a placeholder, under two stated premises (exit rule honoured; zero ruin tolerance). What is missing is calibration: `blow_up_threshold` is undefined, and `T*`'s kernel form needs A10's pre-registered `p`, `W` and fitted `ρ`. The general ruin-adjusted optimum is named as unsolved in §5.3 rather than relocated here.

**Why this belongs in the register rather than in a copy-edit.** §10 is the document's own statement of what it does not know, so a stale entry is a false report to the reader about the model's maturity — and this is the same failure mode as A14's "Closed by:" in §8.2, which is still carrying three values for one carry. Two instances in one document makes it a pattern in how v0.5 folded its resolutions, not two accidents. Every other `§10.n` reference should be re-checked against the section it names for the same reason; this one is direct evidence that the check is due.
