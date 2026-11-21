# Agent skills

Reusable skills live in `skills/`. Install the complete individual skill folder, not this repository root.

| Skill | Purpose | Setup | Review |
|---|---|---|---|
| [First Draft](skills/first-draft/README.md) | Research-backed presentation storyboards and drafts | [Setup](skills/first-draft/SETUP.md) | [Security review](skills/first-draft/SECURITY-REVIEW.md) |
| [Website Competitor Analysis](skills/website-competitor-analysis/README.md) | Website audits and conditional competitor benchmarks | [Setup](skills/website-competitor-analysis/SETUP.md) | [Security review](skills/website-competitor-analysis/SECURITY-REVIEW.md) |

## Install

Clone this repository, then follow the individual setup guide from its root:

```powershell
git clone https://github.com/asheshg/skills.git skills-source
Set-Location skills-source
```

Copy the complete `skills/<skill-name>` directory into your agent's personal skills directory. Do not copy this repository root as one skill. The setup guides refuse to overwrite existing installations.

## Migration

Both skills are normal folders in this repository, not Git submodules. Original standalone repositories remain intact as historical sources. First Draft's six Python helpers matched published commit `cef19e81b56e5fecf728eb63a8c4e3e7c8ec44fd` before migration. The website skill includes local framework/validator work newer than published commit `0e7d39cfd6f668ba1983610bd0c20081689c4812`.

Git LFS is required for the bundled PowerPoint files. Existing third-party rights and per-skill licenses still apply; this repository does not grant a new blanket license. See each skill's review before use.

See [MIGRATION.md](MIGRATION.md) for source commits, exclusions, verification, and remaining risks.
