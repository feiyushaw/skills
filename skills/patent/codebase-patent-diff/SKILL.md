---
name: codebase-patent-diff
description: Establish repository provenance, public-prior-art boundaries, ownership-aware code deltas, and candidate invention scope before mining patents from software codebases.
---

# Codebase Patent Diff

Use this skill before invention mining whenever the target project is a fork, derivative work, paper-associated repository, vendor SDK integration, open-source adaptation, or a system assembled from multiple public components.

The purpose is not to decide legal ownership. The purpose is to prevent the patent workflow from mistaking pre-existing public technology for the applicant's invention and to identify the actual technical delta that deserves further patent analysis.

## Non-negotiable rule

Never infer inventorship from repository location, account ownership, code complexity, authorship metadata, or the fact that code currently resides in the user's repository.

A mechanism that was already public in an upstream repository, paper, patent, standard, documentation, release, presentation, issue, or other accessible disclosure must be treated as prior-art evidence until a qualified patent professional determines otherwise.

## Required workflow

### Stage 1 — Repository provenance

Establish, when evidence permits, repository ownership/visibility, fork/source relationship, relevant branches, license/third-party notices, associated papers/patents/standards/docs, public dates, imported dependencies, and whether the target is original development, adaptation, mirror, or primarily upstream history. Record unknown facts as `UNKNOWN`.

### Stage 2 — Public disclosure boundary

Build a disclosure timeline:

| Evidence | Source | Public date | Mechanism disclosed | Confidence |
|---|---|---|---|---|

Distinguish upstream public disclosure, applicant/user public disclosure, third-party literature, private implementation evidence, and unverified dates. A Git commit date is engineering evidence, not a complete patent-law conclusion.

### Stage 3 — Ownership-aware technical delta

Prefer comparison against: fork parent at common ancestor; paper/release-associated upstream; imported component version; earlier internal baseline; then conventional architecture from reliable references.

Classify changed mechanisms as:

- `UPSTREAM_PRIOR_ART`
- `THIRD_PARTY_PRIOR_ART`
- `COMMON_ENGINEERING`
- `USER_MODIFICATION`
- `POTENTIAL_INVENTION`
- `UNKNOWN_PROVENANCE`

Do not promote a large diff by size alone.

### Stage 4 — Mechanism graph

For each mechanism capture technical input, transformation, decision/computation, output, downstream use, feedback dependency, provenance class, and evidence path/symbol/commit/document.

### Stage 5 — Combination-invention test

Ask what new information crosses component boundaries, what state is updated, whether one component alters another's operating condition/search/evaluation/control, whether feedback exists, what effect arises from the coupling, and whether simple side-by-side use would produce the same result.

### Stage 6 — Exclusion map

Before `cn-patent-invention-mining`, produce:

```markdown
## Excluded from applicant invention pool
- <mechanism>: upstream/public source + evidence

## Eligible for invention mining
- <mechanism>: user delta + why it may solve a technical problem

## Unresolved provenance
- <mechanism>: missing evidence required
```

## Output: Patent Provenance Matrix

| Mechanism | Technical role | Provenance class | Public evidence | User delta | Patent-candidate status | Evidence |
|---|---|---|---|---|---|---|

Candidate status: `EXCLUDE`, `BACKGROUND_ONLY`, `REVIEW_DELTA`, `CANDIDATE`, or `UNRESOLVED`.

## Fork-specific checks

Inspect parent/source metadata, fork-only commits, copied upstream history, changed files against appropriate upstream ref, README/citations/original authors, and license notices. Never equate fork ownership with inventorship. If no material delta exists, report that result rather than fabricating a candidate.

## Paper-associated repositories

Treat the paper and associated implementation as mutually relevant prior-art sources. Extract the paper's named contribution separately from implementation details and mark explicitly presented contributions as strong `BACKGROUND_ONLY` candidates for downstream adaptations.

## Handoff

Pass only `REVIEW_DELTA`, `CANDIDATE`, and unresolved items requiring user evidence to `cn-patent-invention-mining`, preserving provenance labels and evidence links.
