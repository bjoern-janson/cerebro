# R12 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R12_COMPRESSION_V0.1.json`  
**Parse:** `R12_EXHAUSTIVE_PARSE_V0.1.json`  
**Projection ledger:** `R12_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R12 tests whether a one-file theory can preserve logical jurisdiction and standing while compressing repeated graph-theoretic content.

## 1. Projection accounting

```text
R12_EFFECTIVE_PARSE_UNITS      = 31
R12_PRIMARY_PROJECTION_ENTRIES = 31
R12_UNMAPPED_PARSE_UNITS       = 0
R12_DUPLICATE_PRIMARY_OWNERS   = 0
```

Projection completeness passes.

Standing preservation does not yet pass.

## 2. Attack matrix

```text
DEFINITION_TO_FORMALIZATION_RECOLLAPSE            = HIT
ONLY_IF_AS_IFF                                    = CONTAINED
PERMEABILITY_AS_SUFFICIENT_OPEN_ENDEDNESS         = CONTAINED
SOURCE_EQUIVALENT_LABEL_AS_PROVED_EQUIVALENCE     = CONTAINED
SOURCE_INVARIANT_LABEL_AS_PROVED_INVARIANCE       = CONTAINED
FORMAL_RECURRENCE_AS_INDEPENDENT_WARRANT           = CONTAINED
PREDICTION_AS_RESULT                              = CONTAINED
FALSIFICATION_AS_NEGATIVE_RESULT                  = CONTAINED
SOURCE_GRAPH_AS_PROGRAM_MAP                       = CONTAINED
ONE_FILE_AS_ONE_SEMANTIC_OBJECT                   = CONTAINED
```

## 3. HIT — permeability definition projected as formalization

The parse correctly distinguished:

```text
R12:P:README:DEF_PERMEABILITY
role = DEFINITION
```

from later repeated formal occurrences:

```text
R12:P:README:CRITICAL_BRIDGE_OCCURRENCE
role = FORMAL_STRUCTURE

R12:P:README:SUMMARY_FORMAL_RECURRENCE
role = FORMAL_STRUCTURE
```

But the projection ledger sends all three to:

```text
R12:FORMAL:PERMEABILITY
standing = SOURCE_FORMALIZATION
```

Therefore the first occurrence loses its source role even though no content disappears.

This is the same failure family isolated by R09:

\[
\boxed{
\text{semantic recurrence}
\not\Rightarrow
\text{standing identity}.
}
\]

```text
DEFINITION_TO_FORMALIZATION_RECOLLAPSE = HIT
```

The smallest repair is local:

1. add standing-pure `R12:DEF:PERMEABILITY`;
2. remap only `R12:P:README:DEF_PERMEABILITY`;
3. leave the two later formal recurrences in `R12:FORMAL:PERMEABILITY`;
4. repair the recurrence secondary view so it references both primary standings;
5. change no parse unit and add no global role.

## 4. Necessary vs sufficient condition remains contained

The effective content preserves:

```text
OPEN_ENDED -> P_C     [source central claim]
```

without adding:

```text
P_C -> OPEN_ENDED
```

The source's claims that permeability distinguishes open/closed lineages and predicts greater adaptive capacity remain hypothesis/prediction standing.

```text
ONLY_IF_AS_IFF = CONTAINED
PERMEABILITY_AS_SUFFICIENT_OPEN_ENDEDNESS = CONTAINED
```

## 5. Equivalence / invariance labels remain source-relative

The compression separately preserves:

```text
"or equivalently"         -> source conceptual equivalence assertion
"graph-theoretic invariant" -> source status/characterization
```

Neither is promoted to an independently proved theorem.

```text
SOURCE_EQUIVALENT_LABEL_AS_PROVED_EQUIVALENCE = CONTAINED
SOURCE_INVARIANT_LABEL_AS_PROVED_INVARIANCE = CONTAINED
```

## 6. Recurrence remains non-corroborative

The permeability relation occurs three times in different source roles.

The secondary occurrence view has:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
AUTHORITY_EFFECT = NONE
```

The current standing bug is not evidence multiplicity; it is primary-destination mis-typing.

```text
FORMAL_RECURRENCE_AS_INDEPENDENT_WARRANT = CONTAINED
```

## 7. Prediction / falsification / graph-boundary non-regression

R12 still contains no empirical result, negative result, implementation or execution record.

```text
PREDICTION_AS_RESULT             = CONTAINED
FALSIFICATION_AS_NEGATIVE_RESULT = CONTAINED
SOURCE_GRAPH_AS_PROGRAM_MAP      = CONTAINED
```

The source graph G=(V,E), reachability relation and cuts are theory-internal graph objects and emit no #44 map edge.

## 8. Verdict

```text
PROJECTION_COMPLETENESS                       = PASS
STANDING_PRESERVATION                         = FAIL
DEFINITION_TO_FORMALIZATION_RECOLLAPSE        = HIT
NEW_GLOBAL_PARSER_ROLE                        = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE          = NONE
AMENDMENT_005                                 = NOT_EARNED
MAP_EDGE                                      = NONE
PROPAGATION                                   = NONE
CEREBRO_STEP_2                                = CLOSED
```

R12 is not yet a reusable node state.

The failure is localized entirely to D12: one parse unit has the wrong standing-pure compression destination.
