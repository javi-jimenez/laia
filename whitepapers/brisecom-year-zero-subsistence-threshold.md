---
title: "Year Zero: What a Company With Large Ambitions Actually Costs to Keep Alive"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-10-23
version: "1.0"
status: "Draft"
tags: ["company viability", "fixed cost", "B2B contracting", "lean structure", "corporate governance", "year zero"]
keywords: ["minimum viable company", "fixed cost base", "B2B contracts", "no payroll", "subsistence threshold", "corporate governance", "independence"]
license: "CC BY-NC-SA 4.0"
---

# Year Zero: What a Company With Large Ambitions Actually Costs to Keep Alive

## Abstract

This paper is a case study of one company's first twelve months, written from its own ledger rather than from a growth narrative. **Brisecom S.L.** published thirteen technical white papers, built and operates four websites on its own infrastructure, and closed its first year with a **fixed annual cost of approximately €1,124** — two invoices and no others — with **zero employees, zero payroll and zero public funding**.

The claim defended here is narrow and testable: **a company's survival does not depend on how small its costs are, but on whether those costs are proportional to the mechanism that produces its revenue.** In this case the mechanism is B2B contracting: each cost attaches to a contract, and each contract pays before it costs. Everything that did not fit that rule was either deferred, absorbed by the founder personally, or not done.

The paper also states what the figure does not cover, because a cost statement without its exclusions is a marketing claim. €1,124 is what the *company* costs, not what the *year* cost. The difference was borne personally, out of the books, and that fact is part of the result rather than an embarrassment to it.

## 1. The question this paper answers

There is a question founders are asked rarely and answer badly: **what is the smallest structure in which serious work can be done without lying about it?**

The usual answers fall into two groups. The first says a company needs capital, headcount and a burn rate before it can be credible. The second says a company can be a website and an invoice. Both are partly true and both are useless, because neither says *where the line is*.

This paper proposes the line is not a figure. It is a **relationship**: the ratio between the fixed cost base and the revenue mechanism. A €200,000 annual cost base is perfectly healthy against a mechanism that reliably produces €400,000. A €40,000 cost base is fatal against a mechanism that produces nothing for eighteen months.

Everything below is the arithmetic of that relationship in one specific case, with the exclusions stated.

## 2. Method and source of the figures

All figures are taken from the company's own records as of **23 October 2026**, the first anniversary of incorporation. Where a figure is a measurement rather than a statement, the instrument is named.

| Item | Value | Source |
|:---|:---|:---|
| Legal form | **BRISECOM, S.L.** — CIF B23980998 | Registro Mercantil de Valencia, Sección 8.ª, Hoja V-229523, Inscripción 1.ª (30-10-2025) |
| Share capital | **€3,000** | Same registry entry |
| Registered office | Calle Colón 40, 1º 1ª, 46004 Valencia | Same |
| Corporate purpose (CNAE) | **72.10** — research and experimental development in natural sciences and engineering | Same |
| Fixed annual cost | **≈€1,124** | Two supplier invoices, detailed in §3 |
| Employees | **0** | No employment contracts exist |
| Payroll | **€0** | Consequence of the above |
| Public funding received | **€0** | No grant, subsidy or advance has been received |
| White papers published | **13** (this document is the fourteenth) | Public repository, dated per document |
| Websites in operation | **4** | Each with its own version-controlled history |

Two details matter for reproducibility. First, the fixed cost is **two lines, not a category**: a virtual office at **€43.69/month** (mailing and fiscal address) and an accounting firm at **€50/month** (bookkeeping, quarterly returns, annual filings). Second, the registrations the company holds — **PIC 866059651**, **EU Expert ID EX2025D1323771**, **UNGM 1198769**, **EU Transparency Register REG 6002677103007-57** — were obtained at no cost and are verifiable by third parties, which makes them better evidence of activity than any self-description.

## 3. The cost base, and why it is only two lines

The reason the figure is small is not frugality. It is that **every recurring cost was rejected unless it could be attached to a contract that pays for it**.

| Cost | Monthly | Why it exists |
|:---|---:|:---|
| Virtual office (mailing and fiscal address) | €43.69 | A company without a verifiable address cannot invoice, and cannot be found by a client who wants to check it exists |
| Accounting (bookkeeping, quarterly returns, annual filings) | €50.00 | Non-negotiable in Spain. This is the price of the legal form, not a service that can be optimised away |
| **Total** | **€93.69** | **€1,124.28 per year** |

What is *not* on the list is the informative part:

- **No office.** Work happens where the work is. A rented room would have to be paid every month whether or not there is revenue, which is precisely the shape of cost that kills companies of this size.
- **No payroll.** Not a virtue in itself, and not a permanent condition — see §6.
- **No liability insurance.** There is none because **there is no payroll**: with no employment relationship, the risk that insurance covers does not exist. It will be taken out the day the first employment contract exists, not before. Paying a premium against a risk you do not carry is exactly the kind of cost that sinks a company this size.
- **No marketing budget.** Publication is the marketing, and it is priced in hours rather than euros.
- **No software subscriptions.** Infrastructure is self-hosted (§4), which converts a recurring cost into a one-off competence.

## 4. What was built with it

A cost figure means nothing without the output it bought. In the same twelve months, with the cost base above:

**Thirteen technical white papers**, published openly under **CC BY-NC-SA 4.0**, each with an architecture, validation criteria or build conditions. They cover algorithmic ethics, AI governance, formal methods, distributed systems, model collapse, forensic auditing and information sovereignty. They are not opinion pieces: **every one can be read, disputed and cited without asking permission.**

**Four websites**, none bought as a template and none hosted behind an agency:

- the company itself,
- the LAIA project, built around a single methodological commitment — *axioms are given, inferences are proven*,
- the NEPTUNO collaboration framework,
- a personal site.

Behind all four: **own cluster, own version control, own object storage, own private network.** Mail, repositories, deployments and backups, in house.

This is not distrust for its own sake. **Sovereignty without control of infrastructure is a marketing word.** A company that publishes on data governance while renting every layer of its own stack is making a claim it cannot audit — and the first person who should be able to audit it is the one making it.

Measured, not asserted: **261 commits** across the four repositories between **13 December 2025** and **23 October 2026**. A version history cannot be reconstructed backwards; it records what was published, and when.

## 5. The mechanism: B2B contracts, and nothing else

This is the part that makes the cost base rational rather than merely small.

The company sells **contracts to organisations** — research, intelligence and technical assessment services, invoiced B2B. It does **not** sell subscriptions, does not run a consumer product, does not depend on advertising, and has not taken public money. Each of those alternatives would have introduced a cost paid *before* the revenue it produces:

| Mechanism | Cost that must be paid before revenue | Fit with a one-person company |
|:---|:---|:---|
| **B2B contract** | None. The work is scoped, priced and invoiced per engagement | ✅ Costs scale with the contract, not with the ambition |
| Consumer product | Development, support, payments, refunds, acquisition | ❌ Fixed cost against uncertain volume |
| Subscription | Infrastructure sized for peak, churn management, support | ❌ Must be paid every month from month zero |
| Advertising | Audience before revenue, and at a scale this size never reaches | ❌ Buys nothing that can be invoiced |
| Public grants | Reporting, audits, pre-financing of cash flow | ❌ Pays late, and pays against a plan rather than a client |

The B2B mechanism has one property the others do not: **the cost of pursuing an opportunity is close to zero.** Writing a proposal costs hours, not euros. A rejected proposal costs nothing that has to be recovered. That is what allows a company of this size to address institutional and European-scale work at all — seventeen institutions can be approached for the price of the writing.

There is a second consequence, less comfortable. A B2B company of one is **entirely dependent on the founder being able to sell**. The low cost base protects the company from going under between contracts; it does nothing to generate the next one. Frugality is a floor, not an engine, and confusing the two is how small companies die slowly.

## 6. What the figure does not cover — the exclusions, stated

A cost statement whose exclusions are hidden is not a measurement. These are the four that matter.

**First: €1,124 is what the company costs, not what the year cost.** AI credits, domains and hosting were paid **personally, outside the company's books**. The company has two invoices; the work and the means were the founder's. That makes the structure very cheap and it also makes the result **not directly repeatable** by anyone without the same willingness to absorb cost personally. Any reader who tries to replicate the model should count that line before congratulating themselves on the total.

**Second: the company rests on one person, not on a balance sheet.** This is simultaneously a strength for resilience and a weakness for continuity, and both are true at once. A balance sheet survives its founder; a person does not. Nothing in this paper should be read as claiming the arrangement is durable — only that it is *viable*, which is a weaker and more defensible claim.

**Third: zero public funding is a choice, not a virtue.** It means no dependency on a reporting calendar and no pre-financing of cash flow. It also means no external validation, and it excludes a category of work that only public money will pay for. The choice is defensible; it is not free.

**Fourth: the paper says nothing about revenue.** Deliberately. A cost base is a fact; revenue is a distribution. Publishing the first while implying the second is the exact move this paper is written against.

## 7. Generalisable conditions

The case does not generalise as *"companies can run on €1,124"*. It generalises as five conditions, all of which were necessary here:

1. **The revenue mechanism must not require fixed cost to be attempted.** Contracts, not products. Proposals, not funnels.
2. **Every recurring cost must attach to a contract that pays for it.** If a cost cannot name the contract that covers it, it is a bet, and bets belong to the founder's pocket and not to the company's accounts.
3. **The legal form must be preserved even when it looks unnecessary.** Registry entry, accounting and an address are what convert activity into a traceable entity. They are the cheapest part of the structure and the most expensive to be missing when a client checks.
4. **The founder must be able to absorb the means, not just the time.** This is the condition people skip. It is also the one that makes the model unavailable to most people who would want it.
5. **Output must be public.** Thirteen open papers cost the same as thirteen private ones, but only the public version produces the credibility that a company without a sales team has to substitute for one.

## 8. Conclusion

The memorable figure here is €1,124, and it is the least interesting part. What the year actually demonstrates is narrower and more useful:

**A company with large ambitions does not need a large structure. It needs a cost base that is proportional to how it earns, stated exclusions included.**

Thirteen technical papers, four self-hosted websites, **261 commits** of continuous publication and a two-invoice cost structure are compatible — provided everything is sold as B2B contracts, provided the founder carries the means personally, and provided the arithmetic is published with the parts that do not flatter it left visible.

A rounded number is the first thing that gets contradicted. So the number is not rounded, and the year-one claim is stated at the strength it can survive: **the structure is viable.** Whether it is durable is a question for year two, and this paper has no data on it.

## References

1. Registro Mercantil de Valencia — BRISECOM, S.L., Sección 8.ª, Hoja V-229523, Inscripción 1.ª, 30 October 2025.
2. Brisecom, *One Year of Brisecom: Thirteen Papers, Four Websites, Zero Payroll*, 23 October 2026. <https://brisecom.org/blog/one-year-of-brisecom/>
3. LAIA white paper repository. <https://github.com/javi-jimenez/laia/tree/main/whitepapers>
4. Brisecom, *NEPTUNO Network — Rules for Collaborators*, v1.0, 23 October 2026. <https://brisecom.org/neptuno-network/rules/>
5. Brisecom, *Policy on the use of personal intellectual property within Brisecom*, 23 October 2026 (internal).
