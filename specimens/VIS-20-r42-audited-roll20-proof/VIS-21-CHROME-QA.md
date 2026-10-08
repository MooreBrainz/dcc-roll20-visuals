# VIS-21 — Roll20 Chrome Integration / QA Gate

**Status:** Integrated into **VIS-20 rendering proof CSS**; awaiting live Roll20 review.  
**Production boundary:** No main engineering/worker/production HTML or CSS was changed.

## What is now connected to the proof

| Source asset | Preview use | Technique |
| --- | --- | --- |
| `assets/chrome/panels/panel-frame-wide.png` | Main panels across Character, Skills & Spells and Socials | 9-slice `border-image` on a noninteractive pseudo-element |
| `assets/chrome/panels/panel-frame-sidebar-tall.png` | Socials left-column Profile / Popularity | Separate 9-slice frame for small panels |
| `assets/chrome/panels/panel-frame-large.png` | Section/page headings | Centered cropped header background; never stretched across tall panels |
| `assets/chrome/dividers/divider-bar-amber.png` | Panel and library header edges | Narrow horizontal cropped strip |
| `assets/chrome/fields/field-frame-dark.png` | Read-only example fields | Quiet background only, actual input remains |
| `assets/chrome/fields/field-frame-active.png` | Focused input/select states | Subordinate raster texture plus visible 2px focus outline |

The original `field-frame-horizontal.png` stays in the asset library but is **not globally applied yet**: using all three field variants without validating focus/contrast would create unnecessary decorative noise.

## Why slices instead of stretched images

Some source images have transparent centers; others are shallow, textured plates, not empty frames. The implementation uses `border-image-slice` **without `fill`** and maintains the real CSS panel background, to avoid turning working content into unreadable artwork.

Panel borders are decorative `:after` layers with `pointer-events:none`. They do not replace panel contents or carry functional state. A 10px border-image width is used in the narrow layout instead of 14px.

## Local browser smoke test

A self-contained Chromium smoke specimen was composed from the same assets and the same border/divider/field treatment, then rendered at three viewport widths:

- 1400 px: 2-column large panel + narrow panels + full-width card.
- 900 px: same panels with less horizontal room.
- 520 px: stacked panels.

**Observed:** ornamental corner edges remained visible; content and header labels were legible; no panel disappeared in these three smoke views. The test exercised representative cards, not the complete VIS-20 Roll20 proof. It does **not** establish compatibility with Roll20's CSS sanitizer or all responsive layouts.

## Roll20 review checklist

1. Paste the newest `roll20-preview.css` into the existing disposable Roll20 Custom Sheet Sandbox; keep the current proof HTML.
2. Confirm the race banner still displays correctly and that Character / Skills & Spells / Socials navigation remains intact.
3. On Character, inspect Core Stats and the two setup/status panels for corner scale and any text hidden beneath the decorative frame.
4. On Skills & Spells, inspect the tall Skill Library, the shorter Spell Library, row buttons and the library-heading dividers.
5. On Socials, inspect the smaller Profile/Popularity panels, six real club badges, and the adjacent Sponsors / Media panels.
6. Check normal width, narrow sidebar, and a very narrow sheet. Watch for clipping, stretched rivets, overflow, or unreadable inputs.
7. Focus keyboard-accessible inputs; the warm focus outline must remain visible even if the decorative texture is blocked.

If Roll20 strips `border-image`, the original 1px CSS panel borders and dark backgrounds remain as a usable fallback.

## Promotion gate

This is **VIS-21 visual work only**. Nothing is approved for production until the sheet is visually checked inside Roll20. R42's original system data, hidden state gates, and repeating-section relationships remain authoritative.


## VIS-21D — Unified Page Title Nameplates

The original full-width `panel-frame-large.png` treatment was unsuitable for wide page headings. VIS-21B temporarily replaced it with a faint gradient; VIS-21C restored an actual compact art nameplate for **Core Character State**.

VIS-21D now applies the **same compact metal nameplate pattern to all three active proof pages**:

- Character — **Core Character State**
- Skills & Spells — **Entry-Heavy Libraries**
- Socials — **Public Presence**

The nameplate stays at **455 px maximum width** inside the page heading rather than stretching to the full viewport. The full-width heading behind it remains quiet dark metal. Existing ornamental content panel borders and dividers remain unchanged. Text remains live HTML.

The CSS has responsive adjustments at <=720 px and <=390 px for heading wraps. Structural checks confirmed the three page heading containers and CSS selectors, unchanged proof HTML, and balanced CSS braces. An attempted Chromium screenshot run stalled in the current local runtime, so **no new live browser or Roll20 visual test is claimed for VIS-21D**. The earlier VIS-21C local nameplate preview was a separate test.

**Review next:** paste latest CSS in the Roll20 sandbox; check Character, Skills & Spells, and Socials at normal and narrow widths. Specifically look for the full nameplate being visible, long titles staying within the frame, and whether the right-side provenance note remains readable.
