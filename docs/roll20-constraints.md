# Roll20 Constraints

This repository is a visual-design stream, but assets and specimens should be designed for eventual Roll20 custom-sheet use.

## Structural constraints

- Preserve the current sheet's existing systems and attribute relationships.
- Name, Race, and Class are configured on the Character tab and displayed contextually in the header.
- The header contains no Health or Mana indicators.
- Crawler Health remains the existing slot-based Health Bar system.
- Do not create visual widgets that imply new mechanics.
- Repeating sections and canonical records must remain usable as real HTML controls.

## Rendering strategy

Use CSS for:
- layout
- gradients
- shadows
- recessed fields
- focus/hover states
- spacing
- typography
- common panel surfaces

Use image assets for:
- race banner artwork
- transparent class motifs
- ornate chrome/corners
- emblems and club badges
- selective texture

## Responsive requirement

Artwork must crop gracefully. Critical visual information should not sit at extreme edges that disappear in narrower sheet windows.
