# R09 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R09_COMPRESSION_V0.1.json`  
**Effective parse:** `R09_EXHAUSTIVE_PARSE_V0.1` + Amendment 001  
**Projection ledger:** `R09_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The death test asks two independent questions:

\[
\boxed{\text{Did every parse unit receive exactly one primary disposition?}}
\]

and:

\[
\boxed{\text{Did the destination preserve what kind of source unit it was?}}
\]

The first question passes. The second does not yet pass.

## 1. Projection accounting

```text
R09_EFFECTIVE_PARSE_UNITS             = 340
R09_PRIMARY_PROJECTION_ENTRIES        = 339
R09_UNRESOLVED_AT_COMPRESSION_ENTRIES = 1
R09_UNMAPPED_PARSE_UNITS              = 0
R09_DUPLICATE_PRIMARY_OWNERS          = 0
PROJECTION_COMPLETENESS               = PASS
```

Thus any failure below is not missing bookkeeping.

## 2. Attack matrix

```text
LAYER_PURPOSE_RECOLLAPSE                          = HIT
DEFINITION_TO_THEORY_OR_ARCHITECTURE_RECOLLAPSE  = HIT
SOURCE_STATUS_TO_SUBSTANTIVE_STANDING_RECOLLAPSE = HIT
ARCHITECTURE_ASSERTION_RECOLLAPSE                 = HIT
MIXED_HYPOTHESIS_CONCEPTUAL_ROUTING               = HIT

HYPOTHESIS_AS_RESULT                              = CONTAINED
PREDICTION_AS_EVIDENCE                            = CONTAINED
PROTOCOL_AS_EXECUTION                             = CONTAINED
ARCHITECTURE_AS_IMPLEMENTATION                    = CONTAINED
MOCK_OUTPUT_AS_RESULT                             = CONTAINED
FORMAL_RECONCILIATION                             = CONTAINED
FINAL_UNIFIED_AS_SUPERSESSION                     = CONTAINED
TOKEN_IDENTITY_AS_SEMANTIC_IDENTITY               = CONTAINED
LOGICAL_ORDER_AS_ARTIFACT_CHRONOLOGY              = CONTAINED
DEVELOPMENTAL_REFERENCE_AS_MAP_EDGE               = CONTAINED
SOURCE_FORMAT_IRREGULARITY_AS_PARSER_FAILURE      = CONTAINED
SOURCE_INCOMPLETENESS_AS_ABSENCE                  = CONTAINED
RECURRENCE_AS_CORROBORATION                       = CONTAINED
```

## 3. HIT — layer purpose recollapse

All source-local purpose units currently project to:

```text
R09:SCOPE:RESTORATION
```

That destination correctly preserves the repository-level restoration mission, but it does not preserve the distinct research question of each layer family.

For example:

```text
Layer 21 purpose = propose an AGI observatory
Layer 39 purpose = define a recursive-intelligence experiment
Layer 45 purpose = model the reality-representation boundary
Layer 62 purpose = design empirical validation
Layer 72 purpose = design an intelligence operating system
```

A single generic restoration-purpose item loses these source-level distinctions even though every unit is accounted for.

```text
LAYER_PURPOSE_RECOLLAPSE = HIT
```

This is exactly:

\[
\boxed{
\text{complete bookkeeping}
\not\Rightarrow
\text{content-preserving compression}.
}
\]

## 4. HIT — definitions projected into theory/architecture containers

Several definition units terminate in destinations whose standing is conceptual theory or architecture proposal rather than definition.

Witnesses include:

```text
R09:P:L20:CRITERIA        -> R09:ARCH:AGI_RECURSIVE
R09:P:L31:FIELD_DEFINITIONS -> R09:THEORY:UNIVERSAL_FIELD_THERMO
R09:P:L45:DEFINITIONS     -> R09:THEORY:REPRESENTATION_GEOMETRY
R09:P:L48:DEFINITIONS     -> R09:THEORY:CAUSAL_MASS_VELOCITY
R09:P:L58:DEFINITIONS     -> R09:THEORY:REPRESENTATION_GEOMETRY
R09:P:L62:VARIABLES       -> R09:FORMAL:UNIFIED_EQUATION_FAMILY
R09:P:L63:DEPTH_MODEL     -> R09:DEF:CORE_ONTOLOGY but extends a later source-local depth hierarchy beyond the core dictionary
```

The destination may discuss the same topic while still erasing the source standing:

\[
\boxed{
\text{definition about a theory}
\neq
\text{theory assertion}.
}
\]

```text
DEFINITION_TO_THEORY_OR_ARCHITECTURE_RECOLLAPSE = HIT
```

## 5. HIT — source status projected into substantive standing

Many `SOURCE_DESCRIBED_STATUS` units currently terminate in the same theory/architecture item as the substantive content.

Examples:

```text
L18 STATUS -> THEORY:CIVILIZATION
L22 STATUS -> ARCH:AGI_RECURSIVE
L31 STATUS -> THEORY:UNIVERSAL_FIELD_THERMO
L45 STATUS -> THEORY:REPRESENTATION_GEOMETRY
L63 STATUS -> ARCH:ENGINEERING_OS
```

A statement such as:

```text
"this is a proposal / theory; no result is reported"
```

is not itself the proposal/theory content.

R08 already earned this distinction in several forms.

```text
SOURCE_STATUS_TO_SUBSTANTIVE_STANDING_RECOLLAPSE = HIT
```

## 6. HIT — architecture-adjacent conceptual assertions

The candidate routes several conceptual assertions into architecture-proposal objects:

```text
L11 ALIGNMENT_ASSERTIONS -> ARCH:ALIGNMENT_CONTROL
L13 MEMORY_ASSERTION     -> ARCH:RESTORATION_MEMORY
L14 ANCHOR_PRINCIPLE     -> ARCH:RESTORATION_MEMORY
L23 SAFETY_ASSERTION     -> ARCH:ALIGNMENT_CONTROL
L37 FAILURE_MODES        -> ARCH:AGI_RECURSIVE
L64 FAILURE_MODES        -> ARCH:ALIGNMENT_CONTROL
L72 OS_ASSERTIONS        -> ARCH:ENGINEERING_OS
```

These assertions may motivate or constrain an architecture, but:

\[
\boxed{
\text{conceptual assertion}
eq\text{architecture proposal}.
}
\]

```text
ARCHITECTURE_ASSERTION_RECOLLAPSE = HIT
```

## 7. HIT — mixed hypothesis/conceptual routing

Two candidate containers explicitly mix hypothesis and conceptual standing:

```text
R09:THEORY:TRUTH_COUPLING
R09:THEORY:UNIVERSAL_FIELD_THERMO
```

They label internal branches, which is better than silent collapse, but the projection ledger does not route a parse unit to a branch identity. A source-labelled hypothesis and a conceptual definition/assertion both terminate at the same item-level standing.

Therefore the distinction is present in prose but not carried by the projection function itself.

```text
MIXED_HYPOTHESIS_CONCEPTUAL_ROUTING = HIT
```

The smallest repair is standing-pure destinations, not a new coordinate.

## 8. Contained high-risk R09 fixtures

The candidate correctly preserves:

```text
Omega semantics = unresolved across local definitions
R semantics     = local
G_A semantics   = local
Layer 74 path / Layer 73 self-label / creation chronology = separate
Layer 72 Intelligence Compiler endpoint = unresolved
Layer 68 terminal source fragment = unresolved source content
Layer 50 recurrence = occurrence only
source internal dependency graph = no Program Map edge
```

It also preserves:

```text
R09_REPORTED_EMPIRICAL_RESULTS = NONE_ON_FROZEN_SOURCE_SURFACE
R09_REPORTED_NEGATIVE_RESULTS  = NONE_ON_FROZEN_SOURCE_SURFACE
```

without turning that bounded absence into a global negative claim.

## 9. Failure localization

All five hits are compression-destination failures.

They do **not** require:

```text
NEW_GLOBAL_PARSER_ROLE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE
AMENDMENT_005
MAP_EDGE
PROPAGATION
```

The already-earned contract can represent the missing distinctions.

Required local repair:

1. add a standing-pure layer-purpose view;
2. add standing-pure specialized-definition view(s);
3. add a standing-pure source-status view;
4. add standing-pure architecture-principle conceptual assertions;
5. separate explicit hypotheses from conceptual/theoretical branches in mixed theory families;
6. remap only the affected parse-unit IDs.

## 10. Verdict

```text
PROJECTION_COMPLETENESS                           = PASS
STANDING_PRESERVATION                             = FAIL
LAYER_PURPOSE_RECOLLAPSE                          = HIT
DEFINITION_TO_THEORY_OR_ARCHITECTURE_RECOLLAPSE  = HIT
SOURCE_STATUS_TO_SUBSTANTIVE_STANDING_RECOLLAPSE = HIT
ARCHITECTURE_ASSERTION_RECOLLAPSE                 = HIT
MIXED_HYPOTHESIS_CONCEPTUAL_ROUTING               = HIT
AMENDMENT_005                                     = NOT_EARNED
MAP_EDGE                                           = NONE
PROPAGATION                                        = NONE
CEREBRO_STEP_2                                     = CLOSED
```

R09 is not yet a reusable node state.
