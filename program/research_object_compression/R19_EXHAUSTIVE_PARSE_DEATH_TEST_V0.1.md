# R19 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Candidate:** `R19_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-C  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R19 is the first post-R18 surface with deliberate multi-document restatement, proposed axioms, equations, benchmark design, experiment design, two Azus mapping surfaces, external product vocabulary, and source-local formal variants. The death test asks whether the parser preserves these distinctions without turning recurrence into warrant, specification into execution, or same-symbol reuse into identity.

## 1. Candidate accounting

The explicit ID spaces are continuous:

```text
R19P0001-R19P0287 = 287 parsed-representation units
R19U0001-R19U0058 = 58 unresolved-source units
TOTAL              = 345 explicit units
DUPLICATE IDS       = 0
MISSING IDS         = 0
```

However Part A's embedded count header declares:

```text
82 parsed + 16 unresolved = 98
```

while its explicit IDs actually contain:

```text
90 parsed + 16 unresolved = 106
```

Therefore:

```text
DECLARED_PARSE_CARDINALITY_MISMATCH = HIT
SOURCE_UNIT_LOSS                     = NOT_DETECTED
```

This is a local metadata defect, not evidence for a new parser role.

## 2. Attack matrix

```text
DECLARED_PARSE_CARDINALITY_MISMATCH                 = HIT_LOCAL_METADATA
THEORY_OR_AXIOM_AS_EMPIRICAL_RESULT                 = CONTAINED
BENCHMARK_SPECIFICATION_AS_EXECUTION                 = CONTAINED
BENCHMARK_SUCCESS_CRITERION_AS_REPORTED_SUCCESS     = CONTAINED
SOURCE_WORD_PROVES_AS_ACTUAL_VALIDATION              = CONTAINED
EXPERIMENT_SPECIFICATION_AS_EXECUTION                = CONTAINED
EXPECTED_RESULT_AS_REPORTED_RESULT                   = CONTAINED
OBSERVED_PHENOMENON_LABEL_AS_EXECUTION_EVIDENCE      = CONTAINED
FALSIFICATION_CRITERION_AS_FALSIFICATION_EVENT       = CONTAINED
AZUS_MAPPING_AS_IMPLEMENTATION_IDENTITY               = CONTAINED
PDM_REFERENCE_AS_RESOLVED_EXTERNAL_ENDPOINT           = CONTAINED
CROSS_FILE_RESTATEMENT_AS_INDEPENDENT_WARRANT         = CONTAINED
SAME_EQUATION_RECURRENCE_AS_REPLICATION               = CONTAINED
SAME_SYMBOL_AS_SAME_OBJECT                            = CONTAINED
FORMAL_VARIANT_AS_CANONICAL_EQUIVALENCE               = CONTAINED
CORRECTION_EVENT_CRITERIA_VARIANT_AS_SILENT_IDENTITY  = CONTAINED
UNRESOLVED_OPERATIONALIZATION_AS_PARSER_FAILURE       = CONTAINED
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY        = CONTAINED
LICENSE_OMISSION_AS_UNSEEN_PATH                        = CONTAINED
CROSS_REPOSITORY_VOCABULARY_AS_EDGE                   = CONTAINED
```

## 3. Contained — theory, axioms, benchmark and experiment standing

The repository repeatedly uses strong language: `axiom`, `main stability equation`, `core conservation principle`, `proves`, `expected result`, `falsified`, and one schematic is even headed `Observed phenomenon`.

The parse does not let those lexical labels determine empirical standing.

```text
proposed axiom/formalism = THEORY/HYPOTHESIS/FORMAL_STRUCTURE
correctability benchmark = METHODOLOGY/TEST SPECIFICATION
correction-loop simulation = EXPERIMENT SPECIFICATION
expected result = PREDICTION
falsification criterion = TEST CRITERION
```

The `Observed phenomenon` phrase is preserved as a source-described illustration plus an explicit unresolved provenance fragment:

```text
R19P0213 = SOURCE_DESCRIBED_ILLUSTRATION
R19U0040 = EXECUTION PROVENANCE NOT ESTABLISHED
```

No executable simulation, dataset, run log, seed manifest, persisted output, or benchmark result appears on the frozen head.

Therefore:

```text
THEORY_OR_AXIOM_AS_EMPIRICAL_RESULT             = CONTAINED
BENCHMARK_SPECIFICATION_AS_EXECUTION             = CONTAINED
EXPERIMENT_SPECIFICATION_AS_EXECUTION            = CONTAINED
EXPECTED_RESULT_AS_REPORTED_RESULT               = CONTAINED
OBSERVED_PHENOMENON_LABEL_AS_EXECUTION_EVIDENCE = CONTAINED
```

## 4. Contained — external product and substrate mappings

R19 names PDM, Westfield Innovations, Azus, Mesh Network, pressure, signatures, and Carl. These references are source-local context, not resolved program endpoints.

The parse preserves:

```text
PDM/Azus source descriptions and proposed mappings
```

while retaining unresolved endpoint/version/implementation identity where the repository does not pin it.

```text
AZUS_MAPPING_AS_IMPLEMENTATION_IDENTITY     = CONTAINED
PDM_REFERENCE_AS_RESOLVED_EXTERNAL_ENDPOINT = CONTAINED
```

No Program Map edge is emitted.

## 5. Contained — recurrence is provenance, not warrant

The same framework propositions recur across:

```text
README.md
docs/01_core_problem.md
docs/02_primitives.md
docs/03_control_loop.md
docs/04_divergence_dynamics.md
theory/primitives.md
theory/axioms.md
theory/equations.md
experiments/correction_loop_simulation.md
```

and Azus mappings recur in two distinct files.

All are retained as distinct source occurrences.

Nothing in the parse asserts that repeated authorial restatement creates independent empirical support.

```text
CROSS_FILE_RESTATEMENT_AS_INDEPENDENT_WARRANT = CONTAINED
SAME_EQUATION_RECURRENCE_AS_REPLICATION       = CONTAINED
```

Amendment 004 remains sufficient for later compression occurrence accounting.

## 6. Contained — formal variants remain variants

R19 contains source-local variants that must not be normalized away.

### Correction deficit / divergence input

Some surfaces use:

```text
delta = max(0, dOmega_nom/dt - C_cap)
```

while later/formal surfaces use:

```text
delta = max(0, dOmega_nom/dt - Theta*C_cap)
```

Both are parsed separately.

### Restoration threshold

`docs/04_divergence_dynamics.md` distinguishes:

```text
dR/dD > 0 = healthy
dR/dD = 0 = saturation, possibly recoverable
dR/dD < 0 = feedback inversion
```

while `theory/axioms.md` and `theory/equations.md` use:

```text
dR/dD <= 0 = collapse/failure condition
```

The parser does not choose a winner.

### Telemetry vector

`docs/05_azus_mapping.md` proposes:

```text
Psi(t) = [K_c, P_i, L, G_p, S_g]
```

while `examples/azus_mapping.md` proposes:

```text
Psi(t) = [K_c, P_i, L, Theta, eta_c]
```

Again, same symbol does not establish same object definition.

```text
FORMAL_VARIANT_AS_CANONICAL_EQUIVALENCE = CONTAINED
SAME_SYMBOL_AS_SAME_OBJECT               = CONTAINED
```

These are compression pressures, not parse failures.

## 7. Contained — correction-event criteria remain source-local

Different surfaces characterize valid correction through overlapping but non-identical criteria:

```text
external cause + mismatch + structural update + improved future adaptation
(E*, Delta, DeltaR, DeltaOmega)
external origin + structural modification + persistence + DeltaOmega>0
external origin + structural modification + persistence + survival of adaptive system
```

The final variant is explicitly retained as unresolved relative to the others in `R19U0050`.

```text
CORRECTION_EVENT_CRITERIA_VARIANT_AS_SILENT_IDENTITY = CONTAINED
```

## 8. Contained — unresolved is not failed

The 58 unresolved units include operationalization gaps, external endpoint ambiguity, symbol collisions, scale/metric gaps, protocol underspecification, and execution-provenance absence.

They are not represented as falsehoods, negative empirical results, or parser failures.

```text
UNRESOLVED_OPERATIONALIZATION_AS_PARSER_FAILURE = CONTAINED
PARSER_FAILURES = 0
```

## 9. Contained — source aperture and history

The frozen recursive head contains 14 blob paths:

```text
13 research Markdown paths = PARSE_INCLUDED
1 MIT LICENSE              = EXPLICITLY EXCLUDED LEGAL METADATA
0 unenumerated paths
```

The complete 23-commit lineage remains in `R19_SOURCE_SURFACE_V0.1.json` as developmental provenance. It is not admitted as extra current-head source content.

```text
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY = CONTAINED
LICENSE_OMISSION_AS_UNSEEN_PATH                = CONTAINED
```

## 10. Local repair required

The only demonstrated parse defect is the Part A count header.

The shallowest locus is:

```text
METADATA / CARDINALITY ACCOUNTING
```

not semantic unitization, source inventory, parser role, compression ontology, or scientific representation.

Required repair:

```text
R19_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001
Part A effective counts:
  parsed     90
  unresolved 16
  total      106
Whole parse effective counts:
  parsed     287
  unresolved 58
  total      345
```

No unit IDs, content, standing, locators, or source dispositions require change.

## 11. Verdict

```text
PARSE_REPAIR_REQUIRED                = YES_LOCAL_METADATA_ONLY
NEW_EPISTEMIC_DISTINCTION_REQUIRED  = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
BASE_PARSE_CONTRACT_AMENDMENT        = NOT_EARNED
AMENDMENT_005                        = NOT_EARNED
```

Until the local cardinality overlay is frozen and retested:

```text
R19_EXHAUSTIVE_PARSE_STATE = NOT_YET_EARNED
R19_COMPRESSION_ACCESS      = NOT_YET_OPENED
R20_PROGRAM_PARSE_ACCESS    = NOT_YET_OPENED
```

The death test therefore uses the count error as intended: a defect in accounting causes an accounting repair, not gratuitous ontology growth.
