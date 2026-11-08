# EcoCare Cleaning Services — Comprehensive Asset Audit

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Verification & Classification Audit  

---

## 1. Asset Classification Standard

Every visual, typography, script, and third-party asset in the repository is classified into one of the following five categories:

- **[VERIFIED_OWNER]**: Verified authentic EcoCare brand asset supplied in the workspace root.
- **[TEMPLATE_ILLUSTRATIVE]**: Bundled with the purchased Clenix template; legally usable as illustrative photography or decorative vectors, but must NOT be claimed as completed EcoCare projects or real EcoCare employees.
- **[HOLD_PERMISSION]**: Historical or third-party image/logo referenced in old website files; pending explicit client authorization, copyright verification, or privacy consent.
- **[DEMO_REMOVE]**: Clenix placeholder, demo tracking script, or demo API key that must be removed from live pages.
- **[MISSING_LEGACY]**: Referenced in old HTML/PHP handlers, but file is not present in repository.

---

## 2. Brand & Identity Assets

| Asset File / Path | Dimensions / Format | Classification | Action & Implementation Target |
| :--- | :--- | :--- | :--- |
| `logo.png` (root) | 1630x743 RGBA PNG | **[VERIFIED_OWNER]** | Official EcoCare logo. Deploy to `img/logo-dark.png`, `img/logo-dark2.png`, `img/large-logo.png`, and `img/mobile-logo.png`. Set `alt="EcoCare Cleaning Services Limited"`. |
| `logo-icon.png` (root) | 1630x743 RGBA PNG | **[VERIFIED_OWNER]** | Square/symbol brand mark. Used for compact mobile headers and badge icons. |
| `favicon-01.png` (root) | 500x500 RGBA PNG | **[VERIFIED_OWNER]** | Deploy as `img/favicon.png` and update all `<link rel="shortcut icon">` references across all HTML files. |
| `banner-02.jpg` (root) | 1920x706 JPEG | **[VERIFIED_OWNER]** | Official EcoCare hero banner. Integrate as the primary homepage slider background image (`slide1-1.jpg`). |
| `aboutme.png` (root) | 499x499 RGBA PNG | **[VERIFIED_OWNER]** | Branded company overview graphic. Integrate into `about1.html` and homepage About sections. |
| `ecocare contact.jpg` (root) | 1080x1150 JPEG | **[VERIFIED_OWNER]** | Authentic EcoCare service photograph. Deploy to `contact.html` and quote inquiry sections. |
| `ecocare contact-2.jpg` (root) | 686x960 JPEG | **[VERIFIED_OWNER]** | Service photo. Deploy to sidebar widgets and booking forms. |
| `call.png` (root) | 500x500 RGBA PNG | **[VERIFIED_OWNER]** | High-visibility direct dial icon. Used for phone callout boxes (`+233 24 901 4253`). |
| `offer-bg.png` (root) | 1320x384 PNG | **[VERIFIED_OWNER]** | Promotional section background banner. |
| `oru-company-bg.png` (root) | 1920x838 PNG | **[VERIFIED_OWNER]** | Corporate section background banner. |
| `replace.jpg` (root) | 736x736 JPEG | **[VERIFIED_OWNER]** | Feature square photo. Deploy in service showcase. |
| `img/logo-dark.png` | 250x60 PNG | **[DEMO_REMOVE]** | Clenix demo logo. Replaced by `logo.png`. |
| `img/logo-dark2.png` | 250x60 PNG | **[DEMO_REMOVE]** | Clenix demo logo variant. Replaced by `logo.png`. |
| `img/large-logo.png` | 300x80 PNG | **[DEMO_REMOVE]** | Clenix white footer demo logo. Replaced by `logo.png`. |
| `img/favicon.png` | 16x16 PNG | **[DEMO_REMOVE]** | Clenix demo favicon. Replaced by `favicon-01.png`. |

---

## 3. Template Illustrative Photography (`img/`)

| Directory | Files Count | Classification | Usage Rules |
| :--- | :--- | :--- | :--- |
| `img/slider/` | 9 files (`slide*.jpg`) | **[TEMPLATE_ILLUSTRATIVE]** | General illustrative cleaning imagery. Usable as secondary slider slides, but `banner-02.jpg` is prioritized as Slide 1. |
| `img/service/` | 12 files (`service*.jpg`) | **[TEMPLATE_ILLUSTRATIVE]** | Service category cards (Kitchen, Window, Floor, Office). Usable as category visuals with neutral captions. |
| `img/team/` | 14 files (`team*.png`) | **[TEMPLATE_ILLUSTRATIVE]** | Cutout models. **NEVER label these as named EcoCare staff.** Use only in generic "Our Approach" or replace with real staff when authorized. |
| `img/project/` | 8 files (`project*.jpg`) | **[TEMPLATE_ILLUSTRATIVE]** | Usable in gallery to illustrate types of cleaning work (commercial floor, residential deep clean). Do NOT invent fictional clients (e.g. "Google Office"). |
| `img/figure/` | 72 files | **[TEMPLATE_ILLUSTRATIVE]** | Background bubbles, wave dividers, breadcrumb banner (`breadcumb.jpg`), and 404 error illustration (`404.png`). |
| `img/brand/` | 9 files (`brand*.png`) | **[DEMO_REMOVE]** | ThemeForest template demo partner logos. Must be removed from public view unless replaced by real verified associations (e.g., CCAG). |

---

## 4. Third-Party Scripts, Keys & Embeds

| Asset | Location | Classification | Remediation Plan |
| :--- | :--- | :--- | :--- |
| Cloudflare Beacon Script | Lines ~1146 in all 26 HTML pages | **[DEMO_REMOVE]** | Third-party tracking script sending analytics to template author's Cloudflare account. **Delete completely from all HTML pages.** |
| Demo Google Maps Key | `contact.html` line 524 (`AIzaSyBtm...`) | **[DEMO_REMOVE]** | Untrusted public demo API key. Replace with clean, privacy-conscious Google Maps embed iframe targeting Achimota Mile 7, Accra, Ghana (`ECOCARE_CONTENT_DATA.json`). |
| `vendor/php/form-process.php` | Referenced in `js/main.js` | **[MISSING_LEGACY]** | File was not bundled by template author in HTTrack mirror. Implement robust client-side validation, user feedback, and direct `tel:`/`mailto:` fallback channels. |
| `popper.html` | Root directory (99KB) | **[DEMO_REMOVE]** | Scraped WordPress 404 page with heavy tracking scripts. Delete file safely from repository. |

---

## 5. Webfonts & Icon Assets

| Asset | Location | Classification | Status & Integrity |
| :--- | :--- | :--- | :--- |
| Cleaning Flaticon Font | `font/flaticon.css`, `font/Flaticon.*` | **[TEMPLATE_ILLUSTRATIVE]** | 23 dedicated cleaning icons (`flaticon-clean`, `flaticon-mop`, `flaticon-vacuum`, `flaticon-brush`, etc.). Fully verified, renders locally. |
| FontAwesome 5 Free | `css/fontawesome-all.min.css`, `webfonts/fa-*` | **[TEMPLATE_ILLUSTRATIVE]** | Solid, Regular, and Brands webfonts. Verified, renders locally without external CDN dependencies. |
| Google Fonts (`Roboto`, `Poppins`) | `@import` in `style.css` | **[TEMPLATE_ILLUSTRATIVE]** | Standard web font imports. Fully functional. |

