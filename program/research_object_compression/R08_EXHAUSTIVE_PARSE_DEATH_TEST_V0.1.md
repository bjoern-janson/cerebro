# R08 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Parse manifest:** `R08_EXHAUSTIVE_PARSE_V0.1.json`  
**Source surface:** `R08_SOURCE_SURFACE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The test attacks whether the R01–R07 effective parse discipline transports to the substantially larger and more heterogeneous R08 frozen head without inventing reconciliation, validation or empirical standing.

## A. `SOURCE_PATH_COVERAGE`

Frozen source inventory contains 49 blob paths, of which 48 are admitted and one (`LICENSE`) is excluded by frozen scope.

The four parse payloads account for all 48 admitted path occurrences.

```text
ADMITTED_SOURCE_PATHS = 48
PARSE_PAYLOAD_SOURCE_PATHS = 48
UNACCOUNTED_SOURCE_PATHS = 0
SOURCE_PATH_COVERAGE = CONTAINED
```

## B. `PATH_OCCURRENCE_AS_CONTENT_INDEPENDENCE`

`generator_adaptation.py` and `recursive_improvement.py` are two path occurrences of the exact same blob:

```text
00dbdd02405a5838e148badf4262b67479367e50
```

The second path is represented as an exact-content occurrence referring to the first content parse.

```text
PATH_OCCURRENCE_COUNT = 2
UNIQUE_CONTENT_BLOB_COUNT = 1
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

```text
PATH_OCCURRENCE_AS_CONTENT_INDEPENDENCE = CONTAINED
```

## C. `ONE_BYTE_SCRIPT_AS_NEGATIVE_RESULT`

`execution_barrier_phase_boundary.py` is a real path/blob containing exactly one newline.

The parse records only the artifact-content state.

```text
FAILED_EXPERIMENT = NOT_INFERRED
NEGATIVE_RESULT = NOT_INFERRED
EXECUTION_RECORD = NOT_INFERRED
ABSENT_ARTIFACT = NOT_INFERRED
ONE_BYTE_SCRIPT_AS_NEGATIVE_RESULT = CONTAINED
```

## D. `SOURCE_INTERNAL_INCOMPLETENESS_AS_PARSER_FAILURE`

`experiments/README.md` genuinely terminates immediately after:

```text
Each experiment should contain:
```

The parse emits one `UNRESOLVED_SOURCE_FRAGMENT` rather than completing the template, deleting the fragment or classifying the parser as failed.

```text
R08:P:EXP:TEMPLATE_TERMINAL = UNRESOLVED_AT_PARSE_DUE_TO_SOURCE_BLOB_TERMINATION
SOURCE_INTERNAL_INCOMPLETENESS_AS_PARSER_FAILURE = CONTAINED
```

## E. `CROSS_FILE_FORMAL_INCONSISTENCY_AS_RECONCILIATION`

R08 contains several source formulations of evolutionary velocity:

```text
Omega = Delta_G = (partial log|P_reach| / partial G_m) dot G_m
```

while the source-labelled canonical state-transition document writes:

```text
Omega = dG_m/dt
```

and simulation/measurement files instantiate several additional operational proxies.

The manifest explicitly records this as:

```text
PRESERVED_UNRESOLVED_CROSS_SOURCE_FORMAL_TENSION
RECONCILIATION_AUTHORITY = NONE
```

The parser does not silently choose one formula, average them, or infer semantic identity.

```text
CROSS_FILE_FORMAL_INCONSISTENCY_AS_RECONCILIATION = CONTAINED
```

## F. `SOURCE_LABEL_CANONICAL_AS_SUPERSESSION`

`state_transition_equations.md` labels itself the canonical dynamical system. The parse preserves that source self-label as `SOURCE_DESCRIBED_STATUS` only.

It does not infer that all earlier definitions/formalisms are historically superseded.

```text
SOURCE_LABEL_CANONICAL_AS_SUPERSESSION = CONTAINED
```

## G. `ASSUMPTION_AS_SUPPORTED_CLAIM`

`formal/assumptions.md` explicitly states twenty assumptions and says they are not claims of universal truth.

The parse preserves the A1–A20 distinctions under:

```text
SOURCE_STANDING = EXPLICIT_ASSUMPTION_SET
```

and separately preserves the source-labelled strongest assumption.

```text
ASSUMPTION_AS_SUPPORTED_CLAIM = CONTAINED
```

## H. `PROPOSED_PROXY_AS_VALIDATED_MEASURE`

The measurement layer presents latent quantities, proxy families, possible estimators, candidate composites and empirical designs. The parser preserves these under methodology/protocol roles.

No proxy is converted into a reported validation result merely because it has a formula or implementation.

```text
PROPOSED_PROXY_AS_VALIDATED_MEASURE = CONTAINED
```

## I. `PROPOSED_DATASET_AS_EMPIRICAL_DATA`

`phase_boundary_dataset.md` calls itself a proposed empirical framework and contains candidate entries/expected signals.

The parser records schema, candidate entries, expected ordering and methodology, not empirical observations.

```text
PROPOSED_DATASET_AS_EMPIRICAL_DATA = CONTAINED
```

## J. `HISTORICAL_INTERPRETATION_AS_VALIDATION`

Historical case files use strong phrases such as `canonical example` and `demonstrates`. Elsewhere, `theory/phase_transitions.md` explicitly says the historical examples are hypotheses for testing, not confirmed demonstrations.

The parser preserves both source-relative branches and does not resolve the tension by promoting case rhetoric to validation.

```text
HISTORICAL_INTERPRETATION_AS_VALIDATION = CONTAINED
```

## K. `IMPLEMENTED_EVALUATOR_AS_EXECUTED_RESULT`

R08 contains Python modules and simulations whose direct-run blocks can print labels including:

```text
Framework supported
Evidence consistent with
Phase boundary detected
```

The frozen repository contains code, not an admitted execution-result surface.

The parse therefore stores code as implementation/assumptions/output behavior only.

```text
IMPLEMENTED_EVALUATOR_AS_EXECUTED_RESULT = CONTAINED
PROGRAMMED_SUPPORT_LABEL_AS_SCIENTIFIC_SUPPORT = CONTAINED
```

## L. `SIMULATION_PROXY_AS_UNIFIED_OMEGA_MEASURE`

Simulation files operationalize `Omega` in several incompatible/file-local ways, including generator capacity, generator change, change in capability velocity, capability-gain times generator change, and change in improvement-efficiency.

The parse records:

```text
SEMANTIC_IDENTITY = NOT_ESTABLISHED_AS_ONE_OPERATIONAL_ESTIMATOR
```

```text
SIMULATION_PROXY_AS_UNIFIED_OMEGA_MEASURE = CONTAINED
```

## M. `LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE`

Measurement prose uses phrases such as `multiple independent signals`, and other source prose calls mathematical components independent.

The parse preserves the language but gives it no Amendment-004 warrant effect.

```text
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE = CONTAINED
```

## N. `ADMITTED_CFF_FIELD_OMISSION`

The admitted `CITATION.cff` source contains, in addition to title/abstract/version/repository metadata:

- the explicit citation message: `If you use this framework in research, please cite this work.`;
- ten source keywords: adaptive systems, evolutionary dynamics, complex systems, cybernetics, information theory, artificial intelligence, dynamical systems, innovation theory, search theory, self-improvement;
- the CFF schema version `1.2.0`.

The first Part-A parse preserves the abstract, version/release, author and repository field but does not preserve the citation instruction, keyword list or CFF schema version.

Because `CITATION.cff` was admitted rather than scope-excluded, these distinctions may not silently disappear.

```text
ADMITTED_CFF_FIELD_OMISSION = HIT
```

Failure locus:

```text
PARSE COVERAGE / SOURCE METADATA
```

This does not require a new parser role or top-level compression coordinate. A local R08 parse overlay is sufficient.

## O. Accounting status before repair

The candidate manifest currently declares:

```text
PARSE_UNITS = 393
PARSED = 392
UNRESOLVED = 1
PARSER_FAILURES = 0
```

After repairing attack N, counts must be re-derived rather than silently retained.

## Verdict

```text
SOURCE_PATH_COVERAGE                           = CONTAINED
PATH_OCCURRENCE_AS_CONTENT_INDEPENDENCE        = CONTAINED
ONE_BYTE_SCRIPT_AS_NEGATIVE_RESULT             = CONTAINED
SOURCE_INTERNAL_INCOMPLETENESS_AS_PARSER_FAILURE = CONTAINED
CROSS_FILE_FORMAL_INCONSISTENCY_AS_RECONCILIATION = CONTAINED
SOURCE_LABEL_CANONICAL_AS_SUPERSESSION         = CONTAINED
ASSUMPTION_AS_SUPPORTED_CLAIM                  = CONTAINED
PROPOSED_PROXY_AS_VALIDATED_MEASURE             = CONTAINED
PROPOSED_DATASET_AS_EMPIRICAL_DATA              = CONTAINED
HISTORICAL_INTERPRETATION_AS_VALIDATION         = CONTAINED
IMPLEMENTED_EVALUATOR_AS_EXECUTED_RESULT        = CONTAINED
SIMULATION_PROXY_AS_UNIFIED_OMEGA_MEASURE       = CONTAINED
LEXICAL_INDEPENDENCE_AS_WARRANT_INDEPENDENCE    = CONTAINED
ADMITTED_CFF_FIELD_OMISSION                     = HIT

GLOBAL_CONTRACT_FAILURE                         = NO
NEW_PARSER_ROLE_EARNED                          = NO
NEW_TOP_LEVEL_COMPRESSION_COORDINATE_EARNED     = NO
R08_COMPRESSION_AUTHORIZED                      = NO
MAP_AUTHORITY                                   = NONE
SCIENTIFIC_AUTHORITY                            = NONE
PROPAGATE_KERNEL                                = NOT_EARNED
CEREBRO_STEP_2                                  = CLOSED
```
