# R14 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Target:** `R14_EXHAUSTIVE_PARSE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Source surface:** `R14_SOURCE_SURFACE_V0.1.json`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Question

Can the R14 source parse preserve source-local distinctions without turning section-level convenience into epistemic-role collapse?

The attack is intentionally upstream of compression.

\[
\boxed{
\text{section adjacency}
\neq
\text{role identity}.
}
\]

## 2. Accounting checks

```text
ADMITTED_RESEARCH_PATHS          = 10
PARSE_PAYLOAD_SOURCE_PATHS       = 10
DECLARED_PARSE_UNITS             = 97
SUM(PER_SOURCE_UNIT_COUNTS)      = 97
UNACCOUNTED_SOURCE_PATHS         = 0
SOURCE_UNRESOLVED_UNITS          = 0
PARSER_FAILURES                  = 0
```

The manifest denominator is mechanically consistent.

## 3. Attack matrix

```text
CROSS_ARTIFACT_AUDIT_AS_SOURCE_PARSE        = CONTAINED
ENVIRONMENT_FORMAL_VARIANT_COLLAPSE         = CONTAINED
SOURCE_STATUS_RECONCILIATION                = CONTAINED
DOCUMENT_LAYOUT_AS_OBSERVED_FILESYSTEM      = CONTAINED
PSEUDOCODE_AS_EXECUTABLE_IMPLEMENTATION     = CONTAINED
PREDICTION_AS_REPORTED_RESULT               = CONTAINED
RECURRENCE_AS_INDEPENDENT_WARRANT           = CONTAINED
INTERNAL_CAUSAL_ARROW_AS_PROGRAM_MAP_EDGE   = CONTAINED
MULTI_ROLE_PARSE_UNIT                       = HIT
```

## 4. Contained attacks

The four cross-artifact comparisons are kept outside `sources[*].units` as derived audit views. Therefore:

```text
SOURCE_PARSE != CROSS_ARTIFACT_AUDIT
```

The two environment-state definitions remain separately source-local:

```text
docs/simulator-spec.md      : E_t=(R_t,C_t)
environment/README.md       : E_t=(R_t,C_t)
environment/design.md       : E_t=(R_t,C_t,N_t)
```

No equivalence, precedence or supersession is inferred.

The parse also keeps document-described repository layouts separate from the frozen source-surface inventory, and labels Markdown Python sketches as illustrative specification rather than executable implementation.

## 5. Hit — mixed epistemic roles inside a single parse unit

A bounded set of parse units contain source distinctions of more than one epistemic role while exposing only one `role` field.

Examples include:

- `R14:P:README:IDENTITY_STATUS` — identity/title plus status/type;
- `R14:P:AGENT:IDENTITY_STATUS_QUESTION` — status plus research question;
- `R14:P:AGENT:MEASUREMENTS_PREDICTION` — metric definitions plus prediction;
- `R14:P:F1:PURPOSE_STATE` — scope/purpose plus formal state object;
- `R14:P:F2:DEPENDENCY_HYP_BOUNDARY` — formal dependency structure plus empirical-hypothesis boundary;
- `R14:P:F2:PREDICTION_FALSIFICATION_INVARIANT` — prediction plus falsification protocol plus source-labeled invariant;
- `R14:P:METRICS:VECTOR_SIGNATURE_CLOSURE` — metric-vector definition plus predicted trajectory plus adaptive-closure definition;
- `R14:P:SPEC1:METADATA_OBJECTIVE_STATUS` — source status plus experimental objective;
- `R14:P:SPEC1:EXPECTED_FALSIFICATION` — prediction plus falsification protocol;
- `R14:P:SPEC2:METADATA_HYP_STATUS` — source status plus empirical hypothesis;
- `R14:P:SPEC2:SCOPE_ONTOLOGY` — scope boundary plus ontology definitions;
- `R14:P:SPEC2:METRICS_PREDICTION_FALSIFICATION` — metric definitions plus prediction plus falsification;
- `R14:P:SPEC2:MINIMAL_REPO_FUTURE_INVARIANT` — project-layout metadata plus formal invariant/boundary;
- `R14:P:ENVREADME:PURPOSE_STATE` — purpose plus environment-state definition;
- `R14:P:ENVREADME:FUTURE_EXTENSIONS_COMPARISON` — future project paths plus experimental comparison;
- `R14:P:ENVDESIGN:PURPOSE_STATE` — purpose plus formal environment-state definition;
- `R14:P:MECH:PURPOSE_DEFINITION` — purpose/scope plus formal mechanism definition;
- `R14:P:MECH:EXPERIMENTAL_PRINCIPLE_SUMMARY` — protocol, observable-object definition, and research question.

The content is not wrong. The parser projection is too coarse.

Therefore:

\[
\boxed{
\text{semantic inclusion}
\not\Rightarrow
\text{role-faithful parse}.
}
\]

## 6. Failure localization

```text
FAILURE_LOCUS = REPRESENTATION / PARSE-ROLE SEPARABILITY
SOURCE_ERROR  = NONE ESTABLISHED
ONTOLOGY_GAP  = NONE ESTABLISHED
```

The effective contract already requires source-role distinctions to survive. No new top-level coordinate is needed.

## 7. Minimal repair

Freeze the candidate unchanged and add a successor overlay that:

1. demotes exactly the listed mixed-role units from effective primary standing;
2. replaces them with source-local role-pure units;
3. changes no unaffected parse unit;
4. adds no cross-artifact inference as a source unit;
5. preserves all source content and provenance;
6. recomputes the effective denominator mechanically.

```text
AMENDMENT_005 = NOT_EARNED
COMPRESSION    = BLOCKED_PENDING_PARSE_REPAIR
```

## 8. Boundary

R14 has not yet earned a reusable compressed neuron.

```text
R14_REUSABLE_NODE_STATE = NOT_YET_EARNED
R15_PARSE_ACCESS         = CLOSED
PROPAGATE_KERNEL         = NOT_EARNED
CEREBRO_STEP_2           = CLOSED
```
