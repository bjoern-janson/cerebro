# R10 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R10_COMPRESSION_V0.1.json` plus conformance overlays 001-004  
**Parse:** `R10_EXHAUSTIVE_PARSE_V0.1.json`  
**Projection ledger:** `R10_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json` plus Amendment 001  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R10 is the first held-out repository in this sequence to combine, on one frozen head:

- explicit theory/axioms/equations;
- roadmap and open-problem status;
- experimental specifications;
- synthetic numeric output examples;
- source-labeled qualitative `Result` / `Current Findings` analyses;
- `.py` files that are Markdown-fenced as stored;
- ordinary Python proxy components;
- hard-coded toy metric values;
- an intended but interface-inconsistent environmental benchmark;
- a source-internal disagreement about scalar ranking;
- a source-internal disagreement about what `CGET` expands to.

The test asks whether the accumulated compression contract can preserve all of those distinctions without adding a new epistemic role.

## 1. Projection accounting

```text
R10_EFFECTIVE_PARSE_UNITS          = 251
R10_PRIMARY_PROJECTION_ENTRIES     = 251
R10_UNMAPPED_PARSE_UNITS           = 0
R10_DUPLICATE_PRIMARY_OWNERS       = 0
R10_SECONDARY_VIEWS                = 5
R10_DERIVED_BOUNDED_ABSENCES       = 2
```

Secondary views are explicitly reference-only / typed-secondary objects with:

```text
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

Projection completeness passes.

## 2. Attack matrix

```text
QUALITATIVE_INITIAL_ANALYSIS_AS_MEASURED_RESULT        = CONTAINED
NO_MEASURED_RESULT_AS_ERASURE_OF_QUALITATIVE_ANALYSIS = CONTAINED
SYNTHETIC_OUTPUT_AS_QUALITATIVE_FINDING                = CONTAINED
RESULT_FILENAME_AS_RESULT_STANDING                     = CONTAINED

PYTHON_EXTENSION_AS_EXECUTABILITY                      = CONTAINED
FENCED_CODE_AS_EXECUTED_IMPLEMENTATION                 = CONTAINED
ORDINARY_COMPONENT_AS_INTEGRATED_BENCHMARK             = CONTAINED
SYNTHETIC_CALCULATOR_AS_ENVIRONMENTAL_EXPERIMENT       = CONTAINED
HARDCODED_PROXY_AS_MEASUREMENT                         = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_METRIC                  = CONTAINED
IMPLEMENTED_OUTPUT_AS_OBSERVATION                      = CONTAINED

AXIOM_AS_TRUTH                                         = CONTAINED
EQUATION_AS_PROOF                                      = CONTAINED
ROADMAP_COMPLETION_AS_VALIDATION                       = CONTAINED
CASE_STUDY_AS_EVIDENCE                                 = CONTAINED
PREDICTION_AS_SUPPORT                                  = CONTAINED
METHOD_AS_EVIDENCE                                     = CONTAINED

CGET_NAME_VARIANT_AS_CANONICALIZATION                  = CONTAINED
SCALAR_RANKING_AS_RECONCILIATION                       = CONTAINED
SECONDARY_TENSION_AS_SECOND_WARRANT                    = CONTAINED
EXISTING_WORK_REFERENCE_AS_PROGRAM_MAP_EDGE            = CONTAINED
SOURCE_OCCURRENCE_MULTIPLICITY_AS_CORROBORATION        = CONTAINED
```

## 3. Qualitative analysis vs measured result

R10 contains two distinct result-shaped source classes.

### A. Synthetic example output

`experiments/results/example_run.md` states explicitly that its numbers are synthetic examples and not experimental results.

Effective compression destination:

```text
R10:EXAMPLE:SYNTHETIC_OUTPUT
standing = APPLICATION_OR_EXAMPLE / SYNTHETIC_OUTPUT_EXAMPLE
```

### B. Source-labeled qualitative initial analysis

`tools/experiments/test_results.md` uses:

```text
Experimental Test Results
Result:
CGET Classification
Current Findings
```

but also labels the relevant cases `Initial Analysis`, supplies qualitative retrospective reasoning rather than instrument output, and contains no run metadata, raw measurements, logs, seeds or analyzer report provenance.

Effective destination:

```text
R10:RESULT:QUALITATIVE_INITIAL_ANALYSIS
standing = SOURCE_INTERPRETATION
source_standing = SOURCE_LABELED_INITIAL_ANALYSIS_OR_QUALITATIVE_FINDINGS
```

The source label is preserved without being treated as a measured execution result.

Therefore both can coexist with:

```text
R10:STATUS:NO_MEASURED_RESULT
standing = SOURCE_BOUNDED_ABSENCE
```

because the three statements concern different properties:

\[
\boxed{
\text{synthetic report example}
\neq
\text{qualitative source-labeled analysis}
\neq
\text{measured execution result}.
}
\]

```text
QUALITATIVE_INITIAL_ANALYSIS_AS_MEASURED_RESULT        = CONTAINED
NO_MEASURED_RESULT_AS_ERASURE_OF_QUALITATIVE_ANALYSIS = CONTAINED
SYNTHETIC_OUTPUT_AS_QUALITATIVE_FINDING                = CONTAINED
RESULT_FILENAME_AS_RESULT_STANDING                     = CONTAINED
```

This is a positive R10 transport result. No new result ontology is required.

## 4. Implementation ladder

The effective node preserves separately:

```text
ARTIFACT_CONTENT_STATE
EXECUTABLE_IMPLEMENTATION
INTENDED_IMPLEMENTATION_IF_FENCES_REMOVED
IMPLEMENTATION_ASSUMPTION
IMPLEMENTED_OUTPUT_BEHAVIOR
SOURCE_DESCRIBED_INTEGRATION_STATUS
EXECUTION_RECORD
MEASURED_OBSERVATION
```

The frozen source supports:

```text
ordinary Python component blobs                   = 3
Markdown-fenced .py blobs                          = 7
synthetic calculator over hard-coded toy inputs    = PRESENT
integrated environmental benchmark                 = NOT_ESTABLISHED
execution record                                   = NONE_OBSERVED
measured benchmark observation                     = NONE_OBSERVED
```

`experiments/run_all_agents.py` is fenced as stored and also calls APIs not supplied by the frozen MazeWorld/agent interfaces.

The ordinary analyzer modules can calculate scores from manually assigned toy fields, but those fields are construction inputs rather than observations.

Thus:

\[
\boxed{
\text{code present}
\neq
\text{component executable}
\neq
\text{integrated instrument}
\neq
\text{executed instrument}
\neq
\text{measured result}.
}
\]

```text
PYTHON_EXTENSION_AS_EXECUTABILITY                = CONTAINED
FENCED_CODE_AS_EXECUTED_IMPLEMENTATION           = CONTAINED
ORDINARY_COMPONENT_AS_INTEGRATED_BENCHMARK       = CONTAINED
SYNTHETIC_CALCULATOR_AS_ENVIRONMENTAL_EXPERIMENT = CONTAINED
HARDCODED_PROXY_AS_MEASUREMENT                   = CONTAINED
IMPLEMENTED_PROXY_AS_VALIDATED_METRIC            = CONTAINED
IMPLEMENTED_OUTPUT_AS_OBSERVATION                = CONTAINED
```

## 5. Theory / proof / evidence standing

The node preserves source-local assumptions, axioms, definitions, formal structures, hypotheses, predictions and methodologies independently.

The source itself states:

- axioms do not yet constitute a complete mathematical theory;
- equations are not assumed proven;
- empirical validation remains open;
- predictions/falsifiers are future-facing;
- examples are not intended to prove the framework.

Accordingly:

```text
AXIOM_AS_TRUTH                   = CONTAINED
EQUATION_AS_PROOF                = CONTAINED
ROADMAP_COMPLETION_AS_VALIDATION = CONTAINED
CASE_STUDY_AS_EVIDENCE           = CONTAINED
PREDICTION_AS_SUPPORT            = CONTAINED
METHOD_AS_EVIDENCE               = CONTAINED
```

## 6. Source identity disagreement

Primary source occurrences preserve file-local acronym expansions as source status.

The cross-source comparison exists only as secondary view:

```text
R10:TENSION:NAME
```

with no canonicalization authority.

Therefore:

```text
CGET_NAME_VARIANT_AS_CANONICALIZATION = CONTAINED
```

The node remembers that the repository disagrees with itself about its expanded name.

It does not repair the disagreement.

## 7. Scalar-ranking disagreement

Primary source units preserve:

- documentation specifying structural/lexicographic evaluation rather than one intelligence score;
- implementation assumption in `run_benchmark.py` ranking synthetic agents by `Theta*`;
- source-status acknowledgement that future versions may replace scalar ranking.

`R10:TENSION:SCALAR` is a secondary comparison view only.

```text
SCALAR_RANKING_AS_RECONCILIATION = CONTAINED
SECONDARY_TENSION_AS_SECOND_WARRANT = CONTAINED
```

The network-ready neuron therefore remembers disagreement without turning disagreement resolution into a hidden projection side effect.

## 8. Existing-work references

Conceptual relationships to information theory, causal inference, RL, control/viability, active inference, alignment, thermodynamics and AGI remain source-side reference/assertion material.

```text
EXISTING_WORK_REFERENCE_AS_PROGRAM_MAP_EDGE = CONTAINED
MAP_EDGE_EMISSION = NONE
```

No external literature endpoint is resolved and no cross-repository edge is generated.

## 9. Occurrence multiplicity

Many core CGET ideas recur across README, docs, theory, experiments and tools.

The effective primary ledger preserves each source occurrence while Amendment 004 remains in force:

```text
SOURCE_OCCURRENCE_COUNT = reconstructible
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

No repetition across files is counted as independent confirmation.

```text
SOURCE_OCCURRENCE_MULTIPLICITY_AS_CORROBORATION = CONTAINED
```

## 10. R10-specific transport result

R10 demonstrates that the accumulated contract can distinguish, on one repository head:

\[
\boxed{
\begin{aligned}
&\text{theoretical definition}\
&\neq \text{assumption/axiom}\
&\neq \text{prediction}\
&\neq \text{experimental protocol}\
&\neq \text{synthetic result-shaped example}\
&\neq \text{qualitative source-labeled analysis}\
&\neq \text{implementation}\
&\neq \text{synthetic executable calculator}\
&\neq \text{integrated instrument}\
&\neq \text{execution record}\
&\neq \text{measured observation}.
\end{aligned}
}
\]

No new global role or top-level coordinate is required.

## 11. Bounded transportability

R10 required no post-death-test repair.

The only pre-test overlays were conformance to already-earned requirements from the effective R01-R09 contract:

- standing-pure local purpose/identity/example destinations;
- Amendment 003 methodology coordinate and secondary-reuse accounting;
- artifact-state / implementation-standing separation;
- secondary rather than primary tension views.

These are not new R10 anatomical growth.

Therefore:

```text
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005                        = NOT_EARNED
POST_DEATH_TEST_REPAIR               = NONE
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R10_FROZEN_HEADS
```

This is not universal transportability.

## 12. Final R10 verdict

```text
R10_SOURCE_SURFACE                  = FROZEN_FULL_RECURSIVE_HEAD
R10_TOTAL_BLOB_PATHS                = 43
R10_RESEARCH_BEARING_BLOB_PATHS     = 41
R10_UNIQUE_RESEARCH_BLOBS           = 41
R10_MARKDOWN_PATHS                  = 31
R10_PYTHON_PATHS                    = 10

R10_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS = 251
R10_PARSED_UNITS                     = 251
R10_UNRESOLVED_UNITS                 = 0
R10_PARSER_FAILURES                  = 0

R10_PRIMARY_PROJECTION_ENTRIES       = 251
R10_UNMAPPED_PARSE_UNITS             = 0
R10_DUPLICATE_PRIMARY_OWNERS         = 0

R10_MEASURED_EXECUTION_RESULTS       = NONE_OBSERVED_ON_FROZEN_SOURCE_SURFACE
R10_SOURCE_LABELED_QUALITATIVE_ANALYSES = PRESENT
R10_SYNTHETIC_OUTPUT_EXAMPLES        = PRESENT
R10_EXECUTION_RECORDS                = NONE_OBSERVED_ON_FROZEN_SOURCE_SURFACE

R10_REUSABLE_NODE_STATE              = EARNED
R10_MAP_EDGE_EMISSION                = NONE
R10_MAP_AUTHORITY                    = NONE
R10_SCIENTIFIC_AUTHORITY             = NONE
PROPAGATE_KERNEL                     = NOT_EARNED
CEREBRO_STEP_2                       = CLOSED
AMENDMENT_005                        = NOT_EARNED
```

## 13. Sequential boundary

```text
R11_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R12_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This is procedural authorization only.

It creates no R10 -> R11 semantic relation.

The tenth neuron can now be retained as an internally standing-preserving research object without treating code proximity, result-shaped filenames, qualitative classifications, or synthetic scores as scientific evidence.
