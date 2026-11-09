# EcoCare Cleaning Services Limited — Coming Soon Indexing Policy & Deployment Isolation
**Document:** `docs/seo/01_COMING_SOON_INDEXING_POLICY.md`  
**Date:** November 9, 2026  
**Status:** Approved & Implemented in `scripts/build_coming_soon.py`  
**Deployment Target:** Netlify (`publish = "dist/coming-soon"`)  
**Domain:** `https://ecocaregh.com/`  

---

## 1. Executive Summary

EcoCare Cleaning Services Limited operates in two strictly separated deployment states:
- **State A (Active Now):** A lightweight, isolated 7-day Coming Soon website at `https://ecocaregh.com/`.
- **State B (Full Launch):** The complete 18-page canonical website with online quotation scoping, service detail hubs, interactive booking, and portfolio showcase.

This policy defines the technical search engine indexing rules, crawl directives, sitemap architecture, and preview isolation for **State A**.

---

## 2. The Core Indexing Dilemma & Architectural Decision

### Options Considered
1. **Option 1 (Pre-Launch Guarded — Recommended & Active):**
   - Directives: `<meta name="robots" content="noindex, follow">` + Allowed in `robots.txt`.
   - **Rationale:** Prevents Google and Bing from caching temporary countdown text, numbers, and "Coming Soon" page titles as the permanent search snippet for `ecocaregh.com`. When the full site launches 7 days later, search engines will immediately crawl and index the rich, permanent homepage without having to flush out stale Coming Soon snippet text.
   - **Crawlability:** Crawlers are explicitly **Allowed** in `robots.txt` so they can fetch the HTML, verify the official domain ownership, read the brand entity schema, and follow outbound links (e.g. WhatsApp, Facebook, TikTok).
2. **Option 2 (Indexable Brand Anchor):**
   - Directives: `<meta name="robots" content="index, follow">` + Single-URL `sitemap.xml`.
   - **Rationale:** Establishes initial domain indexing immediately with company name, address, phone number, and Accra geography.
   - **Downside:** Google often retains "Coming Soon" title tags in search cache for several weeks after full launch.

### Policy Verdict
State A implements **Option 1** by default with strict crawl compliance:
```html
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://ecocaregh.com/">
```
If the business owner requests immediate domain indexing before launch, setting `"allow_index": true` in `data/seo-pages.json` switches the meta tag to `index, follow` and rebuilds the sitemap automatically.

---

## 3. Dedicated Robots & Sitemap Architecture for State A

Under State A, Netlify serves exclusively from `dist/coming-soon/`. Therefore, the root `robots.txt` and `sitemap.xml` of the full website are **never exposed** in the Coming Soon directory.

### A. Dedicated `dist/coming-soon/robots.txt`
```text
User-agent: *
Allow: /

# Dedicated State A Sitemap for EcoCare Launch Countdown
Sitemap: https://ecocaregh.com/sitemap.xml
```
*Crucial Rule:* Never use `Disallow: /` in `robots.txt`. A disallow rule prevents search engines from fetching the page entirely, which blinds them to the `noindex` tag and may lead to URL-only listing artifacts in search results.

### B. Dedicated `dist/coming-soon/sitemap.xml`
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://ecocaregh.com/</loc>
    <lastmod>2026-11-09</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```
*Zero Leakage:* Exactly 1 URL is listed. Zero unfinished service, pricing, or policy URLs are exposed to crawlers.

---

## 4. Staging & Deploy Preview Protection

To prevent Vercel preview environments (`ecocare-new.vercel.app`) or Netlify deploy-previews (`*.netlify.app`) from competing with or canonicalizing over `https://ecocaregh.com/`, non-production hosts are guarded at the HTTP response level:

### HTTP Header Configuration (`_headers`)
```text
/*
  X-Frame-Options: DENY
  X-XSS-Protection: 1; mode=block
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
```

On Netlify deploy previews and Vercel branch deployments, the following header is added for any preview URL:
```text
X-Robots-Tag: noindex, nofollow
```
This ensures zero duplicate staging indexes in Google without contaminating production HTML with global preview meta tags.

---

## 5. Security & Isolation Verification Gates

The automated builder (`scripts/build_coming_soon.py`) enforces:
1. **Asset Boundary Verification:** Verifies 15/15 local assets (CSS, JS, fonts, logos, preloader artwork).
2. **Exclusion Gate:** Confirms that zero Python backend scripts, zero `.env` files, zero serverless API files (`api/`), zero legal draft warnings, and zero full website HTML files are copied into `dist/coming-soon/`.
3. **URL Integrity:** The brand logo points strictly to `/` (the Coming Soon root), preventing 404 navigation errors.
4. **Timezone Invariance:** The launch deadline is hardcoded in UTC ISO 8601 (`2026-11-16T14:00:00Z`), ensuring identical countdown behavior across all global visitors.
