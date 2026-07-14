# camp-index

The registry data for **camp**, a community-governed plugin repository for
Moodle: one YAML file per plugin, an append-only release ledger, and signed
security advisories. This repository is the source of truth — cloning it
mirrors the registry's brain (RFC §4.1).

- **Browse plugins:** rendered website and Composer metadata are generated
  from this tree (`make dist`).
- **Plugin authors:** the claim-to-publish path is
  [AUTHORS.md](https://github.com/camp-registry/camp-docs/blob/main/AUTHORS.md) —
  steady state is pushing a git tag.
- **The RFC and design docs:** [camp-registry/camp-docs](https://github.com/camp-registry/camp-docs)
- **The `camp` CLI:** [camp-registry/camp-tools](https://github.com/camp-registry/camp-tools)
- **The Moodle client plugin:** [camp-registry/moodle-tool_camp](https://github.com/camp-registry/moodle-tool_camp)

Every pull request is verified by CI (RFC §4.2): schema validation,
append-only ledger enforcement, deterministic rebuild from the tagged
source, hash verification, static checks, and malware scanning.

Status: **pre-launch**. Discovered listings (Tier 0) are search results,
not distributions — maintainers may claim them, or request removal, no
questions asked.
