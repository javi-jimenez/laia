---
title: "Arteries of the Earth: Chokepoints, Trade Circulation and Why Blocking Them Is Self-Harming"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-10-23
version: "1.0"
status: "Draft"
tags: ["trade routes", "chokepoints", "Silk Road", "maritime logistics", "Hormuz", "systemic risk", "NEPTUNO"]
keywords: ["chokepoint", "trade artery", "maritime traffic", "Strait of Hormuz", "Suez", "circulation model", "blockade cost", "Silk Road 2.0"]
license: "CC BY-NC-SA 4.0"
---

# Arteries of the Earth: Chokepoints, Trade Circulation and Why Blocking Them Is Self-Harming

> **Status: a theory with a model and a worked case.** The proposition is that the world trading system behaves
> like a circulatory system: flow concentrates in a small number of narrow vessels, the health of the whole
> depends on those vessels staying open, and a blockage damages the party that causes it as well as the party
> it targets. The model below formalises the first two parts. The third — that blocking is *self*-harming — is
> argued from the model and illustrated with one case, and it is stated as a claim under test rather than as a
> demonstrated law.

## Abstract

Global trade is not distributed evenly across geography. A small number of maritime and terrestrial corridors
carry a disproportionate share of physical volume, and within those corridors a handful of narrow points can
halt flow entirely. This concentration is efficient — it is the result of economies of scale — and it is also
the system's principal fragility.

This paper proposes a **circulation model** of trade: treat corridors as arteries, chokepoints as valves, and
throughput as flow, then ask the questions physiology asks. What happens to a body when an artery is
occluded? What does the occlusion cost the organ downstream, and what does it cost the tissue *at* the
occlusion? The model's central prediction is that the cost is distributed non-linearly: **small blockages are
absorbed, moderate blockages are expensive but survivable, and severe blockages damage the party applying them
as much as the party they are applied to.**

The Strait of Hormuz is used as the worked case, because it is the clearest and most studied instance. The
paper is explicit about what the analogy cannot carry: arteries have no agency, no strategy and no
alternatives, and trade does — which weakens the model precisely where it would be most convenient.

## 1. The proposition

The Silk Road was never a road. It was a **set of corridors** through which goods, people and — more
consequentially — techniques and ideas moved between civilisations that otherwise had little contact. Its
historical importance was not the distance covered but the **contact density** it created along the way.

"Silk Road 2.0" is the observation that the same structure has re-emerged at greater scale: corridors of
concentrated flow, cities that exist because they sit on one, and chokepoints whose closure would be felt far
from the closure itself.

The proposition of this paper is that this structure should be analysed **as a circulation system**, because
circulation systems have well-understood failure modes, and trade policy currently reasons about them
informally. Three consequences follow from taking the model seriously:

1. **Throughput concentration is efficient and therefore self-reinforcing** — which is why it cannot simply be
   declared undesirable and dispersed by policy.
2. **Redundancy is expensive and therefore underprovided** — the classic public-goods problem, applied to
   shipping lanes.
3. **Blocking a chokepoint is a self-targeted instrument** — not out of morality, but out of arithmetic.

## 2. The model

Let a corridor carry a flow $F$ (tonnes or value per unit time) with capacity $C$. Utilisation is
$\rho = F/C$.

Three regimes, borrowed from queueing and from physiology:

| Regime | Condition | Behaviour |
|:---|:---|:---|
| **Laminar** | $\rho \ll 1$ | Flow is proportional to demand; delays are negligible; rerouting is unnecessary |
| **Congested** | $\rho \to 1$ | Delay grows non-linearly with utilisation; small shocks produce large delays; cost rises without any physical blockage |
| **Occluded** | capacity loss | Flow is constrained by remaining capacity; the deficit propagates downstream immediately |

The important property is the **non-linearity at the boundary**. In the congested regime, a 5 %
capacity loss can produce far more than a 5 % cost increase, because delay costs compound — insurance,
demurrage, inventory carrying cost and contract penalties all scale faster than volume. **This is why
chokepoint risk is systematically underpriced in peacetime:** the system spends most of its time in the laminar
regime, where the model behaves linearly and intuition is correct.

### 2.1. The cost of occlusion, to both sides

Define an occlusion that removes a fraction $\phi$ of capacity. The cost falls into three buckets:

$$C_{\text{occlusion}} = \underbrace{C_{\text{reroute}} + C_{\text{delay}}}_{\text{to users}} + \underbrace{C_{\text{enforcement}} + C_{\text{retaliation}}}_{\text{to the blocker}} + \underbrace{C_{\text{reputation}}}_{\text{to both, deferred}}$$

The user-side terms are the ones usually counted. The blocker-side terms are the ones usually not, and they are
the reason for this paper's third consequence:

- **$C_{\text{enforcement}}$** — maintaining a blockade requires force deployed continuously, which is a
  recurring cost, not a one-off.
- **$C_{\text{retaliation}}$** — a blocked party does not passively absorb the loss; it imposes costs in
  domains where it retains leverage.
- **$C_{\text{reputation}}$** — and this one is structural rather than punitive: **every user of the corridor
  now has a reason to buy redundancy.** The blockade, even if lifted, permanently reduces the corridor's value
  to the blocker, because the blocker's leverage *was* the corridor's indispensability.

**That third term is the model's strongest prediction and its most interesting one:** a chokepoint's value as
an instrument is destroyed by using it. It is a wasting asset. This is not a moral claim; it is what follows
from users being rational.

## 3. The worked case: Hormuz

The Strait of Hormuz is the clearest instance because its parameters are extreme and well documented. Roughly
**a fifth of global petroleum liquids consumption** transits it, with very limited alternative capacity — the
available bypass pipelines carry a small fraction of the maritime volume.

Applying the model:

- **Baseline utilisation is high.** The corridor spends much of its time in the congested regime, so the
  system is already paying a delay cost that is invisible because it is normal.
- **$\phi$ is large for any realistic closure.** There is no partial occlusion that is cheap: the alternatives
  are pipelines with a fraction of the capacity.
- **User cost is immediate and global.** Energy prices are set at the margin, so the cost is not borne
  proportionally by volume transited; a small physical deficit produces a large price effect.
- **Blocker-side cost is severe and durable**, through all three terms: enforcement is continuous, retaliation
  is available to many parties, and **every importer's response is to accelerate diversification** — which is
  precisely the destruction of the asset.

**The case illustrates the paper's weakest point as well as its strongest.** Hormuz is a *positional* good: the
gain from controlling it is enormous, which is exactly why it generates conflict rather than trade. The model
predicts that blocking is self-harming **for a party whose interest is trade**; it does not predict that no
party will ever find blocking rational, because a party may value position over production.

## 4. Where the analogy fails

A metaphor that is not bounded becomes a substitute for thought. Four limits, stated plainly:

**Arteries have no agency.** A blocked artery cannot reroute. A trading system can, given time — which means
the model overstates short-run costs and understates long-run adaptation. Long-run adaptation is precisely what
destroys a chokepoint's strategic value, so the model is right about the direction and wrong about the timing.

**Arteries have no alternatives; trade does.** Bypasses exist, cost more, and are built when risk justifies the
expense. The model's occlusion term should therefore decay over time, and in the long run approaches the cost
of the redundant capacity, not the cost of the blockage.

**"Health of the planet" is figurative.** The planet is not an organism and does not sicken. What is real is
that **the sum of many local blockages produces aggregate welfare loss** that no single actor bears, which is a
collective-action problem, not an organismic one. Calling it health is a useful shorthand and a dangerous one if
taken literally, because organisms can be healed by an intervention and markets cannot.

**The model is silent on distribution.** Aggregate loss can coexist with individual gain: a blockade that costs
the world 2 % can enrich a small number of parties substantially. Any claim that "blocking hurts everyone"
must immediately add that **it can still be rational for someone**, which is why the argument for open
corridors cannot rest on arithmetic alone.

## 5. What follows, if the model holds

Not a policy programme — a set of testable implications:

| Implication | How it could be tested |
|:---|:---|
| Corridors spend more time in the congested regime than operators assume | Compare measured delay costs against operator contingency budgets |
| Blockades permanently reduce the leverage of the blocked chokepoint | Measure the share of redundant capacity built in the five years after a closure, against the five before |
| The third-party cost of an occlusion exceeds its direct cost | Compare global price effects against the physical volume deficit |
| Redundancy is systematically underprovided | Observe how much rerouting capacity is built without state intervention |

None of these have been tested here. They are stated because a theory that cannot say what would confirm it is
not a theory, it is a mood.

## 6. Relation to NEPTUNO

The framework described in WP 16 argues that **projection requires immunisation** — that reach without a
reinforced base is not sustainable. This paper's model is the same claim at a different scale: **a trading
system that reaches everywhere through a handful of un-reinforced valves is projecting on an immunised-looking
base that is not actually immunised.**

That parallel is offered as an analogy, and the paper is explicit that analogies between a company framework
and geopolitics prove nothing. What transfers is the reasoning about ordering, not the conclusions.

## 7. Conclusion

The theory, at the strength it can hold:

> **Trade concentrates in narrow corridors; concentration is efficient and therefore durable; the efficient
> level of concentration is above the safe level, because redundancy is a public good nobody is paid to
> provide; and using a chokepoint as an instrument destroys it as an instrument, because the response of every
> user is to build the redundancy that made the chokepoint valuable.**

Blocking is not always irrational — positional goods exist, and this paper says so — but for any actor whose
interest is production rather than position, **the arithmetic of a blockade is negative, and it is negative for
the actor who imposes it.** That is the claim. It is a theory. It has a model, a case, and a list of ways it
could be wrong.

## References

1. Brisecom, *The Trident: Three Layers of Resilience That Converge in One Point of Resolution* (WP 16) — the
   analogous ordering claim at organisational scale. <https://github.com/javi-jimenez/laia/blob/main/whitepapers/neptuno-trident-three-layers-resilience.md>
2. Brisecom, *Defence Is Cheaper Than Attack: A Cost Accounting of Offensive Versus Defensive Posture* (WP 17) —
   companion paper; §5 there explains why positional goods are the limit of the positive-sum argument.
   <https://github.com/javi-jimenez/laia/blob/main/whitepapers/defence-cheaper-than-attack-cost-accounting.md>
3. Energy Information Administration, *World Oil Transit Chokepoints* — the standard reference for corridor
   volumes and bypass capacity.
4. UNCTAD, *Review of Maritime Transport* (annual) — corridor concentration and freight cost series.

> **Note on figures.** The Hormuz share ("roughly a fifth of global petroleum liquids consumption") is quoted
> at the precision at which it is defensible. No component of §3 is presented as a measured cost, because
> none of it has been measured here; the case is used to illustrate the model's terms, not to calibrate them.
