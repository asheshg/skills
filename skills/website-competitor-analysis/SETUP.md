# Setup

## Install from this repository

Requires an agent with local skill support and Python 3.9 or later. The validator uses only the Python standard library. No requirements file, MCP configuration, or package installation is needed.

Run in PowerShell from the outer repository root. This copies only the chosen skill and refuses to overwrite an existing installation. The installed copy does not automatically follow edits in this workspace.

```powershell
$skillHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $env:USERPROFILE '.codex' }
$skillSource = (Resolve-Path 'skills/website-competitor-analysis').Path
$skillParent = Join-Path $skillHome 'skills'
$skillTarget = Join-Path $skillParent 'website-competitor-analysis'
if (Test-Path -LiteralPath $skillTarget) { throw "Installation already exists: $skillTarget" }
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillTarget -Recurse
Set-Location -LiteralPath $skillTarget
```

The installed folder must contain `SKILL.md`, `agents/openai.yaml`, `references/`, and `scripts/` directly. Restart the agent session and invoke `$website-competitor-analysis`. For Claude Code, use `~/.claude/skills` as the destination parent instead. Other hosts need their own discovery path and tool capabilities.

Clone `https://github.com/asheshg/skills.git` into a working directory and run the copy procedure from that repository's root. Both skills are under `skills/`; neither is the repository root. The previous standalone repository is retained for history, not the destination for these updates.

## Host capabilities

Supply browser automation for screenshots and interactions. Presentation generation is performed by the agent's available tools, not by a bundled renderer. PPT requires an explicit user template, Helvetica Neue Regular, and a presentation builder. PDF requires an export path. HTML still requires the agent to author the report.

Run helpers from the installed skill folder, or use absolute paths:

```powershell
python scripts/validate_manifest.py --self-test
python scripts/validate_manifest.py C:\audit\run-manifest.json
```

These commands are for use after source review. A successful manifest validation does not verify screenshot files, source truth, complete schema coverage, or rendered pin placement. The manifest template is intentionally incomplete and should fail validation until populated.

## Update and remove

Keep local brands and project outputs backed up separately. Review upstream changes before replacing an installed copy; never overlay a new copy onto confidential brand data. Remove only the individual installed skill folder when uninstalling. No background service or MCP server is installed by these instructions.

## Verification status

Source review was followed by authorized validator and live-browser tests on 2026-11-21. A copied installation still needs discovery checks in a new agent session. See [the security review](SECURITY-REVIEW.md); validator success does not establish full audit coverage or host discovery.
