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

### Policy Verdict & Search Console Reconciliation
State A implements **Option 1** by default with strict crawl compliance:
```html
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://ecocaregh.com/">
```

#### Search Console Reconciliation Rule:
- **Do NOT submit `sitemap.xml` in Google Search Console while State A (`noindex`) is active.**
- Submitting an XML sitemap containing a URL with `<meta name="robots" content="noindex">` triggers a Google Search Console coverage error: **"Submitted URL marked 'noindex'"**.
- Crawlers will discover and respect `noindex, follow` automatically via ordinary HTTP crawling.
- **Sitemap submission in Google Search Console is scheduled for State B (Full Site Launch Day)** when all 16 canonical pages switch to `index, follow`.

---

## 3. Dedicated Robots & Routing Architecture for State A

Under State A, Netlify serves exclusively from `dist/coming-soon/` (and its synchronized mirror `deploy/coming-soon/`). Therefore, the root `robots.txt` and `sitemap.xml` of the full website are **never exposed** in the Coming Soon directory.

### A. Dedicated `dist/coming-soon/robots.txt`
```text
User-agent: *
Allow: /

# State A: 7-Day Coming Soon Launchpad
# Full sitemap submission is scheduled for State B (Full Site Launch) to prevent Search Console 'Submitted URL marked noindex' warnings.
```
*Crucial Rule:* Never use `Disallow: /` in `robots.txt`. A disallow rule prevents search engines from fetching the page entirely, which blinds them to the `noindex` tag and may lead to URL-only listing artifacts in search results.

### B. Loop-Free Netlify Catch-All Redirects (`_redirects`)
To prevent infinite redirect loops on root `/`:
```text
# State A Static Asset Passthrough
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
```
*Loop Prevention:* Omitting the exclamation mark `!` from `/* / 302` ensures Netlify uses shadowing: since `index.html` exists at `/`, Netlify serves it with HTTP 200 directly. Only non-existent paths (e.g. `/services`, `/about`) are redirected to `/`.

---

## 4. Staging & Deploy Preview Protection (Noindex vs. Access Restriction)

To protect the full website on Vercel preview environments (`ecocare-new.vercel.app`) or Netlify deploy-previews (`*.netlify.app`), two distinct levels of protection must be understood:

### Level 1: Search Engine De-indexing Protection (Active in `vercel.json` and `_headers`)
- `vercel.json` injects `X-Robots-Tag: noindex, nofollow` on all HTTP responses.
- **Effect:** Compliant search engine crawlers (Googlebot, Bingbot, DuckDuckGo) are instructed NOT to index the preview deployment in public search results.
- **Limitation:** This does **NOT** block human visitors who possess the link.

### Level 2: Actual Access Restriction (Authentication / Password Protection)
- If the business requires strict confidentiality where human visitors without credentials cannot view the staging preview:
  - Enable **Vercel Password Protection** in Project Settings -> Deployment Protection (requires Vercel Pro).
  - Or configure HTTP Basic Authentication at the reverse proxy/edge layer.
  - The public production domain on Netlify (`https://ecocaregh.com/`) serves strictly `dist/coming-soon/` (which contains zero full-site files), ensuring complete physical isolation for public visitors.

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

