---
title: "Contract-First, Interface-Agnostic Design: The Operation as the Unit of Software Architecture"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-10-23
version: "1.0"
status: "Draft"
tags: ["software architecture", "contract-first design", "hexagonal architecture", "Unix philosophy", "API design", "separation of concerns"]
keywords: ["contract-first", "interface-agnostic", "ports and adapters", "operation contract", "error taxonomy", "Unix philosophy", "CLI", "API design"]
license: "CC BY-NC-SA 4.0"
---

# Contract-First, Interface-Agnostic Design: The Operation as the Unit of Software Architecture

## Abstract

Most software is organised around its **interfaces**. A command-line tool becomes a set of commands, a web
service becomes a set of endpoints, a desktop application becomes a set of screens. When a second interface is
needed — an API, a library, a GUI, a plugin — the usual response is to build it as a layer over the first,
producing adapters over adapters and business logic distributed across presentation code.

This paper proposes an alternative organising principle: **the operation is the unit of architecture, and the
interface is an adapter over it.** An operation is defined by its name, its input, its output and its complete
error taxonomy; once that contract exists, any number of interfaces can implement it without knowing about each
other.

The claim is deliberately modest in novelty and strong in consequence. The constituent ideas are established —
Unix philosophy, hexagonal architecture, explicit data contracts, file-based persistence. What is proposed is
their **ordering**: contract before interface, not interface before contract. The paper argues that this
ordering is what determines whether a second interface is cheap or catastrophic, and that the difference is
observable within a year of any project that grows past its first interface.

## 1. The problem: interface-first design

Interface-first design is not a mistake anyone makes deliberately. It is what happens when the first
requirement arrives as an interface: *"build a command to do X"* produces a command; *"build an endpoint
for Y"* produces an endpoint. The program is then organised around the shape of that first requirement, and the
business logic accretes around it — in the command's argument parsing, in the endpoint's request handling, in
the screen's event handlers.

The symptoms appear later and are recognisable:

| Symptom | What it indicates |
|:---|:---|
| A second interface requires rewriting the logic | The logic lives in the first interface |
| Adapters layered on adapters | Each new interface wraps the previous one rather than the operation |
| Business rules duplicated across entry points | No single place where a rule lives |
| Error handling differs by entry point | Errors are defined per interface, not per operation |
| Testing requires the interface | The operation cannot be exercised directly |

The cost is not aesthetic. **Every additional interface multiplies the surface where the same rule must be
implemented correctly**, and the number of places a rule can be wrong is the number of places it will be wrong.

There is a specific and underappreciated consequence: **interface-first design makes the software hard to
reason about**, because there is no level at which "what the program does" is written down. What exists is a
set of interfaces that each do something similar. Answering "what does this system do" requires reading all of
them and inferring.

## 2. The proposal

> **Define the operation and its input/output contract first. Make every interface an adapter over it.**

An operation is specified by four things, and only four:

1. **Name** — a stable identifier for the operation, independent of how it is invoked.
2. **Input** — the complete set of parameters, their types and their constraints.
3. **Output** — the complete shape of a successful result.
4. **Errors** — the **complete** taxonomy of ways it can fail.

The fourth is the one most often omitted and the one that does most of the work. An operation whose error
taxonomy is incomplete is not a contract; it is a hope. If the contract says an operation returns one of four
named errors, then every interface must be able to express those four, and **the caller's handling logic is
written once** rather than guessed per interface.

### 2.1. A worked example

Consider a secret-retrieval operation. The interface-first version starts with the command:

```
secrets get brisecom/ovh
```

The contract-first version starts with:

```
Operation: secrets.get
Input:   path        string, required, form "<namespace>/<name>"
Output:  name        string
         type        string
         content     string
         metadata    object
Errors:  NOT_FOUND
         ACCESS_DENIED
         DECRYPTION_FAILED
```

From that contract, every interface is a **translation**, not an implementation:

| Interface | Form | Work required |
|:---|:---|:---|
| CLI | `secrets get brisecom/ovh` | Argument parsing → contract input |
| HTTP | `GET /v1/secrets/brisecom/ovh` | Path parsing → contract input; contract output → JSON; errors → status codes |
| Library | `secrets.get("brisecom/ovh")` | Type mapping only |
| GUI | A tree: `Secrets → brisecom → ovh` | Widget → contract input |

**The mapping is mechanical in every case**, and that is the test of whether the contract is right. If
implementing a new interface requires deciding business logic, the contract is incomplete.

### 2.2. The error taxonomy as the sharpest test

The HTTP mapping deserves specific attention because it is where interface-first design most visibly fails.

Under interface-first design, error handling is invented per endpoint, and the same logical failure gets
different status codes in different places. Under contract-first design, the operation declares its errors and
the mapping is a table:

```
NOT_FOUND         → 404
ACCESS_DENIED     → 403
DECRYPTION_FAILED → 500   (a server-side condition, not a client error)
```

A mapping table that is hard to fill in is diagnostic: **it means the operation's errors were designed for one
interface.** If `DECRYPTION_FAILED` has no sensible status code, either the operation is wrong or the HTTP
interface is being asked to express something it cannot — and both are worth knowing before the code exists.

## 3. The intellectual lineage, and what is actually new

Honesty about provenance matters here, because most of this paper is not new:

| Element | Source |
|:---|:---|
| Small operations with explicit inputs and outputs | Unix philosophy |
| Logic separated from transport | Hexagonal architecture (ports and adapters) |
| Interface as translation rather than implementation | Separation of concerns |
| Explicit structured contracts | Contract-first API design, schema-first tooling |
| State in files, readable by any interface | Unix text-as-interface convention |

**What this paper adds is an ordering rule**: contract before interface, with the contract expressed in terms
of operations rather than resources, endpoints or commands. Hexagonal architecture says *separate* domain from
transport; it does not say *what unit* the domain is organised in. Contract-first API design says *define the
schema first*; it defines schemas for messages, not operations with error taxonomies.

The consequence of that difference is practical: a resource-oriented contract naturally becomes
`GET /things/{id}`, which is an interface wearing a contract's clothes. An **operation**-oriented contract has
no HTTP in it at all, and can therefore be implemented by a shell command with equal fidelity.

**The proposal is a combination, and combinations are legitimate contributions.** What is not legitimate is
presenting a combination as an invention, which is why the table is here rather than buried.

## 4. Consequences

**Second interfaces become cheap.** This is the headline consequence and the one that justifies the ordering.
The cost of interface *n+1* is the cost of a translation, not the cost of a reimplementation.

**Tests target the operation.** An operation can be exercised without any interface, which means the test suite
does not depend on the transport and does not need rewriting when the transport changes. This is the
practical difference between a test suite that survives a refactor and one that is a refactor.

**The system becomes describable.** "What does this program do" has an answer: a list of operations. That list
is documentation that cannot drift from the code, because it *is* the code's organising structure.

**The contract becomes the review artefact.** Reviewing a change becomes reviewing a contract change: what
operation, what input, what output, which errors. Reviews become smaller and more meaningful, because a
contract violation is visible in a diff.

**And a cost, stated honestly:** this style imposes upfront work. Writing a contract before knowing whether the
operation is worth building is speculative design, and speculative design is a well-documented failure mode.
The rule is therefore conditional: **contract-first pays when a second interface is plausible, and costs when
it is not.** Deciding that is judgement, not method.

## 5. Limits and failure modes

**It degenerates into ceremony.** An operation contract per trivial operation produces a catalogue of
one-line contracts that nobody reads. The unit should be the smallest thing that has a meaningful error
taxonomy; below that, the contract is overhead.

**It can freeze the wrong abstraction.** A contract is a commitment. Publishing a bad contract is worse than
having no contract, because clients will depend on it and the cost of correction rises with adoption. Contracts
should be versioned and treated as public API even when they are internal.

**It does not solve distribution.** Contract-first design says nothing about what happens when operations must
be composed across a network, where latency, partial failure and ordering become first-class. The contract
makes the *interface* clean; it does not make a distributed system correct.

**It can be read as a rejection of frameworks.** It is not. A framework can implement an interface; the claim
is only that the framework should not be where the operation lives.

**The strongest objection:** that the ordering is a matter of taste, and that a disciplined interface-first
codebase with good separation achieves the same thing. This is partly true, and the paper's answer is that
**discipline is not transferable while structure is** — a rule about where logic lives survives a change of
team; a convention about where logic lives usually does not.

## 6. Conclusion

The claim in one sentence: **the operation, not the interface, is the unit around which software should be
organised — and the test of whether it is, is how much thought a new interface requires.**

If adding an interface is mechanical, the architecture is right. If adding an interface requires deciding what
the software does, then the interface was the architecture, and the second interface is where that becomes
expensive.

## References

1. Jiménez Gómez, F. J., *From Unix Commands to APIs: Designing Software Around Contracts, Not Interfaces*,
   7 September 2026 — the original post this paper formalises.
   <https://jimenezgomez.org/posts/2026-09-07-contract-first-interface-agnostic-design/>
2. Cockburn, A., *Hexagonal Architecture (Ports and Adapters)*.
3. Raymond, E. S., *The Art of Unix Programming* — the Unix conventions on small tools and text as interface.
4. Brisecom, *Clean Software, Clean Work: Unnecessary Dependency as a Single Problem in Two Layers* (WP 15) —
   the companion argument on interface-agnosticism as an anti-dependency property.
   <https://github.com/javi-jimenez/laia/blob/main/whitepapers/clean-software-clean-work-dependency.md>
5. Brisecom, *ACS: An Assistant Context Standard* (WP 01) — an applied instance of explicit contracts.
   <https://github.com/javi-jimenez/laia/blob/main/whitepapers/acs-assistant-context-standard.md>
