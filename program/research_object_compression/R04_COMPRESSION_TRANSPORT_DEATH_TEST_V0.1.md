# R04 COMPRESSION TRANSPORT DEATH TEST V0.1

**Compression candidate:** `R04_COMPRESSION_V0.1.json`  
**Projection ledger:** `R04_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The test asks whether the effective R01-R03 compression contract transports to an executable research repository without losing role distinctions or manufacturing execution evidence.

## Transport successes

```text
EXECUTABLE_IMPLEMENTATION_AS_EXECUTED_EXPERIMENT      = CONTAINED
IMPLEMENTED_OUTPUT_AS_REPORTED_RESULT                  = CONTAINED
SYNTHETIC_CALIBRATION_AS_EMPIRICAL_FINDING             = CONTAINED
IMPLEMENTATION_ASSUMPTION_AS_SCIENTIFIC_HYPOTHESIS     = CONTAINED
PROTOCOL_PREDICTION_AS_METHOD                          = CONTAINED
SOURCE_STATUS_CODE_PRESENCE_RECONCILIATION             = CONTAINED
MULTIPLE_SOURCE_OCCURRENCES_AS_WARRANT_MULTIPLICITY    = CONTAINED_AT_ZERO_AUTHORITY_BOUNDARY
```

The existing `METHODOLOGY_OR_TEST_PROTOCOL` organizational coordinate is sufficient to hold executable research material when item-level roles remain explicit:

```text
SOURCE_TEST_PROTOCOL
EXECUTABLE_IMPLEMENTATION
IMPLEMENTATION_ASSUMPTION
IMPLEMENTATION_BEHAVIOR
IMPLEMENTED_OUTPUT_BEHAVIOR
```

Thus:

\[
\boxed{
\text{method specification}
\neq
\text{implementation}
\neq
\text{execution}
\neq
\text{result}.
}
\]

No new top-level compression coordinate is required by executable source code on R04.

## Hit — `RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE`

The candidate compression directly cites the same broad parse units in more than one primary compressed item:

```text
R04:P:MATH:PHASE_ERRORS
  -> R04:FORMAL:PHASE_MODEL
  -> R04:FORMAL:ERROR_VECTOR

R04:P:NOTATION:DICTIONARY_CORE
  -> R04:DEF:NOTATION_CORE
  -> R04:FORMAL:SYSTEM_ESTIMATOR
  -> R04:FORMAL:LIE_LADDER

R04:P:NOTATION:DICTIONARY_GAUGE_INFO
  -> R04:DEF:NOTATION_CORE
  -> R04:FORMAL:DUAL_INFORMATION
  -> R04:FORMAL:INVARIANTS_GAUGE

R04:P:NOTATION:ERRORS_PHASE_SYSTEMS
  -> R04:DEF:NOTATION_CORE
  -> R04:FORMAL:HORIZON_OBJECT
  -> R04:FORMAL:PHASE_MODEL
  -> R04:FORMAL:ERROR_VECTOR
```

The projection ledger assigns each unit exactly one primary destination, but the compression candidate silently reuses the raw parse-unit handles elsewhere.

This violates Amendment 003:

\[
\boxed{
\text{repeated representation}
\neq
\text{repeated source}
\neq
\text{independent warrant}.
}
\]

```text
RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE = HIT
```

**Shallowest locus:** R04 compression derivation topology.  
**Global contract change required:** `NO`; Amendment 003 already contains the repair rule.

**Minimal repair:**

1. each broad parse unit keeps exactly one primary compression destination;
2. source-local composite content may receive one dedicated primary compressed item when necessary;
3. other semantic views reference that primary item through typed secondary aliases;
4. aliases carry `AUTHORITY_EFFECT = NONE` and `WARRANT_MULTIPLICITY_EFFECT = NONE`.

## Verdict

```text
R04_EFFECTIVE_PARSE_UNIT_COUNT                 = 80
R04_PRIMARY_PROJECTION_ENTRY_COUNT             = 80
R04_UNMAPPED_PARSE_UNITS                       = 0
EXECUTABLE_RESEARCH_ROLE_TRANSPORT             = PROVISIONALLY_SUPPORTED
NEW_TOP_LEVEL_COMPRESSION_COORDINATE_REQUIRED  = NO
RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE             = HIT
R04_REUSABLE_NODE_STATE                        = NOT_YET_EARNED
R05_ACCESS                                      = NOT_AUTHORIZED
MAP_EDGE_EMISSION                               = NONE
MAP_AUTHORITY                                   = NONE
SCIENTIFIC_AUTHORITY                            = NONE
PROPAGATE_KERNEL                                = NOT_EARNED
CEREBRO_STEP_2                                  = CLOSED
```

R04 fails only at a derivation-accountability rule already earned on R03.