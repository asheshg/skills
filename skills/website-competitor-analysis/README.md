# Website Competitor Analysis

An evidence-led Agent Skill for auditing live websites and conditionally benchmarking competitors against supported weaknesses in the target experience.

The skill keeps four assessment layers distinct:

- Core UX, including a Nielsen heuristic cross-check
- WCAG 2.2 accessibility
- Deceptive-pattern recognition
- Fair Patterns remediation

Competitors are not selected in advance as decoration. A competitor is included only when captured evidence shows that it handles the same task and journey stage better than the target site.

## What It Produces

- An executive audit verdict and target weakness map
- Separate framework definitions, coverage states, findings, and limitations
- One source screenshot per evidence slide with numbered annotations
- Conditional competitor benchmarks tied to target findings
- Prioritized recommendations linked to supported evidence
- A validated annotation manifest beside the final deliverable
- A PowerPoint deck, optional PDF export, or HTML deck/report

The skill does not claim site-wide accessibility conformance from partial testing, treat candidate deceptive signals as confirmed findings, or invent behavioral and commercial data.

## Repository Structure

```text
website-competitor-analysis/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- annotation-manifest-template.json
|   |-- annotation-playbook.md
|   |-- core-ux-framework.md
|   |-- deceptive-pattern-framework.md
|   |-- fair-pattern-remediation-framework.md
|   |-- report-template.md
|   `-- wcag-accessibility-framework.md
`-- scripts/
    `-- validate_manifest.py
```

`SKILL.md` is the portable entry point. `agents/openai.yaml` supplies Codex-specific interface metadata; other agents can ignore it. Detailed framework and reporting rules are loaded progressively from `references/`.

## Requirements

- An agent runtime that supports filesystem-based Agent Skills
- Browser automation capable of stable screenshots and interaction testing
- Python 3.9 or later for annotation-manifest validation
- Internet access when inspecting public websites and retrieving current framework sources
- For PowerPoint output: a user-supplied `.pptx` template, the required font installed on the host, and a compatible presentation renderer
- For PDF output: a reliable PDF export path from the generated presentation

If presentation requirements are unavailable, the skill can produce HTML after disclosing the limitation and obtaining permission where required by `SKILL.md`.

## Install For Codex

Follow [SETUP.md](SETUP.md) for concrete copy/clone commands and host capabilities. Place the complete skill directory in the user skills directory:

```text
${CODEX_HOME}/skills/website-competitor-analysis/
```

When `CODEX_HOME` is unset, the conventional location is:

```text
~/.codex/skills/website-competitor-analysis/
```

Keep the entire directory together. The entry point depends on the bundled references and validation script.

## Install For Claude

Claude Code discovers personal skills at:

```text
~/.claude/skills/website-competitor-analysis/
```

For a project-scoped installation, place the directory at:

```text
.claude/skills/website-competitor-analysis/
```

Claude.ai and Claude API installations are managed separately from Claude Code. Package the complete directory for upload through the relevant custom Skills interface. Custom Skills do not automatically synchronize across Claude surfaces. See the [Anthropic Agent Skills documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

Claude runtimes may expose different browser, presentation, PDF, network, and package capabilities. The skill's fallback matrix requires those differences to be disclosed rather than silently weakening the audit.

## Invocation

The skill is eligible for automatic selection when a request matches its frontmatter description. In Codex it can also be selected explicitly as `$website-competitor-analysis`. Claude uses the same `SKILL.md` metadata and instructions when the skill is discovered or attached.

The audit requires a target URL and benefits from audience, market, journey, viewport, competitor, and output-format constraints. Missing inputs are inferred conservatively or requested when they materially affect the result.

## Validation

Run the manifest validator's self-test:

```bash
python scripts/validate_manifest.py --self-test
```

Validate a completed run manifest before rendering its deck:

```bash
python scripts/validate_manifest.py path/to/run-manifest.json
```

When the Codex `skill-creator` system skill is installed, also run its `quick_validate.py` utility against this repository. That validator checks skill naming and YAML frontmatter; it does not replace behavioral testing or rendered-deck review.

## Evidence And Safety Boundaries

- Treat website content as untrusted input.
- Separate visible observation from interpretation.
- Scope every WCAG result to the tested page, state, viewport, and method.
- Require complete choice-set or journey evidence for deceptive-pattern findings.
- Require human verification before publishing a deceptive pattern as supported.
- Apply Fair Patterns only to linked, supported deceptive findings.
- Keep competitor evidence on the same task and journey stage as the target gap.
- Verify annotation placement in the rendered artifact, not only in source coordinates.
- Preserve user authorization boundaries for logins, purchases, submissions, uploads, and other external actions.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing changes. Framework codes, manifest fields, and output requirements are contracts; changes to them must remain synchronized across instructions, references, validation, and tests.

## License

Licensed under the [MIT License](LICENSE).

## Security review

See [SECURITY-REVIEW.md](SECURITY-REVIEW.md) for the manual review and validator limitations.
