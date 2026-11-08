# EcoCare Website — Changelog

**Project:** EcoCare Cleaning Services Limited — Clenix ThemeForest Migration  
**Repository:** `/Users/apple/Developer/work/ecocare`

---

## [1.0.0] — 8 November 2026

### ✅ Added — New Canonical Pages (14 pages built)
- `index.html` — Canonical EcoCare homepage with real brand, services, taglines, contact
- `about1.html` — About EcoCare: history, mission, CEO/founder Eric Nana Acquah, service philosophy
- `service1.html` — All 12 service listings directory (5 service families)
- `single-service1.html` — EcoClean: residential, commercial, industrial, post-construction, floor, window, event
- `single-service2.html` — Eco-Laundry: washing, ironing, delicates, dry cleaning, pickup & delivery
- `pest-control.html` — EcoFumes: termites, cockroaches, rodents, bed bugs, commercial compliance + safety protocol
- `carpet-cleaning.html` — Carpet: hot water extraction, stain removal, encapsulation, deodorization
- `upholstery-cleaning.html` — Upholstery: fabric sofas, leather conditioning, mattress allergen removal
- `pricing-table.html` — 3 non-priced service packages: Essential Residential, Deep Scrub, Corporate Facility
- `calculate-form.html` — Full quote/booking form with Select2, date picker, URL prefill via `?service=`
- `faq.html` — 9 verified EcoCare questions with Bootstrap accordion
- `contact.html` — Contact with phone, email, address, social links + verified Google Maps iframe embed
- `project1.html` — 8-card project showcase gallery with Isotope filtering by category
- `single-project1.html` — Commercial janitorial project case study detail
- `coming-soon.html` — Branded maintenance placeholder with real contact info
- `404.html` — Branded error page with working navigation and phone number
- `privacy-policy.html` — Draft privacy notice aligned to Ghana Data Protection Act (Act 843)
- `terms-condition.html` — Draft terms of service for EcoCare cleaning engagements

### ✅ Added — Build & Asset Infrastructure
- `scripts/template_core.py` — Modular page generator: `get_head()`, `get_header()`, `get_footer()`, `get_page_banner()`
- `scripts/build_canonical_pages.py` — Builds index, about1, service1, single-service1
- `scripts/build_remaining_canonical.py` — Builds all 14 remaining canonical pages
- `scripts/deprecate_demo_pages.py` — Adds `noindex,follow` and patches demo copyright on 13 deprecated pages
- `scripts/qa_check.py` — Automated QA checker: brand, contact, security, noindex (116 checks)
- `css/ecocare.css` — Brand CSS: CSS variables, logo sizing, service cards, audience boxes, legal notices
- `js/ecocare.js` — URL param prefill, form validation, honest UX feedback, XSS-safe output
- `vercel.json` — Clean URL rewrite rules for Vercel static deployment

### ✅ Added — Documentation Suite (`docs/ecocare/`)
- `IMPLEMENTATION_AUDIT.md` — Source authority tiers, file discovery manifest
- `PAGE_CONTENT_MATRIX.md` — All 26+ HTML files: role, status, route, sections
- `ASSET_AUDIT.md` — Every image, logo, font, vendor asset with status
- `CONTENT_APPROVAL_TODO.md` — 11 decisions requiring client approval (CA-01 to CA-11)
- `CONTENT_MAPPING.md` — Element-by-element mapping of all knowledge base facts to pages
- `ROUTE_REDIRECT_MATRIX.md` — Canonical vs deprecated route table
- `QA_REPORT.md` — Automated + manual QA results (116 passed, 0 issues)
- `RELEASE_BLOCKERS.md` — Pre-launch gate list with resolution guidance

### ✅ Fixed — Template Cleanup
- Removed 52 HTTrack `<!-- Mirrored from ... by HTTrack -->` comments across 26 HTML files
- Removed Cloudflare tracking beacon from all 26 HTML files
- Deleted `popper.html` (99KB scraped WordPress 404 page)
- Fixed `js/bootstrap.min.js` corrupted `require("popper.html")` → `require("popper.js")`

### ✅ Fixed — Brand Replacement
- Copied `logo.png` → `img/logo-dark.png`, `img/logo-dark2.png`, `img/large-logo.png`
- Copied `logo-icon.png` → `img/mobile-logo.png`
- Copied `favicon-01.png` → `img/favicon.png`
- Copied `banner-02.jpg` → `img/slider/slide1-1.jpg`
- Copied `aboutme.png` → `img/figure/aboutme.png`

### ✅ Fixed — Demo Page Deprecation
- Added `<meta name="robots" content="noindex, follow">` to all 13 unused demo pages
- Patched Clenix copyright → EcoCare copyright in all 13 deprecated pages
- Patched `info@clenix.com` → `ecocaregh1on1@gmail.com` in deprecated pages
- Updated all deprecated page titles from `clenix | ...` → `EcoCare — ... (Demo Page)`

### ❌ Removed — Demo Content
- Demo USD prices ($49/$99/$199) from pricing template
- Fabricated counter statistics ("2583+ Clients", "1200+ Projects")
- Demo stock staff models from team page (page deprecated/noindexed)
- Demo partner logos from brand carousel
- Demo Google Maps API key; replaced with verified `maps.google.com/embed` iframe

### ⚠️ Not Changed / Out of Scope
- Clenix CSS/JS animation stack (OwlCarousel, Nivo Slider, MeanMenu) — preserved intact
- Bootstrap 4.3.1 layout grid — preserved intact
- `vendor/` directory contents — untouched
- All 8 customer testimonials — held pending CA-09 client approval
- `info@ecocaregh.com` email — omitted from clickable links pending domain MX verification (CA-01)

