# R07 COMPRESSION TRANSPORT — RETEST V0.1

**Death test:** `R07_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Compression repair:** `R07_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Projection repair:** `R07_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest evaluates only the two demonstrated compression-local failures and preserves the R07 hostile fixtures that were already contained.

## 1. Complete projection accounting with explicit unresolved state

The repaired effective projection is:

```text
R07_EFFECTIVE_PARSE_UNITS                    = 158
R07_PARSED_UNITS                             = 157
R07_PRIMARY_PROJECTION_ENTRIES               = 157
R07_UNRESOLVED_PARSE_UNITS                   = 1
R07_UNRESOLVED_AT_COMPRESSION_ENTRIES        = 1
R07_UNMAPPED_PARSE_UNITS                     = 0
R07_DUPLICATE_PRIMARY_OWNERS                 = 0
```

`R07:P:DO:SEARCH_HIERARCHY` now terminates in:

```text
R07:ASSERT:OPTIMIZATION_VS_DISCOVERY
```

without creating a second semantic item or second warrant.

```text
PARSE_UNIT_WITHOUT_PRIMARY_DISPOSITION = REPAIRED
```

The terminal Deep Learning fragment remains explicitly unresolved rather than forced into a resolved semantic item.

## 2. Source-occurrence self-accounting

`R07:ASSERT:KERNEL_INTERPRETATION` is replaced by one unambiguous record:

```text
SOURCE_OCCURRENCE_COUNT      = 5
WARRANT_INDEPENDENCE_STATUS  = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT  = NONE
```

for exactly five source branches.

```text
CONFLICTING_SOURCE_OCCURRENCE_ACCOUNTING = REPAIRED
```

No source branch was deleted.

## 3. Notation collision remains unresolved rather than hallucinated

R07 continues to preserve:

```text
K_predictive = -d KL(P_true || P_model) / dt
```

separately from source expressions:

```text
D = K(M_Q)
K(M_Q) -> K(I_true)
```

The effective node records:

```text
SEMANTIC_IDENTITY = NOT_ESTABLISHED
```

for the notation collision.

```text
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY = CONTAINED
```

No notation repair is asserted. No claim is made about what the author intended beyond the frozen source.

## 4. Source incompleteness is preserved as unresolved source state

The complete `examples.md` blob itself terminates inside a fenced block after:

```text
Human-designed features
```

The node retains:

```text
R07:P:EX:DL_TERMINAL_FRAGMENT
DISPOSITION = UNRESOLVED_AT_COMPRESSION_DUE_TO_SOURCE_BLOB_TERMINATION
AUTHORITY_EFFECT = NONE
WARRANT_EFFECT   = NONE
```

Therefore:

\[
\boxed{
\text{source internally incomplete}
\neq
\text{source unseen}
\neq
\text{parser failure}
\neq
\text{negative result}.
}
\]

```text
SOURCE_INCOMPLETENESS_AS_NODE_DELETION = CONTAINED
UNRESOLVED_FRAGMENT_AS_NEGATIVE_RESULT = CONTAINED
```

This is the first earned neuron state with an explicitly unresolved source-internal fragment.

## 5. Amendment 004 recurrence discipline

Every multi-source semantic group carries:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

unless separately warranted otherwise. No R07 item establishes such independence.

The lexical phrase `two independent quantities` in the Causal Mass source has:

```text
WARRANT_INDEPENDENCE_EFFECT = NONE
```

so mathematical/component language does not leak into epistemic warrant accounting.

```text
SOURCE_RECURRENCE_AS_WARRANT                 = CONTAINED
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE = CONTAINED
```

## 6. Role-preserving semantic compression

The node may group semantically redundant or tightly coupled source occurrences, but each source branch retains the role of its effective parse unit.

Representative mixed-role item:

```text
R07:HYPOTHESIS:TERMINAL_LIMIT
  SOURCE_ASSERTION_HYPOTHESIS
  SOURCE_INTERPRETATION
  SOURCE_ASSERTION_HYPOTHESIS
```

The aggregate does not rewrite all branches as hypotheses or interpretations.

Likewise the Mapping Quality formal object keeps definitions and formal structures distinct at branch level.

```text
ROLE_BRANCH_LOSS_DURING_SEMANTIC_COMPRESSION = CONTAINED
```

## 7. Historical examples remain examples

The source's positional notation, Cartesian coordinates, calculus, autodiff, compilers, alpha-beta pruning and partial deep-learning case remain typed as:

```text
HISTORICAL_SOURCE_ASSERTION
HISTORICAL_SOURCE_ASSERTION
SOURCE_INTERPRETATION
```

where present.

They do not become AMP empirical validation.

```text
HISTORICAL_EXAMPLE_AS_VALIDATION = CONTAINED
R07_REPORTED_EMPIRICAL_RESULTS   = NONE_ON_FROZEN_SOURCE_SURFACE
```

## 8. Source-described repository structure remains source-described

README's depiction of `examples/` and `simulations/` is preserved without overwriting the immutable frozen-head inventory.

```text
SOURCE_REPOSITORY_DESCRIPTION_AS_REPOSITORY_TRUTH = CONTAINED
```

## 9. No global contract growth

R07 required:

- local parse accounting repair;
- local restoration of repeated formal source occurrences;
- local restoration of omitted/enumerated source distinctions;
- one explicit source-internal unresolved fragment;
- local compression projection repair;
- local source-occurrence self-accounting repair.

It required no new parser role, no new top-level compression coordinate, no Amendment 005, no map edge and no propagation semantics.

The effective contract has therefore transported to a source family containing internally incomplete source text and overloaded notation without resolving either by invention.

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R07_FROZEN_HEADS
```

This is not universal transportability.

## 10. R07 verdict

```text
R07_SOURCE_SURFACE                         = FROZEN_FULL_RECURSIVE_HEAD
R07_TOTAL_BLOBS                            = 11
R07_RESEARCH_BEARING_BLOBS                 = 10
R07_MARKDOWN_BLOBS                         = 10
R07_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS       = 158
R07_PARSED_UNITS                           = 157
R07_UNRESOLVED_PARSE_UNITS                 = 1
R07_PARSE_FAILURES                         = 0
R07_PRIMARY_PROJECTION_ENTRIES             = 157
R07_UNRESOLVED_AT_COMPRESSION_ENTRIES      = 1
R07_UNMAPPED_PARSE_UNITS                   = 0
PARSE_UNIT_COUNT_SELF_INCONSISTENCY        = REPAIRED
REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS     = REPAIRED
ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE = REPAIRED
SOURCE_ASSERTION_OMISSION                  = REPAIRED
PARSE_UNIT_WITHOUT_PRIMARY_DISPOSITION     = REPAIRED
CONFLICTING_SOURCE_OCCURRENCE_ACCOUNTING   = REPAIRED
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY        = CONTAINED
SOURCE_INCOMPLETENESS_AS_NODE_DELETION     = CONTAINED
SOURCE_RECURRENCE_AS_WARRANT               = CONTAINED
HISTORICAL_EXAMPLE_AS_VALIDATION           = CONTAINED
R07_REPORTED_EMPIRICAL_RESULTS             = NONE_ON_FROZEN_SOURCE_SURFACE
R07_REUSABLE_NODE_STATE                    = EARNED_WITH_ONE_EXPLICIT_UNRESOLVED_SOURCE_FRAGMENT
R07_MAP_EDGE_EMISSION                      = NONE
R07_MAP_AUTHORITY                          = NONE
R07_SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```

## 11. Sequential boundary

```text
R08_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R09_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This is procedural authorization only and creates no R07 -> R08 semantic relation.

The first seven research neurons are reconstructible under one effective compression discipline. The seventh legitimately contains unresolved source memory without converting uncertainty into absence or evidence. No synaptic propagation law exists.