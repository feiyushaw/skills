---
name: faithful-paper-translation
description: Translate English academic papers into faithful Chinese reading versions. Use for full-paper, section, paragraph, caption, table, or equation-adjacent translation when fidelity to the source is the priority. Preserve scientific claims, logical strength, terminology, notation, citations, numbers, and document structure. Do not summarize, explain, simplify, or add interpretation unless explicitly requested.
---

# Faithful Paper Translation

## Mission

Produce a Chinese version that preserves what the source paper actually says.

Priority order:

```text
fidelity > completeness > terminology consistency > readability > elegance
```

This skill is for **translation**, not literature review, interpretation, critique, or rewriting.

## Use when

- translating a full English paper into Chinese for reading;
- translating a section, paragraph, figure/table caption, appendix, or supplementary text;
- producing aligned bilingual notes;
- checking an existing Chinese translation against the English source.

Do not use this skill when the user mainly wants a summary, research map, novelty analysis, or explanation. Route those tasks to `literature-research`, `literature-scout`, or the appropriate reasoning skill.

## Non-negotiable fidelity rules

1. Do not omit source claims, conditions, caveats, limitations, or negative results.
2. Do not add explanations, examples, causal mechanisms, motivations, or conclusions that are absent from the source.
3. Preserve claim strength. Examples:
   - `may` / `might` / `can` must not become certainty;
   - `suggests` must not become `proves`;
   - correlation must not become causation.
4. Preserve logical relations: cause, contrast, condition, concession, scope, chronology, and uncertainty.
5. Preserve all numerical values, units, symbols, equation references, figure/table references, and citation markers.
6. Preserve terminology consistently. Prefer the established Chinese technical term; retain the English term on first occurrence when ambiguity is possible.
7. Do not silently repair scientific inconsistencies in the source. If the source appears inconsistent, translate faithfully and flag the issue separately.
8. Do not turn translation into a summary. Every meaningful source segment must remain represented.

## Workflow

```text
source acquisition
→ structure detection
→ terminology lock
→ segment-by-segment translation
→ completeness audit
→ claim-strength audit
→ notation/citation/number audit
→ readable Chinese assembly
```

### 1. Structure detection

Identify headings, paragraphs, equations, captions, tables, footnotes, appendices, and references before translating long documents.

When source extraction is imperfect, reconstruct only obvious PDF line-break artifacts. Do not infer missing scientific content.

### 2. Terminology lock

Before a long translation, establish a compact glossary for recurring terms, abbreviations, methods, variables, and domain-specific phrases.

Use `references/fidelity-and-terminology.md` for the audit policy.

### 3. Translation

Translate at paragraph or coherent semantic-unit level. Preserve the original argument order by default.

Sentence restructuring is allowed only when required for grammatical Chinese, and must not alter emphasis, scope, or logical dependency.

### 4. Completeness audit

For substantial translations, compare source segments against translated segments and check for:

- missing sentences or clauses;
- dropped caveats or conditions;
- skipped captions/tables/footnotes;
- missing citations or equation references;
- accidental compression.

### 5. Scientific fidelity audit

Check separately for:

```text
claim-strength drift
causal-strength drift
scope drift
terminology drift
numerical drift
notation drift
citation drift
added interpretation
```

## Output modes

Support three modes when useful:

### Chinese reading version

Clean Chinese text preserving the original section structure.

### Bilingual aligned version

```text
[Source]
...

[中文]
...
```

Use for difficult passages, terminology-sensitive sections, or translation review.

### Translation audit

Return only suspected fidelity issues with the corresponding source and translation segments.

## Handoff

- explain what the paper means → `literature-research` or direct explanation after translation;
- compare papers / build a research map → `literature-research`;
- test whether a close prior work kills novelty → `literature-scout`;
- translate the user's Chinese manuscript into academic English → `chinese-to-academic-english`.
