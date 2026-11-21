# WCAG 2.2 Accessibility Framework

Use this framework for criterion-level WCAG 2.2 Level A and AA observations. It supports an audit, not certification or a legal opinion.

## Scope Contract

- Record pages, viewports, user journeys, and complete processes tested.
- Record method for every criterion: `automated`, `DOM-manual`, `keyboard`, `screen-reader`, `visual`, or `not-tested`.
- Use `fail`, `risk`, `pass-observed`, `not-applicable`, or `not-tested`.
- Never claim site-wide conformance unless every applicable A and AA criterion and every complete process has been tested and passed by qualified human review.
- A screenshot alone can support a visual observation, not a complete accessibility assessment.

Framework state: `tested-with-findings`, `tested-no-supported-findings`, `partially-tested`, or `not-tested`.

## Level A And AA Registry

| Principle | Level A criteria | Level AA criteria |
|---|---|---|
| Perceivable | 1.1.1 Non-text Content; 1.2.1 Audio-only and Video-only; 1.2.2 Captions (Prerecorded); 1.2.3 Audio Description or Media Alternative; 1.3.1 Info and Relationships; 1.3.2 Meaningful Sequence; 1.3.3 Sensory Characteristics; 1.4.1 Use of Color; 1.4.2 Audio Control | 1.2.4 Captions (Live); 1.2.5 Audio Description (Prerecorded); 1.3.4 Orientation; 1.3.5 Identify Input Purpose; 1.4.3 Contrast (Minimum); 1.4.4 Resize Text; 1.4.5 Images of Text; 1.4.10 Reflow; 1.4.11 Non-text Contrast; 1.4.12 Text Spacing; 1.4.13 Content on Hover or Focus |
| Operable | 2.1.1 Keyboard; 2.1.2 No Keyboard Trap; 2.1.4 Character Key Shortcuts; 2.2.1 Timing Adjustable; 2.2.2 Pause, Stop, Hide; 2.3.1 Three Flashes or Below Threshold; 2.4.1 Bypass Blocks; 2.4.2 Page Titled; 2.4.3 Focus Order; 2.4.4 Link Purpose (In Context); 2.5.1 Pointer Gestures; 2.5.2 Pointer Cancellation; 2.5.3 Label in Name; 2.5.4 Motion Actuation | 2.4.5 Multiple Ways; 2.4.6 Headings and Labels; 2.4.7 Focus Visible; 2.4.11 Focus Not Obscured (Minimum); 2.5.7 Dragging Movements; 2.5.8 Target Size (Minimum) |
| Understandable | 3.1.1 Language of Page; 3.2.1 On Focus; 3.2.2 On Input; 3.2.6 Consistent Help; 3.3.1 Error Identification; 3.3.2 Labels or Instructions; 3.3.7 Redundant Entry | 3.1.2 Language of Parts; 3.2.3 Consistent Navigation; 3.2.4 Consistent Identification; 3.3.3 Error Suggestion; 3.3.4 Error Prevention (Legal, Financial, Data); 3.3.8 Accessible Authentication (Minimum) |
| Robust | 4.1.2 Name, Role, Value | 4.1.3 Status Messages |

Official standard: `https://www.w3.org/TR/WCAG22/`

## Required Finding Record

```text
Criterion and level:
Status:
Page/process scope:
Evidence:
Test method:
Impact:
Recommendation:
Reference:
```

Use `risk` when evidence suggests a barrier but interaction or assistive-technology verification is incomplete. Use `pass-observed` only for the exact page, state, and method tested.

## Coverage Slide

Show:

- framework state;
- pages and complete processes tested;
- criterion counts by status;
- methods completed and omitted;
- limitations, especially missing keyboard or assistive-technology testing.

If any applicable criteria remain `not-tested`, label the result a partial WCAG audit and do not use `compliant`, `conformant`, or `passes WCAG` for the site.
