# SkillSpector scans

Reviewed scanner: NVIDIA SkillSpector 2.12.0, commit `48e0f942ea1f5fdb7aa096a6f65a0adeda2ecc4e`. The migration review used CPython 3.13.18 because NVIDIA recommends Python 3.12/3.13 for prebuilt YARA wheels.

If uv is already installed, install the reviewed revision into an isolated tool environment:

```powershell
uv tool install --python 3.13 git+https://github.com/NVIDIA/SkillSpector.git@48e0f942ea1f5fdb7aa096a6f65a0adeda2ecc4e
skillspector --version
skillspector scan ./skills/first-draft --no-llm --format json
skillspector scan ./skills/website-competitor-analysis --no-llm --format json
```

Use the executable location printed by uv if its tool directory is not on PATH. The scanner and Python runtime are not bundled in this repository. Existing installations should be checked before creating another.

`--no-llm` prevents LLM analysis of file contents. Dependency coordinates may still be sent to OSV.dev; a restricted network can force offline fallback. The scanner does not execute the target scripts.

On Windows, version 2.12.0 does not support its native `--output` file writer. Capture stdout to a trusted report path instead. Reports can contain source snippets; keep raw reports private and publish only reviewed summaries. Do not scan nested Git/LFS object stores or Python caches as if they were the distributable skill.

Interpret the risk score alongside analysis completeness and source review. Large Office assets may exceed inspection limits; a source-only scan cannot clear omitted assets.

[Upstream installation and usage](https://github.com/NVIDIA/SkillSpector#installation).
