# R32 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/arc-reactor`  
**Frozen head:** `16e6972de4f9c5dfb2039baa88d520a41ea7e613`  
**Effective source surface:** 61 blobs / 59 admitted / 2 explicit exclusions  
**Effective parse:** 83 units = 69 represented + 14 explicitly unresolved  
**Effective projection:** 83 primary owners = 69 direct + 14 unresolved-at-compression  
**Effective compression:** 83 source-local standing-pure items  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Accounting

```text
R32_TOTAL_BLOB_PATHS                    = 61
R32_EFFECTIVE_SOURCE_PATHS              = 59
R32_SCOPE_EXCLUDED_PATHS                = 2
R32_UNENUMERATED_PATHS                  = 0

R32_EFFECTIVE_PARSE_UNITS               = 83
R32_PARSED_REPRESENTATIONS              = 69
R32_EXPLICITLY_UNRESOLVED               = 14
R32_PARSER_FAILURES                     = 0

R32_PRIMARY_PROJECTION_ENTRIES          = 83
R32_DIRECT_PROJECTION_ENTRIES           = 69
R32_UNRESOLVED_PROJECTION_ENTRIES       = 14
R32_PRIMARY_COMPRESSED_ITEMS            = 83
R32_UNMAPPED_PARSE_UNITS                = 0
R32_DUPLICATE_PRIMARY_OWNERS            = 0
R32_EXTRA_PROJECTION_UNITS              = 0
R32_SOURCE_PATH_MISMATCHES              = 0
R32_SOURCE_STANDING_MISMATCHES          = 0
```

Canonical owner-map SHA-256:

`caba827dea200d32ddd2eb4bad3386efc8ca1384b75f137fc62ba6d89b4d4247`

## 2. Why compression remains identity-sized

R32's effective parse is already standing-grouped at the lowest source-local level allowed by the frozen contract: one effective unit per source path and source standing, with the unit's locator inventory retaining same-standing distinctions inside the file.

Further reduction would require either:

- merging different source standings, or
- merging different source paths.

Both would erase distinctions that remain relevant to provenance and warrant. Therefore:

```text
83 PARSE UNITS -> 83 COMPRESSION ITEMS
```

is the loss-bounded fixed point for this aperture, not a compression failure.

```text
LOSS_BOUNDED_COMPRESSION != REQUIRED_ITEM_COUNT_REDUCTION
SOURCE_LOCALITY + STANDING_PURITY > FORCED_COMPRESSION_RATIO
```

## 3. Repair lineage

R32 required two local non-semantic repairs before terminal transport.

### Parse metadata repair

`R32_EXHAUSTIVE_PARSE_V0.1_PART_B.json` incorrectly declared `covered_paths=21`; its 45 explicit rows actually span 34 ARC paths.

`R32_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001` changes only:

```text
PART_B_COVERED_PATHS = 21 -> 34
```

The retest passed with no unit, standing, source coordinate, or semantic change.

### Projection-disposition repair

The base projection ledger assigned ordinary `DIRECT_TO_COMPRESSION_ITEM` disposition to all 83 one-to-one owners, including 14 units whose parse disposition is explicitly unresolved.

`R32_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001` changes those 14 primary dispositions to:

```text
UNRESOLVED_AT_COMPRESSION
```

Ownership, item identity, payload, source path/blob and standing remain unchanged. The repair retest passed.

```text
SEMANTIC_UNIT_CHANGE       = NONE
PARSE_STANDING_CHANGE      = NONE
SOURCE_COORDINATE_CHANGE   = NONE
COMPRESSION_PAYLOAD_CHANGE = NONE
OWNER_MAP_CHANGE           = NONE
```

## 4. Transport attack matrix

```text
RESEARCH_PROTOTYPE_AS_VALIDATED_FRAMEWORK                    = CONTAINED
PREDICTION_AS_REPORTED_RESULT                                = CONTAINED
FALSIFICATION_PROTOCOL_AS_OBSERVED_FALSIFICATION             = CONTAINED
SOURCE_EXPECTED_WINNER_METADATA_AS_OBSERVED_WINNER           = CONTAINED
STATIC_AGENT_EVALUATE_CONSTANT_AS_BENCHMARK_RESULT           = CONTAINED
ORACLE_STATIC_ONES_AS_EMPIRICAL_UPPER_BOUND                  = CONTAINED
META_LEARNER_STATIC_PROFILE_AS_OBSERVED_PERFORMANCE          = CONTAINED
ARC_CONTROLLER_PLACEHOLDER_ZEROS_AS_OBSERVED_FAILURE         = CONTAINED
SYNTHETIC_RAHU_SHOCK_AS_EMPIRICAL_VALIDATION                 = CONTAINED
GROUND_TRUTH_FAILURE_LABEL_AS_CAUSAL_DISCOVERY               = CONTAINED
METRIC_IMPLEMENTATION_AS_VALIDATED_CONSTRUCT                 = CONTAINED
AAR_ARITHMETIC_AS_IDENTIFIED_ECONOMIC_QUANTITY               = CONTAINED
C_FUTURE_COMPOSITE_AS_VALIDATED_FUTURE_CAPACITY              = CONTAINED
GAMMA_DISCREPANCY_PROXY_AS_IDENTIFIED_REALITY_COUPLING       = CONTAINED
AE_W_DEPTH_DISTANCE_AS_VALIDATED_CAUSAL_ATTRIBUTION          = CONTAINED
RI_FORMULA_AS_VALIDATED_RECOVERY_INTELLIGENCE                = CONTAINED
RETENTION_PROXY_AS_COMPLETE_STRUCTURAL_RETENTION             = CONTAINED
PHASE_POINT_ANALYSIS_CODE_AS_OBSERVED_PHASE_BOUNDARY         = CONTAINED
AAR_APPROX_1_EXPECTATION_AS_OBSERVED_TRANSITION               = CONTAINED
TELEMETRY_RECORDER_AS_TELEMETRY_ARTIFACT                     = CONTAINED
SERIALIZATION_CAPABILITY_AS_PERSISTED_EXPERIMENT             = CONTAINED
LOGGING_CAPABILITY_AS_EXECUTION_RECORD                       = CONTAINED
EXECUTABLE_SOURCE_AS_SUCCESSFUL_EXECUTION                    = CONTAINED
SOURCE_LEVEL_IMPORT_OR_API_DEFECT_AS_EXECUTED_TEST_FAILURE   = CONTAINED
SOURCE_LEVEL_SOFTWARE_DEFECT_AS_REPORTED_NEGATIVE_RESULT     = CONTAINED
SOFTWARE_DEFECT_AS_THEORY_FALSIFICATION                      = CONTAINED
PLANNED_REPOSITORY_TREE_AS_CURRENT_IMPLEMENTATION            = CONTAINED
CHARTER_WORLD_MODEL_SHOCK_AS_IMPLEMENTED_SHOCK               = CONTAINED
FOUR_IMPLEMENTED_SHOCKS_AS_COMPLETE_MINIMUM_CHARTER_PROTOCOL = CONTAINED
MULTIPLE_LAYER_NAMESPACES_AS_SINGLE_CANONICAL_ONTOLOGY       = CONTAINED
MULTIPLE_ATTRIBUTION_STACKS_AS_SINGLE_IMPLEMENTATION         = CONTAINED
MULTIPLE_PERMEABILITY_STACKS_AS_SINGLE_IMPLEMENTATION        = CONTAINED
SOURCE_RELATION_TO_RAHU_AS_CEREBRO_EDGE                      = CONTAINED
CHRONOLOGICAL_ADDITION_ORDER_AS_CAUSAL_DEPENDENCY            = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                     = CONTAINED
```

No compression-specific semantic failure remains.

## 5. Construct-validity firewall

R32 contains executable proxies for many named theoretical quantities, but their implementation does not validate their intended causal or scientific interpretation.

```text
REALITY_COUPLING_GAMMA
!= DEFAULT_ABSOLUTE_ERROR_OR_THRESHOLD_PROXY
!= VALIDATED_EXTERNAL_INVALIDATION_MEASURE

FAILURE_ATTRIBUTION_P_L_GIVEN_E
!= HEURISTIC_POSTERIOR
!= IDENTIFIED_CAUSAL_FAILURE_LOCATION

AAR_STAR
!= ARITHMETIC_ON_SUPPLIED_COMPONENTS
!= EMPIRICALLY_ESTIMATED_ADAPTIVE_ADVANTAGE

AE_W
!= WEIGHTED_DEPTH_DISTANCE
!= VALIDATED_CAUSAL_ATTRIBUTION_ACCURACY

RI
!= COMPOSITE_RECOVERY_FORMULA
!= VALIDATED_RECOVERY_INTELLIGENCE

C_FUTURE
!= FOUR_COMPONENT_EQUAL_WEIGHT_PROXY
!= IDENTIFIED_FUTURE_ADAPTIVE_CAPACITY
```

The fourteen unresolved parse/compression units preserve these and related operationalization gaps rather than allowing implementation to close them by naming convention.

## 6. Static constants and source expectations remain non-results

Several agents and generators return or encode fixed values:

- `ARCController.evaluate()` returns placeholder zeros;
- ARC-Lite and Oracle Reset return static all-ones metric profiles;
- Flat Optimizer returns static zeros;
- Meta Learner returns a static `.25/.40/.35/.40` profile;
- regime generators attach metadata such as `expected_winner=arc` or `flat_optimizer` and `expected_region=AAR≈1`.

These are implementation constants or predictions.

```text
STATIC_CONSTANT != OBSERVATION
EXPECTED_WINNER != OBSERVED_WINNER
PLACEHOLDER_ZERO != EMPIRICAL_FAILURE
THEORETICAL_CEILING != MEASURED_UPPER_BOUND
```

## 7. Synthetic benchmark firewall

The four current RAHU environments construct controlled synthetic tasks with source-authored ground-truth labels:

```text
parameter drift      depth .10 breadth .10
representation shift depth .40 breadth .35
rule inversion       depth .75 breadth .70
attribution ambiguity depth .90 breadth .85
```

Those labels make attribution measurable *inside the benchmark design*. They do not establish that the structural labels correspond to causal mechanisms in external systems.

```text
SYNTHETIC_GROUND_TRUTH != EXTERNALLY_IDENTIFIED_CAUSAL_STRUCTURE
BENCHMARK_IMPLEMENTATION != BENCHMARK_VALIDATION
ENVIRONMENT_CODE != EXPERIMENT_RESULT
```

The R&D charter additionally requires a world-model transition in its minimum shock suite, while the frozen environment/config/generator implementation exposes only four current shocks. Both facts are preserved.

## 8. Implementation-variant firewall

R32 contains multiple explicit implementation surfaces that share conceptual names but are not silently collapsed:

- documentary hierarchy: parameter / representation / rule / world-model / ontology;
- `AttributionEngine`: five-layer enum;
- `FailureModel`: theta / representation / grammar / ontology;
- `layers.py`: theta / M / G_O / C / Omega;
- `ARCController`: parameter / representation / operator / ontology;
- permeability cost model: theta / representation / grammar / ontology.

It also contains:

- `AttributionEngine` and `FailureModel` as distinct attribution implementations;
- class-based `governor/permeability.py` and function-based `arc/permeability/allocation.py`;
- layer-property costs `.1/.3/.5/.75/1.0` and a separate `1/3/7/15` cost table.

```text
NAME_OVERLAP != OBJECT_IDENTITY
FORMAL_VARIANT != SILENT_CANONICALIZATION
IMPLEMENTATION_MULTIPLICITY != INDEPENDENT_WARRANT
```

## 9. Secondary software audit ceiling

Cross-file comparison identifies source-level interface defects, including:

1. `OracleReset` export versus `OracleResetAgent` definition;
2. ARCController imports of absent `FailureDiagnoser`, `ConfidenceEstimator`, `PermissionGate`, and class `PlasticityAllocator` names;
3. use of missing `AgentState.memory`;
4. Oracle diagnose signature mismatch with the base step loop;
5. governor initializer imports absent permeability names and nonexistent `governor/cost.py`;
6. permeability initializer references `.cost` while frozen module is `costs.py`;
7. evaluation initializer references a nonexistent `recovery_intelligence.py` surface;
8. generator initializer references nonexistent `curriculum.py`/`CurriculumGenerator`;
9. RAHU runner expects `agent.act()` while ARC contract exposes `step()`;
10. RAHU runner expects `environment.observe()`, absent from the environment base;
11. RAHU runner expects tuple-style four-field environment step output while environments return `StepResult` with observation/reward/terminated/truncated/info.

These remain software audit facts only:

```text
SOURCE_DEFECT
!= EXECUTION_RECORD
!= TEST_FAILURE
!= REPORTED_NEGATIVE_RESULT
!= THEORY_FALSIFICATION
```

## 10. Execution and result ceiling

The frozen repository contains substantial executable Python source, but no test source, dataset, persisted benchmark output, telemetry archive, result table, figure, or run log. GitHub returns zero Actions workflow runs and zero combined-status records at the frozen head.

```text
EXECUTABLE_IMPLEMENTATION          = PRESENT
TEST_SOURCE                        = NONE_ON_FROZEN_SURFACE
PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
SOURCE_REPORTED_EMPIRICAL_RESULTS  = 0
SOURCE_REPORTED_NEGATIVE_RESULTS   = 0
GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
COMBINED_STATUS_RECORDS_AT_HEAD    = 0
```

Therefore:

```text
THEORY != IMPLEMENTATION != EXECUTION_RECORD != RESULT
RUNNER_SOURCE != SUCCESSFUL_RUN
TELEMETRY_SCHEMA != TELEMETRY_RECORD
RESULT_SERIALIZATION_CODE != RESULT_ARTIFACT
```

## 11. Temporal provenance

The visible repository history contains 61 commits from the initial commit through the final R&D charter. It shows a rapid sequence of README, ARC component, RAHU component, utility and charter additions. This order is preserved as developmental provenance only.

```text
CURRENT_HEAD != COMPLETE_CAUSAL_HISTORY
HISTORICAL_ADDITION_ORDER != CAUSAL_DEPENDENCY
CHRONOLOGICAL_ADJACENCY != SEMANTIC_EDGE
```

## 12. Repair locality

```text
SOURCE_SURFACE_REPAIR                         = NONE
PARSE_METADATA_REPAIR                         = R32_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001
PARSE_RETEST                                  = PASS
PROJECTION_DISPOSITION_REPAIR                 = R32_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001
PROJECTION_REPAIR_RETEST                      = PASS
POST_TRANSPORT_COMPRESSION_REPAIR             = NONE
SEMANTIC_UNIT_CHANGE                          = NONE
PARSE_STANDING_CHANGE                         = NONE
SOURCE_COORDINATE_CHANGE                      = NONE
COMPRESSION_PAYLOAD_CHANGE                    = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED            = NO
NEW_GLOBAL_PARSER_ROLE                        = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE          = NONE
AMENDMENT_005                                 = NOT_EARNED
```

## 13. Transportability result

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R32_FROZEN_HEADS
```

This remains a bounded historical transport claim, not universal validity.

## 14. Final R32 verdict

```text
R32_SOURCE_SURFACE                    = FROZEN_FULL_RECURSIVE_HEAD_VIA_NONRECURSIVE_TRAVERSAL
R32_FROZEN_HEAD_COMMIT                = 16e6972de4f9c5dfb2039baa88d520a41ea7e613
R32_TOTAL_BLOB_PATHS                  = 61
R32_RESEARCH_BEARING_PATHS            = 59
R32_SCOPE_EXCLUDED_PATHS              = 2
R32_UNENUMERATED_PATHS                = 0

R32_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS  = 83
R32_PARSED_REPRESENTATIONS            = 69
R32_UNRESOLVED_SOURCE_UNITS           = 14
R32_PARSER_FAILURES                   = 0

R32_PRIMARY_PROJECTION_ENTRIES        = 83
R32_DIRECT_PROJECTION_ENTRIES         = 69
R32_UNRESOLVED_PROJECTION_ENTRIES     = 14
R32_PRIMARY_COMPRESSED_ITEMS          = 83
R32_UNMAPPED_PARSE_UNITS              = 0
R32_DUPLICATE_PRIMARY_OWNERS          = 0
R32_SOURCE_STANDING_MISMATCHES        = 0

R32_EXECUTABLE_IMPLEMENTATION         = PRESENT
R32_TEST_SOURCE                       = NONE_ON_FROZEN_SURFACE
R32_PERSISTED_EXECUTION_RECORDS       = NONE_ON_FROZEN_SURFACE
R32_SOURCE_REPORTED_EMPIRICAL_RESULTS = 0
R32_SOURCE_REPORTED_NEGATIVE_RESULTS  = 0
R32_GITHUB_ACTIONS_RUNS_AT_HEAD       = 0
R32_COMBINED_STATUS_RECORDS_AT_HEAD   = 0
R32_TEMPORAL_PROVENANCE               = PRESERVED_61_COMMITS

R32_PARSE_LOCAL_REPAIR                = APPLIED_AND_RETESTED_PASS
R32_PROJECTION_LOCAL_REPAIR           = APPLIED_AND_RETESTED_PASS
R32_POST_TRANSPORT_REPAIR             = NONE
R32_REUSABLE_NODE_STATE               = EARNED
Z32_EFFECTIVE_NODE_STATE              = EARNED
R32_MAP_EDGE_EMISSION                 = NONE
R32_MAP_AUTHORITY                     = NONE
R32_SCIENTIFIC_AUTHORITY              = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
AMENDMENT_005                         = NOT_EARNED
```

`Z32_EFFECTIVE_NODE_STATE` is earned by:

```text
frozen 61-blob source surface
+ exhaustive 83-unit standing-grouped source-local parse
+ local parse-cardinality repair and successful retest
+ identity-sized 83-item loss-bounded compression
+ exact 83-entry one-owner projection
+ local unresolved-disposition repair and successful retest
+ construct/static-value/synthetic-benchmark/software-defect/execution ceilings
+ 61-commit temporal provenance
+ terminal compression transport death-test provenance
```

No new neuron ontology is introduced.

## 15. Sequential boundary

```text
Z01_Z32_REUSABLE_NODE_STATE  = EARNED
R33_PROGRAM_PARSE_ACCESS     = NEXT_AUTHORIZED_REPOSITORY
R34_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R32 -> R33 semantic relation.