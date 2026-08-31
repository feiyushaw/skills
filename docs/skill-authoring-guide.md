# Skill Authoring Guide

## Minimum structure

```text
skills/<domain>/<name>/
  SKILL.md
```

Recommended when relevant:

```text
  agents/openai.yaml
  references/
  templates/
  scripts/
```

## SKILL.md frontmatter

Every skill starts with:

```yaml
---
name: skill-name
description: Describe when to use the skill, what it accomplishes, and important boundaries.
---
```

The `name` must equal the directory basename.

## Write for invocation reliability

The description is a routing surface. Include recognizable situations that should trigger the skill and, when useful, conditions that should not trigger it.

Prefer a small number of standard domain terms over creative synonyms.

## Write for execution reliability

A useful skill normally defines:

1. mission / outcome;
2. inputs the agent should inspect;
3. workflow stages;
4. decision points;
5. persistent output artifacts;
6. completion criteria;
7. important failure modes or prohibited shortcuts.

Do not add sections merely to make the file look complete.

## Facts and decisions

If a fact can be established by inspecting files, tools, logs, source code, documentation, or public sources, the agent should investigate it. Ask the user when a genuine preference, tradeoff, authorization, or unresolved product/research decision is required.

## Progressive disclosure

Keep rules used on nearly every execution in `SKILL.md`. Put specialized reference tables, examples, detailed domain guidance, and templates under the local skill directory and point to them from the relevant step.

## Completion criteria

Each multi-step workflow should make it clear when the current stage is complete. Avoid instructions such as `review carefully` without saying what evidence indicates completion.

## Invocation policy

For substantial user-controlled orchestrators:

```yaml
interface:
  display_name: "Readable Name"
  short_description: "Short action-oriented description"
policy:
  allow_implicit_invocation: false
```

For reusable model-invoked primitives, omit the policy block unless there is a reason to forbid implicit invocation.

## Self-containment

A skill installed by itself must retain the files required for its own behavior. Another skill may be an explicit optional dependency, but repository-global hidden references are prohibited.

## Provenance

When adapting third-party material:

- verify the upstream license;
- preserve required notices;
- record the source in `THIRD_PARTY_NOTICES.md`;
- record local changes when the adaptation is substantial.

When migrating from a private repository to a public destination, verify publication approval before copying content.
