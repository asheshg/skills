# Skill Inspector review: Website Competitor Analysis

## Historical static review

Date: 2026-11-21. Source: local `skills/website-competitor-analysis`, including pre-existing uncommitted changes. This is a separate Git checkout, published as `asheshg/website-competitor-analysis`; its local origin still uses the redirected old owner URL. Published main was verified at `0e7d39cfd6f668ba1983610bd0c20081689c4812`. It has the older combined assessment framework, no validator, and no split WCAG/deceptive/fair framework references. The reviewed local version is ahead of that publication.

**Verdict: CAUTION.** The skill's browser access and evidence capture fit its purpose, but require user-authorized interactions, private-data redaction, and human review of published deceptive-pattern findings.

## Review evidence

SkillSpector 2.12.0 is now installed locally and completed a migrated static-only scan: **73/100, HIGH, DO_NOT_INSTALL**, with 16/16 components inspected under its analysis profile. The earlier working-folder scan scored 48/100. The increase comes from the report quoting the same P6/MP3 matches, which are counted again. All occurrences were reviewed in context; none was suppressed. This report was updated after scanning. Manual source review covered the entry point, agent metadata, sole Python validator, manifest template, seven framework/report references, and contributor instructions. Target scripts were not executed.

| Surface | Finding | Resolution or limitation |
|---|---|---|
| Installation | Root layout is valid for standalone installation; the surrounding workspace now stores it under `skills/`. | SETUP.md documents cloning the shared repository and copying the individual skill folder. |
| Runtime | No presentation renderer or browser is bundled. | Setup explicitly lists required host capabilities; no unnecessary dependency manifest or MCP server was added. |
| Paths | Workflow taught a relative script path that fails outside the installed skill directory. | Entry point now resolves script/reference paths from the skill directory. |
| Validator | Checks codes, states, coordinates, selected finding fields, remediation and benchmark relationships. It accepts some incomplete records, does not validate the full schema, and malformed structures may raise exceptions. | The entry point and setup guide now state its limited scope. Manual review remains required; validation success alone is not release clearance. |
| Evidence | Screenshot existence, URL truth, capture date, one-image rendering, and placement verification are not established by the validator. | Verify these against original captures and rendered output. Do not set human verification flags merely to pass validation. |
| Browser | Audited pages may contain prompt injection or private session data; interaction can change external state. | Entry point now explicitly preserves authorization boundaries and requires private-data redaction. |
| Frameworks | Referenced websites and methodology may change. | Retrieve current primary sources during an actual audit; this setup review did not revalidate external framework content. |

The validator reads a selected JSON manifest and bundled reference files; no shell execution, network client, environment/credential access, persistence, or hidden external transmission was found in it. The agent's browser and export tools are separate permission surfaces.

## Setup changes

Added setup and security-review guides, linked them from the README, clarified install alternatives, excluded local virtual environments, and corrected overstated validation coverage. Kept framework registries and manifest schema unchanged.

## Validation and limits

Static checks cover Python syntax, local Markdown links, required entry points, and JSON parsing. The validator's self-test, a live website audit, generated reports, PowerPoint fidelity, browser permissions, and fresh-session discovery were not executed or verified. The blank manifest template intentionally requires real audit data before it can pass validation.

## Scanner finding review

| Rule | Severity | Location at scan time | Source-aware judgment |
|---|---|---|---|
| P6 | HIGH | SKILL.md:24 | Matches the phrase `output rules` in the description of the report reference. It describes deck formatting, not disclosure of a system prompt. False positive after reading the surrounding instructions. |
| MP3 | HIGH | references/deceptive-pattern-framework.md:41 | Matches `clear state` inside `clear state change`, an exclusion for a disclosed UI transition. It does not clear or modify agent memory. False positive after checking the full taxonomy row. |
| LP3 | MEDIUM | SKILL.md:1 | The local validator reads a chosen manifest and bundled references without an explicit portable tool-scope declaration. File access fits its purpose; the host must enforce permissions. Adding preapproved tools just to silence the warning would not establish confinement. |

Raw scan: `review-artifacts/website-competitor-analysis-skillspector.json` in the outer workspace, excluded from Git. The scanner's complete flag refers to supported static analysis, not live audit correctness or full binary/visual verification.

## Migration scope

The shared repository contains only skill source, references, agent metadata, and bundled brand assets. Nested Git metadata, Python caches, smoke outputs, empty working assets, and local tools are excluded. Earlier scans describe the original working folders; the clean migrated folders are rescanned separately.

The migrated scan adds P6 and MP3 occurrences in this review's explanation table at lines 35-36. They quote the original matches for triage, not executable instructions. The original P6/MP3 source locations and the LP3 warning remain unchanged. The numeric recommendation is retained above; the manual CAUTION verdict reflects this source-aware review and is not a replacement scanner score.

## Subsequent authorized runtime validation — 2026-11-21

The static-review statements above describe the earlier review stage and original standalone publication. The current source is maintained in asheshg/skills under skills/website-competitor-analysis. Subsequently, the validator self-test and a completed PwC annotation manifest passed, and the generated HTML report was rendered with annotation placement checked. Authorized desktop/mobile visits covered the PwC global homepage and its linked AI page, necessary-only cookies, and navigation/search panels. No forms were submitted. This was a scoped audit, not full WCAG or screen-reader certification. Fresh installation/discovery and a repaired-input scanner run remain separate release checks; historical scanner scores above do not describe those results.
