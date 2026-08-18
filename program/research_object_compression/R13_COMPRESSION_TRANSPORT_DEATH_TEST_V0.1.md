# R13 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R13_COMPRESSION_V0.1.json`  
**Effective parse:** 34 primary source units + 4 derived audit views  
**Projection ledger:** `R13_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R13 is the first positive execution-record stress surface in the sequential compression experiment.

## 1. Projection accounting

```text
R13_EFFECTIVE_PRIMARY_PARSE_UNITS = 34
R13_PRIMARY_PROJECTION_ENTRIES    = 34
R13_UNMAPPED_PARSE_UNITS          = 0
R13_DUPLICATE_PRIMARY_OWNERS      = 0
R13_SECONDARY_AUDIT_VIEWS         = 4
```

Projection completeness passes.

## 2. Attack matrix

```text
EXECUTION_RECORD_AS_RESULT_CONCLUSION              = CONTAINED
EXECUTION_RECORD_AS_SCIENTIFIC_VALIDATION          = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_RECORD             = CONTAINED
RESULT_INTERPRETATION_AS_RAW_EVIDENCE               = CONTAINED

RAW_PATH_COUNT_AS_EXECUTION_COUNT                   = CONTAINED
UNIQUE_BLOB_COUNT_AS_INDEPENDENT_EXECUTION_COUNT    = CONTAINED
UNIQUE_BLOB_COUNT_AS_WARRANT_COUNT                  = CONTAINED
BYTE_IDENTICAL_PATHS_AS_REPLICATION                 = CONTAINED
BACKUP_PATH_AS_SECOND_RUN                           = CONTAINED
NOMINAL_SEED_FILENAME_AS_PAYLOAD_RUN_ID             = CONTAINED

SEED42_RESULT_AS_MULTI_SEED_AGGREGATE               = CONTAINED
RUNNER_CAPABILITY_AS_STORED_RUN_PROVENANCE          = CONTAINED
RUNNER_SCHEMA_COMPATIBILITY_AS_GENERATION_PROOF     = CONTAINED
DERIVED_AUDIT_VIEW_AS_SOURCE_EVIDENCE               = CONTAINED
SOURCE_RESULT_RECURRENCE_AS_INDEPENDENT_CORROBORATION = CONTAINED
TRACE_ROW_MULTIPLICITY_AS_WARRANT_MULTIPLICITY      = CONTAINED
```

No compression-specific hit is found on the current bounded attacks.

## 3. Execution record / result separation

The effective node has four distinct standing layers:

```text
R13:IMPL:RUNNER             = EXECUTABLE_IMPLEMENTATION
R13:EXEC:RAW:*              = EXECUTION_RECORD_ARTIFACT
R13:RESULT:SEED42_REPORTED  = REPORTED_EMPIRICAL_RESULT
R13:INTERP:SEED42           = SOURCE_INTERPRETATION_OF_RESULT
```

Therefore a persisted per-timestep trace does not itself become the narrative conclusion, and a narrative result does not masquerade as the raw trace from which it might or might not have been derived.

```text
EXECUTION_RECORD_AS_RESULT_CONCLUSION = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_RECORD = CONTAINED
RESULT_INTERPRETATION_AS_RAW_EVIDENCE = CONTAINED
```

The node grants no scientific-validation effect to any of these objects.

```text
EXECUTION_RECORD_AS_SCIENTIFIC_VALIDATION = CONTAINED
```

## 4. Multiplicity remains typed

The frozen aperture establishes:

```text
raw path occurrences = 10
unique raw blobs      = 4
```

It does not establish:

```text
independent executions = 10
independent executions = 4
independent warrants   = 10
independent warrants   = 4
```

Those counts remain `NOT_ESTABLISHED` in the secondary provenance-ceiling audit.

Thus:

\[
\boxed{
\text{path occurrence}
\neq
\text{content identity}
\neq
\text{execution identity}
\neq
\text{execution independence}
\neq
\text{warrant independence}.
}
\]

```text
RAW_PATH_COUNT_AS_EXECUTION_COUNT = CONTAINED
UNIQUE_BLOB_COUNT_AS_INDEPENDENT_EXECUTION_COUNT = CONTAINED
UNIQUE_BLOB_COUNT_AS_WARRANT_COUNT = CONTAINED
BYTE_IDENTICAL_PATHS_AS_REPLICATION = CONTAINED
BACKUP_PATH_AS_SECOND_RUN = CONTAINED
```

## 5. Seed labels remain nominal provenance

The runner uses the invocation seed to construct `raw_seed_<seed>.json`, but the serialized result dictionary does not include seed/run-id metadata.

Accordingly the effective node preserves filenames as path provenance while keeping:

```text
PAYLOAD_INTERNAL_SEED = ABSENT
```

```text
NOMINAL_SEED_FILENAME_AS_PAYLOAD_RUN_ID = CONTAINED
```

This does not mean the filename is false. It means its jurisdiction is path-level rather than independently self-authenticating payload provenance.

## 6. Seed-42 narrative scope does not leak

Both README and RESULTS_SUMMARY explicitly state:

```text
Seed: 42
```

The presence of later nominal raw-seed paths does not silently broaden those narrative result statements.

```text
SEED42_RESULT_AS_MULTI_SEED_AGGREGATE = CONTAINED
```

No multi-seed narrative result is created by compression.

## 7. Implementation does not backfill provenance

The frozen runner:

- is ordinary Python;
- defines the environment and agent update logic;
- seeds Python randomness;
- contains an explicit random branch for mode E;
- defines the trace schema;
- writes a seed-named JSON file.

The raw artifacts are structurally compatible with that schema.

But:

```text
runner can produce such files
```

is weaker than:

```text
this exact independently documented invocation produced this exact stored path.
```

No separate invocation manifest or internal run identifier is present.

```text
RUNNER_CAPABILITY_AS_STORED_RUN_PROVENANCE = CONTAINED
RUNNER_SCHEMA_COMPATIBILITY_AS_GENERATION_PROOF = CONTAINED
```

## 8. Secondary audit views remain secondary

The following are useful cross-artifact deductions:

```text
10 paths -> 4 unique blobs
four unique mode-E traces differ at sampled t=67
random branch localized to mode E
independent execution count NOT_ESTABLISHED
```

They are retained as secondary audit views only.

```text
DERIVED_AUDIT_VIEW_AS_SOURCE_EVIDENCE = CONTAINED
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

## 9. Result recurrence does not become corroboration

README `Observed`, RESULTS_SUMMARY `Main observation`, and RESULTS_SUMMARY `Signature` all project into the Seed-42 reported-result object.

Their source occurrence count remains reconstructible, with:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

```text
SOURCE_RESULT_RECURRENCE_AS_INDEPENDENT_CORROBORATION = CONTAINED
```

## 10. Trace rows do not become evidence votes

A raw JSON blob contains many timestep records. Those rows are a longitudinal execution trace, not hundreds of independent confirmations of the benchmark hypothesis.

The source blob remains reversible and row-addressable while the compression treats it as one execution-record artifact.

```text
TRACE_ROW_MULTIPLICITY_AS_WARRANT_MULTIPLICITY = CONTAINED
```

## 11. Transportability result

R13 required three parse-level repairs before compression:

```text
1. cross-artifact deductions demoted from source parse
2. raw traces reclassified as execution records rather than result conclusions
3. parse cardinality corrected from declared 39 to explicit 38 / effective 34
```

All three were local repairs using distinctions already earned by the effective contract.

The compression itself requires no successor repair on the current bounded attacks.

```text
POST_COMPRESSION_DEATH_TEST_REPAIR = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005 = NOT_EARNED
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R13_FROZEN_HEADS
```

This is not universal transportability.

## 12. R13 verdict

```text
R13_SOURCE_SURFACE                  = FROZEN_FULL_RECURSIVE_HEAD
R13_TOTAL_BLOB_PATHS                = 13
R13_RESEARCH_BEARING_BLOB_PATHS     = 13
R13_UNIQUE_RESEARCH_BLOBS           = 7
R13_RAW_RESULT_PATH_OCCURRENCES      = 10
R13_UNIQUE_RAW_RESULT_BLOBS          = 4

R13_EFFECTIVE_PRIMARY_PARSE_UNITS   = 34
R13_DERIVED_AUDIT_VIEWS             = 4
R13_SOURCE_UNRESOLVED_UNITS         = 0
R13_PARSER_FAILURES                 = 0

R13_PRIMARY_PROJECTION_ENTRIES      = 34
R13_UNMAPPED_PARSE_UNITS            = 0
R13_DUPLICATE_PRIMARY_OWNERS        = 0

R13_EXECUTION_RECORD_ARTIFACTS      = 4 UNIQUE CONTENT OBJECTS
R13_INDEPENDENT_EXECUTION_COUNT     = NOT_ESTABLISHED
R13_INDEPENDENT_WARRANT_COUNT       = NOT_ESTABLISHED
R13_REPORTED_RESULT_SCOPE           = SEED_42_SOURCE_NARRATIVE

R13_REUSABLE_NODE_STATE             = EARNED
R13_MAP_EDGE_EMISSION               = NONE
R13_MAP_AUTHORITY                   = NONE
R13_SCIENTIFIC_AUTHORITY            = NONE
PROPAGATE_KERNEL                    = NOT_EARNED
CEREBRO_STEP_2                      = CLOSED
AMENDMENT_005                       = NOT_EARNED
```

## 13. Sequential boundary

```text
R14_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R15_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This is procedural authorization only and creates no R13 -> R14 semantic relation.

R13 therefore becomes the first neuron in the sequence that can remember persisted execution traces without converting file count, blob count, timestep count, or source-result recurrence into fabricated replication or warrant multiplicity.
