# First Draft asset review

Reviewed 2026-11-21. The repository owner confirmed permission to redistribute all six assets after being shown the retained source-brand artwork. Permission is owner-attested, not independently verified licensing evidence.

## Inspection results

| File | Slides | ZIP members | XML parts | External hyperlinks | SHA-256 |
|---|---:|---:|---:|---:|---|
| image-delivery-guidelines.pptx | 22 | 270 | 250 | 1 | `d1d487f1a4f921402446e9ae2003e6570d79e25e3144b51627ed6a08c177102b` |
| representation-guidelines.pptx | 49 | 387 | 345 | 34 | `9df46e609a7a12e1af79ecc7c27f7e08705a5ff42e9022fdefb35747c86705d9` |
| visual-guidelines.pptx | 23 | 227 | 186 | 11 | `b51ad14fb742a0a4d297aa3681173a0503b955b1b3beabd186b7d7a410c15020` |
| voice-guidelines.pptx | 18 | 961 | 919 | 1 | `b2d194e51e84cce56ed7c4dc0c3694d9a36172dd6c07f4ee0a16de8585a14be5` |
| editorial-slides-template-dark.pptx | 99 | 635 | 559 | 0 | `937e3a522f4a282f5f374112f34f43c4b1a7d7f8b7b8abc5779858eb5f171a04` |
| editorial-slides-template-light.pptx | 106 | 665 | 587 | 0 | `10862c9d29f464b1f4e80327cd629ad35d4ff9cf60e4ffbb78bea22ef96af30d` |

All 3,145 ZIP members were integrity-checked. Every XML/relationship part was parsed. No VBA projects, ActiveX controls, embedded objects, archive traversal paths, DTD/entity declarations, or unexpected external target schemes were found. All 47 external relationships are ordinary hyperlinks; none was followed during inspection. The two templates have no external relationships.

All 317 slides exported through native Microsoft PowerPoint with macros disabled. Every exported PDF page rasterized with PyMuPDF; all pages were reviewed at contact-sheet resolution. This checks renderability and broad visual content, not full-resolution OCR, image steganography, forensic malware analysis, or font fidelity on other hosts.

## Discrepancy resolved in documentation

The assets still contain original SPACE10 logo artwork and sample photography. They are retained branded references, not fully neutralized templates. Naming substitution does not establish privacy scrubbing or remove embedded brand imagery. Do not promise a brand-neutral output without checking the selected layout and inherited graphics.

## Reproduce

Run `python scripts/inspect_first_draft_assets.py review-artifacts/asset-inventory.json` from the repository root. The scanner reads every archive member without executing Office content. Native PowerPoint exports and local contact sheets are verification artifacts and are not committed.
