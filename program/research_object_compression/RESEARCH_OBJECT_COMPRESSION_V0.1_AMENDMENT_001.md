# RESEARCH_OBJECT_COMPRESSION_V0.1 — AMENDMENT 001

**Object:** `CEREBRO_RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_001`  
**Base contract:** `program/research_object_compression/RESEARCH_OBJECT_COMPRESSION_V0.1.md`  
**Base contract commit:** `d676e9bb7e98f287ededd295f4dcd420e73e9744`  
**Trigger:** `program/research_object_compression/R01_COMPRESSION_DEATH_TEST_V0.1.md`  
**Trigger commit:** `da27a83dafc18304d300835ec9a1b400cb933fa9`  
**Record type:** minimal compression-contract repair  
**Persistent record state:** `FROZEN`  
**Repair scope:** `R_scope + R_span ONLY`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Propagation authorized:** `NO`  
**Cerebro Step 2 reopened:** `NO`

This amendment repairs only the two demonstrated R01 compression failures:

```text
SOURCE_OMISSION_BY_COMPRESSION = HIT
PARAPHRASE_AS_SOURCE_SPAN       = HIT
```

No other compression rule is changed.

---

## 1. Repair R_scope — source-described scope/purpose

The effective V0.1 compression record gains one optional organizational coordinate:

```text
SOURCE_DESCRIBED_SCOPE_OR_PURPOSE
```

This coordinate exists only when the frozen repository surface explicitly states what the repository/framework studies, analyzes, targets, or is for.

It must preserve the source statement without converting that statement into:

- a validated scientific claim;
- an importance ranking;
- a result;
- a map edge;
- a scope inferred from repository name alone.

Thus:

\[
\boxed{
\text{source-described purpose}
\neq
\text{scientific result}
\neq
\text{importance ranking}.
}
\]

This coordinate is earned by the R01 opening description. It does not instantiate the proposed seven-layer #44 ontology.

---

## 2. Repair R_span — payload/source-location separability

Every semantic item must distinguish:

```text
CONTENT
```

from:

```text
SOURCE_LOCATOR
```

`CONTENT` may be a normalized compression payload.

`SOURCE_LOCATOR` must identify the supporting source location independently of the payload wording.

For V0.1, a sufficient locator is:

```text
SOURCE_REPOSITORY
SOURCE_COMMIT
SOURCE_PATH
SOURCE_BLOB
SOURCE_SECTION_PATH
```

or an exact line range if one is available.

An exact excerpt is optional. If present and labeled `EXACT_SOURCE_EXCERPT`, it must be verbatim.

A field named `supporting_text` that contains normalized notation, ellipses, or paraphrase must not be represented as an exact source excerpt.

Therefore:

\[
\boxed{
\text{compressed payload}
\neq
\text{source evidence span/location}.
}
\]

---

## 3. Effective provenance record

The effective semantic-item provenance schema is minimally:

```text
SOURCE_REPOSITORY
SOURCE_COMMIT
SOURCE_PATH
SOURCE_BLOB
SOURCE_SECTION_PATH | SOURCE_LINE_RANGE
EXTRACTION_MODE
```

Optional:

```text
EXACT_SOURCE_EXCERPT
```

The existing immutable source coordinates remain mandatory.

---

## 4. Historical preservation

The frozen base contract and first R01 compression are not rewritten.

For effective V0.1 reconstruction:

1. read the base compression contract;
2. apply this amendment only to the two demonstrated gaps;
3. preserve all unaffected rules exactly.

Likewise the R01 compression is repaired by a separate overlay rather than by replacing the failed first attempt.

---

## 5. Unaffected structure

The amendment does not change:

```text
DEFINITION != HYPOTHESIS != RESULT != NEGATIVE_RESULT
EMPTY_CATEGORY = SOURCE_BOUNDED_ONLY
MAP_EDGE_EMISSION = FORBIDDEN
COMPRESSION_AUTHORITY_EFFECT = NONE
MAP_AUTHORITY_EFFECT = NONE
SCIENTIFIC_AUTHORITY_EFFECT = NONE
PROCESSING_ORDER = R01_TO_R43
PROPAGATE_KERNEL = NOT_EARNED
CEREBRO_STEP_2 = CLOSED
```

No later repository is authorized by the amendment itself.

---

## 6. Frozen status

```text
RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_001 = FROZEN
R_scope                                         = REPAIRED_IN_SCHEMA
R_span                                          = REPAIRED_IN_SCHEMA
BASE_CONTRACT_MUTATED                           = NO
R01_BASE_COMPRESSION_MUTATED                    = NO
R01_RETEST_REQUIRED                             = YES
R02_COMPRESSION                                 = NOT_YET_AUTHORIZED
PROPAGATE_KERNEL                                = NOT_EARNED
MAP_AUTHORITY                                   = NONE
SCIENTIFIC_AUTHORITY                            = NONE
NEXT_OBJECT                                     = R01_COMPRESSION_AMENDMENT_001
```

The compression may normalize meaning for navigation.

It must still point precisely back to where that meaning came from.
