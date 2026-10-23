---
title: "Clean Software, Clean Work: Unnecessary Dependency as a Single Problem in Two Layers"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-10-23
version: "1.0"
status: "Draft"
tags: ["clean software", "professional autonomy", "exitability", "dependency", "open standards", "labour relations", "vendor lock-in"]
keywords: ["clean software", "vendor lock-in", "exitability", "professional autonomy", "open standards", "dependency audit", "portability"]
license: "CC BY-NC-SA 4.0"
---

# Clean Software, Clean Work: Unnecessary Dependency as a Single Problem in Two Layers

## Abstract

Free and open-source licences answer a question about **rights**: may I inspect, modify and redistribute this software? They do not answer a different question, which is frequently more consequential in practice: **how much of my environment does this software take with it?**

This paper proposes *clean software* as a property independent of licence — software that does not introduce unnecessary dependency on a vendor, platform, account, store or ecosystem — and gives it an operational test of nine questions that any user can apply without reading a licence. It then argues that the same property applies, unchanged in structure, to **working relationships**, where it appears as *exitability*: what a person gives, receives, retains, and what happens to their professional life when the relationship ends.

The central claim is that these are not two topics joined by analogy. They are **one property measured in two layers**, and the same audit produces both. The paper is explicit about what it does not claim: clean software is not inherently better software, dependency is not automatically harmful, and the test is a diagnostic instrument rather than a scoring system.

## 1. The gap licences leave

The software-freedom debate has a well-developed vocabulary for rights and a thin one for consequences. A licence tells you what you are *permitted* to do. It says nothing about what remains possible when the vendor changes direction, the account is closed, the store removes the application, the API is deprecated, or the company ceases to exist.

These are not hypothetical conditions. They are the ordinary life cycle of commercial software, and they are precisely the conditions under which the answer to "may I?" becomes irrelevant, because the question has become "can I?".

The distinction matters because the two questions can diverge in both directions:

- Software can be **free and open source and still deeply entangled** — a permissively licensed client that is only useful against one proprietary service is free in the licence and dependent in the architecture.
- Software can be **proprietary and still clean** — a self-contained commercial tool that reads and writes documented formats, runs locally, and leaves nothing behind imposes no dependency that outlasts its usefulness.

A licence cannot distinguish these two cases. That is the gap this paper addresses.

## 2. Definition

**Clean software** is software that does not unnecessarily make external dependencies part of the user's environment — where *dependency* is any requirement without which the user's own data, workflows or continuations stop working.

Three words in that definition carry the weight:

**Unnecessary.** Dependency is not inherently bad. A dependency that buys something the user wants — a network effect, a regulatory guarantee, professional support — is a trade, not a defect. The defect is dependency that is *incidental*: present because of how the software was built, not because of what the user asked for.

**Environment.** The unit of analysis is not the application but the user's computing environment: their files, their formats, their ability to continue working. Software that keeps its dependency inside itself is clean; software that exports its dependency into the user's environment is not.

**Continuation.** The relevant horizon is not "does it work today" but "does it still work when the other party stops". A dependency only becomes visible at the moment it is exercised, which is exactly when it is most expensive to discover.

The asymmetry to note: **the vendor experiences the dependency as an asset and the user experiences it as a liability.** Both are describing the same structure. Any definition that does not acknowledge this will be written from one side only.

## 3. An operational test

A property is only useful if it can be checked. The following nine questions can be answered by a user in minutes, without legal training and without reading a licence:

| # | Question | What a "no" reveals |
|:--|:---|:---|
| 1 | Can I run it locally? | The tool exists only as a service; the vendor is a precondition |
| 2 | Can I use it without creating an account? | Identity is coupled to function |
| 3 | Can I install it without a particular store? | Distribution is a chokepoint |
| 4 | Can I keep using it if the vendor disappears? | There is no fallback state |
| 5 | Can I export my data? | The data is held, not owned |
| 6 | Are the formats documented? | Reversibility depends on the vendor's goodwill |
| 7 | Can another application read my data? | Interoperability is absent by design |
| 8 | Can I replace one component without replacing the ecosystem? | The parts are not separable |
| 9 | Does it work *with* the Internet, or does it *require* the Internet? | Connectivity has been converted from convenience to condition |

These questions are **diagnostic, not normative**. A single "no" does not condemn the software; it identifies where the exit cost lies. A tool may legitimately score "no" on several and still be the right choice — but the user should know which ones, before rather than after.

The test is deliberately answerable by non-specialists. This is the main design constraint: a criterion that requires expertise to apply will be applied only by experts, which is to say, rarely, and by the party with the least interest in the answer.

## 4. The same structure in working relationships

Now consider a working relationship and ask the equivalent question: **how much unnecessary dependency does it introduce into a person's professional life?**

The parallel is not decorative. The failure modes are structurally identical:

| Software dependency | Professional dependency |
|:---|:---|
| Vendor | A single employer |
| Cloud platform | An organisational structure |
| Account | A professional identity defined by the organisation |
| Proprietary API | Company-specific tools and internal processes |
| A non-replaceable ecosystem | Income from one relationship only |
| Undocumented format | Knowledge that cannot be reused independently |
| Vendor-controlled exploitation | Creations whose exploitation someone else controls |

In both layers the dependency is invisible while it functions, becomes visible when exercised, and is most expensive at that moment. In both layers, dependency may be a deliberate trade — job security, training, infrastructure, opportunity — and is not a defect for being one.

What transfers is therefore not a metaphor but a **method**: the same audit, with the nouns changed.

## 5. Exitability

The professional version of the nine questions is a five-part audit, run from the person's side:

**1. What am I giving?** Time, expertise, intellectual property, availability, professional reputation.
**2. What am I receiving?** Money, security, training, infrastructure, opportunity, social protection.
**3. What do I retain?** Knowledge, portfolio, professional identity, intellectual property, the ability to work elsewhere.
**4. What happens when I leave?** Can I continue the career, show the work, use the general experience, work with other clients, keep the professional identity?
**5. What does the other party control?** Schedule, priorities, methods, creations, continuation.

The operative concept is **exitability**: not whether leaving is permitted — nearly every arrangement permits it on paper — but whether leaving is *survivable* in practice, with career, portfolio and identity intact.

This reframing matters because the usual question, "is this a good job?", is unanswerable in the abstract and therefore never answered honestly. Exitability is answerable, and it is answerable *before* signing rather than after leaving.

**Exitability is not loyalty's opposite.** A relationship with high exitability can be long, deep and committed, because commitment chosen from a position of possibility is worth more than commitment produced by the absence of alternatives. What exitability removes is not commitment; it is captivity misdescribed as commitment.

## 6. Why the two layers are one

Three arguments support treating this as a single property rather than two analogies.

**First, one author, one criterion.** The professional formulation was derived from the software formulation by substituting nouns, not by independent inquiry. Where two frameworks share a derivation, presenting them as separate contributions manufactures a distinction that does not exist.

**Second, the same actor is on both sides.** The party that designs software dependency and the party that designs contractual dependency are frequently the same organisation, using the same reasoning: reduce the cost of switching, increase the cost of leaving. Treating the layers separately allows that reasoning to be applied twice while being named once.

**Third — and this is the practical argument — the audit is more useful unified.** A person assessing a tool and a contract runs one audit and gets two answers. Split into two frameworks, the audit is run once, on whichever layer the reader happens to be thinking about, and the other layer is left unaudited.

## 7. Objections

**"This is just vendor lock-in under another name."** Partly. Lock-in names the *state*; clean software names the *property that avoids it* and provides the test. More importantly, lock-in is normally discussed only for software, and this framework's claim is that the same test applies to employment. That extension is the contribution; the software half is a restatement.

**"Autonomy is a luxury of the already-secure."** Largely true, and it should be said plainly rather than avoided. A person choosing between two offers does not have the same room to apply an exitability audit as a person with savings and a client base. The audit is not neutral with respect to bargaining power, and presenting it as though it were would be dishonest. What the audit can do for the weaker party is make the cost of a decision visible *before* it is taken, which is not nothing, but is not the same as having a choice.

**"Clean software is a purity test in disguise."** It is a risk when used as a score. The nine questions produce a profile, not a verdict, and this paper's position is that a tool failing six of nine can be the correct choice if the dependencies are priced correctly. The failure mode is not using the test; it is using it as a substitute for judgement.

**"Systems are interdependent by definition. Nothing is clean."** Correct, and the definition was written to accommodate it: *unnecessary* dependency, not *any* dependency. What is being criticised is dependency that arrives without being chosen and cannot be removed.

## 8. Limitations

The framework is a **diagnostic instrument**, not a measurement. It produces an ordinal profile of where dependencies sit; it does not produce a number that can be compared across tools or across jobs. No such number is proposed here, because the weighting would be arbitrary and would be mistaken for objectivity.

The nine software questions were assembled from practice, not derived from a theory of dependency, and they do not partition the space: several overlap, and there are surely dependencies no question catches.

The professional half rests on **one practitioner's model** and has not been tested across a population. It is offered as a usable audit, not as an empirical finding, and the difference should be kept visible.

Finally: this paper is written by a party with an interest. The author runs a company whose structure is, in part, an application of the framework. That does not invalidate the argument, but a reader is entitled to weigh it, and the argument should be strong enough to survive the disclosure rather than the disclosure being used to substitute for it.

## 9. Conclusion

Licences answer what you may do; they do not answer what remains possible. Clean software is the second question asked of software, and exitability is the same question asked of a working relationship — the same property, in two layers, measured with one audit.

The claim is deliberately narrow. Not that dependency is bad, but that **unnecessary** dependency should be identified before it is exercised rather than after; not that autonomy is achievable, but that its cost can be estimated in advance; not that a criterion replaces judgement, but that judgement is better made with the dependency map visible.

**The software should serve the user's environment, rather than turning the user's environment into an extension of the vendor's ecosystem.** The same sentence holds with one word changed, and that is the whole argument: *the work should serve the worker's professional life, rather than turning the professional life into an extension of the employer's organisation.*

## References

1. Brisecom, *Clean Software: Beyond Free and Open Source*, 1 October 2026. <https://brisecom.org/blog/clean-software/>
2. Brisecom, *Clean Worker: Beyond Employment and Professional Dependency*, 1 October 2026. <https://brisecom.org/blog/clean-worker/>
3. Free Software Foundation, *GNU General Public License v3.0* — the freedoms this paper takes as given and does not restate.
4. Open Source Initiative, *The Open Source Definition*.
5. Brisecom, *Year Zero: What a Company With Large Ambitions Actually Costs to Keep Alive*, 23 October 2026. <https://github.com/javi-jimenez/laia/blob/main/whitepapers/brisecom-year-zero-subsistence-threshold.md> — the structural application of §5 to a company of one.
