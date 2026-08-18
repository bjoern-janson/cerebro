# PERCEPTUAL_INTERFACE_V0.1

**Step:** 2.2 — first sensory interface  
**Pre-write epistemic state:** `FREEZE_CANDIDATE`  
**Persistent record state:** `FROZEN`  
**R01 semantic access:** `CLOSED`  
**Evidence layer:** `NOT_OPENED`  
**Claim layer:** `NOT_OPENED`  

This artifact freezes the smallest currently justified interface by which Cerebro may later encounter a source surface and produce a source-relative observation.

It does **not** authorize semantic ingestion of R01 or any other predecessor repository. It does **not** define evidence, claims, concepts, contradiction relations, summaries, semantic equivalence, importance, relevance, or research state.

The governing developmental boundary is:

\[
\boxed{
\text{world constituted}
\neq
\text{world understood}
}
\]

and the first permitted epistemic transition remains only:

\[
\boxed{
\text{encounter}
\rightarrow
\text{source-relative observation}
}
\]

not:

\[
\text{encounter}
\rightarrow
\text{evidence}
\rightarrow
\text{claim}.
\]

---

## 1. Dependency and authority

`PERCEPTUAL_INTERFACE_V0.1` is a derived interface contract under the already-frozen Cerebro constitution and environment.

It depends on:

- `CEREBRO_CONSTITUTION_V0.1.md`, frozen on `main` at commit `1f394d196e3fb16620793b889516e71bfa68c690`;
- `environment/ENVIRONMENT_CHRONOLOGY_V0.1.md`, frozen on `main` at commit `95d44138268408f5d834c663367583de26878578`.

Its four requirements are **not new constitutional laws**. They are sensory specializations of the frozen constitutional constraints E1–E4 and D1.

The interface cannot authorize a developmental operation that the constitution forbids. In particular:

\[
\boxed{
P1=P2=P3=P4=\texttt{PASS}
\not\Rightarrow
D1=\texttt{PASS}.
}
\]

A perceptually well-formed encounter may still be developmentally impermissible if, for example, its source aperture was selected using semantic machinery Cerebro has not earned.

---

## 2. Common encounter semantics

The four perceptual requirements are adjudicated over the **same encounter event** `e`. Their standing does not compose across unrelated events.

Conceptually:

\[
\boxed{
Q_e
\xrightarrow{\text{attempt}}
(\Omega_e,\Sigma_e?)
}
\]

where:

- `Q_e` — the requested/attempted source surface;
- `\Omega_e` — the realized encounter outcome;
- `\Sigma_e` — the actual usable source surface realized by the attempt, if any.

Only when a usable `\Sigma_e` exists may the encounter continue:

\[
\boxed{
\Sigma_e
\xrightarrow{P2}
P_e
\xrightarrow{P3}
O_e^*
}
\]

where:

- `P_e` — the percept actually produced;
- `O_e^*` — the source-relative observations legitimately admitted from that percept.

`Q_e` and `\Sigma_e` are not assumed identical. A request for a complete object may realize only a bounded partial surface.

If no usable source surface is realized:

\[
\Sigma_e=\varnothing,
\]

then P4 still records the encounter outcome, while P2 and P3 have no source percept to process.

### Composition rule

Correct component standing does not automatically authorize composition:

\[
\boxed{
\operatorname{Valid}(P_i(e_a))
\land
\operatorname{Valid}(P_j(e_b))
\not\Rightarrow
\operatorname{Valid}(P_i(e_a)\circ P_j(e_b)).
}
\]

The source identity, realized surface, derivation, percept, observations, and outcome must belong to the same grounded encounter relation.

This is a direct sensory specialization of:

\[
\boxed{
\text{standing of components}
\neq
\text{standing of composition}.
}
\]

---

## 3. P1 — Bounded, Resolvable Source Encounter

### Requirement

> **Every perceptual encounter must identify a source surface that is independently resolvable at the revision/identity and extent actually encountered. Mutable aliases, implicit revisions, and partial surfaces may not be silently represented as a different or more complete source surface.**

P1 answers:

\[
\boxed{
\textbf{What exact source surface is this encounter about?}
}
\]

A historical source surface must preserve enough identity to distinguish, where the substrate supports it:

- source/repository identity;
- immutable revision or equivalent source identity;
- address/path/object identity within that revision;
- actual encountered object/content identity where independently resolvable;
- explicit region/extent, including whether the whole object or only a bounded portion was encountered.

A branch or similar mutable navigation label may be retained as navigation provenance but is not an immutable historical source identity.

For non-Git substrates, `version-identifiable` means independently resolvable identity appropriate to the source class; it does not require a Git commit.

### Derived invariants

\[
\boxed{
\text{path}\not\Rightarrow\text{version}
}
\]

\[
\boxed{
\text{branch}\not\Rightarrow\text{immutable identity}
}
\]

\[
\boxed{
\text{file identity}\neq\text{encounter extent}
}
\]

\[
\boxed{
\text{bounded}\neq\text{complete}
}
\]

\[
\boxed{
\text{logical research object}\neq\text{mutable current source surface}
}
\]

### Hostile fixtures

- `AMBIGUOUS_SOURCE_SURFACE` — repository + path without immutable revision; **reject**.
- `BRANCH_IDENTITY_LAUNDERING` — mutable branch used as terminal source identity; **reject**.
- `UNDECLARED_PARTIAL_SURFACE` — partial extent represented as whole object; **reject**.
- `BOUNDED_EXACT_SURFACE` — exact revision/object/range with explicit bounded extent; **admit as a valid encounter target**.

### Status

```text
P1 = PROVISIONALLY_CONTAINED
```

---

## 4. P2 — Dependency-Complete Perceptual Provenance

### Requirement

> **Every perceptual record must retain resolvable derivation provenance to the source surface actually encountered and to every transformation, parameter, selection operation, or known loss that is consequential to what that record represents. A transformed, partial, reordered, generated, stale, or otherwise derived representation may not silently masquerade as its source.**

P2 answers:

\[
\boxed{
\textbf{How did this percept actually arise from that source surface?}
}
\]

Conceptually:

\[
\Sigma_e
\xrightarrow{T_1}
X_1
\xrightarrow{T_2}
\cdots
\xrightarrow{T_n}
P_e.
\]

The interface does not require universal byte-perfect perception, retention of every transient intermediate, deterministic reproduction, or prohibition of parsing/rendering/OCR.

It requires that the derivation preserve or expose every distinction consequential to what the percept is allowed to represent.

### Derived invariants

\[
\boxed{
\text{source provenance}\neq\text{derivation provenance}
}
\]

\[
\boxed{
\text{transformed representation}\neq\text{source identity}
}
\]

\[
\boxed{
\text{content provenance}\neq\text{structural provenance}
}
\]

\[
\boxed{
\text{source coordinates}\neq\text{transformed coordinates}
}
\]

\[
\boxed{
\text{dependency-complete provenance}\neq\text{archive every transient byte}
}
\]

Known lossy transformation is not automatically invalid. Unmarked consequential loss is.

### Hostile fixtures

- `RESOLVED_SOURCE_WITH_HIDDEN_TRANSFORM` — exact source rendered/truncated/normalized without transformation provenance; **reject**.
- `STALE_CACHE_SUBSTITUTION` — requested source differs from actual source that produced the percept; **reject**.
- `REORDERED_SOURCE_WITHOUT_STRUCTURE_PROVENANCE` — exact content returned in changed order with order loss hidden; **reject**.
- `COMPOSITE_SOURCE_PROVENANCE_LAUNDERING` — concatenated regions represented as one source-contiguous surface; **reject**.
- `EXPLICIT_LOSSY_PERCEPTUAL_TRANSFORM` — lossy projection with source, transform, realized coverage, and known loss retained; **admit derivation**.

### Status

```text
P2 = PROVISIONALLY_CONTAINED
```

---

## 5. P3 — Source-Relative Observation Authority

### Requirement

> **A perceptual encounter may canonically establish only observations whose truth conditions are exhausted by the resolved source surface and its admitted perceptual derivation. Source assertions, labels, reported measurements, inferred relations, paraphrases, classifications, summaries, or other interpretations may be preserved as encountered or derived material, but may not acquire evidence, claim, or world-level standing merely through perception.**

P3 answers:

\[
\boxed{
\textbf{What, if anything, may this percept legitimately assert?}
}
\]

The core authority ceiling is:

\[
\boxed{
\text{“the source contains/asserts }X\text{”}
\not\Rightarrow
\text{“}X\text{ is established.”}
}
\]

Perfect derivation provenance does not promote interpretation into observation:

\[
\boxed{
T(\Sigma)=P
\not\Rightarrow
P=\operatorname{Meaning}(\Sigma)
}
\]

and:

\[
\boxed{
T(\Sigma)=P
\not\Rightarrow
P=\operatorname{Truth}(\Sigma).
}
\]

### First-interface admissible authority

Examples of source-relative observations include, where the encounter directly warrants them:

- an exact source object was encountered;
- specified bytes/characters occurred in the realized region;
- a literal heading occurred at a source coordinate;
- an exact structured field/value occurred in the encountered representation;
- retrieval was partial;
- a specified transform emitted a specified percept;
- a source contains a literal phrase such as `proven result`.

The following are **not opened** by this interface:

- truth of the proposition expressed by source text;
- evidence status;
- claim status;
- semantic equivalence;
- contradiction relations;
- reported measurement validity;
- support relations;
- author intent;
- importance or relevance;
- summaries or central-claim extraction;
- world-level confidence.

### Hostile fixtures

- `SOURCE_ASSERTION_PROMOTED_TO_OBSERVATION` — source says `X is the mechanism`; Cerebro stores world-level `X is the mechanism`; **reject**.
- `SOURCE_SELF_LABEL_LAUNDERING` — heading `PROVEN RESULT` becomes Cerebro standing `PROVEN`; **reject**.
- `FULLY_PROVENANCED_SEMANTIC_PARAPHRASE` — complete transformation provenance but paraphrase admitted as source observation; **reject**.
- `REPORTED_VALUE_AS_MEASUREMENT` — stored value promoted from source fact to validated measurement; **reject**.
- `LITERAL_SOURCE_OBSERVATION` — exact source-relative literal fact only; **admit observation**.

### Status

```text
P3 = PROVISIONALLY_CONTAINED
```

---

## 6. P4 — Outcome-Separated Perceptual Encounter

### Requirement

> **Every perceptual encounter attempt must leave its realized outcome distinguishable at the granularity required for legitimate downstream treatment. Failed, unresolved, partial, successfully empty, and successfully complete encounters may not be silently collapsed when those distinctions are consequential. A failed or non-perceptual outcome licenses facts about the encounter operation only; it does not itself establish source absence or source content.**

P4 answers:

\[
\boxed{
\textbf{What happened to the encounter attempt itself?}
}
\]

P4 is orthogonal to the existence of a percept. It governs the attempt branch even when no usable `\Sigma_e` or `P_e` exists.

The interface does not freeze a large failure taxonomy. It preserves only outcome distinctions whose collapse changes legitimate treatment.

### Derived invariants

\[
\boxed{
\text{unattempted}
\neq
\text{attempted-but-failed}
}
\]

\[
\boxed{
\text{failed}
\neq
\text{successful-empty}
}
\]

\[
\boxed{
\text{partial}
\neq
\text{complete}
}
\]

when those distinctions are consequential.

A valid negative observation requires a successful encounter whose coverage warrants the bounded absence assertion. Failure may not impersonate absence.

### Hostile fixtures

- `UNATTEMPTED_VS_FAILED_COLLAPSE` — attempted failure leaves same consequential state as never attempted; **reject**.
- `COMPLETE_EMPTY_VS_FAILED_EMPTY_SENTINEL` — adapter's empty failure sentinel becomes a complete empty-source result; **reject**.
- `FAILED_ATTEMPT_ERASED` — failure produces no distinguishable encounter outcome; **reject**.
- `EXPLICIT_FAILED_ENCOUNTER` — exact target + failed operation preserved; source observations remain empty; **admit outcome record**.
- `EXPLICIT_PARTIAL_ENCOUNTER` — realized partial surface and incomplete outcome both retained; **admit bounded partial percept**.
- `COMPLETE_EMPTY_SOURCE` — complete successful encounter independently establishes zero-length source; **admit bounded empty-source observation**.

### Status

```text
P4 = PROVISIONALLY_CONTAINED
```

---

## 7. Non-redundancy result

Second minimization found no redundant perceptual requirement.

For each `P_i`, an isolating failure exists that satisfies the other three while violating `P_i`.

| Requirement | Unique question | Isolating failure |
|---|---|---|
| P1 | Which source surface is this encounter actually about? | ambiguous/mutable/unresolved source identity |
| P2 | How did this percept actually arise from that surface? | hidden/incomplete derivation |
| P3 | What standing may the percept acquire? | interpretation promoted to observation/world fact |
| P4 | What happened to the encounter attempt itself? | failure/non-attempt/partial/empty/complete collapse |

Therefore:

```text
individual redundancy found = 0
```

---

## 8. Cross-layer composition campaign

The hostile composition pass found a real assembly failure when locally valid records were allowed to compose across different encounter identities.

### `CROSS_LAYER_SOURCE_SPLICE`

P1 resolves target `\Sigma_1`; P2 provenance-completely derives a percept from `\Sigma_2`; P3 keeps resulting observations source-relative to `\Sigma_2`; P4 reports success. All isolated records can be valid, but the assembled claim `successful perception of \Sigma_1` is false.

**Repair:** all four requirements are evaluated over one common encounter `e`. The repair does not add P5.

### `CROSS_LAYER_EXTENT_SPLICE`

Requested target is whole-object; realized source is a bounded prefix; detached outcome says `COMPLETE`.

**Repair:** `Q_e`, `\Sigma_e`, and `\Omega_e` are mutually constrained members of the same encounter.

### `CONCURRENT_PERCEPT_MISBINDING`

Two legitimate simultaneous encounters produce two legitimate percepts; processing order incorrectly attaches one percept to the other event.

**Repair:** `PerceptOf(P,e)` must be grounded by encounter membership, not execution adjacency or “latest response.”

### `RETRY_HISTORY_SPLICE`

A failed attempt followed by a successful retry is collapsed into one historical success.

**Repair:** later success does not erase prior encounter history. A deliberately composite retry operation must preserve its constituent attempt provenance when consequential.

### `FABRICATED_EMPTY_SUCCESS`

Transport fails; adapter emits an empty sentinel and records complete success.

**Repair:** no usable `\Sigma_e` means P2 cannot establish a source-to-percept derivation; P4 cannot mark failed realization complete; P3 cannot promote the sentinel to source emptiness.

### `COMPOSITE_SOURCE_ADJACENCY_LAUNDERING`

Two exact source regions are concatenated under perfect provenance; synthetic adjacency is then asserted as source adjacency.

**Repair:** P2 records the synthetic transform; P3 limits authority to facts about the derived percept, not source structure that never existed.

### `STALE_OBSERVATION_AFTER_DERIVATION_INVALIDATION`

A later discovery shows an old transformation lost a distinction needed by a previously admitted observation.

**Repair:** current standing may reopen under P2/P3 while E4 preserves the historical fact that the observation was previously admitted.

### `UNEARNED_SEMANTIC_APERTURE`

An unconstituted semantic selector chooses “the most important file.” The resulting exact encounter can pass P1–P4.

Classification:

```text
P1 = PASS
P2 = PASS
P3 = PASS
P4 = PASS
D1 = FAIL
```

This fixture demonstrates that the sensory interface remains subordinate to the developmental constitution.

### Cross-layer verdict

After common encounter binding:

```text
surviving all-P1-P4 perceptual corruption = 0 observed
new perceptual rule forced                = 0
```

---

## 9. Constitutional localization

The four requirements remain derived from the frozen genome:

### E1 — Grounded Warrant Closure

Supports source resolution and dependency-complete perceptual derivation provenance.

### E2 — Operational Epistemic Separability

Prevents collapse of source identities, consequential transformation distinctions, source-vs-interpretation distinctions, and encounter outcomes.

### E3 — Licensed Effect Closure

Caps perceptual authority and forbids unlicensed composition of otherwise valid perceptual components.

### E4 — Historical Semantic Immutability

Prevents later success, improved tooling, or later interpretation from silently rewriting what was historically encountered or how an earlier percept was treated.

### D1 — Earned, Gap-Bounded Epistemic Differentiation

Prevents semantic perception, semantic source selection, richer failure taxonomies, or new sensory machinery from being introduced before a demonstrated consequential inadequacy earns them.

No additional constitutional law is established by this interface.

---

## 10. Freeze verdict

The freeze threshold is satisfied under the hostile fixtures developed before any semantic encounter with R01:

```text
P1 = PROVISIONALLY_CONTAINED
P2 = PROVISIONALLY_CONTAINED
P3 = PROVISIONALLY_CONTAINED
P4 = PROVISIONALLY_CONTAINED
individual redundancy found          = 0
cross-layer surviving corruption     = 0 observed
new P-rule forced                    = 0
R01 semantic encounters              = 0
```

Therefore:

\[
\boxed{
\texttt{PERCEPTUAL\_INTERFACE\_V0.1}
=\texttt{FROZEN}
}
\]

The deepest interface result is:

\[
\boxed{
\textbf{
Correct source identity, correct provenance, correct authority,
and correct outcome do not compose automatically.
The relations binding them must belong to the same encounter.
}
}
\]

---

## 11. Historical immutability and amendment discipline

This artifact is a frozen historical record of the Step 2.2 perceptual judgment.

A later counterexample should trigger the shallowest sufficient repair:

```text
counterexample
-> localize failure
-> repair encounter semantics / derived perceptual requirement if sufficient
-> amend this frozen interface only if unavoidable
-> revisit the constitution only if the failure cannot be contained below it
```

Future sensory machinery may become richer. This file must not be silently rewritten into a history in which the original interface never existed.

---

## 12. Developmental boundary

Step 2.2 ends here.

Cerebro now has:

```text
Constitution                 = FROZEN
Environment chronology       = FROZEN
Perceptual interface         = FROZEN
Semantic perception          = NOT_OPENED
Evidence                     = NOT_OPENED
Claims                       = NOT_OPENED
Research state               = NOT_OPENED
R01 semantic access          = CLOSED
```

This freeze authorizes **no R01 encounter by itself**. The next developmental transition must separately specify and authorize the first concrete sensory event under this interface.

```text
STEP_2.2                      = CLOSED
PERCEPTUAL_INTERFACE_V0.1    = FROZEN
FIRST_SENSORY_EVENT           = NOT_YET_CONSTITUTED
R01_SEMANTIC_ACCESS           = CLOSED
```
