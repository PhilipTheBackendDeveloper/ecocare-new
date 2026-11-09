#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Coming Soon Deployment Builder
Generates isolated, production-ready standalone Coming Soon sites in:
  1. dist/coming-soon/ (Primary Netlify build artifact target)
  2. deploy/coming-soon/ (Local preview & deployment synchronization target)
Guarantees 100% byte-for-byte identity between coming-soon.html, dist/coming-soon/, and deploy/coming-soon/.
"""

import os
import sys
import shutil
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PUBLISH_DIRS = [
    ROOT_DIR / "dist" / "coming-soon",
    ROOT_DIR / "deploy" / "coming-soon",
]

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
    ("img/logo-preloader.png", "img/logo-preloader.png"),
    ("img/figure/coming-soon.jpg", "img/figure/coming-soon.jpg"),
    # Core JS
    ("js/jquery-3.3.1.min.js", "js/jquery-3.3.1.min.js"),
    ("js/popper.min.js", "js/popper.min.js"),
    ("js/bootstrap.min.js", "js/bootstrap.min.js"),
    ("js/coming-soon-countdown.js", "js/coming-soon-countdown.js"),
]

def clean_targets():
    """Removes previous build output in target directories."""
    for target in PUBLISH_DIRS:
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True, exist_ok=True)
        print(f"✓ Cleaned and prepared {target}")

def copy_individual_assets():
    """Validates and copies individual files to all target directories."""
    for target in PUBLISH_DIRS:
        for src_rel, dst_rel in REQUIRED_ASSETS:
            src = ROOT_DIR / src_rel
            dst = target / dst_rel
            if not src.exists():
                print(f"❌ ERROR: Missing required source file: {src}", file=sys.stderr)
                sys.exit(1)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        print(f"✓ Copied {len(REQUIRED_ASSETS)} core static assets to {target.name}/.")

def copy_directory_trees():
    """Copies font trees (FontAwesome webfonts and Flaticon) to all targets."""
    for target in PUBLISH_DIRS:
        # 1. webfonts/
        src_webfonts = ROOT_DIR / "webfonts"
        dst_webfonts = target / "webfonts"
        if src_webfonts.exists():
            dst_webfonts.mkdir(parents=True, exist_ok=True)
            for item in src_webfonts.glob("*"):
                if item.is_file():
                    shutil.copy2(item, dst_webfonts / item.name)
            print(f"✓ Copied FontAwesome webfonts to {target.name}/.")
        else:
            print("⚠️ Warning: webfonts directory not found in root.", file=sys.stderr)

        # 2. font/
        src_font = ROOT_DIR / "font"
        dst_font = target / "font"
        if src_font.exists():
            dst_font.mkdir(parents=True, exist_ok=True)
            for item in src_font.glob("*"):
                if item.is_file():
                    shutil.copy2(item, dst_font / item.name)
            print(f"✓ Copied Flaticon font assets to {target.name}/.")

def write_isolated_seo_and_routing():
    """Generates isolated State A robots.txt, sitemap.xml, _redirects, and security _headers."""
    robots_content = """User-agent: *
Allow: /

# State A: 7-Day Coming Soon Launchpad
# Full sitemap submission is scheduled for State B (Full Site Launch) to prevent Search Console 'Submitted URL marked noindex' warnings.
"""
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ecocaregh.com/</loc>
    <lastmod>2026-11-09</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    redirects_content = """# State A Static Asset Passthrough
/css/*          /css/:splat          200
/js/*           /js/:splat           200
/img/*          /img/:splat          200
/font/*         /font/:splat         200
/webfonts/*     /webfonts/:splat     200
/robots.txt     /robots.txt          200
/sitemap.xml    /sitemap.xml         200

# Canonical root mapping: legacy index.html permanently redirects to root
/index.html     /                    301

# Sub-route catch-all: non-existent paths redirect to root without looping (unforced, allows index.html to serve /)
/*              /                    302
"""
    headers_content = """/*
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
"""
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

    for target in PUBLISH_DIRS:
        (target / "robots.txt").write_text(robots_content, encoding="utf-8")
        (target / "sitemap.xml").write_text(sitemap_content, encoding="utf-8")
        (target / "_redirects").write_text(redirects_content, encoding="utf-8")
        (target / "_headers").write_text(headers_content, encoding="utf-8")
        (target / "netlify.toml").write_text(netlify_toml_content, encoding="utf-8")
        print(f"✓ Created isolated SEO, headers, redirects, and netlify.toml in {target.name}/.")

def verify_builds():
    """Verifies that all assets referenced in index.html exist and no sensitive files leaked."""
    for target in PUBLISH_DIRS:
        html_file = target / "index.html"
        content = html_file.read_text(encoding="utf-8")

        # Match src="..." and href="..."
        refs = re.findall(r'(?:src|href)=["\']([^"\'#?]+)["\']', content)
        missing = []
        checked = 0

        for ref in refs:
            if ref.startswith(("http://", "https://", "mailto:", "tel:", "//")) or ref == "/":
                continue
            asset_path = target / ref
            checked += 1
            if not asset_path.exists():
                missing.append(ref)

        if missing:
            print(f"❌ ERROR: Missing referenced assets in {target}:", file=sys.stderr)
            for m in missing:
                print(f"   - {m}", file=sys.stderr)
            sys.exit(1)

        # Security check: Ensure zero .env, zero .py, zero unfinished html files exist
        forbidden_extensions = [".py", ".env", ".sh", ".jsonl"]
        for f in target.rglob("*"):
            if f.is_file():
                if f.suffix in forbidden_extensions or "about1" in f.name or "service1" in f.name:
                    print(f"❌ SECURITY ERROR: Unintended file in {target}: {f}", file=sys.stderr)
                    sys.exit(1)

        total_size = sum(f.stat().st_size for f in target.rglob("*") if f.is_file())
        file_count = len(list(f for f in target.rglob("*") if f.is_file()))

        print("========================================================================")
        print(f"EcoCare Standalone Coming Soon Target Verified: {target.name}/")
        print(f"Destination:  {target}")
        print(f"Total Files:  {file_count} files ({total_size / 1024:.1f} KB)")
        print(f"Asset Checks: {checked} relative references verified (0 missing)")
        print("========================================================================")

def main():
    print("Building EcoCare 7-Day Coming Soon Isolated Targets...")
    clean_targets()
    copy_individual_assets()
    copy_directory_trees()
    write_isolated_seo_and_routing()
    verify_builds()

if __name__ == "__main__":
    main()
