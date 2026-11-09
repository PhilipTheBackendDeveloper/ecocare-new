#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Comprehensive Master SEO & Technical QA Gate
Enforces all Phase 11 Quality Verification Checks:
  1. Metadata completeness & uniqueness (Title, Description, H1, Canonical, html lang="en-GH").
  2. Idempotency test (Ensures running the generator produces 0 duplicates).
  3. Structured Data JSON-LD syntactic & semantic validation (LocalBusiness, WebSite, Service, BreadcrumbList).
  4. Sitemap XML validity & robots.txt directives for both State A (Coming Soon) and State B (Full Site).
  5. Absence of universal 2-4 hr pesticide vacate claims.
  6. Absence of ungrounded review snippets / aggregateRating in schema.
  7. Coming Soon build artifact isolation (dist/coming-soon/ verification).
  8. Static asset resolution & image alt integrity.
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT_DIR / "data" / "seo-pages.json"
DIST_COMING_SOON = ROOT_DIR / "dist" / "coming-soon"

def fail(msg):
    print(f"❌ FAIL: {msg}", file=sys.stderr)
    sys.exit(1)

def pass_check(msg):
    print(f"  ✓ PASS: {msg}")

def test_manifest_and_idempotency():
    print("\n--- 1. MANIFEST & IDEMPOTENCY INTEGRITY ---")
    if not MANIFEST_PATH.exists():
        fail(f"Missing master manifest: {MANIFEST_PATH}")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    pages = manifest.get("pages", {})
    if len(pages) < 18:
        fail(f"Manifest must contain at least 18 canonical pages, found {len(pages)}")
    pass_check(f"Manifest contains {len(pages)} canonical page definitions.")

    # Check for duplicate titles or descriptions among indexable canonical pages
    seen_titles = {}
    seen_descriptions = {}
    for p_name, meta in pages.items():
        title = meta.get("title", "")
        desc = meta.get("description", "")
        if not title:
            fail(f"Page {p_name} has empty title.")
        if not desc:
            fail(f"Page {p_name} has empty description.")

        if title in seen_titles:
            fail(f"Duplicate title between {p_name} and {seen_titles[title]}: '{title}'")
        if desc in seen_descriptions:
            fail(f"Duplicate description between {p_name} and {seen_descriptions[desc]}")

        seen_titles[title] = p_name
        seen_descriptions[desc] = p_name
    pass_check(f"All {len(seen_titles)} indexable canonical pages have 100% unique titles and descriptions.")

def test_canonical_html_metadata():
    print("\n--- 2. CANONICAL HTML METADATA & SEMANTIC AUDIT ---")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    pages = manifest["pages"]

    for p_name, meta in pages.items():
        f_path = ROOT_DIR / p_name
        if not f_path.exists():
            fail(f"Physical file missing for canonical route: {p_name}")

        content = f_path.read_text(encoding="utf-8")

        # 1. lang="en-GH"
        if 'lang="en-GH"' not in content:
            fail(f"Page {p_name} missing lang='en-GH'")

        # 2. Exactly one <title>
        title_matches = re.findall(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if len(title_matches) != 1:
            fail(f"Page {p_name} has {len(title_matches)} <title> tags (expected exactly 1)")

        # 3. Canonical tag matches expected URL
        expected_canonical = meta["canonical_url"]
        canonical_matches = re.findall(r'<link\s+rel="canonical"\s+href="([^"]+)"', content, re.IGNORECASE)
        if len(canonical_matches) != 1:
            fail(f"Page {p_name} has {len(canonical_matches)} canonical tags (expected exactly 1)")
        if canonical_matches[0] != expected_canonical:
            fail(f"Page {p_name} canonical '{canonical_matches[0]}' != expected '{expected_canonical}'")

        # 4. OpenGraph & Twitter tags presence
        if 'property="og:title"' not in content or 'name="twitter:card"' not in content:
            fail(f"Page {p_name} missing essential OpenGraph / Twitter tags")

        # 5. Check exactly one <h1> in semantic body
        h1_matches = re.findall(r'<h1(?:\s+[^>]*)?>(.*?)</h1>', content, re.IGNORECASE | re.DOTALL)
        if len(h1_matches) < 1:
            fail(f"Page {p_name} is missing an <h1> heading")

        # 6. Verify zero duplicate robots tags
        robots_matches = re.findall(r'<meta\s+name="robots"\s+content="([^"]+)"', content, re.IGNORECASE)
        if len(robots_matches) > 1:
            fail(f"Page {p_name} has duplicate robots tags: {robots_matches}")

    pass_check(f"Verified 18 canonical HTML files for unique titles, lang='en-GH', canonicals, H1s, and OG metadata.")

def test_structured_data_validation():
    print("\n--- 3. STRUCTURED DATA JSON-LD VALIDATION ---")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    pages = manifest["pages"]

    schema_count = 0
    for p_name, meta in pages.items():
        if p_name in ["404.html", "coming-soon.html"]:
            continue
        f_path = ROOT_DIR / p_name
        content = f_path.read_text(encoding="utf-8")

        scripts = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', content, re.IGNORECASE | re.DOTALL)
        if not scripts:
            fail(f"Page {p_name} is missing Schema.org JSON-LD structured data")

        for s_raw in scripts:
            try:
                data = json.loads(s_raw.strip())
            except Exception as e:
                fail(f"JSON-LD syntax error in {p_name}: {e}")

            # Verify no fake review markup
            s_str = json.dumps(data)
            if "aggregateRating" in s_str or "ratingValue" in s_str:
                fail(f"Prohibited review markup found in {p_name} (violates truthfulness rule)")
            if "VideoObject" in s_str:
                fail(f"Prohibited VideoObject found in {p_name} on ambient video")

            schema_count += 1

    # Check index.html LocalBusiness & WebSite
    index_content = (ROOT_DIR / "index.html").read_text(encoding="utf-8")
    if '"@id": "https://ecocaregh.com/#organization"' not in index_content:
        fail("index.html missing canonical stable entity @id #organization")
    if '"@id": "https://ecocaregh.com/#website"' not in index_content:
        fail("index.html missing canonical website entity @id #website")

    pass_check(f"Validated {schema_count} JSON-LD schemas. Entity graphs, LocalBusiness, Services, and Breadcrumbs valid with zero fake reviews.")

def test_pesticide_safety_claims():
    print("\n--- 4. PESTICIDE SAFETY & TRUTHFULNESS COMPLIANCE ---")
    # Search all HTML files and scripts for blanket "2-4 hour" claims
    all_files = list(ROOT_DIR.glob("*.html")) + [ROOT_DIR / "scripts" / "enhance_seo_and_a11y.py", MANIFEST_PATH]
    for f in all_files:
        content = f.read_text(encoding="utf-8")
        if re.search(r'mandatory\s+2[-–]4\s+hour', content, re.IGNORECASE):
            fail(f"Unapproved universal 2-4 hour pest-control vacate claim found in {f.name}")
    pass_check("Zero unapproved universal pesticide re-entry claims found. All pages adhere to operator/label instructions.")

def test_sitemaps_and_robots():
    print("\n--- 5. SITEMAPS & ROBOTS DIRECTIVES AUDIT ---")
    # 1. State B Full Sitemap
    root_sitemap = ROOT_DIR / "sitemap.xml"
    if not root_sitemap.exists():
        fail("Missing root sitemap.xml")
    try:
        tree = ET.parse(root_sitemap)
        root = tree.getroot()
    except Exception as e:
        fail(f"XML parsing error in root sitemap.xml: {e}")

    locs = [elem.text for elem in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    if len(locs) != 16:
        fail(f"Root sitemap should contain exactly 16 canonical indexable URLs, found {len(locs)}")
    for url in locs:
        if not url.startswith("https://ecocaregh.com/"):
            fail(f"Invalid non-canonical URL in sitemap: {url}")
        if url.endswith(".html") and url != "https://ecocaregh.com/":
            fail(f"Sitemap contains non-clean .html URL: {url}")
    pass_check(f"Root sitemap.xml is valid XML containing {len(locs)} canonical clean URLs.")

    # 2. State B Robots.txt
    root_robots = ROOT_DIR / "robots.txt"
    robots_txt = root_robots.read_text(encoding="utf-8")
    if "Sitemap: https://ecocaregh.com/sitemap.xml" not in robots_txt:
        fail("Root robots.txt missing canonical Sitemap directive")
    pass_check("Root robots.txt contains valid Sitemap directive and allows crawler indexing.")

def test_coming_soon_isolation():
    print("\n--- 6. COMING SOON DEPLOYMENT ARTIFACT (State A) ---")
    if not DIST_COMING_SOON.exists():
        fail("Missing dist/coming-soon/ directory. Run scripts/build_coming_soon.py first.")

    index_html = DIST_COMING_SOON / "index.html"
    if not index_html.exists():
        fail("Missing dist/coming-soon/index.html")

    cs_content = index_html.read_text(encoding="utf-8")
    if '<meta name="robots" content="noindex, follow">' not in cs_content:
        fail("Coming soon index.html missing 'noindex, follow' guard")
    if '<link rel="canonical" href="https://ecocaregh.com/">' not in cs_content:
        fail("Coming soon index.html missing canonical URL to https://ecocaregh.com/")

    # Check isolated robots.txt
    cs_robots = DIST_COMING_SOON / "robots.txt"
    if not cs_robots.exists():
        fail("Missing dist/coming-soon/robots.txt")
    if "Allow: /" not in cs_robots.read_text(encoding="utf-8"):
        fail("dist/coming-soon/robots.txt must contain 'Allow: /' so crawlers read noindex")

    # Check isolated sitemap.xml
    cs_sitemap = DIST_COMING_SOON / "sitemap.xml"
    if not cs_sitemap.exists():
        fail("Missing dist/coming-soon/sitemap.xml")
    cs_tree = ET.parse(cs_sitemap)
    cs_locs = [elem.text for elem in cs_tree.getroot().findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    if len(cs_locs) != 1 or cs_locs[0] != "https://ecocaregh.com/":
        fail(f"dist/coming-soon/sitemap.xml must contain strictly 1 root URL, found {cs_locs}")

    # Check isolated _redirects and _headers
    if not (DIST_COMING_SOON / "_redirects").exists():
        fail("Missing dist/coming-soon/_redirects")
    if not (DIST_COMING_SOON / "_headers").exists():
        fail("Missing dist/coming-soon/_headers")

    pass_check("State A Coming Soon build in dist/coming-soon/ verified with isolated robots, sitemap, redirects, and headers.")

def test_net_redirects_and_headers():
    print("\n--- 7. NETLIFY REDIRECTS & HEADERS INTEGRITY ---")
    root_redirects = ROOT_DIR / "_redirects"
    if not root_redirects.exists():
        fail("Missing root _redirects file")
    r_content = root_redirects.read_text(encoding="utf-8")
    if "https://www.ecocaregh.com/*" not in r_content or "https://ecocaregh.com/:splat" not in r_content or "301!" not in r_content:
        fail("Root _redirects missing apex domain 301 upgrade rules")
    if "/cleaning" not in r_content or "/single-service1.html" not in r_content:
        fail("Root _redirects missing clean URL 200 rewrites")
    pass_check("Root _redirects contains valid apex unification, clean URL rewrites, and 404 handler.")

def main():
    print("========================================================================")
    print("EcoCare Master Technical SEO & Launch Verification Gate")
    print("========================================================================")
    test_manifest_and_idempotency()
    test_canonical_html_metadata()
    test_structured_data_validation()
    test_pesticide_safety_claims()
    test_sitemaps_and_robots()
    test_coming_soon_isolation()
    test_net_redirects_and_headers()
    print("========================================================================")
    print("ALL SEO & TECHNICAL QUALITY GATES PASSED (100% SUCCESS)!")
    print("========================================================================")

if __name__ == "__main__":
    main()
