# R16 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Candidate:** `R16_EXHAUSTIVE_PARSE_V0.1.json` + Parts A-D  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R16 tests whether a parse can preserve a long versioned experiment/implementation lineage without injecting audit conclusions into source memory or allowing result/implementation proximity to launder provenance.

## 1. Candidate accounting

```text
R16_SOURCE_PATHS          = 38
R16_CANDIDATE_PARSE_UNITS = 427
R16_UNRESOLVED_SOURCE_UNITS = 8
R16_PARSER_FAILURES       = 0
```

## 2. Attack matrix

```text
OUTPUT_BEHAVIOR_WITH_APERTURE_ABSENCE = HIT
CROSS_ARTIFACT_AUDIT_AS_SOURCE_UNIT   = HIT

RESULT_FILENAME_AS_RESULT             = CONTAINED
EMPTY_RESULT_SHELL_AS_ZERO_RESULT     = CONTAINED
QUALITATIVE_CLAIM_AS_POPULATED_TABLE  = CONTAINED
CODE_PRESENCE_AS_EXECUTION            = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_LOG  = CONTAINED
PLACEHOLDER_RUNNER_AS_BASELINE_ROBUSTNESS = CONTAINED
VERSION_NUMBER_AS_AUTHORITY_ORDER     = CONTAINED
LATER_POSITIVE_RESULT_AS_ERASURE_OF_EARLIER_NEGATIVE = CONTAINED
SOURCE_INDEPENDENT_SEEDS_AS_WARRANT_INDEPENDENCE = CONTAINED
RAD_RELATION_AS_PROGRAM_MAP_EDGE      = CONTAINED
TOKEN_IDENTITY_AS_SEMANTIC_IDENTITY   = CONTAINED
```

## 3. HIT — output behavior mixed with aperture-level absence

Fifteen code parse units correctly describe implemented print/return behavior but then append a claim such as:

```text
no persisted output artifact
no persisted raw history
no raw runs persisted
```

That absence is not local to the code file. It is derived from exhaustive repository inventory.

Affected units:

```text
R16:P:PY02:OUTPUT
R16:P:PY03:OUTPUT
R16:P:PY04:OUTPUT
R16:P:PY05:OUTPUT
R16:P:PY051:OUTPUT
R16:P:PY06:OUTPUT
R16:P:PY07:OUTPUT
R16:P:PY08:OUTPUT
R16:P:PY09:OUTPUT
R16:P:PY091:OUTPUT
R16:P:ROB10:OUTPUT
R16:P:ROB11:OUTPUT
R16:P:ROB12:OUTPUT
R16:P:EXP10:OUTPUT
R16:P:FDB10:OUTPUT
```

Therefore:

\[
\boxed{
\text{implemented output behavior}
\neq
\text{repository-level absence of persisted output}.
}
\]

```text
OUTPUT_BEHAVIOR_WITH_APERTURE_ABSENCE = HIT
```

The repair must preserve the code-local output behavior and move the absence into a derived audit view.

## 4. HIT — cross-artifact audit conclusions admitted as source units

Eight candidate units are useful conclusions but not file-local source memory:

```text
R16:P:PY03:A_SYMBOL_COLLISION
R16:P:ROB10:AUTHORITY_BOUNDARY
R16:P:ROB11:RAW_RECORD_STATUS
R16:P:ROB11:WARRANT_BOUNDARY
R16:P:ROB12:RAW_RECORD_STATUS
R16:P:EXP10:PROVENANCE_BOUNDARY
R16:P:FDB10:RAW_RECORD_STATUS
R16:P:FDB10:WARRANT_BOUNDARY
```

Examples:

- comparing `A` in the v0.3 code against `A` in the v0.3 specification;
- concluding that placeholder-runner outputs have limited authority relative to v0.9.1;
- concluding that the repository lacks per-seed raw records;
- concluding that seed multiplicity does not establish warrant independence.

All are defensible audit deductions. None should masquerade as a source unit.

```text
CROSS_ARTIFACT_AUDIT_AS_SOURCE_UNIT = HIT
```

Required repair:

```text
source units -> remain source units
cross-artifact deductions -> zero-authority audit views
```

## 5. Contained — result standing

The parse correctly separates:

```text
results_v0.1 = incomplete raw-result shell
results_v0.2 = reported result + reported absence of predicted failure
results_v0.4 = numeric result + explicit non-demonstrations
results_v0.9.1 = numeric toy result + limitations
robustness_results_v1.1 = incomplete/template fragment
robustness_results_v1.2 = missing tables + qualitative source interpretations
```

Thus:

```text
RESULT_FILENAME_AS_RESULT            = CONTAINED
EMPTY_RESULT_SHELL_AS_ZERO_RESULT    = CONTAINED
QUALITATIVE_CLAIM_AS_POPULATED_TABLE = CONTAINED
```

## 6. Contained — implementation/result lineage

The parse preserves ordinary Python implementations separately from result documents.

Most importantly, `robustness_suite_v1.0.py` explicitly says its runner is a temporary placeholder rather than the v0.9.1 simulator. The parse preserves that implementation fact without rewriting `robustness_results_v1.0.md` out of history.

Therefore:

\[
\boxed{
\text{reported robustness table}
\neq
\text{established robustness of v0.9.1}.
}
\]

```text
PLACEHOLDER_RUNNER_AS_BASELINE_ROBUSTNESS = CONTAINED
```

## 7. Contained — version history and negative results

The source progression contains multiple negative or insufficient stages:

```text
v0.1 result shell incomplete
v0.2 predicted failure absent
v0.4 constitutional drift/decoupling absent
v0.8 drift did not reliably degrade Q_Omega
v0.7 later identified as partially artificial
```

Later positive-looking versions remain later source objects; they do not erase these states.

```text
VERSION_NUMBER_AS_AUTHORITY_ORDER = CONTAINED
LATER_POSITIVE_RESULT_AS_ERASURE_OF_EARLIER_NEGATIVE = CONTAINED
```

## 8. Contained — seed and reference authority

The source uses language such as `independent random seeds` and later reports 100 independent seeds. The parse preserves the lexical claim without inferring warrant independence.

Likewise the README says Constitutional Correction adds a missing stability condition to RAD. This remains a source reference/relation assertion with no Program Map edge.

```text
SOURCE_INDEPENDENT_SEEDS_AS_WARRANT_INDEPENDENCE = CONTAINED
RAD_RELATION_AS_PROGRAM_MAP_EDGE = CONTAINED
```

## 9. Verdict

The parser has two representation defects, both already covered by earlier contract discipline.

```text
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005                        = NOT_EARNED
PARSE_REPAIR_REQUIRED                = YES
```

Required repair:

1. replace 15 mixed output/absence units with source-local output units;
2. demote 8 cross-artifact audit units;
3. create derived audit views for repository-level raw-output absence, namespace collision, placeholder-baseline authority ceiling, and seed/warrant ceiling;
4. preserve all 8 genuine unresolved source units.
