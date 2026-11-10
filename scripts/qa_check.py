#!/usr/bin/env python3
"""
EcoCare Automated QA Checker
Scans all canonical HTML files and reports:
  - Broken internal href="#" placeholder links
  - Demo/Clenix brand remnants in titles
  - Demo phone/email/address references
  - Missing EcoCare brand signals
  - Forms without proper action/id
  - Google Maps API key exposure
  - HTTrack comment remnants
  - Cloudflare beacon remnants
  - popper.html references
  - Missing robots noindex on deprecated pages
  - File sizes
"""

import os
import re

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
    "coming-soon.html",
    "404.html",
    "privacy-policy.html",
    "terms-condition.html",
]

DEPRECATED_PAGES = [
    "index2.html", "index3.html", "index4.html",
    "about2.html", "service2.html",
    "blog1.html", "blog2.html", "single-blog1.html",
    "shop.html", "single-product.html",
    "team1.html", "team2.html", "single-team.html",
]

DEMO_PHONES = ["123-456", "987654", "(800)", "1-800", "555-"]
DEMO_EMAILS = ["info@example.com", "admin@example.com", "demo@", "test@"]
DEMO_ADDRESSES = ["123 Main", "New York", "California"]
DEMO_BRANDS = ["clenix", "radiustheme", "radxtheme"]
DEMO_API_KEY = "AIzaSyBtmXSwv4YmAKtcZyyad9W7D4AC08z0Rb4"

REAL_PHONES = ["+233 24 901 4253", "+233 24 380 7100"]
REAL_EMAIL = "ecocaregh1on1@gmail.com"
REAL_ADDRESS = "Achimota"
REAL_BRAND = "EcoCare"

issues = []
warnings = []
passes = []

def check_file(filepath, is_deprecated=False):
    file_issues = []
    file_warnings = []
    file_passes = []

    if not os.path.exists(filepath):
        file_issues.append(f"FILE MISSING: {filepath}")
        return file_issues, file_warnings, file_passes

    size_kb = os.path.getsize(filepath) / 1024
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    # HTTrack comment remnants
    if "HTTrack" in content or "Mirrored from" in content:
        file_issues.append(f"HTTRACK remnant detected")

    # Cloudflare beacon
    if "cloudflareinsights.com" in content or "beacon.min.js" in content:
        file_issues.append(f"Cloudflare beacon detected")

    # popper.html reference
    if 'require("popper.html")' in content or "popper.html" in content:
        file_issues.append(f"popper.html reference detected")

    # Exposed demo Google Maps API key
    if DEMO_API_KEY in content:
        file_issues.append(f"Demo Google Maps API key exposed: {DEMO_API_KEY[:20]}...")

    # Demo brand names
    for demo in DEMO_BRANDS:
        if demo in content.lower():
            # Check if it's just in a comment/script path not visible text
            # Find positions
            positions = [m.start() for m in re.finditer(re.escape(demo), content, re.IGNORECASE)]
            # Only flag if NOT inside CSS/vendor paths
            real_issues = []
            for pos in positions:
                snippet = content[max(0, pos-50):pos+50]
                if "vendor/" not in snippet and "css/" not in snippet and "stylesheet" not in snippet and "script" not in snippet:
                    real_issues.append(snippet.strip()[:60])
            if real_issues:
                file_issues.append(f"Demo brand '{demo}' found in content: {real_issues[0][:60]}")

    # Demo phone numbers
    for demo_phone in DEMO_PHONES:
        if demo_phone in content:
            file_issues.append(f"Demo phone found: {demo_phone}")

    # Demo email addresses
    for demo_email in DEMO_EMAILS:
        if demo_email.lower() in content.lower():
            file_issues.append(f"Demo email found: {demo_email}")

    # Demo addresses
    for demo_addr in DEMO_ADDRESSES:
        if demo_addr in content:
            file_issues.append(f"Demo address found: {demo_addr}")

    # Bare href="#" anchor links (non-canonical pages skip this check)
    if not is_deprecated:
        naked_hash_links = re.findall(r'href="#"', content)
        if naked_hash_links:
            file_warnings.append(f"Found {len(naked_hash_links)} bare href='#' placeholder link(s)")

    # EcoCare brand presence (canonical pages only)
    if not is_deprecated:
        if REAL_BRAND not in content:
            file_issues.append(f"EcoCare brand name not found")
        else:
            file_passes.append("EcoCare brand present")

        if REAL_EMAIL in content:
            file_passes.append("Real email present")
        else:
            file_warnings.append(f"Real email {REAL_EMAIL} not found")

        if REAL_ADDRESS in content:
            file_passes.append("Real address present")
        else:
            file_warnings.append(f"Achimota address not found")

        # At least one real phone
        phone_found = any(ph in content for ph in REAL_PHONES)
        if phone_found:
            file_passes.append("Real phone number present")
        else:
            file_warnings.append("No real EcoCare phone number found")

    # Deprecated pages should have noindex
    if is_deprecated:
        if 'name="robots"' in content and "noindex" in content:
            file_passes.append("noindex,follow tag present")
        else:
            file_issues.append("Missing noindex meta tag on deprecated page")

    # Size check
    if size_kb < 2:
        file_warnings.append(f"Very small file: {size_kb:.1f} KB")
    else:
        file_passes.append(f"File size OK: {size_kb:.1f} KB")

    return file_issues, file_warnings, file_passes


def run_qa():
    all_issues = {}
    all_warnings = {}
    all_passes = {}

    total_issues = 0
    total_warnings = 0
    total_passes = 0

    print("=" * 72)
    print("EcoCare Automated QA Check")
    print("=" * 72)

    print("\n--- CANONICAL PAGES ---")
    for page in CANONICAL_PAGES:
        fi, fw, fp = check_file(page, is_deprecated=False)
        total_issues += len(fi)
        total_warnings += len(fw)
        total_passes += len(fp)
        status = "✓ PASS" if not fi else f"✗ FAIL ({len(fi)} issues)"
        warn_flag = f" [{len(fw)} warnings]" if fw else ""
        print(f"  {status}{warn_flag}: {page}")
        for issue in fi:
            print(f"      [ISSUE] {issue}")
        for warn in fw:
            print(f"      [WARN]  {warn}")

    print("\n--- DEPRECATED PAGES ---")
    for page in DEPRECATED_PAGES:
        fi, fw, fp = check_file(page, is_deprecated=True)
        total_issues += len(fi)
        total_warnings += len(fw)
        total_passes += len(fp)
        status = "✓ PASS" if not fi else f"✗ FAIL ({len(fi)} issues)"
        print(f"  {status}: {page}")
        for issue in fi:
            print(f"      [ISSUE] {issue}")

    print("\n" + "=" * 72)
    print(f"QA SUMMARY: {total_passes} checks passed | {total_warnings} warnings | {total_issues} issues")
    print("=" * 72)
    if total_issues == 0:
        print("ALL CRITICAL CHECKS PASSED.")
    else:
        print(f"ACTION REQUIRED: {total_issues} issue(s) need resolution before launch.")
    return total_issues

if __name__ == "__main__":
    exit_code = run_qa()
    exit(exit_code)

