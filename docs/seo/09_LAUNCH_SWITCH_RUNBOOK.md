# EcoCare Cleaning Services Limited — Launch Switch-Over & Rollback Runbook
**Document:** `docs/seo/09_LAUNCH_SWITCH_RUNBOOK.md`  
**Date:** November 9, 2026  
**Status:** Operational Production Deployment Runbook  
**Domain:** `https://ecocaregh.com/`  

---

## 1. Overview & Pre-Flight Conditions

This runbook defines the exact operational procedure to transition `https://ecocaregh.com/` from **State A (7-Day Coming Soon)** to **State B (Full 18-Page Website)**.

### Pre-Flight Verification Gate (Do NOT Launch Until Closed):
- [ ] **RB-01:** Production email credentials (`RESEND_API_KEY` or SMTP) configured in Netlify environment variables and confirmed by receiving a live test submission in `ecocaregh1on1@gmail.com`.
- [ ] **RB-02:** Client confirms testimonial consent policy.
- [ ] **RB-03:** Client / legal counsel signs off on `privacy-policy.html` and `terms-condition.html`.
- [ ] **RB-07:** Pesticide safety & technician protocol verified with client.

---

## 2. Step-by-Step Switch-Over Procedure

### Step 1: Update `netlify.toml` Publish Directory
In the repository root, edit `netlify.toml`:
```toml
# Change the publish target from dist/coming-soon to . (or dist/full-site)
[build]
  command = "python3 scripts/enhance_seo_and_a11y.py"
  publish = "."
```

### Step 2: Ensure Root `_redirects` and `_headers` Are Active
Verify that `_redirects` and `_headers` exist in the repository root containing:
1. Apex domain unification (`www` -> non-www 301).
2. Clean URL 200 rewrites (`/about` -> `/about1.html`, `/services` -> `/service1.html`, etc.).
3. Legacy `.html` 301 redirects.
4. Custom 404 handler (`/*  /404.html  404`).

### Step 3: Run Full SEO & Metadata Generator
Execute the automated SEO generator locally:
```bash
python3 scripts/enhance_seo_and_a11y.py
```
This updates all canonical HTML files with `lang="en-GH"`, verified OpenGraph/Twitter social cards, structured data JSON-LD, and generates the full 16-URL `sitemap.xml`.

### Step 4: Run Complete QA Test Suite
Ensure 100% test pass rate across all suites:
```bash
python3 scripts/qa_check.py
python3 scripts/verify_responsive_and_routes.py
node scripts/test_form_backend.js
python3 scripts/test_seo_comprehensive.py
```

### Step 5: Commit & Push to GitHub
```bash
git add netlify.toml _redirects _headers sitemap.xml robots.txt
git commit -m "feat(release): switch Netlify publish target to full canonical website"
git push origin main
```
Netlify will automatically detect the push, run the build command, and deploy the full website to `https://ecocaregh.com/` within 30–60 seconds.

---

## 3. Post-Deployment Live Verification (Smoke Tests)

Immediately after Netlify deployment completes, run the following live curl checks:

```bash
# 1. Verify Homepage returns HTTP 200 with full site HTML
curl -I https://ecocaregh.com/

# 2. Verify Clean URLs return HTTP 200
curl -I https://ecocaregh.com/about
curl -I https://ecocaregh.com/services
curl -I https://ecocaregh.com/cleaning
curl -I https://ecocaregh.com/contact

# 3. Verify Legacy .html returns HTTP 301 redirect
curl -I https://ecocaregh.com/about1.html
# Expected: Location: https://ecocaregh.com/about

# 4. Verify www redirects to apex
curl -I https://www.ecocaregh.com/
# Expected: Location: https://ecocaregh.com/

# 5. Verify 404 page returns real HTTP 404 status
curl -I https://ecocaregh.com/non-existent-page-test
# Expected: HTTP/2 404

# 6. Verify full sitemap is accessible
curl -s https://ecocaregh.com/sitemap.xml | grep "<loc>" | wc -l
# Expected: 16 URLs
```

### Search Console Handshake:
1. Log in to [Google Search Console](https://search.google.com/search-console).
2. Go to **Sitemaps** -> Resubmit `sitemap.xml`.
3. Use the **URL Inspection** tool on `https://ecocaregh.com/` -> Click **Test Live URL** -> Click **Request Indexing**.

---

## 4. Emergency Rollback Procedure (Sub-60-Second Recovery)

If any unexpected blocker occurs on the live domain after launch, revert immediately to the isolated Coming Soon landing page:

1. In `netlify.toml`, revert `publish`:
   ```toml
   [build]
     command = "python3 scripts/build_coming_soon.py"
     publish = "dist/coming-soon"
   ```
2. Rebuild the Coming Soon artifact:
   ```bash
   python3 scripts/build_coming_soon.py
   ```
3. Commit and push:
   ```bash
   git add netlify.toml dist/coming-soon/
   git commit -m "revert(release): rollback to isolated 7-day coming soon page"
   git push origin main
   ```
Within 45 seconds, `https://ecocaregh.com/` will safely revert to the pristine Coming Soon countdown page while technical investigations proceed in private.
