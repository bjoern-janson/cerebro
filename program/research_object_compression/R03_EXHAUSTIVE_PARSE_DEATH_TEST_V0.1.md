# R03 EXHAUSTIVE PARSE — DEATH TEST V0.1

**Source surface:** `R03_SOURCE_SURFACE_V0.1.json`  
**Parse attempt:** `R03_EXHAUSTIVE_PARSE_V0.1.json`  
**Record type:** held-out parse transport death test  
**Persistent record state:** `FROZEN`  
**Map authority:** `NONE`  
**Scientific authority:** `NONE`

R03 is the first nested, multi-document repository tested under the R01/R02-derived exhaustive parse contract.

The source inventory itself passes recursive coverage: the frozen Git tree is complete and non-truncated, all 18 blobs are inventoried, 17 research-bearing Markdown files are included, and the MIT license is explicitly excluded from semantic parsing.

However, the first parse attempt violates the already-frozen mixed-standing separability rule demonstrated by R02.

## Attack — `MIXED_STANDING_GROUPING_REGRESSION`

A parse unit may group adjacent source material only while the distinctions share a standing that can be compressed without leakage. R03 contains several locations where the first parse attempt grouped semantically distinguishable standings.

Demonstrated examples:

```text
R03:P:012  CORE_PREDICTION + MODEL_STATUS
R03:P:015  ACCESSIBILITY_PROTOCOL + MODEL_FORM_LIMITATION
R03:P:018  PROXY_LIMITATIONS + TEMPORAL/FALSIFICATION_PROTOCOL
R03:P:019  CURRENT_STATUS + REMAINING_TASKS
R03:P:024  SURVIVAL_PROTOCOL + CONCLUSION_CLAIM
R03:P:033  CASE_FALSIFICATION_CRITERIA + CASE_STATUS/ASSESSMENT
R03:P:053  OBSERVED_AGREEMENT + HYPOTHETICAL_KAPPA_INTERPRETATION
R03:P:065  CONSCIOUSNESS_FALSIFICATION + PROGRAM_LINEAGE_CHAIN + FINAL_SCOPE_CONSTRAINT
R03:P:072  FALSE_COMPRESSION_LIMITATION + CURRENT_NAVIGATION_CAPABILITY_CLAIM
R03:P:074  VALIDATION_REQUIREMENT + CURRENT_CORE_HYPOTHESIS + OPEN_QUESTION
R03:P:078  CROSS_DOMAIN_HYPOTHESIS + FALSE_COMPRESSION_LIMITATION
R03:P:079  NEXT_ACTIONS + CONCLUSION_SYNTHESIS
R03:P:083  PROPOSED_FORMALIZATION + EMPIRICAL_QUESTION + FINAL_PRINCIPLE
```

The source blocks may be adjacent or share headings, but R02 already established:

\[
\boxed{\text{source block}\neq\text{epistemic unit}.}
\]

A compressor receiving these grouped units could allow a status statement to inherit hypothesis standing, a limitation to inherit protocol standing, or an interpretive estimate to masquerade as an observed result.

```text
MIXED_STANDING_GROUPING_REGRESSION = HIT
```

**Shallowest locus:** R03 local parse unitization.

No global parser-contract change is earned because the existing contract already requires mixed-standing separation.

## Contained attacks

```text
RECURSIVE_DIRECTORY_AS_UNENUMERATED_SURFACE = CONTAINED
CASE_NUMBER_GAP_AS_NEGATIVE_HISTORY         = CONTAINED
SOURCE_SPECULATION_AS_CORE_CPB_CLAIM        = CONTAINED
NAMED_IICG_AS_RESOLVED_R01_ENDPOINT         = CONTAINED
SOURCE_VALIDATION_LABEL_AS_PROGRAM_STANDING = CONTAINED
```

## Verdict

```text
R03_SOURCE_SURFACE                    = FROZEN_FULL_RECURSIVE_HEAD
R03_FIRST_EXHAUSTIVE_PARSE            = FROZEN_FAILED_FIRST_ATTEMPT
R03_PARSE_APERTURE                    = ADEQUATE
MIXED_STANDING_GROUPING_REGRESSION    = HIT
GLOBAL_PARSE_CONTRACT_CHANGE_REQUIRED = NO
R03_LOCAL_PARSE_REPAIR_REQUIRED       = YES
R03_COMPRESSION                       = NOT_AUTHORIZED_UNTIL_RETEST
R04_ACCESS                            = NOT_AUTHORIZED
MAP_AUTHORITY                         = NONE
SCIENTIFIC_AUTHORITY                  = NONE
PROPAGATE_KERNEL                      = NOT_EARNED
```
