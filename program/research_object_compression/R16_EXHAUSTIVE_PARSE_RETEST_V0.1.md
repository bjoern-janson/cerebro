# R16 EXHAUSTIVE PARSE — RETEST V0.1

**Base candidate:** `R16_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-D  
**Repair:** `R16_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`

## Accounting

```text
R16_SOURCE_PATHS                    = 38
R16_CANDIDATE_PARSE_UNITS           = 427
R16_DEMOTED_AUDIT_UNITS             = 8
R16_ONE_FOR_ONE_OUTPUT_REPLACEMENTS = 15
R16_EFFECTIVE_PRIMARY_PARSE_UNITS   = 419
R16_DERIVED_AUDIT_VIEWS             = 5
R16_UNRESOLVED_SOURCE_UNITS         = 8
R16_PARSER_FAILURES                 = 0
```

## Retest

```text
OUTPUT_BEHAVIOR_WITH_APERTURE_ABSENCE = REPAIRED
CROSS_ARTIFACT_AUDIT_AS_SOURCE_UNIT   = REPAIRED
RESULT_FILENAME_AS_RESULT             = CONTAINED
EMPTY_RESULT_SHELL_AS_ZERO_RESULT     = CONTAINED
QUALITATIVE_CLAIM_AS_POPULATED_TABLE  = CONTAINED
CODE_PRESENCE_AS_EXECUTION            = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_LOG  = CONTAINED
PLACEHOLDER_RUNNER_AS_BASELINE_ROBUSTNESS = CONTAINED
VERSION_NUMBER_AS_AUTHORITY_ORDER     = CONTAINED
LATER_POSITIVE_RESULT_AS_ERASURE_OF_EARLIER_NEGATIVE = CONTAINED
SOURCE_INDEPENDENT_SEEDS_AS_WARRANT_INDEPENDENCE = CONTAINED
RAD_RELATION_AS_PROGRAM_MAP_EDGE      = CONTAINED
TOKEN_IDENTITY_AS_SEMANTIC_IDENTITY   = CONTAINED
```

The 15 output units now contain only file-local implemented output behavior. Repository-level raw-output absence is represented only by `R16:AUDIT:NO_RAW_RUN_ARTIFACTS`.

The eight cross-artifact deductions are no longer primary parse units.

The unresolved source units remain:

```text
results_v0.1: 4 blank observation/result locations
robustness_results_v1.2: 4 missing result tables
```

These are source incompleteness, not parser failure.

## Verdict

```text
R16_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS = 419
R16_PARSE_FAILURES                   = 0
R16_UNRESOLVED_SOURCE_UNITS          = 8
COMPRESSION_PROJECTION               = AUTHORIZED
AMENDMENT_005                        = NOT_EARNED
R17_ACCESS                           = NOT_AUTHORIZED
```

The effective parse preserves the versioned experiment as history rather than rewriting it into a single retrospectively coherent experiment.
