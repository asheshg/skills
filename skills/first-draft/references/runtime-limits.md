# Runtime Capabilities and Limits

Read before extracting research or generating artifacts.

## Setup and paths

- Install `requirements.txt` with the Python interpreter used to run the scripts. Python 3.10 or newer supports the syntax used here.
- Script/reference paths are relative to the skill directory. Renderer template paths are currently resolved from the process working directory; use absolute paths in project specs and `--template`.
- Fetch bundled PPTX files with Git LFS. A small text file starting with `version https://git-lfs.github.com/spec/v1` is a pointer, not a presentation. Run `git lfs pull` in the clone before using those templates.
- Helvetica Neue is not bundled or embedded by these scripts. Install a licensed copy on machines displaying/exporting the deck or agree on a substitute; assigning the font name alone does not ensure faithful display.

## Research extraction

The extractor writes source text previews, not claims or a synthesized evidence map. The agent must perform that analysis. PDF extraction requires pypdf and does not OCR scanned pages. Images are recorded for separate inspection. DOCX/PPTX extraction reads XML text and does not preserve full visual context. CSV/TSV extraction previews only the first 31 rows. Text is capped at 12,000 characters per text file, 2,500 per PDF page, 3,000 per Office XML part, and 5,000 for a tabular preview.

Check original files for omitted material. Empty notes or warnings are evidence gaps, never proof that a source contains no relevant findings. Use visual inspection/OCR when available; otherwise disclose unreadable pages and request accessible content if it blocks the work. Compute quantitative claims from the full dataset, not the preview.

## Rendering

The PPTX helper preserves the selected template's masters and layout collection. It chooses a layout, then adds text and labeled visual placeholders at fixed widescreen positions. It does not automatically populate each layout's placeholder geometry, draw real charts/tables, place image files, or enforce content capacity. It currently keeps at most six body items and three evidence/footer entries; reject or split excess content before calling it. Speaker notes are currently added to visible footer content rather than PowerPoint's notes pane.

Verify an explicit template exists and is a real PPTX before rendering: the helper can otherwise fall back silently to the bundled default or a generic presentation. If the selected template is missing, report the problem instead of delivering a fallback as brand compliant. Review chosen layouts for relevance; the first nonblank layout is only a heuristic fallback. Inspect slides for inherited placeholders, overlap, contrast, and clipping. Preserved layouts alone do not demonstrate that the slide composition follows the template.

The HTML helper produces a fixed 16:9 printable draft with text and visual-description placeholders. It does not reproduce PowerPoint layouts. Set the brand fonts explicitly. PDF requires a separate browser print/export step; do not report a PDF as generated until the PDF exists and has been checked.

Treat both renderers as draft builders. For finished charts, imagery, template-specific composition, or real speaker notes, add those elements with an appropriate available tool and inspect the resulting artifact. Clearly label remaining placeholders and unverified visual fidelity at delivery.

## Optional integrations and books

Figma Slides requires an available Figma Slides creation/editing tool; inspect current capabilities rather than assuming a particular tool name. If unavailable, offer an available format and obtain the user's format choice. Google Slides-compatible means PPTX import, not a native Google Slides file or guaranteed import fidelity.

The references contain distilled book concepts. Full books and fonts are not distributed. Paths and access reports in `book-sources.md` describe the original author's machine and historical source inspection, not files guaranteed on a new installation. Retrieve the actual source when direct consultation is requested, and disclose unavailable books without inventing attribution.
