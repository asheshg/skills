# Testing

Run from the repository root with Python 3.10 or later, Git LFS assets downloaded,
and `skills/first-draft/requirements.txt` installed in your chosen environment:

```powershell
python -m unittest discover -s tests -v
python skills/website-competitor-analysis/scripts/validate_manifest.py --self-test
python scripts/inspect_first_draft_assets.py review-artifacts/asset-inventory.json
```

The unittest suite uses disposable brand stores and synthetic decks. Tests must work
without pre-existing ignored output folders. Regression checks cover source preservation,
HTML injection rejection, template validation, canvas bounds, notes and contrast.

GitHub Actions runs these checks with Python 3.10 and Git LFS. Native PowerPoint,
Chromium output review, assistive technology, and cross-app imports are separate
integration checks; CI does not claim to run them. Raw verification files belong
under ignored `review-artifacts/`, not in reusable skill source.
