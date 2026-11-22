# EcoCare Cleaning Services — Page & Content Routing Matrix

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Approved Architecture Plan  

---

## 1. Overview & Information Architecture Strategy

The website is structured into a clean, purposeful, static multi-page architecture. Rather than exposing 26 disjointed template demos to the public, we establish **one canonical path per subject area**, ensuring all internal links, breadcrumbs, and search engines target the canonical routes.

### Primary Public Navigation
1. **Home** (`index.html`)
2. **About Us** (`about1.html`)
3. **Services** (`service1.html` — Directory of all 12 services)
   - *EcoClean (Residential, Commercial & Deep Cleaning)* (`single-service1.html` / `cleaning.html`)
   - *Eco-Laundry (Washing, Ironing & Garment Care)* (`single-service2.html` / `laundry.html`)
   - *EcoFumes (Fumigation & Pest Control)* (`pest-control.html`)
   - *Carpet Cleaning (Deep Hot-Water Extraction)* (`carpet-cleaning.html`)
   - *Upholstery Cleaning (Sofas & Delicate Fabric Care)* (`upholstery-cleaning.html`)
4. **Projects / Gallery** (`project1.html`)
5. **Packages & Pricing** (`pricing-table.html` — Package comparison without fake fixed costs)
6. **FAQ** (`faq.html`)
7. **Contact Us** (`contact.html`)
8. **Primary Action CTA:** **Book Now** (`calculate-form.html`)

---

## 2. Screen-by-Screen Content Matrix

| Template File | Live Role / Status | Canonical Target Route | Source Data Used | Key Sections to Populate / Modify | Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `index.html` | **CANONICAL HOME** | `index.html` (`/`) | `ECOCARE_CONTENT_DATA.json` (hero, intro, service_groups, process) | Hero slider (with `banner-02.jpg`), 5 Core Services overview, 12-Service discovery grid, "Who We Serve", 4-Step booking process, Verified benefits, EcoCare footer. | No demo Clenix text, no fake metrics, no 30% discount, official logo in header/footer, working phone & quote CTAs. |
| `index2.html` | Alternative Demo | Redirect to `index.html` | Template layout | Keep for internal layout reference; exclude from public navigation and sitemap. | Not linked in public navigation. |
| `index3.html` | Alternative Demo | Redirect to `index.html` | Template layout | Keep for internal layout reference; exclude from public navigation. | Not linked in public navigation. |
| `index4.html` | Alternative Demo | Redirect to `index.html` | Template layout | Keep for internal layout reference; exclude from public navigation. | Not linked in public navigation. |
| `about1.html` | **CANONICAL ABOUT** | `about1.html` (`/about`) | `ECOCARE_CONTENT_DATA.json` (`company`, `about`), `ECOCARE_MASTER_KNOWLEDGE_BASE.md` §1 | Heritage story (grounded in Ghanaian Companies Code 1963 statement), Mission & Vision pillars, Environmental commitment, Leadership approach, Process overview. | Correct founding narrative (no fake 1992 date), no fake skill percentage bars, EcoCare logo, CTA to Services. |
| `about2.html` | Alternative Demo | Canonical to `about1.html`| Template layout | Keep for reference; exclude from public navigation. | Not linked in public navigation. |
| `service1.html` | **CANONICAL SERVICES DIRECTORY** | `service1.html` (`/services`) | `published_service_directory` (12 cards) | 12-Service grid with dedicated cleaning Flaticons: Office, Commercial, Washing/Ironing, Upholstery, House Cleaning, Fumigation, Industrial, Carpet, Floor, General, Window, Event Clean-Up. | All 12 historic services present; each links to its proper service family detail and quote request. No plumbing or car wash demo cards. |
| `service2.html` | Alternative Demo | Canonical to `service1.html`| Template layout | Keep for reference; exclude from public navigation. | Not linked in public navigation. |
| `single-service1.html` / `cleaning.html` | **CANONICAL SERVICE 1: ECOCLEAN** | `single-service1.html` | `service_groups.cleaning`, `cleaning-details.html` archive | Residential, commercial, industrial, post-construction, move-in/out, floor/marble, window cleaning. Quality assurance, safe equipment, service-specific FAQ. Sidebar with sibling services. | Deep informative copy, no fabricated health claims, brochure download hidden until real PDF provided, quote CTA. |
| `single-service2.html` / `laundry.html` | **CANONICAL SERVICE 2: ECO-LAUNDRY** | `single-service2.html` | `service_groups.laundry`, `service-details.html` archive | Washing, ironing, delicate garment care, dry cleaning, pickup/delivery information (framed honestly as subject to area confirmation). Service parameters sidebar. | Accurate laundry process, no fake pricing tables, working quote button with laundry prefill. |
| `pest-control.html` | **CANONICAL SERVICE 3: ECOFUMES** | `pest-control.html` | `service_groups.pest`, `fumigation-details.html` archive | Termites, cockroaches, rodents, mosquitoes, commercial/residential preventive treatment. Safety protocols, preparation guidelines. | No "100% baby safe" or unverified EPA claims; clear safety instructions; dedicated inquiry form. |
| `carpet-cleaning.html` | **CANONICAL SERVICE 4: CARPET CARE** | `carpet-cleaning.html` | `service_groups.carpet`, `capet-details.html` archive | Hot-water extraction, encapsulation, deep stain/odor treatment, carpet restoration. Fiber care advice, drying time expectations. | Honest drying/stain expectations without absolute guarantees; package inquiries. |
| `upholstery-cleaning.html` | **CANONICAL SERVICE 5: UPHOLSTERY CARE**| `upholstery-cleaning.html` | `service_groups.upholstery`, `Upholstery-details.html` archive | Sofas, dining chairs, mattresses, fabric and leather furniture cleaning. Delicate material handling, deodorization, fabric protection. | Replaces unverified "90% dry" claim with realistic expectations; clear booking CTA. |
| `project1.html` | **CANONICAL PROJECTS / GALLERY** | `project1.html` (`/projects`) | `ECOCARE_MASTER_KNOWLEDGE_BASE.md` §8 | Portfolio gallery of service categories (Commercial, Residential, Carpet Restoration, Post-Construction). Honest captions describing types of work without inventing fake client names. | Real category filters; lightboxes function correctly; no fictional corporate testimonials. |
| `single-project1.html` | Case Study Template | `single-project1.html` | Real project portfolio | Structured case study outline (Challenge, Solution, Scope). | Excluded from public nav unless verified client case study data is approved. |
| `pricing-table.html` | **CANONICAL PACKAGES** | `pricing-table.html` | `ECOCARE_MASTER_KNOWLEDGE_BASE.md` §4, §6 | 3 Service Packages: (1) Carpet & Upholstery Care, (2) Deep Clean & Move-In Package, (3) Commercial & Office Routine Maintenance. "Book Now" buttons. | Replaces \$49/\$99/\$199 demo tiers with custom quote inquiries; clear explanation that pricing depends on property size and condition. |
| `calculate-form.html` | **CANONICAL QUOTE / BOOKING** | `calculate-form.html` (`/request-quote`) | `ECOCARE_MASTER_KNOWLEDGE_BASE.md` §9 | Comprehensive booking request form: Service Family, Specific Service, Property Type, Area/Size, Appointment Date/Time, Name, Phone, Email, Location/Address in Accra, Notes. | Replaces USD price calculator with genuine quote inquiry form; pre-fills service from URL params; client-side validation; clear notice that request is pending confirmation. |
| `faq.html` | **CANONICAL FAQ** | `faq.html` (`/faq`) | `ECOCARE_MASTER_KNOWLEDGE_BASE.md` §6 | 9 Source-aware questions: service areas in Ghana, booking process, commercial cleaning schedules, eco-friendly detergents, preparation for fumigation, payment options. | Responsive Bootstrap 4 accordion; sidebar contact widget; invitation to call for custom requirements. |
| `contact.html` | **CANONICAL CONTACT** | `contact.html` (`/contact`) | `ECOCARE_CONTENT_DATA.json` (`contact`) | Achimota Mile 7 address, +233 24 901 4253, +233 24 380 7100, `ecocaregh1on1@gmail.com`, active social channels (Facebook, TikTok, YouTube). Verified Google Maps embed. | No demo Google Maps key; fixed mailto mismatch; robust contact form with real feedback. |
| `team1.html` | Leadership & Team | `team1.html` | `company.founders_and_leaders` | "Our People & Approach" editorial section; verified roles (Eric Nana Acquah - CEO); avoids stock portraits pretending to be staff. | Honest presentation; no fictional 8-person team. |
| `team2.html`, `single-team.html` | Alternative Demo | Internal reference | Template layout | Excluded from public navigation pending client-approved staff bios. | Not linked in public navigation. |
| `coming-soon.html` | **CANONICAL COMING SOON** | `coming-soon.html` | EcoCare brand assets | Clean maintenance landing page with EcoCare logo, service summary, and direct phone/email contact. | Countdown clock removed (unless launch date confirmed); real contact details. |
| `404.html` | **CANONICAL 404** | `404.html` | EcoCare brand assets | Branded error screen with mop illustration, friendly error message, and working links to Home and Services. | EcoCare logo, working Home/Services navigation. |
| `privacy-policy.html` | **DRAFT LEGAL POLICY** | `privacy-policy.html` | `ECOCARE_CONTENT_DATA.json` (`legacy_policies`) | Privacy notice covering inquiry data, contact channels, and non-disclosure; prominently flagged as DRAFT PENDING LEGAL APPROVAL. | Clean, honest notice without dark patterns. |
| `terms-condition.html` | **DRAFT LEGAL POLICY** | `terms-condition.html` | `ECOCARE_CONTENT_DATA.json` (`legacy_policies`) | Service terms covering estimates, quotes, access to premises, cancellations; flagged as DRAFT PENDING LEGAL APPROVAL. | Clean, honest terms. |
| `shop.html`, `single-product.html` | Unsupported Demo | Archived | E-Commerce demo | EcoCare does not operate an approved public online store. Excluded from public navigation, sitemap, and footer. | Not accessible via public navigation. |
| `blog1.html`, `blog2.html`, `single-blog1.html` | Unsupported Demo | Archived | Blog demo | EcoCare has no client-approved blog editorial archive. Excluded from public navigation and footer. | Not accessible via public navigation. |
| `popper.html` | Extraneous Artifact | Deprecate / Delete | Scraped WordPress 404 | 99KB error file captured during site scraping. | Removed from public build. |

