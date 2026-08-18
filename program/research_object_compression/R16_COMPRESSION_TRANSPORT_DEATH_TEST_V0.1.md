# R16 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Compression candidate:** `R16_COMPRESSION_V0.1.json` + Conformance 001  
**Effective parse:** 419 primary source units  
**Projection ledger:** `R16_PARSE_TO_COMPRESSION_PROJECTION_LEDGER_V0.1.json` + Parts A-D  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R16 asks whether a long versioned experimental lineage can be compressed without retrospective coherence, version authority, execution-provenance laundering, or seed/warrant inflation.

## 1. Projection accounting

```text
R16_EFFECTIVE_PRIMARY_PARSE_UNITS = 419
R16_PRIMARY_PROJECTION_ENTRIES    = 419
R16_UNMAPPED_PARSE_UNITS          = 0
R16_DUPLICATE_PRIMARY_OWNERS      = 0
R16_UNRESOLVED_SOURCE_UNITS       = 8
R16_DERIVED_AUDIT_VIEWS           = 5
```

Projection completeness passes.

## 2. Attack matrix

```text
PRIMARY_RESULT_WITH_CROSS_ARTIFACT_AUDIT        = HIT
SOURCE_STATUS_SECONDARY_REUSE_WITHOUT_ROLE      = HIT

VERSION_NUMBER_AS_AUTHORITY_ORDER               = CONTAINED
LATER_POSITIVE_RESULT_AS_SUPERSESSION            = CONTAINED
LATER_POSITIVE_RESULT_AS_NEGATIVE_ERASURE        = CONTAINED
RESULT_VERSION_LABEL_AS_EXECUTION_BINDING        = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_HISTORY         = CONTAINED
PLACEHOLDER_RESULT_AS_BASELINE_ROBUSTNESS        = CONTAINED
MULTI_SEED_AS_INDEPENDENT_WARRANT                = CONTAINED
LEXICAL_INDEPENDENT_SEEDS_AS_WARRANT_INDEPENDENCE= CONTAINED
EMPTY_TABLE_AS_ZERO                              = CONTAINED
QUALITATIVE_OBSERVATION_AS_POPULATED_MEASUREMENT = CONTAINED
IMPLEMENTATION_AS_EXECUTION                      = CONTAINED
SOURCE_LINEAGE_AS_PROGRAM_MAP_EDGE               = CONTAINED
C_TUPLE_AS_C_PRODUCT                             = CONTAINED
A_ACTION_SPACE_AS_A_ADAPTATION                   = CONTAINED
RECURRENCE_AS_CORROBORATION                      = CONTAINED
```

## 3. HIT — primary result contains cross-artifact audit inference

Candidate item:

```text
R16:RESULT:ROB10
```

correctly owns the reported robustness tables, but its prose also states that implementation provenance points to a temporary placeholder runner rather than the v0.9.1 mechanism.

That latter statement is not part of the reported-result standing. It is a cross-artifact audit conclusion derived from:

```text
robustness_results_v1.0.md
+
robustness_suite_v1.0.py
```

The source-side result and the audit conclusion are both useful, but they must remain different epistemic objects.

The already-created audit view is:

```text
R16:AUDIT:ROB10_BASELINE_AUTHORITY_CEILING
AUTHORITY_EFFECT = NONE
```

Therefore:

\[
\boxed{
\text{valid provenance criticism}
\neq
\text{reported-result content}.
}
\]

```text
PRIMARY_RESULT_WITH_CROSS_ARTIFACT_AUDIT = HIT
```

## 4. HIT — secondary source status reused without an explicit role

Two candidate compressed items contain standing information whose primary owner lies elsewhere:

### Feedback result

`R16:RESULT:FDB10` includes the source's `100 independent seeds` qualifier even though the primary parse unit:

```text
R16:P:FR10:SEED_CLAIM
```

projects to:

```text
R16:STATUS:SOURCE_STANDINGS
```

The qualifier may be associated with the result, but Amendment 003 requires that reuse to be explicit and zero-warrant.

### Robustness placeholder implementation

`R16:IMPL:ROB10_PLACEHOLDER` includes the source status that the runner is a temporary placeholder relative to the intended v0.9.1 baseline, while the primary `PLACEHOLDER_STATUS` unit projects to source status.

Again, the contextual relationship is legitimate; silent secondary reuse is not.

```text
SOURCE_STATUS_SECONDARY_REUSE_WITHOUT_ROLE = HIT
```

Required repair:

1. make the primary result/implementation item prose standing-pure;
2. retain the source-status facts at their primary owner;
3. add typed secondary aliases carrying `AUTHORITY_EFFECT=NONE` and, for seed qualifiers, `WARRANT_MULTIPLICITY_EFFECT=NONE`;
4. retain the cross-artifact robustness ceiling only as an audit view / typed audit relation.

## 5. Contained — version history is not an authority ladder

R16 preserves distinct stages including:

```text
v0.1 incomplete result shell
v0.2 failure mode absent
v0.4 drift/decoupling absent
v0.7 positive-looking but directly lambda-penalized quality
v0.8 explicit confound diagnosis and redesign
v0.9 intended divergence pathway not reliably generated
v0.9.1 repaired toy chain
v1.0 placeholder robustness runner/result pair
v1.1/v1.2 stochastic redesigns
expansion v1.0
feedback v1.0
```

Later versions do not overwrite earlier standing.

```text
VERSION_NUMBER_AS_AUTHORITY_ORDER        = CONTAINED
LATER_POSITIVE_RESULT_AS_SUPERSESSION     = CONTAINED
LATER_POSITIVE_RESULT_AS_NEGATIVE_ERASURE = CONTAINED
```

## 6. Contained — result, implementation, and execution history remain separate

R16 contains ordinary executable source and reported result documents, but no persisted per-run/per-seed raw execution logs on the exhaustive frozen head.

The projection ledger explicitly preserves implementation and result provenance separately and states:

```text
VERSION_LABEL_SIMILARITY != EXECUTION_BINDING
```

Thus a `v0.9.1` code file and `v0.9.1` result file may be candidate-corresponding artifacts without the compression layer asserting that the stored code blob generated the stored result numbers.

```text
RESULT_VERSION_LABEL_AS_EXECUTION_BINDING = CONTAINED
REPORTED_RESULT_AS_RAW_EXECUTION_HISTORY  = CONTAINED
IMPLEMENTATION_AS_EXECUTION               = CONTAINED
```

## 7. Contained — placeholder robustness cannot launder baseline robustness

The source preserves both:

- robustness result tables in `robustness_results_v1.0.md`;
- a runner that explicitly identifies its own dynamics as temporary placeholder logic.

The audit view withholds transport from the placeholder to v0.9.1 robustness.

```text
PLACEHOLDER_RESULT_AS_BASELINE_ROBUSTNESS = CONTAINED
```

The reported tables remain historical source results. Their authority ceiling is not erased; the result itself is not deleted.

## 8. Contained — seed multiplicity does not become warrant multiplicity

R16 has:

- 10-seed placeholder robustness code;
- 100-seed stochastic robustness/expansion/feedback code;
- prose labels including `independent random seeds` and `100 independent seeds`.

The primary ledger retains those source facts and the audit view states:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

Therefore:

```text
MULTI_SEED_AS_INDEPENDENT_WARRANT                 = CONTAINED
LEXICAL_INDEPENDENT_SEEDS_AS_WARRANT_INDEPENDENCE = CONTAINED
```

## 9. Contained — incomplete result artifacts remain incomplete

The eight unresolved source units remain:

```text
results_v0.1: 4 blank result/recovery locations
robustness_results_v1.2: 4 missing main/null numeric tables
```

Qualitative statements in v1.2 remain source interpretations. They do not populate the missing measurements.

```text
EMPTY_TABLE_AS_ZERO                               = CONTAINED
QUALITATIVE_OBSERVATION_AS_POPULATED_MEASUREMENT = CONTAINED
```

## 10. Contained — local formal plurality

R16 preserves separately:

```text
C=(C_obs,C_beh,C_rev)
C=C_obs*C_beh*C_rev
```

and the v0.3 local `A_t` action-space definition separately from adaptation-mechanism `A/A_t`.

```text
C_TUPLE_AS_C_PRODUCT           = CONTAINED
A_ACTION_SPACE_AS_A_ADAPTATION = CONTAINED
```

No canonicalization or contradiction adjudication is manufactured.

## 11. Contained — lineage and recurrence carry no graph authority

The README's RAD relationship remains a source reference assertion only. Repeated C_rev formulas, stability conditions, causal-chain formulations and result patterns remain provenance-bearing occurrences with warrant independence not established.

```text
SOURCE_LINEAGE_AS_PROGRAM_MAP_EDGE = CONTAINED
RECURRENCE_AS_CORROBORATION        = CONTAINED
MAP_EDGE_EMISSION                  = NONE
```

## 12. Failure localization

Both hits are compression-representation defects:

```text
PRIMARY_RESULT_WITH_CROSS_ARTIFACT_AUDIT   -> REPRESENTATION / SECONDARY-VIEW SEPARATION
SOURCE_STATUS_SECONDARY_REUSE_WITHOUT_ROLE -> REPRESENTATION / SECONDARY-REUSE ACCOUNTING
```

They require no source or parse change and no new epistemic category.

```text
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005                        = NOT_EARNED
```

R16 is not yet closed until the primary items are standing-purified and typed secondary aliases are frozen.
