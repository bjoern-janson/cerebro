# R20 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R20_COMPRESSION_V0.1.json` + Parts A-C  
**Effective parse:** 289 primary source units  
**Projection ledger:** `R20_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R20 is the first large software-bearing transport surface in the current sequential run. Its principal risk is standing leakage from documentation/configuration/code/tests into execution or scientific result standing.

## 1. Projection accounting

```text
R20_FROZEN_HEAD_PATHS                 = 81
R20_EFFECTIVE_PRIMARY_PARSE_UNITS     = 289
R20_PARSED_REPRESENTATIONS            = 265
R20_UNRESOLVED_SOURCE_UNITS           = 24
R20_PRIMARY_PROJECTION_ENTRIES        = 289
R20_PRIMARY_COMPRESSED_ITEMS          = 191
R20_UNMAPPED_PARSE_UNITS              = 0
R20_DUPLICATE_PRIMARY_OWNERS          = 0
R20_SECONDARY_AUDIT_VIEWS             = 8
R20_DERIVED_BOUNDED_ABSENCES          = 1
R20_TEMPORAL_PROVENANCE_VIEWS         = 1
```

Projection completeness passes.

The projection ledger is explicit by immutable materialization: each compression item freezes its exact `SOURCE_UNITS` array; the ledger freezes the effective parse ID set, declares those arrays as primary ownership records, and defines the deterministic disposition function. No primary mapping depends on an unstated semantic inference.

```text
PROJECTION_ASSERTION_WITHOUT_LEDGER = CONTAINED
REFERENTIAL_LEDGER_WITH_AMBIGUOUS_OWNERSHIP = CONTAINED
```

## 2. Attack matrix

```text
THEORY_AS_IMPLEMENTATION                              = CONTAINED
DOCUMENTED_PROTOCOL_AS_IMPLEMENTED_PROTOCOL           = CONTAINED
CONFIGURATION_AS_RUN_MANIFEST                         = CONTAINED
CONFIGURATION_EXPECTATION_AS_RESULT                   = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                    = CONTAINED
MAIN_DEMO_AS_FULL_EXPERIMENT                          = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                         = CONTAINED
TEST_SOURCE_AS_PASSED_TEST                            = CONTAINED
TEST_SOURCE_DEFECT_AS_OBSERVED_FAILED_TEST            = CONTAINED
RESULT_PLUMBING_AS_RESULT_ARTIFACT                    = CONTAINED
PLOT_CODE_AS_PLOT_ARTIFACT                            = CONTAINED
LOGGER_CAPABILITY_AS_RUN_PROVENANCE                   = CONTAINED
SOURCE_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT            = CONTAINED
IMPLEMENTATION_BUG_AS_THEORY_FALSIFICATION            = CONTAINED
PROXY_IMPLEMENTATION_AS_CONSTRUCT_VALIDATION          = CONTAINED
REWARD_OBJECTIVE_IMPLEMENTATION_AS_MEASUREMENT_VALIDITY = CONTAINED
SAME_CLASS_NAME_AS_SAME_IMPLEMENTATION_OBJECT         = CONTAINED
PROTOCOL_CONFIG_RUNNER_MISMATCH_AS_SILENT_NORMALIZATION = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT              = CONTAINED
CONCEPTUAL_CITATION_AS_PROGRAM_EDGE                   = CONTAINED
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY        = CONTAINED
LOCAL_SOURCE_COORDINATE_REPAIR_AS_RETROACTIVE_CLEANUP = CONTAINED
```

No compression-specific hit is found on the bounded attacks.

## 3. Documentation / configuration / implementation remain distinct

The effective node preserves three independently reconstructible layers:

```text
DOCUMENTED THEORY / BENCHMARK / EXPERIMENT PROTOCOLS
CONFIGURATION SURFACES
EXECUTABLE IMPLEMENTATION
```

They are not normalized into a single implied experiment.

The strongest example is the permeability surface:

```text
protocol: kappa in [0,1], changing-rule environment, repeated trials
config:   kappa 0..2 step .05, 100 trials, save transition outputs
main.py:  kappa 0..2 step .1, deterministic kappa/(1+kappa), no trial loop
```

The compression preserves all three source branches and places their conflict only in a secondary audit.

```text
DOCUMENTED_PROTOCOL_AS_IMPLEMENTED_PROTOCOL = CONTAINED
PROTOCOL_CONFIG_RUNNER_MISMATCH_AS_SILENT_NORMALIZATION = CONTAINED
```

Likewise the agency-transfer protocol/config/main/helper surfaces remain distinct rather than being fused into a claimed 500-episode removal/transfer run.

## 4. Software existence does not create execution standing

R20 contains substantial executable code:

```text
agents
environments
experiment helpers
runner / registry
metrics
models
rewards
trainers
serialization/loggers
visualization
```

But the frozen source surface contains:

```text
persisted result paths = 0
persisted plot paths = 0
GitHub Actions runs on frozen head = 0
combined status records on frozen head = 0
```

The compression therefore emits no execution-record or reported-result primary item.

```text
IMPLEMENTATION_AS_EXECUTION_RECORD = CONTAINED
RESULT_PLUMBING_AS_RESULT_ARTIFACT = CONTAINED
PLOT_CODE_AS_PLOT_ARTIFACT         = CONTAINED
LOGGER_CAPABILITY_AS_RUN_PROVENANCE = CONTAINED
```

The bounded absence does **not** assert that no one ever ran the repository elsewhere. It establishes only that the frozen repository aperture contains no persisted run/result/plot/CI evidence.

## 5. Test source remains test source

The repository contains pytest source. It does not contain a frozen test report.

The compression preserves test code under implementation/method standing and keeps execution standing empty.

One audit notes that `tests/test_agents.py` attempts to instantiate abstract `BaseAgent`. Another notes interface mismatches elsewhere. These are source-level/code-level diagnoses.

They are not represented as:

```text
TEST_FAILED
BENCHMARK_FAILED
THEORY_FAILED
```

because no frozen execution artifact establishes such events.

```text
TEST_SOURCE_AS_TEST_EXECUTION              = CONTAINED
TEST_SOURCE_AS_PASSED_TEST                  = CONTAINED
TEST_SOURCE_DEFECT_AS_OBSERVED_FAILED_TEST = CONTAINED
```

## 6. Implementation defects remain localized

The secondary implementation audit preserves examples including:

```text
environments __all__ names differ from imported classes
experiment registry names/import expectations diverge from current helpers
EvaluationLoop calls act_without_assistance absent from parsed agent classes
AncestorTrainer calls generic update while current agents inherit no-op model update
```

These defects localize to interfaces/implementation at the frozen head.

No research hypothesis is tested merely because the code contains an inconsistency.

```text
SOURCE_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT = CONTAINED
IMPLEMENTATION_BUG_AS_THEORY_FALSIFICATION = CONTAINED
```

## 7. Proxy implementation does not acquire construct validity

The node can reconstruct concrete operational substitutions:

```text
agency/dependency differences and ratios
strategy diversity fractions
independent-action sovereignty fractions
permeability/update ratios
fixed belief-confidence increments
binary revision pressure
weighted ancestor reward
```

It also preserves the particularly strong agency-transfer instrument pressure:

```text
TransferTaskEnv.score() -> 1.0 when independent_reasoning=True
agency-transfer helper supplies independent_reasoning=True
```

and the permeability pressure:

```text
error -> agent.update() -> counted revision
while BaseAgent.update_model may be no-op
```

These facts are carried by the secondary construct-validity audit.

They do not turn prototype metrics into validated measurements.

```text
PROXY_IMPLEMENTATION_AS_CONSTRUCT_VALIDATION = CONTAINED
REWARD_OBJECTIVE_IMPLEMENTATION_AS_MEASUREMENT_VALIDITY = CONTAINED
```

## 8. Same names and repeated theory do not create identity or warrant

Two distinct classes named `ExperimentLogger` have different module paths and semantics. They remain distinct implementation objects.

Theoretical equations and concepts recur across README, formal notation, architecture, formal model, glossary, experiments and predictions. R20 compression deliberately keeps those source branches separate in V0.1.

Therefore:

```text
SAME_CLASS_NAME_AS_SAME_IMPLEMENTATION_OBJECT = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT      = CONTAINED
WARRANT_INDEPENDENCE_STATUS                   = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT                   = NONE
```

## 9. External comparison does not create program topology

Citation and related-framework documents preserve intellectual context and source-described contrasts.

They emit no endpoint identity, support, dependency, lineage or authority relation.

```text
CONCEPTUAL_CITATION_AS_PROGRAM_EDGE = CONTAINED
R20_MAP_EDGE_EMISSION                = NONE
```

## 10. Provenance and repair lineage

R20 preserves two local historical corrections:

```text
SOURCE_SURFACE_AMENDMENT_001
  one wrong src/utils/config.py blob coordinate repaired by overlay

EXHAUSTIVE_PARSE_AMENDMENT_001
  parser/audit deductions demoted from primary source parse
  agency/permeability YAML expected behavior split from configuration standing
```

The bad historical artifacts remain frozen.

```text
LOCAL_SOURCE_COORDINATE_REPAIR_AS_RETROACTIVE_CLEANUP = CONTAINED
```

The effective neuron is reconstructible from base artifacts plus overlays.

## 11. Transportability result

R20 required local archival/parse repairs, but the global parser/compression phenotype was sufficient.

```text
SOURCE_SURFACE_LOCAL_REPAIR        = 1 COORDINATE_ONLY
PARSE_LOCAL_REPAIR                 = 1 SOURCE_AUDIT_SEPARATION_PLUS_EXISTING_MIXED_STANDING_RULE
POST_COMPRESSION_DEATH_TEST_REPAIR = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_GLOBAL_PARSER_ROLE             = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
BASE_PARSE_CONTRACT_AMENDMENT      = NOT_EARNED
AMENDMENT_005                      = NOT_EARNED
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R20_FROZEN_HEADS
```

This is not universal transportability.

## 12. Final R20 verdict

```text
R20_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD_PLUS_LOCAL_COORDINATE_OVERLAY
R20_FROZEN_HEAD_COMMIT                 = 49ca0aec00a6cc90c5e6c99e0c625b5b336f69cc
R20_TOTAL_BLOB_PATHS                   = 81
R20_RESEARCH_BEARING_PATHS             = 81
R20_UNENUMERATED_PATHS                 = 0

R20_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS   = 289
R20_PARSED_REPRESENTATIONS             = 265
R20_UNRESOLVED_SOURCE_UNITS            = 24
R20_PARSER_FAILURES                    = 0

R20_PRIMARY_PROJECTION_ENTRIES         = 289
R20_PRIMARY_COMPRESSED_ITEMS           = 191
R20_UNMAPPED_PARSE_UNITS               = 0
R20_DUPLICATE_PRIMARY_OWNERS           = 0

R20_EXECUTABLE_IMPLEMENTATION          = PRESENT
R20_TEST_SOURCE                        = PRESENT
R20_RESULT_AND_PLOT_PLUMBING           = PRESENT
R20_PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
R20_SOURCE_REPORTED_EMPIRICAL_RESULTS  = NONE_ON_FROZEN_SURFACE
R20_SOURCE_REPORTED_NEGATIVE_RESULTS   = NONE_ON_FROZEN_SURFACE
R20_GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
R20_COMBINED_STATUS_RECORDS_AT_HEAD    = 0
R20_TEMPORAL_PROVENANCE                = PRESERVED

R20_REUSABLE_NODE_STATE                = EARNED
Z20_EFFECTIVE_NODE_STATE               = EARNED
R20_MAP_EDGE_EMISSION                  = NONE
R20_MAP_AUTHORITY                      = NONE
R20_SCIENTIFIC_AUTHORITY               = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
CEREBRO_STEP_2                         = CLOSED
AMENDMENT_005                          = NOT_EARNED
```

`Z20_EFFECTIVE_NODE_STATE` is the inherited construction:

```text
frozen source surface
+ local source-coordinate overlay
+ exhaustive source parse
+ local source/audit + mixed-standing parse overlay
+ standing-pure compression payloads
+ explicit materialized projection ledger
+ execution/protocol/interface/construct audit provenance
+ bounded absence / temporal provenance
+ compression death-test provenance
```

No new top-level neuron ontology is introduced.

## 13. Sequential boundary

```text
Z01_Z20_REUSABLE_NODE_STATE = EARNED
R21_PROGRAM_PARSE_ACCESS    = NEXT_AUTHORIZED_REPOSITORY
R22_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R20 -> R21 semantic relation.

R20 therefore becomes a neuron that can remember a substantial research-code surface — including prototypes, tests, configs, result plumbing, interface defects and construct-validity ceilings — without converting software availability into empirical authority.
