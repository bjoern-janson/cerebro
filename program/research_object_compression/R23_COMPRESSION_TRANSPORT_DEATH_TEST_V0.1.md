# R23 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/ctre_simulator`  
**Frozen head:** `a3ef7b068a8b93c1892d082d63f35eaf0eae31b6`  
**Effective parse:** 110 units  
**Compression:** 25 primary items  
**Projection:** 110 exact primary owners

## 1. Accounting

```text
R23_FROZEN_HEAD_PATHS              = 8
R23_EFFECTIVE_PARSE_UNITS          = 110
R23_PARSED_REPRESENTATIONS         = 73
R23_EXPLICITLY_UNRESOLVED          = 37
R23_PRIMARY_PROJECTION_ENTRIES     = 110
R23_PRIMARY_COMPRESSED_ITEMS       = 25
R23_UNMAPPED_PARSE_UNITS           = 0
R23_DUPLICATE_PRIMARY_OWNERS       = 0
```

## 2. Attack matrix

```text
README_ENVIRONMENT_AS_IMPLEMENTATION                    = CONTAINED
HIDDEN_CONTEXT_AS_IMPLEMENTED_HIDDEN_VARIABLE            = CONTAINED
STATE_BASELINE_DESCRIPTION_AS_IMPLEMENTED_BASELINE       = CONTAINED
INTERACTION_FEATURE_AS_UNOBSERVED_VARIABLE_DISCOVERY     = CONTAINED
README_HOLDOUT_RULE_AS_IMPLEMENTED_COMMIT_GATE           = CONTAINED
EVALUATOR_AS_HELDOUT_GENERALIZATION_ESTIMATOR            = CONTAINED
CORRELATION_HEURISTIC_AS_GENERALIZATION_EVIDENCE         = CONTAINED
ONE_MUTATION_GUARD_AS_EMERGENT_SPARSITY                  = CONTAINED
EXECUTABLE_ASSERTION_AS_OBSERVED_PASS                    = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                       = CONTAINED
SOURCE_COORDINATE_REPAIR_AS_RETROACTIVE_CLEANUP          = CONTAINED
SERIALIZATION_REPAIR_AS_SEMANTIC_CHANGE                  = CONTAINED
CTRE_NAME_OVERLAP_AS_CORPUS_IDENTITY                     = CONTAINED
PRIMARY_SOURCE_ITEM_WITH_AUDIT_QUALIFIER                 = HIT
```

## 3. Local wording hit

`R23:C006` is a primary README methodology item. Its candidate compression says the source evaluates candidates on a **"purported holdout"**.

The source itself says held-out data. The fact that the frozen evaluator does not implement a genuine held-out fit/evaluation split is independently preserved under unresolved standing in `R23:C024`.

Therefore the qualifier `purported` is parser/audit commentary leaking into a source-standing item.

Shallow repair:

```text
R23:C006 content:
"purported holdout"
->
"held-out data as described by the source"
```

No source-unit ownership, standing, coordinate or item count changes.

## 4. Construct-validity ceiling survives

The effective node must preserve:

```text
context is observed in env.py
StateOnlyAgent consumes context linearly
REE begins with [1,v] and can add v*context
```

Thus the implemented experiment is not cleanly `hidden variable unavailable -> representation invention`. It is closer to `observed context + missing interaction basis -> representation expansion`, with different fixed feature sets across comparator agents.

The evaluator additionally fits and scores on validation data and does not consume train inputs. Internal REE mutation can commit before evaluator evidence.

These facts remain unresolved/zero-authority ceilings, not negative empirical results.

## 5. Execution ladder

```text
implementation present          = YES
executable assertions present   = YES
test source                     = NO
GitHub Actions runs at head     = 0
combined status records at head = 0
persisted run results           = 0
```

Therefore:

```text
assertion code != assertion pass
implementation != execution record
prediction != result
```

## 6. Verdict

```text
R23_LOCAL_COMPRESSION_REPAIR_REQUIRED = 1 CONTENT_WORDING_ONLY
R23_PROJECTION_REMAPS_REQUIRED        = 0
NEW_EPISTEMIC_DISTINCTION_REQUIRED    = NO
NEW_GLOBAL_PARSER_ROLE                = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE  = NONE
AMENDMENT_005                         = NOT_EARNED
```

`Z23` remains blocked until the wording overlay/retest is frozen.
