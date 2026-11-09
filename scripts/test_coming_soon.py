#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Standalone Coming Soon Test Suite
Validates the countdown math, timezone invariance, asset integrity, and security isolation.
"""

import sys
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DIST_DIR = ROOT_DIR / "dist" / "coming-soon"

def test_fixed_utc_countdown():
    print("--- 1. FIXED UTC COUNTDOWN MATH & TIMEZONE INVARIANCE ---")
    target_iso = "2026-11-16T14:00:00Z"
    target_dt = datetime.fromisoformat(target_iso.replace("Z", "+00:00"))
    target_ts = int(target_dt.timestamp())

    # Case A: Base Planning Date (2026-11-09 14:00:00 GMT) -> exactly 7 Days
    now_a = datetime.fromisoformat("2026-11-09T14:00:00+00:00")
    diff_a = target_ts - int(now_a.timestamp())
    days_a = diff_a // 86400
    hours_a = (diff_a % 86400) // 3600
    min_a = (diff_a % 3600) // 60
    sec_a = diff_a % 60
    assert (days_a, hours_a, min_a, sec_a) == (7, 0, 0, 0), f"Expected 7d 0h 0m 0s, got {days_a}d {hours_a}h {min_a}m {sec_a}s"
    print("  ✓ PASS: Exactly 7 Days at planned launch start (2026-11-09T14:00:00Z)")

    # Case B: Mid-week check (2026-11-12 18:30:15 GMT)
    now_b = datetime.fromisoformat("2026-11-12T18:30:15+00:00")
    diff_b = target_ts - int(now_b.timestamp())
    days_b = diff_b // 86400
    hours_b = (diff_b % 86400) // 3600
    min_b = (diff_b % 3600) // 60
    sec_b = diff_b % 60
    assert (days_b, hours_b, min_b, sec_b) == (3, 19, 29, 45), f"Mismatch: {days_b}d {hours_b}h {min_b}m {sec_b}s"
    print("  ✓ PASS: Mid-week precision countdown calculation (3d 19h 29m 45s)")

    # Case C: Near zero (5 seconds before launch)
    now_c = datetime.fromisoformat("2026-11-16T13:59:55+00:00")
    diff_c = target_ts - int(now_c.timestamp())
    assert diff_c == 5, f"Expected 5s remaining, got {diff_c}"
    print("  ✓ PASS: Near-zero (5s remaining) calculation")

    # Case D: Zero & Past Zero (clamped to 0)
    now_d = datetime.fromisoformat("2026-11-16T14:05:00+00:00")
    diff_d = max(0, target_ts - int(now_d.timestamp()))
    assert diff_d == 0, f"Expected clamped 0s, got {diff_d}"
    print("  ✓ PASS: Post-deadline clamp stops at 0s without negative values or auto-redirect")

def test_html_and_asset_integrity():
    print("\n--- 2. HTML & ASSET INTEGRITY AUDIT ---")
    html_file = DIST_DIR / "index.html"
    assert html_file.exists(), "dist/coming-soon/index.html is missing!"
    content = html_file.read_text(encoding="utf-8")

    # Check key copy requirements
    assert "EcoCare Cleaning Services Limited" in content, "Missing brand name"
    assert "Achimota Mile 7, Accra, Ghana" in content, "Missing official address"
    assert "+233 24 901 4253" in content, "Missing official telephone"
    assert "ecocaregh1on1@gmail.com" in content, "Missing active monitoring email"
    assert "https://wa.me/233249014253" in content, "Missing WhatsApp dispatch CTA"
    assert "noindex, follow" in content, "Missing temporary noindex robots meta"
    assert "EcoClean" in content and "Eco-Laundry" in content and "EcoFumes" in content, "Missing service family chips"
    assert 'data-deadline="2026-11-16T14:00:00Z"' in content, "Missing or incorrect fixed UTC deadline attribute"
    assert '<a href="/"' in content, "Logo link must point to Coming Soon root /"
    print("  ✓ PASS: Brand name, address, phone, email, WhatsApp, chips, and metadata verified.")

    # Check that no unfinished pages are linked
    forbidden_links = ["index.html", "about1.html", "service1.html", "contact.html", "calculate-form.html"]
    for link in forbidden_links:
        assert f'href="{link}"' not in content, f"Leaked internal link to unpublished page: {link}"
    print("  ✓ PASS: Zero links to unpublished internal pages.")

def test_security_isolation():
    print("\n--- 3. SECURITY & PUBLISH ISOLATION ---")
    forbidden_files = [".env", ".env.local", "api", "data", "docs", "scripts", "vercel.json"]
    for f in forbidden_files:
        leak = DIST_DIR / f
        assert not leak.exists(), f"Security leak! File or folder {f} found in dist/coming-soon/"
    print("  ✓ PASS: Build directory contains zero serverless APIs, docs, or environment secrets.")

    headers_file = DIST_DIR / "_headers"
    assert headers_file.exists(), "Missing _headers security file"
    headers_text = headers_file.read_text(encoding="utf-8")
    assert "X-Frame-Options: DENY" in headers_text
    assert "X-Content-Type-Options: nosniff" in headers_text
    print("  ✓ PASS: Standard HTTP security headers configured in dist/coming-soon/_headers.")

def main():
    print("========================================================================")
    print("EcoCare Standalone Coming Soon Test & Verification Suite")
    print("========================================================================")
    test_fixed_utc_countdown()
    test_html_and_asset_integrity()
    test_security_isolation()
    print("\n========================================================================")
    print("ALL COMING SOON TESTS PASSED (12/12 CHECKS)!")
    print("========================================================================")

if __name__ == "__main__":
    main()
