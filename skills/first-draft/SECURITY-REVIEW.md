# Skill Inspector review: First Draft

Updated 2026-11-21 after source repairs, asset inspection and authorized runtime tests in `asheshg/skills`.

**Verdict: CAUTION.** The confirmed HTML injection, accidental brand replacement, template fallback and clipped-canvas defects are repaired and covered by regression checks. File writes and third-party document parsing remain sensitive operations; use reviewed inputs and scoped output directories.

## Repairs and evidence

| Area | Current behavior | Verification |
|---|---|---|
| HTML CSS values | Hex colors and plain font-family lists are validated before output. Visible text is escaped. | Script/style closing tags, declarations and CSS escapes rejected without creating output. |
| Brand storage | Existing slugs require a non-overwriting merge; overlapping trees, link escapes and collisions fail before copying. Metadata is preserved. Deletion requires an exact slug and `--yes`. | Disposable store exercises preserved original files, collisions, merge, metadata and deletion confirmation. |
| Manifest writes | Temporary file and atomic replacement protect the old manifest on replacement failure. | Injected disk failure preserves the original JSON and leaves no temporary file. |
| Templates | Selected missing files and LFS pointers fail; theme-specific brand template maps are honored. Output cannot overwrite its template. | Missing/pointer rejection plus light/dark native rendering. |
| Slide content | Dense body/evidence arrays are rejected instead of truncated; notes use the notes pane. Composition scales to template dimensions, and pale visual placeholders have dark text. | Both native variants retain masters/layouts and stay within the canvas; notes and contrast checked. |
| Sanitizer | Source and destination must differ. | Same-file rejection preserves the original bytes. |

Run `python -m unittest discover -s tests -v` from the repository root. Nine regression tests pass. Extraction was also exercised with Markdown, CSV, DOCX, PPTX and PDF synthetic fixtures. Two three-slide PPTX variants rendered in Microsoft PowerPoint and exported to PDF/PNG. HTML rendered in Chromium and exported to a three-page PDF with no content overflow in the sample.

## Assets and provenance

All six assets passed full ZIP/XML/relationship inspection. All 317 slides exported in native PowerPoint with macros disabled and rasterized successfully; contact sheets revealed original source artwork. The owner confirmed permission to retain and redistribute the assets. They are now described as retained branded references, not fully neutralized. See [ASSET-REVIEW.md](ASSET-REVIEW.md) for hashes, counts and boundaries.

## Scanner history and limits

SkillSpector 2.12.0's pre-repair full-package scan returned 59/100, HIGH, DO_NOT_INSTALL, with incomplete coverage after archive/resource limits. A source-only scan returned 53/100 at 60.6% coverage, deliberately omitting sources. Those are historical scores, not results for the repaired code. No suppression baseline was used and no clean automated install certificate is claimed. Manual archive inspection and authorized runtime tests now provide the additional evidence the bounded scan lacked.

The pre-repair AE1 findings concern incomplete template inspection; LP3 concerns file-read/write scope; SC1 concerns minimum-version dependencies; SC4 records offline OSV fallback. A binary RP1 match did not identify a command in executable source. Package names and versions could not receive complete live vulnerability coverage in that restricted scan.

Remaining limits: dependencies are not locked; fonts and import fidelity vary by host; image-based hidden content and legal rights are not independently verified; large or hostile archives are not sandboxed by these helpers. Merge is not transactional: a failed copy may leave newly added files, while collision checks preserve existing files. Keep backups and do not treat the naming sanitizer as a general privacy scrubber. No source installation, global configuration change, or live-site code change is part of these repairs.
