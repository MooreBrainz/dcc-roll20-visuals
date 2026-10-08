# VIS-23B / VIS-24 — Colour Pills & Responsive Density

**Status:** Source-grounded visual corrections committed in the Roll20 rendering proof. **Awaiting Roll20 visual review.**

**Boundary:** VIS-only specimen. No production HTML/CSS/worker, game mechanics, or release metadata changed.

## VIS-23B — Pill correction from user review

The VIS-23 plain square grey chips were **not approved**. Skill/Spell type/family pills are now **rounded, colour-coded tags**. The styling intentionally follows the actual R42 `.sheet-vn-typepill` / `.sheet-vn-actionpill` / `.sheet-vn-familypill` vocabulary rather than assuming the grey prototype was definitive.

### Relevant R42 visual tone mappings

- ATTACK: red (R42 `#9c2c39` border / `#32151b` background)
- UTILITY / CHECK: cyan (R42 `#2d697f` / `#112631`)
- ANIMAL family: violet (R42 `#7562a5` / `#211b35`)
- ICE family: cool blue (R42 `#367b9c` / `#112936`)

The proof uses the sample label `COLD` with the cool-blue ICE visual treatment; `MOVEMENT`, `SENSE`, and `AREA` are **illustrative fixture labels**, not assertions about canonical R42 family catalog entries. Their hues remain visual examples until a source-driven final integration uses the actual R42 tone fields.

The proof HTML gained descriptive `class` attributes on **only ten existing `<i>` tags**, to make the static labels preview their colours. **No existing HTML element, name attribute, action button, or text content was otherwise changed.** This is necessary because CSS cannot reliably infer a category from text contents.

## VIS-24 — Intermediate/narrow density pass

The new `VIS-24 / RESPONSIVE DENSE ROW AND PROVENANCE` CSS section:

- uses `minmax(0,...)` in skill/spell columns to prevent long entries from pushing the sheet horizontally;
- switches library rows to a **two-row / three-column layout** at 721–1100px, keeping name, rank, tags, description, and actions accessible;
- preserves the existing single-column stacked rows at <=720px;
- makes source descriptions, character names, club logos/names and Sponsors/Media columns wrap safely;
- keeps the Socials club rail six columns wide, three columns at <=1050px, and two columns at <=720px;
- stacks the Popularity circle and adjacent text at <=480px without changing the circle data.

The approved muted chrome, compact page title nameplates, engraved navigation and action button styling are retained.

## Verified repository invariants

The GitHub before/after diff was checked against the previous proof HTML. Removing only the newly added pill classes produces the **exact original HTML string**.

- **10/10** coloured pill labels have matching CSS style hooks.
- All `name="..."` attributes remain unchanged.
- Existing button/role labels remain unchanged.
- CSS brace balance = zero.
- VIS-21E muted chrome and VIS-22 engraved navigation remain.
- Canonical R42 skill/spell pill relationships remain an engineering handoff constraint; these preview tags do not replace worker-driven tone gates.

## Roll20 review checklist

1. Replace **both** `roll20-preview.html` and `roll20-preview.css` in your disposable Roll20 proof sandbox. JSON/worker remain unchanged.
2. Skills & Spells: confirm the tags are **rounded and coloured**, not grey rectangles; verify Attack/Utility/Animal/Cool-blue examples.
3. Check ordinary and narrow windows. At intermediate width, long skill/spell rows should wrap into two rows rather than crowding five columns.
4. Ensure ADVANCE / DETAIL / ROLL / ADD COMBAT / PREP / HOT remain reachable and clearly separate from noninteractive coloured pills.
5. Socials: verify long club names wrap, badge images retain their proportions, and Media/Sponsors still sit adjacent at wide widths.
6. Narrow Socials: confirm club rail falls to three then two columns, Popularity remains legible, and Sponsor/Media regions stack.
7. Character: stat tiles should remain as in approved VIS-23; their suitability for the eventual development branch is explicitly **provisional** until live-source integration.

## Gate to next work

VIS-24 is implemented structurally but not visually approved in Roll20. The next iteration may adjust label wrapping/width thresholds if the sandbox demonstrates problems.

Do not promote these fixture controls into engineering. A final Roll20 sheet pass must use the latest trusted development HTML/CSS/worker and re-verify real type/family selection, source/provenance gates and action handlers.
