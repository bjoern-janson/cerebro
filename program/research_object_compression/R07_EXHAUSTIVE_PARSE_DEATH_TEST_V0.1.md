# R07 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/adaptive-metric-compiler`  
**Frozen head:** `47e6423d0da177730d1553d48df74510501778ab`  
**Parse candidate:** `R07_EXHAUSTIVE_PARSE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The death test evaluates whether the existing effective parser aperture transports to R07 without silently repairing source incompleteness, equating notation tokens with semantic objects, or dropping repeated/source-enumerated distinctions.

## A. `PARSE_UNIT_COUNT_SELF_INCONSISTENCY`

The candidate declares:

```text
parse_unit_count = 139
```

Direct enumeration of the frozen `parse_units` array yields:

```text
actual_parse_units = 151
```

The semantic payload is not invalidated by this arithmetic error, but the exhaustive-accounting claim is not self-consistent.

```text
PARSE_UNIT_COUNT_SELF_INCONSISTENCY = HIT
```

## B. `REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS`

`kernel.md` explicitly repeats the formal Causal Mass, salience and computational-gate equations.

The candidate records a conceptual selection unit but does not preserve those three formal source occurrences as distinct parse provenance.

Semantic equivalence with formulas elsewhere does not license deletion of the Kernel occurrences.

\[
\boxed{
\text{semantic recurrence}
\neq
\text{provenance recurrence}.
}
\]

```text
REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS = HIT
```

## C. `ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE`

Several candidate units preserve the broad source statement while dropping source-enumerated distinctions that the parser is capable of identifying. Representative cases:

- README Mapping Quality omits the source's seven listed criteria;
- README repository-structure unit does not preserve the full source-described path list;
- Causal Mass `Scale Independence` collapses the listed intended domains;
- Mapping Quality task-performance examples are omitted inside the metric dictionary;
- Phase Transition motivation does not preserve the exact first historical-example list.

This is selection inside the parse layer rather than loss-bounded compression downstream.

```text
ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE = HIT
```

## D. `SOURCE_ASSERTION_OMISSION`

The candidate also misses several independently classifiable source propositions:

- `definitions.md` says the environment contains underlying structure the agent attempts to model;
- `definitions.md` says metric discovery expands `Omega_viable`;
- `definitions.md` separately interprets the kernel sequence as six operations;
- `causal-mass.md` explicitly calls the two Causal Mass factors `independent quantities`.

These are source assertions/interpretations, not merely headings.

```text
SOURCE_ASSERTION_OMISSION = HIT
```

## E. `SOURCE_INCOMPLETENESS_AS_PARSER_FAILURE`

The frozen `examples.md` blob ends inside a fenced block immediately after:

```text
Human-designed features
```

The candidate does not invent the missing continuation. It records one:

```text
UNRESOLVED_SOURCE_FRAGMENT
```

with disposition:

```text
UNRESOLVED_AT_PARSE_DUE_TO_SOURCE_BLOB_TERMINATION
```

Therefore the parser can be exhaustive relative to the frozen bytes while the source artifact remains internally incomplete.

\[
\boxed{
\text{source incompleteness}
\neq
\text{parser incompleteness}.
}
\]

```text
SOURCE_INCOMPLETENESS_AS_PARSER_FAILURE = CONTAINED
SOURCE_FRAGMENT_COMPLETION_BY_PARSER    = CONTAINED
```

## F. `NOTATION_TOKEN_AS_SEMANTIC_IDENTITY`

R07 uses `K` for predictive improvement:

```text
K = -d KL(P_true || P_model) / dt
```

while also using:

```text
D = K(M_Q)
```

as a complexity expression and later:

```text
K(M_Q) -> K(I_true)
```

inside the terminal hypothesis.

The candidate preserves these in different semantic records and explicitly marks the identity relation as unestablished.

No token-level merge occurs.

```text
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY = CONTAINED_AT_PARSE
```

This is a hostile fixture for compression; containment here does not prove compression will preserve the distinction.

## G. `EXAMPLE_AS_EMPIRICAL_RESULT`

The source labels `examples.md` as examples that *can be interpreted* through AMP. Historical setup, claimed historical transition and AMP interpretation are separately typed.

No example becomes an AMP experiment or reported empirical result.

```text
EXAMPLE_AS_EMPIRICAL_RESULT = CONTAINED
```

## H. `SOURCE_REPOSITORY_DESCRIPTION_AS_TREE_TRUTH`

README depicts `examples/` and `simulations/` directories, while the frozen tree contains `examples.md` and no `simulations/` path.

The parser preserves the README statement as `SOURCE_DESCRIBED_STATUS` and does not rewrite the immutable inventory.

```text
SOURCE_REPOSITORY_DESCRIPTION_AS_TREE_TRUTH = CONTAINED
```

## I. `DESIDERATUM_AS_RESULT`

Causal Mass and Salience list desirable properties. They are represented as method/design desiderata, not observed properties.

```text
DESIDERATUM_AS_RESULT = CONTAINED
```

## J. Verdict

```text
PARSE_UNIT_COUNT_SELF_INCONSISTENCY       = HIT
REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS    = HIT
ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE = HIT
SOURCE_ASSERTION_OMISSION                 = HIT
SOURCE_INCOMPLETENESS_AS_PARSER_FAILURE   = CONTAINED
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY       = CONTAINED_AT_PARSE
EXAMPLE_AS_EMPIRICAL_RESULT               = CONTAINED
SOURCE_REPOSITORY_DESCRIPTION_AS_TREE_TRUTH = CONTAINED
DESIDERATUM_AS_RESULT                     = CONTAINED

GLOBAL_PARSE_CONTRACT_CHANGE              = NOT_EARNED
R07_PARSE_REPAIR                          = REQUIRED
R07_COMPRESSION                           = BLOCKED
MAP_AUTHORITY                             = NONE
SCIENTIFIC_AUTHORITY                      = NONE
PROPAGATE_KERNEL                          = NOT_EARNED
CEREBRO_STEP_2                            = CLOSED
```

All demonstrated failures are coverage/accounting defects inside the R07 parse instance. None requires a new global parser role or top-level compression coordinate.