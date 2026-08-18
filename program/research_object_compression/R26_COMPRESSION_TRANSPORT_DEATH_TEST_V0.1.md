# R26 COMPRESSION TRANSPORT — DEATH TEST V0.1

**Repository:** `bjoern-janson/aseb-framework`  
**Frozen head:** `09abf2ee64bcf4488ba4e093162405c516422d37`  
**Effective parse:** 359 units  
**Projection:** 359 exact primary dispositions  
**Enumerated compressed items:** 96  
**Candidate state:** `FROZEN_CANDIDATE`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

## 1. Projection accounting

```text
R26_EFFECTIVE_PARSE_UNITS          = 359
R26_PRIMARY_PROJECTION_ENTRIES     = 359
R26_ENUMERATED_COMPRESSED_ITEMS    = 96
R26_UNMAPPED_PARSE_UNITS           = 0
R26_DUPLICATE_PRIMARY_OWNERS       = 0
R26_EXTRA_PROJECTION_UNITS         = 0
```

Primary derivation is complete.

## 2. Candidate cardinality attack

Enumerated item objects and declared part headers disagree:

```text
PART_A declared = 33   enumerated = 33   PASS
PART_B declared = 34   enumerated = 36   HIT
PART_C declared = 26   enumerated = 27   HIT

DECLARED_TOTAL   = 93
ENUMERATED_TOTAL = 96
```

The defect is local to `item_count` metadata in Parts B and C. No item identity, standing, content, SOURCE_UNITS array, parse-unit ownership or compressed distinction is missing.

```text
COMPRESSION_CARDINALITY_METADATA = HIT
PRIMARY_PROJECTION_ACCOUNTING    = PASS
```

A local overlay is required before reusable-node credit.

## 3. Semantic attack matrix

```text
CASE_STUDY_AS_EMPIRICAL_RESULT                            = CONTAINED
HISTORICAL_INTERPRETATION_AS_CAUSAL_EVIDENCE             = CONTAINED
LIMITATION_AS_NEGATIVE_RESULT                             = CONTAINED
PROSPECTIVE_EXPERIMENT_AS_EXECUTION                       = CONTAINED
PREDICTION_AS_RESULT                                      = CONTAINED
FALSIFICATION_CONDITION_AS_FALSIFICATION_EVENT            = CONTAINED
FORMAL_CANDIDATE_AS_FIXED_LAW                             = CONTAINED
FORMAL_CANDIDATE_AS_VALIDATED_METRIC                      = CONTAINED
P_C_TO_P_E_TO_O_C_AS_CAUSALLY_IDENTIFIED                 = CONTAINED
D_R_STAR_PRODUCT_AS_DIMENSIONALLY_VALIDATED               = CONTAINED
C_R_AS_CAUSAL_IDENTIFICATION                              = CONTAINED
O_G_PLUS_AS_VALIDATED_OPERATOR_MEASURE                    = CONTAINED
F_A_AS_OPERATIONAL_OBJECTIVE                              = CONTAINED
B_F_STAR_AS_VALIDATED_VALUE_WEIGHTING                     = CONTAINED
HORIZON_VECTOR_AS_MEASURED_BOUNDARY                       = CONTAINED
PHASE_TRANSITION_AS_OBSERVED_RESULT                       = CONTAINED
ANCESTOR_RELATION_AS_ENDPOINT_IDENTITY                    = CONTAINED
ANCESTOR_RELATION_AS_PROGRAM_EDGE                         = CONTAINED
SOURCE_RECURRENCE_AS_INDEPENDENT_WARRANT                  = CONTAINED
CURRENT_HEAD_AS_DEVELOPMENTAL_HISTORY                     = CONTAINED
```

No semantic transport defect is found.

## 4. Standing preservation

The compression preserves the following separations:

```text
candidate variable != fixed law
candidate indicator != validated estimator
historical case != empirical validation
experimental design != execution
prediction != result
limitation != negative result
falsification criterion != falsification event
source relation != endpoint identity != map edge
```

The source's own epistemic caution is retained: the formal-model file calls its variables candidate hypotheses, the case-study file says the cases do not prove ASEB, and the limitations file says the framework remains incomplete.

## 5. No ontology growth is indicated

The detected cardinality defect can be repaired without:

```text
new epistemic distinction
new parser role
new top-level compression coordinate
parse-unit remap
new compressed item
item deletion
standing change
semantic rewrite
```

Therefore:

```text
NEW_EPISTEMIC_DISTINCTION_REQUIRED   = NO
NEW_GLOBAL_PARSER_ROLE               = NONE
NEW_TOP_LEVEL_COMPRESSION_COORDINATE = NONE
AMENDMENT_005                        = NOT_EARNED
```

## 6. Death-test verdict

```text
SEMANTIC_TRANSPORT                    = PASS
PRIMARY_PROJECTION_TRANSPORT          = PASS
CARDINALITY_METADATA                  = HIT
R26_REUSABLE_NODE_STATE               = NOT_YET_EARNED
R27_PROGRAM_PARSE_ACCESS              = NOT_YET_OPENED
```

Required repair is strictly local: correct the effective `item_count` values for Parts B and C by overlay, preserve the defective candidate artifacts as history, and rerun this transport test.
