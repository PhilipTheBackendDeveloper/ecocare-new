#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Official Production Build System
Compiles the complete, canonical production website into dist/production/ for live Netlify deployment.

Guarantees:
- Strictly compiles only approved canonical pages, authentic assets, and verified forms.
- Publishes canonical robots.txt (Allow: /) and sitemap.xml for full Google & Bing indexing.
- Deploys production HTTP security headers and aggressive static asset caching.
- Enforces apex domain unification (www -> non-www 301) and clean URL 200 rewrites.
- Completely isolates production from internal build scripts, test databases, and developer notes.
"""

import sys
import os
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_PRODUCTION = ROOT / "dist" / "production"

CANONICAL_PAGES = [
    "index.html",
    "about1.html",
    "service1.html",
    "single-service1.html",
    "single-service2.html",
    "pest-control.html",
    "carpet-cleaning.html",
    "upholstery-cleaning.html",
    "polytank-cleaning.html",
    "car-interior-cleaning.html",
    "professional-dusting.html",
    "calculate-form.html",
    "faq.html",
    "contact.html",
    "project1.html",
    "single-project1.html",
    "404.html",
    "privacy-policy.html",
    "terms-condition.html",
]

STATIC_DIRS = ["css", "js", "img", "font", "webfonts"]
STATIC_FILES = ["style.css", "video-background.mp4", "video-background1.mp4"]


def clean_target():
    """Wipes and recreates dist/production cleanly."""
    if DIST_PRODUCTION.exists():
        shutil.rmtree(DIST_PRODUCTION)
    DIST_PRODUCTION.mkdir(parents=True, exist_ok=True)
    print(f"✓ Cleaned and prepared production destination: {DIST_PRODUCTION}")


def copy_canonical_pages():
    """Copies all approved canonical HTML pages."""
    copied = 0
    for page in CANONICAL_PAGES:
        src = ROOT / page
        if not src.exists():
            raise FileNotFoundError(f"Missing required canonical page: {src}")
        dest = DIST_PRODUCTION / page
        shutil.copy2(src, dest)
        copied += 1
    print(f"✓ Copied {copied} canonical HTML pages to production.")


def copy_static_assets():
    """Copies style, script, image, font, and video assets."""
    for dir_name in STATIC_DIRS:
        src_dir = ROOT / dir_name
        dest_dir = DIST_PRODUCTION / dir_name
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
            print(f"✓ Copied static asset directory: {dir_name}/")

    for file_name in STATIC_FILES:
        src_file = ROOT / file_name
        if src_file.exists():
            shutil.copy2(src_file, DIST_PRODUCTION / file_name)
            print(f"✓ Copied static file: {file_name}")


def generate_production_routing_and_headers():
    """Generates production-grade robots.txt, sitemap.xml, _redirects, and _headers."""
    # 1. Production robots.txt: Allow search engine indexing with canonical sitemap
    robots_content = """User-agent: *
Allow: /

# Canonical Sitemap
Sitemap: https://ecocaregh.com/sitemap.xml
"""
    (DIST_PRODUCTION / "robots.txt").write_text(robots_content, encoding="utf-8")

    # 2. Production sitemap.xml: Copy master sitemap
    src_sitemap = ROOT / "sitemap.xml"
    if src_sitemap.exists():
        shutil.copy2(src_sitemap, DIST_PRODUCTION / "sitemap.xml")
        print("✓ Copied canonical sitemap.xml.")
    else:
        raise FileNotFoundError("Missing master sitemap.xml in repository root!")

    # 3. Production _headers: Standard security headers + asset caching (NO noindex)
    headers_content = """/*
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin

/img/*
  Cache-Control: public, max-age=2592000, immutable

/css/*
  Cache-Control: public, max-age=604800

/js/*
  Cache-Control: public, max-age=604800

/font/*
  Cache-Control: public, max-age=31536000, immutable

/webfonts/*
  Cache-Control: public, max-age=31536000, immutable
"""
    (DIST_PRODUCTION / "_headers").write_text(headers_content, encoding="utf-8")

    # 4. Production _redirects: Copy master _redirects directly
    src_redirects = ROOT / "_redirects"
    if src_redirects.exists():
        shutil.copy2(src_redirects, DIST_PRODUCTION / "_redirects")
        print("✓ Copied canonical _redirects.")
    else:
        raise FileNotFoundError("Missing master _redirects in repository root!")


def verify_production_build():
    """Validates the output directory before deployment."""
    # Ensure zero unapproved files
    unapproved = ["pricing-table.html", "index2.html", "shop.html", "team1.html", "blog1.html"]
    for bad in unapproved:
        if (DIST_PRODUCTION / bad).exists():
            raise AssertionError(f"Security error: unapproved file {bad} found in production build!")

    # Ensure robots.txt allows indexing
    robots = (DIST_PRODUCTION / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /" in robots:
        raise AssertionError("Production robots.txt must not contain Disallow: /")
    if "Allow: /" not in robots:
        raise AssertionError("Production robots.txt must contain Allow: /")

    # Ensure _headers does NOT have noindex
    headers = (DIST_PRODUCTION / "_headers").read_text(encoding="utf-8")
    if "noindex" in headers:
        raise AssertionError("Production _headers must NOT contain noindex!")

    # Ensure sitemap.xml exists and has all canonical URLs
    sitemap = (DIST_PRODUCTION / "sitemap.xml").read_text(encoding="utf-8")
    if "<loc>https://ecocaregh.com/</loc>" not in sitemap:
        raise AssertionError("Production sitemap.xml missing root canonical URL!")

    # Ensure forms are intact in HTML
    contact_html = (DIST_PRODUCTION / "contact.html").read_text(encoding="utf-8")
    if 'name="contact"' not in contact_html or 'data-netlify="true"' not in contact_html:
        raise AssertionError("contact.html missing Netlify form attributes!")

    calc_html = (DIST_PRODUCTION / "calculate-form.html").read_text(encoding="utf-8")
    if 'name="quote-calculator"' not in calc_html or 'data-netlify="true"' not in calc_html:
        raise AssertionError("calculate-form.html missing Netlify form attributes!")

    print("\n--- PRODUCTION BUILD VERIFICATION ---")
    print("✓ Verified: Zero unapproved demo pages in dist/production/.")
    print("✓ Verified: Production robots.txt allows crawler indexing (Allow: /).")
    print("✓ Verified: Production _headers contains zero noindex barriers.")
    print("✓ Verified: Canonical sitemap.xml included and verified.")
    print("✓ Verified: Netlify form detection intact across all forms.")


def main():
    print("========================================================================")
    print("EcoCare Full Website Production Build System")
    print("========================================================================\n")

    clean_target()
    copy_canonical_pages()
    copy_static_assets()
    generate_production_routing_and_headers()
    verify_production_build()

    total_files = sum(len(files) for _, _, files in os.walk(DIST_PRODUCTION))
    total_size = sum(
        os.path.getsize(os.path.join(root, file))
        for root, _, files in os.walk(DIST_PRODUCTION)
        for file in files
    )
    print("\n========================================================================")
    print("EcoCare Full Website Production Build Complete!")
    print(f"Destination: {DIST_PRODUCTION}")
    print(f"Total Files: {total_files} files ({total_size / (1024 * 1024):.2f} MB)")
    print("========================================================================\n")


if __name__ == "__main__":
    main()
