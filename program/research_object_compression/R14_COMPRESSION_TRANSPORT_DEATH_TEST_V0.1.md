# R14 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression:** `R14_COMPRESSION_V0.1.json` + Amendments 001-002  
**Effective parse:** `R14_EXHAUSTIVE_PARSE_V0.1.json` + Amendments 001-002  
**Projection ledger:** `R14_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R14 tests whether the effective compression contract can preserve a multi-document theoretical and simulator-design repository containing recurrent formalism, unresolved source variants, pseudocode, prospective experiments, predictions, and project-status plurality without turning any of those into stronger standing.

## 1. Projection accounting

```text
R14_EFFECTIVE_PRIMARY_PARSE_UNITS = 133
R14_PRIMARY_PROJECTION_ENTRIES    = 133
R14_UNIQUE_PRIMARY_PARSE_IDS      = 133
R14_UNMAPPED_PARSE_UNITS          = 0
R14_DUPLICATE_PRIMARY_OWNERS      = 0
R14_SECONDARY_REPRESENTATIONS     = 23 parse units with declared secondary projections
R14_DERIVED_SECONDARY_VIEWS       = 5
```

Projection completeness passes.

## 2. Attack matrix

```text
FORMAL_VARIANT_CANONICALIZATION                = CONTAINED
SAME_SYMBOL_AS_SAME_DEFINITION                 = CONTAINED
SOURCE_VARIANT_AS_SUPERSESSION                 = CONTAINED
STATUS_RECONCILIATION                          = CONTAINED
DOCUMENT_PLAN_AS_OBSERVED_FILESYSTEM           = CONTAINED
PSEUDOCODE_AS_EXECUTABLE_IMPLEMENTATION        = CONTAINED
SIMULATOR_SPECIFICATION_AS_IMPLEMENTATION      = CONTAINED
SPECIFICATION_AS_EXECUTION                     = CONTAINED
HYPOTHESIS_RECURRENCE_AS_WARRANT               = CONTAINED
PREDICTION_AS_REPORTED_RESULT                  = CONTAINED
FALSIFICATION_AS_NEGATIVE_RESULT               = CONTAINED
CONDITIONAL_SUCCESS_RULE_AS_OBSERVED_RESULT    = CONTAINED
INTERNAL_CAUSAL_ARROW_AS_PROGRAM_MAP_EDGE      = CONTAINED
SOURCE_RELATION_DIRECTION_REVERSAL             = CONTAINED
SAME_METHOD_ROLE_AS_FORMAL_EQUIVALENCE         = CONTAINED
SOURCE_INVARIANT_LABEL_AS_THEOREM              = CONTAINED
FUTURE_EXTENSION_AS_CURRENT_V0_1               = CONTAINED
CURRENT_PERFORMANCE_AS_FUTURE_CAPACITY         = CONTAINED
AVAILABLE_MECHANISM_AS_SELECTED_MECHANISM      = CONTAINED
ACCESSIBILITY_AS_VIABILITY                     = CONTAINED
SECONDARY_REPRESENTATION_AS_WARRANT_MULTIPLICITY = CONTAINED
DERIVED_BOUNDED_ABSENCE_AS_SOURCE_ASSERTION    = CONTAINED
LOSS_BOUNDED_GROUPING_AS_SOURCE_ERASURE        = CONTAINED_ON_CURRENT_PROJECTION
```

No post-projection compression hit is found on the current bounded attacks.

## 3. Formal variants do not canonicalize themselves

The frozen source contains two environment-state forms:

```text
docs/simulator-spec.md + environment/README.md:
E_t=(R_t,C_t)

environment/design.md:
E_t=(R_t,C_t,N_t)
```

The effective compression preserves them as separate source-scoped objects:

```text
R14:DEF:ENVIRONMENT_VARIANT_RC
R14:DEF:ENVIRONMENT_VARIANT_RCN
```

with:

```text
CANONICALIZATION = NONE
SUPERSESSION      = NOT_ESTABLISHED
```

Thus:

\[
\boxed{
\text{same symbol}
\not\Rightarrow
\text{same formal definition}.
}
\]

```text
FORMAL_VARIANT_CANONICALIZATION = CONTAINED
SAME_SYMBOL_AS_SAME_DEFINITION  = CONTAINED
SOURCE_VARIANT_AS_SUPERSESSION  = CONTAINED
```

## 4. Methodological similarity does not establish formal equivalence

Most RAD surfaces express the intervention as:

```text
J(q,v,Omega) vs J(q,v)
```

while `environment/README.md` uses:

```text
J(G,Omega) vs J(G)
```

The repair preserves the latter as:

```text
R14:METHOD:UPDATE_RULE_VARIANT_G
```

and the cross-source comparison remains a zero-authority secondary view.

Therefore:

\[
\boxed{
\text{same experimental purpose}
\not\Rightarrow
\text{same formal argument structure}.
}
\]

```text
SAME_METHOD_ROLE_AS_FORMAL_EQUIVALENCE = CONTAINED
```

## 5. Source status remains source-scoped

R14 includes multiple project-status occurrences, including:

```text
Ontology defined; hypothesis unverified
simulator specification in progress
Specification defined; implementation pending
variables operationalized
```

The compression retains these statements without manufacturing one reconciled canonical project status.

```text
STATUS_RECONCILIATION = CONTAINED
```

Apparent documentary maturity, filename suffixes, or repeated wording do not establish temporal or authority precedence among these status statements.

## 6. Prose-described repository layouts do not overwrite the observed aperture

README, simulator-spec2, and environment/README describe current, minimal, or future repository layouts containing paths not present in the frozen head.

The compression preserves those descriptions as project/process metadata while the source surface separately records the actual 12-path frozen filesystem.

\[
\boxed{
\text{document-described structure}
\neq
\text{observed repository structure}.
}
\]

```text
DOCUMENT_PLAN_AS_OBSERVED_FILESYSTEM = CONTAINED
FUTURE_EXTENSION_AS_CURRENT_V0_1     = CONTAINED
```

## 7. Specification and pseudocode do not become execution history

`docs/simulator-spec.md` explicitly characterizes itself as a simulator specification with implementation pending. Markdown code-like blocks in the environment documents are preserved as illustrative examples.

The effective node therefore keeps:

```text
SIMULATOR_SPECIFICATION
ILLUSTRATIVE_PSEUDOCODE
EXECUTABLE_IMPLEMENTATION = NONE OBSERVED
EXECUTION_RECORD           = NONE OBSERVED
```

separate.

```text
PSEUDOCODE_AS_EXECUTABLE_IMPLEMENTATION   = CONTAINED
SIMULATOR_SPECIFICATION_AS_IMPLEMENTATION = CONTAINED
SPECIFICATION_AS_EXECUTION                = CONTAINED
```

R14 therefore complements R13:

\[
\boxed{
\text{execution specification}
\neq
\text{implementation}
\neq
\text{execution record}.
}
\]

## 8. Recurrent hypothesis does not become recurrent evidence

The central candidate relation:

\[
\Omega_t\rightarrow\Delta\mathcal G_{t+1}
\]

appears across multiple RAD documents and roles. The source repeatedly identifies it as an empirical hypothesis/question rather than an established result.

The compression groups those occurrences while preserving:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

where recurrence accounting applies.

```text
HYPOTHESIS_RECURRENCE_AS_WARRANT = CONTAINED
```

Repeated formulation is provenance, not replication.

## 9. Prediction, falsification and prospective evaluation remain non-results

The source predicts possible divergence such as:

```text
P_A approx P_B early
O_A > O_B later
R_A > R_B after novelty
possible P up while O down
```

and specifies falsification conditions. It also says, prospectively, that a successful minimal implementation would identify a measurable causal phenomenon while failure could leave the decomposition descriptive and weaken the hypothesis.

None is an observed outcome on the frozen surface.

```text
PREDICTION_AS_REPORTED_RESULT               = CONTAINED
FALSIFICATION_AS_NEGATIVE_RESULT            = CONTAINED
CONDITIONAL_SUCCESS_RULE_AS_OBSERVED_RESULT = CONTAINED
```

The bounded absence items remain:

```text
NO_REPORTED_EMPIRICAL_RESULT
NO_REPORTED_NEGATIVE_RESULT
NO_EXECUTABLE_IMPLEMENTATION
NO_EXECUTION_RECORD
```

## 10. Internal causal structure does not become program topology

RAD contains internal arrows such as:

\[
X\rightarrow F\rightarrow G\rightarrow\mathcal G
\]

and:

\[
\Omega\rightarrow M\rightarrow G\rightarrow F\rightarrow X.
\]

These are source-internal formal structures. They emit no Program Map edge and grant no cross-repository relation.

```text
INTERNAL_CAUSAL_ARROW_AS_PROGRAM_MAP_EDGE = CONTAINED
MAP_EDGE_EMISSION                         = NONE
```

## 11. Direction remains directional

The central empirical hypothesis is source-directional:

\[
\Omega_t\rightarrow\Delta\mathcal G_{t+1}.
\]

Nothing in the compression licenses the converse:

\[
\Delta\mathcal G_{t+1}\rightarrow\Omega_t.
\]

Nor does causal influence establish biconditionality, necessity, or sufficiency beyond what a source explicitly states.

```text
SOURCE_RELATION_DIRECTION_REVERSAL = CONTAINED
```

R12's directionality discipline therefore transports to R14 without a new rule.

## 12. Source invariant labels do not become theorem standing

Two sources use labels such as:

```text
Core Invariant
Final Invariant
```

for the recursive relation family. The compression preserves those labels as source characterization while withholding independently proved invariance/theorem standing.

```text
SOURCE_INVARIANT_LABEL_AS_THEOREM = CONTAINED
```

This is the same standing discipline previously applied to source labels such as `equivalent`, `necessary`, and `invariant`.

## 13. Adaptive state distinctions survive compression

The source explicitly separates:

```text
available mechanisms
selected mechanism
current performance
future adaptive capacity
```

and separately distinguishes accessibility from viability.

The compression maintains distinct objects for policy/state, accessibility, viability, performance/recovery/exploration, and openness.

```text
CURRENT_PERFORMANCE_AS_FUTURE_CAPACITY    = CONTAINED
AVAILABLE_MECHANISM_AS_SELECTED_MECHANISM = CONTAINED
ACCESSIBILITY_AS_VIABILITY                = CONTAINED
```

No scalar adaptive quantity is allowed to erase those source distinctions.

## 14. Secondary representations do not multiply warrant

The projection ledger assigns every effective parse unit exactly one primary owner. Twenty-three parse units also have explicit secondary representations because one source unit contributes lawfully to more than one compressed view.

Those secondary representations do not create new source occurrences or independent evidence.

\[
\boxed{
\text{secondary representation}
\neq
\text{new source}
\neq
\text{independent warrant}.
}
\]

```text
SECONDARY_REPRESENTATION_AS_WARRANT_MULTIPLICITY = CONTAINED
```

## 15. Derived bounded absences are not source assertions

The four bounded absence objects are derived from complete frozen source-surface and parse accounting:

```text
NO_REPORTED_EMPIRICAL_RESULT
NO_REPORTED_NEGATIVE_RESULT
NO_EXECUTABLE_IMPLEMENTATION
NO_EXECUTION_RECORD
```

No source sentence is fabricated saying these things. Their provenance is the complete admitted aperture plus parse ledger.

```text
DERIVED_BOUNDED_ABSENCE_AS_SOURCE_ASSERTION = CONTAINED
```

Thus:

\[
\boxed{
\text{source-bounded absence conclusion}
\neq
\text{source-authored assertion}.
}
\]

## 16. Loss-bounded grouping remains reversible

Some primary compressed objects intentionally group several source-local details rather than reproducing every equation or phrase verbatim. For example `R14:P:F1:CONSTRAINT_MODEL` contains both:

```text
Omega_t=f(X_t,E_t)
M_{t+1}=U(M_t,Omega_t)
```

while its primary compression emphasizes the consequence-signal object and its secondary projection records participation in the causal-chain representation.

This is accepted on the current bounded transport test because:

1. the exact parse unit remains immutable and source-reconstructible;
2. the compressed representations preserve its epistemic role and causal/model distinction;
3. no stronger conclusion is licensed by omitting the exact surface formula from the compressed payload;
4. the explicit projection ledger makes the grouping auditable and reopenable.

Likewise exact metric formulas remain preserved through dedicated metric-formula compression where the pre-projection test demonstrated that their omission was not safely loss-bounded.

Therefore the present distinction is:

\[
\boxed{
\text{compression need not duplicate every source token}
\quad\land\quad
\text{every omitted distinction must remain reconstructibly loss-bounded}.
}
\]

```text
LOSS_BOUNDED_GROUPING_AS_SOURCE_ERASURE = CONTAINED_ON_CURRENT_PROJECTION
```

This does not authorize arbitrary omission in later neurons.

## 17. Transportability result

R14 required:

```text
PARSE REPAIR 001: 18 mixed-role units -> 41 role-pure units
PARSE REPAIR 002: 12 residual mixed-role units -> 25 role-pure units
COMPRESSION REPAIR: 11 omitted source distinctions + 1 formal-variant view
```

All were minimal repairs using distinctions already earned by the effective contract.

No post-projection repair is required on the current attack suite.

```text
POST_PROJECTION_COMPRESSION_REPAIR = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED = NO
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005 = NOT_EARNED
```

Bounded result:

```text
EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R14_FROZEN_HEADS
```

This is not a universal transportability claim.

## 18. R14 verdict

```text
R14_SOURCE_SURFACE                  = FROZEN_FULL_RECURSIVE_HEAD
R14_TOTAL_FILE_PATHS                = 12
R14_RESEARCH_BEARING_PATHS          = 10
R14_UNIQUE_HEAD_BLOBS               = 12

R14_EFFECTIVE_PRIMARY_PARSE_UNITS   = 133
R14_DERIVED_AUDIT_VIEWS             = 4
R14_SOURCE_UNRESOLVED_UNITS         = 0
R14_PARSER_FAILURES                 = 0

R14_PRIMARY_PROJECTION_ENTRIES      = 133
R14_UNMAPPED_PARSE_UNITS            = 0
R14_DUPLICATE_PRIMARY_OWNERS        = 0
R14_DERIVED_SECONDARY_VIEWS         = 5

R14_REPORTED_EMPIRICAL_RESULT       = NONE_OBSERVED_ON_FROZEN_SURFACE
R14_REPORTED_NEGATIVE_RESULT        = NONE_OBSERVED_ON_FROZEN_SURFACE
R14_EXECUTABLE_IMPLEMENTATION       = NONE_OBSERVED_ON_FROZEN_SURFACE
R14_EXECUTION_RECORD                = NONE_OBSERVED_ON_FROZEN_SURFACE

R14_REUSABLE_NODE_STATE             = EARNED
R14_MAP_EDGE_EMISSION               = NONE
R14_MAP_AUTHORITY                   = NONE
R14_SCIENTIFIC_AUTHORITY            = NONE
PROPAGATE_KERNEL                    = NOT_EARNED
CEREBRO_STEP_2                      = CLOSED
AMENDMENT_005                       = NOT_EARNED
```

## 19. Sequential boundary

```text
R15_PROGRAM_PARSE_ACCESS = NEXT_AUTHORIZED_REPOSITORY
R16_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

This is procedural authorization only. It creates no R14 -> R15 semantic relation.

R14 therefore becomes a reusable neuron that can remember a designed causal experiment, unresolved formal variants, predictions, falsification criteria, and project plans without confusing any of them with implementation, execution, observed evidence, theorem standing, or graph authority.
