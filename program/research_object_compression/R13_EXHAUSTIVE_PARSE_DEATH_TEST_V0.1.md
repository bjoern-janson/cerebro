# R13 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Parse candidate:** `R13_EXHAUSTIVE_PARSE_V0.1.json`  
**Source surface:** `R13_SOURCE_SURFACE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R13 is the first repository in the sequence with a compact implementation plus persisted large raw result traces and nominal multi-seed result paths. The death test attacks both standing and provenance multiplicity.

## Attack matrix

```text
RESULTS_DIRECTORY_AS_VALIDATED_RESULT              = CONTAINED
README_RESULT_AS_MULTI_SEED_RESULT                 = CONTAINED
SUMMARY_AS_RAW_EVIDENCE                            = CONTAINED
RUNNER_CAPABILITY_AS_EACH_STORED_EXECUTION         = CONTAINED
RAW_PATH_AS_INDEPENDENT_EXECUTION                  = CONTAINED
NOMINAL_SEED_AS_PAYLOAD_INTERNAL_PROVENANCE        = CONTAINED
DISTINCT_BLOB_AS_INDEPENDENT_WARRANT               = CONTAINED
BYTE_IDENTICAL_PATHS_AS_REPLICATION                = CONTAINED
BACKUP_PATH_AS_SECOND_EXPERIMENT                   = CONTAINED
RAW_TRACE_AS_SCIENTIFIC_VALIDATION                 = CONTAINED
TRACE_ROW_AS_INDEPENDENT_WARRANT                   = CONTAINED

CROSS_ARTIFACT_AUDIT_AS_SOURCE_PARSE_UNIT          = HIT
DERIVED_PROVENANCE_CEILING_AS_SOURCE_STATUS        = HIT
```

## 1. Result standing is preserved

The README explicitly reports an observed/result surface and `RESULTS_SUMMARY.md` explicitly reports a main observation/signature. Both explicitly identify Seed 42.

The raw JSON files are persisted trace artifacts whose field structure matches the frozen runner's output schema.

The parser therefore may preserve result standing without granting scientific validation:

```text
REPORTED_EMPIRICAL_RESULT != VALIDATED_RESULT
SOURCE_INTERPRETATION_OF_RESULT != RAW_EVIDENCE
```

```text
RESULTS_DIRECTORY_AS_VALIDATED_RESULT = CONTAINED
README_RESULT_AS_MULTI_SEED_RESULT = CONTAINED
SUMMARY_AS_RAW_EVIDENCE = CONTAINED
RAW_TRACE_AS_SCIENTIFIC_VALIDATION = CONTAINED
```

## 2. Path/content/execution multiplicity is not collapsed

The frozen source inventory establishes:

```text
raw result path occurrences = 10
unique raw result blobs      = 4
```

with exact byte-identity groups:

```text
42 + 42_backup
43 + 46 + 49
44 + 45 + 47 + 50
48 alone
```

The parse preserves path occurrences separately from unique content objects.

Because raw JSON payloads contain no internal seed/run-id field, filename seed labels are not promoted into payload-internal execution provenance.

```text
RAW_PATH_AS_INDEPENDENT_EXECUTION = CONTAINED
NOMINAL_SEED_AS_PAYLOAD_INTERNAL_PROVENANCE = CONTAINED
DISTINCT_BLOB_AS_INDEPENDENT_WARRANT = CONTAINED
BYTE_IDENTICAL_PATHS_AS_REPLICATION = CONTAINED
BACKUP_PATH_AS_SECOND_EXPERIMENT = CONTAINED
```

## 3. Runner capability does not backfill run provenance

`runner.py` is ordinary executable Python and defines `run_single_seed(seed)`, including `random.seed(seed)` and serialization to `raw_seed_<seed>.json`.

That implementation establishes a possible generation path and a schema correspondence. It does not by itself prove which invocation produced each stored artifact.

```text
RUNNER_CAPABILITY_AS_EACH_STORED_EXECUTION = CONTAINED
```

## 4. Raw trace granularity does not manufacture warrant multiplicity

Each unique JSON blob contains a homogeneous mode-keyed table of timestep records. The immutable blob is retained as the reversible evidence-bearing source object; field/schema distinctions are parsed, but each row is not reified as an independent warrant branch.

```text
TRACE_ROW_AS_INDEPENDENT_WARRANT = CONTAINED
```

The source history of each row remains reconstructible through the blob.

## 5. HIT — cross-artifact audit deductions were admitted as source parse units

Four candidate units are not source-local semantic occurrences:

```text
R13:P:RAW:MULTIPLICITY
R13:P:RAW:DISTINCT_E_TRACE
R13:P:RAW:DETERMINISTIC_MODES
R13:P:RAW:PROVENANCE_CEILING
```

They are useful deductions produced by comparing the frozen inventory, runner and raw blobs.

Examples:

- `10 nominal raw paths -> 4 unique blobs` is an aperture/accounting deduction;
- comparing mode-E t=67 across four blobs is a cross-artifact audit result;
- identifying A-D as non-random relative to E combines implementation inspection with result interpretation;
- concluding independent execution count is not established is an epistemic audit judgment over missing provenance.

None should masquerade as a source-authored parse unit merely because it is well-supported.

Therefore:

\[
\boxed{
\text{source parse}
\neq
\text{cross-artifact audit inference}.
}
\]

```text
CROSS_ARTIFACT_AUDIT_AS_SOURCE_PARSE_UNIT = HIT
DERIVED_PROVENANCE_CEILING_AS_SOURCE_STATUS = HIT
```

## 6. Failure localization

The source surface is complete and the underlying source-local units remain valid.

The failure is representational bookkeeping inside the parse artifact:

```text
FAILURE_LOCUS = PARSE / PRIMARY-VS-DERIVED AUDIT SEPARABILITY
```

No new parser capability is needed. The current contract already distinguishes source parse from derived compression/audit objects through provenance and secondary-view discipline.

Minimal repair:

1. retain all 35 source-local/source-artifact primary parse units unchanged;
2. demote the four cross-artifact deductions to `DERIVED_AUDIT_VIEW` objects;
3. give those views zero scientific/map/warrant effect;
4. preserve them as hostile fixtures for compression without counting them in `Pi_13`.

## 7. Verdict

```text
R13_PARSE_UNITS_CANDIDATE              = 39
R13_SOURCE_PRIMARY_PARSE_UNITS         = 35
R13_DERIVED_AUDIT_VIEWS_TO_DEMOTE      = 4
R13_SOURCE_UNRESOLVED_UNITS            = 0
R13_PARSER_FAILURES                    = 0
CROSS_ARTIFACT_AUDIT_AS_SOURCE_PARSE_UNIT = HIT
DERIVED_PROVENANCE_CEILING_AS_SOURCE_STATUS = HIT
NEW_GLOBAL_PARSER_ROLE                 = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE   = NONE
AMENDMENT_005                          = NOT_EARNED
MAP_EDGE                               = NONE
PROPAGATION                            = NONE
CEREBRO_STEP_2                         = CLOSED
```

The parse is not yet authorized for compression until the four derived views are demoted.
