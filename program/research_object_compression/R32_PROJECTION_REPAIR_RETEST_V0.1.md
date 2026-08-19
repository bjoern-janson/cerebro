# R32 PROJECTION REPAIR — RETEST V0.1

**Effective projection:** base ledger + `R32_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1_AMENDMENT_001`  
**Frozen head:** `16e6972de4f9c5dfb2039baa88d520a41ea7e613`

```text
EFFECTIVE_PARSE_UNITS                  = 83
EFFECTIVE_COMPRESSED_ITEMS             = 83
PRIMARY_PROJECTION_ENTRIES             = 83
DIRECT_TO_COMPRESSION_ITEM             = 69
UNRESOLVED_AT_COMPRESSION              = 14
LOSS_BOUNDED_GROUP_TO_COMPRESSION_ITEM = 0
EXPLICIT_COMPRESSION_EXCLUSION         = 0
COMPRESSION_FAILURE                    = 0
UNMAPPED_PARSE_UNITS                   = 0
DUPLICATE_PRIMARY_OWNERS               = 0
EXTRA_PROJECTION_UNITS                 = 0
SOURCE_PATH_MISMATCHES                 = 0
SOURCE_STANDING_MISMATCHES             = 0
OWNER_MAP_SHA256                       = caba827dea200d32ddd2eb4bad3386efc8ca1384b75f137fc62ba6d89b4d4247
```

The 14 repaired entries remain one-to-one owners of explicit compression items; only their primary projection disposition changes to preserve unresolved standing.

```text
SEMANTIC_UNIT_CHANGE                   = NONE
COMPRESSION_PAYLOAD_CHANGE             = NONE
SOURCE_COORDINATE_CHANGE               = NONE
STANDING_CHANGE                        = NONE
PROJECTION_REPAIR_RETEST               = PASS
TRANSPORT_DEATH_TEST_ACCESS            = OPEN
NEW_EPISTEMIC_DISTINCTION_REQUIRED     = NO
AMENDMENT_005                          = NOT_EARNED
```
