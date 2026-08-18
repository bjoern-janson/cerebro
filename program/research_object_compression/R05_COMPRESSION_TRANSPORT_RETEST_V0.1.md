# R05 COMPRESSION TRANSPORT — RETEST V0.1

**Death test:** `R05_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Compression repair:** `R05_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Projection revalidation:** `R05_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest evaluates only the two demonstrated compression failures while preserving executable/notebook standing boundaries.

## 1. Role-preserving semantic compression

`R05:FORMAL:ETA` and `R05:FORMAL:KSTAR` remain semantically compressed across README and mathematical specification source occurrences.

Their differing source roles are now explicit:

```text
README occurrence                     = FORMAL_STRUCTURE
mathematical-specification occurrence = DEFINITION
```

Thus:

\[
\boxed{
\text{semantic redundancy}
\Rightarrow
\text{compressible}
}
\]

while:

\[
\boxed{
\text{source-role distinction}
\Rightarrow
\text{preserved in branch provenance}.
}
\]

```text
SEMANTIC_REDUNDANCY_ROLE_BRANCH_LOSS = REPAIRED
```

No duplicate warrant branch or scientific standing is created.

## 2. Parse-repair synchronization

The effective compression item:

```text
R05:METHOD:TEST_DIRECT_RUN
```

now contains only the source-local code fact:

```text
Direct execution invokes unittest.main().
```

Repository-wide absence of stored test-run records remains only at the parse-aperture metadata layer.

```text
PARSE_REPAIR_NOT_PROPAGATED_TO_COMPRESSION = REPAIRED
```

## 3. Projection accounting

```text
R05_EFFECTIVE_PARSE_UNITS           = 67
R05_EFFECTIVE_PRIMARY_PROJECTIONS   = 67
R05_UNMAPPED_PARSE_UNITS            = 0
R05_DUPLICATE_PRIMARY_OWNERS        = 0
```

The grouped notebook execution metadata preserves both source fields under one artifact-local status item without changing standing.

## 4. Notebook/executable non-regressions

R05 is the first tested repository containing a Jupyter notebook.

The committed notebook records:

```text
execution_count = null
outputs = []
```

and the effective node preserves:

```text
NOTEBOOK_CODE                    = EXECUTABLE_IMPLEMENTATION
NOTEBOOK_STORED_EXECUTION_STATE  = ARTIFACT_EXECUTION_METADATA
NOTEBOOK_REPORTED_RESULT         = NONE
```

```text
NOTEBOOK_CODE_AS_EXECUTION = CONTAINED
NOTEBOOK_PRESENTATION_AS_RESULT = CONTAINED
```

The executable Python surfaces likewise preserve:

```text
IMPLEMENTED_TEST_ASSERTION != PASSED_TEST
PROGRAMMED_OUTPUT_BEHAVIOR != OBSERVED_RESULT
IMPLEMENTATION_ASSUMPTION != SCIENTIFIC_WARRANT
```

`instrument.py` hard-codes a synthetic `true_k=3` and synthetic response formulas. `experiment.py` applies a deterministic diagnostic fork to those synthetic outputs. No run artifact on the frozen source surface is admitted as a result.

```text
SYNTHETIC_IMPLEMENTATION_AS_EMPIRICAL_FINDING = CONTAINED
TEST_CODE_AS_PASSED_TEST = CONTAINED
PROGRAMMED_DIAGNOSTIC_AS_RESULT = CONTAINED
```

## 5. No global contract growth

R05 required:

- one parse accounting correction;
- one source-local/aperture provenance correction;
- one local compression role-branch repair;
- one local compression synchronization repair.

It required no new global parser role, no new top-level compression coordinate and no network semantics.

The existing effective contract therefore transports to a repository containing:

```text
Markdown theory
mathematical specification
experimental protocol
Python implementation
unittest implementation
Jupyter notebook with explicit non-executed stored state
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R05_FROZEN_HEADS
```

This is not universal transportability.

## 6. R05 verdict

```text
R05_SOURCE_SURFACE                         = FROZEN_FULL_RECURSIVE_HEAD
R05_TOTAL_BLOBS                            = 11
R05_RESEARCH_BEARING_BLOBS                 = 9
R05_MARKDOWN_BLOBS                         = 5
R05_PYTHON_BLOBS                           = 3
R05_NOTEBOOK_BLOBS                         = 1
R05_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS       = 67
R05_PARSE_FAILURES                         = 0
R05_UNRESOLVED_PARSE_UNITS                 = 0
R05_PRIMARY_PROJECTION_ENTRIES             = 67
R05_UNMAPPED_PARSE_UNITS                   = 0
PARSE_UNIT_COUNT_SELF_INCONSISTENCY        = REPAIRED
REPOSITORY_WIDE_ABSENCE_AS_SOURCE_LOCAL_CONTENT = REPAIRED
SEMANTIC_REDUNDANCY_ROLE_BRANCH_LOSS       = REPAIRED
PARSE_REPAIR_NOT_PROPAGATED_TO_COMPRESSION = REPAIRED
NOTEBOOK_EXECUTION_ROLE_TRANSPORT          = SUPPORTED_ON_R05_FROZEN_HEAD
R05_REPORTED_EMPIRICAL_RESULTS             = NONE_ON_FROZEN_SOURCE_SURFACE
R05_REUSABLE_NODE_STATE                    = EARNED_ON_FROZEN_HEAD
R05_MAP_EDGE_EMISSION                      = NONE
R05_MAP_AUTHORITY                          = NONE
R05_SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```

## 7. Sequential boundary

```text
R06_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R07_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This is procedural authorization only and creates no R05 -> R06 semantic relation.

The first five research neurons are reconstructible under one effective compression discipline. No synaptic propagation law exists.
