# R01–R05 COMPRESSION — AMENDMENT 004 REGRESSION V0.1

**Contract amendment:** `RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_004.md`  
**Persistent record state:** `FROZEN`  
**Regression order:** `R01 -> R02 -> R03 -> R04 -> R05`  
**Repair scope:** source-occurrence independence / warrant multiplicity only

Amendment 004 adds the default rule:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

for compressed items containing more than one distinct source parse unit unless separate provenance establishes independence.

This regression asks only whether any previously earned neuron requires a scientific/content repair under that rule.

---

## R01

The Amendment 003 regression already records that four semantically redundant README Core Model units join existing formalism-derived compression items as **additional provenance branches** rather than authority-bearing duplicates.

Under Amendment 004 those multi-source grouped items acquire the effective default:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

No source occurrence is deleted.

```text
R01_CONTENT_CHANGE             = NONE
R01_SOURCE_STANDING_CHANGE     = NONE
R01_SCIENTIFIC_STANDING_CHANGE = NONE
R01_REUSABLE_NODE_STATE        = PRESERVED_UNDER_AMENDMENT_004
```

R02 evaluation is authorized.

---

## R02

R02's effective compression/projection already preserves each of its 39 parse units exactly once and carries no rule converting repeated source occurrence into independent evidential support.

Amendment 004 therefore supplies the same default to any R02 compressed item with more than one primary source occurrence.

```text
R02_CONTENT_CHANGE             = NONE
R02_SOURCE_STANDING_CHANGE     = NONE
R02_SCIENTIFIC_STANDING_CHANGE = NONE
R02_REUSABLE_NODE_STATE        = PRESERVED_UNDER_AMENDMENT_004
```

R03 evaluation is authorized.

---

## R03

R03 already distinguishes secondary representation recurrence from warrant through:

```text
WARRANT_MULTIPLICITY_EFFECT = NONE
```

on typed secondary aliases.

Amendment 004 extends the same non-multiplication discipline to **distinct primary source occurrences** grouped into one compressed semantic item.

The two rules remain distinct:

```text
secondary reuse of one parse unit     -> Amendment 003
multiple source parse-unit recurrence -> Amendment 004
```

No R03 empirical result, interpretation, verdict, methodology item or standing changes.

```text
R03_CONTENT_CHANGE             = NONE
R03_SOURCE_STANDING_CHANGE     = NONE
R03_SCIENTIFIC_STANDING_CHANGE = NONE
R03_REUSABLE_NODE_STATE        = PRESERVED_UNDER_AMENDMENT_004
```

R04 evaluation is authorized.

---

## R04

R04's effective compression already gives secondary aliases:

```text
AUTHORITY_EFFECT = NONE
WARRANT_MULTIPLICITY_EFFECT = NONE
```

and separates implementation from execution/result standing.

Amendment 004 adds only the default non-independence semantics for any multi-source primary semantic group.

No execution record is created and no source recurrence becomes evidence.

```text
R04_CONTENT_CHANGE             = NONE
R04_SOURCE_STANDING_CHANGE     = NONE
R04_SCIENTIFIC_STANDING_CHANGE = NONE
R04_REUSABLE_NODE_STATE        = PRESERVED_UNDER_AMENDMENT_004
```

R05 evaluation is authorized.

---

## R05

R05 explicitly established role-preserving semantic compression for repeated ETA and k* source occurrences and stated:

```text
No duplicate warrant branch or scientific standing is created.
```

Amendment 004 formalizes that already-preserved behavior as the default source-occurrence rule:

```text
WARRANT_INDEPENDENCE_STATUS = NOT_ESTABLISHED
WARRANT_MULTIPLICITY_EFFECT = NONE
```

unless future independent provenance says otherwise.

```text
R05_CONTENT_CHANGE             = NONE
R05_SOURCE_STANDING_CHANGE     = NONE
R05_SCIENTIFIC_STANDING_CHANGE = NONE
R05_REUSABLE_NODE_STATE        = PRESERVED_UNDER_AMENDMENT_004
```

R06 retest is authorized.

---

## Regression verdict

```text
R01 = PASSED
R02 = PASSED
R03 = PASSED
R04 = PASSED
R05 = PASSED

PRIOR_NEURON_SEMANTIC_REPAIR_REQUIRED = NO
PRIOR_NEURON_SCIENTIFIC_CHANGE         = NONE
SOURCE_PROVENANCE_BRANCHES_REMOVED     = NONE
NEW_WARRANTS_CREATED                   = NONE
R06_RETEST                             = AUTHORIZED
R07_ACCESS                             = NOT_AUTHORIZED
MAP_AUTHORITY                          = NONE
SCIENTIFIC_AUTHORITY                   = NONE
PROPAGATE_KERNEL                       = NOT_EARNED
CEREBRO_STEP_2                         = CLOSED
```

The regression establishes only compatibility of the first five earned neuron states with Amendment 004. It does not establish evidential independence or dependence among their repeated source occurrences.
