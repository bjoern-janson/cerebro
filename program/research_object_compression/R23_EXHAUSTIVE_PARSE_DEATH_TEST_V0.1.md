# R23 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/ctre_simulator`  
**Frozen head:** `a3ef7b068a8b93c1892d082d63f35eaf0eae31b6`  
**Effective source surface:** base + source-coordinate Amendment 001  
**Candidate parse:** 73 represented + 39 unresolved = 112 units

## 1. Accounting

```text
FROZEN_HEAD_PATHS      = 8
PARSE_INCLUDED         = 8
UNENUMERATED_PATHS     = 0
CANDIDATE_PARSE_UNITS  = 112
PARSER_FAILURES        = 0
```

## 2. Attack matrix

```text
README_ENVIRONMENT_AS_IMPLEMENTATION                    = CONTAINED
HIDDEN_CONTEXT_CLAIM_AS_IMPLEMENTED_HIDDEN_VARIABLE     = CONTAINED
STATE_BASELINE_DESCRIPTION_AS_IMPLEMENTED_BASELINE      = CONTAINED
README_HOLDOUT_RULE_AS_ACTUAL_COMMIT_GATE               = CONTAINED
PREDICTION_AS_RESULT                                    = CONTAINED
ASSERTION_CODE_AS_ASSERTION_PASS                        = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                      = CONTAINED
INTERACTION_FEATURE_AS_DISCOVERY_OF_UNOBSERVED_VARIABLE = CONTAINED
CORRELATION_HEURISTIC_AS_HELDOUT_GENERALIZATION         = CONTAINED
OFFLINE_EVALUATOR_AS_INDEPENDENT_VALIDATION             = CONTAINED
SPARSE_MUTATION_AS_EMERGENT_RESULT                      = CONTAINED
SOURCE_COORDINATE_REPAIR_AS_RETROACTIVE_CLEANUP         = CONTAINED
REPOSITORY_LEVEL_AUDIT_AS_PRIMARY_SOURCE_UNIT           = HIT
CROSS_REPO_NONRELATION_AS_PRIMARY_SOURCE_UNIT           = HIT
```

## 3. Primary-source locality hit

`R23U0035` and `R23U0036` use the synthetic path `repository` and the commit SHA rather than an actual frozen blob coordinate.

Their content is useful:

- bounded absence of test files,
- no explicit cross-repository identity resolution.

But these are parser-derived repository-level audits, not source-local semantic units. Keeping them in the primary parse would violate reversibility to a source path/blob.

Shallow repair:

```text
R23U0035 -> DEMOTE_TO_SECONDARY_BOUNDED_ABSENCE_AUDIT
R23U0036 -> DEMOTE_TO_SECONDARY_ENDPOINT_AUDIT
```

No source content disappears: both statements remain preserved as zero-authority audit views outside the primary parse.

## 4. Scientific/implementation ceilings

The effective parse must retain the following distinctions without resolution:

```text
README hidden-context story != implemented observation interface
README y=a*v*(1+z)          != implemented 2*v / v*context target
README theta*v baseline     != implemented [v,context] baseline
README holdout commit gate  != REE internal sleep-cycle commit
context observed            != interaction feature already represented
code assertions             != observed assertion passes
```

The evaluator also does not establish held-out generalization: its train inputs are unused and models are fit/scored on validation data. This remains an unresolved implementation/validation fact rather than a reported negative scientific result.

## 5. Verdict

```text
R23_PARSE_CANDIDATE_UNITS          = 112
PRIMARY_SOURCE_UNITS_DEMOTED       = 2
R23_EFFECTIVE_PARSE_UNITS          = 110
R23_EFFECTIVE_REPRESENTED          = 73
R23_EFFECTIVE_UNRESOLVED           = 37
SOURCE_CONTENT_LOSS                = 0
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_GLOBAL_PARSER_ROLE             = NONE
BASE_PARSE_CONTRACT_AMENDMENT      = NOT_EARNED
```

Compression is blocked until the two-unit demotion overlay/retest is frozen.
