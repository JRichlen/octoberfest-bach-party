#!/usr/bin/env python3
"""Inject the roster photo data URIs into index.html's <script id="photo-data"> block.
Idempotent: always replaces the block's contents wholesale."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
html = (root / "index.html").read_text(encoding="utf-8")
photos = json.loads((root / "docs" / "photos.json").read_text(encoding="utf-8"))
blob = json.dumps(photos, separators=(",", ":"))
pat = re.compile(r'(<script id="photo-data" type="application/json">)(.*?)(</script>)', re.S)
if not pat.search(html):
    sys.exit("ERROR: photo-data script block not found in index.html")
html = pat.sub(lambda m: m.group(1) + blob + m.group(3), html, count=1)
(root / "index.html").write_text(html, encoding="utf-8")
print(f"injected {len(photos)} photos, {len(blob)//1024} KB; index.html now {len(html)//1024} KB")
