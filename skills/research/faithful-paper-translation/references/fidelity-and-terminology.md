# Fidelity and Terminology Audit

Use this reference for long or terminology-sensitive academic translation.

## Fidelity checklist

For each translated unit, verify:

- all source propositions are represented;
- negation and comparison direction are unchanged;
- modality and uncertainty are unchanged;
- causal language is not strengthened;
- scope qualifiers such as `under`, `for`, `within`, `except`, `only`, and `in this study` are preserved;
- quantitative values, units, ranges, percentages, p-values, and signs are unchanged;
- citations, equation numbers, figure/table references, and variable names remain traceable;
- no explanatory sentence has been inserted into the translation.

## Claim-strength ladder

Do not move upward without explicit source support:

```text
speculates / hypothesizes
< may / might / could
< suggests / indicates
< supports / is consistent with
< shows / demonstrates
< proves / establishes
```

Treat this ladder as approximate; preserve the source verb rather than mechanically mapping levels.

## Terminology policy

1. Prefer established Chinese technical terminology.
2. On first occurrence, retain the English term in parentheses when:
   - multiple Chinese translations exist;
   - the term is field-specific;
   - the English form will be useful for later literature search.
3. Keep abbreviations stable after definition.
4. Do not translate proper method names, dataset names, software names, symbols, or variable identifiers inconsistently.
5. Maintain a compact glossary for long papers.

Example glossary:

| Source term | Preferred Chinese | Notes |
|---|---|---|
| inverse problem | 逆问题 | do not alternate with “反问题” unless requested |
| finite element method (FEM) | 有限元方法（FEM） | abbreviation retained |
| ill-posed | 不适定 | preserve technical meaning |

## PDF-specific caution

PDF extraction can introduce:

- line-break fragmentation;
- hyphenated words split across lines;
- headers/footers inside paragraphs;
- caption/body interleaving;
- equation tokens detached from sentences.

Repair only layout artifacts that are evident from context. Never invent missing scientific text.
