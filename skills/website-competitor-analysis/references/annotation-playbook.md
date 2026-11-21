# Screenshot Annotation Playbook

The manifest is the evidence contract; this file owns capture and placement rules.

## Capture

Capture the target journeys first. Capture competitors only after a supported target weakness exists.

Prefer `$browse` when available:

```bash
$B goto <url>
$B viewport 1440x1000
$B snapshot -o <out-dir>/<site>-<page>-desktop.png
$B ux-audit
$B console --errors
$B perf
```

Raw `snapshot -i -a -C` labels may support analysis but must not appear in the client deck. If `$browse` is unavailable, use equivalent browser automation and disclose the substitute.

For each source screenshot, record the URL, page/state, viewport, natural width and height, capture date, method, and cleanup. If content was removed or altered for legibility, preserve the raw screenshot and disclose the change.

## One-Screenshot Rule

- Every evidence slide has exactly one source screenshot.
- Do not use screenshot groups, collages, or before/after composites as one evidence figure.
- Framework, summary, and source slides may be text-only.
- If two states are required to prove a finding, use two evidence slides and link them by finding ID.

## Pins

- Use numbered rounded pins only.
- Do not use highlight boxes, callout rectangles, arrows, or text overlays on screenshots.
- Put each pin on or immediately beside the exact visible element described by its row.
- Store pin coordinates relative to the screenshot's natural dimensions, then convert to percentages.
- Record optional element bounds when the finding concerns a control or bounded region.
- Keep pin numbers unique within a slide and identical to the findings-table numbers.

Coordinate conversion:

```text
x_percent = element_center_x / screenshot_natural_width * 100
y_percent = element_center_y / screenshot_natural_height * 100
```

## Source Line

Every finding row uses:

```text
Source: <site and page/state>, <viewport>, captured <YYYY-MM-DD>, <capture method and limitation>
```

Use neutral examples only:

```text
Source: example.com product page, desktop 1440x1000, captured YYYY-MM-DD, browser automation
```

## Placement Verification

After rendering the PPT or HTML deck:

1. Open each evidence slide at presentation size.
2. Confirm the screenshot has not been cropped or stretched.
3. Confirm every pin touches the intended element and no other element.
4. Confirm pin numbers match table rows.
5. Confirm text and sources are readable without overlap.
6. Set `placement_verified: true` only after this check.

If the screenshot's crop or aspect ratio changes, recalculate positions. Do not nudge pins by eye without recording the corrected coordinates in the manifest.

## Framework Evidence

- Core UX annotations use a canonical parameter from `core-ux-framework.md`.
- WCAG annotations identify the criterion, level, status, test method, and reference.
- Deceptive-pattern annotations identify the canonical ID, choice set, status, counter-evidence, harm, source alias, and human verification.
- Fair Pattern remediation remains in the findings table or remediation chapter; it is not a separate visual pin.
- Non-visual claims belong in coverage, limitations, or recommendations, not on a screenshot.

## Competitor Evidence

A competitor annotation is valid only when the manifest records:

- the supported target gap;
- the same user task;
- the same journey stage;
- the competitor behavior that is demonstrably better;
- the transferable pattern and target recommendation.

Generic praise or visual inspiration is not benchmark evidence.
