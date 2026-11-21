# First Draft

A Codex skill that turns research and brand guidelines into presentation storyboards, then builds the selected draft. It combines consulting argument structures with design-storytelling principles while keeping claims tied to research.

## Install

Follow [SETUP.md](SETUP.md) for installation, isolated Python dependencies, LFS assets, and updates. In this workspace the skill is `skills/first-draft`. The shared GitHub repository is `asheshg/skills`; copy this individual skill folder after cloning.

## Use in Codex

Attach or identify research files, then invoke:

```text
Use $first-draft with the attached research for a leadership decision on our
service redesign. Propose three narrative options for a 10-slide deck.
Use the bundled light template and Helvetica Neue regular.
After I select a storyboard, generate PowerPoint and printable HTML.
```

Provide the audience, intended decision/outcome, approximate length, output format, and brand guidelines or template. The skill can reuse a retained brand or store a new one. It proposes 2-4 distinct storyboards with evidence, layouts, visuals, and gaps. You choose a storyboard and formats before deck generation.

Research may include PDFs, DOCX, PPTX, Markdown, text, CSV/TSV, and images for visual inspection. The extractor produces limited text previews; it does not OCR scans or analyze the research by itself. Codex must review sources and build the evidence map.

## Outputs and limits

| Target | Current behavior |
|---|---|
| PowerPoint | Editable draft; preserves template masters/layouts in Home > Layout |
| Google Slides | PPTX for import; import fidelity needs checking |
| HTML | Printable 16:9 text and visual-placeholder draft |
| PDF | Separate browser print/export from HTML |
| Figma Slides | Requires an available Figma Slides tool in the active session |

The local renderers are draft builders. Charts, tables, and images are labeled placeholders rather than completed visuals. PowerPoint content uses fixed positions rather than automatically filling every template layout. Verify spacing, inherited placeholders, contrast, font availability, and content completeness before presenting. See [runtime limits](references/runtime-limits.md).

The bundled editorial light/dark templates default to Helvetica Neue regular. Prefer relevant designed layouts; blank layouts are a last resort. A retained custom brand can supply its own fonts and template rules.

## Local helpers

Run from the installed skill directory. Codex normally prepares the deck spec after storyboard selection; see [the spec reference](references/deck-spec.md).

```powershell
python scripts/brand_store.py list
python scripts/extract_research.py "C:\path\research.pdf" --out "C:\path\project\research-notes.json"
python scripts/render_pptx.py "C:\path\project\deck-spec.json" --out "C:\path\project\draft.pptx" --template "C:\path\template.pptx"
python scripts/render_html_deck.py "C:\path\project\deck-spec.json" --out "C:\path\project\draft.html"
```

For a new retained brand:

```powershell
python scripts/brand_store.py add "C:\path\brand-package" --name "Example Brand" --slug example-brand
```

Adding an existing slug is refused. `--merge` adds new files and refuses collisions; it does not replace files. `delete <slug> --yes` explicitly confirms permanent removal of the retained folder. Back up retained brands first; a failed merge may leave newly copied files, while existing files are preserved. Brand uploads are stored inside `sources/brands/<slug>/`; keep confidential uploads out of public commits. Selection happens in the conversation/deck spec, not through a separate CLI command.

## References

- [Skill instructions](SKILL.md): agent workflow and output standards.
- [Brand extraction](references/brand-extraction.md): normalize brand rules and catalog layouts.
- [Narrative frameworks](references/narrative-frameworks.md): choose an argument and audience journey.
- [Writing pass](references/storytelling-writing.md): revise slide copy.
- [Book sources](references/book-sources.md): attribution and historical access status.

Books, proprietary fonts, and the separate consulting skill are not bundled. Distilled references remain available without those files; direct book consultation requires access to the source. No license grant for third-party materials is implied by this guide.

## Maintenance and review

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY-REVIEW.md](SECURITY-REVIEW.md).

## Verified safety and runtime behavior

See [ASSET-REVIEW.md](ASSET-REVIEW.md) for full archive inspection and native rendering of all 317 retained asset slides. Original branded artwork remains with owner-confirmed redistribution permission. Nine regression checks cover the repaired write/render boundaries; run them from the shared repository root as documented in CONTRIBUTING.md.
