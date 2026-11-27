# EcoCare Cleaning Services Limited — Production Website Repository

[![Production Ready](https://img.shields.io/badge/Status-Production%20Ready-success.svg)](https://ecocaregh.com)
[![Verified Tests](https://img.shields.io/badge/Test%20Suite-100%25%20Passing-brightgreen.svg)](scripts/)
[![Deployment](https://img.shields.io/badge/Deploy%20Target-Netlify%20%26%20Vercel-blue.svg)](netlify.toml)

Official production codebase for **EcoCare Cleaning Services Limited** (`https://ecocaregh.com/`), Greater Accra, Ghana. Headquartered at Achimota Mile 7, EcoCare specializes in corporate janitorial services, residential deep cleaning, doorstep eco-laundry, regulated pest control (EcoFumes), carpet and upholstery extraction, polytank sanitation, car interior detailing, and post-construction scrubbing.

---

## 1. Architecture & Technology Footprint

- **Frontend Core:** Semantic HTML5, Bootstrap 4.3.1, custom modular CSS (`css/ecocare.css`), FontAwesome 5, jQuery 3.3.1, MeanMenu responsive navigation, Owl Carousel, Select2, and datetimepicker.
- **Serverless Backend (Vercel):** Node.js serverless functions in `api/`:
  - `/api/quote`: Validates and records structured booking/quotation requests, fires email notifications to `ecocaregh1on1@gmail.com`, and provides pre-filled WhatsApp URLs.
  - `/api/contact`: Validates general contact and inquiry submissions.
- **Static Hosting (Netlify):** Dual-engine submission support via native Netlify Forms with client-side honeypots, fast-timing bot defenses (<1000ms), and automated fallback to serverless APIs.
- **Direct Dual WhatsApp Dispatch:**
  - **Line 1:** `+233 24 901 4253` (`233249014253`)
  - **Line 2:** `+233 24 380 7100` (`233243807100`)
- **SEO & Canonical Routing:** Full apex domain unification (`https://ecocaregh.com/`), clean URL rewrites without `.html` extensions, custom HTTP 404 handler, JSON-LD structured schemas, and strict `sitemap.xml`.

---

## 2. Directory Structure

```text
├── api/                     # Vercel serverless functions (/api/quote, /api/contact)
├── css/                     # Production stylesheets (ecocare.css, bootstrap, select2, etc.)
├── data/                    # Persistent storage (.gitignore'd submissions.jsonl, seo-pages.json)
├── deploy/                  # Local preview artifacts (coming-soon synchronized copy)
├── dist/                    # Deployment targets:
│   ├── coming-soon/         # State A: Active 7-Day Countdown Landing Page
│   └── staging/             # State B: Full 20-Page Production Canonical Website
├── docs/                    # Architectural documentation, SEO matrices, and runbooks:
│   ├── ecocare/             # Technical specifications, release blockers, content mappings
│   └── seo/                 # Canonical URLs, JSON-LD audits, and 09_LAUNCH_SWITCH_RUNBOOK.md
├── font/ & webfonts/        # Flaticon and FontAwesome vector webfonts
├── img/                     # Optimized visual media assets:
│   ├── blog/                # Insights article thumbnails
│   ├── figure/              # Team and company branding graphics
│   ├── projects/            # Authentic field project photographs & video poster stills
│   │   └── videos/          # Authentic client project MP4 field recordings
│   ├── services/            # Dedicated service photography matching each offering
│   ├── slider/              # Hero video poster and banner slides
│   └── team/                # Authentic leadership and operations crew photography
├── js/                      # Modular scripts (ecocare.js, meanmenu, validator, etc.)
├── scripts/                 # Automated build, verification, QA, and test suites
├── vendor/                  # Third-party slider, carousel, and PHP native fallbacks
├── _headers                 # Production HTTP security headers & asset caching policies
├── _redirects               # Netlify apex unification, clean URLs, and legacy 301 redirects
├── netlify.toml             # Netlify deployment configuration & context switcher
├── robots.txt               # Crawler directives with canonical sitemap reference
├── sitemap.xml              # XML Sitemap indexing all 18 canonical URLs
└── vercel.json              # Vercel clean URL rewrites, redirects, and preview headers
```

---

## 3. Automated Test & Verification Suites

Before every release or deployment, execute the comprehensive test pipeline:

```bash
# 1. Rebuild staging distribution
python3 scripts/build_staging.py

# 2. Run form backend & serverless API test suite (10 unit/integration tests)
node scripts/test_form_backend.js

# 3. Run Netlify form attributes, validation, and honeypot test suite
node scripts/test_netlify_forms.js

# 4. Run master repository QA check (114 validation checks)
python3 scripts/qa_check.py

# 5. Run responsive layout & route rewrite audit (119 checks)
python3 scripts/verify_responsive_and_routes.py

# 6. Run technical SEO, JSON-LD, sitemap, and safety gate
python3 scripts/test_seo_comprehensive.py

# 7. Run Coming Soon state isolation audit
python3 scripts/test_coming_soon.py

# 8. Run exhaustive link, button, modal, and form audit across all pages
python3 scripts/exhaustive_audit.py
```

*One-liner to run all checks:*
```bash
python3 scripts/build_staging.py && node scripts/test_form_backend.js && node scripts/test_netlify_forms.js && python3 scripts/qa_check.py && python3 scripts/verify_responsive_and_routes.py && python3 scripts/test_seo_comprehensive.py && python3 scripts/test_coming_soon.py && python3 scripts/exhaustive_audit.py
```

---

## 4. Production Deployment Workflow

The repository is configured for automated Git-driven deployments (identical to Vercel):
- **Live Production (`main` branch):** Netlify automatically executes `python3 scripts/build_production.py` and publishes `dist/production/`. All 20 canonical pages, Netlify forms, clean URLs, and production SEO (with `Allow: /` and sitemap) deploy live to `https://ecocaregh.com/` in under 45 seconds.
- **Deploy Previews & Branch Deploys:** Netlify builds `dist/staging/` with `X-Robots-Tag: noindex, nofollow` to protect production SEO during testing.
- **Vercel Preview Mirrors:** Vercel automatically deploys preview environments with serverless endpoints `/api/quote` and `/api/contact`.

### To Deploy to Production:
Simply merge `feat/ecocare-four-confirmed-services` into `main` and push to GitHub:
```bash
git checkout main
git merge feat/ecocare-four-confirmed-services
git push origin main
```
Netlify will automatically detect the push to `main`, compile `dist/production/`, and go live immediately.

---

## 5. Contact & Support

- **EcoCare Office:** Achimota Mile 7, Near Police Station, Accra, Ghana
- **Dispatch Lines:** +233 24 901 4253 / +233 24 380 7100
- **Email:** ecocaregh1on1@gmail.com
- **Website:** https://ecocaregh.com
