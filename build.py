#!/usr/bin/env python3
"""Build the crammer.

Emits two things from the same source (template.html + assets/*.svg):

  il-driving-crammer.html  a body fragment for a Claude Artifact (the host supplies
                           the <html>/<head> wrapper itself)
  docs/index.html          a standalone, installable page for GitHub Pages, plus a
                           content-stamped service worker for offline use

Every sign is inlined as a base64 data URI, so the page makes no external requests.
"""
import base64
import hashlib
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
ASSETS = HERE / "assets"
DOCS = HERE / "docs"
TEMPLATE = HERE / "template.html"
SW_TEMPLATE = HERE / "sw-template.js"
ARTIFACT_OUT = HERE / "il-driving-crammer.html"
PAGE_OUT = DOCS / "index.html"
SW_OUT = DOCS / "sw.js"

SIGNS = [
    "stop", "yield", "rr-advance", "crossbuck", "no-pass", "school",
    "merge", "lane-ends", "added-lane", "div-begin", "div-end", "two-way",
    "side-road", "cross-road", "winding", "curve", "chevron", "grade",
    "deer", "ped-x", "bike-x", "signal-ahead", "stop-ahead", "dne",
    "wrong-way", "no-uturn", "advisory", "speed-limit", "work-zone",
]

# --- collect sign artwork ----------------------------------------------------
entries, missing = {}, []
for key in SIGNS:
    path = ASSETS / f"{key}.svg"
    if not path.exists() or path.stat().st_size < 150:
        missing.append(key)
        continue
    raw = path.read_bytes()
    if b"<svg" not in raw[:2000]:  # guard against an error page saved as .svg
        missing.append(key)
        continue
    entries[key] = "data:image/svg+xml;base64," + base64.b64encode(raw).decode("ascii")

sign_js = "{\n" + ",\n".join(f'    "{k}": "{v}"' for k, v in entries.items()) + "\n  }"

template = TEMPLATE.read_text()
if "__SIGN_DATA__" not in template:
    sys.exit("ERROR: template.html is missing the __SIGN_DATA__ placeholder")
body = template.replace("__SIGN_DATA__", sign_js)

# --- 1. artifact fragment ----------------------------------------------------
ARTIFACT_OUT.write_text(body)

# --- 2. standalone installable page ------------------------------------------
DOCS.mkdir(exist_ok=True)

# Registered only here; the artifact sandbox has no service workers.
sw_register = """<script>
if ("serviceWorker" in navigator) {
  addEventListener("load", function () {
    navigator.serviceWorker.register("./sw.js").catch(function () {});
  });
}
</script>"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Practice for the Illinois driver's license written renewal exam: road sign identification using official MUTCD artwork, plus Illinois rules trick questions.">
<meta name="theme-color" content="#00693e">
<link rel="manifest" href="./manifest.webmanifest">
<link rel="icon" href="./icons/icon-192.png">
<link rel="apple-touch-icon" href="./icons/icon-180.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="IL Crammer">
<style>
  /* The artifact host supplies a reset; standalone has to bring its own. */
  *, *::before, *::after {{ box-sizing: border-box; }}
  html {{ -webkit-text-size-adjust: 100%; }}
  body {{ margin: 0; overflow-x: hidden; }}
  img {{ max-width: 100%; }}
  /* Widen the gutter to clear the notch once installed. The header's full-bleed
     offset is derived from --pad, so it tracks this automatically. */
  :root {{ --pad: max(16px, env(safe-area-inset-left), env(safe-area-inset-right)); }}
  footer.plate {{ padding-bottom: env(safe-area-inset-bottom); }}
</style>
</head>
<body>
{body}
{sw_register}
</body>
</html>
"""
PAGE_OUT.write_text(page)

# --- 3. service worker, stamped with a hash of the page ----------------------
version = hashlib.sha256(page.encode()).hexdigest()[:12]
SW_OUT.write_text(SW_TEMPLATE.read_text().replace("__CACHE_VERSION__", version))

(DOCS / ".nojekyll").write_text("")  # GitHub Pages: skip Jekyll processing

print(f"signs embedded : {len(entries)}/{len(SIGNS)}")
print(f"artifact       : {ARTIFACT_OUT.name} ({ARTIFACT_OUT.stat().st_size / 1024:.0f} KB)")
print(f"page           : docs/index.html ({PAGE_OUT.stat().st_size / 1024:.0f} KB)")
print(f"service worker : docs/sw.js (cache il-crammer-{version})")
if missing:
    print("MISSING (skipped):", ", ".join(missing))
