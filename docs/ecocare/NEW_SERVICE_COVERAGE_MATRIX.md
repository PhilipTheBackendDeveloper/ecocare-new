# EcoCare Cleaning Services — Four Client-Confirmed Services Coverage Matrix

**Date:** 10 November 2026  
**Feature Branch:** `feat/ecocare-four-confirmed-services`  
**Governing Standard:** Clenix Purchased Template Architecture, Google SEO Quality Raters Guidelines, and EcoCare Truthfulness Guardrails.

---

## 1. Executive Summary

In response to direct instructions from Daddy (EcoCare business owner), four confirmed service offerings have been deeply integrated across the complete EcoCare website codebase:

1. **Sofa and Carpet Cleaning Solutions** (Strategic bundle enhancement)
2. **Polytank Cleaning** (New dedicated canonical page)
3. **Car Interior Cleaning** (New dedicated canonical page)
4. **Professional Dusting Cleaning** (New dedicated canonical page)

To maintain search authority and prevent keyword cannibalization, **Sofa and Carpet Cleaning Solutions** was architected as an umbrella integration across existing high-performing pages (`carpet-cleaning.html` and `upholstery-cleaning.html`), featuring reciprocal cross-links and bundled quote options rather than a duplicate competing page. Dedicated canonical pages were created for the three other distinct physical service domains.

---

## 2. Traceability Matrix

| Confirmed Offering | Canonical Route | Physical File | Schema.org Type | Discovery Entry Points | Quote Form Keys | Truthfulness & Operational Guardrails |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Sofa and Carpet Cleaning Solutions** | `/carpet-cleaning`<br>`/upholstery-cleaning` | `carpet-cleaning.html`<br>`upholstery-cleaning.html` | `Service` (`#service`) | • Homepage Featured Services #6<br>• Services Directory Card #4<br>• Reciprocal bundle modules on both pages<br>• Nav & Footer menus | `sofa-carpet`<br>`carpet`<br>`upholstery` | Custom quote on inspection; zero fabricated bundle discounts or unrealistic dry time promises. |
| **Polytank Cleaning** | `/polytank-cleaning` | `polytank-cleaning.html` | `Service` (`#service`) | • Homepage Featured Services #7<br>• Services Directory Card #13<br>• Packages custom scope section<br>• All site header & footer menus | `polytank` | Standard non-confined physical scrub and sediment flush. Explicitly disclaims potability/sterilization claims without accredited lab testing. |
| **Car Interior Cleaning** | `/car-interior-cleaning` | `car-interior-cleaning.html` | `Service` (`#service`) | • Homepage Featured Services #8<br>• Services Directory Card #14<br>• Packages custom scope section<br>• All site header & footer menus | `car-interior` | Strictly scoped to mobile doorstep vehicle interior upholstery & detailing across Greater Accra. Exterior paint buffing and mechanical repairs explicitly omitted. |
| **Professional Dusting Cleaning** | `/professional-dusting` | `professional-dusting.html` | `Service` (`#service`) | • Homepage Featured Services #9<br>• Services Directory Card #15<br>• EcoClean suite section `#dusting`<br>• All site header & footer menus | `dusting` | Focuses on electrostatic microfiber particulate trapping and Harmattan haze mitigation for ceiling fans, HVAC vents, and high ledges. Avoids hospital-grade sterilization claims. |

---

## 3. Surface-by-Surface Verification

### 3.1. Navigation Menus & Global Header
- **Desktop Template Main Menu (`nav#dropdown`):**
  - Updated to eliminate fragile hardcoded count (`All 12 Service Listings` &rarr; `Services Directory`).
  - Added clean dropdown links to all canonical offerings across all 21 pages.
- **Mobile Navigation (`jquery.meanmenu.min.js`):**
  - Automatically receives the updated dropdown tree without layout breakage.

### 3.2. Homepage (`index.html`)
- **Featured Services Grid:** Expanded from 6 to 9 balanced Bootstrap cards (3 full rows of 3 columns).
- **Quotation Form (`#ecocare-booking-form`):** Added selectable options for `polytank`, `car-interior`, `dusting`, and `sofa-carpet`.
- **Structured Data:** Injected 3 additional `Offer` nodes into the primary `LocalBusiness` offer catalog.

### 3.3. Service Directory (`service1.html`)
- **Grid Rebalancing:** Expanded from 12 to 15 cards (5 full rows of 3 columns in the native Clenix grid).
- **Card 4 Updated:** Retitled to *Sofa & Upholstery Cleaning* with couch and fabric suite descriptions.
- **Cards 13–15 Added:** Polytank Cleaning, Car Interior Cleaning, and Professional Dusting added with native Clenix hover animations and FontAwesome/Flaticon icons.

### 3.4. Estimation Calculator (`calculate-form.html`)
- Updated `<select name="service" id="form-service">` with all new options.
- Added contextual placeholder instructions encouraging clients to specify tank capacity, vehicle model, or living room suite counts.

### 3.5. Packages & Pricing (`pricing-table.html`)
- Added dedicated custom scoping section detailing quotation factors for Polytanks (capacity/elevation), Vehicles (vehicle class/upholstery type), and Sofa & Carpet bundles.

### 3.6. Frequently Asked Questions (`faq.html`)
- Added 4 verified FAQ entries addressing tank cleaning intervals (6–12 months), mobile car interior on-site power/water requirements, microfiber dusting vs. sweeping, and combined sofa/carpet booking.

### 3.7. Routing & Staging Infrastructure
- **`_redirects` & `vercel.json`:** Clean URL rewrites (HTTP 200) and legacy `.html` redirects (HTTP 301) configured for `/polytank-cleaning`, `/car-interior-cleaning`, and `/professional-dusting`.
- **`scripts/build_staging.py`:** Added new canonical files to compiler manifest; verified zero leaks and strict `X-Robots-Tag: noindex, nofollow` isolation.
- **`sitemap.xml`:** Expanded from 16 to 19 indexable canonical clean routes.

---

## 4. Test Verification Summary

1. `scripts/enhance_seo_and_a11y.py`: ✓ Processed 34 HTML files, generated 19 sitemap routes.
2. `scripts/build_staging.py`: ✓ Compiled 20 canonical pages, 232 files (22.36 MB).
3. `scripts/test_netlify_forms.js`: ✓ 14/14 tests passed.
4. `scripts/qa_check.py`: ✓ 131/131 checks passed, 0 warnings, 0 issues.
5. `scripts/test_coming_soon.py`: ✓ 12/12 checks passed (Public 7-day countdown at `ecocaregh.com` 100% isolated).
6. `scripts/verify_responsive_and_routes.py`: ✓ 120/120 checks passed across 21 pages.
7. `scripts/test_seo_comprehensive.py`: ✓ All 7 quality gates passed (100% success).
