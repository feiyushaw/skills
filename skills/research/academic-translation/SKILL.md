---
name: academic-translation
description: Translate academic and scientific text between English and Chinese while preserving scientific meaning. Use EN→ZH faithful-reading mode for papers and ZH→EN manuscript mode for publication-oriented translation. Do not change claims, evidence, scope, uncertainty, terminology, notation, citations, or scientific argument unless explicitly requested.
---

# Academic Translation

## Mission

Provide one translation entry point for scientific work while keeping two clearly different modes.

```text
English source paper → faithful Chinese reading version
Chinese manuscript     → publication-ready academic English
```

Translation is a language transformation layer. It must not silently become literature review, scientific interpretation, novelty generation, paper architecture, or claim revision.

## Mode A — EN → ZH faithful reading

Use when the source of truth is an English paper, section, paragraph, caption, table, appendix, or equation-adjacent text.

Priority:

```text
fidelity > completeness > terminology consistency > readability > elegance
```

Preserve the source structure and argument order by default. Do not summarize, explain, simplify, repair, or strengthen the paper unless separately requested.

Read `references/en-to-zh-fidelity.md` for the detailed fidelity and terminology audit.

## Mode B — ZH → EN manuscript

Use when the source of truth is a Chinese scientific manuscript or Chinese research paragraph that should become natural academic English.

Priority:

```text
scientific meaning preservation
> claim/evidence fidelity
> idiomatic academic English
> concision and flow
> stylistic polish
```

Sentence-level restructuring is allowed when needed for idiomatic English, but the scientific argument and claim strength must remain unchanged.

Read `references/zh-to-en-meaning-preservation.md` for the detailed meaning-preservation audit.

## Shared workflow

```text
source
→ identify translation direction
→ lock terminology / notation / citations
→ classify claim strength and uncertainty
→ translate by coherent semantic unit
→ discourse adaptation allowed by the selected mode
→ completeness audit
→ scientific-fidelity audit
→ final translated text
```

## Shared hard constraints

Preserve:

- scientific claims and their strength;
- observation vs interpretation vs hypothesis vs speculation;
- causal vs correlational relations;
- scope, conditions, exceptions, and limitations;
- quantitative values, units, variables, equations, figure/table references;
- citations and citation keys;
- terminology and notation consistency.

Flag source inconsistencies separately instead of silently fixing them.

## Handoff

- Need to understand or compare literature → `literature-research`.
- Need to redesign the paper argument → `paper-architect`.
- Need to draft or substantially rewrite prose from evidence/blueprint → `academic-writer`.
- Need to change scientific claims because evidence changed → route upstream to `engineering-research` or `research-idea-refiner` first.
