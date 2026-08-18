# RESEARCH_OBJECT_COMPRESSION_V0.1 — AMENDMENT 002

**Object:** `CEREBRO_RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_002`  
**Base contract:** `program/research_object_compression/RESEARCH_OBJECT_COMPRESSION_V0.1.md`  
**Prior amendment:** `program/research_object_compression/RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_001.md`  
**Trigger:** `program/research_object_compression/R02_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Record type:** minimal compression-derivation repair  
**Persistent record state:** `FROZEN`  
**Repair scope:** `PARSE_TO_COMPRESSION_PROJECTION_PROVENANCE_ONLY`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Propagation authorized:** `NO`

R02 demonstrated that an assertion such as:

```text
ALL_PARSE_UNITS_ACCOUNTED_FOR = true
```

is not itself sufficient warrant for loss-bounded compression.

The effective compression contract therefore gains one required derivation artifact:

```text
PARSE_TO_COMPRESSION_PROJECTION_LEDGER
```

## 1. Projection rule

For every admitted exhaustive parse unit `u`, the ledger must record exactly one primary disposition:

```text
DIRECT_TO_COMPRESSION_ITEM
LOSS_BOUNDED_GROUP_TO_COMPRESSION_ITEM
EXPLICIT_COMPRESSION_EXCLUSION
UNRESOLVED_AT_COMPRESSION
COMPRESSION_FAILURE
```

and identify the destination item or exclusion reason.

Thus:

\[
\boxed{
\forall u\in\Pi_i,
\exists!\,d(u)
}
\]

for the frozen projection ledger, where `d(u)` is the recorded compression disposition.

## 2. Grouping rule

A `LOSS_BOUNDED_GROUP_TO_COMPRESSION_ITEM` is permitted only when the destination preserves the distinctions necessary to recover:

```text
source locator
source standing label when present
item kind / semantic role
bounded content needed for later relation extraction
```

Grouping may reduce redundancy. It may not erase standing differences.

## 3. Exclusion rule

Compression exclusion must be explicit and source-bounded. Typical legal/project-process metadata may be excluded when the frozen compression scope says so.

```text
NOT_MAPPED != IRRELEVANT
```

## 4. Projection truthfulness

The compression may claim complete projection only if the ledger covers every effective parse unit after parse amendments.

\[
\boxed{
\text{coverage assertion}
\neq
\text{coverage warrant}.
}
\]

The ledger is the minimum projection warrant.

## 5. Historical preservation

R01 and R02 frozen compression attempts are not rewritten. Successor projection ledgers and overlays revalidate or repair them under this stronger accountability rule.

R01 must be rechecked first before R02 transport can pass.

## 6. Unaffected rules

```text
COMPRESSION != IMPORTANCE_SELECTION
DEFINITION != HYPOTHESIS != RESULT != NEGATIVE_RESULT
SOURCE_LOCATION != COMPRESSED_PAYLOAD
MAP_EDGE_EMISSION = FORBIDDEN
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
```

## 7. Status

```text
PARSE_TO_COMPRESSION_PROJECTION_LEDGER = REQUIRED
BASE_CONTRACT_MUTATED = NO
NEW_TOP_LEVEL_SEMANTIC_CLASS = NONE
R01_RETEST_REQUIRED = YES
R02_RETEST_AFTER_R01 = YES
R03_R43 = NOT_OPENED
```
