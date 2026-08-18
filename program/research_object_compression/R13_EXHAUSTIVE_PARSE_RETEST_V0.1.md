# R13 EXHAUSTIVE PARSE — RETEST V0.1

**Base parse:** `R13_EXHAUSTIVE_PARSE_V0.1.json`  
**Repair:** `R13_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Death test:** `R13_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1.md`  
**Persistent record state:** `FROZEN`

## 1. Primary-vs-derived separation

The four demonstrated cross-artifact deductions are no longer counted in the effective source parse:

```text
R13:P:RAW:MULTIPLICITY
R13:P:RAW:DISTINCT_E_TRACE
R13:P:RAW:DETERMINISTIC_MODES
R13:P:RAW:PROVENANCE_CEILING
```

They survive as explicit `DERIVED_AUDIT_VIEW` objects with:

```text
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

Therefore:

```text
CROSS_ARTIFACT_AUDIT_AS_SOURCE_PARSE_UNIT = REPAIRED
DERIVED_PROVENANCE_CEILING_AS_SOURCE_STATUS = REPAIRED
```

## 2. Effective source parse accounting

```text
R13_HISTORICAL_CANDIDATE_UNITS      = 39
R13_EFFECTIVE_PRIMARY_PARSE_UNITS   = 35
R13_DERIVED_AUDIT_VIEWS             = 4
R13_SOURCE_UNRESOLVED_UNITS         = 0
R13_PARSER_FAILURES                 = 0
R13_RESEARCH_PATHS_ACCOUNTED        = 13/13
```

No source-local unit was changed or deleted.

## 3. Raw trace/result standing non-regression

The four unique immutable raw blobs remain primary source artifacts with source standing:

```text
PERSISTED_RAW_EXECUTION_TRACE_ARTIFACT
```

Their path occurrences remain separately reconstructible.

The retest preserves:

```text
PERSISTED_RAW_TRACE != SCIENTIFIC_VALIDATION
RAW_PATH != INDEPENDENT_EXECUTION
DISTINCT_BLOB != INDEPENDENT_WARRANT
BYTE_IDENTICAL_PATHS != REPLICATION
BACKUP_PATH != SECOND_EXPERIMENT
```

## 4. Seed-scope non-regression

`README.md` and `RESULTS_SUMMARY.md` remain explicitly scoped to Seed 42.

The nominal multi-seed raw path surface remains separate.

```text
SEED42_SUMMARY_AS_MULTI_SEED_AGGREGATE = CONTAINED
```

## 5. Runner/result provenance non-regression

The frozen runner establishes:

- executable generation logic;
- `random.seed(seed)`;
- mode E's explicit random-choice branch;
- the raw JSON output field schema;
- filename construction `raw_seed_<seed>.json`.

It does not establish, by implementation alone, independent invocation provenance for every stored path.

```text
RUNNER_CAPABILITY_AS_EACH_STORED_EXECUTION = CONTAINED
```

## 6. Retest verdict

```text
R13_EFFECTIVE_PARSE_STATE              = PROVISIONALLY_ADEQUATE_ON_CURRENT_BOUNDED_DEATH_TEST
NEW_GLOBAL_PARSER_ROLE                 = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE   = NONE
AMENDMENT_005                          = NOT_EARNED
MAP_EDGE                               = NONE
PROPAGATION                            = NONE
CEREBRO_STEP_2                         = CLOSED
```

Compression may proceed against the 35-unit effective primary source parse while retaining the four derived audit views as zero-authority hostile fixtures.
