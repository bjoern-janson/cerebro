# R02 COMPRESSION TRANSPORT DEATH TEST V0.1

**Parse contract:** `program/research_object_compression/EXHAUSTIVE_RESEARCH_OBJECT_PARSE_V0.1.md`  
**R02 source surface:** `program/research_object_compression/R02_SOURCE_SURFACE_V0.1.json`  
**R02 exhaustive parse:** `program/research_object_compression/R02_EXHAUSTIVE_PARSE_V0.1.json`  
**R02 compression candidate:** `program/research_object_compression/R02_COMPRESSION_V0.1.json`  
**Record type:** cross-repository compression transport death test  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Cerebro Step 2 reopened:** `NO`

The test asks:

\[
\boxed{
\textbf{Does the R01-derived compression design remain adequate on R02 without losing distinctions or inventing new standing?}
}
\]

R02 is intentionally richer than R01: it contains formal definitions, source-described status, open problems, reported empirical results, CRM proxies, source interpretations of results, methodological limitations, and one reported failed test.

## 1. Transport successes

The existing top-level compression coordinates can represent R02's richer material without introducing a new seven-layer ontology.

The following separations survive structurally:

```text
REPORTED_RESULT != SOURCE_INTERPRETATION_OF_RESULT
REPORTED_RESULT != REPORTED_CRM_PROXY
FAILED_TEST != LIMITATION
LIMITATION != OPEN_PROBLEM
SOURCE_VALIDATION_LABEL != INDEPENDENT_VALIDATION
SOURCE_PROOF_LANGUAGE != SCIENTIFIC_STANDING_UPGRADE
```

The compression uses item-level `item_kind` plus source locators to preserve these distinctions.

```text
R01_TOP_LEVEL_COMPRESSION_VOCABULARY_TRANSPORT = PROVISIONALLY_SUPPORTED
```

## 2. Attack A — `SOURCE_VALIDATION_LABEL_AS_VALIDATION`

`BENCHMARKS.md` calls itself `Empirical Validations & Benchmarks` and says the tests validate IICG.

A lossy compressor could therefore write:

```text
IICG = EMPIRICALLY_VALIDATED
```

The candidate instead records this as `SOURCE_ASSERTION_ABOUT_VALIDATION` and separately stores reported result payloads.

```text
SOURCE_VALIDATION_LABEL_AS_VALIDATION = CONTAINED
```

## 3. Attack B — `PROXY_AS_DIRECT_MEASUREMENT`

Several benchmark sections label success-rate or solved-task deltas as empirical CRM proxies.

The candidate preserves:

```text
REPORTED_EMPIRICAL_RESULT_WITH_PROXY
```

and explicitly forbids:

```text
REPORTED_CRM_PROXY == DIRECT_CRM_MEASUREMENT
```

```text
PROXY_AS_DIRECT_MEASUREMENT = CONTAINED
```

## 4. Attack C — `RESULT_INTERPRETATION_COLLAPSE`

The benchmark reports numerical outcomes and then supplies interpretive `Observation` prose.

The candidate stores numerical outcomes under `REPORTED_RESULTS` and interpretive prose under `ASSERTIONS_OR_HYPOTHESES` with `item_kind = SOURCE_INTERPRETATION_OF_RESULT`.

```text
RESULT_INTERPRETATION_COLLAPSE = CONTAINED_FOR_8PUZZLE_GRAY_DP_COT
```

## 5. Attack D — `FAILED_TEST_CONCEPTUAL_ALIGNMENT_COLLAPSE`

The Kernel Trick limitation states two different things in one source bullet:

1. a simulated RBF-kernel test failed due to environment constraints;
2. the source nevertheless says the conceptual alignment holds.

The exhaustive parse currently represents both in one parse unit with unit kind:

```text
REPORTED_NEGATIVE_RESULT_OR_FAILED_TEST
```

and the compression retains both clauses inside one `REPORTED_FAILED_TEST` item.

That is insufficiently separated. The conceptual-alignment assertion could inherit the negative-result standing, or the failed test could be softened by the conceptual assertion.

The parser is already capable of recognizing both `REPORTED_NEGATIVE_RESULTS / FAILED_TESTS` and `SOURCE_ASSERTIONS / HYPOTHESES`; therefore this is not an aperture limitation. It is a parse-unit decomposition failure.

```text
FAILED_TEST_CONCEPTUAL_ALIGNMENT_COLLAPSE = HIT
```

**Shallowest locus:** exhaustive parse unitization / mixed-standing separability.

**Minimal repair:** split the source bullet into two source-coincident parse units with the same locator but distinct standings; compression must preserve them separately.

## 6. Attack E — `PARSE_ACCOUNTING_WITHOUT_MAPPING`

The R02 compression candidate asserts:

```text
all_parse_units_accounted_for = true
```

but does not include an explicit mapping from every parse-unit ID to either:

```text
COMPRESSION_ITEM
LOSS_BOUNDED_GROUP
EXPLICIT_EXCLUSION
UNRESOLVED
```

Because R02 is richer, manual category comparison is insufficient to prove the projection is loss-bounded. In particular, parse units such as methodological motivation, weighted-measure rationale, and AlphaZero high-level impact metrics are not individually traceable to a compression destination.

Thus:

\[
\boxed{
\text{coverage assertion}
\neq
\text{coverage warrant}.
}
\]

```text
PARSE_ACCOUNTING_WITHOUT_MAPPING = HIT
```

**Shallowest locus:** compression derivation/projection provenance.

**Minimal repair:** require a parse-to-compression projection ledger mapping every admitted parse unit to its compressed representation, grouping, exclusion, unresolved state, or failure.

## 7. Attack F — `WORK_IN_PROGRESS_VS_VALIDATION_RECONCILIATION`

README says empirical validation is work in progress while BENCHMARKS.md describes empirical validations.

The compressor could silently reconcile this into a single current standing.

The candidate preserves both source statements separately and performs no reconciliation.

```text
WORK_IN_PROGRESS_VS_VALIDATION_RECONCILIATION = CONTAINED
```

This is an internal source-state tension to preserve, not a contradiction the compressor may resolve.

## 8. Transport verdict

```text
R02_SOURCE_SURFACE                              = FROZEN_FULL_REPOSITORY_HEAD
R02_EXHAUSTIVE_PARSE                            = FROZEN_WITH_DEMONSTRATED_UNITIZATION_GAP
R02_COMPRESSION_CANDIDATE                       = FROZEN_FAILED_TRANSPORT_ATTEMPT
R01_TOP_LEVEL_COMPRESSION_VOCABULARY_TRANSPORT  = PROVISIONALLY_SUPPORTED
FAILED_TEST_CONCEPTUAL_ALIGNMENT_COLLAPSE       = HIT
PARSE_ACCOUNTING_WITHOUT_MAPPING                = HIT
NEW_TOP_LEVEL_SEMANTIC_CLASS_REQUIRED            = NO
PARSE_UNITIZATION_REPAIR_REQUIRED               = YES
PROJECTION_PROVENANCE_REPAIR_REQUIRED           = YES
R02_REUSABLE_NODE_STATE                         = NOT_YET_EARNED
R03_ACCESS                                       = NOT_AUTHORIZED
MAP_EDGE_EMISSION                                = NONE
MAP_AUTHORITY                                    = NONE
SCIENTIFIC_AUTHORITY                             = NONE
PROPAGATE_KERNEL                                 = NOT_EARNED
CEREBRO_STEP_2                                   = CLOSED
```

R02 does not falsify the R01-derived semantic vocabulary. It demonstrates that exhaustive parsing and loss-bounded compression require stronger **derivation accountability** before the design may scale.