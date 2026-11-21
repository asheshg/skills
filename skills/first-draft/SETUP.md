# Setup

## Install from this repository

Requires an agent with local skill support and Python 3.10 or later. Git LFS is needed when obtaining the bundled PPTX files from GitHub.

Run in PowerShell from the outer repository root. This copies only the chosen skill and refuses to overwrite an existing installation. The installed copy does not automatically follow edits in this workspace.

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillSource = (Resolve-Path 'skills/first-draft').Path
$skillParent = Join-Path $skillHome 'skills'
$skillTarget = Join-Path $skillParent 'first-draft'
if (Test-Path -LiteralPath $skillTarget) { throw "Installation already exists: $skillTarget" }
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse
Set-Location -LiteralPath $skillTarget
```

The installed folder must contain `SKILL.md`, `agents/openai.yaml`, `references/`, and `scripts/` directly. Restart the agent session and invoke `$first-draft`. For Claude Code, use `~/.claude/skills` as the destination parent instead. Other hosts need their own discovery path and tool capabilities.

## Python dependencies and assets

Use an isolated environment inside the installed skill:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Use that interpreter for the helper commands in README.md. Dependency installation accesses the configured Python package index. The requirement versions are lower bounds, not a reproducible lockfile.

Clone `https://github.com/asheshg/skills.git` into a working directory, run `git lfs pull` there, and run the copy procedure from that repository's root. Both skills are under `skills/`; neither is the repository root. The previous standalone repository is retained for history, not the destination for these updates.

Confirm that the bundled light/dark PPTX files are ZIP presentations, not LFS pointer text. Install a licensed Helvetica Neue font or agree on a substitute. Books and the optional consulting skill are not included. Figma Slides requires a connected Figma tool; PDF needs a separate export tool.

## Update and remove

Keep local brands and project outputs backed up separately. Review upstream changes before replacing an installed copy; never overlay a new copy onto confidential brand data. Remove only the individual installed skill folder when uninstalling. No background service or MCP server is installed by these instructions.

## Verification status

Source review was followed by authorized runtime tests on 2026-11-21. See [the security review](SECURITY-REVIEW.md) for source, rendering and asset evidence. A copied installation still needs discovery checks in a new agent session; source validation alone does not establish that the host loaded it.
