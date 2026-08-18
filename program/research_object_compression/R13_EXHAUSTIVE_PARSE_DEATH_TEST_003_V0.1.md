# R13 EXHAUSTIVE PARSE — DEATH TEST 003 V0.1

**Persistent record state:** `FROZEN`

A direct enumeration of explicit parse-unit IDs in `R13_EXHAUSTIVE_PARSE_V0.1.json` yields:

```text
README units          = 6
RESULTS_SUMMARY units = 7
runner units          = 12
unique raw-blob units = 4
raw-path status units = 5
derived audit units   = 4
--------------------------------
explicit units        = 38
```

The base manifest declared:

```text
parse_unit_count = 39
parsed_units     = 39
```

Therefore:

```text
DECLARED_PARSE_CARDINALITY_MISMATCH = HIT
```

After Amendment 001 demotes four derived audit units, the correct effective primary-source count is:

```text
38 - 4 = 34
```

not 35.

## Localization

```text
FAILURE_LOCUS = PARSE ACCOUNTING / MANIFEST CARDINALITY
```

No source unit is missing and no semantic distinction changes.

Minimal repair:

```text
historical explicit candidate units = 38
effective primary source units      = 34
derived audit views                 = 4
```

Amendment 002's four role replacements apply within those 34 primary units and do not change cardinality.

```text
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
AMENDMENT_005                       = NOT_EARNED
MAP_EDGE                            = NONE
PROPAGATION                         = NONE
CEREBRO_STEP_2                      = CLOSED
```
