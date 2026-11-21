# Deceptive Pattern Recognition Framework

Use this framework to identify observable interface patterns that may impair autonomy or informed choice. Do not infer designer intent or make a legal finding.

## Sources And Roles

- Deceptive Design defines the autonomy and informed-choice test and provides the forced-path concept: `https://www.deceptive.design/book/contents/part-1`
- Princeton supplies an e-commerce taxonomy and concrete pattern definitions: `https://webtransparency.cs.princeton.edu/dark-patterns/`
- UXP2 supplies five strategy families and practitioner examples: `https://darkpatterns.uxp2.com/`
- UC Berkeley supplies a detection method based on choice sets, language, CSS asymmetry, structure, and confidence: `https://www.ischool.berkeley.edu/programs/mids/capstone/2026a-spring/deceptive-pattern-detector`

Record the source retrieval date in each audit. Treat Berkeley as detection methodology, not normative authority.

## Detection Method

1. Identify a choice set: related buttons, links, checkboxes, fields, prices, messages, or steps that present one decision.
2. Capture the complete state or journey, not an isolated phrase.
3. Inspect four signal groups: language, visual/CSS asymmetry, DOM/accessibility structure, and cross-option or cross-step behavior.
4. Record counter-evidence: truthful stock data, equivalent reject action, clear disclosure, optional flow, or reversible choice.
5. Match a canonical pattern only when the minimum evidence is met.
6. Require human verification before publishing `supported` or `verified`.

Statuses: `candidate`, `supported`, `verified`, `not-observed`, or `not-tested`.

- `candidate`: one signal; needs more context.
- `supported`: at least two independent signals or one complete-flow observation, with no strong counter-evidence.
- `verified`: the behavior or claim was checked across state/time/flow and confirmed by a human.

Never call ordinary urgency, scarcity, social proof, prominence, or gamification deceptive without evidence that it is false, obscures choice, creates unequal effort, or impairs informed action.

## Canonical Taxonomy

| ID | Canonical pattern | Source aliases / family | Observable signals | Minimum evidence and key exclusion |
|---|---|---|---|---|
| DP-NAG-01 | Nagging | UXP2: Nagging | Repeated prompts redirect the same user task after dismissal. | Repeats across interactions; exclude a single relevant prompt. |
| DP-OBS-01 | Hard to Cancel | Princeton: Obstruction; UXP2: Obstruction/Roach Motel | Exit, cancellation, rejection, or unsubscribe requires more steps or channels than entry. | Compare entry and exit journeys; exclude necessary identity or fraud controls. |
| DP-OBS-02 | Comparison Obstruction | UXP2: Price Comparison Prevention, Intermediate Currency | Units, bundles, credits, or layouts prevent meaningful price comparison. | Show materially harder comparison; exclude domain-required units with clear conversion. |
| DP-SNK-01 | Sneak into Basket | Princeton/UXP2: Sneak into Basket | An item or add-on appears without an explicit user selection. | Verify cart state before and after; exclude clearly selected bundles. |
| DP-SNK-02 | Hidden Costs | Princeton: Hidden Costs | Mandatory charges appear only late in checkout. | Capture earlier and final price states; exclude variable costs explained before commitment. |
| DP-SNK-03 | Hidden Subscription | Princeton: Hidden Subscription; UXP2: Forced Continuity | Recurring billing is disguised as one-time, trial, or optional. | Recurrence is absent or obscured near consent; exclude prominent terms and reminder/cancel controls. |
| DP-SNK-04 | Bait and Switch | UXP2: Bait and Switch | A control produces a materially different result from its label or prior promise. | Verify expected versus actual result; exclude a clear state change or disclosed substitution. |
| DP-INT-01 | Confirmshaming | Princeton: Confirmshaming; UXP2: Toying with Emotion; Berkeley: Confirm Shaming | Decline copy uses guilt, ridicule, fear, or moral pressure. | Compare option language; exclude factual consequence statements. |
| DP-INT-02 | Asymmetric Choice | UXP2: False Hierarchy/Interface Interference; Princeton: Visual Interference/Misdirection; Berkeley: Asymmetric Choice | Business-preferred action has materially greater size, contrast, placement, or semantic clarity. | Compare the whole choice set; prominence alone is insufficient if alternatives remain clear and equal-effort. |
| DP-INT-03 | Trick Question | Princeton/UXP2/Berkeley: Trick Question | Double negatives, reversed conventions, or inconsistent opt-in/opt-out wording obscure the choice. | Show likely interpretation conflict; exclude plain affirmative consent. |
| DP-INT-04 | Pressured Selling | Princeton: Pressured Selling | More expensive variants or add-ons are preselected or repeatedly pushed. | Confirm default or repeated pressure; exclude a clearly optional recommendation. |
| DP-URG-01 | False Urgency | Princeton: Countdown Timer/Limited-time Message; Berkeley: Urgency | A timer or deadline pressures action but resets, persists, or lacks a verifiable end. | Recheck after expiry or across sessions; truthful deadlines are not deceptive. |
| DP-SCA-01 | False Scarcity | Princeton: Low-stock/High-demand; Berkeley: Scarcity | Stock or demand claims appear universal, implausible, or unverifiable. | Recheck variants/time or find contradictory state; truthful inventory is not deceptive. |
| DP-SOC-01 | Unverifiable Social Proof | Princeton: Activity Messages/Testimonials of Uncertain Origin; Berkeley: Social Proof | Peer activity or testimonials lack source, date, or verifiable origin. | Show missing provenance or repeated fabricated state; genuine attributed proof is excluded. |
| DP-FOR-01 | Forced Enrollment | Princeton: Forced Action/Enrollment; UXP2: Forced Action | Account creation, marketing consent, or data sharing is required for an unrelated primary task. | Verify no task-relevant alternative; exclude requirements necessary to deliver the service. |
| DP-FOR-02 | Privacy Zuckering | UXP2/Berkeley: Privacy Zuckering | Defaults, copy, or buried controls cause broader data sharing than users reasonably expect. | Compare stated purpose, defaults, and control depth; do not infer from a privacy link alone. |
| DP-FOR-03 | Forced Path | Deceptive Design: Forced Path | Users must traverse unrelated commercial prompts or steps before the primary task. | Verify the path is mandatory and unrelated; exclude necessary process steps. |

## Required Finding Record

```text
Canonical ID and pattern:
Status and confidence:
Choice set or journey:
Observed signals:
Counter-evidence checked:
User harm:
Human verification:
Source alias and reference:
```

Framework state: `tested-with-findings`, `tested-no-supported-findings`, `partially-tested`, or `not-tested`. Candidate signals may appear in working notes but not as definitive deck claims.
