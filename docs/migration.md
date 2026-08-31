# Migration Record

PR2 performs the first real consolidation into `feiyushaw/skills` after the bootstrap architecture was approved and merged.

## Completed migrations

### Research

Source: `feiyushaw/academic_skills` at `b03a7651300081b9d292630fe50bb8c4be8d2007`.

Destination: `skills/research/`.

The research lifecycle and claim-evidence discipline were preserved. Skill-local references, templates, and scripts required for standalone operation were migrated with their parent skills.

### Patent

Source: `feiyushaw/patent_skills` at `be8f362d72a3f1df4058cccf8b39f3b75ab62b49`.

Destination: `skills/patent/`.

The mandatory provenance gate was preserved. The previously repository-level CNIPA baseline was localized into the relevant skills so individual installation does not create broken references. The Guidance Planner provenance regression was moved under `cn-patent-invention-mining/examples/`.

### Presentation

Source: `feiyushaw/presentation_skill` at `0bcae01f201c8edac4b9243ffa38534d9b9c7a5d`.

Destination: `skills/presentation/`.

The existing Slidev skill and its core docs were made self-contained under local references. A new tool-independent `presentation-architect` separates story/slide design from rendering.

### Matt Pocock engineering/productivity adaptations

Source: `mattpocock/skills` at `6654f6b60cd9d5be8b54c6fafe44346dabeb3b76`.

Adapted rather than blindly copied. Matt-specific setup, tracker configuration, and personal routing were removed. High-value reusable behaviors were mapped into the monorepo invocation/artifact conventions.

See `THIRD_PARTY_NOTICES.md` for licensing and the exact adaptation set.

## Legacy repositories

The source repositories remain intact as historical sources. Do not archive/delete them until the monorepo has been exercised and downstream references have been updated.

## Future migration work

- update legacy READMEs to point to the canonical monorepo after V1 stabilizes;
- decide whether to preserve historical examples such as the full MDOC presentation project in a dedicated examples repository/directory;
- add automated pack installation and dependency validation;
- add regression fixtures for high-value engineering/research workflows.
