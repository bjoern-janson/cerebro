# R10 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Parse candidate:** `R10_EXHAUSTIVE_PARSE_V0.1.json`  
**Source surface:** `R10_SOURCE_SURFACE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The test attacks whether R10's 251-unit parse preserves source-relative epistemic role across theory, roadmap/status prose, synthetic examples, qualitative analyses, benchmark specifications, fenced pseudo-Python artifacts and ordinary Python components.

## Attack matrix

```text
AXIOM_AS_ESTABLISHED_TRUTH                         = CONTAINED
FORMAL_EQUATION_AS_PROVEN_THEOREM                  = CONTAINED
FRAMEWORK_DEFINITION_AS_EMPIRICAL_PROPERTY         = CONTAINED
PREDICTION_AS_EVIDENCE                             = CONTAINED
CASE_STUDY_AS_VALIDATION                           = CONTAINED
ROADMAP_COMPLETION_AS_SCIENTIFIC_VALIDATION        = CONTAINED
RESULTS_PATH_AS_EXECUTION_RECORD                    = CONTAINED
SYNTHETIC_NUMERIC_TABLE_AS_OBSERVATION             = CONTAINED
SOURCE_LABEL_RESULT_AS_MEASURED_RESULT              = CONTAINED
INITIAL_ANALYSIS_AS_INSTRUMENT_VALIDATION           = CONTAINED
PYTHON_EXTENSION_AS_EXECUTABLE_BLOB                 = CONTAINED
EXECUTABLE_COMPONENT_AS_INTEGRATED_INSTRUMENT       = CONTAINED
HARDCODED_METRIC_AS_MEASUREMENT                     = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_METRIC               = CONTAINED
IMPLEMENTED_OUTPUT_BEHAVIOR_AS_EXECUTION            = CONTAINED
SOURCE_RELATION_TO_EXISTING_WORK_AS_PROGRAM_MAP_EDGE= CONTAINED
CGET_NAME_VARIANT_AS_CANONICAL_IDENTITY             = CONTAINED
SCALAR_RANKING_AS_FRAMEWORK_RECONCILIATION          = CONTAINED
RESEARCH_DIRECTION_AS_NEW_AUTHORITY_CLASS            = CONTAINED
SOURCE_STATUS_TABLE_AS_SUBSTANTIVE_RESULT           = CONTAINED
```

## 1. Theory standing

The parse keeps separate:

```text
SOURCE_ASSERTION_ASSUMPTION
SOURCE_ASSERTION_HYPOTHESIS
SOURCE_PREDICTION
DEFINITION / DEFINITION_DICTIONARY
FORMAL_STRUCTURE
METHODOLOGY_OR_TEST_PROTOCOL
SOURCE_INTERPRETATION
SOURCE_DESCRIBED_STATUS
```

The source itself supplies the hostile fixtures:

- `theory/assumptions.md` calls its contents assumptions and potential falsification points;
- `theory/axioms.md` says its axioms do not yet constitute a complete mathematical theory;
- `theory/equations.md` says its equations are proposed vocabulary and are not assumed proven;
- `docs/12_open_problems.md` explicitly keeps formalization, measurement, validation and AGI sufficiency open.

Therefore:

```text
AXIOM_AS_ESTABLISHED_TRUTH = CONTAINED
FORMAL_EQUATION_AS_PROVEN_THEOREM = CONTAINED
FRAMEWORK_DEFINITION_AS_EMPIRICAL_PROPERTY = CONTAINED
```

## 2. Prediction/example standing

Predictions, expected baseline profiles, benchmark progression tables and historical case studies remain predictions/examples/interpretations.

`docs/11_examples_and_case_studies.md` explicitly says retrospective examples are not intended to prove CGET.

```text
PREDICTION_AS_EVIDENCE = CONTAINED
CASE_STUDY_AS_VALIDATION = CONTAINED
```

## 3. Roadmap standing

`ROADMAP.md` marks Phase 0 formal foundation completed while simultaneously stating repository stage:

```text
Theoretical framework + toy benchmark specification
```

and next milestone:

```text
Run experiments and replace conceptual metrics with measured quantities.
```

The parse preserves both.

```text
ROADMAP_COMPLETION_AS_SCIENTIFIC_VALIDATION = CONTAINED
```

`SOURCE_DESCRIBED_RESEARCH_DIRECTION` is treated only as an organizational subrole of source status/open questions. It grants no new scientific standing and no roadmap authority.

```text
RESEARCH_DIRECTION_AS_NEW_AUTHORITY_CLASS = CONTAINED
NEW_GLOBAL_PARSER_ROLE_REQUIRED = NO
```

## 4. Synthetic result-shaped artifact

`experiments/results/example_run.md` explicitly states:

```text
values = synthetic examples
experimental results = NO
```

The parse stores numeric tables as `APPLICATION_OR_EXAMPLE` with synthetic-output standing and preserves the disclaimer/status.

```text
RESULTS_PATH_AS_EXECUTION_RECORD = CONTAINED
SYNTHETIC_NUMERIC_TABLE_AS_OBSERVATION = CONTAINED
```

## 5. Source-labeled qualitative results

`tools/experiments/test_results.md` is more adversarial because it uses:

```text
Experimental Test Results
Result:
Current Findings
CGET Classification
```

while its own status table labels the historical cases `Initial Analysis` and supplies no run metadata, raw observations, seeds, logs or analyzer output.

The parse therefore preserves both dimensions:

```text
SOURCE_LABEL = Result / Finding / Classification
SOURCE_STANDING = Initial Analysis / qualitative interpretation
EXECUTION_PROVENANCE = NONE_OBSERVED
```

For the brute-force -> learned-representation case, the same file's status table says `Initial Analysis` while the body contains only expected signature/failure conditions. Both occurrences survive independently rather than being reconciled.

Thus:

```text
SOURCE_LABEL_RESULT_AS_MEASURED_RESULT = CONTAINED
INITIAL_ANALYSIS_AS_INSTRUMENT_VALIDATION = CONTAINED
SOURCE_STATUS_TABLE_AS_SUBSTANTIVE_RESULT = CONTAINED
```

This establishes the bounded distinction:

\[
\boxed{
\text{source-reported qualitative analysis result}
\neq
\text{measured execution result}.
}
\]

## 6. Python-extension attack

Seven `.py` paths are literally stored with Markdown triple-backtick fences surrounding the Python text.

The parse records this as artifact content state rather than silently stripping the fences.

Three analyzer components are ordinary Python source:

```text
tools/cget_analyzer/cget_metrics.py
tools/cget_analyzer/experiments.py
tools/cget_analyzer/toy_agents.py
```

Therefore:

```text
PYTHON_EXTENSION_AS_EXECUTABLE_BLOB = CONTAINED
```

## 7. Component-vs-integration attack

Ordinary analyzer modules can form a synthetic arithmetic pipeline over hard-coded toy-agent fields.

That does not establish the repository's intended environmental benchmark as integrated/runnable:

- `experiments/run_all_agents.py` is fenced as stored;
- even after hypothetical fence removal it calls interfaces absent or incompatible with frozen `MazeWorld` and agent classes;
- `tools/cget_analyzer/run_benchmark.py` is itself fenced as stored.

The parse therefore keeps:

```text
COMPONENT_CODE_PRESENT = YES
SYNTHETIC_CALCULATOR_PRESENT = YES
INTEGRATED_ENVIRONMENTAL_BENCHMARK = NOT_ESTABLISHED
EXECUTION_RECORD = NONE
```

```text
EXECUTABLE_COMPONENT_AS_INTEGRATED_INSTRUMENT = CONTAINED
```

## 8. Hard-coded proxy attack

Several source artifacts produce measurement-looking quantities from programmed constants:

- CGET toy agent hard-codes `.75/.80/.85/.70/1.0` structural metrics;
- shortest-path and random baselines hard-code CGET interpretation metrics;
- analyzer toy agents hard-code complexity, intervention, composition, reachability and identity inputs;
- analyzer arithmetic functions then calculate scores from those programmed values.

The parse separates:

```text
IMPLEMENTATION_ASSUMPTION
EXECUTABLE_IMPLEMENTATION
IMPLEMENTED_OUTPUT_BEHAVIOR
```

and admits no measured result.

```text
HARDCODED_METRIC_AS_MEASUREMENT = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_METRIC = CONTAINED
IMPLEMENTED_OUTPUT_BEHAVIOR_AS_EXECUTION = CONTAINED
```

## 9. Existing-work relation attack

`docs/10_relationship_to_existing_work.md` asserts conceptual relationships with multiple external fields.

The parse preserves those as source interpretations/references only.

```text
SOURCE_RELATION_TO_EXISTING_WORK_AS_PROGRAM_MAP_EDGE = CONTAINED
MAP_EDGE_EMISSION = NONE
```

## 10. CGET identity-name attack

The source expands the acronym differently:

```text
Causal Generative Equilibrium Theory
Causal Generative Execution Theory
Causal Generative Executable Theory
```

The parse preserves the variation as an unresolved source-identity tension.

```text
CGET_NAME_VARIANT_AS_CANONICAL_IDENTITY = CONTAINED
CANONICALIZATION_AUTHORITY = NONE
```

## 11. Scalar-ranking tension

Documentation says the analyzer does not assign a single intelligence score and benchmark design prefers lexicographic constraints.

`run_benchmark.py` nevertheless intends to rank toy agents by `Theta*` and explicitly notes that a future version may replace this scalar ranking.

The parse stores both branches without choosing one.

```text
SCALAR_RANKING_AS_FRAMEWORK_RECONCILIATION = CONTAINED
RECONCILIATION_AUTHORITY = NONE
```

## 12. Parse accounting

```text
R10_RESEARCH_BEARING_SOURCE_PATHS = 41
R10_PARSE_UNITS                   = 251
R10_PARSED_UNITS                  = 251
R10_UNRESOLVED_UNITS              = 0
R10_PARSER_FAILURES               = 0
R10_UNACCOUNTED_SOURCE_PATHS      = 0
```

## 13. Verdict

No attack demonstrates a missing parser distinction requiring contract growth.

```text
R10_PARSE_DEATH_TEST                    = PASS_ON_CURRENT_BOUNDED_ATTACKS
NEW_GLOBAL_PARSER_ROLE                  = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE    = NONE
AMENDMENT_005                           = NOT_EARNED
MAP_EDGE                                = NONE
PROPAGATION                             = NONE
CEREBRO_STEP_2                          = CLOSED
```

The parse may proceed to compression.

The strongest R10 compression pressure is now not source coverage. It is whether projection can preserve the hierarchy:

```text
THEORY/SPECIFICATION
!= IMPLEMENTED PROXY
!= SYNTHETIC CALCULATOR
!= INTEGRATED BENCHMARK
!= EXECUTION RECORD
!= MEASURED OBSERVATION
```

without collapsing source-labeled qualitative analyses into either pure examples or measured results.
