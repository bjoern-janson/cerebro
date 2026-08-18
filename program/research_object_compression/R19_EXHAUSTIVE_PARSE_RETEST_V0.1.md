# R19 EXHAUSTIVE PARSE — RETEST V0.1

**Base candidate:** `R19_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-C  
**Local repair:** `R19_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Effective reconstruction

Read the frozen candidate artifacts without rewriting them, then apply Amendment 001 only to Part A cardinality metadata.

Effective accounting:

```text
R19P0001-R19P0287 = 287 parsed representations
R19U0001-R19U0058 = 58 unresolved source fragments
TOTAL              = 345 units
DUPLICATE IDS       = 0
MISSING IDS         = 0
PARSER FAILURES     = 0
SOURCE PATHS        = 13/13 accounted
```

Part accounting:

```text
Part A = 90 + 16 = 106
Part B = 83 + 16 = 99
Part C = 114 + 26 = 140
TOTAL  = 287 + 58 = 345
```

## 2. Regression of prior attack matrix

```text
DECLARED_PARSE_CARDINALITY_MISMATCH                 = REPAIRED_BY_OVERLAY
THEORY_OR_AXIOM_AS_EMPIRICAL_RESULT                 = CONTAINED
BENCHMARK_SPECIFICATION_AS_EXECUTION                 = CONTAINED
BENCHMARK_SUCCESS_CRITERION_AS_REPORTED_SUCCESS     = CONTAINED
SOURCE_WORD_PROVES_AS_ACTUAL_VALIDATION              = CONTAINED
EXPERIMENT_SPECIFICATION_AS_EXECUTION                = CONTAINED
EXPECTED_RESULT_AS_REPORTED_RESULT                   = CONTAINED
OBSERVED_PHENOMENON_LABEL_AS_EXECUTION_EVIDENCE      = CONTAINED
FALSIFICATION_CRITERION_AS_FALSIFICATION_EVENT       = CONTAINED
AZUS_MAPPING_AS_IMPLEMENTATION_IDENTITY               = CONTAINED
PDM_REFERENCE_AS_RESOLVED_EXTERNAL_ENDPOINT           = CONTAINED
CROSS_FILE_RESTATEMENT_AS_INDEPENDENT_WARRANT         = CONTAINED
SAME_EQUATION_RECURRENCE_AS_REPLICATION               = CONTAINED
SAME_SYMBOL_AS_SAME_OBJECT                            = CONTAINED
FORMAL_VARIANT_AS_CANONICAL_EQUIVALENCE               = CONTAINED
CORRECTION_EVENT_CRITERIA_VARIANT_AS_SILENT_IDENTITY  = CONTAINED
UNRESOLVED_OPERATIONALIZATION_AS_PARSER_FAILURE       = CONTAINED
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY        = CONTAINED
LICENSE_OMISSION_AS_UNSEEN_PATH                        = CONTAINED
CROSS_REPOSITORY_VOCABULARY_AS_EDGE                   = CONTAINED
```

No new failure appears after the local repair.

## 3. Effective parse state

The parse retains all source-local formal variants for later compression rather than selecting a canonical formula during parsing. In particular:

```text
correction-deficit formulas with and without Theta remain distinct
restoration threshold <0 versus <=0 remains distinct
both Psi telemetry vectors remain distinct
correction-event criterion variants remain distinct
P/R symbol reuse remains non-identifying
```

These are transport pressures, not authorization to synthesize.

## 4. Verdict

```text
R19_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS = 345
R19_PARSED_REPRESENTATIONS           = 287
R19_UNRESOLVED_SOURCE_UNITS          = 58
R19_PARSER_FAILURES                  = 0
R19_PARSE_LOCAL_REPAIRS              = 1 CARDINALITY_METADATA_ONLY
R19_EXHAUSTIVE_PARSE_STATE           = EARNED_FOR_COMPRESSION_INPUT
NEW_EPISTEMIC_DISTINCTION_REQUIRED  = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
BASE_PARSE_CONTRACT_AMENDMENT        = NOT_EARNED
AMENDMENT_005                        = NOT_EARNED
R19_COMPRESSION_ACCESS               = AUTHORIZED
R20_PROGRAM_PARSE_ACCESS             = NOT_YET_OPENED
```

The historical bad count remains visible. The effective parse is correct because the repair is explicit, local, and reconstructible.
