# SOURCE-BOUNDED RELATION EXTRACTION V0.1 — DEATH TEST

**Contract:** `program/relation_extraction/SOURCE_BOUNDED_RELATION_EXTRACTION_V0.1.md`  
**Contract commit:** `71c491062765d3f275a7ca8c7b4a5404a603cbe4`  
**Source surface:** `program/relation_extraction/BOUNDED_SOURCE_SURFACE_V0.1.json`  
**Source-surface commit:** `334e0d42b2b64ae8fd0b3563ac7b2115349cfe00`  
**Candidate result:** `program/relation_extraction/CANDIDATE_RELATION_RESULT_V0.1.json`  
**Candidate commit:** `1ea0e050113fb685bd3f28ff35447e90b482a0c9`  
**Record type:** bounded semantic-relation extraction death-test result  
**Persistent record state:** `FROZEN`  
**Program-map authority:** `NONE`  
**Scientific synthesis authorized:** `NO`  
**Step 2 reopened:** `NO`  
**R01-R42 semantic ingestion:** `NOT_OPENED`

This death test asks the first PROGRAM CONSOLIDATION semantic-boundary question:

\[
\boxed{
\textbf{Can one bounded source surface contribute one relation candidate without the map helping invent that relation?}
}
\]

The tested source is the frozen SSI FR-001 preregistration span at lines 17-21. The tested candidate preserves the explicit statement that `Cerebro's Step 2 discipline` is used only as methodological precedent while denying dependency and authority transfer.

The test does **not** ask whether the existing PROGRAM MAP edge is correct, whether the referenced Step 2 phrase resolves to one exact Cerebro artifact, or whether the extraction procedure generalizes to other repositories.

---

## 1. Death-test standard

A V0.1 source-bounded candidate survives only if:

\[
\boxed{
\text{candidate relation content}
\subseteq
\text{what the frozen source surface explicitly supports}
}
\]

and:

\[
\boxed{
\text{existing map topology}
\not\rightarrow
\text{candidate relation completion}.
}
\]

The critical separation is:

\[
\boxed{
\text{source-grounded relation assertion}
\neq
\text{resolved graph edge}.
}
\]

---

## 2. Attack A — `MAP_EDGE_AS_EXTRACTION_EVIDENCE`

### Construction

The existing PROGRAM MAP already contains a methodological-precedent relation between Cerebro Step 2 and the SSI FR-001 benchmark. The extractor simply cites or copies that map relation and presents it as though it were newly extracted from the bounded source.

### Candidate behavior

The frozen candidate cites only:

```text
bjoern-janson/ssi
research/frontier/authority_invariance_v0_1/SPEC.md
commit e32979f...
blob 2d3d9f...
lines 17-21
```

as supporting relation evidence.

It records:

```text
MAP_EDGE_PROVENANCE_USED = false
EXISTING_MAP_RELATION_CONSULTED_AS_WARRANT = false
```

and refuses to use the existing map to resolve the Step 2 endpoint.

The source span itself contains the methodological-precedent assertion.

### Verdict

```text
MAP_EDGE_AS_EXTRACTION_EVIDENCE = CONTAINED_AT_DERIVATION_RECORD
```

### Scope note

This establishes source-only reconstructibility of the candidate record. It does **not** establish that the human/LLM operator was blind to the existing map relation.

---

## 3. Attack B — `RELATION_PHRASE_STRENGTHENING`

### Construction

The source says:

```text
used only as methodological precedent
```

but the extractor silently strengthens that to one of:

```text
scientifically supports
causally grounds
is required by
is a dependency of
authorizes
```

### Candidate behavior

The candidate freezes:

```text
RELATION_TYPE_LITERAL = METHODOLOGICAL_PRECEDENT
SOURCE_RELATION_PHRASE = is used only as methodological precedent
```

and carries no scientific or map authority effect.

### Verdict

```text
RELATION_PHRASE_STRENGTHENING = CONTAINED
```

---

## 4. Attack C — `NEGATIVE_QUALIFIER_DROPPING`

### Construction

The positive phrase `methodological precedent` is retained while the source's limiting clauses are omitted.

That would produce a semantically amplified relation.

### Candidate behavior

The candidate preserves both explicit exclusions:

```text
Cerebro is not a dependency of this benchmark
Cerebro supplies no authority to this benchmark
```

### Verdict

```text
NEGATIVE_QUALIFIER_DROPPING = CONTAINED
```

This is important because relation meaning is not reconstructible from the positive verb alone.

---

## 5. Attack D — `TARGET_NAME_AS_IDENTITY`

### Construction

The source phrase:

```text
Cerebro's Step 2 discipline
```

is silently resolved to:

```text
perception/STEP_2_LOCAL_DEVELOPMENTAL_FIXED_POINT_V0.1.md
```

merely because the existing program map uses that artifact as the endpoint.

### Candidate behavior

The bounded source contains no exact Cerebro path, commit, blob, or artifact title.

The candidate therefore freezes:

```text
ENDPOINT_RESOLUTION_STATUS = UNRESOLVED_REFERENCE
FROM_EXACT_OBJECT = null
MAP_ADMISSION_STATUS = NOT_ADMITTED_AS_RESOLVED_BINARY_EDGE
```

### Verdict

```text
TARGET_NAME_AS_IDENTITY = CONTAINED_BY_NON_RESOLUTION
```

### Consequence

The first extraction yields a relation assertion but not yet a resolved graph edge.

\[
\boxed{
\text{explicit relation assertion}
\not\Rightarrow
\text{exact endpoint identity}.
}
\]

This is a typed boundary, not a failure to preserve the source assertion.

---

## 6. Attack E — `TOPOLOGY_AS_COMPLETION`

### Construction

Once the methodological-precedent candidate exists, the extractor follows nearby map edges and emits additional relations, for example a dependency, FR-001 continuation edge, or authority-flow path.

### Candidate behavior

The candidate records:

```text
TRANSITIVE_EDGES_EMITTED = []
```

and the contract permits at most one relation candidate.

### Verdict

```text
TOPOLOGY_AS_COMPLETION = CONTAINED
```

---

## 7. Attack F — `RELATION_RECURRENCE_AS_WARRANT`

### Construction

Because the same methodological relation already appears in the program map, the extractor counts the new occurrence as an independent confirmation of that relation.

### Candidate behavior

The candidate records:

```text
RELATION_RECURRENCE_USED_AS_WARRANT = false
```

and retains:

```text
SCIENTIFIC_AUTHORITY_EFFECT = NONE
MAP_AUTHORITY_EFFECT = NONE
```

### Verdict

```text
RELATION_RECURRENCE_AS_WARRANT = CONTAINED
```

The candidate is another representation of a source assertion, not automatically another independent evidential root.

---

## 8. Attack G — `SOURCE_ABSENCE_AS_GLOBAL_NO_RELATION`

### Construction

If a future bounded source emits `NO_RELATION`, the map interprets that as proof that the corresponding research objects have no relation anywhere in the program.

### Contract containment

The frozen contract defines `NO_RELATION` as source-surface relative only.

The first witness is positive and does not instantiate `NO_RELATION`, but the anti-overreach rule is already explicit.

### Verdict

```text
SOURCE_ABSENCE_AS_GLOBAL_NO_RELATION = CONTAINED_AT_CONTRACT_BOUNDARY
```

No global negative relation is authorized.

---

## 9. Attack H — `DERIVATION_INDEPENDENCE_AS_OPERATOR_BLINDNESS`

### Construction

Because the candidate can be reconstructed from the source bytes without citing the existing map, the experiment claims that the extracting operator had no prior knowledge of the relation.

### Actual condition

The current operator has already seen the existing PROGRAM MAP relation during prior consolidation work.

Therefore source-only derivation does not establish cognitive/process blindness.

### Verdict

```text
DERIVATION_INDEPENDENCE_AS_OPERATOR_BLINDNESS = CONTAINED_BY_EXPLICIT_SCOPE
OPERATOR_BLINDNESS                            = NOT_ESTABLISHED
```

This is the strongest important limitation of the first witness.

---

## 10. Result decomposition

The first bounded semantic extraction has two different outcomes that must not be collapsed.

### A. Relation assertion extraction

The frozen source span explicitly supports:

```text
Cerebro's Step 2 discipline
    -- used only as methodological precedent -->
SSI FR-001 benchmark
```

with the negative qualifiers:

```text
NOT_A_DEPENDENCY
NO_AUTHORITY_TRANSFER
```

Therefore:

```text
EXPLICIT_RELATION_ASSERTION_EXTRACTED = YES
SOURCE_ONLY_DERIVATION_RECORD         = SUFFICIENT_FOR_ASSERTION
```

### B. Exact endpoint resolution

The phrase `Cerebro's Step 2 discipline` does not uniquely identify one exact Cerebro artifact from the bounded source surface.

Therefore:

```text
EXACT_REFERENCED_ENDPOINT_RESOLVED = NO
ENDPOINT_STATUS                    = UNRESOLVED_REFERENCE
RESOLVED_BINARY_MAP_EDGE           = NOT_EARNED
```

This is preservation of uncertainty, not extraction failure.

---

## 11. Strongest bounded claim

The first witness supports only:

\[
\boxed{
\texttt{ONE\_SOURCE\_EXPLICIT\_RELATION\_ASSERTION\_RECONSTRUCTIBLE\_WITHOUT\_MAP\_EDGE\_PROVENANCE}
}
\]

with:

```text
ENDPOINT_RESOLUTION = UNRESOLVED_REFERENCE
OPERATOR_BLINDNESS  = NOT_ESTABLISHED
```

It does not support:

- general source-bounded extractor validity;
- blind extraction;
- exact endpoint resolution;
- map-edge admission;
- relation composition;
- relation authority;
- independent-source consensus;
- R01-R42 semantic-ingestion safety;
- program synthesis.

---

## 12. What the map learned without growing an edge

The important result is unusual:

\[
\boxed{
\text{semantic information can be preserved before graph connectivity is earned}.
}
\]

The source contributes a relation assertion to the consolidation record, while exact graph attachment remains withheld.

Thus:

\[
\boxed{
\text{encountered connective claim}
\neq
\text{licensed connective tissue}.
}
\]

This is the program-level analogue of preserving experience without prematurely promoting Observation.

---

## 13. Frozen verdict

```text
SOURCE_BOUNDED_RELATION_EXTRACTION_V0.1 = FROZEN
FIRST_BOUNDED_SOURCE_SURFACE             = FROZEN
FIRST_CANDIDATE_RELATION_RESULT          = FROZEN
EXPLICIT_RELATION_ASSERTION_EXTRACTED    = YES
SOURCE_ONLY_RECONSTRUCTIBILITY           = SUPPORTED_ON_ONE_FROZEN_SOURCE_SPAN
EXACT_ENDPOINT_RESOLUTION                = NOT_EARNED
CANDIDATE_ENDPOINT_STATUS                = UNRESOLVED_REFERENCE
RESOLVED_BINARY_MAP_EDGE                 = NOT_EARNED
OPERATOR_BLINDNESS                       = NOT_ESTABLISHED
RELATION_COMPOSITION                     = NOT_OPENED
RELATION_AUTHORITY                       = NONE
MAP_AUTHORITY                            = NONE
R01_R42_SEMANTIC_INGESTION               = CLOSED
STEP_2                                   = CLOSED
```

The next possible program-consolidation question is narrower than bulk ingestion:

\[
\boxed{
\textbf{What independently warranted operation may resolve a source-side reference phrase to an exact research object without using existing map topology as the answer?}
}
\]

That question is not opened by this result.
