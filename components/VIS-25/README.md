# VIS-25 — Source-Mapped Visual Components (Pilot)

**Status: prepared, opt-in, not installed into production or the evolving development branch.**

This package is the first step from VIS-20/VIS-24 mockup styling toward a source-aware Roll20 integration. It was mapped against the supplied read-only `V38_R42_ENGINEERING.zip`. That package describes an R42 test candidate, **not necessarily your latest development branch**.

## Files

- `vis25-r42-bridge.css` — opt-in, R42-selector-based styling for real navigation, ornate panels, controls, fields, native skill/spell pills and compact stat rows.
- `component-map.md` — exact structural/attribute ownership, existing selectors, risks, asset references, and style boundaries.
- `validation-checklist.md` — activation, roll-back and live Roll20 regression checks.
- `asset-manifest.json` — machine-readable references to existing, already verified raster assets.
- `validate_contract.py` — dependency-free read-only compatibility check for a supplied engineering HTML/CSS snapshot.

## What's different from the VIS-20 proof

VIS-20 targets `.sheet-vis20-*` mockup components. **VIS-25 instead targets existing `.sheet-vn-*` classes from the R42 HTML.** No fake controls, copied fixture skills, invented stats, or example sponsor mechanics are imported.

R42's skill/spell pills already change colour through `sheet-vn-summarytone` and `sheet-vn-familytone` sibling gates. The bridge **does not override their colours**; it only adjusts geometry and readability while preserving rounded pills.

The five R42 stat controls are compact rows, not the large VIS-20 prototype tiles. VIS-25 respects their intrinsic grid geometry; the full-development-sheet stat layout is reserved for later review.

## Opt-in activation — sandbox only

1. On a disposable copy of the current engineering HTML, append **`sheet-vis25-skin`** to the existing wrapper's class list, retaining `sheet-vn-wrapper`.
2. Append the contents of `vis25-r42-bridge.css` **after** the engineering CSS in the sandbox. No separate CSS `@import` is required.
3. Navigation and native skill/spell pill rounding become active immediately inside that wrapper; no HTML rewriting is needed.
4. Add **`sheet-vis25-panel`** to **one selected existing** `sheet-vn-panel`, preferably a low-risk static Character or Socials panel, to pilot the ornamental frame. Optionally add `sheet-vis25-panel--sidebar` or `sheet-vis25-panel--quiet` to the same element.
5. Add **`sheet-vis25-control`** to one real `sheet-vn-btn` and **`sheet-vis25-field`** to one visible `sheet-vn-input` to pilot their treatments.
6. Add **`sheet-vis25-stat`** to one of the five `sheet-vn-stat` elements to inspect how compact rows respond. Keep all existing input and roll button children.
7. Review and revert the opt-in class(es) if any layout/gate behavior changes. Never move a hidden gate, sibling, fieldset, button, or repeating section merely to make chrome fit.

## Non-goals

- No automatic race banner selection or class overlays yet; the proven Tigran asset is not hard-coded across other races.
- No edit to the original R42 engine or to production.
- No worker, health/mana, ability, inventory, deity, achievement, club, sponsor, or loot-box behavior change.
- No final approval for stat tile geometry. A latest-development-source diff is required first.
- No attempt to convert `VIS-20` visual preview HTML into the authoritative sheet.

## What should happen next

The engineering stream provides its latest **HTML, CSS and worker** snapshot. We run a fresh selector/contract comparison; revise the bridge where necessary; pilot **Character + Skills/Spells + Socials** in a disposable Roll20 sandbox; then extend the library tab by tab. The Visual repo remains independent of the production release process.

Useful previous gates: `docs/vis-specs/VIS-06F_R42_Visual_Normalization_Audit.md`, `specimens/VIS-20-r42-audited-roll20-proof/VIS-24-DENSITY-AND-PILLS-QA.md`.
