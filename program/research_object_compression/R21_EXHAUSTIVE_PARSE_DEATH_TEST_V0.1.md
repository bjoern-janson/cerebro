# R21 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/grounded-recursive-adaptation`  
**Frozen head:** `4d7365abe174c595473c02497394a2d8b47ab99c`  
**Frozen source surface:** 25/25 Markdown blobs  
**Parse candidate:** 349 parsed representations + 71 explicitly unresolved = 420 units  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Aperture accounting

```text
FROZEN_HEAD_PATHS             = 25
PARSE_INCLUDED                 = 25
PARSE_EXCLUDED_BY_SCOPE        = 0
PARSE_FAILED_PATHS             = 0
PARSE_UNSUPPORTED_PATHS        = 0
UNENUMERATED_PATHS             = 0
PARSED_REPRESENTATIONS         = 349
EXPLICITLY_UNRESOLVED          = 71
CANDIDATE_PARSE_UNITS          = 420
PARSER_FAILURES                = 0
```

Every frozen-head blob has at least one source-local parse unit. Developmental history is not counted as additional current-head parse content.

## 2. Attack matrix

```text
THETA_3_FACTOR_AS_THETA_4_FACTOR_IDENTITY                 = CONTAINED
THETA_STRUCTURAL_CONDITION_AS_VALIDATED_SCALAR_METRIC     = CONTAINED
THETA_GT_ZERO_AS_THETA_GT_EPSILON_EQUIVALENCE             = CONTAINED
MUTUAL_INFORMATION_AS_CAUSAL_AUTHORITY                     = CONTAINED
CORRELATION_AS_CAUSAL_DIRECTION                            = CONTAINED
KL_DIVERGENCE_AS_USEFUL_INFORMATION                        = CONTAINED
GAMMA_EXPRESSION_AS_VALIDATED_LEARNING_IMPROVEMENT         = CONTAINED
THETA_EXT_TIMES_THETA_INT_AS_SCALE_VALIDATED               = CONTAINED
DELTA_OMEGA_LEQ_C_AS_DIMENSIONALLY_ESTABLISHED             = CONTAINED
GROUNDING_PROBE_SPECIFICATION_AS_IDENTIFICATION_VALIDITY    = CONTAINED
SCIENTIFIC_HYPOTHESIS_LABEL_AS_EMPIRICAL_SUPPORT           = CONTAINED
BENCHMARK_SPECIFICATION_AS_EXECUTION                        = CONTAINED
EXPERIMENT_SPECIFICATION_AS_EXECUTION                       = CONTAINED
PREDICTED_REGIME_AS_OBSERVED_REGIME                        = CONTAINED
FALSIFICATION_CRITERION_AS_FALSIFICATION_EVENT              = CONTAINED
SUCCESSFUL_EVIDENCE_DESCRIPTION_AS_REPORTED_EVIDENCE       = CONTAINED
SOURCE_RELATION_ASSERTION_AS_ENDPOINT_IDENTITY              = CONTAINED
ENDPOINT_IDENTITY_AS_CORPUS_EDGE                            = CONTAINED
CONCEPTUAL_FIELD_COMPARISON_AS_EMPIRICAL_SUPERIORITY       = CONTAINED
APPLICATION_ANALOGY_AS_CROSS_DOMAIN_VALIDATION             = CONTAINED
SOURCE_STATUS_CLAIM_AS_PARSER_RESOLUTION_OF_GAPS            = CONTAINED
MALFORMED_MARKDOWN_AS_PARSER_FAILURE                       = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                    = CONTAINED
CURRENT_HEAD_PARSE_AS_HISTORICAL_LINEAGE                    = CONTAINED
```

No attack requires a parse repair.

## 3. Formal variants remain source-local

The frozen head contains at least three distinct Theta forms/uses:

```text
concepts/cget.md:
Theta_n = D_n * S_n * P_n

docs/experiments.md, formal_model.md, measurement.md, metrics.md:
Theta = D * S * P * V

formalism/theory/theta surfaces:
Theta is also used abstractly as a structural condition and compared to 0 and/or epsilon.
```

The parser does not infer that `V=1`, that the three-factor form is an earlier version, or that the four-factor form supersedes it. The unresolved relationship is retained explicitly.

```text
FORMAL_VARIANT_PRESERVATION = PASS
CANONICALIZATION_AUTHORITY  = NONE
```

## 4. Measurement language does not establish construct validity

R21 proposes measurement objects using mutual information, KL divergence, correlation, change ratios, products, and threshold predicates. The parse preserves those formulas as source formal structures while separately preserving the unresolved identification and calibration problems.

In particular:

```text
I(Delta A; Delta E) != established causal identification
Corr(Delta K, Delta E_real) != established causal direction
D_KL(R_next || R_now) != established useful information yield
Delta(Delta R/Delta E) != validated learning-improvement metric
D*S*P[*V] != validated scalar Theta
```

The source itself reinforces this ceiling in `open_problems.md`, `open_questions.md`, and `falsification.md` by treating measurement validity and probe identification as open problems.

```text
PROPOSED_METRIC_AS_VALIDATED_METRIC = CONTAINED
```

## 5. Experimental standing remains specification-only

The frozen repository contains documentation for:

- benchmark design,
- recursive training/probe methodology,
- measurement procedures,
- predicted regimes,
- falsification criteria,
- possible supporting evidence.

It contains no current-head code, datasets, notebooks, tests, run logs, result tables, persisted plots, or execution records.

```text
IMPLEMENTATION_PRESENT               = 0
EXECUTION_RECORD_PRESENT             = 0
SOURCE_REPORTED_EMPIRICAL_RESULTS    = 0
SOURCE_REPORTED_NEGATIVE_RESULTS     = 0
```

Therefore:

```text
benchmark specification != benchmark execution
experiment methodology  != experiment execution
prediction              != result
falsification criterion != falsification event
```

## 6. Explicit relation assertions stop before corpus topology

R21 explicitly states source-level relationships such as:

```text
GRA subset Ancestor Intelligence
Ancestor Intelligence depends on GRA
GRA -> adaptive stability -> Ancestor Intelligence -> agency propagation
```

Those propositions are preserved exactly as source-authored semantic assertions.

However, the frozen source does not resolve `Ancestor Intelligence` or `Adaptive Intelligence Loop` to an immutable repository/object identifier in the Cerebro corpus.

Thus:

```text
RELATION_ASSERTION_PRESENT = YES
ENDPOINT_IDENTITY_RESOLVED = NO
PROGRAM_EDGE_EMITTED       = NO
AUTHORITY_TRANSFER         = NONE
```

Semantic similarity to earlier parsed repositories is not consumed here.

## 7. Source status claims do not erase unresolved structure

`open_questions.md` describes the framework as conceptually specified, and `open_problems.md` says remaining challenges are not conceptual. Those are source-authored status statements.

The parser independently retains formal variants, threshold ambiguity, symbol-namespace pressure, dimensional gaps, construct-validity gaps, and identification gaps where the frozen source does not resolve them.

```text
SOURCE_STATUS_CLAIM_AS_PARSER_CLOSURE = CONTAINED
```

## 8. Source formatting is not source failure

`docs/experiments.md` contains malformed Markdown around the Theta equation. The intended four-factor multiplication is recoverable from the immediately surrounding component definitions, while the formatting defect itself remains explicitly unresolved.

```text
SOURCE_FORMATTING_DEFECT = PRESERVED
PARSER_FAILURE           = NO
SILENT_SOURCE_REWRITE    = NO
```

## 9. Recurrence does not multiply warrant

The same central equations, regimes, and claims recur across README, concepts, theory, formal model, metrics, measurement, experiments, glossary, architecture, and comparison surfaces.

Each occurrence remains source-local for provenance. Repetition inside one repository does not establish independent corroboration.

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

## 10. Death-test verdict

```text
R21_PARSE_CANDIDATE_UNITS            = 420
R21_EFFECTIVE_PARSE_UNITS            = 420
R21_PARSED_REPRESENTATIONS           = 349
R21_EXPLICITLY_UNRESOLVED            = 71
R21_PARSER_FAILURES                  = 0
R21_POST_PARSE_DEATH_TEST_REPAIR     = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED   = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
BASE_PARSE_CONTRACT_AMENDMENT        = NOT_EARNED
```

The existing exhaustive-parse phenotype transports to R21 without amendment.

Compression may proceed only from this 420-unit effective parse.
