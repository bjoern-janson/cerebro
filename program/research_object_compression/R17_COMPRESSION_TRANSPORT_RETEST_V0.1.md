# R17 COMPRESSION TRANSPORT — RETEST V0.1

**Death test:** `R17_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Repair:** `R17_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Projection accounting non-regression

```text
R17_RESEARCH_SOURCE_PATHS           = 2
R17_EFFECTIVE_PRIMARY_PARSE_UNITS   = 231
R17_PARSED_REPRESENTATIONS          = 210
R17_UNRESOLVED_SOURCE_UNITS         = 21
R17_PRIMARY_PROJECTION_ENTRIES      = 231
R17_PRIMARY_COMPRESSED_ITEMS        = 88
R17_UNMAPPED_PARSE_UNITS            = 0
R17_DUPLICATE_PRIMARY_OWNERS        = 0
R17_DERIVED_AUDIT_VIEWS             = 3
R17_DERIVED_BOUNDED_ABSENCES        = 1
PRIMARY_PROJECTION_CHANGES_IN_REPAIR = 0
```

## 2. Standing-leak repair

`R17:FORMAL:RAD_GENERATOR_IMPROVEMENT` now contains only the formal transition owned by `R17:P:B048`:

```text
G_m -> Gbar_m
```

Normal improvement, evolutionary improvement, higher-order machinery meaning, and the definition/exclusions of Omega remain owned by:

```text
R17:DEF:RAD_GENERATOR_IMPROVEMENT
standing = DEFINITION
```

```text
PRIMARY_ITEM_STANDING_LEAK = REPAIRED
```

No parse owner moved.

## 3. Loss-bound repair

The amended summaries now explicitly preserve all distinctions owned by:

```text
R17:ASSERT:META_CAUSAL_ACCESS
R17:ASSERT:RAD_CORE
R17:DEF:RAD_GENERATOR_IMPROVEMENT
```

including:

```text
open-endedness != mere change
trajectory moves through a space
open recursion lets reality participate in future-rule change
lineage changes the evolutionary space
RAD causal target != merely whether adaptation occurs
normal improvement = C increases
evolutionary improvement = G_m increases
higher-order improvement changes improvement machinery
Omega improvement-rate definition and exclusions
```

```text
MAPPED_DISTINCTION_DROPPED_BY_GROUPING = REPAIRED
```

## 4. Framework identity non-regression

The effective node preserves two source-local framework identities:

```text
README.md   -> Meta-Process Framework
README_2.md -> proposed Recursive Adaptive Dynamics (RAD)
```

Semantic overlap does not create identity equivalence.

The only cross-file identity comparison remains:

```text
R17:AUDIT:FRAMEWORK_IDENTITY_EQUIVALENCE
AUTHORITY_EFFECT = NONE
MAP_EDGE_EFFECT = NONE
```

```text
FRAMEWORK_OVERLAP_AS_IDENTITY_COLLAPSE = CONTAINED
```

## 5. Experimental-standing non-regression

The effective node preserves:

```text
CTC benchmark  = SPECIFICATION_ONLY
RVT001         = EXPERIMENT_SPECIFICATION_ONLY
RAD simulator  = SIMULATOR_SPECIFICATION_AND_PREDICTION_ONLY
```

The frozen repository head contains no executable implementation, persisted execution artifact, dataset, notebook, or reported-result document.

That bounded absence remains secondary audit/provenance information and does not become file-local source content.

```text
EXPERIMENT_SPEC_AS_REPORTED_RESULT   = CONTAINED
PREDICTION_AS_EXECUTION              = CONTAINED
SUCCESS_CONDITION_AS_DEMONSTRATION   = CONTAINED
CAUSAL_ASSERTION_AS_EMPIRICAL_RESULT = CONTAINED
```

## 6. Unresolved-source non-regression

All 21 unresolved source fragments remain unresolved.

The effective node does not silently define or canonicalize:

```text
C in C(rho,T)<=A
operational derivative for C_rev versus E*
G versus G_t
Omega_viable / I_stored measurement
KL intervention semantics
Theta-family measurement
C/Lambda/Gamma failure signatures
q/v/J in README.md
E exploration versus E environment
RAD parent research-program endpoint
H_t/J_t
G_m/Gbar_m definitions beyond source roles
Omega_t consequence information versus Omega improvement rate
CTC delta/K/T/C_future/z(T)
mutual-information estimator/protocol
RVT001 A/U/equal-resources operationalization
RAD simulator J
```

```text
UNRESOLVED_SYMBOL_AS_CANONICALIZED_DEFINITION = CONTAINED
```

## 7. Recurrence and warrant non-regression

The central causal-access invariant recurs across the two source files. The projection ledger preserves both occurrences while the audit view retains:

```text
WARRANT_MULTIPLICITY_EFFECT = NONE
```

```text
RECURRENCE_AS_INDEPENDENT_WARRANT = CONTAINED
```

Repeated framework language is therefore reusable memory, not duplicated evidence.

## 8. Temporal provenance non-regression

The repository developmental history remains reconstructible as:

```text
initial two-line LLM-prompt stub
-> full Meta-Process Framework
-> RAD companion surface added
-> README_2 renamed to README_2.md
```

The current-head parse is not allowed to erase that developmental trajectory, and historical blobs are not silently admitted as additional current-head parse surfaces.

```text
CURRENT_HEAD_PARSE != DEVELOPMENTAL_PROVENANCE
TEMPORAL_LATEST_STATE_AS_RETROACTIVE_CLEANUP = CONTAINED
```

## 9. Lineage and map-authority non-regression

The source statement that RAD evolved from a research program remains an unresolved source fragment because no endpoint is identified on the frozen R17 surface.

No endpoint resolution, cross-repository edge, or Program Map assertion is emitted.

```text
SOURCE_LINEAGE_AS_PROGRAM_MAP_EDGE = CONTAINED
```

## 10. Contract transport result

R17 required one local compression-content repair after its transport death test. It required no new parser role, no new top-level compression coordinate, and no contract amendment.

```text
NEW_EPISTEMIC_DISTINCTION_REQUIRED  = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
NEW_COMPRESSION_CONTRACT_AMENDMENT   = NOT_EARNED
POST_REPAIR_PRIMARY_REMAPS           = 0
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R17_FROZEN_HEADS
```

This is not universal transportability.

## 11. Final R17 verdict

```text
R17_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD
R17_FROZEN_HEAD_COMMIT                 = 642cb6bcd131309b9e9628fc39f228b92e4ed966
R17_TOTAL_BLOB_PATHS                   = 2
R17_RESEARCH_BEARING_PATHS             = 2
R17_UNIQUE_HEAD_BLOBS                  = 2
R17_MARKDOWN_PATHS                     = 2

R17_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS   = 231
R17_PARSED_REPRESENTATIONS             = 210
R17_UNRESOLVED_SOURCE_UNITS            = 21
R17_PARSER_FAILURES                    = 0

R17_PRIMARY_PROJECTION_ENTRIES         = 231
R17_PRIMARY_COMPRESSED_ITEMS           = 88
R17_UNMAPPED_PARSE_UNITS               = 0
R17_DUPLICATE_PRIMARY_OWNERS           = 0

R17_EXECUTABLE_IMPLEMENTATION          = NONE_ON_FROZEN_SURFACE
R17_SOURCE_REPORTED_EMPIRICAL_RESULTS  = NONE_ON_FROZEN_SURFACE
R17_SOURCE_REPORTED_NEGATIVE_RESULTS   = NONE_ON_FROZEN_SURFACE
R17_PERSISTED_EXECUTION_RECORDS        = NONE_ON_FROZEN_SURFACE

R17_FRAMEWORK_IDENTITY_EQUIVALENCE     = NOT_ESTABLISHED
R17_TEMPORAL_PROVENANCE                = PRESERVED
R17_REUSABLE_NODE_STATE                = EARNED
Z17_EFFECTIVE_NODE_STATE               = EARNED

R17_MAP_EDGE_EMISSION                  = NONE
R17_MAP_AUTHORITY                      = NONE
R17_SCIENTIFIC_AUTHORITY               = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
CEREBRO_STEP_2                         = CLOSED
NEW_COMPRESSION_CONTRACT_AMENDMENT     = NOT_EARNED
```

`Z17_EFFECTIVE_NODE_STATE` refers to the inherited effective neuron construction:

```text
frozen source surface
+ exhaustive parse
+ effective compression (base + Amendment 001)
+ complete parse-to-compression projection ledger
+ frozen death-test/retest provenance
```

It does not introduce a new top-level ontology or a separate semantic node type.

## 12. Sequential boundary

```text
Z01_Z17_REUSABLE_NODE_STATE = EARNED
R18_PROGRAM_PARSE_ACCESS    = NEXT_AUTHORIZED_REPOSITORY
R19_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only. It creates no R17 -> R18 semantic relation.

R17 is therefore a reusable neuron that preserves two overlapping causal-framework surfaces without collapsing their identities, preserves experimental designs without promoting them to results, and preserves developmental history without retroactive cleanup.
