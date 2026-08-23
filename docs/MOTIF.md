> **ARCHIVED 2026-08-23 — decision: not applied.** The site's identity became
> "the original Canva site, done right" (cream/blue re-theme, its type voices,
> its card hierarchy). Layering the committee conceit over that would fight it.
> Kept for the record; nothing below is live.

# MOTIF — THE 1810 COMMITTEE
### The locked motif for Andrew & Megan's Final Prost. An overlay on the built page, not a redesign.

Paste source: **`docs/motif-assets.html`** — every component below exists there as finished,
copy-pasteable markup, with the CSS in one `[MOTIF]` block. Open it from `file://`.

---

## 0. READ THIS FIRST — two things changed under this motif

**(a) The page is now V2.** `docs/REDESIGN-V2.md` removed the persona generator. There is no
name input, no beer-mat card, no `persona()`, no 32-bit hash, no `.tap-stamp`. Any motif idea
that hung off the persona card — delegation codes, a deterministic `Licence No. ANK-3F2C`, a
re-lettered rubber stamp — is **dead by construction** and is not in this spec. The signature
moment is now the scroll-driven stein (§9).

**(b) There is a live blocker that must land before any motif CSS.** See §10. It is not a motif
issue and it is currently breaking the stein.

---

## 1. THE CONCEPT, AND THE JOKE IT MAKES

The weekend is treated as a sanctioned international sporting event, and the page is re-framed as
the **document packet issued by its governing body — The 1810 Committee.**

1810 is the year Oktoberfest was founded, *as a wedding party* (Ludwig and Therese, 12 October
1810). That makes this committee's jurisdiction over a bach party genuinely correct rather than a
gag, and it is why the footer seal can say **"Founded at a Wedding"** and mean it.

**The joke is total institutional commitment to lawn games.** Nobody on the page ever admits it
is a party. Every section becomes a numbered Bulletin, the packing list becomes a filed Form, the
scoreboard is an empty medal table awaiting engraving, and there is an oath in three articles.
The comedy lives entirely in the gap between that apparatus and the fact that the main event is
yard games in Iowa. **The frame does the joking. The copy inside the frame is dead straight.**

It also does the inclusion work structurally rather than in a sentence. The root beer is not
accommodated and never explained: it is a discipline with a pictogram, an article of the oath,
and a line in the official record — in the same ink, the same case, the same weight as everything
else. See §4 component F, which is the single most load-bearing idea in this document.

**Why this one.** Two of the three review lanes picked it outright. It is the only concept whose
frame is already inside the client's brief — the client said "Beer Olympics"; this simply refuses
to treat that as a figure of speech. Olympic ceremony is natively both epic and corny to an
American audience, so neither register has to be manufactured. And critically, the guest is
*inside* the grandeur — enrolled, registered, scored — rather than being shown grandeur about
themselves, which is the difference between a page the room laughs *with* and one it suspects is
laughing at it.

---

## 2. WHAT WAS GRAFTED IN, AND WHY

| From | Grafted | Why it was needed |
|---|---|---|
| **The Two Acres** | The **Lebkuchenherz** (§4 D), once, in the masthead | The Committee frame is grand, funny and *emotionally cold*. Two lanes independently prescribed this as the cure. It is the one sincere object on the page — and it is not a foreign body, it is the Committee's founding artifact, the proof of "Founded at a Wedding." One warm object buys the other 2,600 lines the right to stay deadpan. |
| **The Two Acres** | The **flat-guard rail** (§7) | The only guard of the three enforced *in the stylesheet* rather than in a grep a reviewer must remember to run. It makes the bevel/gradient collapse impossible to add by accident. |
| **The Broadcast** | The **bulletin absorbs the section number and kicker** (§4 B) | Games as written stacked a bulletin *above* the retained `.section-num` and `.section-kicker` — four label layers before the title. Absorbing them makes it three, so the apparatus costs no height at 380px. It pays for itself. |
| **The Broadcast** | **Facts-only pictograms, four not six** (§4 F) | Decisive correction. Games named six events (Stein Hoist, Flip Cup, Keg Toss…). **`docs/CONTENT.md` contains no event list** — naming them would invent values, violating the acceptance rule "zero invented values; every [PENDING] a visible TBD." Broadcast got this right: every pictogram depicts a fact the page already asserts, and the unsettled slate is rendered as a visible TBD, which is also the funniest line in the section. |
| **The Broadcast** | The **clerical register** for Bring / Budget / German (§3) | The sections where a guest needs instructions, not atmosphere, are deliberately de-ceremonialised. This is Games' own ceremonial/clerical split, reinforced. |
| **The Broadcast** | The **countdown bug** (§4 I) and the **facts strip** (§4 L) | Every other device here is retrospective apparatus. The bug is the only one that points forward and gives the page a pulse. The facts strip is the six things a person scanning from a group text actually wants. |

**Deliberately not taken:** the roster reordering that moved the bride to last in her own roster to
satisfy a bit. Putting a gag ahead of the bride, on a page her mother will read, is a warmth cost
no budget comment catches. Rosters stay exactly as they are.

---

## 3. THE MOTIF SYSTEM — HOW IT REPEATS, AND HOW THE REGISTER CHANGES

### The recurring mark
**The Sanction Mark** (`.mark`) — an 18px hairline square holding one solid amber **fusil**: a
diamond taller than it is wide, which is the correct Bavarian form, not a square on point. Pure
CSS, six lines, no SVG.

It is deliberately **the same 45° geometry as the page's existing `.lozenge` texture and
`.tbd::before`**. The ambient paper and the committee's mark are one shape at two scales. That is
what welds the motif to the built page instead of letting it sit on top.

### Three tiers, strictly rationed

| Tier | Element | Count |
|---|---|---|
| Seal | The Committee Seal | **1** — footer only |
| Header | The Bulletin line | **7** — one per numbered section |
| Mark | The Sanction Mark | **≤ 12** total |

### The register change is vocabulary, never decoration
The apparatus never changes: same mono, same hairline rule, same mark, same tracking. **Only the
noun and the status word change.** The committee that stages the ceremony also files the
paperwork, and the paperwork is deliberately flatter.

| | **Ceremonial** — §01, §05, the Saturday block, masthead, footer | **Clerical** — §03 Bring, §06 Budget, §07 German |
|---|---|---|
| Noun | BULLETIN · PROTOCOL · OATH · SANCTIONED · ENGRAVED | FORM · APPENDIX · MANIFEST · SCHEDULE |
| Rule | `.rule--protocol` — hairline with a 3px amber rule offset below | plain existing `.rule` |
| Voice | declarations — *"The Committee scores the mug."* | instructions — *"Six items. No substitutions."* |

`.day`-scoped sections (§02 Attire, §04 The Stay) need no extra markup: every motif element is
built from `--accent`, `--line`, `--line-strong` and `--registry`, all of which re-point inside
`.day`. They re-skin free.

**Do not make the clerical sections funnier to compensate. Flatter is better there.**

### Status vocabulary is load-bearing
Settled sections read **IN FORCE** or **FINAL**. They must never read `PROVISIONAL`, `REV. 3` or
`PENDING`. A mother reading *"ACCOMMODATION · PROVISIONAL"* on a phone does not read wit — she
reads *"is the house not booked?"*, and SPEC hard-requires that Friday reads settled. Only §06
Budget, whose figures genuinely are open, is permitted to say **FIGURES PENDING**.

The seven exact strings:

| § | Bulletin line | Read line (replaces the old kicker) |
|---|---|---|
| 01 | Bulletin 01 · Order of Ceremony · In Force | Friday splits · Saturday and Sunday are everyone |
| 02 | Appendix A · Equipment Regulations · In Force | Seven slots · two columns · no guessing |
| 03 | Form 03 · Competitor Kit Manifest · In Force | Pack once · six things |
| 04 | Bulletin 04 · Village & Accommodation · In Force | Where we all land |
| 05 | Bulletin 05 · Register of Competitors · Final | Thirty-three names, one weekend |
| 06 | Form 06 · Schedule of Fees · Figures Pending | What it costs, honestly |
| 07 | Appendix 07 · Language & Pronunciation · Advisory | 15 words, one weekend |

---

## 4. COMPONENT INVENTORY

All pure CSS or inline SVG. No image files, no icon libraries, no external request but Google
Fonts. Finished markup for every one is in `docs/motif-assets.html`.

| | Component | Purpose | Where it goes | Count |
|---|---|---|---|---|
| **A** | `.mark` | The recurring mark; the page's heartbeat | First child of every bulletin; top-right of every `.card--official`; flanking the seal legend | ≤ 12 |
| **B** | `.bulletin` | Turns a section head into a filed document header | First child of each of the 7 `.section-head`s. **Replaces `.section-num` and `.section-kicker` — delete both** | 7 |
| **C** | `.dateline` | Declares the whole page a document packet | Masthead, immediately after `.masthead-where` | 1 |
| **D** | `.lebkuchen` | The gingerbread heart; the one sincere object | Inside the dateline | 1 |
| **E** | `.seal` | Signs the document | Footer, between `.footer-top` and `.footer-lock` | 1 |
| **F** | `.picto` | The disciplines, and the inclusion device | 4-up row inside the Saturday `.tap-tie` | 4 |
| **G** | `.medals` | Empty ceremonial furniture; the visible TBD | A sibling card after the Saturday itinerary `</article>` | 1 |
| **H** | `.oath` | The ceremonial high point | Saturday `.tap-tie`, beneath the pictograms | 1 |
| **I** | `.bug` | The one forward-pointing device | `.navbar-inner`, after `.navbar-mark` | 1 |
| **J** | `.manifest` | §03 as a filed form | Add the class to the existing `.bring-list` | 1 |
| **K** | `.card--official` | Corner mark treatment | Medal table, oath host, Stay hero — **and nothing else** | 3 |
| **L** | `.bottomline` | The six facts a phone reader wants | Full-bleed, immediately before `<footer>` | 1 |

### Notes on the three that carry the most weight

**F · The pictograms — the inclusion device is geometry.**
Aicher/Paris-2024 grammar: ground rule + object + axis, no faces, no motion lines, so they cannot
go corny. Identical construction across all four — `viewBox="0 0 64 64"`, `fill="none"`,
`stroke="currentColor"`, `stroke-width="4"`, square caps, miter joins, edges at **0°/45°/90° only**,
shared ground rule `M6 56 H58`.

The four are **Maß, Root Beer, Shoe-slap, Currywurst** — each backed by a fact already on the page.
**The root beer mug is the *identical path* to the Maß**, plus a straw: same body, same handle,
same stroke weight, same colour. The system cannot tell the two mugs apart, so neither can the
medal table. That is inclusion delivered as a shape rather than as a sentence, which is exactly
what "a running joke, never a disclaimer" asks for. **Never give that cell a qualifier, an
asterisk, or a softer colour.**

Beneath the row: `DISCIPLINES · FOUR SHOWN · FULL SLATE [TBD]`. Spec-compliant, honest, and the
funniest line in the section, because "slate pending" is exactly what a real federation would print.

**E · The seal — the rule of tincture, enforced.**
Metals (cream, amber) never touch metals; colours (blue) never touch colours. A cream chief
carrying blue fusils; a blue field carrying the amber Anstich mallet (the mayor's keg-tapping
hammer), which is the only charge. Two tinctures, one charge, 0°/45°/90° edges, no gradient, no
bevel. This 700-year-old rule is also a contrast guarantee, which is why the seal passes the 1-bit
test by construction. **Gingerbread red is deliberately not promoted to a heraldic field** — that
is the one place this motif could go somewhere ugly.

**D · The heart — and the sanctioned curve.**
Geometric: two arcs of one radius and two straight edges to a point, flat gingerbread red, with
piped icing drawn as a precise dashed stroke (never wobbled). The names are set in Barlow
Condensed as HTML positioned over the SVG — **no script face, no SVG text, no second Fraktur.**

> **THE SANCTIONED CURVE.** The heart's two arcs and its round-capped icing dots are the page's
> **one permitted curve**, in the same way the old rubber stamp was its one permitted tilt.
> Everything else in this motif is 0°/45°/90° only. This must stay written down, or the next
> editor either deletes the heart for breaking the rule or starts adding curves elsewhere.

---

## 5. TYPOGRAPHY

**No new face. Fraktur is spent on `.masthead-wordmark` and stays spent — this motif spends zero.**
Ceremonial weight comes from tracking, rules, caps and enumeration, never from a fancier letterform.

| Role | Spec |
|---|---|
| Bulletin, dateline-sub, seal legend, manifest close | JetBrains Mono 500, `--step--2`, uppercase, `letter-spacing:.18em–.24em`, `--text-faint`; the leading number always `--accent` 700 |
| Declarations — oath, dateline-main | Barlow Condensed 600/700, `--step-0`, uppercase or sentence case, `letter-spacing:.02em–.14em`, cream, between `.rule--protocol` |
| Data — medal table, bug, bulletin numbers | JetBrains Mono, `font-variant-numeric:tabular-nums`, **leading zeros always** (`01`, `03`) |
| Body, instructions, the `.bulletin-read` line | Unchanged Barlow Condensed 400/600. **The motif never reaches into readable prose.** |

**Hard rules.** No italics in any ceremonial string. **No exclamation marks anywhere in committee
voice.** No ornamental drop caps, no small-caps fakery, no letter-spaced lowercase. Roman numerals
confined to the dateline only — the plain date sits directly above it, so the page never makes a
guest do arithmetic. Ordinals spelled out in declarations ("the First Oktoberfest Olympiad"),
digits everywhere else.

---

## 6. COLOUR

Everything comes from the existing tokens, in fixed roles:

- `--amber-400` — the mark's fusil, bulletin numbers, protocol rule, pictogram stroke.
  **Amber is the committee's authority.** It already owns the CTAs, so this reads as continuity.
- `--blue-600` — the seal's field, and the bug's code block. Blue stays Bavaria.
- `--cream-200` — the seal's chief, hairlines, body text.
- `--red-500` — the gingerbread heart only. Never a heraldic field, never promoted.

### The one added accent — `--registry`

```css
:root{ --registry:#8b9cb4; }   /* night */
.day {  --registry:#4f5b70; }  /* day   */
```

**Document furniture only:** bulletin separators and status words, the empty medal cells, the seal
legend, the manifest check boxes. It is the colour of engraved security printing — it gives the
empty medal table a *filed* quality rather than a *missing* one, and it keeps furniture from
competing with amber. **It never sets a sentence and it is never a CTA.**

It is defined as a **semantic token that re-points under `.day`, exactly like every other token in
the sheet, and this is not optional.** A single flat value fails: `#8b9cb4` measures 6.21:1 on
`--night-800` and 4.85:1 on `--night-600`, but only **2.60:1 on `--day-200`** — and bulletins
appear in §02 and §04, which are `.day`-scoped. The day value measures 5.35:1 on `--day-200`.
Both clear AA for the small mono they carry. *(All ratios measured, not estimated.)*

Nothing else is added. No green, no brown, no metallics.

---

## 7. COPY VOICE

Declarative, present tense, literally true, never winking. A statement of fact about a trivial
thing, delivered at full institutional weight, and then it stops.

> **GAMES OF THE FIRST OKTOBERFEST OLYMPIAD · DES MOINES · 19.IX.2026 · SANCTIONED BY THE 1810 COMMITTEE**

> **ART. I.** Every trial is winnable stone-cold sober.
> **ART. II.** The Committee scores the mug, not its contents.
> **ART. III.** Root beer is entered, scored and engraved on the same table as everything else.

> **MEDAL TABLE · ALL COLUMNS EMPTY BY DESIGN · RESULTS TO BE ENGRAVED SATURDAY, AFTER DARK**

> **FORM 03 · SIX (6) ITEMS · NO SUBSTITUTIONS · A COMPETITOR ARRIVING WITHOUT A LAWN CHAIR COMPETES STANDING**

> *Lebkuchenherz* — gingerbread heart. Say it "LAYP-koo-khen-hairts." In Munich you buy one for someone you like.

Note what none of them do: none says "just kidding," none has an exclamation mark, none tells you
it is a joke, and none is at anyone's expense. Every one is a statement that is literally true.

**The German rule.** This motif adds exactly one German word — *Lebkuchenherz* — and it is glossed
in English with a phonetic respelling at its only use. The apparatus is otherwise inherently
English, so the motif cannot leak German into any copied text.

---

## 8. GUARD RAILS

### What would make this collapse

**The risk is dilution into wallpaper.** Officialdom is a system, and systems are cheap to apply —
so the mark ends up on all thirty-odd cards, every list gets a form number, and within one scroll
the apparatus stops being a straight-faced institution and becomes texture. **That is the exact
moment "epic and corny" collapses into merely cheesy** — not because any single element is bad,
but because the frame stops carrying meaning.

The runner-up risk is an **execution** failure: one bevel, one gradient "gold" fill, one drop
shadow on the shield, one `skew()` on a rule, and the seal becomes a fantasy-tavern sticker. That
one is dangerous because the copy can be perfect and the page still dies.

### The guards

**(a) A published, greppable budget.** It ships as a comment at the top of the motif CSS.
**These counts are the design.**

```
.seal 1 · .dateline 1 · .lebkuchen 1 · .bulletin 7 · .mark ≤12
.card--official 3 · .picto 4 · .oath 1 · .medals 1 · .bottomline 1 · .bug 1
Fraktur 0 (already spent)   supporters 0   bevels 0   gradients 0
```

Verify against `index.html` after pasting:

```bash
grep -c 'class="bulletin"'  index.html   # 7
grep -o 'class="mark'       index.html | wc -l   # <= 12
grep -o 'class="picto'      index.html | wc -l   # 4
grep -c 'class="seal"'      index.html   # 1
grep -c 'card--official'    index.html   # 3
grep -c 'UnifrakturMaguntia\|font-fraktur' index.html   # unchanged from before the paste
```

**(b) The flat guard, enforced in the stylesheet — not in a grep somebody has to remember.**

```css
.mark,.seal,.picto,.lebkuchen,.bulletin,.bug,.oath,.medals,
.mark *,.seal *,.picto *,.lebkuchen *,.bug *{
  filter:none !important; box-shadow:none !important;
  text-shadow:none !important; border-radius:0 !important;
}
.seal *,.picto *,.lebkuchen *{ stroke-linejoin:miter; stroke-linecap:square; }
```

The hard `4px 4px 0` shadow stays on `.card--raised` — that is a print artifact on paper stock, a
different and legitimate register. **A seal never casts a shadow.**

**(c) The 1-bit test — a hard gate before any motif change merges.**

```css
html.bit{filter:grayscale(1) contrast(8)}
```

Every device must still read with all colour removed. **Do not gate by forcing
`fill:#000 !important`** — that solid-fills every open pictogram and the whole seal, and reports a
failure where there is none. The definitive version is a raster threshold of a real screenshot.

*This was run.* All four pictograms, the seal (every charge individually), the mark and the heart
survive at 380px in pure black and white. They pass by construction: single stroke weight, flat
fills, no bevels, no tonal steps.

**(d) The read-aloud test.** Any guest must be able to read any line at the table and be pleased.
The grandeur points at the weekend itself and at nothing else. If a line's humour depends on a
guest, a town, or Germans being the butt, cut it.

---

## 9. HOW THIS STAYS OUT OF THE WAY OF THE POUR

**The pour is now the scroll-driven stein** (`.stein`, `index.html` PART 7) — full when you land,
emptying as you scroll, refilling with a brief pour animation, counting `Maß #2`, `#3`. It is the
page's ONE signature moment and its **only moving part.**

The motif's relationship to it is: **no contact at all.**

1. **This motif animates nothing.** Not one transition, not one keyframe. The stein remains the
   only thing that moves on the page. A reduced-motion block is included for the motif classes
   anyway, so that if a future editor adds a transition to a motif element, reduced motion still
   wins.
2. **Nothing is placed in the stein's corner.** The stein is `position:fixed`, `z-index:60`, top
   right below the navbar — and bottom right below 30rem. The countdown bug is the only motif
   element in the navbar; it sits **left**, immediately after `.navbar-mark`, and its clock hides
   below 24rem so it can never crowd the nav toggle or reach the stein's corner. No motif element
   is fixed, sticky, or above `z-index:1` except the `.bottomline`'s sticky FACTS flag, which is
   scoped inside its own scroll container.
3. **No motif element competes for the signature slot.** No second hero object, no full
   achievement, no crest in the masthead. The seal is one small mark in the footer, 116px, at the
   very bottom of the page. The heart is 132px inside the dateline. Neither is placed above the
   fold's primary content.
4. **The stein's own CSS is untouched.** The motif adds a new PART 8 block at the end of the
   stylesheet and edits nothing that already exists — with the single exception of deleting
   `.section-num` and `.section-kicker` *elements* from seven section heads (their CSS rules stay,
   harmless, in case of reuse).

**The one real danger to the pour is not this motif — it is §10, which is currently breaking it.**

---

## 10. BLOCKER — FIX BEFORE ANY MOTIF CSS LANDS

`index.html` **lines 858–887** are orphaned CSS declaration blocks whose selectors were stripped
when the persona section was removed. They are not merely dead — the CSS parser consumes them as a
malformed qualified rule and **swallows the next valid rule after each one.**

Verified in Chromium against the live file, not inferred:

| Rule | Status now | Consequence |
|---|---|---|
| `.stein` | **dropped** | computed `position:static`, `top:auto`, `z-index:auto` — **the scroll-driven stein is not a fixed fixture at all.** It renders inline in the flow between the navbar and `<main>`. The page's signature moment is broken right now. |
| `.input[aria-invalid="true"]` | **dropped** | the non-colour-only invalid cue is dead — an accessibility rule |

Stylesheet rule count goes **290 → 292** when fixed.

**The fix:** delete lines **858–877** and **879–887** — 29 lines. Keep line 878
(`.input[aria-invalid="true"]{…}`), which is the one valid rule stranded inside the region.

This is dangerous beyond those two rules because **the casualty moves.** Whichever rule happens to
follow the orphan block gets eaten — it was the reduced-motion block in an earlier revision, it is
`.stein` today. **If PART 8 is pasted anywhere near it, the motif's own CSS becomes the next
casualty.** Land the deletion first, then paste.

### Landing order

1. Delete the 29 orphaned lines. Confirm `.stein` computes `position:fixed` again.
2. Paste the `[MOTIF]` CSS block as **PART 8**, at the very end of `<style>`, after the
   reduced-motion block.
3. Paste the markup, section by section, from `docs/motif-assets.html`.
4. Run the §8 greps, the 1-bit gate, and a 380px pass.

### Also worth fixing while in there — stale copy from the removed feature

Two glossary entries still describe the deleted persona generator and will confuse a reader:

- `Prüfung` — *"Yours gets handed to you when you pour your fate…"*
- `Bierdeckel` — *"Your poured fate arrives stamped on one."*

Neither is a motif issue; both are V2 leftovers. Reword or drop.

---

## 11. VERIFIED AT BUILD TIME

- Renders correctly from `file://` at **380px**, no horizontal page scroll, nothing clipped.
- **All tap targets ≥ 44px** (the `.bottomline` was 42px in draft and was raised to `var(--tap)`).
- The **1-bit test passes** for every component (raster threshold of a real 380px render).
- Motif CSS contains **zero** `gradient(`, `skew(`, `text-shadow`, non-zero `border-radius`, or
  non-`none` `filter`. Zero exclamation marks in committee copy.
- `--registry` contrast measured on every surface it is used on; both scope values clear AA.
- The `.day` sections re-skin with no extra markup.
- Google Fonts is the only external request; every asset is inline SVG or pure CSS.
