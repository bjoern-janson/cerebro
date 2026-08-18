# R05 EXHAUSTIVE PARSE — REAUDIT V0.1

**Base parse:** `R05_EXHAUSTIVE_PARSE_V0.1.json`  
**Prior accounting repair:** `R05_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`

A compression-projection audit exposed an overlooked provenance defect in one parse unit.

## Hit — source-local code unit carrying repository-wide absence

The base unit:

```text
R05:P:TEST:DIRECT_RUN
```

is source-located to:

```text
test_suite.py > __main__ block
```

but its normalized content includes both:

```text
Direct execution invokes unittest.main().
```

and:

```text
no test-run output is stored on the frozen repository surface.
```

The first statement is supported by `test_suite.py`. The second is a repository-aperture absence conclusion supported by the complete source inventory, not by the local code block.

Thus:

\[
\boxed{
\text{source-local provenance}
\neq
\text{repository-wide absence provenance}.
}
\]

```text
REPOSITORY_WIDE_ABSENCE_AS_SOURCE_LOCAL_CONTENT = HIT
```

The existing category absence record already preserves:

```text
test_run_records = NONE_ON_FROZEN_SOURCE_SURFACE
```

so no new semantic unit is required.

## Minimal repair

Replace only the normalized content of `R05:P:TEST:DIRECT_RUN` with:

```text
Direct execution invokes unittest.main().
```

Keep repository-wide run absence only at the aperture/category-absence layer.

```text
PARSE_UNIT_COUNT_CHANGE = NONE
NEW_PARSE_UNIT = NONE
NEW_PARSER_ROLE = NONE
COMPRESSION_RETEST_REQUIRED = YES
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
```
