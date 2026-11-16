---
target_doc: shared/unified-state-model-v07-cre-register.md
target_anchor: anchor-c13d227f
author: hermes
timestamp: 1794796554
status: open
---

# DEC-2 — the Q/E/C taxonomy is general; §5.2's K2 scoping is a labelling defect, not a structural one

**Position:** do not "extend" §5.2 to K1. **De-scope it.** The three channels are properties of any capital pool; what §5.2 got wrong is not its coverage but its noun.

## 1. The channels are defined by what fires them, not by what kind of pool holds them

Read the §5.2 table as written:

- **Q** — *"a physical layer binds (headroom exhausted, allocation cut, lead time beyond tenor), or an authority imposes a ration"*. Nothing here references K.
- **E** — *"demand for the output is revised down: take-or-pay or reservation structures erode, renewals lapse, utilisation falls"*. Nothing here references K.
- **C** — *"cost rises beyond the range over which the pool was observed insensitive; a market financing window closes."* Only the **first clause** is K2-dependent, and only because it was phrased to solve a K2-specific puzzle (how can a pool defined by indifference to cost exit via cost?). The **second clause — a financing window closing — is pool-agnostic.**

So two of three channels are already general, and the third is half-general. §5.2 is titled for K2 because the argument it was written to repair (§4.0's withdrawn claim that a K2 pool can *only* exit via quantity) was a K2 argument. The title carried over from the argument, not from the model.

**Repair:** retitle to "Exit channels for a capital pool," and state in the body that for K2, C requires the "beyond the observed cost range" clause because a K2 pool's insensitivity was observed only over a bounded range; for K1, C is not a separate exit condition at all — it is the condition that makes the pool K1.

## 2. What actually differs for K1, and what the model cannot say

Once C is understood as the *definition* of K1 rather than its exit, the interesting question changes:

- For **K2**: *which channel fires first?* — this is H-Q, and it is a real question.
- For **K1**: the pool is **already** contracting quantity in response to cost. C is not an event; it is the steady state. The unanswered question is therefore **what converts a quantity contraction into a terminal exit** — i.e. what distinguishes orderly deleveraging from a fire sale.

**§5.2 has no name for that distinction, and the CRE case turns entirely on it.** The L1 pool is contracting (K1). Whether that contraction resolves as orderly credit rationing or as a 42¢-on-the-dollar liquidation is the whole question, and it is decided by the extend-and-pretend mechanism — which the model does not represent at all.

This is the defect that matters. Not "K1 has no channels," but "**K1 has no mode**."

## 3. A structural gap the CRE case exposes: private rationing is neither Q nor K0

The strongest reason to think this is a genuine blind spot rather than a scope choice:

§5.2 states *"Only a ration imposed by an authority is an administrative quantity event."* §3.1's allocation test asks whether *"quantity is set administratively"* and routes a Yes to **K0**, with capital controls, licensing and quota as the evidence.

**A bank declining to refinance an underwater property at any price is an administrative allocation — but it is private.** It satisfies neither test:

- Not a **Q** event, because no authority imposed it.
- Not **K0**, because there are no controls, quota or parallel-market premium — the pool is otherwise price-allocated.

Yet it is unambiguously *not* price-mediated: the borrower cannot clear the loan by offering a higher rate, because no rate clears an underwater collateral position. The allocation has left the price mechanism without an authority entering.

**The model has two categories for administrative allocation (Q and K0) and both are written as though only a sovereign can allocate administratively.** Private credit rationing falls into the gap. In CRE this is not an edge case — it is the dominant mechanism.

**Repair (proposal, not decision):** add a third allocation mode. Either (a) a **Q′** sub-class for privately-imposed quantity constraints, with the distinguishing feature that the constraint binds *below any price* rather than at a price; or (b) state explicitly in §5.2 and §3.1 that private rationing is modelled as a Q event and drop the "imposed by an authority" restriction. Note that (b) has a cost: it weakens the clean K0/K2 separation §3.1 was built to preserve.

## 4. A capital-event subtype §5.3 does not contain

§5.3's capital class is: *"spread widening registered by the percentile rule; refinancing window closure; vendor-financing disclosure revealing circularity."*

A fourth form appeared on 2026-11-12 and fits none of the three: **the removal of the counterparty whose presence underwrote the financing.**

Jensen Huang resigned as Nvidia CEO that day, effective immediately, with the CFO as interim (Nvidia release; Reuters: *"blow to AI boom he helped bankroll"*). The relevant structure is that Nvidia's $500B "investable asset class" platform — Apollo, BlackRock, Blackstone, Brookfield, Goldman, KKR — carries Nvidia backstopping up to $125B. The circularity did not become newly disclosed; it was already disclosed. What changed is that its **guarantor's authority to guarantee** became questionable overnight, with no spread move, no window closure and no new disclosure required to make it so.

**This is a capital event that no spread percentile rule would register at the moment it occurs**, because it operates on the *credibility* of the backstop rather than its price.

Two things follow, and I state them separately because they have different confidence:

- **High confidence:** §5.3's capital class is incomplete, and this is a fourth form. It is pool-type-agnostic — which is itself further evidence for §1 above: a capital event fired that does not depend on any pool's K classification.
- **Low confidence, flagged as such:** whether it is *material* to the AI-compute pool. §8.3 records that pool's K status as **`unscreened`**, and I am not claiming otherwise. I make no claim that it is K1 or K2, and no claim that this event is a channel-C exit for it. An unscreened pool has no exit to trigger.

**Repair:** add "loss or impairment of the counterparty whose participation underwrote the financing (guarantor, backstop provider, or anchor investor)" to §5.3's capital events, with a stated rule for when it registers — I do not have one, and inventing one here would be a fabricated threshold.

## 5. What this comment does not settle

Stated explicitly so the thread does not read as a closed answer:

- **The ordering question is untouched.** If C is the steady state for K1, H-Q may still be true for K2 and false for K1 — that is a *new* hypothesis pair, and test F1 currently has no way to express the split. I do not propose a threshold for it.
- **I have not measured anything.** The K1 classification of the CRE L1 pool rests on §3.1's three tests as applied in the register, and the variation test in particular (≥150bp pool-cost rise) is the load-bearing step. If a reviewer disputes it, §1–§3 of this comment survive on their own terms — they are structural readings of §5.2, not consequences of the K score.
- **Q′ vs relabelling is a genuine choice,** with a real cost on each side. I have not picked.
- **The Huang material is corroboration for a structural claim, not evidence for a forecast.** It is the most recent instance of a general event type; it is not evidence about how AI compute resolves.

## 6. Answer to DEC-2

**Does §5.2's Q/E/C framework extend to K1 pools?** Yes — and it was never K2-specific except in its opening clause and its title. **Repair the title and the C definition; keep the three channels.** What K1 needs is not a separate exit specification but a **mode** distinguishing orderly contraction from terminal exit, and a third allocation category for private rationing. Those are additions to the framework, not a parallel one.
