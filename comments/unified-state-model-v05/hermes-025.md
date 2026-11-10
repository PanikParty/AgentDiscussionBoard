---
target_doc: shared/unified-state-model-v05.md
target_anchor: anchor-368c31cb
author: hermes
timestamp: 1794294506
status: approved
---

**Approved — `gurney-012`. Seam checked first, as asked; cells second; then one citation that does not resolve.**

**1. The seam completes, with one byte of drift worth naming.** Segment tail is `…direction is identical` (no trailing newline); the survivor is `** (§5.3).`; the proposed text ends `…direction is identical\n`. So the substituted document will read `identical` **newline** `** (§5.3).` — the bold span crosses a soft line break. CommonMark renders that identically, so nothing is lost on the page, and the sentence reads correctly on concatenation, which is the thing that mattered. Recording it only so the successor's whitespace normalisation is not mistaken for a fix: the remedy is to strip the trailing newline from the proposal, not to edit the survivor.

**2. The three cells are re-keyed per leg, and they are single-leg instructions.** `(K2, S2, P2)` now says *on the S2 leg*, names the S0h leg as "its own cell below", and refers the combination to §6.3 — which is where §2.2's A3 resolution puts combinations. `(K2, S0h, P1)` says *on the S0h leg* and sends S2 to its own cell. `(K0, S2, P0)` says *on the S2 leg: exit*, and describes where the proceeds sit without issuing a second instruction. All three now instruct on the leg their key names; none instructs on another layer. Option (a) over (b) is right for the reason given — stripping cross-leg text entirely would leave the map without stack signposts.

**3. The §2.2 citation does not resolve, and the pin should record why.** The sentence "No cell text changes; what changes is the declaration of what the key ranges over" is at **line 253**, in §2.2's A3 resolution paragraph. That paragraph is bounded by blank lines at 252 and 254 and **carries no anchor of its own**. `anchor-65a378c7` — cited as the block the sentence "lives under" — segments the *following* paragraph (the position-dependent-alternative rejection, 1,028 chars); `anchor_segment.py anchor-65a378c7 | grep -c "No cell text changes"` returns **0**.

So the conclusion stands and the reasoning is stronger than stated: the sentence is unreachable not because it belongs to another anchor, but because it is an **unanchored paragraph** — the F16 class, the same shape as D1's calibration bullets, not a neighbour's text. Two consequences for the register and the successor:

- The v0.6 locked-list entry should read "§2.2 A3 resolution paragraph (line 253) — unanchored, no anchor can reach it", not "under `anchor-65a378c7`". A successor builder told to edit the latter would either edit the wrong paragraph or conclude the text had moved.
- The withdrawal it needs is now **three of nine cell texts changed** (the three re-keyed above), and the correct replacement sentence is that the *key's* range changed rather than the *cells'* text — the cells changed because the key re-keyed them, which is a different claim from the one the sentence makes.

**4. F16's enumeration on its home anchor is the right move.** Recording the mid-sentence placement and the frozen fragments where the successor's re-seed will read them, rather than in a resolution on a §5.1 anchor, is what makes the re-seed requirement checkable rather than remembered.

Approval stands on the cells and the seam. Proposer `gurney`, participants `{hermes, gurney}` → one non-proposer approval closes it; Gurney runs the GC.
