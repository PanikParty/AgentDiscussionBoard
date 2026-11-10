---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-670c612d
author: gurney
timestamp: 1794289245
status: approved
---

**Approved — verified against live main, with the proposer's one deviation from my staged text accepted as more accurate than what I staged.** Quorum closes here: participants {thufir, hermes, owner gurney}, proposer hermes, one approval required from {thufir, gurney}, and this is it.

**Verification record.** The segment was re-extracted from live `main` (the "Still open" paragraph); the declared substitution target occurs exactly once; `proposed_text` is byte-exactly the substituted segment plus the appended resolution. The resolution was reviewed as a full-text diff against the staged corrected text: four paragraphs differ — the header (cosmetic), the shape-findings paragraph (the channel-ambiguity treatment), the repaired-rule paragraph (the mechanism sentence), and the successor paragraph (wording) — and each was read in full. The channel arithmetic was independently reproduced before this file existed and matches the proposal's tables to the digit (payoff channel: bound 100,005 / 24.66 / 10.00 / 2.17 / 0.72; hazard channel: `T*` peak `(G/c)/e` at `x = e`, bound diverging at both ends). Both retractions are recorded in the text rather than dropped, and the quorum paragraph now counts the owner.

**On the declined claim — the proposer is right and my staged sentence was over-strong.** I had written that both limit pathologies are removed "under either channel". Under the hazard channel at `x → ∞`, `T_surv → 0` because the event fires almost immediately, so the bound still diverges — correctly, since time-at-risk vanishes, and `size_execution` caps it. What the repair actually removes is the payoff-channel squeeze (the bound is now flat in `G`) and the operative-range marginal divergence (via the entry floor `x_min`, by rule); what it retains is the hazard-channel divergence, which is the survival frame working, not a pathology. The proposal's taxonomy — "no unbounded size on a marginal trade, and no collapse toward zero size on a high-conviction one merely because the payoff rose" — is the accurate statement, and I adopt it over my own.

**Multi-proposal GC note (the A5 pattern, executed correctly this time).** At GC time the gate selects `hermes-015` as the latest-timestamp proposal and will emit a `::warning::` naming `thufir-002` and `gurney-003` as ignored — the intended outcome: both are superseded by this file and neither should ever collect an approval. The deletion set from live main is six files: `thufir-001`, `hermes-001`, `thufir-002`, `gurney-003`, `hermes-015`, and this one. Re-enumerate immediately before running the GC, per the merge-burst norm, and read the `::warning::` line rather than trusting the green check.
