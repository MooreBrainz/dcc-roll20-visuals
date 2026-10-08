# VIS-25 — Sandbox Compatibility / QA

**Current state:** Package prepared. The real development-branch code is **not** provided or migrated here; no functional Roll20 test is claimed.

## Static checks before merging into the development stream

Run `python validate_contract.py --html /path/to/sheet.html --css /path/to/sheet.css` against the **latest development snapshot**. R42 is expected to pass; treat any FAIL as a stop and investigate WARNs before proceeding.

1. Compare latest `sheet-vn-wrapper` markup, exact seven `act_vn_tab_*` buttons and adjacency with R42.
2. Diff `attr_*`, `act_*`, `repeating_*` names against the engineering snapshot before and after opt-in. Expected diff: **zero**.
3. Diff hidden `sheet-vn-*` gate elements, ordering and values, especially tab/page state, Skills DETAIL, spell PREP/HOT gates, entity mode, clubs and rewards. Expected diff: **zero**.
4. Confirm no worker, sheet-data, translation or repeating-section changes originate from VIS-25.
5. Verify that GitHub chrome URLs return valid PNG files and that border images use **no fill** (keep content legible).
6. Confirm the existing R42 `summarytone` / `familytone` pill rules still drive all meaningful type/family colours.

## Roll20 visual pilot order

- **Stage A — navigation only:** add `sheet-vis25-skin` to wrapper and CSS after development CSS; verify all seven actual tabs, selected states, entity-mode views and keyboard focus. No panel opt-in yet.
- **Stage B — one simple panel:** add `sheet-vis25-panel` to an existing non-repeating panel; check ornate corners at normal/narrow width, overlay pointer behavior, headings and scrollable content. Try `--quiet` if excessive chrome.
- **Stage C — one action + field:** add `sheet-vis25-control` to an actual action button, `sheet-vis25-field` to a visible input; verify click, hover, disabled and focus states against unchanged worker behavior.
- **Stage D — one stat row:** add `sheet-vis25-stat` on just one existing `sheet-vn-stat`; compare against other four; reject if tabular text shrinks or geometry shifts.
- **Stage E — dense libraries:** verify native rounded, source-coloured pills; detail panel hidden until DETAIL; ADVANCE, ROLL, ADD COMBAT and PREP/HOT buttons; long names and expanded card states.
- **Stage F — Socials:** verify six unchanged club badges, lock/provenance gates, Popularity, Sponsors, deferred interviews and narrow two/three-column badge layouts.

## Rollback

Remove `sheet-vis25-skin` from the root class list (or remove the appended CSS in the disposable test). Optional per-element `sheet-vis25-*` classes can remain inert until another pilot. This should restore existing R42 styling without touching mechanics.

## Hard stop conditions

Stop if any tab or mode becomes unreachable, if a gate is revealed/hidden incorrectly, if a button stops receiving clicks, if a field loses read-only semantics, if a coloured pill loses source-linked colour, if HP/Combat casting state changes, or if a club's hidden identity appears before access.

## Acceptance boundaries

VIS-25 is an **integration-ready styling package**, not a complete production skin. Only a successful sandbox test against the latest development HTML/CSS/worker allows extending coverage. Visual approval never promotes engineering/release state.
