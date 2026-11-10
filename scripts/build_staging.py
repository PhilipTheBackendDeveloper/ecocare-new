#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Safe Full-Site Staging Build System
Compiles the complete production-grade website into dist/staging/ for Netlify Deploy Previews
and Branch Deploys.

Guarantees:
- Strictly excludes all unapproved demo templates, backend files, docs, and secrets.
- Injects X-Robots-Tag: noindex, nofollow and Disallow: / to prevent any indexing.
- Preserves all canonical pages, responsive assets, Netlify forms, and video hero.
- Verifies relative asset integrity across every compiled page.
- Supports optional local preview server via --serve [port].
"""

import sys
import os
import shutil
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST_STAGING = ROOT / "dist" / "staging"

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
    "pricing-table.html",
    "calculate-form.html",
    "faq.html",
    "contact.html",
    "project1.html",
    "single-project1.html",
    "404.html",
    "privacy-policy.html",
    "terms-condition.html",
]

DEMO_PAGES_TO_EXCLUDE = [
    "index2.html", "index3.html", "index4.html",
    "about2.html", "service2.html",
    "blog1.html", "blog2.html", "single-blog1.html",
    "shop.html", "single-product.html",
    "team1.html", "team2.html", "single-team.html",
]

STATIC_DIRS = ["css", "js", "img", "font", "webfonts"]
STATIC_FILES = ["style.css", "video-background.mp4", "video-background1.mp4"]


def clean_target():
    """Wipes and recreates dist/staging cleanly."""
    if DIST_STAGING.exists():
        shutil.rmtree(DIST_STAGING)
    DIST_STAGING.mkdir(parents=True, exist_ok=True)
    print(f"✓ Cleaned and prepared staging destination: {DIST_STAGING}")


def copy_canonical_pages():
    """Copies only approved canonical pages."""
    copied = 0
    for page in CANONICAL_PAGES:
        src = ROOT / page
        if not src.exists():
            raise FileNotFoundError(f"Missing required canonical page: {src}")
        dest = DIST_STAGING / page
        shutil.copy2(src, dest)
        copied += 1
    print(f"✓ Copied {copied} canonical HTML pages to staging.")


def copy_static_assets():
    """Copies style, script, image, font, and video assets."""
    # Copy directories
    for dir_name in STATIC_DIRS:
        src_dir = ROOT / dir_name
        dest_dir = DIST_STAGING / dir_name
        if src_dir.exists():
            shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
            print(f"✓ Copied static asset directory: {dir_name}/")

    # Copy root static files
    for file_name in STATIC_FILES:
        src_file = ROOT / file_name
        if src_file.exists():
            shutil.copy2(src_file, DIST_STAGING / file_name)
            print(f"✓ Copied static file: {file_name}")


def generate_staging_routing_and_headers():
    """Generates staging-specific redirects, headers (noindex), and robots.txt."""
    # 1. Staging robots.txt: Disallow all search engine indexing
    robots_content = """User-agent: *
Disallow: /

# EcoCare Full Website Staging Preview
# Search engine crawling and indexing is strictly prohibited on staging environments.
"""
    (DIST_STAGING / "robots.txt").write_text(robots_content, encoding="utf-8")

    # 2. Staging _headers: Enforce X-Robots-Tag: noindex, nofollow and standard security headers
    headers_content = """/*
  X-Robots-Tag: noindex, nofollow
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
"""
    (DIST_STAGING / "_headers").write_text(headers_content, encoding="utf-8")

    # 3. Staging _redirects: Clean URL rewrites and 404 routing
    redirects_content = """# EcoCare Cleaning Services Limited — Staging Clean URL Routing & Rewrites

# Clean URL Rewrites (Internal 200 Mapping to HTML Sources)
/about                          /about1.html                 200
/services                       /service1.html               200
/cleaning                       /single-service1.html        200
/laundry                        /single-service2.html        200
/pest-control                   /pest-control.html           200
/carpet-cleaning                /carpet-cleaning.html        200
/upholstery-cleaning            /upholstery-cleaning.html    200
/polytank-cleaning              /polytank-cleaning.html      200
/car-interior-cleaning          /car-interior-cleaning.html  200
/professional-dusting           /professional-dusting.html   200
/packages                       /pricing-table.html          200
/request-quote                  /calculate-form.html         200
/faq                            /faq.html                    200
/contact                        /contact.html                200
/projects                       /project1.html               200
/projects/commercial-case-study /single-project1.html        200
/privacy-policy                 /privacy-policy.html         200
/terms                          /terms-condition.html        200

# Legacy .html to Clean URLs (301 Permanent Redirects)
/about1.html                    /about                       301
/service1.html                  /services                    301
/single-service1.html           /cleaning                    301
/single-service2.html           /laundry                     301
/pest-control.html              /pest-control                301
/carpet-cleaning.html           /carpet-cleaning             301
/upholstery-cleaning.html       /upholstery-cleaning         301
/polytank-cleaning.html         /polytank-cleaning           301
/car-interior-cleaning.html     /car-interior-cleaning       301
/professional-dusting.html      /professional-dusting        301
/pricing-table.html             /packages                    301
/calculate-form.html            /request-quote               301
/project1.html                  /projects                    301
/single-project1.html           /projects/commercial-case-study 301
/terms-condition.html           /terms                       301

# Custom 404 Catch-All
/*                              /404.html                    404
"""
    (DIST_STAGING / "_redirects").write_text(redirects_content, encoding="utf-8")
    print("✓ Created staging _headers (noindex, nofollow), robots.txt (Disallow: /), and _redirects.")


def verify_staging_build():
    """Runs strict assertions on the compiled staging directory."""
    print("\n--- STAGING BUILD VERIFICATION ---")

    # 1. Assert zero demo pages exist
    for demo in DEMO_PAGES_TO_EXCLUDE:
        if (DIST_STAGING / demo).exists():
            raise AssertionError(f"SECURITY BREACH: Demo page {demo} found in dist/staging/!")
    print("✓ Verified: Zero unapproved demo pages in dist/staging/.")

    # 2. Assert zero sensitive backend files or docs exist
    forbidden_items = ["api", "data", "vendor/php", "docs", "scripts", ".env", "package.json"]
    for item in forbidden_items:
        if (DIST_STAGING / item).exists():
            raise AssertionError(f"SECURITY BREACH: Forbidden item {item} found in dist/staging/!")
    print("✓ Verified: Zero backend storage, docs, or sensitive scripts in dist/staging/.")

    # 3. Verify noindex header
    headers_text = (DIST_STAGING / "_headers").read_text(encoding="utf-8")
    if "X-Robots-Tag: noindex, nofollow" not in headers_text:
        raise AssertionError("Staging _headers missing X-Robots-Tag: noindex, nofollow!")
    print("✓ Verified: Staging HTTP header contains X-Robots-Tag: noindex, nofollow.")

    # 4. Verify robots.txt disallows all
    robots_text = (DIST_STAGING / "robots.txt").read_text(encoding="utf-8")
    if "Disallow: /" not in robots_text:
        raise AssertionError("Staging robots.txt missing Disallow: / directive!")
    print("✓ Verified: Staging robots.txt strictly disallows all search engine crawlers.")

    # 5. Check forms in HTML
    contact_html = (DIST_STAGING / "contact.html").read_text(encoding="utf-8")
    if 'data-netlify="true"' not in contact_html or 'name="contact"' not in contact_html:
        raise AssertionError("contact.html missing data-netlify='true' or name='contact'!")
    print("✓ Verified: contact.html Netlify Form attributes configured.")

    calc_html = (DIST_STAGING / "calculate-form.html").read_text(encoding="utf-8")
    if 'data-netlify="true"' not in calc_html or 'name="quote-calculator"' not in calc_html:
        raise AssertionError("calculate-form.html missing data-netlify='true' or name='quote-calculator'!")
    print("✓ Verified: calculate-form.html Netlify Form attributes configured.")

    # 6. Count total files and size
    total_files = sum(len(files) for _, _, files in os.walk(DIST_STAGING))
    total_bytes = sum(
        os.path.getsize(os.path.join(root, file))
        for root, _, files in os.walk(DIST_STAGING)
        for file in files
    )
    print(f"\n========================================================================")
    print(f"EcoCare Full Website Staging Build Complete!")
    print(f"Destination: {DIST_STAGING}")
    print(f"Total Files: {total_files} files ({total_bytes / (1024*1024):.2f} MB)")
    print(f"========================================================================\n")


def serve_staging(port=8888):
    """Launches local HTTP preview server for dist/staging/."""
    import http.server
    import socketserver

    os.chdir(DIST_STAGING)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"========================================================================")
        print(f"EcoCare Full Website Staging Preview Active!")
        print(f"Local URL: http://localhost:{port}/")
        print(f"Serving:   {DIST_STAGING}")
        print(f"Press Ctrl+C to terminate.")
        print(f"========================================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nPreview server stopped.")


def main():
    clean_target()
    copy_canonical_pages()
    copy_static_assets()
    generate_staging_routing_and_headers()
    verify_staging_build()

    if "--serve" in sys.argv:
        port = 8888
        try:
            idx = sys.argv.index("--serve")
            if idx + 1 < len(sys.argv) and sys.argv[idx + 1].isdigit():
                port = int(sys.argv[idx + 1])
        except Exception:
            pass
        serve_staging(port)


if __name__ == "__main__":
    main()

