# SOURCE-BOUNDED RELATION EXTRACTION V0.1

**Object:** `CEREBRO_SOURCE_BOUNDED_RELATION_EXTRACTION_V0.1`  
**Parent:** `program/PROGRAM_CONSOLIDATION_V0.1.md`  
**Record type:** derived program-consolidation extraction contract  
**Persistent record state:** `FROZEN`  
**Constitutional authority:** `NONE`  
**Scientific authority:** `NONE`  
**Map authority:** `NONE`  
**Cerebro developmental feature authorized:** `NO`  
**Step 2 reopened:** `NO`  
**R01-R42 semantic ingestion opened:** `NO`

This object defines the smallest semantic boundary for PROGRAM CONSOLIDATION:

\[
\boxed{
\textbf{Can one bounded source surface contribute one relation candidate to the program map without the map helping invent that relation?}
}
\]

It does not constitute a general semantic-ingestion engine, a graph inference system, a relation-composition calculus, or a new Cerebro cognitive organ.

The governing principle is:

\[
\boxed{
\textbf{The map may remember connective tissue, but it may not grow connective tissue from its own reflections.}
}
\]

---

## 1. Source-bounded extraction object

For one immutable/version-identifiable source surface `S`, an extraction attempt may produce at most one relation candidate `r`:

\[
S
\xrightarrow{\operatorname{Extract}_1}
r?
\]

The extraction operator is bounded by the exact source bytes and may not use existing program-map edges as evidence for the relation being extracted.

The source surface must be frozen before extraction.

The extraction result is a **candidate map relation record**, not a scientific conclusion and not an authoritative map edge.

\[
\boxed{
\text{candidate relation}
\neq
\text{scientific relation established}
\neq
\text{map authority}.
}
\]

---

## 2. Conceptual extraction dispositions

The following are extraction-level dispositions only. They are not new canonical Cerebro statuses and do not modify the PROGRAM MAP schema by themselves.

```text
EXPLICIT_RELATION
DERIVED_RELATION
UNRESOLVED_REFERENCE
NO_RELATION
```

Their meanings are:

### `EXPLICIT_RELATION`

The bounded source surface itself explicitly asserts a relation between an identifiable source-side referent and another referent.

The relation record must preserve the exact supporting span or resolvable source location.

### `DERIVED_RELATION`

The relation is not literally asserted in the source, but follows from a separately frozen, explicit transformation rule whose inputs are contained in the bounded source surface.

No `DERIVED_RELATION` is permitted in the first V0.1 witness. This class remains conceptual only until separately warranted.

### `UNRESOLVED_REFERENCE`

The source explicitly gestures toward another object or relation endpoint, but the referenced endpoint cannot be resolved without unsupported interpretation.

The extractor must preserve the unresolved reference rather than guess.

### `NO_RELATION`

No qualifying relation assertion is established on the bounded surface under the frozen extraction rule.

`NO_RELATION` is source-surface relative. It does not mean that no relation exists elsewhere.

---

## 3. First-v0.1 extraction rule

The first witness is intentionally narrow.

A candidate may be emitted only when all of the following hold:

1. **Bounded source identity** — repository, path, commit, and blob are frozen.
2. **Explicit assertion** — the relation is directly stated in the bounded source text.
3. **Source-side endpoint identifiable** — the source object making the assertion is exact.
4. **Referenced endpoint text preserved** — the source's own referential phrase is copied into the candidate record.
5. **Relation phrase preserved** — the source's own relation phrase is represented without semantic strengthening.
6. **Negative qualifiers preserved** — explicit exclusions such as `not a dependency` or `no authority` must travel with the candidate.
7. **No map-edge evidence** — an existing map relation may not be cited as provenance for extraction.
8. **No transitive completion** — no additional edge may be inferred from graph topology.
9. **No identity-by-name** — resolving a referenced endpoint requires separate endpoint-resolution provenance.
10. **One source, one relation** — the V0.1 witness stops after one candidate.

Thus:

\[
\boxed{
\text{source assertion}
\rightarrow
\text{candidate edge}
}
\]

but not:

\[
\text{source assertion}
\rightarrow
\text{candidate edge}
\rightarrow
\text{neighboring inferred edges}.
\]

---

## 4. Relation-record minimum

A V0.1 candidate relation record must contain at least:

```text
CANDIDATE_ID
SOURCE_SURFACE
SOURCE_OBJECT
RELATION_DISPOSITION
RELATION_TYPE_LITERAL
SOURCE_RELATION_PHRASE
SOURCE_REFERENCED_ENDPOINT_PHRASE
SUPPORTING_SOURCE_SPAN
NEGATIVE_QUALIFIERS
ENDPOINT_RESOLUTION_STATUS
ENDPOINT_RESOLUTION_PROVENANCE
MAP_EDGE_PROVENANCE_USED = NO
SCIENTIFIC_AUTHORITY_EFFECT = NONE
MAP_AUTHORITY_EFFECT = NONE
```

If endpoint resolution fails, the extraction result remains `UNRESOLVED_REFERENCE` rather than being completed by the map.

---

## 5. Source provenance versus relation provenance

PROGRAM CONSOLIDATION must preserve:

\[
\boxed{
\text{source provenance}
\neq
\text{relation provenance}.
}
\]

For source-bounded extraction:

- source provenance establishes the bytes/surface encountered;
- extraction provenance establishes which span caused the candidate relation to be emitted;
- endpoint-resolution provenance establishes why a referenced phrase maps to a particular research object;
- relation authority remains separate and is not granted by any of the above.

Therefore:

\[
\boxed{
\text{complete relation provenance}
\not\Rightarrow
\text{scientific authority}.
}
\]

---

## 6. Recurrence firewall

Repeated map representation must not bootstrap warrant.

\[
\boxed{
\text{relation recurrence}
\neq
\text{relation independence}
\neq
\text{relation warrant}.
}
\]

A later extraction pass may not cite an existing candidate/map edge as independent evidence merely because the same relation was previously represented.

Independent-source counting, if ever constituted, must trace provenance roots and deduplicate common ancestry rather than count appearances.

No such counting mechanism is authorized by V0.1.

---

## 7. Composition firewall

The extractor is a typed edge ledger contributor, not an inference engine.

If separate bounded surfaces later yield:

\[
A\xrightarrow{r_1}B,
\qquad
B\xrightarrow{r_2}C,
\]

V0.1 does **not** emit:

\[
A\rightarrow C.
\]

The non-rule is:

\[
\boxed{
\operatorname{Edge}(A,B,r_1)
\land
\operatorname{Edge}(B,C,r_2)
\not\Rightarrow
\operatorname{Edge}(A,C,r_3).
}
\]

Composition, if ever authorized, requires its own research object and warrant.

---

## 8. First witness surface

The first source surface is not selected from R01-R42.

It is an already encountered, already mapped, frozen SSI artifact:

```text
repository = bjoern-janson/ssi
path       = research/frontier/authority_invariance_v0_1/SPEC.md
commit     = e32979fc7c66ea01903c4e2beeea9f37dddf13f7
blob       = 2d3d9f63e170657889dabaa60790fc977281a8ff
```

The relevant source assertion is the sentence stating that Cerebro's Step 2 discipline is used only as methodological precedent, while explicitly denying dependency and authority transfer.

This surface is chosen because it is already in PROGRAM MAP coverage. Its use does not open bulk semantic ingestion of the predecessor corpus.

---

## 9. Independence boundary

Two distinct questions must not be collapsed:

\[
\boxed{
\text{derivation independence}
\neq
\text{operator blindness}.
}
\]

### Derivation independence

A candidate relation is derivationally independent of the map if another auditor can reconstruct the candidate from:

```text
frozen source surface
+ frozen extraction rule
+ separately justified endpoint resolution
```

without consulting any pre-existing map relation.

### Operator blindness

Operator blindness would require the extracting agent/process not to have prior knowledge of the target map relation.

The current conversational operator has already seen the existing PROGRAM MAP edge. Therefore:

```text
OPERATOR_BLINDNESS = NOT_ESTABLISHED
```

The V0.1 witness may test source-only reconstructibility, but it may not claim a blind extraction result.

---

## 10. Death-test targets

The first witness must be attacked against at least:

```text
MAP_EDGE_AS_EXTRACTION_EVIDENCE
RELATION_PHRASE_STRENGTHENING
NEGATIVE_QUALIFIER_DROPPING
TARGET_NAME_AS_IDENTITY
TOPOLOGY_AS_COMPLETION
RELATION_RECURRENCE_AS_WARRANT
SOURCE_ABSENCE_AS_GLOBAL_NO_RELATION
DERIVATION_INDEPENDENCE_AS_OPERATOR_BLINDNESS
```

Any hit localizes before broad source ingestion.

---

## 11. Scope ceiling

A successful V0.1 witness may establish at most:

```text
ONE_SOURCE_EXPLICIT_RELATION_CANDIDATE_RECONSTRUCTIBLE_WITHOUT_MAP_EDGE_PROVENANCE
```

It may not establish:

- general relation-extractor validity;
- semantic ingestion safety for R01-R42;
- completeness of the relation taxonomy;
- correctness of all endpoint resolution;
- relation composition;
- scientific support aggregation;
- program synthesis;
- map authority.

---

## 12. Frozen state

```text
SOURCE_BOUNDED_RELATION_EXTRACTION_V0.1 = FROZEN
FIRST_WITNESS_SURFACE                   = SSI_FR001_SPEC
R01_R42_SEMANTIC_INGESTION              = CLOSED
DERIVED_RELATION_EXTRACTION              = NOT_OPENED
RELATION_COMPOSITION                     = NOT_OPENED
INDEPENDENT_SOURCE_COUNTING              = NOT_OPENED
OPERATOR_BLINDNESS                       = NOT_ESTABLISHED
MAP_AUTHORITY                            = NONE
SCIENTIFIC_SYNTHESIS                     = NOT_AUTHORIZED
STEP_2                                   = CLOSED
```
