# Screenshot annotation

Save the reusable audit record with evidence IDs independent of presentation slide numbers. Link the test log, including non-visual checks, blocked states and results with no findings, using `audit.test_record`. Keep file paths relative to the record when practical. Use `audit.selected_frameworks` to identify the checks requested and record each unselected framework as `not-tested`. Use `audit.output_format` to record audit-only or the requested presentation format.

Preserve raw captures for the scoped device sizes. Store the desktop capture in the primary slide fields and mobile in `mobile_capture`. If one size is blocked or outside scope, use the available image as the primary capture, omit `mobile_capture` and record `capture_limit`. Record the URL, state, viewport, natural image dimensions, capture date and method.

Generate marker numbers and table rows from the same finding records. Use numbered Tata CLiQ-style pins for visible evidence. Annotate both images in a desktop/mobile pair. Reuse the same pin number where both show the same issue and use separate numbered rows for distinct issues. When a finding is device-specific, pin it only where the evidence shows it and keep the other capture as context. Each pin must support its linked row. Apply Westside outlines only when explicitly requested. Keep description text in the table.

Store each marker’s coordinates as percentages of its source image width and height. Use the finding’s `x_percent` and `y_percent` for the primary capture and `mobile_pin` with the same keys for the second capture. Set primary coordinates to null when a finding appears only in the second capture. Leave `mobile_pin` null when evidence appears only in the primary capture. If a claim needs more than one state, link the captures under the same finding. Keep non-visual evidence in the test record or summary.

Fit captures in square-cornered frames without cropping or stretching and, when a deck is requested, inspect every rendered evidence slide at presentation size. Check that each pin touches its intended element, each number matches its row, and sources and text are readable. Set `placement_verified` after inspection.

For supplied heuristics, record the source in `frameworks.core-ux.parameter_source` and list the exact selected codes in `parameter_codes`. Leave both empty to use the built-in Core UX registry. Every Core UX finding must reference a code from the selected set.
