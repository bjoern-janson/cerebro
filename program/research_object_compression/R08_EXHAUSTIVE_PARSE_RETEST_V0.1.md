# R08 EXHAUSTIVE PARSE — RETEST V0.1

**Death test:** `R08_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1.md`  
**Repair:** `R08_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest evaluates only `ADMITTED_CFF_FIELD_OMISSION` and preserves all previously contained hostile fixtures.

## 1. CFF coverage repair

The effective parse now preserves the previously omitted admitted distinctions:

```text
CFF_VERSION = 1.2.0
CITATION_MESSAGE = "If you use this framework in research, please cite this work."
KEYWORDS = 10 source-provided research-positioning terms
```

No keyword is promoted into a scientific claim, field dependency, map edge or warrant.

```text
ADMITTED_CFF_FIELD_OMISSION = REPAIRED
```

## 2. Effective parse accounting

```text
ADMITTED_SOURCE_PATHS     = 48
EFFECTIVE_PARSE_UNITS     = 396
PARSED_UNITS              = 395
UNRESOLVED_UNITS          = 1
PARSER_FAILURES           = 0
UNACCOUNTED_SOURCE_PATHS  = 0
```

The unresolved unit remains:

```text
R08:P:EXP:TEMPLATE_TERMINAL
```

because the frozen source itself terminates after `Each experiment should contain:`.

## 3. Preserved non-regressions

```text
PATH_OCCURRENCE_AS_CONTENT_INDEPENDENCE          = CONTAINED
ONE_BYTE_SCRIPT_AS_NEGATIVE_RESULT               = CONTAINED
SOURCE_INTERNAL_INCOMPLETENESS_AS_PARSER_FAILURE = CONTAINED
CROSS_FILE_FORMAL_INCONSISTENCY_AS_RECONCILIATION = CONTAINED
SOURCE_LABEL_CANONICAL_AS_SUPERSESSION           = CONTAINED
ASSUMPTION_AS_SUPPORTED_CLAIM                    = CONTAINED
PROPOSED_PROXY_AS_VALIDATED_MEASURE              = CONTAINED
PROPOSED_DATASET_AS_EMPIRICAL_DATA               = CONTAINED
HISTORICAL_INTERPRETATION_AS_VALIDATION           = CONTAINED
IMPLEMENTED_EVALUATOR_AS_EXECUTED_RESULT          = CONTAINED
PROGRAMMED_SUPPORT_LABEL_AS_SCIENTIFIC_SUPPORT   = CONTAINED
SIMULATION_PROXY_AS_UNIFIED_OMEGA_MEASURE         = CONTAINED
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE      = CONTAINED
```

## Verdict

```text
R08_EFFECTIVE_EXHAUSTIVE_PARSE = ADEQUATE_ON_FROZEN_V0.1_DEATH_TEST
R08_EFFECTIVE_PARSE_UNITS      = 396
R08_PARSED_UNITS               = 395
R08_UNRESOLVED_UNITS           = 1
R08_PARSE_FAILURES             = 0
R08_COMPRESSION                = AUTHORIZED
GLOBAL_CONTRACT_CHANGE         = NONE
NEW_PARSER_ROLE                = NONE
NEW_TOP_LEVEL_COMPRESSION_CLASS = NONE
MAP_AUTHORITY                  = NONE
SCIENTIFIC_AUTHORITY           = NONE
PROPAGATE_KERNEL               = NOT_EARNED
CEREBRO_STEP_2                 = CLOSED
```
