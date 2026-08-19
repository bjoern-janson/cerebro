# R36 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Repository:** `bjoern-janson/controlled-adaptation-thesis`  
**Frozen head:** `040113221b04ccc86e74e568b769b7927ff9a376`  
**Frozen root tree:** `a1a77bdc3ef16f602a82fff608b1d2d26a1e3637`  
**Effective candidate parse:** 139 units = 135 represented + 4 explicitly unresolved  
**Admitted source paths:** 10/10  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Mechanical closure

```text
TOTAL_BLOB_PATHS                  = 11
ADMITTED_SOURCE_PATHS             = 10
SCOPE_EXCLUDED_PATHS              = 1
UNENUMERATED_PATHS                = 0
EFFECTIVE_PARSE_UNITS             = 139
PARSED_REPRESENTATIONS            = 135
EXPLICITLY_UNRESOLVED             = 4
PARSER_FAILURES                   = 0
ADMITTED_PATHS_WITHOUT_UNIT       = 0
DUPLICATE_UNIT_IDS                = 0
UNIT_ID_RANGE                     = R36P0001-R36P0139
```

## 2. Freeze-boundary attack

`FREEZE.md` declares v1.0 frozen at `91ffe403879607d40a5e9c8babed1c5016ba0eba`, with four core files:

- `THESIS.md`
- `docs/ARCHITECTURE.md`
- `docs/GOVERNANCE.md`
- `docs/BENCHMARK.md`

Independent Git comparison from the declared freeze commit to the frozen R36 head shows exactly one later commit and only these changed paths:

```text
.github/pull_request_template.md
FREEZE.md
LINEAGE.md
README.md
STATUS.md
```

No frozen core path changed.

```text
DECLARED_FROZEN_CORE = VERIFIED_UNCHANGED_TO_R36_HEAD
FROZEN_CORE != POST_FREEZE_METADATA
POST_FREEZE_METADATA != RETROACTIVE_CORE_REVISION
```

## 3. Candidate-theory / empirical-result attack

The core explicitly describes itself as a coherent candidate architecture and explicitly denies empirical validation.

```text
CANDIDATE_THEORY_AS_VALIDATED_THEORY                    = CONTAINED
CAUSAL_ARCHITECTURE_PROPOSAL_AS_CAUSAL_IDENTIFICATION  = CONTAINED
PREDICTED_LAYER_INTERVENTION_AS_DEMONSTRATED_MECHANISM = CONTAINED
HELD_OUT_CONSEQUENCE_RULE_AS_OBSERVED_HELD_OUT_RESULT   = CONTAINED
EMPIRICAL_PREDICTION_AS_REPORTED_RESULT                 = CONTAINED
```

No source file reports an executed architecture comparison.

## 4. Benchmark standing attack

`docs/BENCHMARK.md` is part of the frozen v1.0 core and contains a benchmark concept/protocol. Post-freeze lineage metadata separately names a `Constitutional Continual Adaptation Benchmark v0.1` frozen evaluation protocol/preregistration.

These are not silently collapsed.

```text
FROZEN_CORE_BENCHMARK_CONCEPT
!= SOURCE_REPORTED_EXTERNAL_BENCHMARK_V0_1_PREREGISTRATION
!= BENCHMARK_IMPLEMENTATION
!= BENCHMARK_EXECUTION
!= BENCHMARK_RESULT
```

The repository contains no implementation, test suite, dataset, benchmark-validity result set, or result artifact.

## 5. External-lineage attack

R36 names external or successor objects but does not contain their primary artifacts:

```text
R36P0118  Causal Mass
R36P0120  Consequence-to-Authority Bridge v0.1
R36P0123  Benchmark v0.1 preregistration artifact
R36P0126  self-governance event primary record
```

They remain explicitly unresolved at the primary-artifact level.

```text
SOURCE_REPORTED_LINEAGE != ENDPOINT_IDENTITY
SOURCE_REPORTED_SHA256 != LOCAL_PRIMARY_ARTIFACT_VERIFICATION
SOURCE_REPORTED_RESULT != INSPECTED_EXECUTION_RECORD
CONCEPTUAL_ANCESTRY != AUTHORITY_INHERITANCE
```

No external primary object is imported into R36 by reference.

## 6. Authority-type attack

The core distinguishes epistemic, operational, and context-dependent arbitration authority.

```text
EPISTEMIC_AUTHORITY != OPERATIONAL_AUTHORITY != ARBITRATION_AUTHORITY
VALIDATED_OUTCOME != VALIDATED_MECHANISM
CORRECT_PREDICTION != UNIVERSAL_AUTHORITY
SUCCESSFUL_INTERVENTION != UNRESTRICTED_POLICY_CONTROL
```

Generic source notation `E→ΔW` is retained as an architectural abstraction and does not erase the later typed-authority distinction.

## 7. Learning/adaptation attack

```text
STORED_CORRECTION != INCORPORATED_STATE
INCORPORATED_STATE != CAUSALLY_REALIZED_BEHAVIOR
LEARNING != LONG_TERM_ADAPTIVE_GOVERNANCE
PERSISTENCE != INTELLIGENCE
```

The parse preserves these as candidate distinctions, not demonstrated causal stages.

## 8. Challenge-topology attack

The source proposes independent/dimension-relevant challenge channels and a prohibition on a constitution being sole judge of evidence against itself.

```text
CHALLENGE_CHANNEL_PROPOSAL != VERIFIED_INDEPENDENCE
RAW_CHALLENGE != COMMAND
VALID_CHALLENGE_PROPOSAL != OBSERVED_CAPTURE_RESISTANCE
AFFECTED_PARTY_APPEAL_AS_DESIGN_CHANNEL != EXECUTED_APPEAL_RESULT
```

The source itself says selective challenge resistance remains empirically open.

## 9. Failure-localization attack

The four frozen benchmark intervention classes are proposals:

```text
ΔU  update failure
Δ𝒞  constitutional failure
ΔO  interface failure
ΔQ  challenge failure
```

Transport rejects:

```text
FOUR_CLASS_TAXONOMY_AS_UNIVERSAL_CAUSAL_DECOMPOSITION = CONTAINED
PREDICTED_INTERVENTION_AS_IDENTIFIED_CAUSAL_LOCUS     = CONTAINED
MATCHED_SYMPTOM_DESIGN_AS_EXECUTED_DISCRIMINATION     = CONTAINED
```

## 10. Internal result-status / Cerebro-governance attack

The v1.0 source defines internal future-result statuses `Support`, `Failure`, and `Break`.

```text
SOURCE_SUPPORT_STATUS != OBSERVED_SUPPORT
SOURCE_FAILURE_STATUS != OBSERVED_FAILURE
SOURCE_BREAK_STATUS   != OBSERVED_BREAK
SOURCE_BREAK_RULE     != CEREBRO_AMENDMENT_AUTHORITY
```

The rule that only a Break licenses v1.0 core expansion is governance of the source object, not permission to change Cerebro's global parse/compression ontology.

## 11. Minimal-sufficient-revision attack

The source defines:

```text
minimize revision cost subject to restored reliability
```

and lists held-out recovery, retention, transfer, boundary preservation, latency, reopening and collateral-change criteria.

The weights and thresholds are explicitly domain-dependent; benchmark thresholds are prospective.

```text
CONCEPTUAL_OBJECTIVE != CALIBRATED_OPTIMIZATION_FUNCTION
PROPOSED_THRESHOLD != EMPIRICALLY_SELECTED_THRESHOLD
```

## 12. Current implementation boundary

`STATUS.md` explicitly places implementation in the future:

1. latent structural causal generators;
2. matched surface renderers;
3. intervention-grounded repair oracles;
4. leakage and independence audits;
5. frozen benchmark-validity result set before agent comparison.

The immutable R36 tree contains none of those implementations or results.

```text
CURRENT_IMPLEMENTATION_BOUNDARY = PROSPECTIVE
EXECUTABLE_ARCHITECTURE         = NONE_ON_R36_HEAD
TEST_SOURCE                     = NONE_ON_R36_HEAD
RESULT_ARTIFACTS                = NONE_ON_R36_HEAD
```

## 13. GitHub execution/chronology ceiling

```text
VISIBLE_COMMIT_COUNT                                  = 3
POST_FREEZE_COMMIT_COUNT                              = 1
WORKFLOW_SOURCE_PATHS_AT_HEAD                         = 0
PR_TRIGGERED_WORKFLOW_RUNS_VISIBLE_THROUGH_CONNECTOR = 0
COMBINED_STATUS_RECORDS_VISIBLE_THROUGH_CONNECTOR     = 0
```

Because no workflow source exists at the frozen head, the run/status absence is unsurprising but remains connector-bounded.

```text
NO_HEAD_WORKFLOW != UNIVERSAL_NONEXECUTION_PROOF
COMMIT_ORDER != SEMANTIC_EDGE
```

## 14. Source typo

`docs/GOVERNANCE.md` contains `challene debt` in one debt list. Context identifies it as the challenge-debt category already present elsewhere.

This is a lexical source typo, not an epistemic distinction or semantic contradiction.

```text
TYPO_CORRECTION_AUTHORITY = NONE_REQUIRED
PARSE_REPAIR              = NONE
```

The parse preserves the source wording in notes while normalizing the category only at the semantic-label level.

## 15. Death-test verdict

```text
SOURCE_COVERAGE                       = PASS
FREEZE_BOUNDARY                       = PASS
STANDING_SEPARATION                   = PASS
CORE_METADATA_SEPARATION              = PASS
THEORY_RESULT_SEPARATION              = PASS
BENCHMARK_IMPLEMENTATION_RESULT_SPLIT  = PASS
EXTERNAL_REFERENT_CONTAINMENT          = PASS
AUTHORITY_TYPE_SEPARATION              = PASS
SOURCE_GOVERNANCE_CEREBRO_SPLIT        = PASS
EXECUTION_LINEAGE                      = PASS
UNRESOLVED_REFERENCE_PRESERVATION      = PASS
SEMANTIC_DEATH_TEST                    = PASS

SOURCE_SURFACE_REPAIR                  = NONE
PARSE_REPAIR                           = NONE
NEW_EPISTEMIC_DISTINCTION_REQUIRED     = NO
NEW_GLOBAL_PARSER_ROLE                 = NONE
AMENDMENT_005                          = NOT_EARNED
COMPRESSION_ACCESS                     = OPEN
```

The four unresolved primary-artifact references remain part of the effective parse; they are not parser failures and do not block loss-bounded compression.