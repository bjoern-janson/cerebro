# R29 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/rahu-benchmark`  
**Frozen head:** `63368297857a1f5d67c7e522f812255c8c84041f`  
**Effective source surface:** 33 blobs / 32 admitted / 1 legal exclusion  
**Effective parse:** 266 units = 201 represented + 65 explicitly unresolved  
**Projection:** 266 exact primary dispositions  
**Compression:** 83 source-local standing-pure items  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Accounting

```text
R29_EFFECTIVE_SOURCE_PATHS          = 32
R29_EFFECTIVE_PARSE_UNITS           = 266
R29_PARSED_REPRESENTATIONS          = 201
R29_EXPLICITLY_UNRESOLVED           = 65
R29_PRIMARY_PROJECTION_ENTRIES      = 266
R29_PRIMARY_COMPRESSED_ITEMS        = 83
R29_DIRECT_PROJECTION_ENTRIES       = 28
R29_GROUP_PROJECTION_ENTRIES        = 238
R29_UNMAPPED_PARSE_UNITS            = 0
R29_DUPLICATE_PRIMARY_OWNERS        = 0
R29_EXTRA_PROJECTION_UNITS          = 0
R29_SOURCE_PATH_MISMATCHES          = 0
R29_SOURCE_STANDING_MISMATCHES      = 0
```

Canonical owner-map SHA-256: `3dc53e94d9edf00e6e8a63fcfe0ad0ceead0c594ba929dfea259f9c3261e6188`.

## 2. Compression representation

Each compression item owns exactly one source path and one source standing. Its effective payload is deterministically materialized by ordered concatenation of the frozen parse `NORMALIZED_CONTENT` for exactly the listed `SOURCE_UNITS`; each item freezes that payload with `PAYLOAD_SHA256`.

```text
SOURCE_LOCAL_GROUPING != CROSS_SOURCE_SYNTHESIS
SOURCE_STANDING_PURITY != STANDING_COLLAPSE
REFERENCE_DEFINED_PAYLOAD != ABSENT_PAYLOAD
SOURCE_OCCURRENCE_MULTIPLICITY != WARRANT_INDEPENDENCE
```

No compression item creates cross-file identity or independent corroboration.

## 3. Attack matrix

```text
DOCUMENTED_AIC_AS_VALIDATED_LAW                         = CONTAINED
DOCUMENTED_ACCEPTANCE_RULE_AS_REPORTED_SUCCESS          = CONTAINED
FALSIFICATION_CRITERION_AS_OBSERVED_FALSIFICATION       = CONTAINED
AUTHORITY_WEIGHT_AS_IDENTIFIED_CAUSAL_AUTHORITY         = CONTAINED
INHERITANCE_DECAY_CODE_AS_CAUSAL_AUTHORITY_PROOF        = CONTAINED
MRAT_THRESHOLD_ROUTER_AS_CAUSAL_ATTRIBUTION             = CONTAINED
GENERATOR_LABEL_AS_REACHABLE_GENERATOR_ROUTING          = CONTAINED
PTVS_FRICTION_AS_FAILURE_ATTRIBUTION                    = CONTAINED
FORMAL_REE_CRITERION_AS_IMPLEMENTATION_IDENTITY         = CONTAINED
REE_GAP_THRESHOLD_AS_VALIDATED_SATURATION_MEASURE       = CONTAINED
IMPLEMENTED_ADI_AS_CANONICAL_DOCUMENT_ADI               = CONTAINED
INVERSE_UPDATE_FREQUENCY_AS_MEASURED_LATENCY            = CONTAINED
RAHU_EVALUATOR_AS_FULL_FIVE_LAYER_COMPOSITION           = CONTAINED
FIXTURE_TELEMETRY_AS_RUN_TELEMETRY                      = CONTAINED
EXPECTED_FIXTURE_VALUES_AS_EMPIRICAL_RESULTS             = CONTAINED
MOCK_AUTHORITY_FIELDS_AS_CAUSAL_MEASUREMENT              = CONTAINED
MOCK_TASK_RESULT_AS_BENCHMARK_VALIDATION                 = CONTAINED
KAPPA_TEST_SOURCE_AS_PHASE_TRANSITION_RESULT             = CONTAINED
KAPPA_EXPECTATION_AS_CRITICAL_KAPPA_ESTIMATE             = CONTAINED
MISSING_KAPPA_MODULE_AS_REPORTED_NEGATIVE                = CONTAINED
STALE_TEST_INTERFACE_AS_EXECUTED_TEST_FAILURE            = CONTAINED
INTEGRATION_TEST_INTENT_AS_END_TO_END_EXECUTION          = CONTAINED
SOFTWARE_DEFECT_AS_THEORY_FALSIFICATION                  = CONTAINED
SOURCE_RELATION_TO_ADAPTIVE_INHERITANCE_AS_ENDPOINT_ID   = CONTAINED
SOURCE_RELATION_ASSERTION_AS_CEREBRO_EDGE                = CONTAINED
CURRENT_HEAD_AS_COMPLETE_HISTORY                         = CONTAINED
```

No compression-specific semantic failure is found.

## 4. Formal and implementation variants remain visible

The documentary and executable surfaces are not silently normalized.

### REE

Documentation specifies representation saturation using bounded-search residual language:

```text
Gamma_hat_Bmax approximately equals e_t
```

Frozen code instead computes:

```text
compressibility_gap = residual_error - max_budget_compressibility
saturated = compressibility_gap > 0.9
```

Therefore:

```text
FORMAL_REE_SATURATION != IMPLEMENTED_GAP_THRESHOLD
```

### ADI

Documentation leaves ADI conceptually dependent on LBR, post-error confidence and structural updating. Frozen code computes a bounded confidence-revision versus authority-revision disconnect.

```text
DOCUMENTARY_ADI != IMPLEMENTED_ADI_VARIANT
```

### Adaptation latency

When no explicit latency is supplied, frozen ACS code uses inverse update frequency.

```text
INVERSE_UPDATE_FREQUENCY != OBSERVED_CONTRADICTION_TO_CORRECTION_LATENCY
```

These are preserved variants/ceilings, not parser conflicts requiring canonicalization.

## 5. Construct-validity firewall

R29 implements variables named authority, attribution, admissibility, structural expansion and corrigibility. Transport preserves the difference between executable proxy and identified construct.

```text
THEORETICAL_CAUSAL_AUTHORITY
!= STORED_AUTHORITY_WEIGHT
!= VALIDATED_CAUSAL_MEASURE

MRAT_ROUTING_CODE
!= IDENTIFIED_FAILURE_CAUSE

REE_GATE_CODE
!= VALIDATED_REPRESENTATION_DISCOVERY

ARR_ADI_ACS_FUNCTIONS
!= VALIDATED_CORRIGIBILITY_CONSTRUCTS
```

The 65 unresolved units retain identification, calibration, estimator and integration gaps.

## 6. Test, fixture and execution firewall

The frozen source contains extensive unit, experiment, fixture and integration test code. Much of it targets APIs absent from or inconsistent with the current implementation. The κ-transition test additionally imports a nonexistent `src.experiments.kappa` module and metric functions absent from frozen `src.rahu.metrics`.

Synthetic fixtures directly encode expected authority/confidence revisions and scenarios. `tests/test_rahu.py` uses a task that writes pre/post authority telemetry directly, rather than deriving those measurements from the tested system state.

These facts retain source-level software/test standing only:

```text
TEST_SOURCE != TEST_EXECUTION != TEST_VERDICT
FIXTURE_TELEMETRY != RUN_TELEMETRY
MOCK_AUTHORITY_FIELD != CAUSALLY_OBSERVED_AUTHORITY
EXPECTED_BEHAVIOR != OBSERVED_BEHAVIOR
SOFTWARE_INTERFACE_DRIFT != EMPIRICAL_NEGATIVE_RESULT
```

## 7. Execution and result ceiling

The frozen repository contains documentation, executable Python, pytest source and synthetic fixtures. It contains no persisted benchmark output, result table, dataset or run log. GitHub returns zero workflow runs and zero combined-status records at the frozen head.

```text
IMPLEMENTATION                         = PRESENT
TEST_SOURCE                            = PRESENT
PERSISTED_EXECUTION_RECORDS            = NONE_ON_FROZEN_SURFACE
SOURCE_REPORTED_EMPIRICAL_RESULTS      = 0
SOURCE_REPORTED_NEGATIVE_RESULTS       = 0
GITHUB_ACTIONS_RUNS_AT_HEAD            = 0
COMBINED_STATUS_RECORDS_AT_HEAD        = 0
```

Thus:

```text
IMPLEMENTATION != EXECUTION_RECORD != RESULT
TEST_SOURCE != TEST_RUN != TEST_PASS_OR_FAIL_EVIDENCE
```

## 8. Relation and authority firewall

R29 explicitly states that Adaptive Inheritance supplies a theoretical framework while RAHU supplies an experimental instrument. That authored relation is retained only at `SOURCE_RELATION_ASSERTION` standing.

```text
SOURCE_RELATION_ASSERTION
!= ENDPOINT_IDENTITY
!= RESOLVED_EDGE
!= COMPOSITION
!= AUTHORITY
```

No Cerebro synapse is emitted.

## 9. Repair locality

R29 required no source-surface repair, no semantic parse repair and no compression repair.

```text
SOURCE_SURFACE_REPAIR                    = NONE
POST_PARSE_DEATH_TEST_REPAIR             = NONE
POST_COMPRESSION_DEATH_TEST_REPAIR       = NONE
SEMANTIC_UNIT_CHANGE                     = NONE
STANDING_CHANGE                          = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED       = NO
NEW_GLOBAL_PARSER_ROLE                   = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE     = NONE
AMENDMENT_005                            = NOT_EARNED
```

## 10. Transportability result

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R29_FROZEN_HEADS
```

This is a bounded historical transport claim, not universal validity.

## 11. Final R29 verdict

```text
R29_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD_VIA_NONRECURSIVE_TRAVERSAL
R29_FROZEN_HEAD_COMMIT                 = 63368297857a1f5d67c7e522f812255c8c84041f
R29_TOTAL_BLOB_PATHS                   = 33
R29_RESEARCH_BEARING_PATHS             = 32
R29_SCOPE_EXCLUDED_PATHS               = 1
R29_UNENUMERATED_PATHS                 = 0

R29_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS   = 266
R29_PARSED_REPRESENTATIONS             = 201
R29_UNRESOLVED_SOURCE_UNITS            = 65
R29_PARSER_FAILURES                    = 0

R29_PRIMARY_PROJECTION_ENTRIES         = 266
R29_PRIMARY_COMPRESSED_ITEMS           = 83
R29_UNMAPPED_PARSE_UNITS               = 0
R29_DUPLICATE_PRIMARY_OWNERS           = 0

R29_EXECUTABLE_IMPLEMENTATION          = PRESENT
R29_TEST_SOURCE                        = PRESENT
R29_PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
R29_SOURCE_REPORTED_EMPIRICAL_RESULTS  = 0
R29_SOURCE_REPORTED_NEGATIVE_RESULTS   = 0
R29_GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
R29_COMBINED_STATUS_RECORDS_AT_HEAD    = 0
R29_TEMPORAL_PROVENANCE                = PRESERVED

R29_REUSABLE_NODE_STATE                = EARNED
Z29_EFFECTIVE_NODE_STATE               = EARNED
R29_MAP_EDGE_EMISSION                  = NONE
R29_MAP_AUTHORITY                      = NONE
R29_SCIENTIFIC_AUTHORITY               = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
AMENDMENT_005                          = NOT_EARNED
```

`Z29_EFFECTIVE_NODE_STATE` is earned by the inherited construction:

```text
frozen 33-blob source surface
+ exhaustive 266-unit source-local parse
+ clean parse death test
+ 83 source-local standing-pure compression items
+ exact 266-entry primary ownership materialization
+ construct-validity / formal-variant / test-fixture / execution ceilings
+ temporal provenance
+ compression transport death-test provenance
```

No new neuron ontology is introduced.

## 12. Sequential boundary

```text
Z01_Z29_REUSABLE_NODE_STATE  = EARNED
R30_PROGRAM_PARSE_ACCESS     = NEXT_AUTHORIZED_REPOSITORY
R31_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R29 -> R30 semantic relation.