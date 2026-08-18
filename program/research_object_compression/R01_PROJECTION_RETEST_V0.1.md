# R01 PROJECTION RETEST V0.1

**Trigger:** `R01_PARSE_PROJECTION_DEATH_TEST_V0.1.md`  
**Repair:** `R01_COMPRESSION_V0.1_AMENDMENT_002.json`  
**Projection ledger:** `R01_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Record type:** bounded regression retest  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest evaluates only the source-provenance branch loss demonstrated after Amendment 002 made parse-to-compression projection accountability explicit.

## 1. Repair check

The four README Core Model parse units now project into existing compressed semantic items while retaining both source-local provenance branches:

```text
README summary branch
+
formalism detailed branch
```

No duplicate scientific warrant is inferred from the two source locations.

\[
\boxed{
\text{multiple source locations}
\neq
\text{multiple independent warrants}.
}
\]

```text
R01_DUPLICATE_SEMANTICS_SOURCE_PROVENANCE_LOSS = REPAIRED
```

## 2. Complete projection check

The frozen ledger contains one disposition for each of the 21 effective R01 parse units.

```text
EFFECTIVE_PARSE_UNIT_COUNT = 21
PROJECTION_ENTRY_COUNT = 21
UNMAPPED_PARSE_UNITS = 0
COMPRESSION_FAILURES = 0
```

## 3. Non-regression

The repair adds no semantic item, no new claim, no result, no edge, and no authority.

The original R01 compression and prior amendments remain frozen historical artifacts.

## 4. Verdict

```text
R01_EXHAUSTIVE_PARSE = ADEQUATE_ON_FROZEN_V0_1_APERTURE
R01_PARSE_TO_COMPRESSION_PROJECTION = COMPLETE
R01_EFFECTIVE_COMPRESSION = ADEQUATE_UNDER_AMENDMENT_002
R01_REUSABLE_NODE_STATE = RE-EARNED_UNDER_STRONGER_PROJECTION_ACCOUNTABILITY
R01_MAP_EDGE_EMISSION = NONE
R01_MAP_AUTHORITY = NONE
R01_SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
R02_RETEST = AUTHORIZED
R03_R43 = NOT_OPENED
```

R01 survives the stronger exhaustive-parse design after one provenance-only repair.