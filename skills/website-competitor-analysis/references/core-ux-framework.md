# Core UX Audit Framework

Use this framework for usability, information, interface, navigation, interaction, and visual-design findings. It is the only authority for Core UX parameter codes. Assess applicable parameters in each state. The presentation always includes the full baseline below, in source order, even when a short audit tests a subset.

## Status And Scoring

Record framework state as `tested-with-findings`, `tested-no-supported-findings`, `partially-tested`, or `not-tested`.

Score observed Core UX parameters from 1-5 and explain each score with evidence:

- `5`: Clear best-in-set execution with strong evidence.
- `4`: Strong execution with minor friction.
- `3`: Adequate but inconsistent or undifferentiated.
- `2`: Noticeable friction or unclear execution.
- `1`: Blocks comprehension, trust, navigation, or task completion.

Do not average away severe outliers.

## Canonical parameters

The baseline reproduces the two website assessment tables on pages 29?30 of the Tata CLiQ UI/UX Audit. Preserve the headers, row order, group labels, codes, names and descriptions. Blank area cells continue the preceding group. In the deck, group those cells vertically as in the reference.

### 1/2

| Area of focus | Code | Parameter | Description |
|---|---|---|---|
| Visual design | VD1 | Contrast and Readability | Text colours that contrast well with background |
|  | VD2 | Number of Colours used | Limited number of colours used (best practice is to use 3 to 4) |
|  | VD3 | Alignment of Elements | Alignment of elements (text, headers, images, boxes, etc.) |
|  | VD4 | Visual Balance | Balance between amount of text and images (i.e., screens/pages are illustrative and informative) |
|  | VD5 | Use of White Space | Optimal use of white space (e.g. left and right margins are not too wide, uncondensed text) |
|  | VD6 | Visual Differentiation | Clear distinction between elements to avoid visual clutter and highlight key content. |
|  | VD7 | Status Cues | Clear indicators for different states (e.g., added to cart, applied offers) |
| Information design | IN1 | Information Gathering | Available technical and commercial information on all products and services in portfolio |
|  | IN2 | Personalized Suggestions | Recommended products and services based on personal information collected |
|  | IN3 | Promotions and Offers | Consolidated section on website with promotions and offers on products and services |
|  | IN4 | FAQs | Comprehensive FAQs addressing top complaints |
|  | IN5 | Guided Tutorials | Video or screenshot tutorials guiding customers step-by-step |
|  | IN6 | Data Validation | Validating data entry at every step to avoid cumulative error |
|  | IN7 | Error Messages | Appropriate error and recovery messages |
|  | IN8 | Status Notifications | Proactive customers notifications through email or SMS about the status of their application |
|  | IN9 | Rich Media & Social Proof | Product preview videos and customer reviews for better engagement and credibility. |

### 2/2

| Area of focus | Code | Parameter | Description |
|---|---|---|---|
| Information Architecture | IA1 | Nomenclature | Consistent and appropriate labelling |
|  | IA2 | Organization | Hierarchy and Grouping of similar elements/options in a logical order - chronological, alphabetical, sequential |
|  | IA3 | Visibility & Accessibility | Ensuring important information (e.g., delivery timelines, stock availability) is immediately accessible. |
| Interface design | IF1 | Consistency | Consistent user interface across platforms and seamless experience across all use cases |
|  | IF2 | Responsive | Support for major browsers, use of adaptive images and adaptability to screen specific resolutions |
|  | IF3 | Aesthetic & Minimal | Interface should not contain information which is irrelevant or rarely needed |
| Navigation design | ND1 | Headers & Navigation | Consistent headers, logos, and navigation elements across screens/pages, with easy ability to go back without losing progress. |
|  | ND2 | Dynamic Search & Cross-Category Results | Intuitive and dynamic suggested searches (e.g., auto-completion based on click-through analysis, natural language processing incl. error correction and predictive result generation) |
|  | ND3 | Navigation Menu Location | Static and visible navigation menu on all pages |
|  | ND4 | Product Categorization | Filtering options for devices and services based on brand, recommended products, price, new products, op. system, star rating, best-selling, and special promotional offers |
|  | ND5 | Backward Navigation | Consistent backward navigation ability |
|  | ND6 | Progress Indicators | Visual elements to depict progress within a process |
| Interaction design | ID1 | Active Wording | Active wording using colours and layout to promote user transactions (e.g. call-to-action buttons) |
|  | ID2 | Transitions | Smooth & Contextual animations |
|  | ID3 | Error Prevention | Helpful messages in error-prone areas, confirmation options |
|  | ID4 | Control Element | Using appropriate control elements for choices |

## Nielsen Heuristic Cross-Check

Cross-check each reviewed screen against the applicable Nielsen heuristics: system status; real-world match; user control; consistency; error prevention; recognition over recall; flexibility; minimalist design; error recovery; help and documentation.

Source: `https://www.nngroup.com/articles/ten-usability-heuristics/`

Use the two review skills when installed. When unavailable, use the principles listed here and record the fallback:

- `$nielsen-heuristics-audit` for a systematic heuristic evaluation.
- `$don-norman-principles-audit` for discoverability, affordances, signifiers, feedback, mapping, constraints, and conceptual models.

Use Don Norman?s principles to inspect discoverability, affordances, signifiers, feedback, mapping, constraints and conceptual models. Keep the Tata CLiQ baseline as the source of deck codes. Record Nielsen and Norman mappings in the test log without adding columns or a separate benchmark to the deck.

## Target-Gap Logic

Audit the target before selecting benchmarks. For every competitor example, require the same task, journey stage, and target weakness:

| Target code | Target evidence | Severity | Better competitor evidence | Transferable pattern | Recommendation |
|---|---|---|---|---|---|

If no competitor is demonstrably better, omit the benchmark and recommend a sourced best-practice fix.
