# R23 COMPRESSION TRANSPORT — RETEST V0.1

**Base compression:** `R23_COMPRESSION_V0.1.json` + effective Parts A/B  
**Repair overlay:** `R23_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Frozen head:** `a3ef7b068a8b93c1892d082d63f35eaf0eae31b6`

The effective compression inherits all 25 primary items and changes only audit-tainted wording in `R23:C006`. No standing, coordinate, source ownership or count changes.

```text
R23_EFFECTIVE_PARSE_UNITS             = 110
R23_PRIMARY_PROJECTION_ENTRIES        = 110
R23_EFFECTIVE_COMPRESSED_ITEMS        = 25
R23_UNMAPPED_PARSE_UNITS              = 0
R23_DUPLICATE_PRIMARY_OWNERS          = 0
R23_PROJECTION_REMAPS                 = 0
```

## Retest matrix

```text
PRIMARY_SOURCE_ITEM_WITH_AUDIT_QUALIFIER             = CONTAINED
README_ENVIRONMENT_AS_IMPLEMENTATION                 = CONTAINED
HIDDEN_CONTEXT_AS_IMPLEMENTED_HIDDEN_VARIABLE         = CONTAINED
INTERACTION_FEATURE_AS_UNOBSERVED_VARIABLE_DISCOVERY  = CONTAINED
README_HOLDOUT_RULE_AS_ACTUAL_COMMIT_GATE            = CONTAINED
EVALUATOR_AS_HELDOUT_GENERALIZATION_ESTIMATOR         = CONTAINED
ONE_MUTATION_GUARD_AS_EMERGENT_SPARSITY               = CONTAINED
EXECUTABLE_ASSERTION_AS_OBSERVED_PASS                 = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                    = CONTAINED
CTRE_NAME_OVERLAP_AS_CORPUS_IDENTITY                  = CONTAINED
```

No remaining transport hit is found.

## Final R23 verdict

```text
R23_SOURCE_SURFACE                    = FROZEN_FULL_RECURSIVE_HEAD_PLUS_COORDINATE_OVERLAY
R23_FROZEN_HEAD_COMMIT                = a3ef7b068a8b93c1892d082d63f35eaf0eae31b6
R23_TOTAL_BLOB_PATHS                  = 8
R23_UNENUMERATED_PATHS                = 0

R23_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS  = 110
R23_PARSED_REPRESENTATIONS            = 73
R23_EXPLICITLY_UNRESOLVED             = 37
R23_PARSER_FAILURES                   = 0
R23_PRIMARY_LOCALITY_REPAIR           = 1 DEMOTION_OVERLAY

R23_PRIMARY_PROJECTION_ENTRIES        = 110
R23_EFFECTIVE_COMPRESSED_ITEMS        = 25
R23_UNMAPPED_PARSE_UNITS              = 0
R23_DUPLICATE_PRIMARY_OWNERS          = 0
R23_COMPRESSION_SERIALIZATION_REPAIR  = 1
R23_COMPRESSION_WORDING_REPAIR        = 1

R23_IMPLEMENTATION_PRESENT            = 1
R23_TEST_SOURCE_PRESENT               = 0
R23_GITHUB_ACTIONS_RUNS_AT_HEAD       = 0
R23_COMBINED_STATUS_RECORDS_AT_HEAD   = 0
R23_PERSISTED_EXECUTION_RECORDS       = NONE_ON_FROZEN_SURFACE
R23_SOURCE_REPORTED_EMPIRICAL_RESULTS = 0
R23_SOURCE_REPORTED_NEGATIVE_RESULTS  = 0
R23_TEMPORAL_PROVENANCE               = PRESERVED

R23_REUSABLE_NODE_STATE               = EARNED
Z23_EFFECTIVE_NODE_STATE              = EARNED
R23_MAP_EDGE_EMISSION                 = NONE
R23_MAP_AUTHORITY                     = NONE
R23_SCIENTIFIC_AUTHORITY              = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
AMENDMENT_005                         = NOT_EARNED
```

`Z23_EFFECTIVE_NODE_STATE` is the inherited construction:

```text
frozen source surface
+ source-coordinate repair overlay
+ exhaustive parse
+ source-locality demotion overlay/retest
+ source-branch-aware standing-pure compression
+ serialization repair provenance
+ exact 110-unit primary ownership ledger
+ wording repair overlay
+ construct/execution/endpoint secondary audits
+ compression death-test/retest provenance
```

No new neuron ontology is introduced.

## Sequential boundary

```text
Z01_Z23_REUSABLE_NODE_STATE = EARNED
R24_PROGRAM_PARSE_ACCESS    = NEXT_AUTHORIZED_REPOSITORY
R25_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R23 -> R24 semantic relation.
