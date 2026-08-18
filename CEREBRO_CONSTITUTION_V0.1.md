# CEREBRO CONSTITUTION v0.1

**Status:** `FROZEN`  
**Frozen:** 2026-08-18  
**Scope:** Step 1 — genome only

> Cerebro begins with a bounded theory of legitimate change. It has no senses, memory store, corpus model, evidence schema, claim class, graph, learned component, or research-control machinery at this stage.

## 1. Constitutional object

Cerebro evaluates candidate state transitions of the form

\[
(S_t,H_t) \xrightarrow{\Delta} (S_{t+1},H_{t+1}).
\]

The constitution does **not** decide scientific truth. It constrains whether a proposed canonical transition is legitimate.

The constitution has two layers:

\[
\mathcal C_{0.1}=\mathcal C_E+\mathcal C_D
\]

with

\[
\mathcal C_E=\{E1,E2,E3,E4\}
\]

and

\[
\mathcal C_D=\{D1\}.
\]

Thus

\[
\boxed{\mathcal C_{0.1}=\{E1,E2,E3,E4,D1\}}.
\]

## 2. Scope boundaries

Two boundaries are constitutional and must not be collapsed:

\[
\boxed{\text{CANONICAL} \neq \text{TRUE}}
\]

`Canonical` means legitimately admitted into persistent Cerebro state with its represented epistemic role, scope, standing, and provenance. A canonical object may later be supported, contradicted, unresolved, rejected, superseded, or otherwise bounded without ceasing to be a legitimate historical object.

\[
\boxed{\text{LEGITIMATE TRANSITION} \neq \text{GUARANTEED TRUTH}}
\]

The constitution regulates legitimate epistemic transition. It does not manufacture contact with reality, guarantee source truth, guarantee instrument reliability, or make admitted empirical material infallible.

## 3. Provisional primitive vocabulary

The constitution depends provisionally on nine terms. These are minimal operational meanings, not a downstream ontology.

### 3.1 State — `S_t`
The canonical epistemic state at developmental time `t`.

### 3.2 History — `H_t`
The ordered record of admitted state-transition events through `t`. History records how canonical state changed; it is not interchangeable with current state.

### 3.3 Candidate transition — `Delta`
A proposed change to canonical state.

### 3.4 Canonical
Legitimately admitted into Cerebro's persistent state with an explicit epistemic role and standing. Canonicality does not assert truth.

### 3.5 Source-grounded artifact
An immutable or version-identifiable source object whose identity and relevant content can be resolved independently of a derived object referring to it. Source grounding establishes the existence/content of the source object, not the truth of every assertion it contains.

### 3.6 Derived object
Anything admitted through extraction, transformation, inference, synthesis, classification, association, or another operation rather than merely being the terminal source artifact itself.

### 3.7 Standing
The epistemically relevant status and transition rights assigned to an object in a canonical state.

### 3.8 Warrant
The admitted basis cited to license a specific canonical transition or standing. Provenance explains origin; warrant licenses standing.

### 3.9 Dependency
A represented relation whose standing can make one object's epistemic disposition relevant to a transition involving another. A dependency is itself an epistemic object, not trusted infrastructure beneath the epistemic system.

## 4. Epistemic constitution

### E1 — Grounded Warrant Closure

A canonical derived object must retain dependency-complete, resolvable derivation provenance relative to the operation that produced it.

Any epistemic standing transition must possess a finite, semantically well-founded warrant structure whose relevant authority does not derive from the transition being authorized.

Consequences:

- existence/derivation provenance and standing-warrant provenance are distinct;
- source grounding does not automatically terminate standing warrant;
- authority cycles are forbidden even when there is no literal graph self-loop;
- mutually stabilizing warrant structures without an admitted well-founded root do not bootstrap authority;
- dependency-complete provenance includes epistemically consequential acquisition, selection, control, and adjudication operators when those operators materially determine the warrant set or standing;
- dependency relations cannot establish their own authority merely by appearing in the dependency representation.

### E2 — Operational Epistemic Separability

Any established distinction whose loss changes canonical transition admissibility must remain operationally distinguishable to the machinery making that admissibility judgment.

Equivalently, two objects or states may not be treated as epistemically interchangeable for an operation when their established transition rights differ.

A distinction merely stored but unavailable to the transition mechanism is not preserved operationally.

Consequences:

- different IDs are insufficient when the transition evaluator still collapses the relevant distinction;
- scope, dependency, standing dimension, representation, or relation distinctions must remain operational when their loss changes admissibility;
- operation-relative representation equivalence may be established, but must not be assumed merely because two representations are individually adequate;
- when a consequential collapse is demonstrated, E2 identifies the representational failure and D1 may license bounded differentiation.

### E3 — Licensed Effect Closure

Every operation that can alter canonical epistemic standing **or the warrant/control context from which standing is computed** must itself be licensed for its specific epistemic effect.

For any proposed effect, Cerebro must evaluate the complete currently operative and relevant warrant structure for the target, standing dimension, scope, dependency context, and any epistemically consequential control or transformation operators.

No effect may exceed its license. No recognized relevant object within a constituted admission surface may be silently suppressed. No admitted relevant warrant may be silently omitted. No selection, exclusion, classification, scoping, deferment, aggregation, prioritization, composition, conflict-resolution, relevance, stopping, criterion, translation, migration, dependency-traversal, or other authority-bearing operator may transport standing merely because it is available to the implementation.

Claims of completeness may extend only over coverage for which completeness is itself warranted.

When incompatible warrants remain unresolved and no licensed resolution rule exists, no resolving standing transition is licensed.

When newly admitted warrant or newly earned representation makes an existing canonical disposition relevant for reconsideration, that disposition must receive an explicit warranted treatment rather than being preserved or changed by silent inertia.

Preservation means: a transition may not modify canonical structure outside the effect closure positively licensed by its complete warrant and dependency context. It does **not** assert metaphysical independence of everything outside that closure.

### E4 — Historical Semantic Immutability

Later development may append corrections, reinterpretations, supersessions, and current-standing changes, but it may not mutate the canonical historical record of what Cerebro represented earlier or the operative semantics required to reconstruct that earlier state.

Conceptually:

\[
H_t \preceq H_{t+1}
\]

where the prior history remains an unchanged historical prefix of the later history.

Historical bytes alone are insufficient: historical replay must preserve the meaning of statuses, relations, dependency semantics, scopes, and other transition-relevant concepts as they operated at the historical point.

Therefore:

- contradicted is not deleted;
- superseded is not never-existed;
- retrospective interpretation is not contemporaneous interpretation;
- correcting current standing does not rewrite earlier standing;
- discovering or rejecting a dependency later does not rewrite the fact that an earlier state did or did not use that dependency.

## 5. Developmental constitution

### D1 — Earned, Gap-Bounded Differentiation

Cerebro may increase or alter its epistemic representational distinctions or transition-admissibility behavior only in response to a demonstrated consequential inadequacy of the prior epistemic representation.

The resulting development is bounded by the demonstrated gap: it may alter only representational distinctions or admissibility behavior implicated by that inadequacy. Previously valid behavior outside the established dependency closure of the gap is preserved unless separately warranted.

Software changes that preserve canonical distinctions and transition-admissibility behavior are ordinary engineering evolution and do not require D1.

D1 governs epistemic development, not code cleanliness, performance optimization, module naming, storage layout, or other implementation changes that are epistemically equivalent.

A representation's greater richness or expressivity does not grant it greater epistemic authority.

## 6. Law-level separation

The five laws are retained because each excludes a demonstrated failure class not independently excluded by the other four.

| Law | Constitutional question |
|---|---|
| **E1 — Grounded Warrant Closure** | Is the warrant/dependency structure legitimately grounded and semantically well-founded? |
| **E2 — Operational Epistemic Separability** | Does the representation preserve distinctions that can change legitimate treatment? |
| **E3 — Licensed Effect Closure** | What may the complete warrant/control/dependency context legitimately cause? |
| **E4 — Historical Semantic Immutability** | May later development alter what the system historically represented or meant? |
| **D1 — Earned, Gap-Bounded Differentiation** | When and how far may Cerebro itself acquire new epistemic structure? |

E1 is not reducible to E3: E1 governs whether a warrant structure is eligible to participate in adjudication; E3 governs what an eligible warrant context may cause.

E2 is not reducible to D1: E2 requires preservation of consequential distinctions; D1 governs when new representational differentiation is permitted and how far it may extend.

E4 is orthogonal to the current-state laws: it preserves historical truthfulness even when current revision is fully warranted.

## 7. Hostile constitutional fixture families

These are **tests**, not additional constitutional laws.

### A — Conflicting warrants
**Status:** `PROVISIONALLY_CONTAINED`

Attacks include:

- ordinary conflicting warrants;
- recursively conflicting warrants and warrants about warrants;
- semantic authority cycles;
- recency, quantity, evidence-type, specificity, and scope-size laundering;
- unwarranted conflict-resolution operators;
- conflicts about conflict-resolution rules;
- partial and unknown scope overlap;
- post-hoc scope narrowing;
- unlicensed uniform treatment across varying warrant contexts.

Core derived invariant:

> No epistemic conclusion may be obtained by silently selecting, excluding, combining, prioritizing, or uniformly applying warrants. Each such operation is itself authority-bearing when it affects canonical standing.

### B — Strategic admission / omission
**Status:** `PROVISIONALLY_CONTAINED`

Attacks include:

- selective extraction;
- strategic exclusion and deferment;
- incomplete coverage represented as complete coverage;
- prospective but outcome-favoring admission apertures;
- policy self-certification;
- selective typing and scope assignment;
- target/question substitution;
- adaptive relevance;
- adaptive thresholds;
- optional stopping and state-dependent search termination;
- outcome-conditioned evidence acquisition.

Core derived invariant:

> Selection may allocate access; it does not allocate authority. A bounded epistemic aperture may control attention, but it may not silently manufacture broader authority from the evidence stream that its own control policy selected.

### C — Order dependence / representation hysteresis
**Status:** `PROVISIONALLY_CONTAINED`

Attacks include:

- processing order used as priority;
- lossy incremental reduction;
- irreversible transitions that alter future warrant treatment without license;
- representation hysteresis when a consequential distinction is learned after an earlier disposition;
- non-conservative representation development;
- representation migration that silently changes standing;
- two adequate representations with unproven transport equivalence;
- epistemically equivalent representations producing non-convergent standing.

Core derived invariant:

> History may be path-dependent; current authority may not be accidentally so. Processing order may determine what Cerebro saw when, but it may not determine current standing once the same relevant warrant context and transition-relevant distinctions are available, absent warranted sequential dependence.

### D — False dependency
**Status:** `PROVISIONALLY_CONTAINED`

Attacks include:

- unwarranted dependency edges;
- omitted standing dependencies;
- dependency shielding through provenance truncation;
- dependency inflation;
- shared provenance treated as dependency;
- computational dependency collapsed into authority dependency;
- transitive path propagation without operator warrant;
- direction, condition, scope, or dependency-strength laundering;
- mutually validating dependency relations;
- dependency correction that rewrites history;
- graph absence treated as proof of independence.

Core derived invariants:

> Dependencies are epistemic objects inside the system, not trusted infrastructure beneath it.

> A dependency path has no more authority than the warranted propagation semantics of the relations composing that path.

> Absence of a represented dependency is not proof of independence.

## 8. Derived invariants — not additional laws

The following are retained as testable consequences, not promoted into the constitution:

- `newer != stronger`;
- `older != stronger`;
- `more numerous != stronger`;
- `specificity != precedence`;
- `broader scope != precedence`;
- `similarity != support`;
- `selected evidence != complete evidence`;
- `not extracted != not present`;
- `not examined != false`;
- `processing order != epistemic priority`;
- `representation richness != authority`;
- `same label != same epistemic state`;
- `individual representation adequacy != cross-representation equivalence`;
- `shared provenance != standing dependency`;
- `computational dependency != authority dependency`;
- `absence of dependency edge != established independence`;
- `grounded dependency edges != warranted arbitrary path traversal`;
- `standing of premises != standing of their relation`;
- `standing of premises != standing of their transformation rule`;
- `historical preservation != current-standing inertia`;
- `control dependency != authority dependency`.

## 9. Constitutional amendment rule

`v0.1` is frozen, not sacred.

A constitutional amendment may be considered only when a frozen counterexample demonstrates either:

1. the current constitution admits a transition that should be inadmissible; or
2. the current constitution forbids a transition independently established as necessary.

Before amendment, failure must be localized to the shallowest sufficient level. Constitutional change is the deepest revision locus and must not be used when the failure can be repaired at a shallower level such as fixture, implementation, interpretation, operation, or representation.

Any amendment must:

- preserve the prior constitution historically;
- identify the counterexample that forced reopening;
- state the smallest constitutional change required;
- preserve prior hostile fixtures unless separately superseded with warrant;
- avoid importing mature research conclusions as primitive constitutional premises.

## 10. Freeze basis

`CEREBRO_CONSTITUTION_V0.1` is frozen because:

- five-law non-redundancy has been demonstrated by independent failure fixtures;
- hostile families A–D are provisionally contained without requiring a sixth law;
- known escape routes reduce to the existing laws or their derived consequences;
- the law vocabulary is substrate-independent;
- the amendment path is itself governed;
- the constitution does not require mature SSI or later research-lineage conclusions as premises.

This is **not** a claim of metaphysical completeness.

It is a claim of adversarially supported minimality sufficient to end Step 1.

## 11. Developmental boundary after freeze

At this freeze point:

- Genome: present.
- Senses: absent.
- Artifact substrate: absent.
- Observation representation: absent.
- Evidence representation: absent.
- Claim representation: absent.
- Memory store: absent.
- Research-state replay: absent.
- Learned machinery: absent.
- Research control: absent.

No downstream Cerebro structure is licensed merely because it seems useful.

\[
\boxed{\text{No new Cerebro epistemic structure without demonstrated consequential inadequacy.}}
\]

Step 1 ends here.
