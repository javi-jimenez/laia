---
title: "Encrypted Audit Aggregation: A Specification and a Reproducible Cost Harness for Computing Over Data That Is Never Decrypted"
authors: ["Francisco Javier Jiménez Gómez"]
affiliation: "Brisecom / LAIA Project"
date: 2026-11-27
version: "1.0.2"
status: "Draft"
order: 25
topic: "Homomorphic encryption, encrypted auditing, reproducibility, pre-registration"
tags: ["homomorphic encryption", "encrypted auditing", "privacy-preserving computation", "auditability", "reproducibility", "preregistration", "cost modelling"]
keywords: ["fully homomorphic encryption", "audit trail", "aggregate queries", "operation counting", "trusted timestamping", "negative results"]
doi: "10.5281/zenodo.24582258"
license: "CC BY 4.0 (text) / Apache-2.0 (code)"
---

# Encrypted Audit Aggregation: A Specification and a Reproducible Cost Harness for Computing Over Data That Is Never Decrypted

<!-- doi:start -->
> **DOI:** [10.5281/zenodo.24582258](https://doi.org/10.5281/zenodo.24582258) · Zenodo (concept DOI [10.5281/zenodo.24581624](https://doi.org/10.5281/zenodo.24581624)) · cite this version
<!-- doi:end -->

**Author:** Francisco Javier Jiménez Gómez

**Organization:** BRISECOM SL


## Abstract

An auditor needs aggregate facts about a trail of events — how many, how often,
how severe — but the party holding the trail will not hand over the raw records,
and the auditor will not accept a number produced by a black box. Fully
homomorphic encryption (FHE) makes the computation possible in principle. It does
not answer the engineering question that decides whether a deployment is viable:
*for a given trail and a given query, how many cryptographic operations does the
answer cost, and can somebody else check that arithmetic without owning an FHE
stack?*

This paper specifies four aggregate queries over a typed audit trace, gives a
normative, fully written-down operation-count model for their homomorphic
evaluation, and publishes a dependency-free harness that reproduces the counts
and an independent plaintext oracle that fixes what "correct" means. The model's
latency component is deliberately inert: without a calibration record measured on
real hardware the harness reports `null` rather than a number, because a benchmark
whose constants are invented cannot be refuted.

The contribution is explicitly **not** the primitive. Homomorphic encryption was
proposed in 1978 and the first fully homomorphic scheme appeared in 2009; this
work assumes both. What is claimed, and timestamped, is a *design and its
evaluation protocol*: a specification with falsifiable hypotheses, a cost model
derived on paper, and a harness that lets a third party disagree with it in
minutes. The encrypted backend is a declared, documented gap — an unimplemented
function that raises rather than a stub that pretends.

## 1. The question this paper answers, and the one it does not

Two questions get confused whenever encrypted computation is discussed, and
confusing them is how a good piece of work ends up with no defensible credit:

| | **Question A** | **Question B** |
|:---|:---|:---|
| **Asks** | can we build it, and how fast is it? | what exactly is specified, and who can check it? |
| **Cost** | months, hardware, people | days, and almost nothing |
| **Decays if delayed** | not much | yes: priority belongs to whoever fixes it in public first |

This paper is about **B**, and it says so at the top. It does not evaluate a
running encrypted backend, because there is none: §7 records that as a gap
instead of hiding it behind a benchmark of something else.

The distinction matters because the failure mode on the other side is common and
expensive. A paper that claims to have *created* homomorphic encryption is
refuted in the first question of the first review. A paper that claims to have
*specified and made checkable* a design is refuted only by finding an error in
the specification — which is a much harder thing to do, and a much more useful
outcome for everyone.

## 2. Prior art, stated plainly

- **Rivest, Adleman and Dertouzos (1978)** proposed computing on encrypted data
  and named the property *privacy homomorphism*.
- **Gentry (2009)** gave the first fully homomorphic construction.
- Mature open implementations exist — **OpenFHE**, **Microsoft SEAL**, **HElib**,
  **TFHE-rs**, **Concrete** — and each carries its own parameter discipline,
  noise budget and performance envelope.
- The intellectual property landscape is dense, and the field is not one in which
  a small organisation should expect to hold blocking rights on a primitive.

Nothing in this paper competes with any of that. The contribution sits one level
up: at the level of *what a compliance-driven audit actually needs to compute*,
and *how its cost can be stated in a form that survives contact with a reviewer*.

## 3. Trust model and what is out of scope

| Actor | Holds | Trusted with |
|:---|:---|:---|
| **Trail owner** | plaintext records, secret key | everything |
| **Compute node** | evaluation key only | nothing about the plaintext |
| **Result consumer** | decryption key share | the aggregate only |

The assumed adversary is an **honest-but-curious compute node** and an observer of
the traffic. The following are explicitly **not** addressed in this version, and
their absence is a limitation rather than an oversight:

- a **malicious** node returning a wrong result (this needs verifiable
  computation, a different problem with a different literature);
- **side channels** in the implementation;
- **key compromise**;
- **differential privacy** of the released aggregate.

## 4. Data model

A trail is `n` records over a schema of typed fields:

| Kind | Parameter | Encoded as |
|:---|:---|:---|
| `category` | `domain` = number of distinct values >= 2 | one-hot over `domain` lanes |
| `integer` | `bits` from 1 to 64 | binary decomposition, `bits` lanes |
| `float` | `max_abs` > 0 | fixed-point, scaled (§6) |

Field names are restricted to valid identifiers so that the command-line tool and
the JSON interchange format cannot disagree about what a name is.

## 5. The four aggregates

Every query is a **conjunction of equality filters** plus one aggregate:

| Kind | Requires | Returns |
|:---|:---|:---|
| `count` | — | number of matching records |
| `sum` | target field, integer or float | sum of that field over matches |
| `histogram` | group-by field of kind `category` | count per value |
| `threshold_count` | integer target field, `threshold` | matches whose value >= threshold |

Filters on non-`category` fields are **rejected**, not silently approximated.
Silent approximation is how a measurement harness starts lying: the first
approximation is convenient, the second is invisible, and the third is in a
published table.

## 6. Cost model

The model counts operations **per ciphertext**, because an FHE evaluation computes
over packed slots. Let `S` be the number of slots per ciphertext (default 8192)
and `C = max(1, ceil(n/S))` the number of ciphertexts for `n` records.

**Lane reduction.** Reducing `S` lanes to one costs `R = ceil(log2 S)` rotations,
`R` additions and a multiplicative depth of 1 (a tree sum).

**Equality on a category value.** Let `b = bit_length(domain - 1)`. The equality
test costs:

| `b` | ciphertext×ciphertext mults | additions | depth |
|---|---|---|---|
| 1 | 0 | 1 | 0 |
| >= 2 | `2(b-1)` | `b` | `(b-1) + ceil(log2 b)` |

This is stated as an **upper bound for a textbook circuit on the given encoding**,
not as an optimum. §10 invites a refutation; a better circuit would be a stronger
result than this paper.

**Filter conjunction** of `k` predicates sums the per-predicate cost and, for
`k >= 2`, adds `k-1` multiplications and `ceil(log2 k)` depth.

**Aggregate terms** add, respectively: nothing for `count`; one multiplication
(mask × value) for `sum`; a binary comparison chain of depth `(b-1)+ceil(log2 b)`
for `threshold_count`; and `d` copies of the equality test plus `d-1` combiners
for a histogram of domain `d`.

**Latency is not modelled by default.** Given a calibration record measured on
real hardware — seconds per multiplication, per addition, per rotation, per
bootstrap, and the number of multiplicative levels before a bootstrap is needed —
latency is the sum over operations of (count × seconds_per_op) plus the bootstraps that depth forces.
Without that record the harness emits `"latency": null`. There is no default
timing constant anywhere in the code, because a default constant is an invented
measurement with a plausible face.

## 7. Correctness, and the gap that is declared

Correctness is defined operationally: an independent **plaintext oracle** computes
the same aggregate over the same trace, and any encrypted implementation must
agree with it. Integer aggregates must match **exactly**; a float `sum` must agree
within a relative error of `1e-6` and an absolute error of `1e-3 × max_abs`.

The encrypted backend in this version is **absent on purpose**:

```
def evaluate_encrypted(trace, query, *, library="openfhe"):
    raise NotImplementedError(...)
```

It raises with a message that names which FHE libraries were detected and what
the conformance requirement is. A stub that returns a plausible-looking number
would have been easier to write and would have made the whole deposit worthless.

Declared gaps in version 1.0.2: no encrypted backend; no calibration on real
hardware (every timing is `null`); no security parameters chosen; no
minimum-bucket suppression; malicious-node protection and differential privacy out
of scope.

> A gap that is written down can be closed and cited. A gap that is hidden becomes
> a retraction.

## 8. Residual leakage — what encryption does not fix

Even with a perfect backend, this design leaks:

1. `n`, the schema, and the number of queries issued;
2. the **query structure**, unless the query itself is encrypted (a harder,
   separate problem);
3. the **aggregate result** — and a histogram of a rare category can single out an
   individual;
4. the timing and size of ciphertexts at the compute node.

Point 3 is the one that gets people hurt in production. FHE protects the records
in transit through the computation; it does not protect a person whose row is the
only one in a bucket of size one. **A minimum-bucket-suppression rule is a
deployment requirement and is not part of this version.** Stating this here, in
the specification rather than in a footnote, is the difference between a tool and
a liability.

## 9. Reproducibility as the actual contribution

The deposit ships:

- a **normative specification** (`SPECIFICATION.md`) with every formula written
  out and every approximation labelled;
- a **pre-registration** (`PREREGISTRATION.md`) with six falsifiable hypotheses,
  decision thresholds, and a table of declared gaps, fixed before any measurement
  exists;
- an **evaluation protocol** with deviation logging;
- a **harness** of roughly 1,400 lines, standard library only, with 25 tests whose
  expected values are derived on paper from the specification rather than recorded
  from a previous run;
- a **SHA-256 manifest** of every file, and an **RFC 3161 trusted timestamp** over
  that manifest from an external authority.

The verification a third party performs requires no trust in the author:

```bash
grep -v -E "CHECKSUMS.sha256|timestamp.token" CHECKSUMS.sha256 | sha256sum -c
openssl ts -verify -data CHECKSUMS.sha256 -in timestamp/timestamp.token \
        -CAfile timestamp/freetsa-cacert.pem -untrusted timestamp/freetsa-tsa.crt
```

Two files are excluded from their own manifest, necessarily: the manifest cannot
contain its own hash, and the seal cannot contain the hash of the file it seals.
Everything else — including the timestamp authority's certificates and the
verification instructions — is covered.

The publication history is part of the record. Version 1.0.0 uploaded the papers
but **not** the manifest or the seal, so the proof pointed at a file a reader
could not obtain. Version 1.0.1 fixed that but rewrote its citation file *after*
sealing it, invalidating the seal for every subsequent reader. Version 1.0.2 is
the first in which the chain verifies end to end from the public record alone.
Both defects were mine, both were found by performing the verification as a
stranger would, and both are documented rather than quietly superseded — because
the failure mode this paper argues against is the one where a plausible artefact
is never actually checked.

## 10. How this specification can be refuted

Send a trace, a query, a slot count, and the operation counts you derive by hand,
alongside the counts the harness prints. Three outcomes are possible and all are
useful:

1. **The harness is wrong.** It gets fixed, and the fix is credited in the
   changelog.
2. **The circuit in §6 is not an upper bound** for the stated encoding. That is a
   better result than this paper, and it will be recorded as such.
3. **A prior publication already defines this exact protocol and harness.** The
   priority claim is withdrawn and replaced by a citation. Priority is a fact about
   dates, not a preference.

## 11. Applications, in order of how soon they become real

- **Auditing what cannot be read** (LAIA): aggregate statistics over the motor's
  own traces, computed by a party that never sees them.
- **Validation over a client's data** (NEPTUNO): a node checks properties and
  returns aggregates while never holding the plaintext.
- **Search over encrypted vectors**: nearest-neighbour over encrypted embeddings,
  for retrieval without exposing the corpus.
- **Graph and constraint algorithms under encryption**: the most ambitious line,
  and the one most likely to end as a poster without results.

A practical warning that belongs in any planning document: FHE is, in order of
magnitude, **three to six orders of magnitude slower** than the equivalent
plaintext operation, depending on scheme and operation. Any promise of real-time
behaviour without measured numbers is a promise that breaks in the first demo.

## 12. Conclusion

The defensible claim is narrow and it is enough:

> BRISECOM published, on 27 November 2026, a normative specification, a
> pre-registered evaluation protocol and a reproducible, dependency-free cost
> harness for aggregating audit-trail statistics over homomorphically encrypted
> data, with a trusted timestamp and a DOI: `10.5281/zenodo.24581624`.

Not the invention of the primitive; not a working encrypted implementation; not a
performance claim. The value of publishing the design *before* the implementation
is that the design can now be attacked by people who do not need permission,
hardware or an account — and being attacked in public is the only form of credit
that survives scrutiny.

## References and primary sources

1. R. L. Rivest, L. Adleman, M. L. Dertouzos. *On Data Banks and Privacy
   Homomorphisms.* Foundations of Secure Computation, 1978.
2. C. Gentry. *Fully Homomorphic Encryption Using Ideal Lattices.* STOC 2009.
3. OpenFHE — https://openfhe.org · Microsoft SEAL —
   https://github.com/microsoft/SEAL · HElib —
   https://github.com/homenc/HElib · TFHE-rs —
   https://github.com/zama-ai/tfhe-rs
4. IETF RFC 3161, *Internet X.509 Public Key Infrastructure: Time-Stamp Protocol.*
5. Deposit and harness (this paper's artefact):
   https://doi.org/10.5281/zenodo.24581624
