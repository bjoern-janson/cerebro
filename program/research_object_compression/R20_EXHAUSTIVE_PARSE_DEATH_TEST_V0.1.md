# R20 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Candidate:** `R20_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-C  
**Effective source surface:** `R20_SOURCE_SURFACE_V0.1.json` + Amendment 001  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R20 is the first large implementation-heavy repository after the recent theory-first neurons. The primary attack is whether an exhaustive parser can preserve code/config/test content without importing its own audit conclusions into source-authored semantic units or converting implementation existence into execution standing.

## 1. Candidate accounting

```text
R20_SOURCE_PATHS              = 81
R20_CANDIDATE_PARSE_UNITS     = 387
R20_PARSED_REPRESENTATIONS    = 321
R20_UNRESOLVED_CANDIDATES     = 66
R20_PARSER_FAILURES           = 0
```

All 81 admitted frozen-head paths are represented. Coverage itself passes.

## 2. Attack matrix

```text
DERIVED_AUDIT_AS_PRIMARY_SOURCE_UNIT                 = HIT
PARSER_APERTURE_ASSERTION_AS_SOURCE_CONTENT          = HIT_LOCAL
CONFIGURATION_AND_PREDICTION_MIXED_STANDING          = HIT

THEORY_AS_IMPLEMENTATION                             = CONTAINED
DOCUMENTED_PROTOCOL_AS_RUN_MANIFEST                  = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                   = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                        = CONTAINED
TEST_SOURCE_AS_PASSED_TEST                           = CONTAINED
CONFIGURATION_AS_EXECUTED_CONFIGURATION              = CONTAINED
RESULT_PLUMBING_AS_RESULT_ARTIFACT                   = CONTAINED
PLOT_CODE_AS_PLOT_ARTIFACT                           = CONTAINED
IMPLEMENTATION_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT   = CONTAINED
IMPLEMENTATION_DEFECT_AS_THEORY_FALSIFICATION        = CONTAINED
PROXY_IMPLEMENTATION_AS_CONSTRUCT_VALIDATION         = CONTAINED
SAME_CLASS_NAME_AS_SAME_IMPLEMENTATION_OBJECT        = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT             = CONTAINED
CURRENT_HEAD_AS_COMPLETE_DEVELOPMENTAL_HISTORY       = CONTAINED
```

## 3. Hit — derived audit material entered the primary parse

A large set of Part B/C `DISTINCTION` records are not propositions authored by the code files. They are correct parser/audit judgments such as:

```text
implementation != execution
test source != executed test
plotting code != plot artifact
proxy implementation != construct validation
same class name != same object
```

These distinctions are important, but their proper standing is a secondary audit view derived from the frozen aperture and cross-artifact comparison.

The same applies to several unresolved records whose content is actually repository-level or cross-artifact audit, for example:

```text
main/config/protocol mismatch
no frozen result artifact
helper + environment measurement circularity
registry names versus actual frozen tree
trainer/evaluation interfaces versus agent methods
duplicate ExperimentLogger names across modules
CI/workflow absence
```

They must not be represented as if a single source file authored the conclusion.

This reproduces an already-known discipline from earlier execution-bearing neurons:

\[
\boxed{
\text{source parse}
\neq
\text{cross-artifact audit deduction}.
}
\]

No new parser role is required. The repair is demotion to secondary audit provenance.

## 4. Hit — local parser aperture wording in README unit

Historical `R20P0008` ends with a parser/audit statement that the repository points to protocols rather than reporting results. The source-supported methodological content is valid; the frozen-head result absence is an aperture audit.

Required repair:

```text
R20P0008 = narrow to source-authored evaluation/falsification methods only
result absence = secondary frozen-aperture audit
```

No unit count change follows from this narrowing.

## 5. Hit — configuration and prediction mixed standing

Two YAML units combine runtime configuration with explicit expected behavior:

```text
R20P0018 agency_transfer.yaml
  configuration: 500 episodes / assisted-removal schedule / metrics
  prediction: independent performance rises and dependency falls

R20P0019 permeability_transition.yaml
  configuration: kappa sweep / step / trials / save targets
  prediction: low kappa unstable, high kappa adaptive
```

The existing mixed-standing unitization rule applies.

Required source-coincident splits:

```text
R20P0322 = PREDICTION from configs/agency_transfer.yaml
R20P0323 = PREDICTION from configs/permeability_transition.yaml
```

The historical configuration units remain, with effective content narrowed to configuration fields only.

## 6. Effective demotion set

### Parsed representations demoted from primary source parse to secondary audit

```text
Part A:
R20P0143

Part B:
R20P0150 R20P0155 R20P0160 R20P0165 R20P0168
R20P0172 R20P0176 R20P0179 R20P0184 R20P0187
R20P0190 R20P0191 R20P0195 R20P0198 R20P0201
R20P0202 R20P0205 R20P0209 R20P0212 R20P0216
R20P0220 R20P0225 R20P0229 R20P0232 R20P0236
R20P0239 R20P0242 R20P0244 R20P0247 R20P0251
R20P0255 R20P0259 R20P0263 R20P0268 R20P0271
R20P0274 R20P0275 R20P0277 R20P0280 R20P0281
R20P0285 R20P0288 R20P0291 R20P0294 R20P0295

Part C:
R20P0299 R20P0300 R20P0303 R20P0304 R20P0307 R20P0308
R20P0312 R20P0313 R20P0316 R20P0317 R20P0320 R20P0321
```

Count:

```text
58 parsed candidate units demoted
```

### Unresolved candidates demoted to secondary audit

```text
Part A:
R20U0008 R20U0009 R20U0010 R20U0013 R20U0015
R20U0023 R20U0024 R20U0025 R20U0026 R20U0027
R20U0029 R20U0030 R20U0032 R20U0033
R20U0035 R20U0036 R20U0037

Part B:
R20U0039 R20U0040 R20U0041 R20U0042
R20U0044 R20U0045 R20U0046 R20U0048 R20U0049
R20U0050 R20U0051 R20U0052 R20U0053 R20U0054
R20U0055 R20U0056 R20U0058 R20U0059 R20U0060
R20U0061 R20U0062 R20U0063

Part C:
R20U0064 R20U0065 R20U0066
```

Count:

```text
42 unresolved candidate units demoted
```

The remaining unresolved units are source-local underspecifications such as undefined measurement scales, package-local export mismatch, generic feedback schema, and local metric-input semantics.

## 7. Secondary audit families earned by the demotion

The demoted records remain reconstructible under zero-authority audit families:

```text
R20:AUDIT:IMPLEMENTATION_EXECUTION_CEILING
R20:AUDIT:PROTOCOL_CONFIG_RUNNER_DIVERGENCE
R20:AUDIT:TEST_EXECUTION_CEILING
R20:AUDIT:RESULT_AND_PLOT_ABSENCE
R20:AUDIT:CROSS_MODULE_INTERFACE_DEFECTS
R20:AUDIT:PROXY_CONSTRUCT_VALIDITY_CEILING
R20:AUDIT:NAME_IDENTITY_COLLISIONS
R20:AUDIT:EXTERNAL_AND_CROSS_FRAMEWORK_RELATION_CEILING
```

Each has:

```text
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

These audits may describe defects and incompatibilities. They do not create empirical negative results.

## 8. Post-repair cardinality

Starting from:

```text
321 parsed + 66 unresolved = 387
```

Apply:

```text
-58 parsed audit deductions
-42 unresolved audit deductions
+2 source-coincident prediction units
```

Effective source parse becomes:

```text
265 parsed representations
24 unresolved source-local units
289 effective primary parse units
```

All 81 source paths remain represented because demoted audit records are supplemental to source-bearing units, not the sole representation of any admitted path.

## 9. What remains correctly separated

The candidate already contains the critical execution ladder:

```text
documented theory/protocol
!= configuration
!= executable implementation
!= test implementation
!= execution record
!= reported result
```

No persisted execution/result/plot artifact appears on the frozen head, and no GitHub Actions/status execution record is attached to the frozen head. Those are frozen-aperture audits, not source-local README/code propositions.

Likewise implementation defects such as registry import mismatches or missing evaluation methods remain implementation-level diagnoses:

```text
implementation defect
!= benchmark failure
!= negative scientific result
!= falsification of Ancestor Architecture.
```

## 10. Verdict

The failures are local applications of already-earned source/audit separability and mixed-standing rules.

```text
PARSE_REPAIR_REQUIRED                = YES_LOCAL
NEW_EPISTEMIC_DISTINCTION_REQUIRED  = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
BASE_PARSE_CONTRACT_AMENDMENT        = NOT_EARNED
AMENDMENT_005                        = NOT_EARNED
```

Until the local overlay and retest are frozen:

```text
R20_EXHAUSTIVE_PARSE_STATE = NOT_YET_EARNED
R20_COMPRESSION_ACCESS      = NOT_YET_OPENED
R21_PROGRAM_PARSE_ACCESS    = NOT_YET_OPENED
```

R20 therefore teaches no new anatomy yet. It tests whether existing anatomy is applied honestly to software artifacts.
