# Audit Deck Template

Use this as the client-facing structure. Keep format decisions and internal process metadata out of the deck.

## Required Sequence

1. Cover: target, audit scope, date.
2. Executive audit verdict: strongest evidence-backed gaps and priorities.
3. Framework map: purpose, source, scope, and execution state for Core UX, WCAG 2.2, Deceptive Patterns, and Fair Patterns.
4. Core UX definitions: canonical parameters used in the audit. Detailed decks show the complete registry across as many template layouts as needed.
5. Core UX coverage and target weakness map.
6. Core UX evidence slides.
7. WCAG 2.2 definition and claim limits.
8. WCAG coverage: pages/processes, methods, and criterion counts by status.
9. WCAG evidence slides.
10. Deceptive Patterns definition and canonical taxonomy.
11. Deceptive Patterns coverage: choice sets/journeys tested and findings by status.
12. Deceptive-pattern evidence slides.
13. Fair Patterns remediation, only for supported deceptive findings. Otherwise show `not invoked` on the framework map and omit this chapter.
14. Consolidated target gaps.
15. Conditional gap-to-benchmark matrix.
16. Competitor evidence slides, only where a competitor is better on the same task and journey stage.
17. Prioritized recommendations.
18. Sources and limitations.

## Framework Map

| Framework | Purpose | Source | Scope | State | Limitation |
|---|---|---|---|---|---|

Allowed diagnostic states: `tested-with-findings`, `tested-no-supported-findings`, `partially-tested`, and `not-tested`. Fair Patterns may use `not-invoked`.

Do not omit a diagnostic framework because it has no findings. Its state and limitations remain visible.

## Core UX Chapter

Use only codes from `core-ux-framework.md`.

| Code | Parameter | Definition | What good looks like | Common failure | Nielsen heuristic |
|---|---|---|---|---|---|

| Code | Target evidence | Score | Severity | User/task impact |
|---|---|---:|---|---|

## WCAG Chapter

Use criterion statuses instead of 1-5 scoring.

| Criterion | Level | Status | Page/process | Method | Evidence | Recommendation | Reference |
|---|---|---|---|---|---|---|---|

Always state that observed passes apply only to the tested state and method. Never use site-wide conformance language for partial coverage.

## Deceptive Patterns Chapter

| Canonical ID | Pattern | Status | Choice set/journey | Signals | Counter-evidence | User harm | Human verified | Reference |
|---|---|---|---|---|---|---|---|---|

Do not present `candidate` signals as definitive findings.

## Fair Patterns Chapter

| Linked finding | Fair Pattern | Replacement behavior | Why it restores autonomy | Constraint | Success evidence | Reference |
|---|---|---|---|---|---|---|

## Gap-To-Benchmark Chapter

| Target code/finding | Target evidence | Competitor | Same task and stage | Better evidence | Transferable pattern | Recommendation |
|---|---|---|---|---|---|---|

If no supported competitor benchmark exists, say so in the matrix and omit the evidence slide.

## Evidence Slide Contract

Every evidence slide uses one source screenshot and one findings table.

```text
Title:
Framework and state:
Screenshot:
Viewport:
Journey stage:
Pin number:
Finding:
Evidence:
Framework code/result:
User harm:
Recommendation:
Source:
```

Required table columns: `No`, `Finding`, `Evidence`, `Framework`, `Recommendation`, `Source`.

- Put only numbered rounded pins on target screenshots.
- Do not add highlight boxes, callout rectangles, or paragraph overlays.
- Keep explanatory text outside the screenshot.
- Pins and rows must be generated from the validated annotation manifest.
- Check placement in the rendered artifact and update `placement_verified`.

## PPT Requirements

- Start from the user's supplied PowerPoint template.
- Create slides only from existing template layouts and preserve its masters.
- Remove source example slides and source-brand references.
- Do not create custom audit layouts, a `.potx`, or a separate audit template.
- Use Helvetica Neue Regular only; no italics.
- Respect layout text limits and split dense chapters across additional existing layouts.
- Do not include a method slide.

## HTML Requirements

- Use a landscape presentation viewport.
- Use the same deck order and evidence-slide contract as PPT.
- Use exactly one `<img>` screenshot on each evidence slide.
- Keep framework and summary slides text-only when no screenshot is needed.

## Recommendations

Group recommendations into immediate fixes, structural improvements, and experiments. Every recommendation must link to a supported target finding.

## Deck QA

- Framework definitions precede their findings.
- Every framework has an explicit state and source.
- Every code resolves to one definition.
- Every evidence slide has one screenshot.
- Every annotation exists in the validated manifest.
- Every pin matches its table row and visible UI element.
- Every source names page, viewport, capture date, and method.
- Every WCAG result includes criterion, level, status, method, and W3C reference.
- Every supported deceptive result is human-verified and has Fair Pattern remediation.
- Every competitor slide maps to the same target task and journey stage.
- Rendered slides have no clipped text, overlaps, missing sources, or misplaced pins.

## Sources

List audited URLs, capture dates, viewports, test methods, framework references, blocked states, assumptions, and evidence limits.
