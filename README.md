# IL Renewal Crammer

A practice tool for the Illinois driver's license **written renewal exam**, built to mimic the
format of the actual Secretary of State computer test: a sign appears, you pick its meaning from
four choices, and you're graded immediately.

## What's in it

Three tabs:

- **Sign Quiz** — 29 signs, shown one at a time with four multiple-choice meanings. Weighted toward
  the pairs people actually confuse: Merge vs. Lane Ends vs. Added Lane, Divided Highway Begins vs.
  Ends, Side Road's T-stem vs. Cross Road's plus, Curve vs. Winding Road, and the yellow *advisory*
  speed plate vs. the white *regulatory* speed limit.
- **Rules Quiz** — 25 Illinois-specific trick questions: exact distances, right-of-way, hill parking,
  BAC limits, Scott's Law, flashing yellow arrows.
- **Shape & Color Key** — the fallback for when you don't recognize a symbol. Shape and color alone
  narrow down the meaning (octagon = stop, downward triangle = yield, circle = railroad, and so on).

Scoring uses the real exam's 80% passing threshold, and both quizzes shuffle on every run.

## Sign artwork

The signs are **not redrawings**. They are the official Manual on Uniform Traffic Control Devices
(MUTCD) vector art published by the U.S. Federal Highway Administration — public domain as works of
the U.S. federal government — retrieved from Wikimedia Commons. Each `assets/*.svg` is the real
source file, named here by its role and mapped to its MUTCD code in `template.html`
(e.g. `stop.svg` = R1-1, `no-uturn.svg` = R3-4).

An earlier version of this tool used hand-drawn approximations. They were wrong often enough to teach
the wrong picture, which defeats the point, so they were replaced wholesale.

## Rules content

Facts are drawn from current Illinois statute rather than from memory or test-prep summaries. Some
that are easy to get backwards, with citations:

| Rule | Value | Source |
| --- | --- | --- |
| Dim high beams — oncoming | within **500 ft** | 625 ILCS 5/12-210 |
| Dim high beams — following | within **300 ft** | 625 ILCS 5/12-210 |
| Signal before turning — in town | **100 ft** | 625 ILCS 5/11-804 |
| Signal before turning — outside town | **200 ft** | 625 ILCS 5/11-804 |
| Stop at railroad crossing | **15–50 ft** from nearest rail | 625 ILCS 5/11-1201 |
| Park from a fire hydrant | no closer than **15 ft** | 625 ILCS 5/11-1303 |
| Stop for a school bus | at least **20 ft** | — |
| BAC limit, 21+ | **0.08%** | — |
| BAC limit, under 21 | **zero tolerance** | — |

The in-town vs. outside-town signal distances, and the two headlight distances, are pairs the exam
likes to swap on you.

## Build

The published page is a single self-contained HTML file — every sign is embedded as a base64 data
URI, so it works offline and has no external requests.

```sh
python3 build.py     # assets/*.svg + template.html -> il-driving-crammer.html
```

Edit `template.html` (the quiz decks live in the `SIGNS` and `RULES` arrays near the top of the
`<script>`), then re-run the build. Do not edit `il-driving-crammer.html` directly — it is generated
and will be overwritten.

## Caveat

This is a study aid, not an official Illinois Secretary of State resource. Verify anything that
matters against [ilsos.gov](https://www.ilsos.gov) before your test.
