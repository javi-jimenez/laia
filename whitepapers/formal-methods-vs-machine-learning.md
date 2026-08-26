---
title: "Formal Methods vs. Machine Learning: Computational Cost and Truth Affinity"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2025-12-30
version: "1.0"
status: "Draft"
tags: ["formal methods", "machine learning", "verification", "computational cost", "explainability", "truth affinity", "LAIA"]
keywords: ["formal verification", "machine learning", "computational cost", "truth affinity", "hybrid systems", "explainability"]
license: "CC BY-NC-SA 4.0"
---

# Formal Methods vs. Machine Learning: Computational Cost and Truth Affinity

## Abstract

This paper compares two paradigms for building AI systems: **formal methods** (specification, verification, synthesis) and **machine learning** (ML, particularly deep learning). We introduce the concept of **truth affinity**—the propensity of a system to produce correct, justifiable, and verifiable outputs—and analyze the computational cost of each approach across three axes: initial development, training/verification, and maintenance. We also examine the factors that change the cost ratio over time and the emergence of hybrid systems that combine the strengths of both paradigms. The analysis is grounded in the LAIA project's commitment to formal, verifiable reasoning.

## 1. Introduction

In the coming generations, two paradigms will compete and complement each other:

- **Formal methods:** Systems built on mathematical logic, grammars, and automata, including model checking, formal verification, and programmatic synthesis.
- **Machine learning:** Statistical models that approximate functions from data, with probabilistic guarantees.

Each paradigm has distinct strengths and weaknesses in terms of computational cost and the ability to produce trustworthy outputs.

## 2. Truth Affinity: Definitions

**Truth affinity** is the ability of a system to produce outputs that:

1. Correspond to verifiable facts, invariants, or requirements;
2. Justify *why* the output is correct.

### 2.1 Formal Methods

- **High truth affinity** when the specification is correct and complete.
- Verification provides evidence within the formal model.
- **Risk:** If the specification is poor, the guarantees are misleading (garbage-in, garbage-out).

### 2.2 Machine Learning

- **Probabilistic affinity** dependent on data quality and coverage.
- May hallucinate or exhibit biases.
- **Limited explainability** except through XAI (explainable AI) techniques.

## 3. Computational Cost

We analyze cost across three axes: initial development, training/compiling/verification, and maintenance/adaptation.

### 3.1 Short Term (1–3 Years)

- **ML** dominates language and vision tasks.
- **Formal methods** remain in critical niches (safety-critical systems).

### 3.2 Medium Term (3–7 Years)

- Improvements in synthesis and verification reduce costs in structured domains.
- ML improves efficiency (distillation, sparsity, dedicated hardware).

### 3.3 Long Term (>7 Years)

- Hybrids emerge: specifications that guide ML; ML that suggests formal invariants.
- The cost/benefit ratio depends heavily on available hardware.

## 4. Guidance Estimates

| Approach | Development Cost | Compute Cost | Maintenance |
|----------|------------------|--------------|-------------|
| **Formal methods** | High human cost to specify | Verification can be intensive (10²–10⁴ core-seconds for non-trivial modules) | Efficient with good modularity |
| **ML** | Moderate (data labeling) | 10⁶–10⁹ GPU-seconds for large models | Continuous retraining |

## 5. Factors That Change the Cost Ratio

- **Specialized hardware** (TPU, NPU, SMT accelerators) and algorithmic advances reduce costs on both sides.
- **Data vs. specifications:** Labeled data is expensive; formally specifying properties is also costly.
- **Hybridization:** Combining paradigms can reduce total cost while improving truth affinity.

## 6. Hybrid Systems

The most promising direction is the convergence of formal methods and ML:

- **Specifications that guide ML:** Use formal constraints to constrain and validate ML outputs.
- **ML that suggests formal invariants:** Use learned patterns to propose hypotheses for formal verification.
- **Verified ML:** Apply formal verification to ML components in safety-critical contexts.

The LAIA project embodies this hybrid philosophy, grounding AI reasoning in formal logic while leveraging the scalability of modern computation.

## 7. Conclusion

Neither paradigm is universally superior. The choice between formal methods and ML—and the optimal balance between them—depends on the domain, the availability of specifications vs. data, and the required level of truth affinity. The future lies in hybrid systems that combine the rigor of formal methods with the scalability of machine learning.

## 8. Future Work

- Empirical benchmarks of hybrid systems.
- Quantification of truth affinity across domains.
- Tooling for verified ML.
- Integration with the ACS standard for traceable reasoning.

## References

1. Jiménez Gómez, F. J. (2025). *Computational cost and truth affinity: formal languages vs ML (Draft)*.
2. Jiménez Gómez, F. J. (2026). *ACS: An Assistant Context Standard*. LAIA Whitepapers.
3. LAIA Project. *Ethical Artificial Intelligence*. https://laia.brisecom.org/
