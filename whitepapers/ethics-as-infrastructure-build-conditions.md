---
title: "Ethics as Infrastructure: Build Conditions and the Layer the EU AI Act Does Not Regulate"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-10-21
version: "1.0"
status: "Draft"
tags: ["AI ethics", "EU AI Act", "labour rights", "AI governance", "ethical economy", "build conditions", "LAIA"]
keywords: ["ethics as infrastructure", "build conditions", "AI Act Article 14", "Article 26", "platform work directive", "algorithmic management", "fundamental rights impact assessment", "AI literacy"]
license: "CC BY-NC-SA 4.0"
---

# Ethics as Infrastructure: Build Conditions and the Layer the EU AI Act Does Not Regulate

**IP Holder & Principal Researcher:** Francisco Javier Jiménez Gómez

**Affiliation:** BRISECOM SL / LAIA Project

**Publication Date:** October 2026

**Document Classification:** Technical Whitepaper — Governance & Applied Ethics

## Abstract

European AI regulation has reached a level of maturity that was hard to imagine a decade ago: a risk-tiered horizontal Regulation, a directive on algorithmic management in platform work, a binding international convention, and a data-protection regime with a right against solely automated decisions. Yet all of these instruments share an unexamined boundary. They regulate **what an AI system does** and **who is legally answerable for it**, but they do not regulate **the conditions under which the system was built**. A model can be documented, conformant, and certified while the people who trained it, annotated its data, or designed its architecture worked without authority, without recognition, and without a channel to report what they knew.

This paper formulates that gap precisely and proposes a way to close it voluntarily. It defines *ethics as infrastructure* — an engineering property, not a declaration — as the set of five structural conditions (participatory problem definition, transparency of working conditions, recognition of invisible labour, benefit sharing, and protected voice) that must hold before the first commit, not after the last audit. It then maps each condition against the AI Act (Regulation (EU) 2024/1689) and its adjacent instruments, showing which obligations already exist, which are weaker than commonly assumed (notably Article 26(7) and Article 27), and which have no legal counterpart at all. Finally, it specifies the **Build-Conditions Disclosure (BCD)**: a compact, auditable instrument of eight items that an organisation can answer for any AI system, designed to be embedded in an Article 27 fundamental-rights assessment or an Article 95 code of conduct without requiring new legislation.

## 1. Introduction

### 1.1. The layer nobody audits

Discussions of ethical AI have a standard topology. They begin with model behaviour (bias, hallucination, safety), move to data (consent, provenance, copyright), and end with governance (documentation, conformity assessment, post-market monitoring). Every one of these layers is real, and each now has at least partial legal backing in the European Union.

There is a layer beneath them that is almost never questioned: **who builds the AI, and under what conditions?** In most organisations the technical expert is structurally converted into a *resource* — a supplier of execution for decisions taken elsewhere. That arrangement is rarely defended explicitly; it is simply inherited from industrial management and reproduced in knowledge work.

The consequence is not merely unfair. It is *technical*. Organisations that withhold authority from the people who understand the system while assigning them accountability for its outcomes do not distribute responsibility: they manufacture scapegoats, and they suppress exactly the information that would prevent failure. When such a system malfunctions, the post-mortem reliably discovers that someone knew — and had no channel, or no incentive, to say so.

### 1.2. Contribution and method

This paper makes three contributions:

1. A **definition** of ethics as infrastructure in terms of five verifiable structural conditions (Section 4), rather than a list of values.
2. A **legal mapping** of those conditions against the AI Act and adjacent instruments, identifying the precise point at which European law stops (Section 5).
3. A **proposed disclosure instrument** — the Build-Conditions Disclosure — with eight items, evidence expectations, and integration paths into existing conformity and code-of-conduct mechanisms (Section 6).

The method is doctrinal and practitioner-based. It reads the AI Act at article level rather than at the level of its recitals and press summaries, and it draws on applied experience in AI system construction. It does not present empirical measurement of build conditions across organisations; that is the obvious next step and is flagged as a limitation (Section 7).

## 2. Background

Three literatures converge on this problem and none of them closes it.

**Operational ethics and design theory.** Value Sensitive Design established that values must be enrolled at design time, because by the time a system exists its moral shape is largely fixed (Friedman & Hendry, 2019). The operational-ethics literature followed by translating principles into lifecycle mechanisms: participatory audit, transparency, accountability, continuous evaluation (LAIA, 2024; OECD, 2019; UNESCO, 2021). These mechanisms target *the system*, not *the organisation that produces it*.

**Critique of ethics discourse.** Wagner (2018) documented how voluntary ethics frameworks can function as a substitute for regulation rather than a complement to it. This is the strongest available warning against the instrument proposed in Section 6: any voluntary disclosure can decay into a plaque. The design of the BCD is a direct response to that risk — it asks for *artefacts and named responsibilities*, not for statements of intent.

**Labour-focused AI research.** Crawford (2021), Roberts (2019) and Gray & Suri (2019) documented the extractive supply chains of contemporary AI: annotation labour designed to be unassignable, moderation work performed under non-disclosure, mineral and energy costs displaced geographically. Their accounts make the abstract claim of Section 1.1 concrete: the invisibility of the workforce is not an accident of distance, it is a design feature.

What none of these literatures does — and what European law also does not do — is convert the observation into an obligation. That is the gap addressed here.

## 3. The object of regulation

### 3.1. What the AI Act regulates

The AI Act is a product-safety instrument. Its addressees are **providers** and **deployers** — legal or natural persons, public authorities, agencies or other bodies — and its object is the **AI system** as a good placed on the market or put into service. Obligations attach to systems by risk tier, and enforcement attaches to entities.

That architecture is coherent, and it is the reason the Regulation is enforceable at all: liability must attach to a legal person. But it has a structural consequence that is rarely stated: **the internal life of the producing organisation is outside the object of regulation**. Whether the annotation team was paid a living wage, whether the engineer had a say in the architecture, whether the deadline was feasible, whether the person who flagged the risk kept their job: none of this is a fact the Regulation asks anyone to establish.

### 3.2. Where the Act comes close, and how close

Four provisions approach the territory without entering it.

**Article 14 — human oversight with authority.** Article 14 is the strongest textual support for the thesis of this paper. It does not merely require that a human be "in the loop": it requires that oversight be *effective*, and paragraph 4 specifies that the persons assigned to oversight must have the necessary competence, training **and authority**, as well as the necessary support, and must be able to decide not to use the system, or to disregard, override or reverse its output. Read carefully, Article 14 forbids the ornamental overseer: an organisation that appoints a signatory who cannot stop the process has not implemented human oversight.

Its limit is equally clear: Article 14 protects the **operation** of a high-risk system. It says nothing about the authority of the engineer during **construction**. The act of overriding an output is regulated; the act of being overruled while designing the mechanism that produces it is not.

**Article 26(7) — information of workers.** Before putting a high-risk AI system into service at the workplace, deployers must inform workers' representatives and the affected workers that they will be subject to it, in accordance with Union and national law on information and consultation. Employment-related AI — recruitment, task allocation, monitoring, promotion, termination — is high-risk under Annex III, point 4, so this provision has real reach.

But the obligation is *information*, not negotiation, co-determination, or a veto. The reference to national information-and-consultation rules is a renvoi, not a harmonised right, and it depends entirely on the strength of the labour-law regime in each Member State. For a provision that concerns the most consequential AI deployments in most people's lives, this is a remarkably thin instrument.

**Article 27 — fundamental rights impact assessment.** The FRIA is the closest thing the Act has to a structural assessment of consequences. Its scope, however, is narrower than its reputation: it applies to deployers that are bodies governed by public law or private entities providing public services, and to creditworthiness and insurance use cases under Annex III, point 5. A **private employer** deploying Annex III, point 4 employment AI is, in principle, **not** required to perform one.

**Article 4 — AI literacy.** Providers and deployers must take measures to ensure a sufficient level of AI literacy among their staff. This is the Act's only direct engagement with the people inside the organisation. It is framed as *competence*, not as *dignity*, *voice*, or *working conditions*, and it is satisfied by training, not by governance.

### 3.3. Adjacent instruments and their boundaries

Beyond the AI Act, four instruments fill parts of the gap:

- **Directive (EU) 2024/2831 on platform work** is the only EU text that regulates *algorithmic management as a labour question*: transparency of automated systems, human oversight and human review of automated decisions, and information and consultation of platform workers' representatives. Its limitation is jurisdictional rather than conceptual — it covers platform workers, not the employees of AI-producing organisations.
- **Article 22 GDPR** grants the individual right not to be subject to a decision based solely on automated processing with legal or similarly significant effects. It protects the *data subject* before the algorithm; there is no equivalent provision protecting the *person who built* the algorithm.
- **Council of Europe Framework Convention on AI (CETS No. 225)** frames the field in human-rights terms, which is the vocabulary in which "the expert had no voice" is a governance failure rather than a management preference. It is a treaty of general principles, not a labour instrument.
- **ILO Declaration on Fundamental Principles and Rights at Work** (1998, amended 2022) supplies the oldest and most robust floor: freedom of association, collective bargaining, and — since 2022 — a safe and healthy working environment. It is binding on members as constitutional commitments, not as operational AI obligations.

| Condition (Section 4) | AI Act | Adjacent instruments | Coverage |
| --- | --- | --- | --- |
| C1 Participatory problem definition | Art. 14 (operation only) | — | **Partial / out of scope** |
| C2 Transparency of conditions | Art. 4 (competence only) | CETS 225 (general) | **Weak** |
| C3 Recognition of invisible labour | Arts. 10, 11, 12 (data, docs) | ILO, EPSR | **Indirect** |
| C4 Benefit sharing | — | EPSR (programmatic) | **None** |
| C5 Protected voice | Art. 26(7) (information) | Dir. 2024/2831, ILO C87/C98 | **Partial, sector-bound** |

The table is the core legal finding of this paper: not that European law is silent, but that it is **silent at exactly one altitude** — the organisation that builds the system.

## 4. Ethics as infrastructure

### 4.1. Definition

> **Ethics as infrastructure** is the set of structural conditions in an organisation that make it possible for the people who construct an AI system to exercise judgment, to be recognised for it, and to report what they know — and that remain true when the deadline, the client, or the hierarchy makes them inconvenient.

The metaphor is deliberately engineering-flavoured, and it is meant literally. Infrastructure has four properties that distinguish it from decoration:

1. It is **built before the thing it supports**.
2. It is **load-bearing**: removing it causes collapse, not inconvenience.
3. It is **invisible until it fails**.
4. It is **verified by inspection, not by assertion**.

A plaque in a lobby fails all four tests. It is applied after construction, it supports nothing, it is visible precisely because it does nothing, and nobody inspects it.

### 4.2. The five conditions

The definition is operationalised as five conditions, each of which admits evidence.

**C1 — Participatory problem definition.** The people who will implement the system participate in defining the problem before requirements are fixed. *Evidence:* named participants, dated decision records, and at least one documented instance in which a technical objection changed the requirement.

**C2 — Transparency of conditions.** The conditions of the work (contract, remuneration basis, allocation of liability, ownership of the output) are known to the people doing it before they begin, and changes are renegotiated rather than announced. *Evidence:* the actual contract or statement of work, and the change log.

**C3 — Recognition of invisible labour.** Data annotation, evaluation, red-teaming, documentation and maintenance are attributed, compensated and career-counted. *Evidence:* the remuneration and attribution policy applied to those roles, plus the data-governance documentation required by Article 10.

**C4 — Benefit sharing.** The distribution of the value created — equity, royalties, licensing, or equivalent — is defined ex ante rather than asserted ex post. *Evidence:* the instrument that defines it.

**C5 — Protected voice.** A person can raise a technical or ethical objection without retaliation, through a channel that is independent of the person whose decision is being questioned. *Evidence:* the channel, its independence, and anonymised statistics on objections raised and outcomes.

C5 is the condition most often confused with culture. Culture is what people believe about speaking up; C5 is what happens to them when they do. The distinction is testable, and it is the one that Article 14 approaches but does not reach.

### 4.3. Why this is not a welfare argument

The claim is not that ethical build conditions are *nicer*. It is that they are **epistemically superior**. Systems fail on information: the person who knows the data is wrong, the benchmark is contaminated, or the schedule is impossible is typically not the person with the authority to stop. Every condition above is a mechanism for moving local knowledge to where decisions are taken. That is why hierarchies that withhold authority from experts produce systems that are simultaneously more fragile, less secure, and more expensive — the defects are paid for later, as incidents and rework.

## 5. Discussion: the cost of the gap

The practical consequence of Section 3 is that a fully conformant high-risk AI system, with complete technical documentation, a risk-management file, logging, an overseer with nominal authority, and workers informed as required by Article 26(7), can still have been built in conditions that no ethics framework would endorse. Conformity is a statement about the *artefact*. It is not a statement about the *process that produced the artefact*, and the two can diverge arbitrarily.

Two objections deserve a response.

**"Labour law already covers this."** Partly — where labour law is strong, and where the people building the system are employees within its jurisdiction. Neither holds generally: AI supply chains cross borders, and a significant share of annotation and evaluation work is performed by contractors, crowdworkers, or subsidiaries outside the reach of the deploying organisation's obligations.

**"Voluntary instruments are sufficient."** This is precisely the position Wagner (2018) identified as ethics-washing. A voluntary instrument is defensible only if it is *falsifiable*: if an auditor can look at the evidence and conclude that a claim is false. The BCD in Section 6 is designed under that constraint.

## 6. The Build-Conditions Disclosure

### 6.1. Specification

The BCD is a single-page disclosure, completed per system, containing eight items. Each item requires an artefact or a named responsibility — never a statement of intent.

| # | Item | Required evidence | Maps to |
| --- | --- | --- | --- |
| 1 | Problem definition participants | Names/roles + dated decision record | C1 |
| 2 | Instances of technical objection upheld | Count and summary, anonymised | C1, C5 |
| 3 | Contractual conditions of build | Statement of work or equivalent | C2 |
| 4 | Attribution and pay of data work | Policy + applied example | C3 |
| 5 | Benefit-sharing instrument | Equity/royalty/licence clause | C4 |
| 6 | Escalation channel and its independence | Channel owner + reporting line | C5 |
| 7 | Outcome statistics of objections | Raised / upheld / retaliation cases | C5 |
| 8 | Overseer authority in practice | Nomination + documented override | Art. 14 |

Item 8 exists to make the Article 14 requirement concrete: not "an overseer was appointed", but "an overseer exercised authority, and here is the record".

### 6.2. Integration without new legislation

The BCD does not require a new regulation, and proposing one would be the weakest possible move: the gap is not primarily one of missing text but of missing *practice*. Three existing hooks are sufficient:

1. **Article 27 FRIA.** Where a FRIA is required, the BCD is a natural annex: rights impacts and build conditions are two views of the same organisation. Where the FRIA is *not* required — notably the private employer case identified in Section 3.2 — adopting the BCD voluntarily is the only available substitute.
2. **Article 95 codes of conduct.** For systems outside the high-risk scope, a code of conduct that commits to BCD disclosure converts a voluntary declaration into an auditable commitment.
3. **ISO/IEC 42001.** An AI management system provides the documented process container: the BCD becomes evidence inside an existing audit cycle rather than a new ceremony.

### 6.3. Failure modes

A disclosure instrument has three predictable failure modes, and each needs a structural answer rather than a good intention.

- **Self-reporting bias.** Answered by requiring artefacts — contracts, logs, counts — instead of prose, and by sampling: an auditor verifies two items in depth, chosen at random.
- **Gaming by aggregation.** Answered by per-system disclosure; organisation-level averages are exactly where bad conditions hide.
- **Weaponisation against individuals.** Answered by anonymisation at item level and by publishing only aggregate outcome statistics for items 2 and 7.

## 7. Limitations

First, the paper's evidentiary base is practitioner experience and doctrinal reading; it does not measure the distribution of build conditions across a sample of organisations. A survey using the eight BCD items would be the natural empirical follow-up, and the instrument is specified precisely so that it can be tested.

Second, the BCD is voluntary, and Section 6.3 does not eliminate the ethics-washing risk identified by Wagner — it only raises its cost. Nothing in this paper substitutes for binding obligations on the *build* side of AI production; what it offers is a mechanism that works before such obligations exist.

Third, the legal reading is time-sensitive. The AI Act's high-risk obligations for Annex III systems began to apply on 2 August 2026, and a legislative proposal tabled in late 2025 would defer parts of that timetable. Article-level analysis should be re-verified against the consolidated text in force at the moment of use.

Fourth, the five conditions are necessary, not sufficient. An organisation can satisfy all five and still build a harmful system; the conditions govern *how* the system is produced, not *whether* it should be.

## 8. Conclusion

The European regulatory stack now covers model behaviour, data, documentation, oversight and post-market monitoring. It does not cover the conditions in which AI systems are built, and the provisions that come closest — Article 14 on oversight authority, Article 26(7) on worker information, Article 27 on rights impact, Article 4 on literacy — stop at the boundary of the producing organisation, or stop at information rather than participation.

The contribution of this paper is not a new principle. It is a **precise statement of the gap and a falsifiable instrument for closing it voluntarily**: five structural conditions, eight disclosure items, three integration paths, and an explicit account of the ways the instrument can fail. Ethics that exists only as a document is decoration; decoration can be removed without consequence, which is exactly how one recognises it. Infrastructure cannot — and that is the whole difference.

## References

1. Council of Europe. *Framework Convention on Artificial Intelligence and Human Rights, Democracy and the Rule of Law*, CETS No. 225. Opened for signature 5 September 2024.
2. Crawford, K. *Atlas of AI: Power, Politics, and the Planetary Costs of Artificial Intelligence.* Yale University Press, 2021.
3. European Parliament and Council. *Directive (EU) 2024/2831 on improving working conditions in platform work.* Official Journal of the European Union, 2024.
4. European Parliament and Council. *Regulation (EU) 2016/679 (General Data Protection Regulation).* Official Journal of the European Union, 2016. In particular Article 22.
5. European Parliament and Council. *Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (Artificial Intelligence Act).* Official Journal of the European Union, 2024. Articles 4, 9, 10, 11, 12, 14, 26, 27, 95, 99, 113; Annex III.
6. European Parliament, Council and Commission. *European Pillar of Social Rights.* Official Journal of the European Union, C 428, 2017.
7. Friedman, B., & Hendry, D. G. *Value Sensitive Design: Shaping Technology with Moral Imagination.* MIT Press, 2019.
8. Gray, M. L., & Suri, S. *Ghost Work: How to Stop Silicon Valley from Building a New Global Underclass.* Houghton Mifflin Harcourt, 2019.
9. International Labour Organization. *Declaration on Fundamental Principles and Rights at Work.* 1998, amended 2022.
10. International Organization for Standardization. *ISO/IEC 42001:2023 — Information technology — Artificial intelligence — Management system.* 2023.
11. Jiménez Gómez, F. J. *Operational Algorithmic Ethics: From Principles to Practice.* LAIA Whitepapers, 2024.
12. Jiménez Gómez, F. J. *Governance of Autonomous Systems: A Framework for Accountability.* LAIA Whitepapers, 2024.
13. Jiménez Gómez, F. J. *Collaborative Operational Framework: Human-AI Synergy Across the Neptuno Network.* LAIA Whitepapers, 2026.
14. Jiménez Gómez, F. J. *Working as Equals: Ethics as Infrastructure, Not Decoration.* jimenezgomez.org, 2026.
15. National Institute of Standards and Technology. *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1. 2023.
16. OECD. *Recommendation of the Council on Artificial Intelligence*, OECD/LEGAL/0449. 2019, amended 2024.
17. Roberts, S. T. *Behind the Screen: Content Moderation in the Shadows of Digital Labour.* Yale University Press, 2019.
18. Shneiderman, B. *Human-Centered AI.* Oxford University Press, 2022.
19. UNESCO. *Recommendation on the Ethics of Artificial Intelligence.* Adopted 23 November 2021.
20. Wagner, B. *Ethics as an Escape from Regulation: From "Ethics-Washing" to Ethics-Shopping?* In *Being Profiled: Cogitas Ergo Sum*, Amsterdam University Press, 2018.

---

*Published by BRISECOM SL · Valencia, Spain · Licensed under CC BY-NC-SA 4.0 unless otherwise noted. Intellectual property of the methods described herein belongs to Francisco Javier Jiménez Gómez.*
