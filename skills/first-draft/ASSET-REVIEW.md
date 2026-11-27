# First Draft asset review

Reviewed 2026-11-21. The repository owner confirmed permission to redistribute all six assets after being shown the retained source-brand artwork. Permission is owner-attested, not independently verified licensing evidence.

## Inspection results

| File | Slides | ZIP members | XML parts | External hyperlinks | SHA-256 |
|---|---:|---:|---:|---:|---|
| image-delivery-guidelines.pptx | 22 | 270 | 250 | 1 | `d1d487f1a4f921402446e9ae2003e6570d79e25e3144b51627ed6a08c177102b` |
| representation-guidelines.pptx | 49 | 387 | 345 | 34 | `9df46e609a7a12e1af79ecc7c27f7e08705a5ff42e9022fdefb35747c86705d9` |
| visual-guidelines.pptx | 23 | 227 | 186 | 11 | `b51ad14fb742a0a4d297aa3681173a0503b955b1b3beabd186b7d7a410c15020` |
| voice-guidelines.pptx | 18 | 961 | 919 | 1 | `b2d194e51e84cce56ed7c4dc0c3694d9a36172dd6c07f4ee0a16de8585a14be5` |
| editorial-slides-template-dark.pptx | 99 | 635 | 559 | 0 | `3505be412a791c1203c8dfaa9969234067619685e5354d3b006c04299d26ae01` |
| editorial-slides-template-light.pptx | 106 | 665 | 587 | 0 | `0d67f1e79310aa45b2881993c1741f429ab6144b7f9be2a10e03fe630f752051` |

All 3,145 ZIP members were integrity-checked. Every XML/relationship part was parsed. No VBA projects, ActiveX controls, embedded objects, archive traversal paths, DTD/entity declarations, or unexpected external target schemes were found. All 47 external relationships are ordinary hyperlinks; none was followed during inspection. The two templates have no external relationships.

At the original review, all 317 slides exported through native Microsoft PowerPoint with macros disabled. The template hashes above reflect the later wordmark replacement. Every exported PDF page rasterized with PyMuPDF; all pages were reviewed at contact-sheet resolution. This checks renderability and broad visual content, not full-resolution OCR, image steganography, forensic malware analysis, or font fidelity on other hosts.

## Discrepancy resolved in documentation

The two presentation templates use a generic wordmark. The template and guideline assets may still contain source imagery or sample photography. They are retained branded references, not fully neutralized templates. Naming substitution does not establish privacy scrubbing or remove embedded brand imagery. Do not promise a brand-neutral output without checking the selected layout and inherited graphics.

## Reproduce

Run `python scripts/inspect_first_draft_assets.py review-artifacts/asset-inventory.json` from the repository root. The scanner reads every archive member without executing Office content. Native PowerPoint exports and local contact sheets are verification artifacts and are not committed.
