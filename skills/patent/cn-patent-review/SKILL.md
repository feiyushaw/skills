---
name: cn-patent-review
description: Review Chinese software/AI invention-patent drafts for claim scope, support, clarity, disclosure sufficiency, technical-subject-matter framing, and consistency before professional filing review.
---

# CN Patent Review

Use this skill to challenge a draft rather than merely polish language. Use `references/cnipa-baseline.md` as a working baseline and verify current rules before filing-quality conclusions.

## Review order

1. reconstruct the claimed invention from independent claims;
2. verify specification support;
3. test unnecessary narrowing;
4. test missing essential mechanisms;
5. test algorithm/software technical framing;
6. test fallback claim coverage;
7. check terminology and figures;
8. compare against prior-art findings if available.

## Independent-claim review

Label every limitation `ESSENTIAL`, `FALLBACK`, `IMPLEMENTATION`, `RESULT_ONLY`, `UNSUPPORTED`, or `AMBIGUOUS`, then propose a revised feature skeleton before prose edits.

## Support review

| Claim | Feature | Specification support | Embodiment support | Risk | Action |
|---|---|---|---|---|---|

Flag broad genus terms supported by only one narrow example when alternatives are not explained.

## Software/AI checks

Check technical origin of data, data/state transformation, algorithm/system interaction, technical effect, model construction/training/inference details when material, input/output relation to the concrete scene, and enablement detail.

## Prior-art robustness

If a search report exists, identify closest reference, retain the distinguishing nucleus, ensure effect support, and build commercially meaningful fallback levels. Do not add arbitrary differences just to evade one reference.

## Review output

```markdown
# Patent Draft Review — <Candidate ID>
## Executive assessment
## Critical defects
## Independent-claim feature audit
## Support matrix
## CN software/AI examination risks
## Prior-art robustness
## Scope unnecessarily lost
## Missing fallback positions
## Disclosure gaps
## Terminology / consistency issues
## Recommended revision order
```

Use severity `S0` (filing blocker), `S1` (major), `S2` (improvement). Never guarantee allowance/validity or invent missing embodiments.
