# Core UX Audit Framework

Use this framework for usability, information, interface, navigation, interaction, and visual-design findings. It is the only authority for Core UX parameter codes. A short audit selects a subset of these codes; it never creates or redefines codes.

## Status And Scoring

Record framework state as `tested-with-findings`, `tested-no-supported-findings`, `partially-tested`, or `not-tested`.

Score observed Core UX parameters from 1-5 and explain each score with evidence:

- `5`: Clear best-in-set execution with strong evidence.
- `4`: Strong execution with minor friction.
- `3`: Adequate but inconsistent or undifferentiated.
- `2`: Noticeable friction or unclear execution.
- `1`: Blocks comprehension, trust, navigation, or task completion.

Do not average away severe outliers.

## Canonical Parameters

| Area | Code | Parameter | What to inspect |
|---|---|---|---|
| Visual design | VD1 | Contrast and Readability | Text and imagery remain legible against their backgrounds. |
| Visual design | VD2 | Number of Colours Used | A controlled palette supports hierarchy and meaning. |
| Visual design | VD3 | Alignment of Elements | Text, headings, images, controls, and containers align consistently. |
| Visual design | VD4 | Visual Balance | Text, imagery, controls, and whitespace have intentional visual weight. |
| Visual design | VD5 | Use of White Space | Spacing separates groups and supports scanning. |
| Visual design | VD6 | Visual Differentiation | Important content is distinct without visual clutter. |
| Visual design | VD7 | Status Cues | States, progress, selection, and feedback are visible. |
| Information design | IN1 | Information Gathering | Required technical and commercial information is available. |
| Information design | IN2 | Personalized Suggestions | Recommendations use relevant, consented context and remain explainable. |
| Information design | IN3 | Promotions and Offers | Offers are findable, understandable, and consolidated where useful. |
| Information design | IN4 | FAQs | FAQs address recurring questions and decision barriers. |
| Information design | IN5 | Guided Tutorials | Complex tasks receive suitable step-by-step guidance. |
| Information design | IN6 | Data Validation | Inputs are validated close to the point of entry. |
| Information design | IN7 | Error Messages | Errors explain the problem and recovery action. |
| Information design | IN8 | Status Notifications | Users receive timely, relevant status updates. |
| Information design | IN9 | Rich Media and Social Proof | Media and proof improve understanding and credibility. |
| Information architecture | IA1 | Nomenclature | Labels are consistent, specific, and familiar to users. |
| Information architecture | IA2 | Organization | Related options and content are grouped in a logical hierarchy. |
| Information architecture | IA3 | Visibility and Accessibility | Important information is available at the point of need. |
| Interface design | IF1 | Consistency | Components and controls behave consistently across pages and platforms. |
| Interface design | IF2 | Responsive | Layout, images, and controls work across supported viewports and browsers. |
| Interface design | IF3 | Aesthetic and Minimal | The interface excludes irrelevant or rarely needed content. |
| Navigation design | ND1 | Headers and Navigation | Global navigation, logos, and headers remain predictable. |
| Navigation design | ND2 | Dynamic Search and Cross-Category Results | Search supports intent, suggestions, and useful result recovery. |
| Navigation design | ND3 | Navigation Menu Location | Primary navigation remains visible and predictable. |
| Navigation design | ND4 | Product Categorization | Categories and filters match user shopping or decision models. |
| Navigation design | ND5 | Backward Navigation | Users can return, undo, or move backward without losing context. |
| Navigation design | ND6 | Progress Indicators | Multi-step processes expose location, progress, and remaining work. |
| Interaction design | ID1 | Active Wording | Labels and CTA language describe actions clearly. |
| Interaction design | ID2 | Transitions | Motion and state changes are smooth, contextual, and non-blocking. |
| Interaction design | ID3 | Error Prevention | Risky actions include prevention, constraints, or confirmation. |
| Interaction design | ID4 | Control Element | Choices use controls appropriate to their behavior and cardinality. |

## Parameter Definition Slide

Before detailed findings, define every Core UX code used later with:

```text
Code:
Parameter:
Plain-language definition:
What good looks like:
Common failure pattern:
Related Nielsen heuristic:
```

Detailed decks use the complete canonical list. Short audits may show only the selected canonical codes.

## Nielsen Heuristic Cross-Check

Map relevant findings to the ten Nielsen heuristics: system status; real-world match; user control; consistency; error prevention; recognition over recall; flexibility; minimalist design; error recovery; help and documentation.

Source: `https://www.nngroup.com/articles/ten-usability-heuristics/`

Optional adjacent skills may deepen this lens when installed:

- `$nielsen-heuristics-audit` for a systematic heuristic evaluation.
- `$don-norman-principles-audit` for discoverability, affordances, signifiers, feedback, mapping, constraints, and conceptual models.

Keep this skill as the report orchestrator and map adjacent-skill findings back to the canonical codes above.

## Target-Gap Logic

Audit the target before selecting benchmarks. For every competitor example, require the same task, journey stage, and target weakness:

| Target code | Target evidence | Severity | Better competitor evidence | Transferable pattern | Recommendation |
|---|---|---|---|---|---|

If no competitor is demonstrably better, omit the benchmark and recommend a sourced best-practice fix.
