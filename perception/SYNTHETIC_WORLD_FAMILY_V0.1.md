# SYNTHETIC_WORLD_FAMILY_V0.1

**Step:** 2.6b — bounded synthetic world family constitution  
**Persistent record state:** `FROZEN`  
**Depends on:** `perception/CURRENT_TRANSITION_SURFACE_V0.1.md`  
**Oracle transition:** `DELTA_ENC` only  
**R01 content access:** `CLOSED`  
**R01 semantic access:** `CLOSED`  
**New source contact:** `NONE`  
**Observation object:** `NOT_YET_EARNED`  
**Collision search at freeze:** `NOT_YET_EXECUTED`

This artifact fixes the synthetic world family **before** the Step 2.6 collision search. It does not inspect R01, constitute a new live encounter, create an observation, open evidence or claims, or alter the already-frozen oracle surface.

The required ordering is:

\[
\boxed{
\mathcal T_{\mathrm{current}}^{(2.6)}\ \text{frozen}
\rightarrow
\mathcal W_{\mathrm{syn}}\ \text{frozen}
\rightarrow
\text{collision search}
}
\]

No world may be added after seeing the collision result without creating a successor synthetic-family artifact.

---

## 1. Frozen current representation used by the suite

For this bounded suite, the currently represented state of a synthetic already-constituted resolution-only encounter is projected as:

\[
\boxed{
\widehat X(W)=
(
q,
\sigma_{id},
\epsilon,
\omega,
\pi,
\eta
)
}
\]

where:

- `q` — exact target binding;
- `sigma_id` — realized source identity/surface identity admitted by the encounter;
- `epsilon` — realized encounter extent;
- `omega` — outcome class;
- `pi` — derivation/source-contact provenance class required by the current contract;
- `eta` — encounter-history class required by P4/E4.

This tuple is a **suite projection**, not a new Cerebro schema or canonical class. It is only the minimal comparison surface needed to instantiate the already-frozen current encounter distinctions in synthetic fixtures.

The base represented state is:

```text
q        = SYNTHETIC_ANCHOR_A0
sigma_id = SYNTHETIC_ANCHOR_A0
extent   = IDENTITY_ONLY
outcome  = RESOLVED
provenance = LIVE_DIRECT
history    = SINGLE_ATTEMPT_SUCCESS
```

No source content, child object, metadata payload, semantic interpretation, observation, evidence, or claim is present in `X_hat`.

---

## 2. Collision-candidate family — 64 hidden-property worlds

The collision-candidate family is the full Cartesian product of six binary **latent** dimensions while holding the base represented encounter state fixed.

\[
\boxed{
\mathcal W_{\mathrm{latent}}
=
\{0,1\}^{6}
}
\]

Thus:

\[
\boxed{
|\mathcal W_{\mathrm{latent}}|=64.
}
\]

The six axes are deliberately boring and orthogonal to the resolution-only encounter:

| Axis | `0` | `1` | Current status |
|---|---|---|---|
| `H1_LITERAL` | hidden literal token `ALPHA` | hidden literal token `BETA` | unencountered content |
| `H2_LABEL` | hidden source label `DRAFT` | hidden source label `PROVEN` | unencountered source-authored label |
| `H3_PROPOSITION` | hidden text expresses proposition `P` | hidden text expresses proposition `Q` | unencountered semantic content |
| `H4_METADATA` | hidden metadata variant `M0` | hidden metadata variant `M1` | unexposed metadata |
| `H5_COPY_RELATION` | hidden material unique | hidden material copy-derived/repeated | unencountered relation |
| `H6_STRUCTURE` | hidden structure `FLAT` | hidden structure `BRANCHED` | unenumerated structure |

For every world in this family:

\[
\boxed{
\widehat X(W)=\widehat X_0.
}
\]

These latent facts are available to the synthetic fixture generator only. They are not silently admitted into Cerebro's encounter representation.

The family intentionally does **not** include a downstream operation that reads or reasons over these dimensions. The only oracle remains the frozen `DELTA_ENC` candidate transition.

---

## 3. Encoder positive controls — six already-required distinctions

Six additional worlds perturb distinctions the current interface already requires the encounter representation to expose. They are included to ensure the equality filter does not mistake an intentionally malformed/coarsened encoder for a new developmental gap.

Each control changes exactly one comparison coordinate relative to `X_hat_0`:

| World | Changed represented coordinate | Control value |
|---|---|---|
| `C1_TARGET_BINDING` | `q` | `SYNTHETIC_ANCHOR_B0` |
| `C2_REALIZED_IDENTITY` | `sigma_id` | `SYNTHETIC_ANCHOR_B0` |
| `C3_EXTENT` | `epsilon` | `BOUNDED_PARTIAL_SURFACE` |
| `C4_OUTCOME` | `omega` | `NOT_RESOLVED` |
| `C5_PROVENANCE` | `pi` | `STALE_CACHE_SUBSTITUTION_EXPOSED` |
| `C6_HISTORY` | `eta` | `FAILED_THEN_RESOLVED` |

For every control world `C_i`:

\[
\boxed{
\widehat X(C_i)\neq\widehat X_0.
}
\]

and for `i != j`:

\[
\boxed{
\widehat X(C_i)\neq\widehat X(C_j).
}
\]

These controls do not create new transition types. They test only that the Step 2.6 equality filter respects distinctions already required by the frozen encounter contract.

---

## 4. Total frozen family

\[
\boxed{
\mathcal W_{\mathrm{syn}}
=
\mathcal W_{\mathrm{latent}}
\cup
\{C_1,\ldots,C_6\}
}
\]

with:

\[
\boxed{
|\mathcal W_{\mathrm{syn}}|=70.
}
\]

The exhaustive unordered pair space therefore contains:

\[
\boxed{
\binom{70}{2}=2415
}
\]

pairs.

The equality filter retains only pairs satisfying:

\[
\boxed{
\widehat X(W_a)=\widehat X(W_b).
}
\]

Because all 64 latent worlds share `X_hat_0` and every positive control has a unique represented state, the frozen family predicts exactly:

\[
\boxed{
\binom{64}{2}=2016
}
\]

same-representation candidate pairs.

This pair count is part of the frozen suite specification and will be checked during execution rather than assumed as the experimental result.

---

## 5. Frozen oracle and disposition rule

The suite may evaluate only the already-frozen oracle transition:

\[
\boxed{
\mathcal T_{\mathrm{current}}^{(2.6)}
=
\{\Delta_{\mathrm{enc}}\}.
}
\]

For every latent-family world, `DELTA_ENC` is the same candidate effect class: canonical admission of a truthful record of the already-constituted resolution-only encounter represented by `X_hat_0` under the current P1–P4 / E1–E4 semantics.

The hidden axes do not alter the encounter target, realized identity, extent, outcome, admitted provenance, encounter history, or authority ceiling of that candidate record.

No additional transition sensitive to `H1`–`H6` may be introduced during execution.

---

## 6. Collision criterion

For every unordered pair in the frozen family:

1. compute the two frozen suite projections `X_hat`;
2. discard the pair if the projections differ;
3. for surviving pairs, evaluate the same `DELTA_ENC` disposition in each world;
4. report a collision only if:

\[
\boxed{
\widehat X(W_a)=\widehat X(W_b)
\land
D_{\mathcal C}(W_a,\Delta_{\mathrm{enc}})
\neq
D_{\mathcal C}(W_b,\Delta_{\mathrm{enc}}).
}
\]

A collision demonstrates representational insufficiency. It does **not** establish that the minimal repair is an Observation object.

---

## 7. Execution stopping rule

The search stops only when either:

```text
COLLISION_FOUND
```

or the complete frozen unordered pair family has been exhausted.

If no collision is found after exhaustion, the maximum permitted result is:

```text
NO_COLLISION_ON_FROZEN_SYNTHETIC_SUITE
```

This is a bounded negative result. It does not establish universal representational sufficiency.

---

## 8. Hostile suite-integrity fixtures

### `POST_RESULT_WORLD_ADDITION`

Add or alter synthetic worlds after the collision outcome is known.

**Expected:** `REJECT_SUITE_MUTATION_AFTER_FREEZE`.

### `INTERESTING_CONTENT_BIAS`

Construct R01-like or research-bearing semantic content specifically to encourage a desired observation-layer result.

**Expected:** `REJECT_SEMANTICALLY_BIASED_SYNTHETIC_FAMILY`.

### `POSITIVE_CONTROL_COLLAPSE`

Treat a pair that differs on target identity, realized identity, extent, outcome, provenance, or encounter history as having equal current representation.

**Expected:** `REJECT_MALFORMED_CURRENT_ENCODER`.

### `SMUGGLED_CONSEQUENCE`

Introduce a new operator that reads a hidden axis solely so that two latent worlds acquire different treatment.

**Expected:** `REJECT_SELF_JUSTIFYING_TASK`.

### `NO_COLLISION_AS_UNIVERSAL_PROOF`

Promote exhaustion of this bounded family into a claim that no representational collision can exist.

**Expected:** `REJECT_BOUNDED_NEGATIVE_RESULT_OVERREACH`.

---

## 9. Freeze verdict

```text
STEP_2.6a                         = CLOSED
STEP_2.6b_FAMILY                  = FROZEN
SYNTHETIC_WORLD_COUNT             = 70
LATENT_COLLISION_CANDIDATES       = 64
ENCODER_POSITIVE_CONTROLS         = 6
TOTAL_UNORDERED_PAIR_COUNT        = 2415
EXPECTED_EQUAL_REPRESENTATION_PAIRS = 2016
ORACLE_TRANSITION                 = DELTA_ENC
NEW_SOURCE_CONTACT                = NONE
R01_CONTENT_ACCESS                = CLOSED
R01_SEMANTIC_ACCESS               = CLOSED
FIRST_OBSERVATION_OBJECT          = NOT_YET_EARNED
COLLISION_SEARCH                  = NOT_YET_EXECUTED
```

Therefore:

\[
\boxed{
\texttt{SYNTHETIC_WORLD_FAMILY_V0.1}
=
\texttt{FROZEN}
}
\]

Only after this freeze may the exhaustive collision search execute.