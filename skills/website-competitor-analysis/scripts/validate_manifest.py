"""Validate an audit annotation manifest before deck rendering."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRAMEWORK_STATES = {
    "tested-with-findings",
    "tested-no-supported-findings",
    "partially-tested",
    "not-tested",
}
SCREENSHOT_ROLES = {"target-gap", "competitor-benchmark", "recommendation", "source"}


def registry() -> dict[str, set[str]]:
    sources = {
        "core-ux": ("references/core-ux-framework.md", r"\|\s*([A-Z]{2}\d)\s*\|"),
        "wcag-2.2-aa": ("references/wcag-accessibility-framework.md", r"\b(\d\.\d\.\d{1,2})\b"),
        "deceptive-patterns": ("references/deceptive-pattern-framework.md", r"\|\s*(DP-[A-Z]{3}-\d{2})\s*\|"),
        "fair-patterns": ("references/fair-pattern-remediation-framework.md", r"\|\s*(FP-\d{2})\s*\|"),
    }
    return {
        name: set(re.findall(pattern, (ROOT / path).read_text(encoding="utf-8")))
        for name, (path, pattern) in sources.items()
    }


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    codes = registry()
    frameworks = data.get("frameworks", {})
    for name in ("core-ux", "wcag-2.2-aa", "deceptive-patterns"):
        state = frameworks.get(name, {}).get("state")
        if state not in FRAMEWORK_STATES:
            errors.append(f"frameworks.{name}.state is invalid: {state!r}")
    fair_state = frameworks.get("fair-patterns", {}).get("state")
    if fair_state not in FRAMEWORK_STATES | {"not-invoked"}:
        errors.append(f"frameworks.fair-patterns.state is invalid: {fair_state!r}")

    slides = data.get("slides", [])
    if not slides:
        errors.append("slides must contain at least one evidence slide")
    for slide in slides:
        label = f"slide {slide.get('slide', '?')}"
        if slide.get("screenshot_role") not in SCREENSHOT_ROLES:
            errors.append(f"{label}: invalid screenshot_role")
        dims = slide.get("screenshot_dimensions", {})
        if not isinstance(dims.get("width"), int) or dims.get("width", 0) <= 0:
            errors.append(f"{label}: screenshot width must be a positive integer")
        if not isinstance(dims.get("height"), int) or dims.get("height", 0) <= 0:
            errors.append(f"{label}: screenshot height must be a positive integer")

        pins: set[int] = set()
        for finding in slide.get("findings", []):
            pin = finding.get("pin")
            prefix = f"{label}, pin {pin!r}"
            if not isinstance(pin, int) or pin < 1:
                errors.append(f"{prefix}: pin must be a positive integer")
            elif pin in pins:
                errors.append(f"{prefix}: duplicate pin")
            else:
                pins.add(pin)
            for axis in ("x_percent", "y_percent"):
                value = finding.get(axis)
                if not isinstance(value, (int, float)) or not 0 <= value <= 100:
                    errors.append(f"{prefix}: {axis} must be between 0 and 100")
            for field in ("title", "description", "recommendation", "source"):
                if not finding.get(field):
                    errors.append(f"{prefix}: missing {field}")

            supported_deceptive = False
            framework_results = finding.get("framework_results", [])
            if not framework_results:
                errors.append(f"{prefix}: at least one framework_result is required")
            for result in framework_results:
                framework = result.get("framework")
                code = result.get("code")
                if framework not in ("core-ux", "wcag-2.2-aa", "deceptive-patterns"):
                    errors.append(f"{prefix}: unknown framework {framework!r}")
                    continue
                if code not in codes[framework]:
                    errors.append(f"{prefix}: unknown {framework} code {code!r}")
                if framework in ("wcag-2.2-aa", "deceptive-patterns") and not result.get("reference"):
                    errors.append(f"{prefix}: {framework} result requires a reference")
                if framework == "wcag-2.2-aa" and not result.get("verification_method"):
                    errors.append(f"{prefix}: WCAG result requires verification_method")
                if framework == "deceptive-patterns" and result.get("result") in ("supported", "verified"):
                    supported_deceptive = True
                    if result.get("verified_by_human") is not True:
                        errors.append(f"{prefix}: supported deceptive result requires human verification")
                    if not finding.get("user_harm"):
                        errors.append(f"{prefix}: supported deceptive result requires user_harm")

            remediations = finding.get("remediations", [])
            if supported_deceptive and not remediations:
                errors.append(f"{prefix}: supported deceptive result requires remediation")
            if remediations and not supported_deceptive:
                errors.append(f"{prefix}: remediation requires a supported deceptive result")
            for remediation in remediations:
                code = remediation.get("code")
                if code != "custom" and code not in codes["fair-patterns"]:
                    errors.append(f"{prefix}: unknown Fair Pattern code {code!r}")

            if slide.get("screenshot_role") == "competitor-benchmark":
                if not finding.get("target_gap") or not finding.get("competitor_benchmark"):
                    errors.append(f"{prefix}: competitor benchmark requires target_gap and competitor_benchmark")
                if finding.get("same_task_verified") is not True or not slide.get("journey_stage"):
                    errors.append(f"{prefix}: competitor benchmark requires same task and journey stage")
    return errors


def self_test() -> int:
    data = {
        "frameworks": {
            "core-ux": {"state": "tested-with-findings"},
            "wcag-2.2-aa": {"state": "partially-tested"},
            "deceptive-patterns": {"state": "tested-with-findings"},
            "fair-patterns": {"state": "tested-with-findings"},
        },
        "slides": [{
            "slide": 1,
            "screenshot_role": "target-gap",
            "screenshot_dimensions": {"width": 1440, "height": 1000},
            "findings": [{
                "pin": 1,
                "x_percent": 50,
                "y_percent": 50,
                "title": "Hidden recurring charge",
                "description": "Recurrence is absent beside the purchase action.",
                "recommendation": "Disclose recurrence before commitment.",
                "source": "example.com checkout, desktop, captured YYYY-MM-DD, manual review",
                "user_harm": "The user may enter a recurring payment unintentionally.",
                "framework_results": [
                    {"framework": "core-ux", "code": "IN1", "result": "2"},
                    {
                        "framework": "deceptive-patterns",
                        "code": "DP-SNK-03",
                        "result": "supported",
                        "reference": "https://webtransparency.cs.princeton.edu/dark-patterns/",
                        "verified_by_human": True,
                    },
                ],
                "remediations": [{"code": "FP-02"}],
            }],
        }],
    }
    assert validate(data) == []
    data["slides"][0]["findings"][0]["x_percent"] = 101
    assert any("x_percent" in error for error in validate(data))
    print("OK: self-test")
    return 0


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        return self_test()
    if len(sys.argv) != 2:
        print("usage: validate_manifest.py <manifest.json> | --self-test", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
