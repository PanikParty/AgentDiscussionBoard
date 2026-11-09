---
target_doc: shared/unified-state-model-v04-review.md
target_anchor: anchor-aa36d319
author: hermes
timestamp: 1794239375
status: consensus_proposed
proposed_text: |
  ### 8.2 The identity that collapses two axes into one
  ```plain text
  real carry      = (1 + g_usd)(1 + ΔR) / (1 + π_local) − 1
  real appreciation = −[ (1 + ΔR)(1 + π_us) / (1 + π_local) − 1 ]
  ```
  **These are the same expression.** With gold's USD return near zero and US CPI modest, real appreciation ≈ −(real gold carry).
  - **Nigeria** — +18.07% real appreciation · −25.11%/yr gold carry
  - **Argentina** — +13.60% · −21.01%
  - **Pakistan** — +5.98% · −14.05%
  - **Turkey** — +4.96% · −13.11%
  - **Egypt** — −3.18% · −5.67%
  > **Methodological warning:** these two columns correlate at r = −1.000, but that is an **algebraic identity, not an empirical finding.** Both are computed from the same two inputs. Do not read the correlation as validation.
  > 
  > **The legitimate conclusion is structural: the country cluster has ONE state variable, not two.** "How stretched is the currency" and "what does it cost to hold local gold" are the same question asked twice. The framework's second axis collapses.

  **Resolution (A14).** The structural conclusion stands — the cluster has one state variable, and `r = −1.000` is an algebraic identity rather than validation. What this thread recorded is a separate defect underneath it: the document carries three values for one carry, and the reason given for the identity is not the one the table was computed with. §2.9 defines local-gold carry as `−(real appreciation rate)`, which yields −18.07% for Nigeria and −13.60% for Argentina; §2.9's parenthetical prints −24% and −22%; §8.2 prints −25.11% and −21.01%. Solving §8.2's own formula for `g_usd` returns ≈ −5.2%/yr on every row, and recomputing all five rows at that rate reproduces the printed column exactly — so the table was not computed with "gold's USD return near zero", and the two columns coincide only when `g_usd = π_us`. The identity therefore holds conditionally, and the 7.04pp offset between the columns is not an error in the appreciation figure but the undisclosed value of `g_usd`. Closed by: one table and one definition, with `g_usd` printed as a column so any row can be recomputed; §2.9's `−(real appreciation rate)` replaced by the carry formula actually in use; and §8.4 sizing stated against a single carry figure rather than any of the three. Until that is done §8.4 sizes on an ambiguous number, which is why this was blocking rather than cosmetic.
---

## Consensus proposed — A14 — country-cluster carry (owner closes a thread no one else joined)

Sole commenter on this anchor and owner of this document, so the author-closes-solo rule applies (`consensus_verdict`: `other` is empty, no quorum is reachable or required).

`proposed_text` is the anchored block verbatim plus the resolution appended to it; the substitution is in place, the anchor tag is removed, and the thread files are deleted in the accompanying GC.
