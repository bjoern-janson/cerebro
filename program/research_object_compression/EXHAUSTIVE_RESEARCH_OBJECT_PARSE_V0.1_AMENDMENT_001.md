# EXHAUSTIVE_RESEARCH_OBJECT_PARSE_V0.1 — AMENDMENT 001

**Object:** `CEREBRO_EXHAUSTIVE_RESEARCH_OBJECT_PARSE_V0.1_AMENDMENT_001`  
**Base contract:** `program/research_object_compression/EXHAUSTIVE_RESEARCH_OBJECT_PARSE_V0.1.md`  
**Trigger:** `program/research_object_compression/R02_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1.md`  
**Record type:** minimal parse-contract repair  
**Persistent record state:** `FROZEN`  
**Repair scope:** `MIXED_STANDING_UNITIZATION_ONLY`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R02 demonstrated that one source block may contain multiple parser-recognizable propositions with different standings.

The Kernel Trick limitation contains both:

```text
REPORTED_FAILED_TEST
SOURCE_CONCEPTUAL_ASSERTION
```

A parse unit may therefore not be defined solely by a heading, bullet, paragraph, or source block when doing so collapses distinct parser-recognizable standings.

## Repair rule

When one source-local block contains two or more distinctions that the frozen parser aperture can independently classify, the effective parse must emit separate source-coincident parse units.

\[
\boxed{
\text{source block identity}
\neq
\text{semantic standing identity}.
}
\]

The units may share exactly the same source locator. They remain distinct because their semantic dispositions differ.

Required preservation:

```text
SAME_SOURCE_LOCATION = ALLOWED
DISTINCT_PARSE_UNIT_ID = REQUIRED
DISTINCT_UNIT_KIND = REQUIRED_WHEN_STANDING_DIFFERS
```

The repair does not require clause splitting when no standing-relevant distinction is recognized under the frozen parser aperture.

## Non-inferences

```text
MULTIPLE_PARSE_UNITS_AT_ONE_LOCATION != MULTIPLE_INDEPENDENT_SOURCES
UNIT_COUNT != WARRANT_COUNT
SEMANTIC_SPLIT != TEXTUAL_INDEPENDENCE
```

## Historical rule

Frozen base parse artifacts are not rewritten. Repository-specific amendments overlay only the demonstrated mixed-standing collapse.

## Status

```text
MIXED_STANDING_UNITIZATION = REQUIRED
BASE_PARSE_CONTRACT_MUTATED = NO
NEW_SEMANTIC_ONTOLOGY = NO
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
```
