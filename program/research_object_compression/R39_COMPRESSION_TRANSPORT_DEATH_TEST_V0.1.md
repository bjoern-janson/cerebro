# R39 Compression Transport Death Test v0.1

## Object
`R39_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1`

Repository: `bjoern-janson/cars`  
Frozen repository head: `190fa39ae5a011377f8fd6eeddb975158a483b05`  
Frozen root tree: `fc9c99ff89d1953faa2da45c54658156adf26170`

Terminal state: `PASS_AFTER_PARSE_METADATA_REPAIR`  
Map authority: `NONE`  
Scientific authority added by Cerebro: `NONE`  
Propagation: `NOT_EARNED`

## Transport accounting

```text
R39_TOTAL_FROZEN_BLOBS             = 165
R39_PARSE_ADMITTED_PATHS           = 163
R39_SCOPE_EXCLUDED_PATHS           = 2
R39_EFFECTIVE_PARSE_UNITS          = 191
R39_BASE_PATH_UNITS                = 163
R39_SEMANTIC_SPLIT_UNITS           = 28
R39_PRIMARY_COMPRESSION_ITEMS      = 163
R39_DIRECT_PROJECTION_ENTRIES      = 138
R39_GROUP_PROJECTION_ENTRIES       = 53
R39_UNMAPPED_PARSE_UNITS           = 0
R39_DUPLICATE_PRIMARY_OWNERS       = 0
R39_EXTRA_PROJECTION_UNITS         = 0
R39_PATH_MISMATCHES                = 0
R39_STANDING_MISMATCHES            = 0
R39_STANDING_MIXED_ITEMS           = 0
```

Canonical parse unit-set SHA-256:

`b6871fc2f04f58ba084be8fc0b2bcd6a847983e9633a552ff48693f9ec5c2a3e`

Canonical compression item-set SHA-256:

`eb0ab6a4cfdcb34553dd87c35ac3eb7197c61ed048bdcd3c85a59936b0351453`

Canonical owner-map SHA-256:

`6ed91b60ed0570b5c78b3e1f152267fc222f74abcd61ddbab71984c856731b88`

## Compression rule

`one item per source path x source standing`

Every item has:

- one immutable source occurrence;
- exact primary parse-unit ownership;
- same-path semantic split attachments where required;
- a payload SHA-256 over the ordered owned parse content;
- `SOURCE_OCCURRENCE_COUNT=1`;
- `WARRANT_INDEPENDENCE_STATUS=NOT_ESTABLISHED`;
- `WARRANT_MULTIPLICITY_EFFECT=NONE`.

No compression item crosses source paths or source standings.

## High-risk transport checks

| Attack | Transport result |
|---|---|
| Historical ASI-0 contract state merged into current terminal state | CONTAINED |
| Attempt #1 Boolean-pair domain failure merged into scientific negative | CONTAINED |
| Boolean-triple repair / repair CI promoted to outcome evidence | CONTAINED |
| Workflow source promoted to workflow execution | CONTAINED |
| Persisted result promoted to independently verified execution | CONTAINED |
| ASI-0 diagnostic equivalence promoted to scientific endpoint | CONTAINED |
| Post-outcome diagnosis allowed to rewrite `C=0,A=0,STOP` | CONTAINED |
| Candidate-pool pass capacity merged with realized-selection admission | CONTAINED |
| B0-v2 plumbing merged with B0 manipulation validity or B1 outcome | CONTAINED |
| A-series treatment labels allowed to contaminate generation seed interpretation | CONTAINED |
| Pilot-0 causal nonzero merged with practical largeness | CONTAINED |
| Pilot-1 finite-estimator burden promoted to intrinsic adaptive complexity | CONTAINED |
| Match1/P3/fresh-seed dissolution removed from developmental lineage | CONTAINED |
| Predictive future-plasticity signal promoted to causal plasticity | CONTAINED |
| Synthetic references / benchmark examples promoted to real-system evidence | CONTAINED |
| Same-path semantic splits counted as independent warrants | CONTAINED |
| Source-local references promoted to endpoint identity or map edge | CONTAINED |
| Chronological adjacency promoted to semantic relation | CONTAINED |
| Absence of qualifying evidence promoted to evidence against a hypothesis | CONTAINED |

## Source-local result ceilings retained by transport

### ASI-0

The terminal persisted scientific result remains:

`C=0, A=0, classification=STOP`

Standing:

`PERSISTED_SCIENTIFIC_RESULT_SOURCE_REPORTED`

Execution ceiling:

`verified repair/closure CI != independently verified canonical outcome execution`

Successful repair validation in GitHub Actions, including run `31393480741`, is preserved as execution provenance for the repair/closure layer only.

### Pilot-0

The fresh-cohort R1 result preserves a nonzero causal encoding effect on `T_instability`, while its interval remains within the inherited `±0.05` practical scale.

Therefore:

`causally nonzero != practically large`

The B0/B1 separation remains:

`manipulation validation != outcome evidence`

and the broader supplied-depth boundary remains:

`diagnostic success != revision-governance success != adaptation success`

`interface diagnosis != interface invention`

### Pilot-1

The initial descriptive finite-estimator excess is preserved together with the stronger identification sequence: exact-state matching, P3 strengthening, residual collapse, and fresh-seed sign reversal.

Therefore:

`finite-estimator burden != intrinsic adaptive complexity`

### Future-plasticity / synthetic layers

Forecastability remains predictive rather than causal. G0-G3 failure does not establish intrinsic unpredictability. Synthetic red-team and jump-world artifacts remain development evidence only.

## Projection invariants

The ledger gives exactly one primary owner to every parse unit:

`191 parse units -> 163 compression items`

with:

`138 DIRECT_TO_COMPRESSION_ITEM + 53 LOSS_BOUNDED_GROUP_TO_COMPRESSION_ITEM`

and:

`0 unmapped + 0 duplicate owners + 0 path mismatch + 0 standing mismatch`.

Same-path grouped units retain their individual parse IDs inside the owning item, so grouping does not erase the semantic distinctions that triggered the split.

## Repair record

One shallow Cerebro archival repair occurred:

`PARSE_REPAIR = MANIFEST_HASH_SEMANTICS_NORMALIZATION_ONLY`

Cause: pre-persistence byte SHA labels would become ambiguous after whitespace-normalized JSON persistence.

Revision: replace ambiguous shard `sha256` metadata with explicitly defined canonical JSON-object SHA-256 values.

Effect:

```text
SEMANTIC_UNIT_CHANGES = 0
STANDING_CHANGES      = 0
COVERAGE_CHANGES      = 0
PROJECTION_CHANGES    = 0
COMPRESSION_CHANGES   = 0
NEW_EPISTEMIC_DISTINCTION = 0
```

No further repair was required:

```text
SOURCE_SURFACE_REPAIR    = NONE
COMPRESSION_REPAIR       = NONE
PROJECTION_REPAIR        = NONE
POST_TRANSPORT_REPAIR    = NONE
AMENDMENT_005            = NOT_EARNED
```

## Effective transport contract

`EFFECTIVE_COMPRESSION_CONTRACT_TRANSPORT = SUPPORTED_ON_R01_R39_FROZEN_HEADS`

This states transport compatibility only. It grants no relation composition, synapse construction, challenge-channel authority, or scientific authority.

## Terminal node state

```text
R39_REUSABLE_NODE_STATE   = EARNED
Z39_EFFECTIVE_NODE_STATE  = EARNED
R39_MAP_EDGE_EMISSION     = NONE
R39_MAP_AUTHORITY         = NONE
R39_SCIENTIFIC_AUTHORITY  = NONE
PROPAGATE_KERNEL          = NOT_EARNED
AMENDMENT_005             = NOT_EARNED
```

Sequential state:

```text
Z01_Z39_REUSABLE_NODE_STATE  = EARNED
R40_PROGRAM_PARSE_ACCESS     = NEXT_AUTHORIZED_REPOSITORY
R41_R43_PROGRAM_PARSE_ACCESS = NOT_YET_OPENED
```

## Neural firewall

`E_map=0`

`Propagate=NOT_EARNED`

`Authority=0`

## Terminal verdict

`R39_COMPRESSION_TRANSPORT_DEATH_TEST_V0.1 = PASS_AFTER_PARSE_METADATA_REPAIR`

R39 is durably eligible to become the thirty-ninth earned Cerebro neuron once this terminal record is persisted and read back from `main`.

R40 is procedurally next-authorized only. It is not opened by this artifact.
