---
title: "ACS: An Assistant Context Standard for Persistent, Traceable AI Memory"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2025-12-30
version: "1.0"
status: "Draft"
tags: ["AI", "memory", "context", "standard", "traceability", "LLM", "ACS"]
keywords: ["assistant context", "axioms", "inferences", "persistent memory", "hallucination", "traceability"]
license: "CC BY-NC-SA 4.0"
---

# ACS: An Assistant Context Standard for Persistent, Traceable AI Memory

## Abstract

Large language models (LLMs) operate within ephemeral context windows that are reset between sessions, producing a characteristic "amnesia effect" that undermines continuity, reproducibility, and trust in AI-assisted workflows. This paper introduces the **Assistant Context Standard (ACS)**, a lightweight, human- and machine-readable specification for persistent structured memory that separates user-defined facts (Axioms) from machine-derived reasoning (Inferences). The standard provides a minimal contract for AI-assisted collaboration, enabling traceable reasoning, reduced hallucination, and reproducible decision-making across sessions, agents, and environments. We present the logical segmentation architecture, a reference file format, and a protocol for controlled promotion of validated inferences into axioms.

## 1. Introduction

The integration of AI assistants into engineering, research, and decision-making workflows has exposed a fundamental limitation: the absence of persistent, structured memory. When an assistant and a human work iteratively on a repository or task, the assistant frequently loses critical context upon engine or interface changes, leading to repeated explanations, conflicting decisions, and an inability to audit *why* a particular conclusion was reached.

This "amnesia effect" is not merely an inconvenience; it undermines the reliability of AI as a decision-support system. In high-stakes domains—geopolitics, investment, defense, and complex engineering—the inability to separate *facts* from *assumptions* creates a material risk of hallucinated or unjustifiable outputs.

The **Assistant Context Standard (ACS)** addresses this gap by defining a minimal, standard file that captures the essential state of an AI-assisted collaboration. Its core design principle is the **separation of Axioms from Inferences**: the human dictates reality; the machine processes possibilities.

## 2. Motivation and Problem Statement

### 2.1 The Amnesia Effect

Current AI systems operate in ephemeral memory silos (context windows). When a session ends, the model loses:

- The project's goals and constraints;
- Decisions already made and rejected;
- Domain-specific terminology and their definitions;
- The rationale behind prior outputs.

This forces users to re-establish context repeatedly, wastes effort, and introduces inconsistencies.

### 2.2 Hallucination and Lack of Traceability

Without an explicit distinction between user-provided facts and model-generated reasoning, two failure modes emerge:

1. **Fact fabrication:** The model invents data that contradicts user-defined reality.
2. **Untraceable reasoning:** The model cannot justify *which specific premise* led to a conclusion, making audit impossible.

## 3. The ACS Framework

### 3.1 Logical Segmentation Architecture

The ACS framework is based on a tripartition of information, separating concerns across three logical layers:

#### A. Axiom Layer (Control Document)

- **Definition:** Immutable facts and control rules dictated by the user.
- **Function:** Acts as the "DNA" of the context. If a fact is not in the Axiom layer, it does not exist for the AI.
- **Protocol:** Includes general bases (BH-GEN) and domain-specific research bases (e.g., BH-INVESTIGATION).

#### B. Process Layer (AI)

- **Definition:** The logical reasoning engine.
- **Function:** Applies the Axioms to solve problems without contaminating the original database.

#### C. Inference/Hypothesis Layer (Results Document)

- **Definition:** The "output" of the system.
- **Function:** Records analysis, findings, and suggestions. This data is provisional until the user validates it and promotes it to the Axiom layer.

### 3.2 Reference File Format

The standard proposes a manifest file (e.g., `ASSISTANT_CONTEXT.md`, `.ai-context.yaml`, or `.assistant.md`) located at the root of the working folder. The minimal YAML front matter includes:

```yaml
id: <unique-identifier>
created_at: <timestamp>
updated_at: <timestamp>
user: <principal>
location: <working-directory>
purpose: <mission-statement>
files_changed: <list>
next_steps: <list>
status: <state>
```

### 3.3 Extended Structure (v2.0)

For larger projects, the standard extends to include:

#### A. Task Manifest (`task_state`)

- **Current Goal:** The current macro objective.
- **Sub-tasks:** Checklist of pending and completed tasks.
- **Blocking Issues:** Technical obstacles encountered in previous sessions.

#### B. Entity Dictionary (`knowledge_graph`)

- **Definitions:** Glossary of domain-specific terms.
- **Key Files:** Mapping of critical files and their functions.

#### C. Architecture Decision Records (ADR)

- **Decisions:** Recorded decisions with rationale (e.g., "Use UUID instead of incremental ID because X") to prevent the AI from re-proposing rejected alternatives.

### 3.4 Advanced Mechanisms

1. **Inheritance Hierarchy:** Context files may be merged hierarchically (global vs. module-level), with subdirectory files taking priority. This enables "context per module."
2. **Session Signature (State Hash):** A `last_state_hash` summarizes the code/system state; significant changes trigger a request to update the manifest.
3. **Token Budget Management:** Explicit priority levels define which parts of the context may be omitted when the file grows large (e.g., old history) and which are mandatory (e.g., the current goal).

## 4. Methodology

The ACS framework is evaluated against three criteria:

1. **Continuity:** Ability to resume a task across sessions without loss of critical state.
2. **Traceability:** Ability to reconstruct the reasoning path from axioms to conclusions.
3. **Reproducibility:** Ability to reproduce a given output under the same context.

Qualitative evaluation is performed through reference implementations in AI-assisted engineering and research workflows.

## 5. Applications

### 5.1 Geopolitics and Investment

The separation of axioms from inferences allows monitoring of complex scenarios (e.g., logistics, conflict risk) with mathematical precision. For an investor, this provides full traceability: the exact axiom that drove a decision is always identifiable.

### 5.2 Software Engineering

ACS enables context-per-module, architecture decision records, and state-hash-based change detection, preventing the AI from re-proposing rejected solutions.

### 5.3 Research and Defense

In high-stakes environments, ACS provides an immutable record of reasoning, supporting audit and accountability.

## 6. Conclusion

The ACS Framework is more than a way to use AI; it is a knowledge-management standard. It enables the transition from "playing" with AI to "governing" information for critical decisions in a volatile world. By separating user-defined truth from machine-derived reasoning, ACS delivers the continuity, traceability, and reproducibility required for trustworthy AI-assisted collaboration.

## 7. Future Work

- Formal specification of the ACS schema (JSON-LD / TOML variants).
- Reference implementations and tooling.
- Versioning and signature mechanisms for axiom promotion.
- Interoperability with existing context and agent frameworks.

## References

1. Jiménez Gómez, F. J. (2025). *Proposal: ASSISTANT_CONTEXT standard for continuity between sessions*. RFC-0001.
2. Jiménez Gómez, F. J. (2026). *Unified Context Protocol for Assistants (UCPA / ACS)*. v2.0.
3. Jiménez Gómez, F. J. (2026). *Taming the Chaos of AI*.
4. Jiménez Gómez, F. J. (2026). *ACS Framework (Assistant Context Standard)*. Technical note.
