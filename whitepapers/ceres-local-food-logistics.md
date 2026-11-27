---
title: "CERES: Last-Mile Food Logistics Without a Platform — Surplus from the Field, Carried by Young Self-Employed Couriers"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-11-27
version: "1.0"
status: "Draft"
order: 26
topic: "Agri-food, last-mile logistics, cooperativism, food loss, platform-free coordination"
tags: ["agri-food", "last mile", "food loss", "cooperatives", "self-employment", "logistics", "urban agriculture", "food sovereignty"]
keywords: ["food surplus", "short food supply chain", "cooperative", "autónomo", "false self-employment", "route ownership", "cold chain", "last-mile"]
doi: "10.5281/zenodo.24583114"
license: "CC BY-NC-SA 4.0"
---

# CERES: Last-Mile Food Logistics Without a Platform

<!-- doi:start -->
> **DOI:** [10.5281/zenodo.24583114](https://doi.org/10.5281/zenodo.24583114) · Zenodo (concept DOI [10.5281/zenodo.24583102](https://doi.org/10.5281/zenodo.24583102)) · cite this version
<!-- doi:end -->

**Author:** Francisco Javier Jiménez Gómez

**Organization:** BRISECOM SL

## Abstract

Product leaves the field every week that never enters the commercial channel: it is
the wrong size, the wrong shape, the surplus of a good season, or the share that a
distributor does not want that week. At the same time, there are workplaces and
neighbourhoods where fresh food arrives badly or not at all, and there are young
people who want work that is theirs rather than a shift assigned by an application.

The conventional answer to this gap is a delivery platform. This paper specifies the
opposite arrangement: **no platform, no commission, no dispatcher algorithm.** The
courier is self-employed or a member of a cooperative; the route is theirs; the
farmer sells what would otherwise be lost; the buyer pays for food, not for
intermediation.

Two questions decide whether such a scheme works, and neither is rhetorical:

1. **If nobody takes a commission, who pays for the work?** Answer: the same spread
   that intermediation takes today. The paper states it as a parametric model, not
   as a claim about current prices.
2. **If nobody dispatches, who coordinates?** Answer: a shared board, owned routes,
   and a commons rule — specified here, because "they organise themselves" is a
   slogan until it is written down.

The paper also states, without softening, the three ways this design can fail: legal
reclassification of couriers as false self-employed, a cold chain that cannot be
guaranteed at ambient temperature, and a coordination board that quietly becomes a
dispatcher with a different name.

## 1. What stays in the field, and why

Three different things get called "surplus", and mixing them is how a well-meaning
project ends up distributing food that should not be eaten:

| Category | What it is | Sellable | Donatable | Fit for this scheme |
|:---|:---|:--:|:--:|:--:|
| **Excedente** | Good, sellable product that the channel did not absorb this week | yes | yes | **yes — the core of the model** |
| **Descarte comercial** | Fit for consumption, rejected for size, shape or cosmetic grading | yes, discounted | yes | **yes — this is where the volume is** |
| **Residuo** | Not fit for human consumption | no | no | **no — never** |

The scheme lives in the first two rows. The third is compost, animal feed or
disposal, and a project that blurs the boundary is one food-poisoning incident away
from ending.

**Why it exists at all** is a matter of grading and forecasting, not of abundance:
a supermarket accepts a calibrated size; a household does not care. A distributor
forecasts a week ahead; a farmer harvests what the weather gives. The gap is
structural, and it is priced at zero by the party holding it — which is exactly why
it can be sold cheaply without anyone being exploited.

## 2. What this is not

- **Not a delivery platform.** There is no application taking a percentage, no
  rating that disciplines the courier, and no algorithm assigning work. If a
  percentage appears, the model has failed and should be renamed.
- **Not a charity.** Charity distributes what is left over and depends on the
  donor's mood. This is a commercial chain with thin margins, which is more durable.
- **Not Glovo with better intentions.** Glovo's couriers are, in practice, directed
  by an application that sets price, route and penalty. Removing the application
  while keeping the direction is the legal problem described in §4, not a solution
  to it.
- **Not a claim that food waste ends.** It reduces a specific flow: commercial
  surplus within a radius a bicycle can cover.

## 3. The economic model, as formulas rather than promises

The scheme has one funding pool and four claims on it. Let:

| Symbol | Meaning | Unit |
|:---|:---|:---|
| `P_r` | retail price of the same product in a conventional shop | €/kg |
| `P_f` | price paid to the farmer (farm-gate) | €/kg |
| `P_c` | price paid by the buyer in this scheme | €/kg |
| `m` | intermediation margin taken today: `P_r - P_f` | €/kg |
| `k` | the fraction of `m` that this scheme captures | 0..1 |
| `q` | kilograms per drop | kg |
| `d` | drops per route | — |
| `c_km` | cost per kilometre of the vehicle (energy, wear, insurance share) | €/km |
| `L` | route length | km |
| `t` | hours per route | h |
| `w` | the courier's target hourly income | €/h |

**The buyer's price** must stay below retail or nobody switches:

```
P_c = P_f + k·m        with 0 < k < 1
```

**The route's gross income**:

```
G = d · q · k · m
```

**The route's cost** (the courier's own vehicle, own insurance, own time):

```
C = L · c_km + t · w
```

**The condition for the model to exist at all**:

```
d · q · k · m  >  L · c_km + t · w
```

Three consequences follow, and they are the whole design:

1. **Volume per drop matters more than price.** `q` and `d` multiply; `m` and `k`
   divide. A scheme that fights for a higher `k` while delivering one bag at a time
   cannot work. This is why the target is **workplaces** — a kitchen, a canteen, an
   office with a fridge — where `q` is tens of kilograms, not a household basket.
2. **Distance is the enemy, and it is measurable.** `L · c_km` grows with the radius;
   the scheme only works in a dense ring around the field. Valencia and l'Horta are
   exactly that geography.
3. **The courier's income is a residual, and it must be stated as one.** `w` is what
   remains after costs, not what the buyer feels like paying. A scheme where the
   courier absorbs the volatility is a scheme that collapses in the first bad week.

> **What this model does not know.** Every value above is a parameter, and none is a
> measured fact about Valencia today. Filling the table is the pilot's first job
> (§9). Presenting assumed values as findings is the failure mode this paper exists
> to avoid.

## 4. Legal form: why the cooperative is not a detail

The organising question is not "platform or no platform"; it is **who has the power
to direct the work**. Under Spanish law, a self-employed courier who receives
instructions, a fixed schedule and penalties is at risk of being reclassified as an
employee — the *falso autónomo* doctrine. That risk belongs to whoever directs, and
in a platform it is systematically transferred to the courier.

| Form | Who directs | Who sets the price | Legal exposure | Fit |
|:---|:---|:---|:---|:---|
| **Platform + autónomo** | the platform | the platform | high: reclassification, fines | no — the thing we are leaving |
| **Autónomo, own clients** | the courier | the courier | low, if genuinely independent | yes for a single route owner |
| **Cooperativa de trabajo asociado** | the members, by assembly | the assembly | low; the courier *is* the owner | yes **preferred** |
| **Association without legal form** | nobody, in practice | unclear | high: no invoicing, no liability | no |

**The recommendation is a cooperative of work, with the option of an individual
autónomo for a rider who wants a single route.** Both are legitimate; the
cooperative is stronger because it makes the absence of a dispatcher structural
rather than a promise. In a cooperative the rider cannot be directed by an
application, because the application is not a member and has no vote.

**Three obligations that come with handling food**, independent of legal form:

- registration as a food business operator before the first delivery;
- hygiene rules of Regulation (EC) 852/2004, including traceability one step back
  and one step forward;
- transport conditions compatible with the product: ambient for dry and robust
  produce, temperature-controlled for anything perishable (§6).

> NOTE: **Flagged for verification before publication.** The specific articles of the
> Spanish food-loss prevention legislation and the current registration scheme
> (RGSEAA) must be checked against the consolidated text before this paper is cited
> in a proposal. They are named here as obligations, not as article numbers, because
> a wrong number in a legal section discredits the whole document.

## 5. Coordination without a dispatcher

"Self-organised" is not a mechanism. Here is one, in the open, so it can be broken:

**The board.** One shared list, visible to all members, with three columns: what is
available at the field today, which route each member owns, and what a member has
committed to collect. It can be a blackboard, a spreadsheet or a messaging group.
**It is not an application that assigns**: nothing arrives in a courier's phone as
an order with a deadline.

**Owned routes.** Each route belongs to a member, permanently, and can be sold or
inherited within the cooperative. Ownership is what replaces assignment: a rider
does not wait to be dispatched to a street, because that street is theirs.

**The commons rule.** Two constraints the assembly fixes and does not negotiate per
delivery:

1. **A price floor for the farmer**, so competition between riders cannot be funded
   by squeezing the field.
2. **A ceiling on the radius**, so a route cannot be extended to win a client at the
   cost of the cold chain and the rider's hours.

**The failure mode, named.** A board that starts telling members where to go has
become a dispatcher with a different name, and the legal analysis of §4 applies
again. The test is mechanical: **if a member can refuse a delivery without penalty,
it is a board; if refusal has a cost, it is an employer.**

## 6. The cold chain, and the honest limit

A bicycle with a crate is not a refrigerated vehicle. The scheme is therefore
specified around what ambient transport can actually carry:

| Product | Ambient, short route | Needs cold | Verdict |
|:---|:---|:---|:---|
| Dry produce (potato, onion, citrus, squash) | yes | no | yes core |
| Robust fruit and vegetable, same-day | yes, under 2 h, shaded | no | yes core |
| Leafy greens, summer | no | yes | no unless insulated box with ice |
| Dairy, meat, fish, prepared food | no | yes | no outside scope |
| Anything requiring a temperature record | no | yes + logger | no outside scope |

**The rule that follows:** the scheme carries what a crate on a bicycle can carry
safely, and refuses the rest — visibly, in writing, before a client asks. Widening
the catalogue to win a customer is how a food-safety incident gets invited.

## 7. Why young people, and why that is not a marketing line

The scheme is aimed at people entering work for the first time, and the reason is
structural rather than sentimental:

- **The capital requirement is near zero.** A second-hand bicycle, a crate and
  insurance. No licence, no premises, no fleet.
- **The skill is learnable in a week**, and the route is a territory a person can
  own — which is exactly what an entry-level job in a warehouse does not offer.
- **The cooperative is a school in governance.** Young members vote on the price
  floor and the radius. That is civic practice with an invoice attached.

**And the counter-argument, stated:** delivery work is physically demanding, exposed
to weather and traffic, and easy to romanticise from an office. The scheme does not
claim dignity by association. It claims three concrete things: the income is
transparent (`w` is derived, not negotiated per delivery), the route is owned, and
the worker has a vote. Whether that is enough is a question for the pilot, not for
this paragraph.

## 8. What this design cannot do

- **It does not fix agricultural prices.** It captures a fraction `k` of an existing
  spread; it does not create demand.
- **It does not scale beyond a dense ring.** At 40 km the courier's cost exceeds the
  margin; the model is urban-periurban by construction.
- **It does not remove the need for a cold chain or a food-safety system**, only
  narrows the catalogue to what avoids them.
- **It does not eliminate the temptation to become a platform.** The moment a member
  is told where to go, the advantage is gone and the legal risk returns.
- **It has no measured numbers yet.** Everything in §3 is a formula awaiting a pilot.

## 9. Pilot design — València and l'Horta

| Element | Specification |
|:---|:---|
| **Geography** | l'Horta Nord and l'Horta Sud, inside a 15 km radius of the city; delivery to workplaces and to neighbourhoods outside the commercial last mile |
| **Volume** | 3 producers, 5 routes, 2 drops per route per day, target `q` >= 25 kg per drop |
| **Legal form** | one cooperativa de trabajo asociado, 5 founding members; each owns one route |
| **Duration** | 12 weeks, of which the first 2 are legal and cold-chain setup with no deliveries |
| **Instrumentation** | every route logged: `d`, `q`, `L`, `t`, kilograms saved from loss, €/kg paid to the farmer versus the conventional channel |
| **Falsifiable hypotheses** | see below |

### Hypotheses fixed before the pilot

| ID | Hypothesis | Falsified if |
|:---|:---|:---|
| **H1** | A route of 2 drops at >= 25 kg each exceeds `L·c_km + t·w` at a buyer price below retail | any week closes negative with `q` at target |
| **H2** | `k` can be held below 0.5, so the buyer pays at most half the intermediation margin and still funds the route | the required `k` exceeds 0.5 to break even |
| **H3** | No member refuses a delivery because of a penalty — i.e. the board is a board | refusal carries any cost, formal or social |
| **H4** | The ambient catalogue of §6 reaches >= 70 % of the kilograms available from the three producers | more than 30 % of volume needs cold |
| **H5** | Farmers prefer this channel to discarding, at a lower price than the conventional one | a producer returns to discarding at equal or better net price |

**H3 is the one to watch.** It is the hypothesis that distinguishes this scheme from
every platform that calls itself a cooperative.

## 10. Conclusion

The gap between what the field produces and what the city eats is not a shortage of
technology. It is a shortage of a legal and economic arrangement in which the person
carrying the box owns something: the route, the price, or the vote.

CERES proposes that arrangement in the smallest form that can be tested — five
people, five routes, twelve weeks, one cooperative, no application. If the
arithmetic in §3 holds with measured numbers, the model is worth scaling. If it does
not, the result is still worth publishing, because the failure mode of every
platform alternative so far has been to keep the platform and rename the commission.

## References and primary sources

1. Regulation (EC) No 852/2004 of the European Parliament and of the Council on the
   hygiene of foodstuffs.
2. Spanish food-loss prevention legislation — **article numbers to be verified
   against the consolidated text before citation** (§4).
3. Spanish cooperative law (state and Valencian level) — legal form of the
   *cooperativa de trabajo asociado*.
4. Spanish self-employment registration (RETA) and the *falso autónomo* doctrine.
5. FAO, *The State of Food and Agriculture* — losses versus waste, definitions used
   in §1.
