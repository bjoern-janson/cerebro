# RESEARCH_OBJECT_COMPRESSION_V0.1 — AMENDMENT 004

**Object:** `CEREBRO_RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_004`  
**Trigger:** `R06_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Record type:** minimal compression-contract repair  
**Persistent record state:** `FROZEN`  
**Repair scope:** `R_occurrence ONLY`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Propagation authorized:** `NO`

R06 demonstrated:

```text
PRIMARY_SOURCE_RECURRENCE_AS_WARRANT_MULTIPLICITY = HIT
```

The existing contract distinguishes semantic redundancy from provenance redundancy and Amendment 003 distinguishes secondary representation reuse from independent warrant. R06 demonstrates a different multiplicity problem: several **distinct parse units** may be source occurrences of the same or closely related semantic object.

## 1. R_occurrence — source occurrence is not warrant independence

For any compressed item with more than one distinct primary source parse unit:

```text
SOURCE_OCCURRENCE_COUNT
WARRANT_INDEPENDENCE_STATUS
WARRANT_MULTIPLICITY_EFFECT
```

must be reconstructible.

Default semantics are:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

unless separate provenance establishes independence at the relevant evidential/warrant level.

Thus:

\[
\boxed{
\text{source-occurrence multiplicity}
\neq
\text{warrant independence}
\neq
\text{warrant multiplicity}.
}
\]

and:

\[
\boxed{
|\operatorname{SourceOccurrences}(x)|>1
\not\Rightarrow
|\operatorname{IndependentWarrants}(x)|>1.
}
\]

This rule applies even when source occurrences appear in different files or sections of the same repository.

## 2. Independence must be positively warranted

`WARRANT_INDEPENDENCE_STATUS` may not become `ESTABLISHED` merely because source occurrences differ by:

- file path;
- section;
- wording;
- date within the same lineage;
- author repetition;
- semantic role;
- compressed branch identity.

Independence requires separate evidence about the generating provenance sufficient for the independence claim being made.

Where independence is unresolved, preserve:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
```

rather than guessing dependence or independence.

## 3. Relation to Amendment 003

Amendment 003 governs:

\[
\text{one parse unit}
\rightarrow
\text{multiple compressed representations}.
\]

Its rule is:

\[
\text{repeated representation}
\neq
\text{repeated source}
\neq
\text{independent warrant}.
\]

Amendment 004 governs:

\[
\text{multiple distinct parse units}
\rightarrow
\text{one compressed semantic object}.
\]

Its rule is:

\[
\text{repeated source occurrence}
\neq
\text{independent warrant}.
\]

Neither rule replaces the other.

## 4. No suppression of provenance

This amendment does **not** authorize deleting repeated source occurrences.

The compression must still preserve every source branch required by the existing provenance rules.

Therefore:

\[
\boxed{
\text{preserve recurrence as provenance}
\quad\land\quad
\text{do not convert recurrence into warrant}.
}
\]

## 5. No new authority algebra

This amendment introduces no scalar evidence count, confidence score, authority weight, or independence coefficient.

```text
SOURCE_OCCURRENCE_COUNT      = descriptive accounting only
WARRANT_INDEPENDENCE_STATUS  = source/warrant provenance status only
WARRANT_MULTIPLICITY_EFFECT  = NONE by default
```

No edge, claim or scientific standing is strengthened by occurrence count alone.

## 6. Regression order

Because this amendment changes the effective compression semantics:

```text
R01_RETEST_REQUIRED = YES
R02_RETEST_AFTER_R01 = YES
R03_RETEST_AFTER_R02 = YES
R04_RETEST_AFTER_R03 = YES
R05_RETEST_AFTER_R04 = YES
R06_RETEST_AFTER_R05 = YES
R07_R43 = NOT_OPENED
```

Historical parse/compression artifacts remain frozen. A successor overlay or effective-contract interpretation may supply the new fields; prior records are not silently rewritten.

## 7. Unaffected structure

```text
SOURCE_SURFACE -> EXHAUSTIVE_PARSE -> PROJECTION_LEDGER -> COMPRESSION
SEMANTIC_REDUNDANCY MAY COLLAPSE
PROVENANCE BRANCHES MUST SURVIVE
SOURCE_ROLE DISTINCTIONS MUST SURVIVE
SECONDARY_ALIAS WARRANT_MULTIPLICITY_EFFECT = NONE
METHOD != EVIDENCE
IMPLEMENTED != EXECUTED != OBSERVED != ESTABLISHED
MAP_EDGE_EMISSION = FORBIDDEN
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
```
