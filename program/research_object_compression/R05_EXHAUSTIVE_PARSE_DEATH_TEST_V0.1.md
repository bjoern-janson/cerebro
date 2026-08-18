# R05 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Object:** `CEREBRO_R05_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1`  
**Candidate parse:** `program/research_object_compression/R05_EXHAUSTIVE_PARSE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R05 is the first held-out repository containing a committed Jupyter notebook in addition to Markdown and executable Python.

The death test asks whether the frozen parse remains internally auditable and whether executable/notebook source is prevented from acquiring empirical standing merely from implementation or presentation.

## 1. Source inventory coverage

The recursive Git tree is non-truncated and contains 11 blobs:

```text
RESEARCH_BEARING = 9
EXCLUDED          = 2
```

Every blob has an explicit source-surface disposition.

```text
RECURSIVE_SOURCE_INVENTORY = CONTAINED
```

## 2. Notebook execution laundering

`demo.ipynb` contains one code cell with:

```text
execution_count = null
outputs         = []
```

The parse preserves the code as `EXECUTABLE_IMPLEMENTATION` and the notebook execution metadata as separate source-local units.

It does not emit a result, execution record, validation event or warrant.

```text
NOTEBOOK_CODE_AS_EXECUTION          = CONTAINED
NOTEBOOK_PRESENTATION_AS_RESULT     = CONTAINED
EMPTY_OUTPUTS_AS_GLOBAL_NONEXECUTION = CONTAINED_AT_SOURCE_SCOPE
```

The last result means only that no stored notebook execution output exists in the frozen notebook file. It does not establish that the notebook was never executed elsewhere.

## 3. Test implementation laundering

`test_suite.py` defines executable unittest assertions but the frozen repository contains no test-run record.

```text
IMPLEMENTED_TEST_AS_PASSED_TEST = CONTAINED
```

## 4. Programmed diagnostic labels

`instrument.py` and `experiment.py` contain strings such as:

```text
Measured Optimal Horizon k*
OBSERVER-LIMITED HORIZON detected
STRUCTURE-LIMITED HORIZON detected
```

These are preserved as potential `IMPLEMENTED_OUTPUT_BEHAVIOR`, not observed experimental results.

```text
PROGRAMMED_LABEL_AS_REPORTED_RESULT = CONTAINED
```

## 5. Synthetic mechanism as empirical finding

`instrument.py` hard-codes `true_k = 3` and synthetic response formulas used by the executable demonstration.

```text
SYNTHETIC_IMPLEMENTATION_AS_EMPIRICAL_FINDING = CONTAINED
IMPLEMENTATION_ASSUMPTION_AS_SCIENTIFIC_WARRANT = CONTAINED
```

## 6. Parse self-accounting

The candidate artifact declares:

```text
parse_unit_count = 68
```

but direct enumeration of the frozen `parse_units` array yields:

```text
ACTUAL_PARSE_UNITS = 67
```

No source semantic unit is thereby shown missing; the defect is the parse record's own accounting field.

This violates the consolidation accounting invariant:

\[
\boxed{
\text{coverage assertion}
\neq
\text{coverage warrant}.
}
\]

and more specifically:

\[
\boxed{
\text{declared unit count}
=
\text{enumerated effective unit count}
}
\]

must hold before compression.

```text
PARSE_UNIT_COUNT_SELF_INCONSISTENCY = HIT
```

### Failure locus

```text
LOCUS = PARSE_ACCOUNTING_METADATA
SEMANTIC_UNITIZATION_FAILURE = NO
NEW_PARSER_ROLE_REQUIRED = NO
```

## 7. Verdict

```text
R05_SOURCE_SURFACE                         = FROZEN_FULL_RECURSIVE_HEAD
R05_PARSE_CANDIDATE                        = FROZEN_FAILED_FIRST_ATTEMPT
R05_DECLARED_PARSE_UNITS                   = 68
R05_ENUMERATED_PARSE_UNITS                 = 67
PARSE_UNIT_COUNT_SELF_INCONSISTENCY        = HIT
NOTEBOOK_EXECUTION_ROLE_BOUNDARY            = CONTAINED
IMPLEMENTED_TEST_AS_PASSED_TEST            = CONTAINED
PROGRAMMED_LABEL_AS_REPORTED_RESULT        = CONTAINED
SYNTHETIC_IMPLEMENTATION_AS_EMPIRICAL_FINDING = CONTAINED
NEW_GLOBAL_PARSE_CLASS                     = NONE
COMPRESSION                                = BLOCKED_PENDING_ACCOUNTING_REPAIR
MAP_AUTHORITY                              = NONE
SCIENTIFIC_AUTHORITY                       = NONE
PROPAGATE_KERNEL                           = NOT_EARNED
CEREBRO_STEP_2                             = CLOSED
```

The required repair is count/accounting-only. The frozen candidate parse is not silently rewritten.
