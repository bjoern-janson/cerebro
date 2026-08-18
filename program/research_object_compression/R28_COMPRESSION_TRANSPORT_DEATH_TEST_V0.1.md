# R28 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/adaptive-inheritance`  
**Frozen head:** `5fce9982cd74ef735ac4b6ffae8e1bdf494b35fa`  
**Effective source surface:** 24 blobs / 23 admitted / 1 scope exclusion  
**Effective parse:** 287 units after pre-manifest serialization repair  
**Projection:** 287 exact primary dispositions  
**Compression:** 61 source-local standing-pure items  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Accounting

```text
R28_EFFECTIVE_SOURCE_PATHS          = 23
R28_EFFECTIVE_PARSE_UNITS           = 287
R28_PARSED_REPRESENTATIONS          = 241
R28_EXPLICITLY_UNRESOLVED           = 46
R28_PRIMARY_PROJECTION_ENTRIES      = 287
R28_PRIMARY_COMPRESSED_ITEMS        = 61
R28_UNMAPPED_PARSE_UNITS            = 0
R28_DUPLICATE_PRIMARY_OWNERS        = 0
R28_EXTRA_PROJECTION_UNITS          = 0
R28_SOURCE_PATH_MISMATCHES          = 0
R28_SOURCE_STANDING_MISMATCHES      = 0
```

Projection completeness passes. The canonical owner-map SHA-256 is `a71635f6435da41c6df3c8b1629dd391ac30482235ac1737c0981b338e6b368d`.

## 2. Compression representation

Each compression item is defined by exactly one source path and one source standing. Its payload is the ordered loss-bounded projection of `NORMALIZED_CONTENT` from exactly the listed `SOURCE_UNITS` in the frozen parse. The item therefore does not require cross-file synthesis or an invented canonical theory statement.

```text
SOURCE_LOCAL_GROUPING != CROSS_SOURCE_SYNTHESIS
SOURCE_UNIT_REFERENCE != LOSS_OF_SOURCE_PAYLOAD
```

Ten items contain one source unit and 51 contain multiple same-path/same-standing units. Source occurrence multiplicity never creates independent warrant.

## 3. Attack matrix

```text
BAD_PARSE_PART_A_AS_EFFECTIVE_COMPRESSION                 = CONTAINED
REFERENCE_DEFINED_PAYLOAD_AS_EMPTY_PAYLOAD                = CONTAINED
CROSS_PATH_GROUPING_AS_CANONICAL_THEORY                   = CONTAINED
CROSS_STANDING_GROUPING_AS_STANDING_COLLAPSE              = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                  = CONTAINED
AIC_AS_EMPIRICALLY_VALIDATED                              = CONTAINED
AUTHORITY_WEIGHT_AS_IDENTIFIED_CAUSAL_AUTHORITY           = CONTAINED
IMPLEMENTED_ATTENUATION_AS_CAUSAL_AUTHORITY_PROOF         = CONTAINED
MRAT_THRESHOLD_ROUTER_AS_CAUSAL_ATTRIBUTION               = CONTAINED
PTVS_FRICTION_AS_FAILURE_ATTRIBUTION                      = CONTAINED
REE_CALLABLE_GATE_AS_VALIDATED_REPRESENTATION_POLICY      = CONTAINED
REE_EXTERNAL_INPUTS_AS_ESTIMATED_QUANTITIES               = CONTAINED
RAHU_METRIC_FUNCTIONS_AS_CONSTRUCT_VALIDITY               = CONTAINED
PLACEHOLDER_STRUCTURAL_DISTANCE_AS_VALIDATED_DISTANCE     = CONTAINED
REFERENCE_AGENT_AS_VALIDATED_CORRIGIBLE_AGENT             = CONTAINED
EXPECTED_ACTION_LABEL_AS_EXECUTED_ADAPTATION              = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                             = CONTAINED
TEST_SOURCE_AS_TEST_PASS                                  = CONTAINED
STALE_TEST_INTERFACE_AS_EXECUTED_FAILURE                  = CONTAINED
IMPLEMENTATION_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT        = CONTAINED
IMPLEMENTATION_DEFECT_AS_THEORY_FALSIFICATION             = CONTAINED
FALSIFICATION_CRITERION_AS_FALSIFICATION_EVENT            = CONTAINED
PROSPECTIVE_ACCEPTANCE_RULE_AS_REPORTED_SUCCESS           = CONTAINED
SOURCE_DEPENDENCY_GRAPH_AS_CEREBRO_EDGE                   = CONTAINED
SOURCE_RELATION_ASSERTION_AS_RESOLVED_ENDPOINT            = CONTAINED
CURRENT_HEAD_AS_COMPLETE_HISTORY                          = CONTAINED
```

No compression-specific semantic failure is found.

## 4. Theory, implementation, measurement and evidence remain separate

R28 has unusually close code/document correspondence for the inheritance attenuation law, but transport does not convert correspondence into construct validity.

```text
THEORETICAL_CAUSAL_AUTHORITY
!= IMPLEMENTED_WEIGHT_VARIABLE
!= VALIDATED_CAUSAL_MEASURE
```

Likewise:

```text
MRAT_ROUTING_CODE != VALIDATED_CAUSAL_ATTRIBUTION
REE_GATE_CODE != VALIDATED_REPRESENTATION_DISCOVERY
ADI_OR_ACS_FUNCTION != VALIDATED_CORRIGIBILITY_CONSTRUCT
```

The 46 unresolved units preserve the missing identification, calibration, threshold, scale and end-to-end validation conditions.

## 5. Software audit remains zero-authority

Frozen-head comparison identifies interface drift and incomplete end-to-end wiring, including:

```text
tests import InheritanceEngine
  while package exports AdaptiveInheritanceEngine

MRAT tests expect context dictionaries / mapping outputs / should_expand_representation
  while router accepts scalar residuals and returns AttributionVector

PTVS tests call compute_lbr(trajectories), evaluate(), get_violations()
  while frozen analyzer exposes a stored-record API

RAHU package root does not export RAHUHarness directly
RAHU tests call evaluate_agent / evaluate_ree_condition and obsolete ARR signatures

RAHU tasks call mechanism(...)
  while frozen Mechanism exposes execute() and no __call__

RAHUHarness.compute_arr requires get_baseline_authority_weight
  while supplied AdaptiveAgent/ReferenceAdaptiveAgent lacks that getter

ReferenceAdaptiveAgent changes mechanism on representation_failure
  but does not attenuate the invalid prior authority weight

RAHU structural distance is 0 for equality and 1 for any inequality
  rather than the documented structural metric

RAHU evaluator does not directly compose the frozen PTVS/MRAT/Inheritance/REE classes
```

These are source-level implementation/interface facts only.

```text
SOFTWARE_AUDIT != RUN_RECORD != TEST_FAILURE != SCIENTIFIC_NEGATIVE
```

## 6. Execution and result ceiling

The frozen source contains documentation, Python implementation, and pytest source. It contains no persisted benchmark result, test report, dataset, or run log. GitHub reports zero workflow runs and zero combined-status records at the frozen head.

```text
IMPLEMENTATION               = PRESENT
TEST_SOURCE                   = PRESENT
PERSISTED_EXECUTION_RECORDS   = NONE_ON_FROZEN_SURFACE
SOURCE_REPORTED_RESULTS       = 0
SOURCE_REPORTED_NEGATIVES     = 0
GITHUB_ACTIONS_RUNS_AT_HEAD   = 0
COMBINED_STATUS_AT_HEAD       = 0
```

Therefore:

```text
IMPLEMENTATION != EXECUTION_RECORD != RESULT
TEST_SOURCE != TEST_RUN != TEST_PASS_OR_FAIL_EVIDENCE
```

## 7. Relation and authority firewall

R28 source documents contain architecture/module and metric dependency relations. Compression retains them at `SOURCE_RELATION_ASSERTION` standing only.

```text
SOURCE_RELATION_ASSERTION != ENDPOINT_IDENTITY != RESOLVED_EDGE != COMPOSITION != AUTHORITY
```

No Cerebro map edge or synapse is emitted.

## 8. Repair locality

R28 required one pre-manifest local archival repair because the first serialized Part A candidate contained stale extra rows despite a 67-unit header. The effective A1/A2 shards contain the already-parsed 67 intended units; the failed candidate remains in lineage.

```text
PRE_MANIFEST_PARSE_SERIALIZATION_REPAIR = PRESENT
SEMANTIC_UNIT_CHANGE                    = NONE
STANDING_CHANGE                         = NONE
SOURCE_COORDINATE_CHANGE                = NONE
POST_PARSE_DEATH_TEST_REPAIR            = NONE
POST_COMPRESSION_DEATH_TEST_REPAIR      = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED      = NO
NEW_GLOBAL_PARSER_ROLE                  = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE    = NONE
AMENDMENT_005                           = NOT_EARNED
```

## 9. Transportability result

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R28_FROZEN_HEADS
```

This is a bounded historical transport claim, not universal validity.

## 10. Final R28 verdict

```text
R28_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD_VIA_NONRECURSIVE_TRAVERSAL
R28_FROZEN_HEAD_COMMIT                 = 5fce9982cd74ef735ac4b6ffae8e1bdf494b35fa
R28_TOTAL_BLOB_PATHS                   = 24
R28_RESEARCH_BEARING_PATHS             = 23
R28_SCOPE_EXCLUDED_PATHS               = 1
R28_UNENUMERATED_PATHS                 = 0

R28_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS   = 287
R28_PARSED_REPRESENTATIONS             = 241
R28_UNRESOLVED_SOURCE_UNITS            = 46
R28_PARSER_FAILURES                    = 0

R28_PRIMARY_PROJECTION_ENTRIES         = 287
R28_PRIMARY_COMPRESSED_ITEMS           = 61
R28_UNMAPPED_PARSE_UNITS               = 0
R28_DUPLICATE_PRIMARY_OWNERS           = 0

R28_EXECUTABLE_IMPLEMENTATION          = PRESENT
R28_TEST_SOURCE                        = PRESENT
R28_PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
R28_SOURCE_REPORTED_EMPIRICAL_RESULTS  = 0
R28_SOURCE_REPORTED_NEGATIVE_RESULTS   = 0
R28_GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
R28_COMBINED_STATUS_RECORDS_AT_HEAD    = 0
R28_TEMPORAL_PROVENANCE                = PRESERVED

R28_REUSABLE_NODE_STATE                = EARNED
Z28_EFFECTIVE_NODE_STATE               = EARNED
R28_MAP_EDGE_EMISSION                  = NONE
R28_MAP_AUTHORITY                      = NONE
R28_SCIENTIFIC_AUTHORITY               = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
AMENDMENT_005                          = NOT_EARNED
```

`Z28_EFFECTIVE_NODE_STATE` is the inherited construction:

```text
frozen source surface
+ exhaustive source-local parse
+ explicit pre-manifest serialization repair lineage
+ parse death-test provenance
+ source-local standing-pure 61-item compression
+ exact 287-entry primary ownership materialization
+ construct-validity / software-interface / evidence ceilings
+ temporal provenance
+ compression transport death-test provenance
```

No new neuron ontology is introduced.

## 11. Sequential boundary

```text
Z01_Z28_REUSABLE_NODE_STATE  = EARNED
R29_PROGRAM_PARSE_ACCESS     = NEXT_AUTHORIZED_REPOSITORY
R30_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R28 -> R29 semantic relation.