# R32 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/arc-reactor`  
**Frozen head:** `16e6972de4f9c5dfb2039baa88d520a41ea7e613`  
**Candidate parse:** 83 units = 69 represented + 14 explicitly unresolved  
**Candidate source coverage:** 59 admitted paths  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Mechanical checks

```text
UNIT_ID_RANGE                    = R32P0001-R32P0083
UNIQUE_UNIT_IDS                  = 83
DUPLICATE_UNIT_IDS               = 0
ADMITTED_SOURCE_PATHS            = 59
SOURCE_PATHS_WITH_PRIMARY_UNIT   = 59
SOURCE_PATHS_WITHOUT_PRIMARY_UNIT= 0
PARSER_FAILURES                  = 0
```

One candidate metadata defect is localized:

```text
PART_B_DECLARED_COVERED_PATHS = 21
PART_B_ACTUAL_COVERED_PATHS   = 34
```

The 45 Part-B rows, their paths, blobs, standings, locators and normalized contents are internally intact. The global manifest already records Part B as 34 paths and the whole parse as 59/59 paths. This is a cardinality/header defect only.

## 2. Standing attack matrix

```text
RESEARCH_PROTOTYPE_AS_VALIDATED_SYSTEM                    = CONTAINED
PREDICTION_AS_REPORTED_RESULT                             = CONTAINED
FALSIFICATION_CRITERION_AS_OBSERVED_FALSIFICATION         = CONTAINED
STATIC_EVALUATE_CONSTANT_AS_BENCHMARK_RESULT              = CONTAINED
ORACLE_STATIC_ONES_AS_EMPIRICAL_UPPER_BOUND               = CONTAINED
META_STATIC_PROFILE_AS_OBSERVED_PERFORMANCE               = CONTAINED
SYNTHETIC_ENVIRONMENT_AS_EMPIRICAL_VALIDATION              = CONTAINED
METRIC_FUNCTION_AS_VALIDATED_CONSTRUCT                     = CONTAINED
AAR_ARITHMETIC_AS_IDENTIFIED_ECONOMIC_QUANTITY             = CONTAINED
C_FUTURE_COMPOSITE_AS_VALIDATED_FUTURE_CAPACITY            = CONTAINED
GAMMA_DISCREPANCY_PROXY_AS_IDENTIFIED_REALITY_COUPLING     = CONTAINED
AE_W_DEPTH_DISTANCE_AS_VALIDATED_CAUSAL_ATTRIBUTION        = CONTAINED
RI_FORMULA_AS_VALIDATED_RECOVERY_INTELLIGENCE              = CONTAINED
PHASE_BOUNDARY_CODE_AS_OBSERVED_AAR_TRANSITION             = CONTAINED
REGIME_METADATA_EXPECTED_WINNER_AS_RESULT                  = CONTAINED
TELEMETRY_OR_SERIALIZATION_CAPABILITY_AS_RUN_ARTIFACT      = CONTAINED
LOGGING_CAPABILITY_AS_EXECUTION_RECORD                     = CONTAINED
SOURCE_LEVEL_IMPORT_OR_API_DEFECT_AS_EXECUTED_FAILURE      = CONTAINED
SOURCE_LEVEL_IMPORT_OR_API_DEFECT_AS_EMPIRICAL_NEGATIVE    = CONTAINED
SOFTWARE_DEFECT_AS_THEORY_FALSIFICATION                    = CONTAINED
PLANNED_REPOSITORY_STRUCTURE_AS_CURRENT_TREE               = CONTAINED
PLANNED_WORLD_MODEL_SHOCK_AS_IMPLEMENTED_SHOCK             = CONTAINED
IMPLEMENTED_FOUR_SHOCK_SUITE_AS_COMPLETE_CHARTER_PROTOCOL  = CONTAINED
MULTIPLE_LAYER_NAMESPACES_AS_SILENT_IDENTITY               = CONTAINED
MULTIPLE_ATTRIBUTION_STACKS_AS_SINGLE_IMPLEMENTATION        = CONTAINED
MULTIPLE_PERMEABILITY_STACKS_AS_SINGLE_IMPLEMENTATION       = CONTAINED
CHRONOLOGICAL_ADDITION_ORDER_AS_CAUSAL_DEPENDENCY          = CONTAINED
```

No semantic standing failure is found.

## 3. Secondary software audit

These are parser deductions from comparing frozen source files. They are **not** primary source-authored claims and are not execution records.

```text
AUDIT_01 = agents/__init__.py imports OracleReset while oracle_reset.py defines OracleResetAgent
AUDIT_02 = ARCController imports FailureDiagnoser, ConfidenceEstimator, PermissionGate and PlasticityAllocator names absent from the referenced frozen modules
AUDIT_03 = ARCController and OracleResetAgent write self.state.memory while AgentState defines no memory field
AUDIT_04 = OracleResetAgent.diagnose(true_failure_layer) conflicts with ARCBaseAgent.step() calling diagnose() with no argument
AUDIT_05 = governor/__init__.py imports names absent from governor/permeability.py and imports nonexistent governor/cost.py
AUDIT_06 = arc/permeability/__init__.py imports nonexistent .cost while frozen module is costs.py
AUDIT_07 = evaluation/__init__.py imports recovery_intelligence from a nonexistent recovery_intelligence.py surface; frozen implementation is recovery.py
AUDIT_08 = rahu/generators/__init__.py imports nonexistent curriculum/CurriculumGenerator
AUDIT_09 = RAHUExperiment expects agent.act(observation), while frozen ARC agent contract exposes step(observation)
AUDIT_10 = RAHUExperiment expects environment.observe(), absent from BaseEnvironment
AUDIT_11 = RAHUExperiment tuple-unpacks a four-field step result while frozen environments return StepResult dataclass with observation,reward,terminated,truncated,info
AUDIT_12 = ARC-Full evaluate() is placeholder zeros; baseline/oracle metric constants are implementation constants, not observed measurements
AUDIT_13 = structural namespaces differ across docs, ARCController, diagnosis.py, failure_model.py, layers.py and permeability costs
AUDIT_14 = layer-cost scales differ between layers.py and permeability/costs.py
AUDIT_15 = charter includes a world-model transition in minimum RAHU, while current config/env/generator suite implements four shocks only
```

These audits establish source-level software/interface pressure only:

```text
SOURCE_DEFECT != EXECUTED_FAILURE != REPORTED_NEGATIVE_RESULT != THEORY_FALSIFICATION
```

## 4. Execution/result ceiling

The frozen tree contains executable Python source but no test source, dataset, persisted run, result table, telemetry archive, plot, or benchmark output. GitHub returns zero workflow runs and zero combined-status records at the frozen head.

```text
EXECUTABLE_IMPLEMENTATION          = PRESENT
TEST_SOURCE                        = NONE_ON_FROZEN_SURFACE
PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
SOURCE_REPORTED_EMPIRICAL_RESULTS  = 0
SOURCE_REPORTED_NEGATIVE_RESULTS   = 0
GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
COMBINED_STATUS_RECORDS_AT_HEAD    = 0
```

## 5. Formal and construct variants preserved

The parse keeps distinct, without silent canonicalization:

- five-layer documentary hierarchy versus four- and five-layer implementation namespaces;
- `AttributionEngine` versus `FailureModel` attribution implementations;
- class-based governor permeability versus function-based `arc/permeability` allocation;
- fixed layer-property costs versus `1/3/7/15` permeability costs;
- candidate future-shock/reachable-space `C_future` concepts versus the equal-weight four-component implementation proxy;
- predicted `AAR*≈1` boundary versus phase-point analysis code.

```text
FORMAL_OR_IMPLEMENTATION_VARIANT != IDENTITY != EMPIRICAL_SELECTION
```

## 6. Verdict

```text
SEMANTIC_DEATH_TEST              = PASS
SOURCE_COVERAGE                  = PASS
STANDING_SEPARATION              = PASS
EXECUTION_RESULT_SEPARATION      = PASS
CONSTRUCT_VALIDITY_FIREWALL      = PASS
METADATA_CARDINALITY             = FAIL_LOCAL
REPAIR_SCOPE                     = PART_B_COVERED_PATH_COUNT_ONLY
PARSE_REOPEN_REQUIRED            = NO
SEMANTIC_UNIT_CHANGE_REQUIRED    = NO
STANDING_CHANGE_REQUIRED         = NO
SOURCE_COORDINATE_CHANGE_REQUIRED= NO
NEW_EPISTEMIC_DISTINCTION        = NO
AMENDMENT_005                    = NOT_EARNED
```

Compression remains closed until the local metadata overlay is frozen and the parse retest passes.