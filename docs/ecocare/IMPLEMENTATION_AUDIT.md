# EcoCare Cleaning Services — Implementation Audit & Source Hierarchy

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Canonical Foundation Audit  
**Author:** Lead Engineering & Implementation Team  

---

## 1. Discovered Source Artifacts & Exact Repository Paths

A recursive inspection of `/Users/apple/Developer/work/ecocare/` identifies the following canonical source and asset files:

### 1.1 EcoCare Knowledge & Content Specifications
- `knowledge.md` (`/Users/apple/Developer/work/ecocare/knowledge.md`): Initial audit of the legacy EcoCare website (`ecocare-website.vercel.app` / `PhilipTheBackendDeveloper/ecocare-website`). Contains legacy service cards, historic contact numbers, and PHP form error analysis.
- `ECOCARE_MASTER_KNOWLEDGE_BASE.md` (`/Users/apple/Developer/work/ecocare/ECOCARE_MASTER_KNOWLEDGE_BASE.md`): Master content bible (735 lines). Comprehensive narrative covering history, governance, five service families, twelve historic cards, draft editorial copy, risk registers, and verification requirements.
- `ECOCARE_CONTENT_DATA.json` (`/Users/apple/Developer/work/ecocare/ECOCARE_CONTENT_DATA.json`): Canonical structured dataset (131KB) containing structured service groups, editorial copy proposals, historical review texts (flagged `HOLD`), source manifest, and risk registers.
- `ECOCARE_README.md` (`/Users/apple/Developer/work/ecocare/ECOCARE_README.md`): Overview of content packages and client review cautions.
- `ECOCARE_THEMEFOREST_AI_PROMPT.md` (`/Users/apple/Developer/work/ecocare/ECOCARE_THEMEFOREST_AI_PROMPT.md`): Migration rules and priority directives.
- `template-inventory.md` (`/Users/apple/Developer/work/ecocare/template-inventory.md`): 44KB technical catalog of the Clenix HTML5 template architecture, component classes, styles, and scripts.

### 1.2 Official Supplied EcoCare Brand Assets (Root Directory)
- `logo.png` (1630x743 RGBA PNG): Official high-resolution EcoCare Cleaning Services logo with signature brand icon and typography.
- `logo-icon.png` (1630x743 RGBA PNG): Official EcoCare brand mark icon variant.
- `favicon-01.png` (500x500 RGBA PNG): Official square EcoCare brand icon for browser favicons and touch icons.
- `banner-02.jpg` (1920x706 JPEG): Official branded hero banner graphic for homepage slider.
- `aboutme.png` (499x499 RGBA PNG): Branded circular company overview feature graphic.
- `ecocare contact.jpg` (1080x1150 JPEG) & `ecocare contact-2.jpg` (686x960 JPEG): Branded team/customer service visual assets.
- `call.png` (500x500 RGBA PNG): Direct communication callout badge icon.
- `offer-bg.png` (1320x384 PNG) & `oru-company-bg.png` (1920x838 PNG): Branded section background patterns.
- `replace.jpg` (736x736 JPEG): Square promotional feature photo.
- Contextual imagery: `Attractive black female cleaning agent _ Premium AI-generated image.jpg`, `Elderly People and House Cleaning Services in OKC.jpg`, `Love!.jpg`, `My_PDF.png`, `mobile copy.png`, `noName.png`, `5f3ed2dd-f80e-410d-b913-5491b32062de.jpg`.

### 1.3 Clenix ThemeForest Template Source Files
- **Core HTML Pages (26 screens + 1 artifact):**
  - Homepages: `index.html`, `index2.html`, `index3.html`, `index4.html`
  - About: `about1.html`, `about2.html`
  - Services: `service1.html`, `service2.html`, `single-service1.html`, `single-service2.html`
  - Projects: `project1.html`, `single-project1.html`
  - Team: `team1.html`, `team2.html`, `single-team.html`
  - Pricing & Calculation: `pricing-table.html`, `calculate-form.html`
  - FAQ: `faq.html`
  - Shop (Demo): `shop.html`, `single-product.html`
  - Blog (Demo): `blog1.html`, `blog2.html`, `single-blog1.html`
  - Contact: `contact.html`
  - Utilities: `coming-soon.html`, `404.html`
  - Scraped Error Artifact: `popper.html` (99KB WordPress 404 page from radiustheme.com)
- **CSS Architecture:** `style.css` (8,200+ lines, custom indexed), `css/bootstrap.min.css`, `css/animate.min.css`, `css/fontawesome-all.min.css`, `css/jquery.datetimepicker.css`, `css/magnific-popup.css`, `css/meanmenu.min.css`, `css/normalize.css`, `css/select2.min.css`.
- **JavaScript Core:** `js/jquery-3.3.1.min.js`, `js/bootstrap.min.js`, `js/popper.min.js`, `js/modernizr-3.7.1.min.js`, `js/main.js`, `js/jquery.meanmenu.min.js`, `js/isotope.pkgd.min.js`, `js/imagesloaded.pkgd.min.js`, `js/jquery.magnific-popup.min.js`, `js/jquery.datetimepicker.full.min.js`, `js/select2.min.js`, `js/validator.min.js`, `js/waypoints.min.js`, `js/jquery.counterup.min.js`, `js/jquery.countdown.min.js`, `js/jquery.elevatezoom.js`.
- **Vendor Plugins:** `vendor/OwlCarousel/` (Owl Carousel 2), `vendor/slider/` (Nivo Slider).
- **Icon Webfonts:** `font/flaticon.css` + `font/Flaticon.*` (23 cleaning icons), `webfonts/fa-*` (FontAwesome 5 Free).
- **Template Media:** `img/slider/` (9 images), `img/service/` (12 images), `img/team/` (14 cutouts), `img/blog/` (18 images), `img/project/` (8 images), `img/figure/` (72 images), `img/brand/` (9 placeholders).

---

## 2. Source Authority & Publication Policy

To guarantee factual integrity, legal compliance, and avoid unverified claims, all public-facing text and functionality must adhere strictly to the following four-tier authority hierarchy:

1. **Tier 1 — Explicit Owner-Approved Current Information:**
   - Real business facts formally confirmed by leadership (e.g., active corporate phone numbers, confirmed physical office address in Achimota Mile 7, Accra).
   - Only confirmed facts may be stated without qualifiers.
2. **Tier 2 — Source-Aware Knowledge Bank Entries (`ECOCARE_CONTENT_DATA.json` & `ECOCARE_MASTER_KNOWLEDGE_BASE.md`):**
   - Core five service families (EcoClean, Eco-Laundry, EcoFumes, Carpet Cleaning, Upholstery Cleaning).
   - Twelve historic service directory card names.
   - Proposed editorial copy (hero, intro, process, service intro) edited into neutral, professional, truthful prose.
3. **Tier 3 — Historical Website Archive (Old HTML/PHP):**
   - Historical references (e.g., claimed incorporation in September 2014 under the Ghanaian Companies Code 1963; CCAG membership).
   - *Policy:* Retained for brand heritage but framed cautiously as historical statements rather than unverified active claims.
   - Testimonials, numerical counters (e.g., "2583+ clients"), and discounts (e.g., "30% off") are strictly held pending client approval.
4. **Tier 4 — Clenix ThemeForest Template Source:**
   - **UI, styling, layout, and animation source ONLY.**
   - Never a factual or content source for EcoCare.
   - All Clenix demo text, demo phone numbers, demo addresses, demo team members, and demo prices (\$49/\$99/\$199) must be completely eliminated from live public routes.

---

## 3. Implementation Guardrails & Non-Negotiables

1. **No Hallucinations or Fake Content:**
   - No fabricated pricing, fake customer reviews, fictional staff portraits, unverified certifications (e.g., EPA/CCAG), or absolute safety guarantees ("100% baby safe").
2. **Every Link & Button Works:**
   - No `href="#"`, `javascript:void(0)` dummy links, or broken internal routes.
   - All 12 historic service listings navigate to the specific service family detail page.
3. **Form Integrity:**
   - Forms must not pretend to send emails if no backend handler exists.
   - Implement real client-side validation, robust error/success feedback, and direct telephone/email click-to-contact fallbacks.
4. **Branding Consistency:**
   - EcoCare logo, icon, and favicon deployed globally across all pages, headers, footers, mobile menus, and browser metadata.

