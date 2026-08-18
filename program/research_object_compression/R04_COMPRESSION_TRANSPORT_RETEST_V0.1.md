# R04 COMPRESSION TRANSPORT RETEST V0.1

**Death test:** `R04_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Compression repair:** `R04_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Projection repair:** `R04_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest evaluates only `RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE` and preserves the executable-research non-regressions from the first transport test.

## 1. Primary projection ownership

Each of the 80 effective parse units now has exactly one primary compression destination.

`R04:P:MATH:PHASE_ERRORS` is owned by the source-local composite item:

```text
R04:FORMAL:MATH_PHASE_ERRORS_SOURCE
```

The broad notation units remain owned by:

```text
R04:DEF:NOTATION_CORE
```

```text
EFFECTIVE_PARSE_UNIT_COUNT        = 80
EFFECTIVE_PRIMARY_PROJECTIONS     = 80
UNMAPPED_PARSE_UNITS              = 0
DUPLICATE_PRIMARY_OWNERS          = 0
```

## 2. Secondary semantic views

Phase/error and notation recurrence in other compressed semantic views now occurs only through typed secondary aliases.

Every alias records:

```text
PRIMARY_COMPRESSION_ITEM
SOURCE_UNIT_SUBSET
SECONDARY_ROLE
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

No secondary view cites the raw parse unit as a second derivation branch.

```text
RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE = REPAIRED
ALIAS_AS_WARRANT                    = CONTAINED
```

## 3. Executable-research transport

R04 is the first tested repository with executable implementation artifacts. The existing compression contract preserves the following without a new top-level coordinate:

```text
SOURCE_TEST_PROTOCOL
EXECUTABLE_IMPLEMENTATION
IMPLEMENTATION_ASSUMPTION
IMPLEMENTATION_BEHAVIOR
IMPLEMENTED_OUTPUT_BEHAVIOR
```

under the organizational `METHODOLOGY_OR_TEST_PROTOCOL` coordinate.

The standing separations survive:

\[
\boxed{
\text{method}
\neq
\text{implementation}
\neq
\text{execution}
\neq
\text{result}.
}

Specifically:

- `main.py` hard-codes a nominal horizon and synthetic response formulas;
- `mdl_analysis.py` explicitly uses synthetic calibration arrays in its direct-run block;
- `analyze_horizon.py` loads the dataset but computes the frozen profile from N/sigma proxy formulas;
- programmed strings such as `Measured k*` and `Observer-Limited Architecture Confirmed` are potential runtime output behavior only;
- no frozen R04 run artifact is present.

Therefore:

```text
EXECUTABLE_IMPLEMENTATION_AS_EXECUTED_EXPERIMENT  = CONTAINED
IMPLEMENTED_OUTPUT_AS_REPORTED_RESULT              = CONTAINED
SYNTHETIC_CALIBRATION_AS_EMPIRICAL_FINDING         = CONTAINED
```

## 4. Preserved source tension

README lists `implement generator estimation pipeline` as a next milestone while the same frozen head contains `estimate_generator.py` implementing a polynomial/Ridge estimator module.

The compression preserves both source-relative facts and does not adjudicate whether the milestone is complete, partially complete, stale, or refers to integration rather than module existence.

```text
SOURCE_STATUS_CODE_PRESENCE_RECONCILIATION = CONTAINED
```

## 5. Transportability result

R04 required local parse and derivation repairs but **no new global parser ontology and no new top-level compression coordinate**.

The effective compression contract has now represented:

- small theoretical repositories;
- benchmark/result-bearing repositories;
- recursively nested heterogeneous research repositories;
- executable experimental repositories containing code, synthetic assumptions and potential runtime outputs.

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R04_FROZEN_HEADS
```

This is not universal transportability.

## 6. R04 verdict

```text
R04_SOURCE_SURFACE                         = FROZEN_FULL_RECURSIVE_HEAD
R04_TOTAL_BLOBS                            = 13
R04_RESEARCH_BEARING_BLOBS                 = 11
R04_EXECUTABLE_SOURCE_BLOBS                = 6
R04_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS       = 80
R04_PARSE_FAILURES                         = 0
R04_UNRESOLVED_PARSE_UNITS                 = 0
R04_PRIMARY_PROJECTION_ENTRIES             = 80
R04_UNMAPPED_PARSE_UNITS                   = 0
RAW_PARSE_UNIT_MULTI_PRIMARY_REUSE         = REPAIRED
EXECUTABLE_RESEARCH_ROLE_TRANSPORT         = SUPPORTED_ON_R04_FROZEN_HEAD
R04_REPORTED_EMPIRICAL_RESULTS             = NONE_ON_FROZEN_SOURCE_SURFACE
R04_REUSABLE_NODE_STATE                    = EARNED_ON_FROZEN_HEAD
R04_MAP_EDGE_EMISSION                      = NONE
R04_MAP_AUTHORITY                          = NONE
R04_SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```

## 7. Sequential boundary

```text
R05_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R06_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only and creates no R04 -> R05 semantic relation.

The first four research neurons are now reconstructible under one effective compression discipline. No synaptic propagation law exists.