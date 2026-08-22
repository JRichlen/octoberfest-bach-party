# V2 REDESIGN BRIEF — locked decisions from the client (2026-08-21)

The client reviewed the live v1 and ruled. These override SPEC.md where they conflict.
CONTENT.md remains the fact authority (rosters, addresses, times, TBDs, German rule).

## 1. KILL "Pour my fate" as a section
The persona generator ("The Tap", section 01) is a waste: a wall of text, a lot of prose,
a distraction. Remove the whole interactive section: name input, pour button, beer-mat
card, ranks/epithets/stats/dares/toasts, its JS and its CSS. The German 101 glossary
STAYS. The Saturday Beer Olympics block stays but loses its "your Prüfung is in effect /
Pour my fate" tie-in — rewrite that note to be about the Beer Olympics itself.

## 2. The stein becomes a SCROLL-DRIVEN page fixture
The beer-filling visual was the funny part — keep the stein, promote it to a small
persistent page element (top corner near the masthead/nav, unobtrusive at 380px):
- It starts FULL when you land.
- It EMPTIES as you scroll down (drink level tracks scroll progress).
- When it hits empty, a REFILL pours it back to full (brief pour animation),
  and it starts emptying again on further scroll. A tiny counter of refills is
  welcome ("Maß #3" style, German glossed once) but optional.
- prefers-reduced-motion: no animation — a static stein, no level changes, or a
  simple stepped level without transitions. No scroll-jacking, passive listener,
  requestAnimationFrame-throttled.

## 3. Gals / Guys gate on arrival
On first load the visitor picks **Gals** or **Guys** (two big buttons, an obvious
switch to change later — a toggle in the header). No storage: default state on every
load is the chooser; the choice only lives for the page session in JS state.
- The choice filters FRIDAY: Guys see the lads' settled Friday schedule; Gals see
  the ladies' Friday. The other column is hidden, not rendered side by side.
- Saturday and Sunday are shown to BOTH (they're shared).
- Attire grid: show both columns (everyone needs to know the colour rules), but
  it's fine to emphasise the chosen side.
- The word on screen is "Gals" / "Guys" for the chooser; the rosters keep their
  "The Ladies" / "The Lads" titles from CONTENT.md.
- The gate must not block reading: choosing is one tap, switching is always visible,
  and deep links (#stay etc) still work — if someone arrives via a hash link, don't
  trap them behind the chooser; show the chooser as a dismissible banner instead.

## 4. Costumes fold into Saturday
Already true in v1 (the "Need a costume?" block lives in Saturday's Beer Olympics
entry) — keep it there, it survives the redesign untouched. The attire section's
"see the options" cross-link stays.

## 5. Rosters move to the side gutters
"Meet the Party" stops being a big section. On wide screens (≥ ~64rem) the 33 people
run down the LEFT and RIGHT page gutters as small portrait cards — photos with the
name + role, taken from the original site (the photo-data pipeline already provides
them; four people have monogram fallbacks). Ladies one side, Lads the other.
- The gutters are decorative rails: position: fixed or sticky columns outside the
  main content column, scrolling with (or subtly slower than) the page.
- On phones (< 64rem) there are no gutters — the rosters collapse back into a compact
  section (small grid of photo + name + role), placed where section 06 was. Do not
  drop anyone on mobile.
- The img.roster-photo / span.roster-monogram + photo-data hydration contract from
  SPEC.md §Meet the Party is UNCHANGED — same markup shape, same script block, blob
  stays {} until the build step injects it.

## 6. Everything else stands
Design system, palette, nav (renumber for the removed section), German rule, TBD
rules, footer line, no external requests beyond Google Fonts, one file, no storage,
380px-first, a11y bar — all as in SPEC.md. The nav loses "The Tap" and gains nothing.
