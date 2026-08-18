# R14 COMPRESSION — PRE-PROJECTION DEATH TEST V0.1

**Target:** `R14_COMPRESSION_V0.1.json` + accounting Amendment 001  
**Effective parse:** 133 primary source units  
**Persistent record state:** `FROZEN`

## 1. Question

Can every distinction in the final role-pure R14 parse be assigned to a loss-bounded compressed representation without silently normalizing source variants or dropping lower-level source detail?

## 2. Result

```text
C_SIGMA = 1
C_PI    = 1
C_D     = 0
```

The compression candidate is directionally correct but incomplete for explicit 133-unit projection.

## 3. Hits

```text
README_CURRENT_STATUS_PARTIAL_LOSS          = HIT
FALSIFICATION_OUTCOME_INTERPRETATION_LOSS  = HIT
OMEGA_QUALITY_VARIANTS_LOSS                = HIT
OPENNESS_CASE_INTERPRETATION_LOSS          = HIT
METRIC_FORMULA_DETAIL_LOSS                 = HIT
PSEUDOCODE_STRUCTURE_LOSS                  = HIT
MECHANISM_PROFILE_DETAIL_LOSS              = HIT
MECHANISM_LIBRARY_DESIGN_LOSS              = HIT
SOURCE_INVARIANT_LABEL_LOSS                = HIT
UPDATE_RULE_NOTATION_VARIANT_COLLAPSE       = HIT
SIMULATOR_MODEL_LAYER_LOSS                  = HIT
```

## 4. Examples

### 4.1 Source status

README explicitly lists:

```text
ontology defined
variables operationalized
simulator specification in progress
empirical hypothesis untested
```

The candidate preserves most of this standing across broader status objects but does not retain `variables operationalized` as a reconstructible source-status distinction.

### 4.2 Falsification alternatives

`agent/state.md` gives three possible interpretations if the central hypothesis fails:

```text
adaptive-space evolution unnecessary
another mechanism performs the same function
decomposition descriptive rather than causal
```

The general falsification item does not preserve this source interpretation family.

### 4.3 Omega quality

`core/formalism2.md` explicitly states Omega is not assumed perfect and may be complete, incomplete, delayed, noisy, or misrepresented. This is not equivalent to the existing consequence-signal definition.

### 4.4 Metric formulas

The candidate names recovery/exploration metrics but does not retain the exact source formulas:

```text
R=(P(t+Delta)-P_min)/(P_pre-P_min)
E_m=|newly activated G_i|/T
E_d=H_q(t)
```

### 4.5 Update-rule notation variants

Most source surfaces use:

```text
J(q,v,Omega) vs J(q,v)
```

but `environment/README.md` presents:

```text
J(G,Omega) vs J(G)
```

The latter cannot be silently treated as the former merely because the surrounding methodological intent is similar.

\[
\boxed{
\text{same methodological role}
\not\Rightarrow
\text{same formal argument structure}.
}
\]

### 4.6 Source invariant labels

`core/formalism2.md` and `docs/simulator-spec2.md` explicitly use source labels `Core Invariant` and `Final Invariant`. Those labels must survive as source characterization without acquiring theorem standing.

## 5. Failure localization

```text
FAILURE_LOCUS = REPRESENTATION / COMPRESSION GRANULARITY
SOURCE_ERROR  = NONE ESTABLISHED
PARSER_ERROR  = NONE ESTABLISHED ON FINAL EFFECTIVE SET
CONTRACT_GAP  = NONE ESTABLISHED
```

All missing distinctions fit existing effective coordinates and standing rules.

## 6. Minimal repair

Add source-scoped compressed items for exactly the omitted distinctions. Do not alter the existing candidate items and do not canonicalize variants.

```text
AMENDMENT_005          = NOT_EARNED
PROJECTION_LEDGER       = BLOCKED_PENDING_COMPRESSION_REPAIR
MAP_EDGE_EMISSION       = NONE
PROPAGATE_KERNEL        = NOT_EARNED
```
