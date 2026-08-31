---
name: cn-patent-prior-art
description: Search and analyze prior art for Chinese invention-patent candidates using feature decomposition, Chinese/English terminology, patent classifications, claim mapping, and novelty/inventive-step analysis.
---

# CN Patent Prior Art

Use after invention mining and before final claim drafting. Use `references/cnipa-baseline.md` as a working baseline and verify current examination rules before filing-quality conclusions.

## Goal

Determine what appears known, where the strongest prior-art pressure lies, and which feature combination should anchor the application. This is patentability-oriented search, not a freedom-to-operate opinion.

## Required inputs

Candidate ID, technical problem, core mechanism, essential/optional features, known products/papers/patents, and earliest relevant internal/public disclosure date if known.

## Search preparation

### Feature decomposition

Break the candidate into atomic and relational features. The inventive unit may be a relationship among known features rather than any term alone.

### Bilingual terminology

Build Chinese patent-style terms, common Chinese engineering terms, English patent-style terms, academic/industry synonyms, broader and narrower terms. Avoid only internal naming.

### Classification expansion

Identify likely IPC/CPC neighborhoods when useful and validate them against sample results.

## Search ladder

Search from exact mechanism combinations to two-feature combinations, core feature + domain, core feature without domain, known assignees/competitors + mechanism, then papers/standards/product docs/open source. Prefer primary sources.

## Date handling

Record priority, filing, publication, and non-patent public disclosure dates. Do not compare only publication years.

## Claim mapping

| Feature | Candidate | Reference disclosure | Exact / inferred / absent | Evidence |
|---|---|---|---|---|

Summarize whether one reference discloses all essentials, remaining differences, technical effect of differences, and combination motivation.

## Inventive-step framing

Use closest prior art → distinguishing features → supported technical effect → objective technical problem → reason a skilled person would or would not arrive at the combination. Do not manufacture effects after seeing prior art.

## Search report output

```markdown
# <Candidate ID> Prior-Art Report
## Candidate summary
## Search date and databases/sources
## Search terminology
## Classification strategy
## Strong references
## Feature comparison matrix
## Novelty assessment
## Inventive-step pressure
## Features worth moving into independent claim
## Features better kept dependent
## Drafting traps revealed by prior art
## Additional evidence/tests to capture
## Search limitations
```

State limitations rather than claiming exhaustive search. Hand the selected claim nucleus and comparison matrix to `cn-patent-drafting`.
