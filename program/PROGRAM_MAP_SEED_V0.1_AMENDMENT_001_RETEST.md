# PROGRAM MAP SEED V0.1 AMENDMENT 001 — RETEST

**Base map:** `program/PROGRAM_MAP_SEED_V0.1.json`  
**Base map commit:** `b9ded8322076fd718fa726360edd3af82b907754`  
**Trigger death test:** `program/PROGRAM_MAP_SEED_DEATH_TEST_V0.1.md`  
**Trigger commit:** `8543abbc82385852a50465ec06c6a8604e601aef`  
**Amendment:** `program/PROGRAM_MAP_SEED_V0.1_AMENDMENT_001.json`  
**Amendment commit:** `f737d46a5e35d434167df80be1def677d8e9fb5e`  
**Record type:** minimal repair retest  
**Persistent record state:** `FROZEN`  
**Retest family:** `CROSS_SOURCE_RELATION_PROVENANCE_ONLY`  
**Program-map authority:** `NONE`  
**Scientific synthesis authorized:** `NO`

This retest evaluates only the failure demonstrated in `PROGRAM_MAP_SEED_DEATH_TEST_V0.1.md`:

```text
CROSS_SOURCE_RELATION_WITH_SINGLE_SOURCE_PROVENANCE = HIT
```

No other map family is reopened.

---

## 1. Retest target A — FR-001 continuation relation

The original relation:

```text
REL:SSI_SPEC_CONTINUES_FR001
```

connected the SSI FR-001 benchmark to the Cerebro-preserved FR-001 question while citing only the SSI artifact.

The amendment now freezes:

```text
RELATION_BASIS = DERIVED_CROSS_SOURCE_IDENTITY
PROVENANCE = [
  CEREBRO_FRONTIER_FR001_ENTRY,
  SSI_FR001_SPEC
]
RELATION_STANDING = DERIVED_FROM_FROZEN_CROSS_SOURCE_IDENTITY
```

The first provenance member constitutes the earlier parked question and candidate invariant. The second constitutes the later SSI benchmark object carrying the same research target.

The edge no longer presents a cross-source identity relation as though a single source alone established the connection.

### Verdict

```text
FR001_CONTINUATION_PROVENANCE = REPAIRED
```

---

## 2. Retest target B — Cerebro Step 2 methodological precedent relation

The original relation:

```text
REL:CEREBRO_STEP2_PRECEDENT_FOR_SSI_FR001
```

cited the SSI preregistration but not the exact frozen Cerebro Step 2 artifact resolved as its source endpoint.

The amendment now freezes:

```text
RELATION_BASIS = EXPLICIT_CROSS_REFERENCE_WITH_RESOLVED_TARGET
PROVENANCE = [
  SSI_EXPLICIT_CROSS_REFERENCE,
  CEREBRO_FROZEN_STEP2_TARGET
]
RELATION_STANDING = SUPPORTED_BY_EXPLICIT_CROSS_REFERENCE_AND_TARGET_RESOLUTION
```

This separates two jobs:

1. the SSI source establishes that Cerebro Step 2 discipline is being used as methodological precedent only;
2. the Cerebro source resolves the exact historical object referenced by that relation.

### Verdict

```text
STEP2_PRECEDENT_PROVENANCE = REPAIRED
```

---

## 3. Attack — `MULTI_SOURCE_PROVENANCE_AS_MULTI_SOURCE_AUTHORITY`

### Construction

Because a relation now cites two frozen sources, the map treats the relation as carrying stronger scientific authority than a single-source relation.

### Containment

Both replacement relations retain:

```text
MAP_AUTHORITY_EFFECT = NONE
```

Multi-source provenance improves reconstructibility of the map edge. It does not aggregate scientific warrant.

Thus:

\[
\boxed{
\text{more complete relation provenance}
\neq
\text{more scientific authority}.
}
\]

### Verdict

```text
MULTI_SOURCE_PROVENANCE_AS_MULTI_SOURCE_AUTHORITY = CONTAINED
```

---

## 4. Attack — `DERIVED_IDENTITY_AS_SOURCE_IDENTITY_CLAIM`

### Construction

`DERIVED_CROSS_SOURCE_IDENTITY` is interpreted to mean that either source artifact itself explicitly asserted the full cross-project continuation relation.

### Containment

The relation basis is explicitly `DERIVED_CROSS_SOURCE_IDENTITY`, not `EXPLICIT_CROSS_REFERENCE`.

The map therefore preserves the distinction:

\[
\boxed{
\text{derived relation supported by multiple frozen sources}
\neq
\text{relation explicitly asserted by either source alone}.
}
\]

### Verdict

```text
DERIVED_IDENTITY_AS_SOURCE_IDENTITY_CLAIM = CONTAINED
```

---

## 5. Retest verdict

The demonstrated relation-provenance gap is repaired by the amendment without changing the research objects or expanding map authority.

```text
CROSS_SOURCE_RELATION_WITH_SINGLE_SOURCE_PROVENANCE = REPAIRED
PROGRAM_MAP_SEED_BASE                               = FROZEN_UNCHANGED
PROGRAM_MAP_AMENDMENT_001                           = FROZEN
EFFECTIVE_SEED_RELATION_PROVENANCE                  = PROVISIONALLY_ADEQUATE_ON_CURRENT_BOUNDED_COVERAGE
MAP_AUTHORITY                                       = NONE
PROGRAM_SYNTHESIS                                   = NOT_ESTABLISHED
PROGRAM_MAP_COMPLETENESS                            = NOT_ESTABLISHED
R01_R42_SEMANTIC_RELATIONS                          = NOT_INGESTED
R43_SSI_SEMANTIC_RELATIONS                          = FR001_LINEAGE_ONLY
STEP_2                                              = CLOSED
FR001                                               = NOT_ESTABLISHED
```

The effective first atlas is therefore admissible for its current narrow purpose:

\[
\boxed{
\text{membership + chronology + selected frozen cross-project lineage}
}
\]

It is **not** a complete semantic map of the research program.

---

## 6. Stopping boundary

This retest does not itself authorize bulk ingestion of R01-R42 semantics.

The next program-consolidation question is separate:

\[
\boxed{
\text{How should source-by-source semantic relation ingestion be bounded so that the map cannot manufacture its own connective tissue?}
}
\]

That question remains unopened by this retest.