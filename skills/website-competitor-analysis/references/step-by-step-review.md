# Screen-by-screen review

Map the in-scope journeys from their ordinary entry points. Complete each journey on desktop and mobile, including meaningful loading, success, empty and error states. Record blocked steps and why. A screen is a visible state, including distinct states that share a URL.

| Step | Goal and starting state | Visible action | Expected result | Observed result | Tata CLiQ code and result | Nielsen / Norman cross-check | Evidence and date |
|---|---|---|---|---|---|

For each screen:

1. Record URL, viewport, region and session state. Use visible controls to act once, then refresh the snapshot and wait for the result to settle. Capture meaningful transient states separately. Tool failures and blocked access are test limitations.
2. For each desktop and mobile state, evaluate every applicable Tata CLiQ baseline parameter before moving on. Record passes, substantiated issues and untested checks by code. Cross-check against the applicable Nielsen heuristics and Don Norman principles in the Core UX reference. Record the mapping in the test log, including why a check could not be verified. Keep the Tata CLiQ codes in the deck's findings table. Search evidence must distinguish recent searches, featured content, typed suggestions and submitted results. Record the exact realistic query and the settled result. For filters, check the selection and results together, then clear and repeat.
3. Repeat suspected issues from a documented reset or record why repetition was blocked. Check alternative explanations and require visible evidence and a specific task impact before publishing. Keep speculative diagnoses out of the findings table.
4. Capture raw desktop/mobile evidence, keeping one row for a shared issue. Include all supported blockers and UX/UI issues with a clear heuristic and task impact. Annotate all relevant visible evidence, and reuse a row number across devices for the same issue. When revising an audit, account for old findings and remove unsupported claims from every slide, note and summary.
