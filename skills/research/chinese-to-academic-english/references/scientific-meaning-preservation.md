# Scientific Meaning Preservation

Use this reference when translating Chinese manuscript text into academic English.

## Meaning-preservation audit

For each paragraph, record mentally or explicitly:

```text
paragraph role
main scientific statement
supporting evidence/reasoning
qualification / uncertainty
scope / conditions
terminology / notation locks
```

After translation, verify these remain unchanged.

## Common failure modes

### 1. Claim inflation

Chinese:

> 结果表明该方法具有一定鲁棒性。

Unsafe:

> The results demonstrate that the method is highly robust.

The English adds both certainty and degree.

### 2. Invented comparison

Do not add `outperforms`, `superior`, `state-of-the-art`, or `competitive` unless the Chinese source or supplied evidence makes that comparison.

### 3. Causal inflation

Chinese statements such as `与...相关`, `伴随着`, or `在...条件下观察到` must not become `causes`, `leads to`, or `results from` without support.

### 4. Scope broadening

Do not turn a result observed for one benchmark, parameter range, mesh resolution, dataset, or experimental setting into a universal statement.

### 5. Hidden interpretation

Do not insert mechanistic explanations merely to improve paragraph flow. If an explanation is scientifically useful but absent from the Chinese source, suggest it separately rather than embedding it in the translation.

## Academic English policy

Prefer:

- standard technical terms;
- concrete scientific subjects;
- precise verbs;
- explicit logical connectors only when supported;
- concise syntax;
- stable terminology.

Avoid:

- ornamental phrases with little semantic content;
- unnecessary claims of novelty or importance;
- generic phrases such as `It is worth noting that` when the sentence can state the point directly;
- excessive `clearly`, `obviously`, `remarkably`, `significantly` unless justified;
- literal Chinese sentence order when it produces awkward English.

## Relationship to academic-writer

Translation ends when the Chinese scientific meaning has been faithfully rendered as natural English.

If the user then asks to reorganize paragraphs, strengthen section flow, rewrite an Introduction, or revise a Method section according to a paper blueprint, hand off to `academic-writer` rather than silently expanding the translation task.
