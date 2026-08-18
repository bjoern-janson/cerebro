# R07 EXHAUSTIVE PARSE — RETEST V0.1

**Death test:** `R07_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1.md`  
**Repair:** `R07_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The retest reopens only the four demonstrated R07 parse failures.

## 1. Accounting

The frozen base array contains 151 units. Amendment 001 adds 7 units.

```text
R07_EFFECTIVE_PARSE_UNITS = 158
R07_PARSED_UNITS          = 157
R07_UNRESOLVED_UNITS      = 1
R07_PARSER_FAILURES       = 0
```

```text
PARSE_UNIT_COUNT_SELF_INCONSISTENCY = REPAIRED
```

## 2. Repeated formal source occurrences

The Kernel's source-local formal occurrences of:

- Causal Mass;
- salience;
- computational gating;

are now explicit parse units. They remain distinct provenance occurrences even where their semantics recur in `definitions.md`, `formalism.md`, or component documents.

```text
REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS = REPAIRED
```

## 3. Enumerated distinctions

The repaired units preserve the source-enumerated Mapping Quality criteria, README repository structure, Causal Mass intended scales, task-performance examples and first phase-transition example list.

```text
ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE = REPAIRED
```

## 4. Omitted source assertions

The effective parse now preserves:

```text
R07:P:DEF:ENVIRONMENT_STRUCTURE
R07:P:DEF:VIABLE_SPACE_EXPANDS
R07:P:DEF:KERNEL_INTERPRETATION
R07:P:CM:COMPONENT_INDEPENDENCE
```

The last item records the source's use of `independent quantities` only as source content. It has:

```text
WARRANT_INDEPENDENCE_EFFECT = NONE
```

and therefore cannot satisfy Amendment 004 warrant-independence requirements.

```text
SOURCE_ASSERTION_OMISSION = REPAIRED
```

## 5. Source incompleteness remains source incompleteness

The terminal `examples.md` fragment remains:

```text
R07:P:EX:DL_TERMINAL_FRAGMENT
ROLE = UNRESOLVED_SOURCE_FRAGMENT
```

No continuation is generated.

```text
SOURCE_INCOMPLETENESS_AS_PARSER_FAILURE = CONTAINED
SOURCE_FRAGMENT_COMPLETION_BY_PARSER    = CONTAINED
```

This establishes a bounded precedent:

\[
\boxed{
\text{exhaustive parse over frozen source bytes}
\not\Rightarrow
\text{source artifact is internally complete}.
}
\]

## 6. Notation-token non-regression

Predictive-improvement `K`, complexity-form `K(M_Q)` and terminal-limit `K(M_Q)/K(I_true)` remain semantically unmerged.

```text
NOTATION_TOKEN_AS_SEMANTIC_IDENTITY = CONTAINED_AT_PARSE
```

## 7. Verdict

```text
R07_SOURCE_SURFACE                  = FROZEN_FULL_RECURSIVE_HEAD
R07_EFFECTIVE_EXHAUSTIVE_PARSE_UNITS = 158
R07_PARSED_UNITS                    = 157
R07_UNRESOLVED_PARSE_UNITS          = 1
R07_PARSE_FAILURES                  = 0

PARSE_UNIT_COUNT_SELF_INCONSISTENCY          = REPAIRED
REPEATED_FORMAL_SOURCE_OCCURRENCE_LOSS       = REPAIRED
ENUMERATED_DISTINCTION_COMPRESSION_AT_PARSE  = REPAIRED
SOURCE_ASSERTION_OMISSION                    = REPAIRED

GLOBAL_PARSE_CONTRACT_CHANGE         = NONE
R07_COMPRESSION_TEST                 = AUTHORIZED
R08_ACCESS                           = NOT_AUTHORIZED
MAP_AUTHORITY                        = NONE
SCIENTIFIC_AUTHORITY                 = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
CEREBRO_STEP_2                        = CLOSED
```

The parse is exhaustive relative to the frozen R07 aperture while preserving one source-internal unresolved fragment.