#!/usr/bin/env python3
"""Embed the official MUTCD sign SVGs into the crammer HTML as base64 data URIs."""
import base64
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"
TEMPLATE = HERE / "template.html"
OUT = HERE / "il-driving-crammer.html"

EXPECTED = [
    "stop", "yield", "rr-advance", "crossbuck", "no-pass", "school",
    "merge", "lane-ends", "added-lane", "div-begin", "div-end", "two-way",
    "side-road", "cross-road", "winding", "curve", "chevron", "grade",
    "deer", "ped-x", "bike-x", "signal-ahead", "stop-ahead", "dne",
    "wrong-way", "no-uturn", "advisory", "speed-limit", "work-zone",
]

entries = {}
missing = []
for key in EXPECTED:
    path = ASSETS / f"{key}.svg"
    if not path.exists() or path.stat().st_size < 150:
        missing.append(key)
        continue
    raw = path.read_bytes()
    # Sanity: must actually be SVG, not an error page.
    if b"<svg" not in raw[:2000]:
        missing.append(key)
        continue
    b64 = base64.b64encode(raw).decode("ascii")
    entries[key] = f"data:image/svg+xml;base64,{b64}"

js = "{\n" + ",\n".join(
    f'    "{k}": "{v}"' for k, v in entries.items()
) + "\n  }"

html = TEMPLATE.read_text()
if "__SIGN_DATA__" not in html:
    sys.exit("ERROR: template is missing the __SIGN_DATA__ placeholder")
html = html.replace("__SIGN_DATA__", js)
OUT.write_text(html)

kb = OUT.stat().st_size / 1024
print(f"embedded {len(entries)}/{len(EXPECTED)} signs -> {OUT.name} ({kb:.0f} KB)")
if missing:
    print("MISSING (will be skipped in the quiz):", ", ".join(missing))
else:
    print("all signs present")
