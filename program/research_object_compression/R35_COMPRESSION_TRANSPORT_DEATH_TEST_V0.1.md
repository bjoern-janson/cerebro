# R35 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/dostoevskian-cybernetics`  
**Frozen head:** `f4159b63d0dcdb748f4b9ce6009439103e9a2690`  
**Frozen root tree:** `69753e8f4bc2c3500b1213e788859bad6a3fb596`  
**Effective source surface:** 6 blobs = 5 admitted + 1 explicit exclusion  
**Effective exhaustive parse:** 98 units  
**Effective compression:** 61 items  
**Explicit unresolved compression items:** 5  
**Compression repair:** `R35_COMPRESSION_V0.1_AMENDMENT_001` — cardinality metadata only  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Effective accounting

```text
R35_TOTAL_BLOB_PATHS                     = 6
R35_EFFECTIVE_SOURCE_PATHS               = 5
R35_SCOPE_EXCLUDED_PATHS                 = 1
R35_UNENUMERATED_PATHS                   = 0

R35_EFFECTIVE_PARSE_UNITS                = 98
R35_REPRESENTED_PARSE_UNITS              = 98
R35_EXPLICIT_UNRESOLVED_UNITS            = 5
R35_PARSER_FAILURES                      = 0

R35_PRIMARY_PROJECTION_ENTRIES           = 98
R35_DIRECT_PROJECTION_ENTRIES            = 34
R35_GROUPED_PROJECTION_ENTRIES           = 64
R35_PRIMARY_COMPRESSED_ITEMS             = 61
R35_SINGLETON_COMPRESSED_ITEMS           = 34
R35_GROUPED_COMPRESSED_ITEMS             = 27
R35_UNMAPPED_PARSE_UNITS                 = 0
R35_DUPLICATE_PRIMARY_OWNERS             = 0
R35_EXTRA_PROJECTION_UNITS               = 0
R35_SOURCE_STANDING_MISMATCHES           = 0
```

Canonical projection-pair list SHA-256:

`6c7f307bbf9a77fd4e4950118950e9c2aa9f0e57a0b871a95266b53a238a68d9`

## 2. Compression-repair lineage

The initially persisted compression candidate misstated the item partition as 42 singleton / 19 grouped. The semantic item definitions and source mappings were unchanged.

Local amendment `R35_COMPRESSION_V0.1_AMENDMENT_001` corrects only:

```text
DIRECT_ITEMS:             42 -> 34
LOSS_BOUNDED_GROUP_ITEMS: 19 -> 27
```

with effective parse-unit dispositions:

```text
DIRECT_PARSE_UNITS = 34
GROUPED_PARSE_UNITS = 64
```

Therefore:

```text
COMPRESSION_REPAIR = CARDINALITY_METADATA_ONLY
SEMANTIC_ITEM_CHANGES = 0
SOURCE_STANDING_CHANGES = 0
PROJECTION_MAPPING_CHANGES = 0
UNRESOLVED_STATUS_CHANGES = 0
```

The repair is local and does not earn a new global distinction.

## 3. Proposed-framework / implemented-system firewall

Transport preserves the source's own status:

```text
PROPOSED_FRAMEWORK != IMPLEMENTED_SYSTEM
PROPOSED_CFAE != EXECUTED_CFAE
PROPOSED_BENCHMARK != EXECUTED_BENCHMARK
PROPOSED_METRIC != VALIDATED_MEASUREMENT
```

The frozen repository contains no experiment code, result artifacts, tests, or workflow source.

## 4. README structure / frozen-tree firewall

README describes:

```text
experiments/
results/benchmarks/
```

but the immutable frozen tree contains neither.

Transport preserves both facts without retroactive cleanup:

```text
SOURCE_DESCRIBED_STRUCTURE = PRESENT
PERSISTED_HEAD_STRUCTURE   = ABSENT
TREE_AUTHORITY_FOR_ACTUAL_HEAD_STATE = YES
```

The documentation conflict is evidence about repository state, not evidence that experiments ran elsewhere or never existed elsewhere.

## 5. Execution-lineage firewall

Frozen-head GitHub queries expose:

```text
WORKFLOW_SOURCE_PATHS_VISIBLE_AT_HEAD = 0
PR_TRIGGERED_WORKFLOW_RUNS_VISIBLE_THROUGH_QUERIED_CONNECTOR = 0
COMBINED_STATUS_RECORDS_VISIBLE_THROUGH_QUERIED_CONNECTOR = 0
```

Transport rejects:

```text
ALGORITHM_DESCRIPTION_AS_EXECUTION = CONTAINED
BENCHMARK_DESIGN_AS_RESULT = CONTAINED
ABSENT_HEAD_WORKFLOW_AS_UNIVERSAL_NONEXECUTION_PROOF = CONTAINED
```

## 6. Core hypothesis firewall

The durable source hypothesis is transported only as a hypothesis:

> Error detection and error attribution are distinct; explicit causal attribution before structural revision may improve adaptation efficiency and preservation.

Transport does not convert this into:

```text
EXPLICIT_ATTRIBUTION_IS_NECESSARY = NOT_EARNED
CFAE_OUTPERFORMS_STRONG_ALTERNATIVES = NOT_EARNED
CAUSAL_FAILURE_HIERARCHY_IS_UNIVERSAL = NOT_EARNED
```

`OPEN_QUESTIONS.md` explicitly keeps the explicit-versus-implicit comparison open.

## 7. Failure-hierarchy firewall

The five-level hierarchy is preserved as a proposed taxonomy:

```text
OBSERVATION
INFERENCE
MECHANISM
REPRESENTATION
INTERFACE
```

but transport does not treat semantic levels as empirically separable causal modules.

The source itself leaves one overlap unresolved:

```text
OBSERVATION_MAPPING_CHANGE
-> LEVEL_1 in one formulation
-> LEVEL_3 in another formulation
```

Therefore:

```text
R35Z0058 = UNRESOLVED
```

No compression merge erases that ambiguity.

## 8. Identifiability firewall

Two formal interfaces remain distinct:

```text
TARGET FACTORIZATION: L = L_hat ∘ O
ACTION-CONDITIONED HYPOTHESIS DISCRIMINATION: max_a I(H;O|a) > 0
```

Transport preserves their relation as unestablished:

```text
R35Z0059 = UNRESOLVED
```

No equivalence theorem is manufactured.

## 9. State-observability firewall

CFAE's transition residual reads `s_{t+1}` directly, while the theoretical setup mediates world state through an observation interface.

Transport preserves:

```text
TRANSITION_RESIDUAL_DEFINITION = PRESENT
STATE_ACCESS_CONTRACT = NOT_ESTABLISHED
```

and:

```text
R35Z0060 = UNRESOLVED
```

Thus algorithmic notation is not promoted into an executable observability guarantee.

## 10. Metric firewall

Transport preserves the metric family as proposed mathematical objects only:

```text
A_epistemic
C_improve
K_retain
A_local
optional composite Score
```

It rejects:

```text
FORMULA_AS_VALIDATED_CONSTRUCT = CONTAINED
SYNTHETIC_CORRECT_LABEL_AS_GENERAL_CAUSAL_ORACLE = CONTAINED
OPTIONAL_SCORE_AS_NATURAL_INTELLIGENCE_SCALAR = CONTAINED
```

The source's own no-single-scalar warning remains primary.

## 11. Performance-recovery sign firewall

The source writes:

```text
ΔP_future = integral(R_agent - R_preference) dt
```

while describing `R_preference` as target performance and `ΔP_future` as performance recovery/capability gained.

No sign convention is source-resolved.

```text
R35Z0057 = UNRESOLVED
```

Transport rejects silent inversion or absolute-value normalization.

## 12. Correct-abstention denominator firewall

Correct abstention may require zero structural change, while `C_improve` divides by structural-change magnitude.

No zero-denominator convention is supplied.

```text
R35Z0061 = UNRESOLVED
```

Transport rejects invented epsilon smoothing, arbitrary exclusion, or a hidden alternate metric.

## 13. Open-frontier firewall

The following remain explicitly open:

- scalable failure-hypothesis inference;
- whether explicit attribution beats implicit adaptation under fair capacity control;
- autonomous representation restructuring;
- learned revision cost λ;
- active interface expansion;
- multi-agent contradiction sharing without false authority;
- boundary conditions where attribution is unnecessary overhead.

Transport preserves:

```text
OPEN_PROBLEM != CAPABILITY
PREDICTION != RESULT
PROPOSED_DIRECTION != IMPLEMENTATION
```

## 14. Level-4 / Level-5 authority firewall

The current factorization `{O_hat,T_hat,R_hat}` is supplied by the framework.

Therefore:

```text
FACTORED_MODEL != AUTONOMOUS_REPRESENTATION_DISCOVERY
DETECT_NONIDENTIFIABILITY != INVENT_NEW_INTERFACE
EPISTEMIC_HALT != LEVEL_5_SOLUTION
```

The source explicitly identifies autonomous restructuring and interface expansion as future work.

## 15. Provenance/reopenability firewall

The repository proposes preserving reasons, evidence, falsifiers, discarded alternatives, and reopening paths.

Transport retains these as design requirements only:

```text
PROVENANCE_PROPOSAL != IMPLEMENTED_CAUSAL_MEMORY
REOPENABILITY_PRINCIPLE != DEMONSTRATED_CORRECTION_PATH
```

## 16. Title / literary-authority firewall

The title contains “Dostoevskian,” but the frozen surface contains no Dostoevsky text analysis or evidence-bearing literary interpretation.

Transport emits no claim about Dostoevsky, literary theory, psychology, or historical authorship from the title alone.

## 17. Commit-history firewall

Returned repository history contains seven commits from initial commit through `OPEN_QUESTIONS.md`.

Chronology supports only local developmental provenance:

```text
README -> THEORY -> CFAE -> METRICS -> OPEN QUESTIONS
```

at the level of visible commit creation/update order.

It does not imply:

```text
CHRONOLOGICAL_ADJACENCY = SEMANTIC_EDGE
COMMIT_ORDER = CAUSAL_VALIDATION
```

## 18. Warrant-multiplicity firewall

Repeated statements across README, THEORY, CFAE, and METRICS are compression-grouped only where standing and payload are compatible.

```text
SOURCE_OCCURRENCE_COUNT != WARRANT_INDEPENDENCE
SOURCE_OCCURRENCE_COUNT != WARRANT_MULTIPLICITY
```

Default warrant independence remains `NOT_ESTABLISHED`; multiplicity effect remains `NONE`.

## 19. Source relation / Cerebro-edge firewall

R35 contains conceptual components and internal document relations, but transport emits no cross-repository endpoint identity or graph edge.

```text
CONCEPTUAL_RELATION
!= ENDPOINT_IDENTITY
!= RESOLVED_EDGE
!= COMPOSITION
!= AUTHORITY
```

## 20. Unresolved-set preservation

The terminal unresolved set is exactly:

```text
R35Z0057 performance-recovery sign/normalization
R35Z0058 observation-mapping failure-depth overlap
R35Z0059 target-identifiability vs hypothesis-discrimination relation
R35Z0060 transition-state observability requirement
R35Z0061 C_improve zero-denominator abstention boundary
```

None is treated as a parser failure, and none blocks node transport because the uncertainty itself is preserved as part of the node.

## 21. Transport attack matrix

```text
README_STRUCTURE_AS_PERSISTED_IMPLEMENTATION      = CONTAINED
PROPOSED_CFAE_AS_EXECUTED_MECHANISM               = CONTAINED
PROPOSED_BENCHMARK_AS_EMPIRICAL_RESULT            = CONTAINED
METRIC_FORMULA_AS_VALIDATED_CONSTRUCT              = CONTAINED
EXPLICIT_ATTRIBUTION_AS_PROVEN_NECESSITY          = CONTAINED
FAILURE_TAXONOMY_AS_UNIQUE_CAUSAL_DECOMPOSITION   = CONTAINED
TARGET_FACTORIZATION_AS_MI_EQUIVALENCE_THEOREM    = CONTAINED
TRANSITION_RESIDUAL_AS_OBSERVABLE_IMPLEMENTATION  = CONTAINED
PERFORMANCE_RECOVERY_SIGN_AS_SILENTLY_REPAIRED    = CONTAINED
ZERO_DENOMINATOR_AS_SILENTLY_REGULARIZED          = CONTAINED
CORRECT_ABSTENTION_AS_PERMANENT_REFUSAL            = CONTAINED
FACTORED_MODEL_AS_AUTONOMOUS_REPRESENTATION       = CONTAINED
EPISTEMIC_HALT_AS_INTERFACE_INVENTION              = CONTAINED
OPEN_QUESTION_AS_DEMONSTRATED_CAPABILITY           = CONTAINED
TITLE_AS_LITERARY_EVIDENCE                         = CONTAINED
SOURCE_OCCURRENCE_AS_WARRANT_MULTIPLICITY          = CONTAINED
COMMIT_ORDER_AS_SEMANTIC_TOPOLOGY                  = CONTAINED
```

No transport failure remains.

## 22. Repair locality

```text
SOURCE_SURFACE_REPAIR       = NONE
PARSE_REPAIR                = NONE
COMPRESSION_REPAIR          = R35_COMPRESSION_V0.1_AMENDMENT_001
COMPRESSION_REPAIR_SCOPE    = CARDINALITY_METADATA_ONLY
PROJECTION_REPAIR           = NONE
POST_TRANSPORT_REPAIR       = NONE
NEW_EPISTEMIC_DISTINCTION   = NO
NEW_GLOBAL_PARSER_ROLE      = NONE
AMENDMENT_005               = NOT_EARNED
```

## 23. Transportability result

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R35_FROZEN_HEADS
```

This is a bounded historical transport statement only. It grants no map, propagation, or scientific authority.

## 24. Final R35 verdict

```text
R35_SOURCE_SURFACE                    = FROZEN_COMPLETE_HEAD_TREE
R35_FROZEN_HEAD_COMMIT                = f4159b63d0dcdb748f4b9ce6009439103e9a2690
R35_FROZEN_ROOT_TREE                  = 69753e8f4bc2c3500b1213e788859bad6a3fb596
R35_TOTAL_BLOB_PATHS                  = 6
R35_RESEARCH_BEARING_PATHS            = 5
R35_SCOPE_EXCLUDED_PATHS              = 1
R35_UNENUMERATED_PATHS                = 0

R35_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS  = 98
R35_REPRESENTED_PARSE_UNITS           = 98
R35_UNRESOLVED_SOURCE_UNITS           = 5
R35_PARSER_FAILURES                   = 0

R35_PRIMARY_PROJECTION_ENTRIES        = 98
R35_DIRECT_PROJECTION_ENTRIES         = 34
R35_GROUPED_PROJECTION_ENTRIES        = 64
R35_PRIMARY_COMPRESSED_ITEMS          = 61
R35_UNMAPPED_PARSE_UNITS              = 0
R35_DUPLICATE_PRIMARY_OWNERS          = 0
R35_SOURCE_STANDING_MISMATCHES        = 0

R35_PERSISTED_EXPERIMENT_CODE         = NONE
R35_PERSISTED_RESULT_ARTIFACTS        = NONE
R35_WORKFLOW_SOURCE                   = NONE
R35_PR_TRIGGERED_HEAD_RUNS_QUERIED    = 0
R35_COMBINED_STATUS_RECORDS_QUERIED   = 0
R35_VISIBLE_COMMIT_COUNT              = 7

R35_SOURCE_SURFACE_REPAIR             = NONE
R35_PARSE_REPAIR                      = NONE
R35_COMPRESSION_REPAIR                = R35_COMPRESSION_V0.1_AMENDMENT_001
R35_PROJECTION_REPAIR                 = NONE
R35_POST_TRANSPORT_REPAIR             = NONE
R35_REUSABLE_NODE_STATE               = EARNED
Z35_EFFECTIVE_NODE_STATE              = EARNED
R35_MAP_EDGE_EMISSION                 = NONE
R35_MAP_AUTHORITY                     = NONE
R35_SCIENTIFIC_AUTHORITY              = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
AMENDMENT_005                         = NOT_EARNED
```

`Z35_EFFECTIVE_NODE_STATE` is earned by:

```text
frozen complete 6-blob head surface
+ exhaustive 98-unit parse
+ five explicit unresolved specification boundaries preserved
+ loss-bounded 98 -> 61 compression
+ exact one-owner projection
+ local cardinality-only compression repair
+ no execution/result overclaim
+ successful terminal transport containment
```

**TERMINAL TRANSPORT VERDICT: PASS.**