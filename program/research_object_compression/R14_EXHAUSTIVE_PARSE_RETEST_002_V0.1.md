# R14 EXHAUSTIVE PARSE — RETEST 002 V0.1

**Effective input:** base parse + Amendments 001-002  
**Persistent record state:** `FROZEN`

## 1. Accounting

```text
BASE_PRIMARY_UNITS                     = 97
AMENDMENT_001_DEMOTED                 = 18
AMENDMENT_001_REPLACEMENTS            = 41
INTERMEDIATE_EFFECTIVE_UNITS          = 120
AMENDMENT_002_DEMOTED                 = 12
AMENDMENT_002_REPLACEMENTS            = 25
FINAL_EFFECTIVE_PRIMARY_UNITS         = 133
DERIVED_AUDIT_VIEWS                   = 4
ADMITTED_RESEARCH_PATHS               = 10
UNACCOUNTED_SOURCE_PATHS              = 0
```

\[
97-18+41-12+25=133.
\]

The final effective set consists of:

```text
67 unchanged original source units
41 Amendment-001 role-pure units
25 Amendment-002 role-pure units
= 133 primary source units
```

## 2. Full effective-set role audit

The audit rechecks every effective primary unit, not only the units introduced by Amendment 002.

Authority-relevant role boundaries tested:

```text
IDENTITY vs STATUS
SCOPE/PURPOSE vs RESEARCH QUESTION
DEFINITION/FORMALIZATION vs EMPIRICAL HYPOTHESIS
FORMALIZATION vs EXPERIMENTAL INTERVENTION
METRIC DEFINITION vs PREDICTION
PREDICTION vs FALSIFICATION PROTOCOL
PROJECT PLAN vs OBSERVED FILESYSTEM
ILLUSTRATIVE PSEUDOCODE vs IMPLEMENTATION
METHOD vs RESULT
SOURCE LABEL vs INDEPENDENT THEOREM STANDING
```

Result:

```text
RESIDUAL_MULTI_ROLE_PARSE_UNIT = NOT_FOUND_ON_FINAL_EFFECTIVE_SET
```

No source-local unit in the final 133-unit set was found to require a further authority-relevant role split under the frozen parser aperture.

## 3. Formal-variant preservation

The final effective set retains independently:

```text
SPEC1:ENVIRONMENT_STATE      E_t=(R_t,C_t)
ENVREADME:ENVIRONMENT_STATE  E_t=(R_t,C_t)
ENVDESIGN:ENVIRONMENT_STATE  E_t=(R_t,C_t,N_t)
```

The comparison among them remains a derived audit view only.

```text
SAME_SYMBOL_AS_CANONICAL_IDENTITY = FORBIDDEN
SOURCE_VARIANT_SUPERSESSION       = NOT_ESTABLISHED
```

## 4. Status and filesystem preservation

The final set separately preserves:

```text
README project-status occurrence
simulator-spec project-status occurrence
spec2 project-status occurrence
README-described repository layout
spec2 minimal/future layout
environment future-path plan
observed frozen filesystem aperture
```

No source-status reconciliation or prose-to-filesystem substitution is performed.

## 5. Artifact standing

```text
PSEUDOCODE_AS_IMPLEMENTATION          = CONTAINED
SIMULATOR_SPEC_AS_IMPLEMENTATION      = CONTAINED
PREDICTION_AS_RESULT                  = CONTAINED
FALSIFICATION_AS_NEGATIVE_RESULT      = CONTAINED
RECURRENCE_AS_INDEPENDENT_WARRANT     = CONTAINED
INTERNAL_CAUSAL_ARROW_AS_MAP_EDGE     = CONTAINED
```

## 6. Final parse verdict

```text
R14_EFFECTIVE_PRIMARY_PARSE_UNITS = 133
R14_DERIVED_AUDIT_VIEWS           = 4
R14_PARSE_ROLE_SEPARABILITY       = SUPPORTED_ON_FULL_EFFECTIVE_SET
R14_SOURCE_UNRESOLVED_UNITS       = 0
R14_PARSER_FAILURES               = 0
R14_COMPRESSION                   = AUTHORIZED
AMENDMENT_005                     = NOT_EARNED
R15_PARSE_ACCESS                  = CLOSED
```

This retest supersedes only the *adequacy conclusion* of the earlier bounded retest. It does not mutate or erase either earlier failure record.
