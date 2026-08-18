# R22 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/causal-transition-condition`  
**Frozen head:** `fe899838979fcf0e6ee2f43011420a79b58daff8`  
**Frozen source surface:** 24/24 blobs  
**Parse candidate:** 206 parsed representations + 72 explicitly unresolved = 278 units  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Aperture accounting

```text
FROZEN_HEAD_PATHS             = 24
PARSE_INCLUDED                 = 24
PARSE_EXCLUDED_BY_SCOPE        = 0
PARSE_FAILED_PATHS             = 0
PARSE_UNSUPPORTED_PATHS        = 0
UNENUMERATED_PATHS             = 0
PARSED_REPRESENTATIONS         = 206
EXPLICITLY_UNRESOLVED          = 72
CANDIDATE_PARSE_UNITS          = 278
PARSER_FAILURES                = 0
```

All current-head paths are represented, including `.gitignore`, requirements, tests, executable code and the misleadingly named UTF-8 text blob `figures/ctc_overview.png`.

## 2. Attack matrix

```text
FILE_EXTENSION_AS_CONTENT_TYPE                         = CONTAINED
CAUSAL_TRANSITION_AS_CONSTRAINT_TRANSITION_IDENTITY    = CONTAINED
CAUSAL_TRANSITION_AS_CONSTRAINT_TRAJECTORY_IDENTITY    = CONTAINED
CTC_AS_CAUSAL_PERMEABILITY_PRINCIPLE_IDENTITY          = CONTAINED
CAUSAL_PERMEABILITY_RELATION_AS_CORPUS_ENDPOINT        = CONTAINED
MATHCAL_G_DEFINITION_AS_OBSERVABILITY                   = CONTAINED
OMEGA_TO_DELTA_G_ARROW_AS_CAUSAL_IDENTIFICATION         = CONTAINED
WEAK_CTC_DERIVATIVE_AS_STRONG_CTC_CAUSAL_PROOF         = CONTAINED
OPEN_ENDEDNESS_AS_INDEPENDENTLY_OPERATIONALIZED         = CONTAINED
BENCHMARK_SPECIFICATION_AS_EXECUTION                    = CONTAINED
IMPLEMENTATION_AS_SUCCESSFUL_EXECUTION                  = CONTAINED
RUNTIME_PRINT_LABEL_AS_OBSERVATION                      = CONTAINED
PLACEHOLDER_EXAMPLE_DATA_AS_REPORTED_RESULT             = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                           = CONTAINED
SOURCE_INTERFACE_DEFECT_AS_FAILED_TEST_EVENT            = CONTAINED
GITIGNORED_RESULT_ABSENCE_AS_NO_EXECUTION               = CONTAINED
TREATMENT_SWITCH_AS_VALIDATED_PERMEABILITY              = CONTAINED
TREATMENT_CODED_MECHANISM_STRING_AS_VALIDATED_GROWTH    = CONTAINED
SYNTHETIC_REMOVAL_INPUT_AS_MEASURED_RESIDUAL_CAPABILITY = CONTAINED
SOURCE_REPORTED_CONCEPTUAL_RESULT_AS_EMPIRICAL_RESULT   = CONTAINED
NEW_CONCEPTUAL_RESULT_STANDING_AS_GLOBAL_PARSER_ROLE    = HIT
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                = CONTAINED
CURRENT_HEAD_AS_DEVELOPMENTAL_HISTORY                   = CONTAINED
```

One local parser-standing hit is found.

## 3. Local hit: unlicensed result standing

`R22P0121` records the evolution log's Stage 6 phrase `Result:` for a semantic-label stress test. The source reports:

```text
Delta K != 0
Delta G = 0
```

and narratively concludes that the name changed while the causal bridge remained.

The candidate parser gave this unit the standing:

```text
REPORTED_CONCEPTUAL_TEST_RESULT
```

That is not an earned new global source-standing role. The source contains a conceptual/source-authored report, not a frozen empirical execution record.

The shallowest repair is therefore local:

```text
R22P0121 standing:
REPORTED_CONCEPTUAL_TEST_RESULT
->
SOURCE_ASSERTION_CONCEPTUAL
```

The unit remains distinct because the source explicitly labels a result and its provenance ceiling matters. Only its standing is corrected.

```text
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_GLOBAL_PARSER_ROLE             = NO
PARSE_CONTRACT_AMENDMENT           = NOT_EARNED
```

## 4. Nomenclature remains unresolved, not normalized

The frozen head contains multiple names around the same acronym/topic surface:

```text
Causal Transition Condition
Constraint Transition Condition
Constraint–Trajectory Coupling
Causal Permeability Principle
```

The parser preserves where each label occurs and whether the source describes a relationship/evolution. It does not manufacture global identity among them.

Especially:

```text
source relation to Causal Permeability
!= endpoint identity
!= R18 identity
!= corpus edge
```

## 5. Causal measurement remains unearned

The source proposes:

```text
Omega_t -> Delta mathcal G_(t+1)
partial mathcal G_(t+1) / partial Omega_t > 0
E* rightsquigarrow C_rev
```

but also explicitly states `mathcal G` is not directly observable. The frozen repository does not provide a validated causal-identification procedure for these quantities.

The implementation's current permeability proxy is the treatment switch itself, and mechanism expansion is directly generated only in the treatment-on branch. These are valid source facts about the prototype but do not establish the scientific causal claim.

```text
PROXY_IMPLEMENTATION_AS_CONSTRUCT_VALIDATION = CONTAINED
```

## 6. Execution standing remains bounded

The repository contains implementation, experiment runners and pytest source, but:

```text
GITHUB_ACTIONS_RUNS_AT_HEAD     = 0
COMBINED_STATUS_RECORDS_AT_HEAD = 0
PERSISTED_TEST_REPORTS          = 0
PERSISTED_BENCHMARK_RESULTS     = 0
```

Additionally, `.gitignore` explicitly ignores normal generated `results/`, `figures/`, `*.csv` and `*.json` artifacts.

Therefore current-head absence of generated results cannot identify absence of execution.

The proper ladder is:

```text
implementation present
!= execution established
!= result established
```

Source-level API incompatibilities are retained as unresolved implementation facts, not transformed into observed test failures.

## 7. Reported conceptual stress test remains provenance-limited

The Stage 6 semantic-collision narrative is preserved after the standing repair as a source-authored conceptual assertion with explicit result labeling.

It does not become:

```text
reported empirical result
execution record
independent replication
scientific authority
```

## 8. Death-test verdict

```text
R22_PARSE_CANDIDATE_UNITS          = 278
R22_LOCAL_STANDING_REPAIR_REQUIRED = 1
R22_UNIT_COUNT_CHANGE              = 0
R22_UNIT_REMAPS                    = 0
R22_PARSER_FAILURES                = 0
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_GLOBAL_PARSER_ROLE             = NO
BASE_PARSE_CONTRACT_AMENDMENT      = NOT_EARNED
```

Compression is blocked until the one-unit standing overlay is frozen and retested.
