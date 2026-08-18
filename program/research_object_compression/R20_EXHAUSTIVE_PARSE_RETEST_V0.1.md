# R20 EXHAUSTIVE PARSE — RETEST V0.1

**Base candidate:** `R20_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-C  
**Local repair:** `R20_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Effective reconstruction

Apply the frozen source-coordinate repair, then the parse repair overlay without rewriting historical candidates.

```text
R20_SOURCE_PATHS                    = 81
R20_EFFECTIVE_PARSED_REPRESENTATIONS = 265
R20_EFFECTIVE_UNRESOLVED_UNITS       = 24
R20_EFFECTIVE_PRIMARY_PARSE_UNITS    = 289
R20_PARSER_FAILURES                  = 0
```

All 81 admitted current-head paths retain at least one effective primary source representation.

## 2. Repaired source/audit boundary

```text
58 parser/audit distinction records = DEMOTED_FROM_PRIMARY_PARSE
42 cross-artifact/repository audit unresolved records = DEMOTED_FROM_PRIMARY_PARSE
```

They remain reconstructible as secondary audit provenance. They are not lost and do not become source-authored propositions.

The key repaired invariant is:

\[
\boxed{
\text{source-local semantic content}
\neq
\text{cross-artifact audit conclusion}.
}
\]

## 3. Repaired mixed-standing configs

```text
R20P0018 = agency-transfer runtime configuration only
R20P0322 = source-coincident agency-transfer prediction

R20P0019 = permeability runtime configuration only
R20P0323 = source-coincident permeability-regime prediction
```

No standing is now collapsed in those YAML blocks.

## 4. Execution ladder regression

```text
THEORY_AS_IMPLEMENTATION                           = CONTAINED
DOCUMENTED_PROTOCOL_AS_RUN_MANIFEST                = CONTAINED
CONFIGURATION_AS_RUN_MANIFEST                      = CONTAINED
IMPLEMENTATION_AS_EXECUTION_RECORD                 = CONTAINED
TEST_SOURCE_AS_TEST_EXECUTION                      = CONTAINED
TEST_SOURCE_AS_PASSED_TEST                         = CONTAINED
RESULT_PLUMBING_AS_RESULT_ARTIFACT                 = CONTAINED
PLOT_CODE_AS_PLOT_ARTIFACT                         = CONTAINED
IMPLEMENTATION_DEFECT_AS_EMPIRICAL_NEGATIVE_RESULT = CONTAINED
IMPLEMENTATION_DEFECT_AS_THEORY_FALSIFICATION      = CONTAINED
PROXY_IMPLEMENTATION_AS_CONSTRUCT_VALIDATION       = CONTAINED
SAME_CLASS_NAME_AS_SAME_IMPLEMENTATION_OBJECT      = CONTAINED
```

The frozen repository provides implementations, tests and result plumbing but no persisted execution/result/plot artifacts and no attached GitHub Actions/status evidence for the frozen head.

Those absences remain secondary aperture facts.

## 5. Local source unresolved units retained

The 24 remaining unresolved units are source-local underspecifications such as:

```text
measurement scales and calibration
future-agent horizon / descendant identification
kappa_c estimator
module-local export inconsistency
feedback schema ambiguity
local metric scale/denominator semantics
```

They are not parser failures or empirical negatives.

## 6. Verdict

```text
R20_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS = 289
R20_PARSED_REPRESENTATIONS           = 265
R20_UNRESOLVED_SOURCE_UNITS          = 24
R20_PARSER_FAILURES                  = 0
R20_PARSE_LOCAL_REPAIRS              = 1
R20_EXHAUSTIVE_PARSE_STATE           = EARNED_FOR_COMPRESSION_INPUT
NEW_EPISTEMIC_DISTINCTION_REQUIRED  = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
BASE_PARSE_CONTRACT_AMENDMENT        = NOT_EARNED
AMENDMENT_005                        = NOT_EARNED
R20_COMPRESSION_ACCESS               = AUTHORIZED
R21_PROGRAM_PARSE_ACCESS             = NOT_YET_OPENED
```

R20 therefore reaches compression with software-specific audit pressure preserved, but without allowing that audit pressure to contaminate the source parse.
