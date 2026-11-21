# Contributing

`SKILL.md` owns the workflow; `references/` owns conditional guidance; `agents/openai.yaml` owns interface metadata. Keep script flags, dependency requirements, README examples, and setup instructions synchronized.

The shared repository stores this skill under `skills/first-draft`. Keep all references relative to the skill directory and use absolute project/template paths at runtime. Keep Git LFS attributes beside the assets.

Never commit private brands, research uploads, generated decks, books, fonts, browser profiles, or credentials. Sanitizing naming does not establish redistribution rights or remove all private material.

Before release, inspect the diff, validate frontmatter and local links, compile Python source without running it, and check that bundled PPTX assets are real ZIP files. After a separate execution review, test extraction and both renderers with disposable fixtures, check template layouts, and visually inspect output. Test brand replacement/deletion only in a disposable copy. Skill Inspector review itself must not execute the target scripts.

No license for the First Draft source or bundled third-party presentation assets is established here. The owner must confirm rights before publishing or adding a license. Do not copy the website skill's MIT license onto these materials by assumption.
