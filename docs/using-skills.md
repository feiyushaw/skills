# Using the skill monorepo

## Discover skills

```bash
python3 scripts/list-skills.py
python3 scripts/list-skills.py --domain research
python3 scripts/list-skills.py --json
```

The canonical human-readable overview is `docs/catalog.md`.

## Validate the repository

```bash
python3 scripts/validate-skills.py
```

Validation checks:

- `skills/<domain>/<name>/SKILL.md` layout;
- lowercase kebab-case and globally unique skill names;
- frontmatter `name` / `description`;
- pack references to existing skills and packs;
- pack manifest names;
- pack include cycles.

## Install a pack

The repository does not hard-code a Codex, Claude Code, or other agent directory because those conventions may differ by product/version. Pass the destination explicitly:

```bash
python3 scripts/install-pack.py engineering --target /path/to/agent/skills
python3 scripts/install-pack.py research --target /path/to/agent/skills
python3 scripts/install-pack.py full --target /path/to/agent/skills
```

Preview first:

```bash
python3 scripts/install-pack.py full --target /path/to/agent/skills --dry-run
```

By default skills are copied. During local development you may use symlinks:

```bash
python3 scripts/install-pack.py engineering \
  --target /path/to/agent/skills \
  --mode symlink
```

Use `--force` only when replacing an existing installed skill intentionally.

## Stable vs experimental

`full` includes the stable `engineering`, `research`, `presentation`, `patent`, and `productivity` packs. It intentionally excludes `experimental`.

Install experimental skills explicitly:

```bash
python3 scripts/install-pack.py experimental --target /path/to/agent/skills
```

## Development rule

A new skill should enter a stable pack only when its boundary, invocation behavior, handoff, and completion criteria are clear. New ideas can live in `experimental` until repeated use justifies promotion.
