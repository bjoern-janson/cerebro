# R08 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R08_COMPRESSION_V0.1.json`  
**Projection ledger:** `R08_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json`  
**Effective parse:** 396 units  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The death test asks whether complete unit accounting is also standing-preserving and loss-bounded under the R01–R07 effective contract.

## 1. Projection accounting

The candidate ledger accounts for all effective parse units:

```text
EFFECTIVE_PARSE_UNITS          = 396
PRIMARY_PROJECTIONS            = 395
UNRESOLVED_DISPOSITIONS        = 1
UNMAPPED_PARSE_UNITS           = 0
DUPLICATE_PRIMARY_OWNERS       = 0
```

```text
PARSE_ACCOUNTING_WITHOUT_MAPPING = CONTAINED
```

But mapping completeness alone is not sufficient.

---

## 2. `EXECUTABLE_ROLE_RECOLLAPSE`

The candidate maps source-local roles including:

```text
SOURCE_DESCRIBED_SCOPE_OR_PURPOSE
IMPLEMENTATION_ASSUMPTION
EXECUTABLE_IMPLEMENTATION
IMPLEMENTED_OUTPUT_BEHAVIOR
SOURCE_ASSERTION_HYPOTHESIS
```

into broad compressed items such as:

```text
R08:CODE:CAUSAL_ANALYSIS
R08:CODE:GENERATOR_METRICS
R08:CODE:OMEGA
R08:CODE:SIMULATION_SUITE
```

The projection ledger records the source roles, but the destination items themselves are typed as generic `EXECUTABLE_IMPLEMENTATION` and do not preserve the distinction as separate node-state objects.

This violates the R04-earned boundary:

\[
\boxed{
\text{method specification}
\neq
\text{implementation assumption}
\neq
\text{implemented output behavior}
\neq
\text{execution}
\neq
\text{result}.
}
\]

A ledger annotation cannot make a mixed-standing destination semantically adequate by itself.

```text
EXECUTABLE_ROLE_RECOLLAPSE = HIT
```

Failure locus: compression representation.

No new top-level coordinate is required. The existing executable/method coordinate can be split by already-earned roles.

---

## 3. `HISTORICAL_CASE_ROLE_RECOLLAPSE`

Case units carrying different standings are mapped into single interpretation objects.

Examples:

```text
R08:P:HAD:HISTORICAL_HYPOTHESIS
  SOURCE_ASSERTION_HYPOTHESIS
  -> R08:INTERP:HISTORICAL_AD

R08:P:HAD:PROXIES
  METHODOLOGY_OR_TEST_PROTOCOL
  -> R08:INTERP:HISTORICAL_AD

R08:P:HML:D3_CANDIDATE
  SOURCE_ASSERTION_HYPOTHESIS
  -> R08:INTERP:HISTORICAL_ML

R08:P:HSCI:PROXIES
  METHODOLOGY_OR_TEST_PROTOCOL
  -> R08:INTERP:HISTORICAL_SCIENCE
```

This re-collapses parser-separated hypothesis/method/interpretation standing during compression—the failure class first exposed by R03.

```text
HISTORICAL_CASE_ROLE_RECOLLAPSE = HIT
```

No new semantic role is earned. Existing hypothesis, methodology and interpretation roles are sufficient.

---

## 4. `CROSS_DOMAIN_EXAMPLE_DESTINATION_LOSS`

Several source example collections are mapped into destinations whose compressed content does not preserve their enumerated examples.

Representative cases:

```text
R08:P:D06:EXAMPLES
  [printing press, programming languages, scientific method, automated research systems]
  -> R08:INTERP:HISTORICAL_SCIENCE

R08:P:MGM:HISTORICAL_EXAMPLES
  [scientific method, programming languages, automatic differentiation]
  -> R08:INTERP:HISTORICAL_SCIENCE

R08:P:TPHASE:HISTORICAL_EXAMPLES
  [scientific method, programming languages, compilers, automatic differentiation]
  -> R08:STATUS:HISTORICAL_CASE_QUALIFIER
```

The source units are technically mapped but their distinctions are not represented by the destination payload.

Thus:

\[
\boxed{
\text{projection destination exists}
\not\Rightarrow
\text{projection destination preserves content}.
}
\]

```text
CROSS_DOMAIN_EXAMPLE_DESTINATION_LOSS = HIT
```

A source-interpretation item for cross-domain examples is sufficient; no new top-level class is required.

---

## 5. `ASSUMPTION_PURPOSE_RECOLLAPSE`

`R08:P:ASSUME:PURPOSE` is source-described scope/purpose but is projected into `R08:ASSERT:ASSUMPTIONS`, whose payload represents the assumption set itself.

The source purpose explains what the assumptions document is for; it is not itself an assumption.

```text
ASSUMPTION_PURPOSE_RECOLLAPSE = HIT
```

Repair is local: project the purpose to program/source scope while retaining A1–A20 in the assumption item.

---

## 6. Amendment-004 recurrence discipline

The ledger makes multi-source occurrence counts reconstructible and explicitly inherits:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

No source recurrence is counted as corroboration.

Exact duplicated simulation content likewise carries zero warrant multiplication.

```text
PRIMARY_SOURCE_RECURRENCE_AS_WARRANT = CONTAINED
EXACT_DUPLICATE_BLOB_AS_WARRANT = CONTAINED
```

---

## 7. Formal-tension non-regressions

The candidate keeps separate:

```text
R08:DEF:OMEGA_DELTA_G
R08:DEF:OMEGA_DGM_DT
R08:DEF:OMEGA_OPERATIONAL_FAMILY
```

and separate state representations A/B.

```text
CROSS_FILE_FORMAL_RECONCILIATION = CONTAINED
CANONICAL_SELF_LABEL_AS_SUPERSESSION = CONTAINED
```

---

## 8. Empirical-standing non-regressions

```text
PROPOSED_PROXY_AS_VALIDATED_MEASURE = CONTAINED
PROPOSED_DATASET_AS_EMPIRICAL_DATA  = CONTAINED
SIMULATION_CODE_AS_EXECUTION_RECORD = CONTAINED
PROGRAMMED_SUPPORT_LABEL_AS_SCIENTIFIC_SUPPORT = CONTAINED
HISTORICAL_CASE_RHETORIC_AS_VALIDATION = CONTAINED
ONE_BYTE_SCRIPT_AS_NEGATIVE_RESULT = CONTAINED
```

No reported empirical result or negative result is admitted from R08.

---

## Verdict

```text
PARSE_ACCOUNTING_WITHOUT_MAPPING             = CONTAINED
EXECUTABLE_ROLE_RECOLLAPSE                   = HIT
HISTORICAL_CASE_ROLE_RECOLLAPSE              = HIT
CROSS_DOMAIN_EXAMPLE_DESTINATION_LOSS        = HIT
ASSUMPTION_PURPOSE_RECOLLAPSE                = HIT
PRIMARY_SOURCE_RECURRENCE_AS_WARRANT          = CONTAINED
CROSS_FILE_FORMAL_RECONCILIATION             = CONTAINED
PROPOSED_PROXY_AS_VALIDATED_MEASURE           = CONTAINED
PROPOSED_DATASET_AS_EMPIRICAL_DATA            = CONTAINED
SIMULATION_CODE_AS_EXECUTION_RECORD           = CONTAINED
HISTORICAL_CASE_RHETORIC_AS_VALIDATION        = CONTAINED

GLOBAL_CONTRACT_FAILURE                       = NO
NEW_PARSER_ROLE_EARNED                        = NO
NEW_TOP_LEVEL_COMPRESSION_COORDINATE_EARNED   = NO
R08_REUSABLE_NODE_STATE                       = NOT_YET_EARNED
R09_ACCESS                                    = BLOCKED
MAP_AUTHORITY                                 = NONE
SCIENTIFIC_AUTHORITY                          = NONE
PROPAGATE_KERNEL                              = NOT_EARNED
CEREBRO_STEP_2                                = CLOSED
```
