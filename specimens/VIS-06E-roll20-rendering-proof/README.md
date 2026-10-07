# VIS-06E — Roll20 Rendering Proof

Purpose: prove that the approved ornate visual language can be rendered with reusable assets and Roll20-compatible HTML/CSS without flattening the character sheet into one image.

## Current proof contents

- Cinematic race-reactive header using a replaceable Tigran proof banner.
- Separate transparent Barbarian-family class overlay.
- Display-only crawler / Race / Class identity in the header.
- Level / Floor context and the existing entity-mode concept.
- Seven current crawler tabs.
- Reusable metal/bronze chrome assets.
- Compact stat treatment using the crawler's actual five-stat model: STR / INT / CON / DEX / CHA.
- Live HTML input/focus surface.
- Existing 10-slot Health Bar treatment shown only in working content.
- Source/provenance badge.
- Repeating-style record examples.
- Representative chat-template card.
- R42 mapping notes in `mapping.md`.

## Important status

The current race banner is a **proof asset**, not final cinematic Tigran artwork. Its job is to establish layering, crop behavior, contrast zones, and interchangeability. Final race artwork can replace it without changing the proof HTML structure.

The specimen does not alter production HTML, CSS, attributes, workers, or mechanics.

## Acceptance criteria

- Ornate border treatment survives without interfering with live controls.
- No mechanics are invented.
- Working text remains readable over approved artwork.
- Race and class layers can be swapped independently.
- Shared chrome is reusable across multiple panel sizes.
- Narrower layouts remain usable even if banner cropping becomes more aggressive.
- R42 relationships remain authoritative.

## Next proof work

1. Replace the abstract Tigran proof art with optimized cinematic artwork.
2. Add at least one non-Barbarian class-overlay family.
3. Add the neutral fallback header to the specimen.
4. Test the same chrome on a dense repeating section and a compact sidebar.
5. Translate the specimen state selectors into a Roll20-safe hidden visual-state mapping proposal.
