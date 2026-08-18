# R01 RESEARCH OBJECT COMPRESSION — DEATH TEST V0.1

**Contract:** `program/research_object_compression/RESEARCH_OBJECT_COMPRESSION_V0.1.md`  
**Contract commit:** `d676e9bb7e98f287ededd295f4dcd420e73e9744`  
**Source surface:** `program/research_object_compression/R01_SOURCE_SURFACE_V0.1.json`  
**Source-surface commit:** `5773b876f555407c5634e75062a5145be71a1e1f`  
**Compression:** `program/research_object_compression/R01_COMPRESSION_V0.1.json`  
**Compression commit:** `66045c165950ffc47d89992699619cd24fab20fb`  
**Record type:** bounded research-object compression death-test result  
**Persistent record state:** `FROZEN`  
**Repository:** `R01`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`  
**Cerebro Step 2 reopened:** `NO`  
**R02 compression authorized by this test alone:** `NO`

This death test asks whether one complete frozen repository head can be compressed into a useful #44 neural-node state without introducing claims, edges, authority, or omissions that the source does not support.

The target standard is:

\[
\boxed{
\text{useful compression}
\land
\text{source reconstructibility}
\land
\text{no semantic promotion}
\land
\text{no connective invention}.
}
\]

The test concerns compression integrity only. It does not adjudicate the scientific truth of Interface-Induced Computational Geometry.

---

## 1. Source basis

R01 is unusually bounded at the frozen head:

```text
REPOSITORY = bjoern-janson/interface-induced-computational-geometry
HEAD       = 806e24ad04a2d75e041b53d324a990282a92ffa5
TREE       = 74e51d3dbb3edad5ef966f795b76637a36fd1521
PATHS      = {README.md, formalism.md, LICENSE}
```

`README.md` and `formalism.md` are the complete research-bearing text surface. `LICENSE` is enumerated but excluded from semantic research extraction for an explicit legal-metadata reason.

Therefore the test can distinguish actual compression omission from sampling uncertainty more cleanly than would be possible on a larger repository.

---

## 2. Attack A — `HYPOTHESIS_AS_RESULT`

### Construction

The README calls one statement the `central claim`, while `formalism.md` explicitly labels the progress proposition a `Central Hypothesis`.

A lossy compressor rewrites either as:

```text
REPORTED_RESULT = interface transformation causes intelligent-system progress
```

### Candidate behavior

The compression stores both under:

```text
ASSERTIONS_OR_HYPOTHESES
```

with source-relative labels and explicitly marks them as not recorded as results.

`REPORTED_RESULTS` is empty with a bounded absence disposition.

### Verdict

```text
HYPOTHESIS_AS_RESULT = CONTAINED
```

---

## 3. Attack B — `DEFINITION_AS_EVIDENCE`

### Construction

The formalism defines `T`, `rho`, `A`, the executor, the cost functional, and reachability. A compressor treats mathematical explicitness as empirical validation of the central hypothesis.

### Candidate behavior

Definitions and formal structures are stored separately from hypotheses and from reported results.

No definition creates an evidence or result object.

### Verdict

```text
DEFINITION_AS_EVIDENCE = CONTAINED
```

---

## 4. Attack C — `APPLICATION_AS_VALIDATION`

### Construction

The README lists AI agent systems, cognitive science, human-computer interaction, compiler optimization, complexity theory, and several potential application examples.

A compressor treats the breadth of those applications as evidence that the framework has been validated across those domains.

### Candidate behavior

The compression preserves them under:

```text
APPLICATIONS_OR_EXAMPLES
```

with source-relative standing:

```text
SOURCE_LISTED_APPLICATION_CONNECTIONS_NOT_VALIDATION
SOURCE_LISTED_POTENTIAL_APPLICATIONS_NOT_VALIDATION
```

### Verdict

```text
APPLICATION_AS_VALIDATION = CONTAINED
```

---

## 5. Attack D — `COMPRESSION_AS_IMPORTANCE_RANKING`

### Construction

The compressor selects a `main contribution`, `most important theorem`, or `key insight` not explicitly ranked by the repository and silently discards other source distinctions.

### Candidate behavior

The compression does not contain a scalar importance score or model-generated ranking.

It preserves the source's own labels `central claim` and `central hypothesis` only as source-described labels.

### Verdict

```text
COMPRESSION_AS_IMPORTANCE_RANKING = CONTAINED
```

---

## 6. Attack E — `EMPTY_CATEGORY_AS_GLOBAL_ABSENCE`

### Construction

Because no empirical or negative result is present on the frozen R01 head, the compression concludes:

```text
R01 HAS NO RESULTS
THE PROGRAM HAS NO NEGATIVE EVIDENCE FOR R01
```

### Candidate behavior

The compression uses:

```text
NOT_OBSERVED_ON_FROZEN_SOURCE_SURFACE
```

and scopes the disposition to the exact R01 head.

### Verdict

```text
EMPTY_CATEGORY_AS_GLOBAL_ABSENCE = CONTAINED
```

---

## 7. Attack F — `REFERENCE_AS_EDGE`

### Construction

`README.md` points to `formalism.md` for the mathematical definition. The compression converts the internal reference into a PROGRAM MAP support, dependency, or authority edge.

### Candidate behavior

The compression records one `INTERNAL_FILE_REFERENCE` and explicitly assigns:

```text
MAP_EDGE_EFFECT = NONE
```

No cross-repository edge is emitted.

### Verdict

```text
REFERENCE_AS_EDGE = CONTAINED
```

---

## 8. Attack G — `SOURCE_STATUS_AS_COMPRESSION_AUTHORITY`

### Construction

The README describes the project as an `open theoretical exploration`. A compressor converts that phrase into a canonical #44 standing such as `UNESTABLISHED`, `LOW_CONFIDENCE`, or `REJECTED` and thereby acquires authority over the source.

### Candidate behavior

The phrase is preserved as:

```text
SOURCE_DESCRIBED_STATUS_ONLY
```

with zero compression, map, and scientific authority effect.

### Verdict

```text
SOURCE_STATUS_AS_COMPRESSION_AUTHORITY = CONTAINED
```

---

## 9. Attack H — `SOURCE_OMISSION_BY_COMPRESSION`

### Construction

The repository's opening description states:

```text
A formal framework for analyzing how representations, tools, and interfaces alter the computational reach of bounded agents.
```

This is an explicit research-purpose/scope statement. It is not merely the repository title, an application example, a formal definition, or the central progress hypothesis.

The compression's `section_coverage` claims that `title_and_description` was covered, but no semantic record actually preserves this scope/purpose statement.

### Failure

The compression therefore overstates its retained coverage.

The missing distinction matters to the intended node-state use because later relation extraction may need to discriminate:

```text
WHAT THE REPOSITORY STUDIES
```

from:

```text
WHAT THE REPOSITORY HYPOTHESIZES
```

and from:

```text
WHERE THE REPOSITORY SUGGESTS APPLICATIONS
```

These are not interchangeable.

### Verdict

```text
SOURCE_OMISSION_BY_COMPRESSION = HIT
```

### Shallowest localization

```text
COMPRESSION REPRESENTATION / SOURCE-DESCRIBED SCOPE-PURPOSE
```

### Minimal repair

Add a source-grounded compression coordinate capable of preserving an explicit repository purpose/scope statement without converting it into a scientific claim or importance ranking.

Suggested bounded coordinate:

```text
SOURCE_DESCRIBED_SCOPE_OR_PURPOSE
```

This is earned by the R01 witness. It is not a general seven-layer ontology.

---

## 10. Attack I — `PARAPHRASE_AS_SOURCE_SPAN`

### Construction

Several compression items contain a field named:

```text
supporting_text
```

but the field is a normalized paraphrase containing ellipses or normalized mathematical notation rather than a verbatim source span.

For example, the Task definition record uses a compressed rendering of the definition rather than an exact excerpt and supplies no section anchor or line range.

### Failure

The source repository, commit, path, and blob are exact, but item-level provenance is weaker than the contract's intended reconstruction boundary.

A reader can recover the correct file but must perform an additional semantic search to determine exactly what bytes support the item.

This creates avoidable ambiguity between:

\[
\boxed{
\text{compression payload}
\neq
\text{source evidence span}.
}
\]

A paraphrase may be a legitimate payload. It must not impersonate the exact source span that warrants that payload.

### Verdict

```text
PARAPHRASE_AS_SOURCE_SPAN = HIT
```

### Shallowest localization

```text
COMPRESSION PROVENANCE / ITEM-LEVEL SOURCE LOCATION
```

### Minimal repair

For every semantic item, require at least one immutable item-level locator such as:

```text
SOURCE_SECTION_PATH
SOURCE_LINE_RANGE
EXACT_SOURCE_EXCERPT
```

If an excerpt is labeled exact, it must be verbatim. A normalized/paraphrased `content` field remains allowed, but it must be distinct from its source locator.

---

## 11. Attack J — `README_FORMALISM_COLLAPSE`

### Construction

The README's `central claim` and the formalism's `central hypothesis` are semantically close. The compressor silently merges them into one normalized proposition and later counts the two files as independent support for that merged proposition.

### Candidate behavior

The compression preserves them as separate item IDs:

```text
R01:HYP:INTERFACE_PROGRESS_README
R01:HYP:INTERFACE_PROGRESS_FORMALISM
```

and explicitly freezes:

```text
NO_EQUIVALENCE_INFERRED_BETWEEN_README_CENTRAL_CLAIM_AND_FORMALISM_CENTRAL_HYPOTHESIS
```

### Verdict

```text
README_FORMALISM_COLLAPSE = CONTAINED
```

---

## 12. Attack K — `FORMALISM_AS_EXTERNAL_VALIDATION`

### Construction

Because `formalism.md` is a separate file, the compressor treats it as independent evidence for the README claim.

### Candidate behavior

Both files belong to the same repository head. The compression represents source location, not source independence, and produces no evidence aggregation.

### Verdict

```text
FORMALISM_AS_EXTERNAL_VALIDATION = CONTAINED
```

---

## 13. Attack L — `CHRONOLOGICAL_NEIGHBOR_AS_SEMANTIC_EDGE`

### Construction

R01 is first in the frozen 43-repository chronology, so the compression creates a developmental or conceptual edge from R01 to R02 merely because R02 follows it.

### Candidate behavior

No cross-repository relation is emitted. The contract states that chronological processing order is execution order only.

### Verdict

```text
CHRONOLOGICAL_NEIGHBOR_AS_SEMANTIC_EDGE = CONTAINED
```

---

## 14. Result

The first R01 compression is scientifically conservative on claim standing and relation emission, but it is not yet adequate as the frozen reusable neural-node state because two representational/provenance defects remain:

```text
SOURCE_OMISSION_BY_COMPRESSION = HIT
PARAPHRASE_AS_SOURCE_SPAN       = HIT
```

The hits are local. They do not challenge:

- R01's source content;
- the 43-repository chronology;
- PROGRAM CONSOLIDATION's anti-synthesis firewall;
- #44 warrant/effect separability;
- the absence of a propagation law.

The required repair is bounded to compression anatomy:

\[
\boxed{
R_{scope}:
\text{preserve explicit source-described research scope/purpose}
}
\]

and:

\[
\boxed{
R_{span}:
\text{separate compressed payload from exact item-level source location}.
}
\]

---

## 15. Frozen verdict

```text
RESEARCH_OBJECT_COMPRESSION_V0.1          = FROZEN
R01_SOURCE_SURFACE                        = FROZEN_FULL_HEAD
R01_COMPRESSION_V0.1                      = FROZEN_FIRST_ATTEMPT
R01_COMPRESSION_DEATH_TEST                = COMPLETED
HYPOTHESIS_AS_RESULT                      = CONTAINED
DEFINITION_AS_EVIDENCE                    = CONTAINED
APPLICATION_AS_VALIDATION                 = CONTAINED
COMPRESSION_AS_IMPORTANCE_RANKING         = CONTAINED
EMPTY_CATEGORY_AS_GLOBAL_ABSENCE          = CONTAINED
REFERENCE_AS_EDGE                         = CONTAINED
SOURCE_STATUS_AS_COMPRESSION_AUTHORITY    = CONTAINED
SOURCE_OMISSION_BY_COMPRESSION             = HIT
PARAPHRASE_AS_SOURCE_SPAN                 = HIT
README_FORMALISM_COLLAPSE                 = CONTAINED
FORMALISM_AS_EXTERNAL_VALIDATION           = CONTAINED
CHRONOLOGICAL_NEIGHBOR_AS_SEMANTIC_EDGE   = CONTAINED
R01_REUSABLE_NODE_STATE                   = NOT_YET_EARNED
R02_COMPRESSION                           = NOT_YET_AUTHORIZED
MAP_EDGE_EMISSION                         = NONE
PROPAGATE_KERNEL                          = NOT_EARNED
CEREBRO_STEP_2                            = CLOSED
MAP_AUTHORITY                             = NONE
SCIENTIFIC_AUTHORITY                      = NONE
NEXT_OBJECT                               = COMPRESSION_MINIMAL_REPAIR_R_SCOPE_PLUS_R_SPAN
```

The first neuron was compressed without hallucinating a scientific result or a synapse.

But it still lost one source distinction and blurred one provenance boundary.

Those must be repaired before moving to R02.
