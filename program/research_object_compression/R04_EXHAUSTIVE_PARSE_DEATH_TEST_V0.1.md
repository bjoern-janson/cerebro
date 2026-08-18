# R04 EXHAUSTIVE PARSE DEATH TEST V0.1

**Parse:** `R04_EXHAUSTIVE_PARSE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R04 is the first repository in the sequence whose admitted research surface contains executable source code as well as prose.

The test asks whether the effective parser preserves every recognized source distinction without converting implementation into execution evidence.

## Contained attacks

```text
ROOT_ONLY_INVENTORY_ON_NESTED_REPOSITORY       = CONTAINED
SOURCE_CODE_PRESENCE_AS_EXECUTION              = CONTAINED
PROGRAMMED_OUTPUT_LABEL_AS_OBSERVED_RESULT     = CONTAINED
HARD_CODED_SYNTHETIC_ASSUMPTION_AS_FINDING     = CONTAINED
IMPLEMENTATION_BEHAVIOR_AS_SOURCE_ASSERTION    = CONTAINED
CODE_PRESENCE_AS_STATUS_RECONCILIATION         = CONTAINED
TEXT_CODE_RECURRENCE_AS_INDEPENDENT_WARRANT    = CONTAINED_AT_PARSE_BOUNDARY
```

The code surface is represented with source-local kinds such as:

```text
EXECUTABLE_IMPLEMENTATION
IMPLEMENTATION_ASSUMPTION
IMPLEMENTATION_BEHAVIOR
IMPLEMENTED_OUTPUT_BEHAVIOR
```

These are item-level parser roles permitted under the existing open `UNIT_KIND` field. They do not add a top-level #44 ontology class.

In particular, `main.py` hard-codes `true_horizon = 3` and can print `Observer-Limited Architecture Confirmed`; `mdl_analysis.py` explicitly uses synthetic calibration arrays; `analyze_horizon.py` prints `Measured k*` from proxy formulas. None is parsed as a frozen empirical result because the repository head contains no execution record.

## Hit A — `MIXED_STANDING_UNITIZATION_R04`

Several candidate units combine distinctions already recognizable under the frozen parser aperture:

```text
R04:P:README:IDENTITY_PURPOSE
  IDENTITY_TITLE + SOURCE_DESCRIBED_SCOPE_OR_PURPOSE

R04:P:THEORY:SCOPE_HYP
  SOURCE_DESCRIBED_SCOPE_OR_PURPOSE + SOURCE_ASSERTION_HYPOTHESIS

R04:P:MATH:SCOPE
  SOURCE_DESCRIBED_SCOPE_OR_PURPOSE + SOURCE_ASSERTION_CONCEPTUAL_DISTINCTION

R04:P:MATH:LIE_VARIANCE
  FORMAL_STRUCTURE + SOURCE_ASSERTION_HYPOTHESIS/ASSUMPTION
```

The experimental-protocol units also mix procedures with expected outcomes or adjudication rules:

```text
R04:P:PROTOCOL:PHASE_I
R04:P:PROTOCOL:PHASE_II_III_IV
R04:P:PROTOCOL:PHASE_V_VI
R04:P:PROTOCOL:PHASE_VII
```

This violates the already-frozen R02 rule:

\[
\boxed{\text{source block identity} \neq \text{semantic standing identity}.}
\]

```text
MIXED_STANDING_UNITIZATION_R04 = HIT
```

**Shallowest locus:** R04 parse unitization.  
**Global parser-contract change:** `NO`.

## Hit B — `NOTATION_PREDICTION_OMISSION`

`docs/notation.md` explicitly states directional predictions in the Sample Size and Noise Level sections:

```text
dk*/dN > 0
dk*/dsigma < 0
```

The candidate dictionary unit preserves the symbol meanings but not those source assertions.

```text
NOTATION_PREDICTION_OMISSION = HIT
```

**Shallowest locus:** R04 parse coverage.  
**Minimal repair:** add a source-grounded prediction unit; do not infer the remaining response-surface derivatives from other files into the notation source.

## Verdict

```text
R04_SOURCE_SURFACE                     = FROZEN_FULL_RECURSIVE_HEAD
R04_RESEARCH_BEARING_BLOBS             = 11
R04_EXECUTABLE_SOURCE_BLOBS            = 6
R04_INITIAL_PARSE_UNITS                = 71
SOURCE_CODE_ROLE_BOUNDARY              = CONTAINED
MIXED_STANDING_UNITIZATION_R04         = HIT
NOTATION_PREDICTION_OMISSION            = HIT
NEW_GLOBAL_PARSER_ONTOLOGY_REQUIRED    = NO
R04_COMPRESSION                        = NOT_AUTHORIZED
R05_ACCESS                             = NOT_AUTHORIZED
MAP_EDGE_EMISSION                      = NONE
MAP_AUTHORITY                          = NONE
SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
CEREBRO_STEP_2                         = CLOSED
```

R04 has not yet earned a reusable parse. The demonstrated failures are local and must be repaired before compression.