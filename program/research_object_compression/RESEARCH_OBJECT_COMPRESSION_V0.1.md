# RESEARCH_OBJECT_COMPRESSION_V0.1

**Object:** `CEREBRO_RESEARCH_OBJECT_COMPRESSION_V0.1`  
**Parent:** `program/PROGRAM_CONSOLIDATION_V0.1.md`  
**Network context:** `program/network_architecture/WARRANT_EFFECT_SEPARABILITY_V0.1.md`  
**Record type:** source-bounded research-object compression contract  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Computational kernel authorized:** `NO`  
**Propagation algebra authorized:** `NO`  
**Bulk semantic ingestion authorized:** `NO`  
**Sequential repository compression authorized:** `R01_ONLY_UNTIL_DEATH_TESTED`  
**Cerebro Step 2 reopened:** `NO`

This object constitutes the first compression boundary for the 43 pre-Cerebro research repositories.

The target is not an unconstrained summary. It is a provenance-preserving, loss-bounded node state whose retained distinctions remain reconstructible from an exact repository surface.

The governing transformation is:

\[
\boxed{
R_i@H_i
\xrightarrow{\operatorname{Compress}_{0.1}}
Z_i
}
\]

where `H_i` is an immutable repository head and `Z_i` is a derived program-level compression with zero map or scientific authority of its own.

The governing principle is:

\[
\boxed{
\textbf{Preserve what the repository actually says; do not let compression decide what the program should believe.}
}
\]

---

## 1. Developmental boundary

The frozen `PROGRAM_CONSOLIDATION_V0.1` seed explicitly left `R01-R42` semantic ingestion unopened. This successor object opens only a new **program-consolidation compression surface**, beginning with `R01` by explicit research direction.

This does not reopen Cerebro's Step 2 perceptual development.

\[
\boxed{
\text{PROGRAM CONSOLIDATION source access}
\neq
\text{Cerebro Step 2 sensory access}.
}
\]

Therefore both may remain true:

```text
PROGRAM_COMPRESSION_R01_SOURCE_ACCESS = OPEN_FOR_FROZEN_HEAD
CEREBRO_STEP_2_R01_CONTENT_ACCESS     = CLOSED
CEREBRO_STEP_2_R01_SEMANTIC_ACCESS    = CLOSED
```

No compression item becomes a Cerebro observation, evidence object, claim, or developmental feature by being stored under `program/`.

---

## 2. Repository order

Compression proceeds in the frozen chronology from `environment/ENVIRONMENT_CHRONOLOGY_V0.1.md`:

\[
\boxed{R01,R02,\ldots,R43.}
\]

The first witness is `R01` only.

No later repository is compressed under V0.1 until the R01 compression and its death test are frozen.

Chronological processing order is an execution order only. It does not create semantic, causal, dependency, support, or authority edges between adjacent repositories.

---

## 3. Frozen source surface

Before compression, each repository attempt must freeze:

```text
REPOSITORY_ID
REPOSITORY_FULL_NAME
DEFAULT_BRANCH
FROZEN_HEAD_COMMIT
FROZEN_HEAD_TREE
INCLUDED_PATHS
INCLUDED_BLOBS
EXCLUDED_PATHS
EXCLUSION_REASONS
SURFACE_COMPLETENESS
```

A compression may claim `FULL_REPOSITORY_HEAD_SURFACE` only when every path at the frozen head has been enumerated and every research-bearing text path is included or explicitly excluded with a non-semantic reason.

A moving branch name is not sufficient provenance. The immutable commit and blob identities govern.

---

## 4. Compression is not importance selection

The compressor must not ask:

> What are the important ideas in this repository?

unless a source itself explicitly supplies an importance ranking that is being preserved as source content.

Instead, the V0.1 compressor asks:

> What source-grounded research distinctions on this frozen surface must remain available so that later program-level relation extraction can reconstruct what this repository actually asserted, defined, reported, rejected, left unresolved, or explicitly referenced?

Thus:

\[
\boxed{
\text{compression}
\neq
\text{importance ranking}
\neq
\text{synthesis}.
}
\]

---

## 5. Minimal compression record

The first compression record may contain the following organizational coordinates:

```text
OBJECT_ID
REPOSITORY_ID
IDENTITY
SOURCE_SURFACE
SOURCE_DESCRIBED_STATUS
DEFINITIONS
FORMAL_STRUCTURES
ASSERTIONS_OR_HYPOTHESES
REPORTED_RESULTS
REPORTED_NEGATIVE_RESULTS
LIMITATIONS_OR_OPEN_QUESTIONS
APPLICATIONS_OR_EXAMPLES
INTERNAL_REFERENCES
EXPLICIT_CROSS_REPOSITORY_REFERENCES
UNRESOLVED_REFERENCES
NON_INFERENCES
COMPRESSION_STANDING
```

These fields are compression-level organizational coordinates only. They are not a seven-layer #44 ontology and do not amend Cerebro's constitution.

Empty arrays are allowed and often required.

---

## 6. Item provenance

Every non-empty semantic item must contain enough immutable provenance to reconstruct the source basis, including at minimum:

```text
SOURCE_REPOSITORY
SOURCE_COMMIT
SOURCE_PATH
SOURCE_BLOB
SOURCE_LOCATION_OR_EXACT_SUPPORTING_TEXT
EXTRACTION_MODE
```

For V0.1:

```text
EXTRACTION_MODE = EXPLICIT_SOURCE_CONTENT
```

for all semantic content.

No `DERIVED_RELATION`, inferred mechanism, cross-repository identity resolution, or theory synthesis is permitted in the R01 witness.

---

## 7. Required semantic separations

The compression must preserve at least the following distinctions when the source surface contains them:

\[
\boxed{
\text{definition}
\neq
\text{hypothesis/assertion}
\neq
\text{reported result}
\neq
\text{reported negative result}
\neq
\text{application/example}
\neq
\text{open question/status}.
}
\]

A mathematical definition is not converted into empirical support.

A central hypothesis is not recorded as a reported result.

An illustrative application is not recorded as validation.

A source-described `open theoretical exploration` is not promoted to `SUPPORTED` or demoted to `REJECTED`.

---

## 8. Bounded absence

If a category is empty after exhaustive parsing of the frozen source surface, the strongest admissible statement is source-bounded:

```text
NOT_OBSERVED_ON_FROZEN_SOURCE_SURFACE
```

not:

```text
DOES_NOT_EXIST
NEVER_CONSIDERED
FALSE
```

Thus:

\[
\boxed{
\text{not observed in }R_i@H_i
\neq
\text{absent from the research program}.
}
\]

This applies especially to negative results, open questions, dependencies, and cross-repository references.

---

## 9. Compression does not emit map edges

The compression may preserve an explicit reference exactly as encountered.

It may not silently convert that reference into a resolved PROGRAM MAP edge.

\[
\boxed{
\text{compressed reference}
\neq
\text{resolved endpoint}
\neq
\text{licensed edge}.
}
\]

Any future cross-object edge still passes through the already-frozen relation-extraction / endpoint-resolution boundaries.

For the R01 witness:

```text
MAP_EDGE_EMISSION = FORBIDDEN
```

---

## 10. Compression does not grant authority

The compression may accurately report that a source calls something a claim, hypothesis, result, theorem, benchmark, or conclusion.

That reporting does not independently validate the source's standing.

\[
\boxed{
\text{source-described standing}
\neq
\text{compression-granted standing}.
}
\]

Therefore:

```text
COMPRESSION_AUTHORITY_EFFECT = NONE
MAP_AUTHORITY_EFFECT         = NONE
SCIENTIFIC_AUTHORITY_EFFECT  = NONE
```

---

## 11. Historical fidelity

The compression is bound to one immutable head.

If a later head changes terminology, deletes a claim, adds a negative result, or resolves an open question, the earlier compression remains historically valid as a compression of the earlier head.

\[
\boxed{
Z_i(H_a)
\neq
Z_i(H_b)
\quad\text{may both be historically valid.}
}
\]

A later compression must not silently rewrite an earlier compression to make later understanding appear present at the earlier head.

---

## 12. Reconstruction ladder

The intended inspectability path is:

\[
\boxed{
\text{program map}
\rightarrow
\text{compressed research object}
\rightarrow
\text{frozen repository head}
\rightarrow
\text{exact source file/blob}.
}
\]

The compression is useful only if this ladder remains traversable.

---

## 13. R01 witness authorization

This contract authorizes exactly one bounded witness:

```text
REPOSITORY_ID     = R01
REPOSITORY        = bjoern-janson/interface-induced-computational-geometry
COMPRESSION_COUNT = 1
```

The witness must freeze its exact repository head and source manifest before the compression result is written.

After the R01 result, a hostile death test must attack at least:

```text
HYPOTHESIS_AS_RESULT
DEFINITION_AS_EVIDENCE
APPLICATION_AS_VALIDATION
COMPRESSION_AS_IMPORTANCE_RANKING
EMPTY_CATEGORY_AS_GLOBAL_ABSENCE
REFERENCE_AS_EDGE
SOURCE_STATUS_AS_COMPRESSION_AUTHORITY
SOURCE_OMISSION_BY_COMPRESSION
```

If a consequential distinction cannot be represented without changing this contract, freeze the failure before revising the schema.

---

## 14. Frozen status

```text
RESEARCH_OBJECT_COMPRESSION_V0.1       = FROZEN
PROCESSING_ORDER                        = R01_TO_R43
CURRENT_AUTHORIZED_REPOSITORY           = R01_ONLY
R01_PROGRAM_COMPRESSION_ACCESS          = OPEN
R02_R43_PROGRAM_COMPRESSION_ACCESS      = NOT_YET_OPENED
CEREBRO_STEP_2                           = CLOSED
CEREBRO_STEP_2_R01_CONTENT_ACCESS        = CLOSED
CEREBRO_STEP_2_R01_SEMANTIC_ACCESS       = CLOSED
MAP_EDGE_EMISSION                        = FORBIDDEN
PROPAGATE_KERNEL                         = NOT_EARNED
MAP_AUTHORITY                            = NONE
SCIENTIFIC_AUTHORITY                     = NONE
NEXT_OBJECT                              = R01_FROZEN_SOURCE_SURFACE_V0.1
```

The first neuron may be compressed.

It may not yet fire, connect itself, or teach the network what to believe.
