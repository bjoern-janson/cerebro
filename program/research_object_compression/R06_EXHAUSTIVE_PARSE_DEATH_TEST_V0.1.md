# R06 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Object:** `CEREBRO_R06_EXHAUSTIVE_PARSE_DEATH_TEST_V0.1`  
**Parse candidate:** `R06_EXHAUSTIVE_PARSE_V0.1.json`  
**Source surface:** `R06_SOURCE_SURFACE_V0.1.json`  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R06 is the first held-out repository in the sequence whose main pressure is proposal/operationalization standing rather than executable-source standing.

## Attack A — `SOURCE_PATH_INTEGRITY`

Every parse unit must resolve to an admitted path/blob pair on the frozen source surface.

The unit:

```text
R06:P:MATH:FERTILITY
```

records:

```text
path = 03_Mathematical_Formormalization.md
```

but the frozen source inventory contains:

```text
03_Mathematical_Formalization.md
```

with blob:

```text
5f2dc22a34629262633deea648457bb3dd159ae4
```

The blob is correct but the path is not an admitted source path, so source reconstruction fails at the path coordinate.

```text
SOURCE_PATH_INTEGRITY = HIT
```

Failure locus: parse provenance / source locator.

No semantic repair is licensed.

---

## Attack B — `SECTION_HEADING_AS_EPISTEMIC_STANDING`

The README section `Non-Claims` contains four explicit negations followed by a positive statement:

```text
It proposes a unifying hypothesis about adaptive epistemic dynamics.
```

The candidate parse records that positive statement as:

```text
semantic_role = SCOPE_LIMIT
standing_qualifier = SOURCE_SELF_CHARACTERIZATION
```

The surrounding section label does not make the positive proposition a scope limit.

The already-earned rule applies:

\[
\boxed{
\text{source block identity}
\neq
\text{epistemic unit standing}.
}
\]

The unit should retain its positive source standing independently of the heading that contains it.

```text
SECTION_HEADING_AS_EPISTEMIC_STANDING = HIT
```

Failure locus: local R06 unit standing.

---

## Attack C — `CANDIDATE_METRIC_AS_ESTABLISHED_MEASURE`

`03_Mathematical_Formalization.md` explicitly says its metrics are candidate operational tools and are not final universal equations.

The parse preserves candidate qualifiers on the elasticity, compression-gain, abstraction-tax, time-elasticity, tool-metabolism, fertility, and possible scientific-score formulas.

No `REPORTED_RESULT`, `ESTABLISHED_MEASURE`, scientific-standing update, or authority effect is emitted.

```text
CANDIDATE_METRIC_AS_ESTABLISHED_MEASURE = CONTAINED
```

---

## Attack D — `PROPOSED_BENCHMARK_AS_EXECUTED_BENCHMARK`

`04_Benchmark_Design.md` repeatedly proposes evaluation dimensions, forgetting tests, representation-respec tests, task families and success criteria.

The parse represents these as:

```text
METHODOLOGICAL_TEST_PROTOCOL
```

with source-relative proposal qualifiers.

No execution, observed outcome or empirical result is inferred.

```text
PROPOSED_BENCHMARK_AS_EXECUTED_BENCHMARK = CONTAINED
```

---

## Attack E — `THEORETICAL_FAILURE_MODE_AS_NEGATIVE_RESULT`

R06 describes failure modes such as premature compression, permanent expansion, the Hoarder, the Ignorer and unhealthy representation lifetimes.

These are represented as source assertions with `SOURCE_DESCRIBED_FAILURE_MODE` qualifiers, not empirical negative results.

```text
THEORETICAL_FAILURE_MODE_AS_NEGATIVE_RESULT = CONTAINED
```

---

## Attack F — `OPEN_QUESTION_AS_CLAIM`

The README primary research question and six explicit open problems remain `OPEN_QUESTION` units.

```text
OPEN_QUESTION_AS_CLAIM = CONTAINED
```

---

## Attack G — `NON_CLAIM_INVERSION`

The explicit negative bullets under `Non-Claims` remain source-bounded scope limits and do not become positive scientific claims.

```text
NON_CLAIM_INVERSION = CONTAINED
```

This attack is distinct from Attack B: the problem is not the genuine non-claims, but allowing the section heading to overwrite the standing of a positive proposition colocated with them.

---

## Verdict

```text
SOURCE_PATH_INTEGRITY                 = HIT
SECTION_HEADING_AS_EPISTEMIC_STANDING = HIT
CANDIDATE_METRIC_AS_ESTABLISHED_MEASURE = CONTAINED
PROPOSED_BENCHMARK_AS_EXECUTED_BENCHMARK = CONTAINED
THEORETICAL_FAILURE_MODE_AS_NEGATIVE_RESULT = CONTAINED
OPEN_QUESTION_AS_CLAIM               = CONTAINED
NON_CLAIM_INVERSION                  = CONTAINED
```

The effective compression contract is not challenged.

Both demonstrated failures are local to the R06 parse and require no new parser ontology.

```text
GLOBAL_CONTRACT_CHANGE = NOT_EARNED
R01_R05_REGRESSION = NOT_REQUIRED
R06_COMPRESSION = BLOCKED_PENDING_LOCAL_PARSE_REPAIR
MAP_EDGE_EMISSION = NONE
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
CEREBRO_STEP_2 = CLOSED
```
