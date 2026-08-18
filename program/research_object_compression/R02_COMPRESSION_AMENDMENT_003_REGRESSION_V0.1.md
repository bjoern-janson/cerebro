# R02 COMPRESSION — AMENDMENT 003 REGRESSION V0.1

**Contract amendment:** `RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_003.md`  
**Effective R02 parse:** base + `R02_EXHAUSTIVE_PARSE_V0.1_AMENDMENT_001.json`  
**Effective R02 compression before this regression:** base + `R02_COMPRESSION_V0.1_AMENDMENT_001.json`  
**Persistent record state:** `FROZEN`

R02 is re-evaluated after R01 under the newly earned `METHODOLOGY_OR_TEST_PROTOCOL` coordinate.

## Attack — `LEGACY_METHODOLOGY_AS_ASSERTION`

The R02 exhaustive parse already distinguishes:

```text
R02:P:README:MOTIVATION        kind = METHODOLOGICAL_MOTIVATION
R02:P:README:WEIGHT_RATIONALE kind = METHODOLOGICAL_RATIONALE
```

The prior compression repair preserved those units as:

```text
R02:ASSERT:MOTIVATION
R02:ASSERT:WEIGHT_RATIONALE
```

under `ASSERTIONS_OR_HYPOTHESES` because no method coordinate yet existed.

Amendment 003 now makes that projection insufficient:

\[
\boxed{\text{methodological motivation/rationale}\neq\text{assertion or hypothesis}.}
\]

```text
LEGACY_METHODOLOGY_AS_ASSERTION = HIT
```

**Shallowest locus:** effective R02 compression projection under successor contract.

The source semantics and parse standing were already correct. No parse repair and no source reinterpretation are required.

## Secondary reuse audit

The effective R02 projection ledger assigns every effective parse unit one primary destination. No additional compression view is currently identified that reuses either methodological parse unit as a second authority-bearing occurrence.

```text
R02_SECONDARY_REUSE_WITHOUT_ROLE = NOT_DEMONSTRATED
```

## Required repair

Relocate only the two methodological items from the legacy assertion view into `METHODOLOGY_OR_TEST_PROTOCOL`, preserving their content, source locators, and source-relative standing. Preserve the frozen prior representation historically and mark the legacy assertion items superseded in effective reconstruction.

## Verdict

```text
R02_EFFECTIVE_PARSE_UNIT_COUNT       = 39
R02_PARSE_REPAIR_REQUIRED            = NO
LEGACY_METHODOLOGY_AS_ASSERTION      = HIT
R02_LOCAL_COMPRESSION_REPAIR_REQUIRED= YES
R02_SEMANTIC_REINTERPRETATION        = NONE
R02_STANDING_CHANGE                  = NONE
R03_RETEST                           = BLOCKED_UNTIL_R02_REPAIR
R04_ACCESS                           = NOT_AUTHORIZED
MAP_AUTHORITY                        = NONE
SCIENTIFIC_AUTHORITY                 = NONE
```
