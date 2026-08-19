# R35 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/dostoevskian-cybernetics`  
**Frozen head:** `f4159b63d0dcdb748f4b9ce6009439103e9a2690`  
**Frozen root tree:** `69753e8f4bc2c3500b1213e788859bad6a3fb596`  
**Source surface:** 6 blobs = 5 admitted + 1 explicit scope exclusion  
**Candidate parse:** 98 units  
**Explicit unresolved:** 5  

## 1. Surface completeness attack

Immutable recursive tree returned `truncated=false` and exactly six blobs. Every blob has a frozen disposition. `.gitignore` is explicitly excluded as repository-hygiene metadata; all five research Markdown files are represented.

```text
UNENUMERATED_PATHS = 0
ADMITTED_PATHS_WITHOUT_PARSE_UNIT = 0
PARSER_FAILURES = 0
```

**PASS.**

## 2. Proposed-framework / implementation leakage attack

The README describes `experiments/` and `results/` subtrees, but the frozen tree contains neither. No source code, experiment logs, benchmark result files, workflow source, or test source exists at the frozen head.

```text
README_DESCRIBED_STRUCTURE != PERSISTED_TREE
PROPOSED_CFAE != IMPLEMENTED_CFAE
PROPOSED_BENCHMARK != EXECUTED_BENCHMARK
METRIC_DEFINITION != MEASURED_RESULT
```

R35P0093 preserves the conflict with tree authority for persisted-state claims.

**PASS.**

## 3. Execution-lineage attack

Queried frozen-head GitHub surfaces expose zero PR-triggered workflow-run witnesses and zero combined-status records. The root tree contains no `.github/workflows` subtree.

```text
ALGORITHM_DESCRIPTION != EXECUTABLE_IMPLEMENTATION
NO_WORKFLOW_SOURCE != HISTORICAL_NONEXECUTION_PROOF
NO_RESULT_PATHS_AT_HEAD != CLAIM_THAT_NO_OFFREPO_RUN_EVER_OCCURRED
```

The parse makes only frozen-repository claims.

**PASS.**

## 4. Research-status attack

`README.md` explicitly calls the object a proposed framework and experimental program; `OPEN_QUESTIONS.md` explicitly states that fundamental questions remain unresolved.

The parse does not promote:

- CFAE into a demonstrated mechanism;
- Factored Shock Benchmark into executed evidence;
- Level-4 restructuring into demonstrated representation invention;
- interface expansion into a demonstrated capability;
- multi-agent provenance sharing into an implemented protocol;
- explicit attribution into comparative superiority.

**PASS.**

## 5. Metric-validation attack

`A_epistemic`, `C_improve`, `K_retain`, `A_local`, and the optional composite score are preserved as proposed metrics only.

```text
FORMULA != IDENTIFIED_CONSTRUCT
DEFINITION != ESTIMATOR_VALIDATION
OPTIONAL_SCORE != NATURAL_SCALAR_OF_ADAPTIVE_INTELLIGENCE
```

The source itself states that no single scalar fully captures adaptive intelligence and requires individual metrics to remain visible.

**PASS.**

## 6. Performance-recovery sign attack

Source formula:

```text
ΔP_future = integral(R_agent - R_preference) dt
```

with `R_preference` described as target performance under the new environment. Surrounding prose treats `ΔP_future` as recovery/capability gained. The source does not specify whether a non-positive deficit convention, sign inversion, baseline shift, or another normalization is intended.

```text
R35P0094 = UNRESOLVED
```

No silent sign flip is allowed.

**PASS BY PRESERVED UNRESOLUTION.**

## 7. Failure-depth uniqueness attack

README Level 1 includes corrupted sensory mapping / observation-model adjustment, while THEORY Level 3 lists changed observation mapping as a mechanism failure.

The source does not state a criterion deciding whether an observation-mapping change is Level 1 or Level 3.

```text
R35P0095 = UNRESOLVED
```

No forced localization is allowed.

**PASS BY PRESERVED UNRESOLUTION.**

## 8. Identifiability-equivalence attack

Two formal objects appear:

```text
L = L_hat ∘ O
```

and:

```text
max_a I(H;O|a) > 0
```

The first is target-relative factorization through an observation interface; the second is action-conditioned discrimination among hypotheses. The repository does not establish their equivalence or sufficient conditions linking them.

```text
R35P0096 = UNRESOLVED
```

**PASS BY PRESERVED UNRESOLUTION.**

## 9. Transition-state observability attack

THEORY states that world state is mediated through an interface, while CFAE computes transition residual directly from `s_{t+1}`. The source does not state whether this state is observed, inferred, privileged evaluator state, or latent.

```text
R35P0097 = UNRESOLVED
```

The parse therefore does not claim that CFAE is operationally implementable from the declared observation interface.

**PASS BY PRESERVED UNRESOLUTION.**

## 10. Correct-abstention metric boundary attack

Correct abstention is rewarded when no structural revision is justified, but `C_improve` divides by structural-change magnitude. A justified zero-revision case can therefore produce a zero denominator; no convention is specified.

```text
R35P0098 = UNRESOLVED
```

No epsilon smoothing, case exclusion, or alternate score is invented.

**PASS BY PRESERVED UNRESOLUTION.**

## 11. Attribution-ground-truth attack

`A_epistemic` assumes a notion of correct causal attribution. The proposed synthetic benchmark can in principle author such labels, but the repository contains no executed benchmark and no general external attribution oracle.

The parse does not convert benchmark-author labels into a validated real-world causal-attribution procedure.

**PASS.**

## 12. Open-question inversion attack

Every OPEN_QUESTIONS item remains future work. In particular:

```text
CURRENT_FACTORIZATION != AUTONOMOUS_CAUSAL_DECOMPOSITION
EPISTEMIC_HALT != INTERFACE_INVENTION
EXPLICIT_ATTRIBUTION_HYPOTHESIS != COMPARATIVE_ADVANTAGE
DYNAMIC_LAMBDA_PREDICTION != LEARNED_REVISION_POLICY
MULTI_AGENT_PROPOSAL != AUTHORITY-SAFE_COMMUNICATION
```

**PASS.**

## 13. Title/literary-authority attack

The repository title uses “Dostoevskian,” but the frozen research surface contains no literary corpus analysis, textual evidence, or empirical claim about Dostoevsky. No literary interpretation is manufactured from the title.

**PASS.**

## 14. Chronology attack

The returned repository history contains seven commits from initial commit through `OPEN_QUESTIONS.md`. Chronology supports developmental provenance only.

```text
COMMIT_ORDER != SEMANTIC_EDGE
COMMIT_ORDER != CAUSAL_VALIDATION
```

**PASS.**

## 15. Final parse verdict

```text
R35_TOTAL_BLOB_PATHS                  = 6
R35_ADMITTED_SOURCE_PATHS             = 5
R35_SCOPE_EXCLUDED_PATHS              = 1
R35_UNENUMERATED_PATHS                = 0
R35_EFFECTIVE_PARSE_UNITS             = 98
R35_REPRESENTED_PARSE_UNITS           = 98
R35_EXPLICIT_UNRESOLVED_UNITS         = 5
R35_PARSER_FAILURES                   = 0
R35_ADMITTED_PATHS_WITHOUT_PARSE_UNIT = 0
R35_PARSE_REPAIR                      = NONE
R35_EXHAUSTIVE_PARSE_STATE            = FROZEN
```

The five unresolved units are required preservation objects, not parse failures.

**DEATH TEST: PASS.**

Map authority remains `NONE`; scientific authority remains `NONE`; propagation remains `NO`.