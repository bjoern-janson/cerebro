# R24 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/ree`  
**Frozen head:** `855432a9f55be699e2747e7aaea38a34285cf5a8`  
**Effective exhaustive parse:** 115 units  
**Compression:** `R24_COMPRESSION_V0.1.json`  
**Projection ledger:** `R24_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Derivation accounting

```text
R24_FROZEN_HEAD_BLOB_PATHS          = 4
R24_ADMITTED_RESEARCH_PATHS          = 3
R24_EXCLUDED_LEGAL_PATHS             = 1
R24_EFFECTIVE_PARSE_UNITS            = 115
R24_PARSED_REPRESENTATIONS           = 87
R24_EXPLICITLY_UNRESOLVED            = 28
R24_PRIMARY_PROJECTION_ENTRIES       = 115
R24_PRIMARY_COMPRESSED_ITEMS         = 37
R24_UNMAPPED_PARSE_UNITS             = 0
R24_DUPLICATE_PRIMARY_OWNERS         = 0
R24_EXTRA_PROJECTION_UNITS           = 0
```

Projection completeness passes. Every effective parse unit has exactly one primary compression owner.

## 2. Attack matrix

```text
REPORTED_RESULT_AS_EXECUTION_RECORD                         = CONTAINED
REPORTED_RESULT_AS_REPRODUCED_RESULT                        = CONTAINED
REPORTED_RESULT_AS_INSTRUMENT_LINEAGE                       = CONTAINED
SOURCE_REPORTED_NEGATIVE_RESULT_AS_EXECUTION_ARTIFACT       = CONTAINED
SOURCE_REPORTED_IMPLEMENTATION_AS_FROZEN_IMPLEMENTATION     = CONTAINED
README_DESCRIBED_STRUCTURE_AS_FROZEN_IMPLEMENTATION         = CONTAINED
ABSENT_INSTRUMENT_AS_FALSE_REPORTED_RESULT                   = CONTAINED
ABSENT_INSTRUMENT_AS_NO_EXECUTION_EVER                       = CONTAINED
PERSISTENT_ERROR_AS_IDENTIFIED_REPRESENTATION_FAILURE       = CONTAINED
TORSION_THRESHOLD_AS_VALIDATED_INTERFACE_DIAGNOSTIC         = CONTAINED
FIXED_CANDIDATE_FAMILY_AS_OPEN_ENDED_INTERFACE_INVENTION    = CONTAINED
INTERACTION_SELECTION_AS_GENERAL_CAUSAL_DISCOVERY           = CONTAINED
LOCAL_SYNTHETIC_RESULT_AS_GENERAL_INTERFACE_INVENTION       = CONTAINED
THREE_SEEDS_AS_INDEPENDENT_REPLICATION                      = CONTAINED
README_VALIDATION_RECURRENCE_AS_INDEPENDENT_WARRANT         = CONTAINED
STABILIZATION_DESCRIPTION_AS_PERSISTED_REPAIR_CODE          = CONTAINED
PROJECT_METADATA_AS_NEW_TOP_LEVEL_COORDINATE                = CONTAINED
SOURCE_REPORTED_IMPLEMENTATION_AS_NEW_TOP_LEVEL_COORDINATE  = CONTAINED
CTRE_SIMULATOR_AS_R23_ENDPOINT                              = CONTAINED
CONNECTED_PROJECT_REFERENCE_AS_PROGRAM_EDGE                 = CONTAINED
EXTERNAL_VALIDATED_PROTOTYPE_STATUS_AS_R24_EVIDENCE         = CONTAINED
CURRENT_HEAD_AS_DEVELOPMENTAL_HISTORY                       = CONTAINED
TEMPORARY_REQUIREMENTS_PATH_AS_CURRENT_IMPLEMENTATION       = CONTAINED
UNRESOLVED_FRAGMENT_AS_FALSE_CLAIM                          = CONTAINED
UNRESOLVED_FRAGMENT_AS_PARSER_FAILURE                       = CONTAINED
```

No compression-specific failure is found.

## 3. R24 preserves a source-reported result without fabricating execution lineage

The effective compression contains source-reported empirical results from both `README.md` and `docs/validation.md`, including:

```text
Seed 42  -> post-shift MSE 0.04105, representation size 3, mutations 1
Seed 123 -> post-shift MSE 0.04234, representation size 3, mutations 1
Seed 789 -> post-shift MSE 0.04309, representation size 3, mutations 1
Average post-shift MSE -> 0.04216
```

and qualitative reported outcomes for pressure detection, hypothesis generation/selection, representation expansion, stabilization, and restored performance.

Those statements remain under `REPORTED_RESULTS / REPORTED_EMPIRICAL_RESULT` standing because the source explicitly reports them as validation results.

The same frozen head contains no executable instrument, raw data, run log, checkpoint, test report, CI record, or result artifact outside the Markdown report from which the experiment can be reconstructed.

Therefore the effective node preserves simultaneously:

```text
SOURCE_REPORTED_EMPIRICAL_RESULT = PRESENT
PERSISTED_EXECUTION_RECORD       = NONE_ON_FROZEN_SURFACE
INSTRUMENT_LINEAGE               = NOT_RECONSTRUCTIBLE_FROM_FROZEN_SURFACE
REPRODUCTION_INDEPENDENCE        = NOT_ESTABLISHED
```

The absence ceiling does not erase the reported result; the reported result does not erase the provenance ceiling.

## 4. Reported negative result remains provenance-limited

`docs/validation.md` reports that the first implementation repeatedly committed the same hypothesis despite successful expansion, followed by a stabilization mechanism and a reduction from thousands of repeated commits to one structural transition.

Compression preserves:

```text
R24:C035 = REPORTED_NEGATIVE_RESULT
R24:C034 = SOURCE_REPORTED_IMPLEMENTATION description
R24:C036 = REPORTED_EMPIRICAL_RESULT after stabilization
```

The repair implementation and corresponding execution records are not persisted in the frozen repository.

Therefore:

```text
REPORTED_NEGATIVE_RESULT != EXECUTION_ARTIFACT
REPORTED_REPAIR          != PERSISTED_REPAIR_CODE
```

## 5. Source-described implementation remains distinct from implementation presence

The validation document names `REEAgent`, a torsion tracker, `AnonymousHypothesisGenerator`, selection behavior, and stabilization logic. The README also describes a repository structure containing:

```text
agent.py
environment.py
hypotheses.py
tracker.py
evaluator.py
experiments/phase_transition.py
```

None of those paths exists at the frozen head. The visible six-commit history contains no commit adding them.

The compression therefore carries implementation descriptions through the existing `SOURCE_DESCRIBED_STATUS` coordinate with `SOURCE_REPORTED_IMPLEMENTATION` or `PROJECT_PROCESS_METADATA` standing.

It does not emit an `EXECUTABLE_IMPLEMENTATION` item.

```text
SOURCE_REPORTED_IMPLEMENTATION != FROZEN_IMPLEMENTATION_PRESENT
SOURCE_DESCRIBED_TREE           != FROZEN_TREE
```

No new top-level coordinate is needed.

## 6. Failure diagnosis remains weaker than interface identification

The compressed theory branch retains:

```text
prediction failure
-> torsion / representational pressure
-> structural discovery
-> representation expansion
```

while the unresolved branch retains that persistent error is not uniquely diagnostic of representation insufficiency and that torsion lacks a frozen estimator/calibration protocol.

Thus:

```text
ERROR_SIGNAL != IDENTIFIED_REPRESENTATION_FAILURE
TORSION_THRESHOLD_0_01 != VALIDATED_DIAGNOSTIC_BOUNDARY
```

The result report demonstrates only the source-described local experiment; it does not upgrade the general diagnostic mechanism beyond the evidence preserved by that source.

## 7. Candidate selection does not acquire Level-3 invention standing

The source explicitly lists a candidate family:

```text
null
augment
interaction
```

and reports selection of the interaction candidate in a synthetic environment whose target changes to `velocity * context`.

Compression preserves the source term `autonomous hypothesis generation` while retaining the unresolved distinction between:

```text
selection among predefined structural primitives
```

and:

```text
open-ended invention of an unavailable representation primitive
```

Therefore no general interface-invention, causal-discovery, or cross-domain authority is emitted.

## 8. Repeated reported values do not multiply warrant

The README and validation document repeat the same three seed-level values and success narrative. The three seeds also belong to one source-described experimental lineage.

Compression preserves all occurrences but does not interpret them as independent replication.

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

## 9. Relation assertions remain pre-topological

`docs/ecosystem.md` explicitly relates REE to named projects/concepts including `CTRE Simulator`, Interface-Induced Computational Geometry, Computational Phase Boundaries, Resolution Horizon, Causal Permeability, and Causal Mass.

The relation item is retained under `EXPLICIT_CROSS_REPOSITORY_REFERENCES` but no endpoint is bound to a Cerebro repository node.

In particular:

```text
CTRE Simulator name overlap != R23 identity
SOURCE_RELATION_ASSERTION    != ENDPOINT_IDENTITY
ENDPOINT_IDENTITY            != PROGRAM_EDGE
```

The source-described `Validated prototype` status of CTRE Simulator remains a statement about an unresolved external endpoint and supplies no R24 scientific warrant.

## 10. Bounded absence and temporal provenance remain reconstructible

The frozen head contains three admitted research Markdown files plus the explicitly excluded license. It contains no current executable/data/test/run surface.

The development history separately records a temporary one-line `requirements.txt` containing `numpy>=1.26.0`, later removed when `docs/ecosystem.md` was created.

That historical dependency path neither disappears from provenance nor becomes current implementation evidence.

```text
CURRENT_HEAD_PARSE != DEVELOPMENTAL_HISTORY
```

## 11. Transportability result

R24 required no parse repair and no compression repair.

```text
POST_PARSE_DEATH_TEST_REPAIR           = NONE
POST_COMPRESSION_DEATH_TEST_REPAIR     = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED     = NO
NEW_GLOBAL_PARSER_ROLE                 = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE   = NONE
BASE_PARSE_CONTRACT_AMENDMENT          = NOT_EARNED
AMENDMENT_005                          = NOT_EARNED
```

Bounded transport claim:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R24_FROZEN_HEADS
```

This is not a universal transportability claim.

## 12. Final R24 verdict

```text
R24_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD
R24_FROZEN_HEAD_COMMIT                 = 855432a9f55be699e2747e7aaea38a34285cf5a8
R24_TOTAL_BLOB_PATHS                   = 4
R24_RESEARCH_BEARING_PATHS             = 3
R24_EXCLUDED_LEGAL_PATHS               = 1
R24_UNENUMERATED_PATHS                 = 0

R24_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS   = 115
R24_PARSED_REPRESENTATIONS             = 87
R24_EXPLICITLY_UNRESOLVED              = 28
R24_PARSER_FAILURES                    = 0

R24_PRIMARY_PROJECTION_ENTRIES         = 115
R24_PRIMARY_COMPRESSED_ITEMS           = 37
R24_UNMAPPED_PARSE_UNITS               = 0
R24_DUPLICATE_PRIMARY_OWNERS           = 0

R24_EXECUTABLE_IMPLEMENTATION          = NONE_ON_FROZEN_SURFACE
R24_TEST_SOURCE                        = NONE_ON_FROZEN_SURFACE
R24_PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE
R24_SOURCE_REPORTED_EMPIRICAL_RESULTS  = PRESENT
R24_SOURCE_REPORTED_NEGATIVE_RESULTS   = PRESENT
R24_REPORTED_RESULT_DOCUMENT           = docs/validation.md
R24_INSTRUMENT_LINEAGE                 = NOT_RECONSTRUCTIBLE_FROM_FROZEN_SURFACE
R24_GITHUB_ACTIONS_RUNS_AT_HEAD        = 0
R24_COMBINED_STATUS_RECORDS_AT_HEAD    = 0
R24_TEMPORAL_PROVENANCE                = PRESERVED

R24_REUSABLE_NODE_STATE                = EARNED
Z24_EFFECTIVE_NODE_STATE               = EARNED
R24_MAP_EDGE_EMISSION                  = NONE
R24_MAP_AUTHORITY                      = NONE
R24_SCIENTIFIC_AUTHORITY               = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
AMENDMENT_005                          = NOT_EARNED
```

`Z24_EFFECTIVE_NODE_STATE` is the inherited construction:

```text
frozen source surface
+ exhaustive source parse
+ parse death-test provenance
+ standing-pure source-local compression
+ exact 115-entry projection ledger
+ result/execution/instrument-lineage audit
+ representation-failure / autonomy / generalization audits
+ unresolved endpoint and recurrence audits
+ bounded absence / temporal provenance
+ compression transport death-test provenance
```

No new neuron ontology is introduced.

## 13. Sequential boundary

```text
Z01_Z24_REUSABLE_NODE_STATE = EARNED
R25_PROGRAM_PARSE_ACCESS    = NEXT_AUTHORIZED_REPOSITORY
R26_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R24 -> R25 semantic relation.
