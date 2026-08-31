---
name: chinese-to-academic-english
description: Translate Chinese scientific manuscript text into natural, publication-ready academic English while preserving the scientific argument. Use when the user writes the paper in Chinese first and wants English manuscript prose. Sentence-level restructuring is allowed for idiomatic academic English, but scientific claims, evidence, scope, uncertainty, terminology, notation, citations, and paragraph intent must not be changed or strengthened.
---

# Chinese to Academic English

## Mission

Convert an already formed Chinese scientific argument into natural academic English without changing the science.

Priority order:

```text
scientific meaning preservation
> claim/evidence fidelity
> idiomatic academic English
> concision and flow
> stylistic polish
```

This skill is a **translation-and-discourse adaptation layer**, not a novelty generator or hidden paper architect.

## Boundary with `academic-writer`

Use this skill when the source of truth is a Chinese manuscript or Chinese scientific paragraph.

Use `academic-writer` when the task is to draft or substantially revise English prose from an approved paper blueprint, evidence, and section contract.

Do not silently redesign the paper, add scientific arguments, add citations, invent advantages, or strengthen results during translation.

## Core rule

> The English version may restructure sentences, but must not restructure the scientific argument unless explicitly requested.

## Preserve exactly

- scientific claims and their strength;
- observation vs interpretation vs hypothesis vs speculation;
- causal vs correlational statements;
- scope, conditions, exceptions, and limitations;
- experimental facts and quantitative results;
- technical terminology and abbreviations;
- mathematical notation, variable names, equations, and units;
- citation keys and reference placement when possible;
- figure/table/equation references;
- paragraph-level scientific intent.

## Allowed adaptation

To produce natural academic English, you may:

- reorder clauses within a sentence;
- split overloaded Chinese sentences;
- merge short repetitive sentences when meaning is unchanged;
- replace Chinese discourse habits with standard English scientific syntax;
- make grammatical subjects explicit;
- choose standard field terminology;
- remove literal Chinese redundancy that has no scientific content.

Do not use these permissions to change the argument structure or introduce new claims.

## Workflow

```text
Chinese source
→ scientific meaning lock
→ terminology / notation lock
→ claim-strength classification
→ English translation
→ discourse adaptation
→ sentence-flow audit
→ scientific fidelity audit
→ final academic English
```

Use `references/scientific-meaning-preservation.md` for the fidelity audit.

### 1. Scientific meaning lock

Before translating substantial text, identify:

- the paragraph's scientific job;
- its main claim or observation;
- evidence or reasoning supporting it;
- qualifications and limitations;
- terms and notation that must remain stable.

### 2. Translation

Translate for meaning rather than Chinese word order. Prefer standard academic constructions and standard technical terms.

Avoid ornamental academic language. Do not increase formality by replacing precise simple verbs with vague inflated phrases.

### 3. Discourse adaptation

English paragraphs should normally make the paragraph role visible early and maintain explicit logical relations between sentences.

However, do not add transitions that imply a stronger causal or argumentative relation than the Chinese source contains.

### 4. Fidelity audit

Check for:

```text
added claim
missing condition
claim-strength inflation
causal-strength inflation
scope change
terminology drift
number / unit drift
citation or notation damage
paragraph-intent change
```

## Translation examples

Chinese source:

> 数值结果表明，该方法在较粗网格下仍能较好地重构缺陷区域。

Acceptable:

> Numerical results show that the proposed method can reconstruct the defective region accurately even on relatively coarse meshes.

Not acceptable unless supported elsewhere:

> The proposed method significantly outperforms existing approaches and enables highly accurate defect reconstruction on coarse meshes.

The second version invents a comparison and strengthens the claim.

## Output modes

### Clean manuscript English

Return only the translated academic English when the user wants text ready to place in the manuscript.

### Bilingual review mode

For difficult or high-stakes passages:

```text
[中文原文]
...

[English]
...

[Fidelity notes]
...
```

Use fidelity notes only for material ambiguities or translation decisions.

### Translation audit mode

Compare an existing English version against the Chinese source and flag scientific-meaning drift without rewriting unrelated prose.

## Handoff

- scientific logic or contribution is still unstable → `research-idea-refiner` / `paper-architect`;
- English section needs broader drafting/revision after translation → `academic-writer`;
- evidence does not support the translated claim → `experiment-designer`;
- translate an English paper into Chinese → `faithful-paper-translation`;
- near-complete manuscript risk audit → `manuscript-review`.
