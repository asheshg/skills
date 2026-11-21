# Contributing

`SKILL.md` owns the workflow; `references/` owns conditional guidance; `agents/openai.yaml` owns interface metadata. Keep script flags, dependency requirements, README examples, and setup instructions synchronized.

The shared repository stores this skill under `skills/first-draft`. Keep all references relative to the skill directory and use absolute project/template paths at runtime. Keep Git LFS attributes beside the assets.

Never commit private brands, research uploads, generated decks, books, fonts, browser profiles, or credentials. Sanitizing naming does not establish redistribution rights or remove all private material.

Before release, inspect the diff, validate frontmatter and local links, compile Python source without running it, and check that bundled PPTX assets are real ZIP files. After a separate execution review, test extraction and both renderers with disposable fixtures, check template layouts, and visually inspect output. Test brand replacement/deletion only in a disposable copy. Skill Inspector review itself must not execute the target scripts.

The owner confirmed permission to redistribute the six bundled presentation assets on 2026-11-21; see ASSET-REVIEW.md for the inspected inventory and the limits of that attestation. This does not establish a general source or third-party license. Confirm rights for new assets before publishing them or adding a license. Do not copy the website skill's MIT license onto these materials by assumption.

## Checks

From the shared repository root:

```powershell
python -m unittest discover -s tests -v
python scripts/inspect_first_draft_assets.py review-artifacts/asset-inventory.json
```

Tests use disposable brand stores and synthetic deck content. Asset inspection is read-only. Native PowerPoint, Chromium, PDF and live-site evidence are integration checks recorded separately; unit tests do not establish their results.
