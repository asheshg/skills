# Skill Inspector review: First Draft

Date: 2026-11-21. Source: local `skills/first-draft`, including pre-existing uncommitted changes. Published source: `asheshg/first-draft`; the local origin still uses the redirected old owner URL. published main was verified at `cef19e81b56e5fecf728eb63a8c4e3e7c8ec44fd`. GitHub access succeeds outside the restricted shell sandbox.

**Verdict: CAUTION.** Manual source assessment only; the automated install gate remains blocked pending complete asset inspection. Do not use arbitrary third-party deck specifications as trusted renderer input.

## Review evidence

SkillSpector 2.12.0 is installed. The migrated full-package scan returned **59/100, HIGH, DO_NOT_INSTALL**, exit 2, with **0.7% complete component coverage** after resource and archive limits. The separately scoped source scan returned **53/100, HIGH, DO_NOT_INSTALL**, with **60.6% coverage**; it deliberately omitted `sources/*`. Neither is installation clearance. Manual review covered SKILL.md, agent metadata, all six Python helpers, requirements, brand manifest, and referenced runtime/brand/spec guidance. Target scripts were not executed.

| Surface | Finding | Required control |
|---|---|---|
| Installation | Local outer checkout uses `skills/first-draft`; published standalone repository already has a root entry point. The original published clone instructions were valid. | Use SETUP.md and copy only the skill folder. |
| Dependencies | python-pptx and pypdf use minimum versions without a lockfile. | Install in a venv and review resolved versions for releases. |
| Brand writes | `brand_store.py:add_brand` deletes an existing slug before copying. `--merge` can replace same-named child directories. Using a source inside its destination can lose source data. | Back up brands, use disjoint source/destination paths, and confirm replacement/deletion. This behavior remains in code. |
| HTML | `render_html_deck.py` escapes visible text but interpolates raw font and color values into a style element. A malicious value can close that element and inject markup/script or cause remote fetches. | Only render agent-reviewed brand tokens. This is an unresolved code issue for untrusted specs, not a sanitization guarantee. |
| Templates | `resolve_template` silently falls back if a requested file does not exist; layouts use fixed geometry and truncated body/footer lists. | Verify the chosen file first and inspect outputs; see runtime-limits.md. |
| Sanitization | `sanitize_pptx.py` replaces particular brand strings in XML; it is not a general privacy scrubber. | Inspect embedded media, metadata, links, notes, and rights separately before sharing. |
| Publication | No First Draft license was found. Third-party templates and guidelines are bundled. | Owner must establish redistribution rights; renaming materials does not establish those rights. |

No network client, credential reader, subprocess launcher, persistence hook, or obfuscated payload was found in the Python helpers. Package installation and optional connected tools have their own network behavior. This observation does not cover all content embedded in bundled Office assets.

## Setup changes

Added a dedicated setup guide, contributor guide, review report, and outer repository index. Corrected installation instructions, added isolated environment exclusions, and made the agent's input and destructive-write boundaries explicit. Existing helper behavior and existing user edits were preserved.

## Validation and limits

Static checks inspect Python syntax, internal Markdown file links, required entry points, JSON files, and bundled PPTX ZIP integrity. They do not prove rendering, font fidelity, dependency compatibility, book access, or installation discovery in a fresh agent session. No install, package download, publish, or target-script execution was performed.

## Migration scope

The shared repository contains only skill source, references, agent metadata, and bundled brand assets. Nested Git metadata, Python caches, smoke outputs, empty working assets, and local tools are excluded. Earlier scans describe the original working folders; the clean migrated folders are rescanned separately.

## Scanner triage

| Rule | Severity | Location | Judgment |
|---|---|---|---|
| AE1 | HIGH | SKILL.md:24, two template references | Both targets are present, but scanner limits prevented full inspection. This remains an open coverage limitation, not a proven malicious payload and not a cleared finding. |
| LP3 | MEDIUM | SKILL.md:1 | Helpers read chosen inputs and write outputs/retained brands. The capability fits the purpose; host permissions still need enforcement. |
| RP1 | MEDIUM | representation-guidelines.pptx | Matched a short package-runner-looking byte sequence in a binary archive. No corresponding command was found in the executable helpers; embedded asset inspection remains incomplete. |
| SC1 | LOW | requirements.txt:1-2 | Both dependencies have minimum versions rather than exact pins. Use an isolated environment; this is not a reproducible dependency lock. |
| SC4 | LOW | requirements.txt | Live OSV lookup was unavailable from the restricted scan process. Offline fallback does not establish current CVE coverage. |

Raw migrated scan and source-only scan reports are retained in the original workspace's ignored `review-artifacts/` directory. Earlier scans against nested Git/LFS metadata were superseded and are not release evidence. This summary was updated after scanning; no suppression baseline was used. No scanned skill code was executed.
