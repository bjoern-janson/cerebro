# R27 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/axiom-forge-mk1`  
**Frozen head:** `5a488d137c947df8eb8f88fba6dd74fc1b25985c`  
**Effective source surface:** base + source-surface Amendment 001  
**Effective parse:** 156 units  
**Projection:** 156 exact primary dispositions  
**Compression:** 85 source-local standing-pure items  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Accounting

```text
R27_EFFECTIVE_SOURCE_PATHS          = 32
R27_EFFECTIVE_PARSE_UNITS           = 156
R27_PARSED_REPRESENTATIONS          = 131
R27_EXPLICITLY_UNRESOLVED           = 25
R27_PRIMARY_PROJECTION_ENTRIES      = 156
R27_PRIMARY_COMPRESSED_ITEMS        = 85
R27_UNMAPPED_PARSE_UNITS            = 0
R27_DUPLICATE_PRIMARY_OWNERS        = 0
R27_EXTRA_PROJECTION_UNITS          = 0
```

Projection completeness passes.

## 2. Attack matrix

```text
BAD_RECURSIVE_TREE_SNAPSHOT_AS_EFFECTIVE_SOURCE          = CONTAINED
PATH_READ_MISMATCH_AS_SOURCE_FACT                        = CONTAINED
THEORY_OBJECT_AS_IMPLEMENTED_PROXY                       = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_THEORY_OBJECT             = CONTAINED
CONSEQUENCE_MEMORY_AS_CAUSAL_CONSEQUENCE_USE             = CONTAINED
PARAMETER_MUTATION_AS_MECHANISM_LEVEL_RECURSION          = CONTAINED
D_C_CONSTANT_AS_MEASURED_RECURSIVE_DEPTH                 = CONTAINED
MEMORY_RATIO_AS_CAUSAL_C_E                               = CONTAINED
PARAMETER_COUNT_AS_BENEFICIAL_A_C                        = CONTAINED
PRODUCT_PROXY_AS_G_V                                     = CONTAINED
CONFIGURATION_AS_RUN_MANIFEST                            = CONTAINED
OUTPUT_DIRECTORY_CONFIG_AS_PERSISTED_RESULT              = CONTAINED
ROOT_RUNNER_SOURCE_AS_SUCCESSFUL_EXECUTION                = CONTAINED
EXPERIMENT_HELPER_AS_COMPLETE_BENCHMARK                  = CONTAINED
LONG_HORIZON_SOURCE_AS_COMPATIBLE_EXECUTION               = CONTAINED
METRIC_EXPORT_SURFACE_AS_IMPORTABLE_PACKAGE              = CONTAINED
METRIC_IMPLEMENTATION_AS_CONSTRUCT_VALIDITY              = CONTAINED
CORRELATION_AS_CAUSAL_CONSEQUENCE_AUTHORITY              = CONTAINED
SHUFFLE_CONTROL_AS_CAUSAL_IDENTIFICATION                 = CONTAINED
EVENT_CATEGORY_AS_TRUE_RECURSIVE_DEPTH                   = CONTAINED
RETENTION_AS_BENEFICIAL_CONSOLIDATION                    = CONTAINED
VIABILITY_HEURISTIC_AS_FUTURE_ADAPTIVE_CAPACITY          = CONTAINED
COMPOSITE_PRODUCT_AS_VALIDATED_CAUSAL_MODEL              = CONTAINED
HYPOTHESIS_EVALUATOR_AS_COMPLETED_REGRESSION              = CONTAINED
STATISTICAL_HELPER_AS_DOCUMENTED_INFERENCE_DOCTRINE       = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                            = CONTAINED
TEST_SOURCE_AS_TEST_PASS                                 = CONTAINED
REPORT_CODE_AS_GENERATED_REPORT                          = CONTAINED
SOFTWARE_DEFECT_AS_OBSERVED_BENCHMARK_FAILURE            = CONTAINED
SOFTWARE_DEFECT_AS_SCIENTIFIC_NEGATIVE_RESULT            = CONTAINED
SOFTWARE_DEFECT_AS_THEORY_FALSIFICATION                  = CONTAINED
DOCUMENTED_30_PLUS_SEEDS_AS_EXECUTED_EVIDENCE            = CONTAINED
PREDICTION_AS_RESULT                                     = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                 = CONTAINED
CURRENT_HEAD_AS_DEVELOPMENTAL_HISTORY                    = CONTAINED
```

No compression-specific semantic failure is found.

## 3. Observability lineage is preserved rather than erased

R27 exposed a tooling-level conflict before semantic parsing: path/ref and recursive-tree reads returned nested coordinates/content inconsistent with the frozen commit's root tree. The initial source-surface candidate was therefore repaired by a non-recursive root-to-subtree traversal.

The effective node preserves:

```text
bad candidate source-surface artifact
+ explicit source-surface Amendment 001
+ no semantic units generated before repair
```

Thus:

```text
TOOL_OUTPUT_CONFLICT != SOURCE_CHANGE
LOCAL_COORDINATE_REPAIR != RETROACTIVE_CLEANUP
```

## 4. Theory and proxies remain separate

The source theory defines:

```text
D_c = recursive depth
C_e = consequence coupling
A_c = adaptive consolidation
G_V = future/generative viability
D_c*C_e*A_c -> G_V
```

The frozen RECA agent and metrics implement concrete proxies, including fixed depth, count/ratio quantities, event-category estimators, association metrics, retention metrics and trajectory heuristics.

The effective compression never substitutes those proxies back into the theoretical definitions as if construct validity were established.

```text
THEORY_VARIABLE != IMPLEMENTED_PROXY != VALIDATED_MEASURE
```

## 5. Consequence recording does not become causal grounding

`RECAAgent.receive_consequence()` stores consequence information. Candidate modification/evaluation code exists. The compression preserves both literal implementation facts.

The secondary audit additionally records that the frozen modification score is a local parameter heuristic rather than a direct use of the stored consequence value.

Therefore:

```text
CONSEQUENCE_PRESENT != CONSEQUENCE_CAUSALLY_CONTROLS_MODIFICATION
```

No causal authority is granted by field naming.

## 6. Cross-file interface defects remain implementation-local

Frozen-head audit identifies at least these implementation/interface pressures:

```text
root run_experiment.py imports `run_experiment`
  while reca_vs_baseline exposes `compare_agents`

LongHorizonTester expects:
  environment.state
  apply_perturbation()
  evaluate_viability()
  transition.next_state/done/reward
while current GridWorld.step returns numeric reward and lacks those methods

metrics/__init__.py names ViabilityMetric/CompositeRECA-style exports
  while corresponding modules expose different concrete result/function objects

evaluate_reca_hypothesis()
  exposes metadata/hypothesis framing rather than fitting the documented predictive regression
```

These are code/interface observations at the frozen head. No persisted execution artifact establishes that a benchmark/test actually failed because of them.

```text
SOURCE_LEVEL_DEFECT != EXECUTION_FAILURE != EMPIRICAL_NEGATIVE_RESULT
```

## 7. Metric code does not acquire causal/construct authority

R27 contains more measurement machinery than R20 and still transports cleanly because the node preserves its warrant ceilings:

- recursive depth depends on supplied event classification;
- consequence coupling is association-based with shuffle sanity check, not intervention identification;
- adaptive consolidation quantifies retention, not automatically beneficial retention;
- viability is heuristic/trajectory-based;
- composite RECA multiplies proxy components whose common scaling is not established;
- raw correlation labels do not implement the full documented inferential standard.

```text
MEASUREMENT_IMPLEMENTATION != MEASUREMENT_VALIDITY
```

## 8. Evidence ladder remains intact

The frozen head contains:

```text
theory/specification       = PRESENT
configuration              = PRESENT
executable implementation  = PRESENT
test source                = PRESENT
analysis/report plumbing   = PRESENT
persisted benchmark runs   = NONE_ON_FROZEN_SURFACE
persisted test reports     = NONE_ON_FROZEN_SURFACE
reported empirical results = 0
reported negative results  = 0
GitHub workflow runs       = 0
combined status records    = 0
```

Therefore:

```text
IMPLEMENTATION != EXECUTION_RECORD != RESULT
TEST_SOURCE != TEST_RUN != TEST_PASS
REPORT_GENERATOR != GENERATED_REPORT
```

## 9. Documented standard remains prospective

The docs demand repeated seeds, perturbation/ablation controls, effect sizes/uncertainty and structural variables predictive of later viability; the implementation plan calls for approximately 30+ seeds as part of a stronger minimum claim.

No frozen artifact shows those conditions were met.

```text
SPECIFIED_EVIDENCE_STANDARD != SATISFIED_EVIDENCE_STANDARD
```

## 10. Repair locality and ontology pressure

R27 required two pre-compression local archival repairs:

```text
SOURCE_SURFACE_AMENDMENT_001
  full nested blob-coordinate table repaired after observability conflict

EXHAUSTIVE_PARSE_AMENDMENT_001
  Part A covered_paths header repaired to include src/__init__.py
```

Neither required a semantic unit change. Compression itself required no repair.

```text
POST_COMPRESSION_DEATH_TEST_REPAIR     = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED     = NO
NEW_GLOBAL_PARSER_ROLE                 = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE   = NONE
BASE_PARSE_CONTRACT_AMENDMENT          = NOT_EARNED
AMENDMENT_005                          = NOT_EARNED
```

## 11. Transportability result

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R27_FROZEN_HEADS
```

This remains a bounded claim, not universal transportability.

## 12. Final R27 verdict

```text
R27_SOURCE_SURFACE                    = FROZEN_HEAD_PLUS_COORDINATE_OVERLAY
R27_FROZEN_HEAD_COMMIT                = 5a488d137c947df8eb8f88fba6dd74fc1b25985c
R27_EFFECTIVE_BLOB_PATHS              = 32
R27_UNENUMERATED_PATHS                = 0

R27_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS  = 156
R27_PARSED_REPRESENTATIONS            = 131
R27_EXPLICITLY_UNRESOLVED             = 25
R27_PARSER_FAILURES                   = 0

R27_PRIMARY_PROJECTION_ENTRIES        = 156
R27_PRIMARY_COMPRESSED_ITEMS          = 85
R27_UNMAPPED_PARSE_UNITS              = 0
R27_DUPLICATE_PRIMARY_OWNERS          = 0

R27_EXECUTABLE_IMPLEMENTATION         = PRESENT
R27_TEST_SOURCE                       = PRESENT
R27_ANALYSIS_AND_REPORT_PLUMBING      = PRESENT
R27_PERSISTED_EXECUTION_RECORDS       = NONE_ON_FROZEN_SURFACE
R27_SOURCE_REPORTED_EMPIRICAL_RESULTS = 0
R27_SOURCE_REPORTED_NEGATIVE_RESULTS  = 0
R27_GITHUB_ACTIONS_RUNS_AT_HEAD       = 0
R27_COMBINED_STATUS_RECORDS_AT_HEAD   = 0
R27_TEMPORAL_PROVENANCE               = PRESERVED

R27_REUSABLE_NODE_STATE               = EARNED
Z27_EFFECTIVE_NODE_STATE              = EARNED
R27_MAP_EDGE_EMISSION                 = NONE
R27_MAP_AUTHORITY                     = NONE
R27_SCIENTIFIC_AUTHORITY              = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
AMENDMENT_005                         = NOT_EARNED
```

`Z27_EFFECTIVE_NODE_STATE` is the inherited construction:

```text
frozen root commit/tree
+ repaired non-recursive nested source-surface overlay
+ exhaustive source-local parse
+ parse metadata overlay/retest
+ standing-pure source-local compression
+ exact 156-entry primary ownership materialization
+ observability/software-interface/construct-validity/evidence audits
+ bounded absence / temporal provenance
+ compression transport death-test provenance
```

No new neuron ontology is introduced.

## 13. Sequential boundary

```text
Z01_Z27_REUSABLE_NODE_STATE = EARNED
R28_PROGRAM_PARSE_ACCESS    = NEXT_AUTHORIZED_REPOSITORY
R29_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R27 -> R28 semantic relation.
