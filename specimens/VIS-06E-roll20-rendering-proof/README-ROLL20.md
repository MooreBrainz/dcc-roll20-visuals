# Load VIS-06E in Roll20

This folder is a **visual rendering proof**, not the production character sheet. It is safe to load in a test game or Roll20 Custom Sheet Sandbox to inspect the proposed chrome, banner layering, stat sizing, Health Bar treatment, and responsive behavior.

## Best option: Custom Sheet Sandbox

Roll20's Custom Sheet Sandbox is available to Pro users and accepts uploaded HTML/CSS files.

1. Download `roll20-preview.html` and `roll20-preview.css` from this folder.
2. Open the Roll20 Custom Sheet Sandbox.
3. Upload `roll20-preview.html` as the HTML file.
4. Upload `roll20-preview.css` as the CSS file.
5. A translation file is not required for this proof, but `translation.json` is included if the sandbox prompts for one.
6. Open a character sheet and resize the window to test the header crop and compact layouts.

## Existing game

In a test game's settings, choose a **Custom** character sheet and place the contents of `roll20-preview.html` in HTML Layout and `roll20-preview.css` in CSS Styling.

Do **not** replace your ongoing production sheet with this proof unless you have a backup. This specimen contains only a small subset of R42 and does not contain the production sheet workers or mechanics.

## What should work

- GitHub-hosted header/chrome imagery.
- Cinematic banner + independent class overlay.
- The real five-stat naming model.
- Current entity-mode values.
- Existing 10-slot Health Bar attribute names.
- Responsive visual layout.

## What is intentionally nonfunctional

- Navigation buttons are visual only.
- No R42 sheet workers are included.
- No class/race selection logic is included.
- The chat card is a visual sample rather than a wired roll template.
- The displayed sample values are not a replacement for production data.

If an SVG asset is rejected by Roll20's image security policy in your environment, record which asset failed. The same proof assets can be exported to PNG without changing the layout architecture.
