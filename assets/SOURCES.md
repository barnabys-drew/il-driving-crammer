# Sign asset provenance

All files in this directory are official **MUTCD** (Manual on Uniform Traffic Control Devices) sign
artwork published by the U.S. Federal Highway Administration. As works of the U.S. federal
government they are in the **public domain**. Retrieved from Wikimedia Commons.

| File | MUTCD code | Sign |
| --- | --- | --- |
| `stop.svg` | R1-1 | Stop |
| `yield.svg` | R1-2 | Yield |
| `dne.svg` | R5-1 | Do Not Enter |
| `wrong-way.svg` | R5-1a | Wrong Way |
| `no-uturn.svg` | R3-4 | No U-Turn |
| `speed-limit.svg` | R2-1 | Speed Limit |
| `crossbuck.svg` | R15-1 | Railroad Crossbuck |
| `rr-advance.svg` | W10-1 | Railroad Advance Warning |
| `no-pass.svg` | W14-3 | No Passing Zone (pennant) |
| `school.svg` | S1-1 | School Zone / Crossing |
| `merge.svg` | W4-1 | Merge |
| `lane-ends.svg` | W4-2 | Lane Ends |
| `added-lane.svg` | W4-3 | Added Lane |
| `div-begin.svg` | W6-1 | Divided Highway Begins |
| `div-end.svg` | W6-2 | Divided Highway Ends |
| `two-way.svg` | W6-3 | Two-Way Traffic |
| `cross-road.svg` | W2-1 | Cross Road |
| `side-road.svg` | W2-2 | Side Road |
| `curve.svg` | W1-2L | Curve |
| `winding.svg` | W1-5R | Winding Road |
| `chevron.svg` | W1-8L | Chevron Alignment |
| `grade.svg` | W7-1 | Steep Grade / Hill |
| `deer.svg` | W11-3 | Deer Crossing |
| `ped-x.svg` | W11-2 | Pedestrian Crossing |
| `bike-x.svg` | W11-1 | Bicycle Crossing |
| `signal-ahead.svg` | W3-3 | Signal Ahead |
| `stop-ahead.svg` | W3-1 | Stop Ahead |
| `advisory.svg` | W13-1P | Advisory Speed Plate |
| `work-zone.svg` | W20-1 | Road Work Ahead |

Note: a few signs are directional variants on Commons (`W1-2L`, `W1-5R`, `W1-8L`) — the base code
redirects to the left/right version.

## Re-fetching

Canonical URL pattern:

```
https://commons.wikimedia.org/wiki/Special:FilePath/MUTCD_<code>.svg
```

Wikimedia rate-limits bulk downloads and will return **HTTP 429** with a `retry-after` (10 minutes
when this set was pulled). Space requests out and honor the header.
