# R07 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Effective parse:** base + `R07_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Compression candidate:** `R07_COMPRESSION_V0.1.json`  
**Projection ledger:** `R07_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The death test asks whether the effective R01-R06 compression contract transports to R07 while preserving one source-internal unresolved fragment and a source notation collision.

## A. `PARSE_UNIT_WITHOUT_PRIMARY_DISPOSITION`

The effective parse has 158 units:

```text
157 parsed
1 unresolved source fragment
```

The candidate/ledger accounts for:

```text
156 primary projections
1 unresolved-at-compression disposition
1 unmapped parsed unit
```

The unmapped unit is:

```text
R07:P:DO:SEARCH_HIERARCHY
```

Its source distinction—search over representations versus solution search—cannot disappear merely because related optimization/discovery units were already compressed.

```text
PARSE_UNIT_WITHOUT_PRIMARY_DISPOSITION = HIT
```

## B. `CONFLICTING_SOURCE_OCCURRENCE_ACCOUNTING`

`R07:ASSERT:KERNEL_INTERPRETATION` contains five source branches but the frozen JSON candidate contains two declarations of the same key:

```text
source_occurrence_count = 4
...
source_occurrence_count = 5
```

Even if a particular JSON parser keeps the later value, the persistent record is ambiguous and violates Amendment 004 accounting discipline.

```text
CONFLICTING_SOURCE_OCCURRENCE_ACCOUNTING = HIT
```

## C. `NOTATION_TOKEN_AS_SEMANTIC_IDENTITY`

The compression keeps predictive-improvement `K` distinct from the source's `K(M_Q)` complexity/informational-structure notation:

```text
R07:FORMAL:MAPPING_QUALITY.notation_collision.semantic_identity_status = NOT_ESTABLISHED
R07:HYPOTHESIS:TERMINAL_LIMIT.notation_semantic_identity = NOT_ESTABLISHED
```

No formula is repaired or reconciled.

```text
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY = CONTAINED
```

This is a bounded R07 result, not a universal notation-resolution theorem.

## D. `SOURCE_INCOMPLETENESS_AS_NODE_DELETION`

The incomplete end of `examples.md` is not omitted from the node merely because it cannot be semantically completed.

The candidate carries:

```text
R07:P:EX:DL_TERMINAL_FRAGMENT
-> UNRESOLVED_AT_COMPRESSION_DUE_TO_SOURCE_BLOB_TERMINATION
```

with zero authority and zero warrant effect.

```text
SOURCE_INCOMPLETENESS_AS_NODE_DELETION = CONTAINED
UNRESOLVED_FRAGMENT_AS_NEGATIVE_RESULT = CONTAINED
```

## E. `SOURCE_RECURRENCE_AS_WARRANT`

Multi-source semantic items explicitly retain Amendment 004 defaults:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

The source's lexical statement that Causal Mass combines `independent quantities` is separately represented with:

```text
WARRANT_INDEPENDENCE_EFFECT = NONE
```

Therefore mathematical/component independence language does not become evidential independence.

```text
SOURCE_RECURRENCE_AS_WARRANT = CONTAINED
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE = CONTAINED
```

## F. `ROLE_BRANCH_LOSS_DURING_SEMANTIC_COMPRESSION`

Multi-source items preserve each source parse unit and its effective parse role. Representative examples include:

- formal definitions + formal structures in `R07:FORMAL:MAPPING_QUALITY`;
- conceptual assertions + interpretations + hypotheses in `R07:ASSERT:CAUSAL_RELEVANCE_MODEL`;
- formal README occurrence + hypothesis occurrences for the terminal-limit family remain in separate primary items rather than silently merged.

```text
ROLE_BRANCH_LOSS_DURING_SEMANTIC_COMPRESSION = CONTAINED
```

## G. `HISTORICAL_EXAMPLE_AS_VALIDATION`

Each example preserves:

```text
HISTORICAL_SOURCE_ASSERTION
HISTORICAL_SOURCE_ASSERTION
SOURCE_INTERPRETATION
```

rather than `REPORTED_RESULT`.

```text
HISTORICAL_EXAMPLE_AS_VALIDATION = CONTAINED
```

## H. `DESIGN_DESIDERATUM_AS_OBSERVED_PROPERTY`

Causal Mass and Salience properties remain design/method desiderata. No observation or result is inferred.

```text
DESIGN_DESIDERATUM_AS_OBSERVED_PROPERTY = CONTAINED
```

## I. `SOURCE_REPOSITORY_DESCRIPTION_AS_REPOSITORY_TRUTH`

README's `examples/` and `simulations/` structure remains a source-described status item with:

```text
frozen_tree_reconciliation = NOT_PERFORMED_BY_COMPRESSION
```

```text
SOURCE_REPOSITORY_DESCRIPTION_AS_REPOSITORY_TRUTH = CONTAINED
```

## J. Scientific standing

The frozen source surface contains no admitted empirical execution/result artifact for AMP.

```text
R07_REPORTED_EMPIRICAL_RESULTS = NONE_ON_FROZEN_SOURCE_SURFACE
```

Formulas, historical examples and proposed phase transitions do not alter that.

## K. Verdict

```text
PARSE_UNIT_WITHOUT_PRIMARY_DISPOSITION        = HIT
CONFLICTING_SOURCE_OCCURRENCE_ACCOUNTING      = HIT
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY           = CONTAINED
SOURCE_INCOMPLETENESS_AS_NODE_DELETION        = CONTAINED
SOURCE_RECURRENCE_AS_WARRANT                  = CONTAINED
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE  = CONTAINED
ROLE_BRANCH_LOSS_DURING_SEMANTIC_COMPRESSION  = CONTAINED
HISTORICAL_EXAMPLE_AS_VALIDATION              = CONTAINED
DESIGN_DESIDERATUM_AS_OBSERVED_PROPERTY       = CONTAINED

GLOBAL_COMPRESSION_CONTRACT_CHANGE            = NOT_EARNED
R01_R06_REGRESSION_REQUIRED                   = NO
R07_LOCAL_COMPRESSION_REPAIR                  = REQUIRED
R08_ACCESS                                    = BLOCKED
MAP_AUTHORITY                                 = NONE
SCIENTIFIC_AUTHORITY                          = NONE
PROPAGATE_KERNEL                              = NOT_EARNED
CEREBRO_STEP_2                                = CLOSED
```

R07 has not demonstrated a new global compression distinction. Its two failures are local derivation/accounting defects.