# RESEARCH_OBJECT_COMPRESSION_V0.1 — AMENDMENT 003

**Object:** `CEREBRO_RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_003`  
**Trigger:** `R03_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Record type:** minimal compression-contract repair  
**Persistent record state:** `FROZEN`  
**Repair scope:** `R_method + R_reuse ONLY`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Propagation authorized:** `NO`

R03 demonstrated two contract-level gaps:

```text
METHODOLOGY_AS_ASSERTION     = HIT
SECONDARY_REUSE_WITHOUT_ROLE = HIT
```

The existing loss-bounded grouping rule already governs `PARSE_STANDING_RECOLLAPSE_IN_COMPRESSION`; no new rule is added for that local R03 failure.

## 1. R_method — source methodology/test protocol

The effective compression record gains one optional organizational coordinate:

```text
METHODOLOGY_OR_TEST_PROTOCOL
```

It is used only for source-grounded material whose semantic role is how a research claim, model, case, benchmark, dataset, falsification criterion or validation procedure is to be constructed or tested.

Examples include:

```text
measurement protocol
case-selection protocol
positive/negative control design
proxy specification
falsification criterion
predefined temporal horizon rule
test procedure
benchmark design
```

The coordinate must preserve source standing and must not convert method into evidence or scientific standing.

\[
\boxed{
\text{method/test protocol}
\neq
\text{hypothesis/assertion}
\neq
\text{reported result}
\neq
\text{limitation}.
}
\]

A methodological item may itself contain an explicit limitation or assumption only if those distinct standings remain separately recoverable; otherwise parse/compression standing separability governs.

This is a compression-level organizational coordinate, not a new Cerebro constitutional or #44 network ontology class.

## 2. R_reuse — secondary representation accounting

Amendment 002 requires exactly one primary projection disposition for every effective parse unit. R03 demonstrates that primary accounting alone is insufficient when the same parse unit is represented again elsewhere in the compression.

Every non-primary semantic reuse must now satisfy exactly one of:

```text
REFERENCE_TO_PRIMARY_COMPRESSION_ITEM
TYPED_SECONDARY_ALIAS
```

A `TYPED_SECONDARY_ALIAS` must identify:

```text
PRIMARY_COMPRESSION_ITEM
SECONDARY_ROLE
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

No secondary alias may cite the parse unit as though it were a second independent source occurrence.

Thus:

\[
\boxed{
\text{repeated representation}
\neq
\text{repeated source}
\neq
\text{independent warrant}.
}
\]

Where possible, navigation/application views should reference the already-compressed primary item rather than duplicate source-unit derivation.

## 3. Unaffected structure

```text
SOURCE_SURFACE -> EXHAUSTIVE_PARSE -> PROJECTION_LEDGER -> COMPRESSION
DEFINITION != HYPOTHESIS != RESULT != NEGATIVE_RESULT
SOURCE_LOCATION != COMPRESSED_PAYLOAD
SOURCE_BLOCK != EPISTEMIC_UNIT
GROUPING_MAY_NOT_ERASE_STANDING
MAP_EDGE_EMISSION = FORBIDDEN
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
```

## 4. Regression order

Because this amendment changes the effective compression contract:

```text
R01_RETEST_REQUIRED = YES
R02_RETEST_AFTER_R01 = YES
R03_RETEST_AFTER_R02 = YES
R04_R43 = NOT_OPENED
```

The historical R01/R02 compressions are not silently rewritten. If the new coordinate exposes an earlier omission, repair occurs by overlay.
