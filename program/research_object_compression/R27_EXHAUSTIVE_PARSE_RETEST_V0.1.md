# R27 EXHAUSTIVE PARSE — RETEST V0.1

**Repository:** `bjoern-janson/axiom-forge-mk1`  
**Frozen head:** `5a488d137c947df8eb8f88fba6dd74fc1b25985c`  
**Effective source surface:** base + source-surface Amendment 001  
**Effective parse:** base Parts A-C + parse Amendment 001  
**Persistent record state:** `FROZEN`

## 1. Accounting

```text
R27_EFFECTIVE_SOURCE_PATHS       = 32
R27_COVERED_SOURCE_PATHS         = 32
R27_PARSED_REPRESENTATIONS       = 131
R27_EXPLICITLY_UNRESOLVED        = 25
R27_EFFECTIVE_PARSE_UNITS        = 156
R27_PARSER_FAILURES              = 0
R27_PATHS_WITHOUT_PRIMARY_UNIT   = 0
R27_EXTRA_UNIT_PATHS             = 0
```

Part A effective coverage now includes `src/__init__.py`. No semantic unit changed.

## 2. Non-regression checks

```text
THEORY_VS_IMPLEMENTED_PROXY          = PRESERVED
IMPLEMENTATION_VS_EXECUTION          = PRESERVED
TEST_SOURCE_VS_TEST_EXECUTION        = PRESERVED
CONFIG_VS_RUN                        = PRESERVED
METRIC_VS_CONSTRUCT_VALIDITY         = PRESERVED
CORRELATION_VS_CAUSAL_COUPLING       = PRESERVED
PREDICTION_VS_RESULT                 = PRESERVED
SOFTWARE_DEFECT_VS_NEGATIVE_RESULT   = PRESERVED
CURRENT_HEAD_VS_HISTORY              = PRESERVED
```

## 3. Verdict

```text
R27_EFFECTIVE_EXHAUSTIVE_PARSE = FROZEN
POST_PARSE_REPAIR              = METADATA_ONLY
SEMANTIC_REPAIR                = NONE
NEW_EPISTEMIC_DISTINCTION      = NO
NEW_GLOBAL_PARSER_ROLE         = NONE
PARSE_CONTRACT_AMENDMENT       = NOT_EARNED
```

Compression is authorized from exactly 156 effective parse units.
