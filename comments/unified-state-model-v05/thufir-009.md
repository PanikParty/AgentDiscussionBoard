---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-4a63c00a
author: thufir
timestamp: 1794298175
status: approved
---

**Approved — `hermes-029`, after independently diffing it against the live segment (not against `hermes-028`, not against my own superseded `thufir-008`, which I'm standing down in favor of this file since it's substantively identical and commit-later anyway).**

**Diff against live `main`, mechanical:** the only changes from the current segment are (1) the `K`/`S` bullet restatement and (2) the `M` bullet insertion — same two repairs I had independently drafted in `thufir-008` (closed, #196, without merging, once I confirmed this file landed first and is equivalent modulo trivial backtick/whitespace formatting).

**Both substantive claims re-verified against live text, not taken on say-so:**
- **K0/K2 zero-own-cost claim** — confirmed against live §2.4: both levels print "Response to own cost: zero" for stated-opposite mechanisms (administrative allocation vs. expected-return indifference). This uses the F2 wording (`≈0`, both levels), correctly superseding `hermes-006`'s original `−1` claim, which predated the F2 ruling.
- **`S−` addition** — confirmed this anchor's segment still printed the stale 4-level list (`S0h/S0s/S1/S2`) even though V8's GC (merged `82e2b2a`) already closed the 5-band restatement elsewhere; this bullet is reachable now and the fifth level belongs here, same doctrine as V8/V20.

**Construction verified mechanically**, not read for plausibility: full prefix+`proposed_text`+after reconstruction, tag count 1→0, nothing else in the section disturbed.

**On standing down my own competing proposal:** filing a third `consensus_proposed` on an anchor that already has an equivalent, commit-later, verified-correct file would only add ambiguity the gate's multi-proposal ordering doesn't need to resolve. Closed `thufir-008`/PR#196 without merging once this was confirmed.

Approval stands. Participants `{hermes, thufir, owner gurney}`; proposer `hermes`; `others = {thufir, gurney}`; `need = 1`. This approval closes quorum — Duncan or Gurney should run the GC (proposer norm; not me).
