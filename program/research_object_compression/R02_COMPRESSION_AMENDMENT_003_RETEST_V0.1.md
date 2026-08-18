# R02 COMPRESSION — AMENDMENT 003 RETEST V0.1

**Trigger:** `R02_COMPRESSION_AMENDMENT_003_REGRESSION_V0.1.md`  
**Compression repair:** `R02_COMPRESSION_V0.1_AMENDMENT_002.json`  
**Projection repair:** `R02_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`

The retest evaluates only the methodology-as-assertion regression exposed by Amendment 003.

The two parse units retain exactly their original content and source-relative semantic roles while moving from the legacy assertion view to the newly earned method coordinate:

```text
R02:P:README:MOTIVATION
  -> R02:METHOD:MOTIVATION

R02:P:README:WEIGHT_RATIONALE
  -> R02:METHOD:WEIGHT_RATIONALE
```

The legacy assertion representations remain historical but are superseded in effective reconstruction.

```text
LEGACY_METHODOLOGY_AS_ASSERTION = REPAIRED
R02_EFFECTIVE_PARSE_UNIT_COUNT  = 39
R02_EFFECTIVE_PROJECTION_COUNT  = 39
R02_UNMAPPED_PARSE_UNITS        = 0
R02_CONTENT_CHANGE              = NONE
R02_SOURCE_STANDING_CHANGE      = NONE
R02_SCIENTIFIC_STANDING_CHANGE  = NONE
R02_SECONDARY_REUSE_RULE        = PASSED_ON_REPAIRED_UNITS
R02_REUSABLE_NODE_STATE         = RE-EARNED_UNDER_AMENDMENT_003
R03_COMPRESSION_RETEST          = AUTHORIZED
R04_ACCESS                      = NOT_AUTHORIZED
MAP_AUTHORITY                   = NONE
SCIENTIFIC_AUTHORITY            = NONE
PROPAGATE_KERNEL                = NOT_EARNED
```

R02 demonstrates that a later earned compression distinction can reclassify the derived node representation without rewriting what the repository originally said.
