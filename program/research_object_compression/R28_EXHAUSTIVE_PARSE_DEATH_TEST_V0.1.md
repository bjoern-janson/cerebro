# R28 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/adaptive-inheritance`  
**Frozen head:** `5fce9982cd74ef735ac4b6ffae8e1bdf494b35fa`  
**Effective source surface:** `R28_SOURCE_SURFACE_V0.1.json`  
**Effective parse:** Part A1 + A2 + B–J under local serialization Amendment 001  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Accounting

```text
R28_EFFECTIVE_SOURCE_PATHS        = 23
R28_EFFECTIVE_PARSE_UNITS         = 287
R28_PARSED_REPRESENTATIONS        = 241
R28_EXPLICITLY_UNRESOLVED         = 46
R28_PARSER_FAILURES               = 0
R28_MISSING_ADMITTED_PATHS        = 0
R28_DUPLICATE_EFFECTIVE_UNIT_IDS  = 0
```

The original `PART_A` candidate is not effective: it serialized stale extra rows despite a 67-unit header and would collide with downstream IDs. It was detected before the effective manifest and replaced by A1/A2. No semantic unit, standing, or source coordinate was changed by the repair.

## 2. Attack matrix

```text
BAD_PART_A_SERIALIZATION_AS_EFFECTIVE_PARSE              = CONTAINED
AIC_AS_EMPIRICALLY_VALIDATED                             = CONTAINED
AUTHORITY_WEIGHT_AS_IDENTIFIED_CAUSAL_AUTHORITY          = CONTAINED
AUTHORITY_UPDATE_CODE_AS_CAUSAL_IDENTIFICATION           = CONTAINED
MRAT_THRESHOLD_ROUTER_AS_CAUSAL_ATTRIBUTION              = CONTAINED
ATTRIBUTION_SIMPLEX_AS_TRUE_FAILURE_LOCUS                 = CONTAINED
LBR_AS_FAILURE_ATTRIBUTION                               = CONTAINED
REE_INPUTS_AS_ESTIMATED_QUANTITIES                       = CONTAINED
REE_DECISION_CODE_AS_VALIDATED_EXPANSION_POLICY          = CONTAINED
PLACEHOLDER_STRUCTURAL_DISTANCE_AS_VALIDATED_METRIC      = CONTAINED
REFERENCE_AGENT_AS_VALIDATED_CORRIGIBLE_AGENT            = CONTAINED
EXPECTED_ACTION_LABEL_AS_EXECUTED_INTERVENTION           = CONTAINED
RAHU_TASK_SPECIFICATION_AS_BENCHMARK_EXECUTION           = CONTAINED
DOCUMENTED_ACCEPTANCE_RULE_AS_SATISFIED_ACCEPTANCE       = CONTAINED
FALSIFICATION_CRITERION_AS_FALSIFICATION_EVENT           = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                             = CONTAINED
TEST_SOURCE_AS_TEST_PASS                                 = CONTAINED
STALE_TEST_API_AS_OBSERVED_TEST_FAILURE                  = CONTAINED
SOURCE_LEVEL_INTERFACE_DEFECT_AS_EMPIRICAL_NEGATIVE      = CONTAINED
SOURCE_LEVEL_INTERFACE_DEFECT_AS_THEORY_FALSIFICATION    = CONTAINED
NO_WORKFLOW_RUN_AS_TEST_FAILURE                          = CONTAINED
DOC_MODULE_DEPENDENCY_AS_CEREBRO_EDGE                    = CONTAINED
SOURCE_RELATION_ASSERTION_AS_ENDPOINT_RESOLUTION         = CONTAINED
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY           = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                 = CONTAINED
```

No semantic parse failure is found.

## 3. Construct-validity firewall

The source uses names such as causal authority, attribution, corrigibility, residual compressibility, structural distance, ADI and ACS. The effective parse preserves the source definitions and the literal implementations, while separately preserving unresolved identification/calibration questions.

```text
SOURCE_THEORETICAL_CONSTRUCT != IMPLEMENTED_PROXY != VALIDATED_MEASURE
```

In particular, mechanism weights are implementation variables unless an independent design establishes their causal relation to future influence; the default MRAT router is a threshold baseline unless independently validated as causal attribution.

## 4. Implementation/test drift is not execution evidence

Frozen source inspection identifies interface pressures including:

- `tests/test_inheritance.py` imports `InheritanceEngine`, while the package exports `AdaptiveInheritanceEngine`;
- MRAT tests expect a dictionary/context API and `should_expand_representation`, while the frozen router accepts scalar residuals and returns `AttributionVector`;
- PTVS tests expect `compute_lbr(trajectories)`, `evaluate`, and `get_violations`, while the frozen analyzer uses stored records and different method names;
- RAHU tests import `RAHUHarness` from the package root and call methods/signatures absent from the frozen package/evaluator;
- RAHU tasks call supplied mechanisms directly, while the frozen `Mechanism` exposes `.execute()` and no `__call__`;
- evaluator ARR requests a baseline-authority getter absent from the supplied abstract/reference agent interface;
- reference-agent updates do not attenuate old mechanism authority;
- evaluator structural distance is a 0/1 placeholder and does not implement the documented structural metric.

These are source-level software observations. The frozen head has zero GitHub Actions runs and zero combined-status records, and contains no persisted run/test output.

```text
SOURCE_LEVEL_INTERFACE_PRESSURE != EXECUTION_FAILURE != EMPIRICAL_NEGATIVE_RESULT
```

## 5. Evidence ladder

```text
theory/specification        = PRESENT
executable implementation   = PRESENT
test source                 = PRESENT
prospective falsification   = PRESENT
persisted benchmark runs    = NONE_ON_FROZEN_SURFACE
persisted test reports      = NONE_ON_FROZEN_SURFACE
source-reported results     = 0
source-reported negatives   = 0
GitHub workflow runs        = 0
combined status records     = 0
```

Therefore:

```text
IMPLEMENTATION != EXECUTION_RECORD != RESULT
TEST_SOURCE != TEST_RUN != TEST_PASS_OR_FAIL_EVIDENCE
FALSIFICATION_RULE != FALSIFICATION_EVENT
```

## 6. Relation firewall

The architecture and metric documents contain source-level dependency graphs. These remain source assertions only.

```text
SOURCE_RELATION_ASSERTION != ENDPOINT_IDENTITY != RESOLVED_EDGE != CEREBRO_SYNAPSE
```

No map edge is emitted.

## 7. Repair locality

```text
PRE_MANIFEST_SERIALIZATION_REPAIR = R28_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001
SEMANTIC_UNIT_CHANGE              = NONE
STANDING_CHANGE                   = NONE
SOURCE_COORDINATE_CHANGE          = NONE
POST_PARSE_DEATH_TEST_REPAIR      = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_GLOBAL_PARSER_ROLE            = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005                     = NOT_EARNED
```

## 8. Verdict

```text
R28_EXHAUSTIVE_PARSE_STATE = FROZEN
R28_PARSE_DEATH_TEST       = PASS
COMPRESSION_AUTHORIZED     = YES
R28_MAP_EDGE_EMISSION      = NONE
R28_MAP_AUTHORITY          = NONE
R28_SCIENTIFIC_AUTHORITY   = NONE
```

The pass is bounded to this frozen source surface and does not grant scientific authority to the source claims.