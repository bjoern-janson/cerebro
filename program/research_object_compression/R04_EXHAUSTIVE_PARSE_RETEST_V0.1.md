# R04 EXHAUSTIVE PARSE RETEST V0.1

**Death test:** `R04_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1.md`  
**Repair:** `R04_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`

The retest evaluates only the two demonstrated failures.

## Mixed-standing unitization

The eight failed units are replaced by source-coincident but role-separated units. Identity, scope, hypothesis, formal definition, experimental method, expected outcome and adjudication rule are no longer collapsed merely because they occur in one section.

```text
MIXED_STANDING_UNITIZATION_R04 = REPAIRED
```

## Notation prediction omission

The two explicit `docs/notation.md` directional predictions are now represented as their own source assertion unit:

```text
dk*/dN > 0
dk*/dsigma < 0
```

No other response-surface derivatives are imported into the notation source from other files.

```text
NOTATION_PREDICTION_OMISSION = REPAIRED
```

## Executable-source non-regression

The parse continues to distinguish:

```text
EXECUTABLE_IMPLEMENTATION
IMPLEMENTATION_ASSUMPTION
IMPLEMENTATION_BEHAVIOR
IMPLEMENTED_OUTPUT_BEHAVIOR
```

from:

```text
REPORTED_EMPIRICAL_RESULT
```

No run artifact exists on the frozen R04 head. Programmed strings such as `Measured k*` or `Observer-Limited Architecture Confirmed` therefore remain code behavior only.

```text
CODE_AS_EXECUTION_EVIDENCE = CONTAINED
```

## Verdict

```text
R04_EFFECTIVE_PARSE_UNIT_COUNT        = 80
R04_PARSE_FAILURES                    = 0
R04_UNRESOLVED_PARSE_UNITS            = 0
MIXED_STANDING_UNITIZATION_R04        = REPAIRED
NOTATION_PREDICTION_OMISSION          = REPAIRED
EXECUTABLE_SOURCE_ROLE                = PRESERVED
R04_EXHAUSTIVE_PARSE                  = ADEQUATE_ON_EFFECTIVE_V0_1_APERTURE
R04_COMPRESSION                       = AUTHORIZED
R05_ACCESS                            = NOT_AUTHORIZED
MAP_EDGE_EMISSION                     = NONE
MAP_AUTHORITY                         = NONE
SCIENTIFIC_AUTHORITY                  = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
CEREBRO_STEP_2                        = CLOSED
```

R04 is now eligible for the held-out compression transport test.