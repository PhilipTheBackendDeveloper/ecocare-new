#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Coming Soon Deployment Builder
Generates an isolated, production-ready standalone Coming Soon site in dist/coming-soon/.
"""

import os
import sys
import shutil
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / "dist" / "coming-soon"

REQUIRED_ASSETS = [
    # HTML source
    ("coming-soon.html", "index.html"),
    # Core CSS
    ("css/normalize.css", "css/normalize.css"),
    ("css/main.css", "css/main.css"),
    ("css/bootstrap.min.css", "css/bootstrap.min.css"),
    ("css/fontawesome-all.min.css", "css/fontawesome-all.min.css"),
    ("css/animate.min.css", "css/animate.min.css"),
    ("font/flaticon.css", "font/flaticon.css"),
    ("style.css", "style.css"),
    # Images & Branding
    ("img/favicon.png", "img/favicon.png"),
    ("img/large-logo.png", "img/large-logo.png"),
    ("img/figure/coming-soon.jpg", "img/figure/coming-soon.jpg"),
    # Core JS
    ("js/jquery-3.3.1.min.js", "js/jquery-3.3.1.min.js"),
    ("js/popper.min.js", "js/popper.min.js"),
    ("js/bootstrap.min.js", "js/bootstrap.min.js"),
    ("js/coming-soon-countdown.js", "js/coming-soon-countdown.js"),
]

def clean_dist():
    """Removes previous build output in dist/coming-soon."""
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    print(f"✓ Cleaned and prepared {DIST_DIR}")

def copy_individual_assets():
    """Validates and copies individual files."""
    for src_rel, dst_rel in REQUIRED_ASSETS:
        src = ROOT_DIR / src_rel
        dst = DIST_DIR / dst_rel
        if not src.exists():
            print(f"❌ ERROR: Missing required source file: {src}", file=sys.stderr)
            sys.exit(1)
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    print(f"✓ Copied {len(REQUIRED_ASSETS)} core static assets.")

def copy_directory_trees():
    """Copies font trees (FontAwesome webfonts and Flaticon)."""
    # 1. webfonts/
    src_webfonts = ROOT_DIR / "webfonts"
    dst_webfonts = DIST_DIR / "webfonts"
    if src_webfonts.exists():
        dst_webfonts.mkdir(parents=True, exist_ok=True)
        for item in src_webfonts.glob("*"):
            if item.is_file():
                shutil.copy2(item, dst_webfonts / item.name)
        print("✓ Copied FontAwesome webfonts.")
    else:
        print("⚠️ Warning: webfonts directory not found in root.", file=sys.stderr)

    # 2. font/
    src_font = ROOT_DIR / "font"
    dst_font = DIST_DIR / "font"
    if src_font.exists():
        dst_font.mkdir(parents=True, exist_ok=True)
        for item in src_font.glob("*"):
            if item.is_file():
                shutil.copy2(item, dst_font / item.name)
        print("✓ Copied Flaticon font assets.")

def write_netlify_headers():
    """Generates standard security headers for Netlify deployment."""
    headers_content = """/*
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
"""
    headers_file = DIST_DIR / "_headers"
    headers_file.write_text(headers_content, encoding="utf-8")

    netlify_toml_content = """[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
"""
    (DIST_DIR / "netlify.toml").write_text(netlify_toml_content, encoding="utf-8")
    print("✓ Created Netlify security headers and isolated netlify.toml.")

def verify_build():
    """Verifies that all assets referenced in dist/coming-soon/index.html exist."""
    html_file = DIST_DIR / "index.html"
    content = html_file.read_text(encoding="utf-8")

    # Match src="..." and href="..."
    refs = re.findall(r'(?:src|href)=["\']([^"\'#?]+)["\']', content)
    missing = []
    checked = 0

    for ref in refs:
        # Ignore external links, mailto, tel, absolute domain URLs, or root /
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "//")) or ref == "/":
            continue
        asset_path = DIST_DIR / ref
        checked += 1
        if not asset_path.exists():
            missing.append(ref)

    if missing:
        print(f"❌ ERROR: Missing referenced assets in build output:", file=sys.stderr)
        for m in missing:
            print(f"   - {m}", file=sys.stderr)
        sys.exit(1)

    # Compute total size
    total_size = sum(f.stat().st_size for f in DIST_DIR.rglob("*") if f.is_file())
    file_count = len(list(f for f in DIST_DIR.rglob("*") if f.is_file()))

    print("========================================================================")
    print("EcoCare Standalone Coming Soon Build Verified!")
    print(f"Destination:  {DIST_DIR}")
    print(f"Total Files:  {file_count} files ({total_size / 1024:.1f} KB)")
    print(f"Asset Checks: {checked} relative references verified (0 missing)")
    print("========================================================================")

def main():
    print("Building EcoCare 7-Day Coming Soon Isolated Site...")
    clean_dist()
    copy_individual_assets()
    copy_directory_trees()
    write_netlify_headers()
    verify_build()

if __name__ == "__main__":
    main()
