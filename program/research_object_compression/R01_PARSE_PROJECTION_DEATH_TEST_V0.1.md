# R01 PARSE-TO-COMPRESSION PROJECTION DEATH TEST V0.1

**Triggering contract amendment:** `RESEARCH_OBJECT_COMPRESSION_V0.1_AMENDMENT_002.md`  
**R01 exhaustive parse:** `R01_EXHAUSTIVE_PARSE_V0.1.json`  
**R01 effective compression before this test:** base compression + Amendment 001  
**Record type:** projection-accountability regression test  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

The stronger projection rule requires every R01 parse unit to have an auditable compression destination while preserving standing-relevant source provenance.

## Result

Most R01 parse units map cleanly to existing compression items or explicit exclusions. However four README Core Model units expose a source-provenance loss:

```text
R01:P:README:CORE_MODEL:TASK
R01:P:README:CORE_MODEL:INTERFACE
R01:P:README:CORE_MODEL:ARCHITECTURE
R01:P:README:CORE_MODEL:REACHABILITY
```

The effective compression preserves their normalized semantics in:

```text
R01:DEF:TASK
R01:DEF:INTERFACE
R01:DEF:ARCHITECTURE
R01:FORMAL:REACHABILITY
```

but those compressed items cite only `formalism.md` as source support.

Thus the projection would falsely make the README source-local expression disappear from the compressed derivation history.

\[
\boxed{
\text{semantic redundancy}
\neq
\text{provenance redundancy}.
}
\]

```text
R01_DUPLICATE_SEMANTICS_SOURCE_PROVENANCE_LOSS = HIT
```

**Shallowest locus:** compression projection provenance.

**Minimal repair:** retain the existing compressed semantic item and add the README source locator as an additional provenance branch. No new semantic item, claim, result, or edge is required.

## Other units

The following dispositions are adequate:

- README title -> repository identity;
- opening purpose -> `R01:SCOPE:01`;
- abstract assertions -> existing assertion items;
- README internal reference -> existing internal-reference item;
- applications/examples/status -> existing items;
- README license note -> explicit legal-metadata exclusion;
- formalism definitions/formal structures/hypothesis -> existing items;
- formalism title -> explicit document-title/navigation exclusion.

## Verdict

```text
R01_PROJECTION_LEDGER_COMPLETE = NO
R01_EFFECTIVE_COMPRESSION_INVALIDATED_SCIENTIFICALLY = NO
R01_SEMANTIC_CONTENT_LOSS = NO_DEMONSTRATED
R01_SOURCE_PROVENANCE_BRANCH_LOSS = HIT
R01_REPAIR_SCOPE = FOUR_ADDITIONAL_SOURCE_LOCATORS_ONLY
R02_RETEST = BLOCKED_UNTIL_R01_REPAIR
MAP_AUTHORITY = NONE
SCIENTIFIC_AUTHORITY = NONE
PROPAGATE_KERNEL = NOT_EARNED
```
