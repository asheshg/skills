# Fair Pattern Remediation Framework

Use this framework only after a `supported` or `verified` deceptive-pattern finding. It provides remediation options, not diagnostic scores.

Source: `https://www.fairpatterns.ai/resources/library`

## Library

| Code | Fair pattern | Use it to |
|---|---|---|
| FP-01 | Neutral or Protective Default | Replace biased defaults with neutral or user-protective settings. |
| FP-02 | Adequate Information | Disclose costs, terms, recurrence, data use, deadlines, stock basis, and consequences before action. |
| FP-03 | Seamless Path | Make exit, cancellation, rejection, unsubscribe, and comparison direct. |
| FP-04 | Non-Intrusive Information | Present relevant information without interrupting a task the user initiated. |
| FP-05 | Plain and Empowering Language | Use clear, neutral wording that explains options and consequences. |
| FP-06 | Free Action | Let users act without unrelated enrollment, sharing, or commercial detours. |
| FP-07 | Fair UX | Give intended choices honest hierarchy, comparable visibility, and understandable controls. |

## Starting Crosswalk

| Deceptive pattern | Candidate fair patterns |
|---|---|
| Nagging | FP-04, FP-06 |
| Hard to Cancel or Comparison Obstruction | FP-03, FP-02 |
| Sneaking, Hidden Costs, Hidden Subscription | FP-02, FP-01 |
| Confirmshaming or Trick Question | FP-05, FP-07 |
| Asymmetric Choice or Pressured Selling | FP-07, FP-01 |
| False Urgency, False Scarcity, Unverifiable Social Proof | FP-02, FP-04 |
| Forced Enrollment, Privacy Zuckering, Forced Path | FP-06, FP-01, FP-03 |

Choose one or more patterns based on the actual harm and implementation constraints. If none fits, use `custom` and describe the neutral replacement plainly.

## Required Remediation Record

```text
Linked deceptive-pattern finding:
Fair pattern code and name:
Replacement behavior:
Why it restores autonomy:
Implementation constraints:
Success evidence:
Reference:
```

Do not create a Fair Patterns chapter when there are no supported deceptive findings. State `not invoked: no supported deceptive-pattern finding` in the framework map.
