# R05 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Candidate compression:** `R05_COMPRESSION_V0.1.json`  
**Projection ledger:** `R05_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Effective parse:** base + Amendment 001 + Amendment 002  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R05 tests the effective compression contract against a compact repository containing theory, protocol, Python implementation, unittest code and a Jupyter notebook.

## 1. Coverage accounting

The projection ledger contains one primary disposition for each effective parse unit:

```text
EFFECTIVE_PARSE_UNITS = 67
PRIMARY_PROJECTION_ENTRIES = 67
UNMAPPED_PARSE_UNITS = 0
```

```text
PARSE_TO_COMPRESSION_COVERAGE = CONTAINED
```

## 2. Notebook and executable standing

The compression preserves:

```text
NOTEBOOK_EXECUTION_METADATA
EXECUTABLE_IMPLEMENTATION
IMPLEMENTATION_ASSUMPTION
IMPLEMENTED_TEST_ASSERTION
IMPLEMENTED_OUTPUT_BEHAVIOR
```

without emitting a reported result.

```text
NOTEBOOK_OUTPUT_AS_RESULT = CONTAINED
TEST_CODE_AS_PASSED_TEST = CONTAINED
PROGRAMMED_DIAGNOSTIC_AS_RESULT = CONTAINED
SYNTHETIC_MODEL_AS_EMPIRICAL_RESULT = CONTAINED
```

## 3. Hit A — semantic redundancy with role-branch loss

Two compression items intentionally group semantically repeated source material:

```text
R05:FORMAL:ETA
R05:FORMAL:KSTAR
```

Each has two source branches:

```text
README.md                     -> FORMAL_STRUCTURE
docs/mathematical_specification.md -> DEFINITION
```

The candidate records both parse-unit IDs but does not preserve the differing source-local semantic roles inside the grouped destination.

This violates the effective grouping rule:

\[
\boxed{
\text{semantic redundancy may collapse}
\quad\land\quad
\text{role distinction must remain recoverable}.
}
\]

```text
SEMANTIC_REDUNDANCY_ROLE_BRANCH_LOSS = HIT
```

No new top-level coordinate is required. The minimum repair is branch-level role metadata on the grouped items.

## 4. Hit B — parse repair not propagated

The candidate compression was frozen before `R05_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_002.json`.

Its item:

```text
R05:METHOD:TEST_DIRECT_RUN
```

still says:

```text
Direct execution invokes unittest.main(); no stored run output is present.
```

The effective parse now correctly limits the source-local content to:

```text
Direct execution invokes unittest.main().
```

Repository-wide absence remains at the aperture-level absence record.

Therefore:

```text
PARSE_REPAIR_NOT_PROPAGATED_TO_COMPRESSION = HIT
```

The repair is content/provenance synchronization only.

## 5. Non-hit — artifact-local execution state

Notebook execution metadata is stored under the existing status coordinate with item kind:

```text
ARTIFACT_EXECUTION_METADATA
```

It is explicitly scoped to the notebook artifact and does not become project status or experimental standing.

```text
ARTIFACT_EXECUTION_METADATA_AS_PROJECT_STATUS = CONTAINED
```

## 6. Non-hit — recurrence as warrant

Repeated mathematical definitions across README and mathematical specification are derivational source occurrences only.

```text
SOURCE_RECURRENCE_AS_WARRANT = CONTAINED_AT_ZERO_AUTHORITY_BOUNDARY
```

## 7. Verdict

```text
R05_COMPRESSION_CANDIDATE                  = FROZEN_FAILED_FIRST_ATTEMPT
SEMANTIC_REDUNDANCY_ROLE_BRANCH_LOSS       = HIT
PARSE_REPAIR_NOT_PROPAGATED_TO_COMPRESSION = HIT
NEW_TOP_LEVEL_COMPRESSION_COORDINATE       = NONE
NEW_GLOBAL_PARSE_CLASS                     = NONE
R05_REPORTED_EMPIRICAL_RESULTS             = NONE_ON_FROZEN_SOURCE_SURFACE
R05_REUSABLE_NODE_STATE                    = NOT_YET_EARNED
R06_ACCESS                                 = NOT_AUTHORIZED
MAP_AUTHORITY                              = NONE
SCIENTIFIC_AUTHORITY                       = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```
