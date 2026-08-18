# R03 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Effective parse:** base + Amendments 001/002, 105 units  
**Compression candidate:** `R03_COMPRESSION_V0.1.json`  
**Projection ledger:** `R03_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Record type:** held-out compression transport death test  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The test asks whether the R01/R02-derived compression contract transports to R03 without losing parser-earned distinctions or manufacturing standing.

## Successes before failure

R03 confirms that the existing vocabulary can still represent definitions, formal structures, source hypotheses, source-reported results, source-reported negative/falsification pressure, limitations/open questions, status, applications/examples and unresolved named program references.

The candidate correctly preserves:

```text
SYNTHETIC_RESULT != HISTORICAL_EMPIRICAL_RESULT
SOURCE_VALIDATION_LANGUAGE != INDEPENDENT_VALIDATION
SIMULATED_RATER_COMPARISON != BLINDED_EXTERNAL_RATER_STUDY
SOURCE_PROPOSED_REFINEMENT != RETROACTIVE_SOURCE_REWRITE
SPECULATIVE_EXTENSION != CORE_CPB_CLAIM
NAMED_IICG_REFERENCE != RESOLVED_R01_ENDPOINT
```

However, three transport failures remain.

---

## Attack A — `METHODOLOGY_AS_ASSERTION`

R03 contains extensive parser-recognized methodological objects:

- measurement architecture;
- proxy definitions;
- structural-event detection rules;
- positive/false-positive/false-negative dataset construction;
- temporal validation procedure;
- prospective predictive benchmark;
- falsification criteria;
- synthetic adversarial test design;
- convergent-validity comparison design;
- case-specific controls and falsification procedures.

The frozen R01/R02 compression vocabulary has no top-level coordinate for method/test protocol. The candidate therefore projects twenty distinct methodological parse units into:

```text
ASSERTIONS_OR_HYPOTHESES
  -> R03:ASSERT:METHODOLOGY
```

This changes their semantic role. A procedure for testing a claim is not itself a claim about the world, and a falsification rule is not merely a limitation.

\[
\boxed{\text{method/test protocol}\neq\text{hypothesis/assertion}\neq\text{limitation}.}
\]

```text
METHODOLOGY_AS_ASSERTION = HIT
```

**Shallowest locus:** compression vocabulary / missing organizational coordinate.

**Earned repair pressure:** add one optional compression coordinate capable of preserving source-described methodology/test protocol without converting it into evidence, result or scientific standing.

---

## Attack B — `PARSE_STANDING_RECOLLAPSE_IN_COMPRESSION`

R03's parse was repaired specifically so distinct standings survive source unitization. The compression candidate then groups several of those units back into one compressed item.

Examples:

```text
R03:ASSERT:AUTODIFF
  CASE_SCOPE
  CASE_HYPOTHESIS
  CASE_MODEL
  CASE_PREDICTION
  HISTORICAL_INTERPRETATION
  CASE_VERDICT

R03:ASSERT:DEEP_SCALING
  FALSIFICATION_HYPOTHESIS
  HISTORICAL_INTERPRETATION
  EVIDENTIAL_ASSESSMENT
  CASE_VERDICT

R03:SPEC:CONSCIOUSNESS
  SCOPE_LIMIT
  SPECULATIVE_HYPOTHESES
```

The existing Amendment 002 grouping rule already forbids grouping that erases standing differences.

```text
PARSE_STANDING_RECOLLAPSE_IN_COMPRESSION = HIT
```

**Shallowest locus:** R03 local compression grouping.

**Global contract change required:** `NO` for this hit; the existing grouping rule is sufficient.

---

## Attack C — `SECONDARY_REUSE_WITHOUT_ROLE`

The primary projection ledger correctly gives every effective parse unit exactly one primary disposition. But the candidate also reuses some parse units in additional compression items, for example:

```text
case units -> primary case assertion
same case units -> APPLICATIONS_OR_EXAMPLES

consciousness/cross-domain units -> primary hypothesis/observation
same units -> APPLICATIONS_OR_EXAMPLES

program-lineage units -> more than one named reference item
```

Those secondary occurrences are not typed as aliases, derivational joins, or non-warrant-bearing navigation references.

A later graph could count the repeated compressed occurrences as repeated support even though they originate from one parse unit.

\[
\boxed{\text{secondary representation recurrence}\neq\text{independent warrant}.}
\]

```text
SECONDARY_REUSE_WITHOUT_ROLE = HIT
```

**Shallowest locus:** compression derivation accounting.

**Earned repair pressure:** every non-primary reuse must be explicitly role-typed and authority-inert, or replaced by a reference to the primary compressed item instead of repeating the parse unit as a new semantic occurrence.

---

## Contained attacks

```text
NESTED_SURFACE_OMISSION                 = CONTAINED
CASE_004_GAP_AS_NEGATIVE_HISTORY        = CONTAINED
SYNTHETIC_RESULT_AS_HISTORICAL_RESULT   = CONTAINED
SIMULATED_RATERS_AS_EXTERNAL_VALIDATION = CONTAINED
SOURCE_REFINEMENT_AS_RETROACTIVE_TRUTH  = CONTAINED
SPECULATION_AS_CORE_ONTOLOGY            = CONTAINED
IICG_NAME_AS_RESOLVED_R01_ENDPOINT       = CONTAINED
MAP_EDGE_EMISSION                        = NONE
```

---

## Verdict

```text
R03_SOURCE_SURFACE                       = FROZEN_FULL_RECURSIVE_HEAD
R03_EFFECTIVE_EXHAUSTIVE_PARSE           = ADEQUATE_ON_FROZEN_V0_1_APERTURE
R03_FIRST_COMPRESSION_CANDIDATE          = FROZEN_FAILED_TRANSPORT_ATTEMPT
METHODOLOGY_AS_ASSERTION                 = HIT
PARSE_STANDING_RECOLLAPSE_IN_COMPRESSION = HIT
SECONDARY_REUSE_WITHOUT_ROLE             = HIT
NEW_TOP_LEVEL_SEMANTIC_COORDINATE_NEEDED = METHODOLOGY_OR_TEST_PROTOCOL
LOCAL_GROUPING_REPAIR_REQUIRED           = YES
SECONDARY_REUSE_ACCOUNTING_REPAIR        = YES
R03_REUSABLE_NODE_STATE                  = NOT_YET_EARNED
R04_ACCESS                               = NOT_AUTHORIZED
MAP_AUTHORITY                            = NONE
SCIENTIFIC_AUTHORITY                     = NONE
PROPAGATE_KERNEL                         = NOT_EARNED
```

R03 does not require a larger epistemic brain. It requires the compression layer to stop treating test procedures as beliefs and repeated representations as repeated evidence.
