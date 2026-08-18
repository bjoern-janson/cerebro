# R01 COMPRESSION V0.1 AMENDMENT 001 — RETEST

**Base compression:** `program/research_object_compression/R01_COMPRESSION_V0.1.json`  
**Base compression commit:** `66045c165950ffc47d89992699619cd24fab20fb`  
**Trigger death test:** `program/research_object_compression/R01_COMPRESSION_DEATH_TEST_V0.1.md`  
**Trigger commit:** `da27a83dafc18304d300835ec9a1b400cb933fa9`  
**Contract amendment:** `program/research_object_compression/RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_001.md`  
**Contract-amendment commit:** `b320a8275ad5cdd41ef27eb1d5b35f877b6f2e75`  
**R01 amendment:** `program/research_object_compression/R01_COMPRESSION_V0.1_AMENDMENT_001.json`  
**R01-amendment commit:** `33b5809d4bff0af793d2d1d99a7335d1536afbab`  
**Record type:** bounded compression-repair retest  
**Persistent record state:** `FROZEN`  
**Retest families:** `SOURCE_OMISSION_BY_COMPRESSION`, `PARAPHRASE_AS_SOURCE_SPAN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Cerebro Step 2 reopened:** `NO`

This retest evaluates only the two failures demonstrated by the first R01 compression death test.

No other compression family is reopened.

---

## 1. Retest A — `SOURCE_OMISSION_BY_COMPRESSION`

### Original failure

The R01 README explicitly describes the repository as:

```text
A formal framework for analyzing how representations, tools, and interfaces alter the computational reach of bounded agents.
```

The first compression claimed coverage of the opening description but preserved no semantic coordinate for this source-described scope/purpose.

### Repair

The contract amendment adds the optional coordinate:

```text
SOURCE_DESCRIBED_SCOPE_OR_PURPOSE
```

and the R01 overlay now preserves the statement under:

```text
R01:SCOPE:01
```

with exact repository, commit, path, blob, section path, and exact excerpt.

The item is explicitly marked:

```text
SOURCE_DESCRIBED_SCOPE_OR_PURPOSE_ONLY
```

and does not become a result, hypothesis, importance score, or map edge.

### Verdict

```text
SOURCE_OMISSION_BY_COMPRESSION = REPAIRED
```

---

## 2. Retest B — `PARAPHRASE_AS_SOURCE_SPAN`

### Original failure

The first compression used `supporting_text` fields containing normalized paraphrases or notation without a distinct exact source locator.

The repository/commit/path/blob coordinates were immutable, but the reader still had to search the file semantically to find the exact local support.

### Repair

The contract amendment now requires source-location/payload separability.

Every R01 semantic item receives an effective locator consisting of:

```text
SOURCE_REPOSITORY
SOURCE_COMMIT
SOURCE_PATH
SOURCE_BLOB
SOURCE_SECTION_PATH
```

through the overlay's `item_level_source_locator_overrides`.

The existing `supporting_text` fields are explicitly reclassified as normalized locating aids / payload support summaries, not exact source excerpts.

The only field labeled `exact_source_excerpt` in the amendment is the verbatim R01 opening description.

Therefore the effective compression no longer relies on a paraphrase impersonating an exact source span.

### Verdict

```text
PARAPHRASE_AS_SOURCE_SPAN = REPAIRED
```

---

## 3. Non-regression check — `SCOPE_AS_IMPORTANCE`

### Construction

Because the new scope/purpose coordinate preserves the opening description, the compression promotes that description to the repository's `most important` idea.

### Containment

The coordinate records only source-described purpose/scope and contains no importance ordering.

The source's separate labels `central claim` and `central hypothesis` remain independently preserved.

### Verdict

```text
SCOPE_AS_IMPORTANCE = CONTAINED
```

---

## 4. Non-regression check — `LOCATOR_AS_WARRANT_UPGRADE`

### Construction

Because every compressed item now has more precise provenance, the compression treats the item as more scientifically warranted than it was before.

### Containment

Improved source localization changes reconstructibility only.

It does not change source standing or scientific authority.

\[
\boxed{
\text{better provenance precision}
\neq
\text{greater scientific warrant}.
}
\]

### Verdict

```text
LOCATOR_AS_WARRANT_UPGRADE = CONTAINED
```

---

## 5. Effective R01 compression state

The effective R01 V0.1 node state is reconstructed from:

```text
RESEARCH_OBJECT_COMPRESSION_V0.1.md
+ RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_001.md
+ R01_SOURCE_SURFACE_V0.1.json
+ R01_COMPRESSION_V0.1.json
+ R01_COMPRESSION_V0.1_AMENDMENT_001.json
```

The historical first attempt and death test remain preserved.

The effective state now preserves:

1. immutable repository/head identity;
2. complete frozen-head path enumeration;
3. explicit source-described scope/purpose;
4. source-described status;
5. formal definitions;
6. formal structures;
7. source-labelled assertions/hypotheses;
8. bounded absence of reported results and negative results;
9. applications/examples without validation leakage;
10. internal reference without map-edge emission;
11. explicit absence dispositions for cross-repository and unresolved references;
12. item-level source locations separate from normalized payloads.

No scientific synthesis is added.

---

## 6. R01 verdict

```text
R01_SOURCE_SURFACE                         = FROZEN_FULL_REPOSITORY_HEAD
R01_FIRST_COMPRESSION                      = FROZEN_FAILED_FIRST_ATTEMPT
R01_COMPRESSION_AMENDMENT_001              = FROZEN
SOURCE_OMISSION_BY_COMPRESSION             = REPAIRED
PARAPHRASE_AS_SOURCE_SPAN                  = REPAIRED
SCOPE_AS_IMPORTANCE                        = CONTAINED
LOCATOR_AS_WARRANT_UPGRADE                 = CONTAINED
R01_EFFECTIVE_COMPRESSION                  = ADEQUATE_ON_FROZEN_V0_1_DEATH_TEST
R01_REUSABLE_NODE_STATE                    = EARNED_ON_FROZEN_HEAD
R01_REPORTED_RESULTS                       = NOT_OBSERVED_ON_FROZEN_SOURCE_SURFACE
R01_REPORTED_NEGATIVE_RESULTS              = NOT_OBSERVED_ON_FROZEN_SOURCE_SURFACE
R01_CROSS_REPOSITORY_EDGES                 = NONE_EMITTED
R01_MAP_AUTHORITY                          = NONE
R01_SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```

---

## 7. Sequential authorization boundary

The contract required R01 to survive its compression death test before proceeding chronologically.

That condition is now satisfied for the frozen V0.1 surface.

Therefore:

```text
R02_PROGRAM_COMPRESSION_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R03_R43_PROGRAM_COMPRESSION_ACCESS = NOT_YET_OPENED
```

This authorization is procedural only.

It grants no semantic relation between R01 and R02.

\[
\boxed{
R01\text{ compressed before }R02
\not\Rightarrow
R01\text{ supports, causes, or precedes }R02\text{ conceptually}.
}
\]

The first research neuron is now a reconstructible compressed state.

It still has zero propagation law and zero authority to wire itself to the next neuron.
