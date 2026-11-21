# Contributing

Contributions should improve audit reliability without turning individual audit preferences or isolated failures into universal rules.

## Before Making Changes

1. Read `SKILL.md` and the reference file that owns the behavior being changed.
2. Confirm that the change belongs in the portable skill rather than a specific audit run.
3. Keep `SKILL.md` concise and move conditional detail into the relevant reference.
4. Preserve existing authorization, evidence, accessibility-claim, and human-verification boundaries.

## Contract Ownership

- `SKILL.md` owns routing, workflow, essential constraints, and fallback behavior.
- `references/core-ux-framework.md` owns Core UX codes and scoring.
- `references/wcag-accessibility-framework.md` owns WCAG statuses and claim limits.
- `references/deceptive-pattern-framework.md` owns deceptive-pattern IDs and evidence thresholds.
- `references/fair-pattern-remediation-framework.md` owns remediation IDs.
- `references/annotation-manifest-template.json` owns the evidence-manifest shape.
- `references/annotation-playbook.md` owns screenshot and pin-placement rules.
- `references/report-template.md` owns deck order and format requirements.
- `scripts/validate_manifest.py` enforces machine-checkable manifest invariants.

Do not duplicate framework registries or schemas in multiple files. Update the owning file and its consumers together.

## Change Guidelines

- Use lowercase, stable framework identifiers.
- Add new framework codes only when their definition, detection rule, counter-evidence, and source are explicit.
- Do not convert partial checks into conformance claims.
- Do not publish candidate deceptive signals as supported findings.
- Keep competitor selection conditional on a supported target weakness.
- Keep public documentation brand-neutral and free of client or audit-run artifacts.
- Avoid committing generated decks, screenshots, browser profiles, or site-specific manifests to this repository.
- Keep agent-specific metadata optional so `SKILL.md` remains portable across compatible runtimes.

## Validation

Run these checks before opening a pull request:

```bash
python scripts/validate_manifest.py --self-test
```

Validate any changed or newly created manifest fixture with:

```bash
python scripts/validate_manifest.py path/to/manifest.json
```

If the Codex `skill-creator` validator is available, run `quick_validate.py` against the skill directory. For changes affecting deck construction or annotation rules, render a complete audit artifact and visually verify screenshot fidelity, pin placement, text overflow, source notes, and layout preservation.

## Pull Requests

A pull request should state:

- the reliability problem being solved;
- the files that own the changed contract;
- the validation performed;
- any runtime-specific behavior or remaining limitation.

Keep unrelated generated files and audit outputs out of the change.
