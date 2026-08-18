# R27 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/axiom-forge-mk1`  
**Frozen head:** `5a488d137c947df8eb8f88fba6dd74fc1b25985c`  
**Effective source surface:** base + `R27_SOURCE_SURFACE_V0.1_AMENDMENT_001.json`  
**Parse candidate:** 131 represented + 25 unresolved = 156 units  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Effective source-surface accounting

```text
FROZEN_HEAD_BLOBS                 = 32
PARSE_INCLUDED                    = 32
PARSE_EXCLUDED_BY_SCOPE           = 0
PARSE_FAILED_PATHS                = 0
PARSE_UNSUPPORTED_PATHS           = 0
UNENUMERATED_PATHS                = 0
```

The source surface used for parsing is the repaired non-recursive-tree traversal. The rejected recursive-tree/path-read snapshot has zero semantic authority.

## 2. Primary parse accounting

```text
PARSED_REPRESENTATIONS            = 131
EXPLICITLY_UNRESOLVED             = 25
CANDIDATE_PARSE_UNITS             = 156
PARSER_FAILURES                   = 0
UNIQUE_SOURCE_PATHS_IN_UNITS      = 32
SOURCE_PATHS_WITHOUT_PRIMARY_UNIT = 0
UNIT_PATHS_OUTSIDE_SOURCE_SURFACE = 0
```

Semantic coverage is complete by path and unit.

## 3. Metadata attack

Part A's `covered_paths` header lists ten paths but contains a valid source unit:

```text
R27P0067 -> src/__init__.py
```

`src/__init__.py` is present in the repaired source surface and has a valid unit; it is missing only from the Part A metadata header.

```text
PRIMARY_SEMANTIC_COVERAGE              = PASS
PART_A_COVERED_PATHS_HEADER_COMPLETENESS = HIT
```

Required repair: add `src/__init__.py` to the effective Part A coverage header by overlay. No unit content, standing, ID, coordinate or path disposition changes.

## 4. Semantic attack matrix

```text
THEORY_VARIABLE_AS_IMPLEMENTED_PROXY                    = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_THEORY_VARIABLE          = CONTAINED
CONSEQUENCE_MEMORY_AS_CONSEQUENCE_CAUSAL_USE            = CONTAINED
PARAMETER_MUTATION_AS_MECHANISM_LEVEL_RECURSION         = CONTAINED
FIXED_D_C_PROXY_AS_MEASURED_RECURSIVE_DEPTH             = CONTAINED
MEMORY_RATIO_AS_CAUSAL_CONSEQUENCE_COUPLING             = CONTAINED
PARAMETER_COUNT_AS_ADAPTIVE_CONSOLIDATION               = CONTAINED
PRODUCT_PROXY_AS_FUTURE_VIABILITY                       = CONTAINED
CONFIGURATION_AS_EXECUTED_RUN                           = CONTAINED
OUTPUT_PATH_AS_PERSISTED_RESULT                         = CONTAINED
ROOT_RUNNER_SOURCE_AS_SUCCESSFUL_EXECUTION               = CONTAINED
EXPERIMENT_HELPER_AS_FULL_BENCHMARK                     = CONTAINED
LONG_HORIZON_SOURCE_AS_COMPATIBLE_EXECUTION              = CONTAINED
METRIC_IMPLEMENTATION_AS_VALID_CAUSAL_MEASUREMENT        = CONTAINED
CORRELATION_AS_CAUSAL_CONSEQUENCE_COUPLING              = CONTAINED
SHUFFLE_SANITY_CHECK_AS_CAUSAL_IDENTIFICATION            = CONTAINED
EVENT_LABEL_AS_TRUE_RECURSIVE_DEPTH                     = CONTAINED
RETENTION_AS_BENEFICIAL_CONSOLIDATION                   = CONTAINED
VIABILITY_HEURISTIC_AS_G_V                              = CONTAINED
COMPOSITE_PRODUCT_AS_VALIDATED_CAUSAL_MODEL             = CONTAINED
STATISTICAL_HELPER_AS_FULL_INFERENCE_PROTOCOL            = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                           = CONTAINED
TEST_SOURCE_AS_TEST_PASS                                = CONTAINED
REPORT_CODE_AS_REPORT_ARTIFACT                          = CONTAINED
IMPLEMENTATION_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT       = CONTAINED
IMPLEMENTATION_DEFECT_AS_THEORY_FALSIFICATION            = CONTAINED
DOCUMENTED_30_SEED_STANDARD_AS_EXECUTED_EVIDENCE         = CONTAINED
PREDICTION_AS_RESULT                                    = CONTAINED
CURRENT_HEAD_AS_DEVELOPMENTAL_HISTORY                   = CONTAINED
```

No semantic parse repair is required.

## 5. Theory and implementation remain separate objects

The source theory defines:

```text
D_c = recursive depth
C_e = consequence coupling
A_c = adaptive consolidation
G_V = future/generative viability
D_c * C_e * A_c -> G_V
```

The executable RECA agent contains implementation proxies with narrower semantics, including a fixed `D_c=1.0`, memory/parameter-count based values, and a local parameter heuristic for modification scoring.

The parser preserves both source layers independently. It does not overwrite the theory with implementation meanings or elevate the proxies to construct-valid measurements.

```text
THEORY_OBJECT != IMPLEMENTED_PROXY
```

## 6. Consequence intake is not equivalent to causal consequence use

The RECA agent stores consequences through `receive_consequence`. That fact remains implementation content.

Whether consequence values actually drive candidate selection/evaluation is a cross-file/code-path audit question. The primary parse does not infer causal grounding from the existence of a consequence-memory field.

```text
CONSEQUENCE_OBSERVED != CONSEQUENCE_CAUSALLY_CONTROLS_MODIFICATION
```

## 7. Metric implementation remains below construct validity

R27 includes executable modules for recursive depth, consequence coupling, adaptive consolidation, viability, composite RECA scoring and statistical helpers.

Those are real implementation artifacts. They do not automatically establish that:

- event labels identify true recursive mechanism depth;
- correlation identifies causal consequence authority;
- retained structure is beneficial adaptive consolidation;
- trajectory heuristics identify future adaptive capacity;
- multiplication of proxy scores is a valid causal model.

The primary parse keeps these semantics separate and explicitly unresolved where the source leaves construct validity open.

## 8. Software audit facts do not become scientific results

Cross-file inspection finds interface/implementation pressures including:

- root runner imports `run_experiment` from a module whose frozen public function surface exposes `compare_agents` rather than that name;
- long-horizon tester expects environment/transition APIs not provided by current `GridWorld`;
- metrics package initializer names exports inconsistent with objects defined in corresponding modules;
- the analysis hypothesis-evaluation helper exposes metadata/hypothesis framing rather than a completed regression test.

These are secondary implementation/interface audits. The frozen source has no execution artifact proving an observed benchmark/test failure, and no such defect is represented as an empirical negative result or theoretical falsification.

```text
SOURCE_LEVEL_DEFECT != EXECUTED_FAILURE != SCIENTIFIC_NEGATIVE_RESULT
```

## 9. Test source remains test source

The frozen head contains `tests/test_metrics.py`, but GitHub exposes:

```text
WORKFLOW_RUNS_AT_HEAD       = 0
COMBINED_STATUS_RECORDS     = 0
PERSISTED_TEST_REPORT_PATHS = 0
```

Thus:

```text
TEST_SOURCE != TEST_EXECUTION != TEST_PASS
```

## 10. Benchmark doctrine remains prospective

The documentation calls for repeated seeds/replicates, perturbation/ablation controls, effect sizes/uncertainty and structural variables that predict later viability. The implementation plan specifies approximately 30+ seeds as part of a stronger definition of done.

No current-head result artifact demonstrates those conditions.

```text
DOCUMENTED_STANDARD != SATISFIED_STANDARD
```

## 11. Death-test verdict

```text
R27_CANDIDATE_PARSE_UNITS              = 156
R27_EFFECTIVE_SEMANTIC_PARSE_UNITS     = 156
R27_PARSED_REPRESENTATIONS             = 131
R27_EXPLICITLY_UNRESOLVED              = 25
R27_PARSER_FAILURES                    = 0
R27_SEMANTIC_REPAIR_REQUIRED           = NO
R27_METADATA_REPAIR_REQUIRED           = PART_A_COVERED_PATHS_HEADER_ONLY
NEW_EPISTEMIC_DISTINCTION_REQUIRED     = NO
NEW_GLOBAL_PARSER_ROLE                 = NONE
BASE_PARSE_CONTRACT_AMENDMENT          = NOT_EARNED
```

Compression remains blocked until the local coverage-header overlay is frozen and the parse retest confirms the same 156-unit semantic object.
