
# EcoCare Cleaning Services — Existing Website Knowledge Bank

**Researched on:** 8 November 2026  
**Purpose:** Preserve the old website's useful business information, service descriptions, content structure, assets and known technical problems as a source of reference for a future website. **This is an audit, not a redesign plan.**

## 0. Research standards and caveats

- **[SITE]** = present on the existing public website, but *not independently verified with the business*. A published claim is not necessarily a true or current fact.
- **[CODE]** = directly observed in the user's connected GitHub source repository, `PhilipTheBackendDeveloper/ecocare-website` (main branch at review time).
- **[INFERENCE]** = analytical interpretation, not a confirmed business requirement.
- **[CONFIRM]** = information that must be confirmed by Daddy / EcoCare before use in the new public website.
- Public HTML text and public repository source were inspected. Dynamic form submissions were **not** sent; email delivery, end-to-end booking, database state, mobile rendering, accessibility tooling, and Lighthouse scores were **not** experimentally validated. A browser visual screenshot audit was not completed. The old custom domain was inaccessible to these web checks; the owner's report of missed renewal has not been independently established.
- Logos, photos, reviews, customer names, awards, discount offers and numerical KPIs must not be treated as client-approved without permission and source verification.

**Canonical public source:** https://ecocare-website.vercel.app/  
**Canonical code source:** https://github.com/PhilipTheBackendDeveloper/ecocare-website  
**Source tree:** https://api.github.com/repos/PhilipTheBackendDeveloper/ecocare-website/git/trees/main?recursive=1

## 1. Business identity

| Attribute | Existing-site information | Status / caveat |
| --- | --- | --- |
| Public brand | EcoCare | [SITE] |
| Legal name | EcoCare Cleaning Services Ltd / EcoCare Cleaning Services Limited | [SITE] Confirm precise registry spelling |
| Related labels | Ecoclean, EcoClean, Eco-Laundry, EcoFumes | [SITE] Terminology inconsistent; clarify trademark/brand architecture |
| Industry | Cleaning, laundry, fumigation/pest control, carpet and upholstery cleaning | [SITE] |
| Main office | Achimota Mile 7, Accra, Ghana | [SITE] Ask for map pin/GhanaPost GPS |
| Service footprint | Operations across Ghana | [SITE] [CONFIRM] Current coverage/fees, not established per region |
| Claimed registration | September 19, 2014, under the Ghanaian Companies Code 1963 | [SITE] [CONFIRM] Check registration documents/current legal citation |
| Claimed business commencement | September 30, 2014 | [SITE] [CONFIRM] |
| Claimed association | Contract Cleaners Association of Ghana (CCAG) | [SITE] [CONFIRM] membership/current standing |
| Named founder/shareholder | Eric Nana Acquah | [SITE] [CONFIRM] |
| Second named shareholder | Margaret Owusua **Boakye** (company copy) | [SITE] [CONFIRM] |
| Team page name | Margaret Owusua **Acquah** (team profile) | [SITE] **Name conflict** vs Boakye; do not silently normalize |
| Leadership | Eric Nana Acquah — CEO; Margaret Owusua Acquah — Administrative Accountant | [SITE] [CONFIRM] current roles, names, permission to feature |
| Tagline 1 | “Protect the Environment, Live Better, Prolong Life.” | [SITE] Preserve as old brand language; confirm final wording |
| Tagline 2 | “You got dirt? We got Clean.” | [SITE] Wording/grammar needs approval if polished |
| Positioning | Quality, sustainability, convenience, professional expertise, customer satisfaction | [SITE]/[INFERENCE] |

### Mission / vision language captured from About page

- **Neighborhood Revitalization:** Work with neighbours to build cleaner, safer neighbourhoods and improve environmental quality.
- **Sustainable Growth:** Develop an eco-conscious cleaning economy that creates jobs and protects the environment.
- **Excellence:** Continuous innovation and improvement to sustain high quality.

Site: https://ecocare-website.vercel.app/about-us.html

### Differentiators promoted in the old website

- Expert team and service quality.
- “Eco-friendly” products and methods.
- Broad commercial and domestic service coverage.
- Pickup/delivery or at-home service, according to service type.
- Competitive/affordable pricing and flexible scheduling, with no substantiating price table.
- “24/7 Supports” is **advertised**, but service hours differ per category; confirm meaning of support availability.

## 2. Contact and public-facing channels

| Channel | Old site value | Status |
| --- | --- | --- |
| Phone A | +233 24 901 4253 | [SITE] footer/contact/about |
| Phone B | +233 24 380 7100 | [SITE] footer/contact/about |
| Main Gmail | ecocaregh1on1@gmail.com | [SITE] footer/booking |
| Other Gmail | ecocare1on1@gmail.com | [SITE] appears parenthetically on contact page; **not same address** |
| Branded mailbox | info@ecocaregh.com | [SITE] contact page; [CODE] form recipient in several PHP handlers; mail delivery **unverified** |
| Office | Mile 7, Achimota, Accra | [SITE] |
| Historical custom domain | ecocaregh.com | [SITE]/[CODE] domain in email; ownership, DNS, renewal, current delivery unverified |
| Deployment address | ecocare-website.vercel.app | public website available in the web crawler |

**Configured social links in page source (ownership/activity not verified):**

- Facebook: https://www.facebook.com/profile.php?id=100006412849415&mibextid=ZbWKwL
- TikTok: https://www.tiktok.com/@ecocarecompanylimited
- YouTube channel: https://www.youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA

**Important:** Ask which two phone numbers, primary email and social accounts should appear publicly, and whether the branded mailbox can actually receive/send mail before choosing it for contact forms.

## 3. Complete old service taxonomy

### A. EcoClean — residential, commercial and industrial cleaning

**[SITE] Description summary:** Domestic cleaning; office/commercial cleaning; industrial/warehouse/manufacturing-site cleaning; regular maintenance and intensive/deep cleaning; window and glass cleaning; tiles/grout and floor polishing/cleaning; move-in/out; post-construction; sanitization/disinfection; curtain/drapery care; event cleanup. Some descriptions contain strong health and sanitation claims that need qualification.

Old service cards (service-grid page) include:

1. Office Cleaning
2. Commercial Cleaning
3. Upholstery Cleaning
4. House Cleaning Services
5. Industrial Cleaning
6. Carpet Cleaning
7. Floor Cleaning (written “Mable, Tiles & Grout” — presumably marble, but confirm)
8. General Cleaning
9. Window and Glass Cleaning
10. Event Clean-Up Services

**Packages advertised** on cleaning detail page:
- Carpet & Upholstery Care Package
- Deep Clean Package
- Move-In/Move-Out Cleaning Package
- Post-Construction Clean Package

No trustworthy published package prices, dimensions, minimum order, cleaning checklist, or contract duration was located.

**Old page:** https://ecocare-website.vercel.app/cleaning-details.html

### B. Eco-Laundry — garment care

**[SITE]** Washing, ironing, delicate-item dry cleaning, stain handling, collection/pickup and delivery.

**Packages/options shown:**
- Ironing only
- Washing only
- Dry Cleaning
- Pick-Up and Delivery

**Need confirmation:** actual garment types accepted, turnaround times, collection zones, pricing model, item care/claims policy, payment methods and availability.

**Old page:** https://ecocare-website.vercel.app/service-details.html

### C. EcoFumes — fumigation and pest control

**[SITE]** Treatment/management of termites, mosquitoes, cockroaches, rodents and other pests; residential, office, commercial/industrial, warehouse and restaurant settings; preventive visits and tailored treatment plans.

**Packages shown:**
- Basic Pest Control Package
- Comprehensive Pest Management Package
- Commercial & Industrial Pest Control Package
- Emergency Pest Control Package
- Eco-Friendly Pest Control Package

**[CONFIRM]** Safety, treatment products, site preparation, re-entry period, staff qualifications, licensing/approvals and the difference between professional pest treatment and true fumigation. Do **not** reuse unconditional statements such as being completely safe for pets/children or free from harsh chemicals without evidence.

**Old page:** https://ecocare-website.vercel.app/fumigation-details.html

### D. Carpet cleaning

**[SITE]** Deep cleaning and stain/odour removal, with method descriptions for hot-water extraction/steam, dry cleaning and encapsulation; initial assessment, pretreatment, extraction and deodorizing.

**Packages shown:**
- Standard Deep Cleaning Package
- Premium Restoration Package
- Pet-Friendly Package
- Commercial Carpet Care Package

**[CONFIRM]** Methods/equipment actually owned; fabric restrictions, drying estimates, pricing by square metre/room, service coverage and safety claims.

**Old page:** https://ecocare-website.vercel.app/capet-details.html (spelling is `capet` in old URL).

### E. Upholstery cleaning

**[SITE]** Sofa, chair, fabric/leather treatment, dry/steam cleaning and stain removal. Historical copy says equipment performs warm-water extraction and carpets/upholstery become “90% dry” after extraction; this quantitative claim needs proof before republishing.

**Packages shown:**
- Stain Removal
- Leather Upholstery Conditioning
- Fabric Protection
- Deep Upholstery Sanitization

**[CONFIRM]** Whether all these are actually sold as separate packages, equipment/material suitability, leather care, drying time, pricing, and before/after images.

**Old page:** https://ecocare-website.vercel.app/Upholstery-details.html (capital `U` in URL).

## 4. Hours and operational coverage shown on service pages

- **Laundry:** Monday–Saturday 7:30 a.m.–7:00 p.m.; Sunday **closed**.
- **Cleaning:** Monday–Friday 7:30 a.m.–7:00 p.m.; Saturday/Sunday 8:30 a.m.–7:00 p.m.
- **Carpet, upholstery and fumigation:** same 7:30 a.m. weekday and 8:30 a.m. weekend timetable appears on corresponding pages.
- **About:** advertises **24/7 support**, which may refer to answering enquiries, not performing services; clarify.
- All published schedules are historical unconfirmed website content. The general booking flows do not show confirmed real-time capacity.

## 5. Old customer journey / information architecture

**Navigation:** Home → About Us → Services dropdown (View All, Laundry, EcoClean, EcoFumes, Carpet, Upholstery) → Projects → Contacts.

**Homepage sections** observed from text/source:
1. Logo/navigation/hero with environmental slogan; banner images rather than a homepage video tag.
2. Six featured categories: Upholstery, Home Cleaning, Carpet Cleaning, Laundry, Commercial Cleaning, Fumigation and Pest Control.
3. Company introduction and leadership background.
4. Phone call CTA.
5. Three-step customer process: select service → book/schedule → the team serves / pickup and delivery or on-site visit.
6. “Why Trust Us”: quality, experienced team, green commitment, convenience.
7. Brochure advertisement with an image of a QR code, **not an identifiable direct downloadable PDF**. No PDF asset exists in the inspected repository tree.
8. Testimonials.
9. Client/partner logos.
10. “30% Off Discount” promotional CTA — **date and terms unverified**.
11. Footer with contact information, social links, privacy and terms.

**About page:** history, mission/vision, brand arguments, KPI counters, leaders/team and three testimonials.

**Services grid:** 12 visible service-card entries, search input and category checkboxes. The visible page/source does not establish that the filters produce real results. Several cards link through to common cleaning-detail or booking pages.

**Projects link:** currently resolves to `/categories.html`, a mixed carpet/upholstery/window-cleaning gallery, not a clearly organized case-study portfolio. Multiple images/video thumbnails may be illustrative rather than documented client jobs. Ask for approved case studies, location, photos and outcomes.

**Service-detail pages:** summary, gallery/video/reviews, package list, related service options, static published hours, embedded Google map and Book Service action.

**Contact page:** two phone numbers, mixed email addresses, address, enquiry form and map. Form points to PHP.

**Legal:** privacy policy and short cancellation/suspension terms; the terms page lacks broader service contract topics such as refunds, warranties, limits, liability, customer preparation, chemical use, delayed delivery and complaints.

## 6. Source inventory / routes

The source repository currently has **20 root-level HTML files and 9 PHP files**, not counting HTML files buried under vendor assets. We inspected public page text for the main routes and read source markup for key files. Two service-list variants and the booking-done page exist in GitHub but direct public web-tool fetches were inaccessible during the review; their live deployment status must not be inferred from this alone.

| File | Purpose | Status |
| --- | --- | --- |
| `index.html` | Home | Public crawler accessible; source read |
| `about-us.html` | Company/story/team | Public accessible; source read |
| `service-grid.html` | All-services listing | Public accessible; source read |
| `service-details.html` | Laundry detail | Public accessible; source read |
| `cleaning-details.html` | EcoClean detail | Public accessible; source read |
| `fumigation-details.html` | EcoFumes detail | Public accessible; source read |
| `capet-details.html` | Carpet detail | Public accessible; source read |
| `Upholstery-details.html` | Upholstery detail | Public accessible; source read |
| `categories.html` | “Projects”/gallery page | Public accessible; source read |
| `contact-us.html` | Contact | Public accessible; source read |
| `booking.html` | General cleaning booking | Public accessible; source read |
| `booking-laundry.html` | Laundry booking | Public accessible; source read |
| `booking-fumigation.html` | Fumigation booking | Public accessible; source read |
| `booking-upholstery.html` | Upholstery booking | Public accessible; source read |
| `booking-capet.html` | Carpet booking | Public accessible; source read |
| `privacy-policy.html` | Privacy information | Public accessible |
| `terms-condition.html` | Partial terms | Public accessible |
| `booking-done.html` | Intended confirmation screen | Source present; not verified integrated/deployed |
| `service-list.html` | Alternative service listing template | Source present; not verified public |
| `service-list2.html` | Second alternative listing template | Source present; not verified public |

**PHP files:** `appointment.php`, `appointment_handler.php`, `Laundry-booking.php`, `carpet-booking.php`, `fumigation-booking.php`, `upholstery-booking.php`, `contact.php`, `process.php`, `send-email.php`. Also present: a tracked `debug.log` that should be checked for safety/necessity before migrating or republishing.

**Repository technology footprint:** Static HTML, CSS, Bootstrap, jQuery, Owl Carousel, AOS, Select2, assorted vendor JS, and PHP contact/booking email handlers. No `vercel.json`, package.json, application backend, or build configuration was present in the inspected root/tree. This is not a Next.js project. Repository tree contained approximately 498 image files and **no video files or PDF files** by common extensions at review time.

## 7. Booking and contact forms — code-level findings

**Not proven operational.** Form existence in HTML does not prove messages are delivered. In the checked repository, PHP handlers call the native `mail()` function. Vercel does not automatically execute arbitrary PHP scripts as a standard static site; a suitable runtime or separate backend would need to be configured. No supporting runtime configuration was found in this repository. Avoid declaring bookings successful without an actual tested delivery path.

| Form | HTML `action` | Example fields | Issues verified in source |
| --- | --- | --- | --- |
| General cleaning `booking.html` | `appointment.php` | `name`, `phone`, `email`, `serviceType`, `state`, `location`, `appointmentDate`, `appointmentTime` | Handler expects `serviceMode`, but form sends `state`; likely missing data/validation failure; `appointment_handler.php` separately expects snake_case fields yet is not linked from this form. |
| Laundry `booking-laundry.html` | `Laundry-booking.php` | `serviceType`, `modeOfService`, `location`, dates | Handler expects `serviceMode`, not `modeOfService`; subject text is incorrectly “Ecocare Fumigation Booking”. |
| Fumigation `booking-fumigation.html` | `fumigation-booking.php` | `serviceType`, `serviceMode`, `location`, dates | Field names appear aligned; delivery/runtimes still unverified. |
| Upholstery `booking-upholstery.html` | `upholstery-booking.php` | `service_type`, `service_mode`, `appointment_date`, `appointment_time` | Handler expects camelCase equivalents (`serviceType`, `serviceMode`, `appointmentDate`, `appointmentTime`), causing mismatch; wrong fumigation subject. |
| Carpet `booking-capet.html` | `carpet-booking.php` | `serviceType`, `state`, `location`, dates | Handler redirects to missing `carpet-booking.html` instead of real `booking-capet.html`. |
| Contact `contact-us.html` | `contact.php` | `name`, `email`, `phone`, `message` | PHP native mail; uses `FILTER_SANITIZE_STRING`, removed in newer PHP versions; no proven delivery; branded recipient mailbox unverified. |

**Business workflow gaps in current source:**

- No supported evidence of a persisted booking database, booking reference or dashboard.
- No real-time appointment availability, conflict detection or staff dispatch logic established.
- No price calculation, price quote, deposit, customer tracking or receipts.
- No verified confirmation email/SMS/WhatsApp, nor staff notification monitoring.
- Customer address is captured as a selectable location, without a detailed street/address or map pin in the shown forms.
- No cancellation/rescheduling interface or operational exception handling established.
- No end-to-end test or actual mail delivery was run here; these are source-audit findings, not results of a production penetration test.

**Risk:** Do not launch a new contact/booking UI with an untested success message. Either clearly present it as an enquiry/quote request or implement a real tested backend and notification system when scope is agreed.

## 8. Other content and UX/quality flags

### High-priority correction candidates

1. **Unverifiable business metrics** — About page says “2583+ Satisfied Clients”, “80+ Expert Team”, “2129+ Project Completed”, “10+ Years of experience”. Obtain evidence or remove. Years should be calculated from actual operating start, not left frozen.
2. **Inconsistent identities** — Margaret’s surname appears as Boakye and Acquah; “Ecoclean” is used as if it were the company name despite the registered brand EcoCare.
3. **Conflicting contact channels** — Two different Gmail addresses appear, branded `info@ecocaregh.com` appears on contact/handlers, plus two phone numbers. Confirm active routing.
4. **Offer credibility** — Homepage promises a 30% discount without visible dates, scope or eligibility; remove until approved.
5. **Client logos and reviews** — Names and testimonials appear on the website, but permission/authenticity is not substantiated by publication alone.
6. **24/7 vs scheduled hours** — Clarify support vs on-site operating hours and category schedules.
7. **Legal text and data handling** — Privacy policy is general and does not map to an actually verified form-processing stack, retention, processors, rights request channel, etc. Under Ghana’s Data Protection Act, 2012 (Act 843), personal data handling has compliance implications; obtain appropriate legal/business review before launch.
8. **Eco/environment/chemical claims** — Avoid absolute health or non-toxic claims without documentation, especially fumigation.

### UI, SEO and content observations grounded in code

- Every inspected page shares the generic `<title>EcoCare Cleaning Services Limited</title>`; no per-page meta description was found in the HTML reviewed.
- Many images use alt text `img` or `image`; need meaningful descriptions for real content images and decorative handling for others.
- Site root contains misspelled filenames `capet-details.html` and `booking-capet.html`; uppercase `Upholstery-details.html` is case-sensitive on some hosts.
- Service-grid search and checkbox controls look like filter UI, but no tested effective filtering was established; keyword inputs have no semantic form `name` in the inspected section.
- Homepage source contains commented-out references to third-party template `html.truelysell.com/template3/search.html` and login flows; `booking-done.html` contains a comment identifying a 2023 HTTrack mirror of that template. Audit and remove unused template remnants before migrating.
- Brochure is advertised with a QR-code image, but no PDF asset or direct PDF link was located in the inspected repository source. QR content has not been decoded/verified; do not imply a live brochure download exists.
- Homepage `<video>` markup and `.mp4/.webm` assets were not observed. A new 15-second home hero video was separately discussed for EcoCare in a previous project conversation; it is not evidence that the current home page deploys video.
- Repository assets include some filenames suggesting third-party stock/Unsplash/premium imagery and a large vendor asset library. Rights and actual representation of EcoCare work must be confirmed before reuse.
- Footer copyright reads © 2025 although this audit is in November 2026.
- No actual Lighthouse/mobile-device/accessibility/SEO crawler test was completed. Do not invent scores or claim verified broken mobile views.

## 9. Testimonial and clientele records — approval required

**Homepage reviewer identities/roles shown:** Nana Esi (Doctor), Raymond Okyere (Tech Lead), Peter Darko (CEO), Derek Agyapong (Operations Manager).

**About-page reviewer identities/roles shown:** Sarah Amissiah (Residential Client), Jessica Poku (Uber), Jephthah Datsomor (Moove Ghana).

**Service-page reviewer names:**
- Laundry: Doris Asante, Paul Asamoah, Eric Baffour, Bradley Aggrey.
- Cleaning: John Hussy, James Appiah, Michael Owusu, Jessica Awuah.
- Fumigation: Philip Agyei, Reagan Tetteh, Samuella Yeboah, Nora Nyarko.
- Carpet: Daniel Agyemang, Frank Quaye, Kevin Gyamfi, Rebecca Eshun.
- Upholstery: Dennis Quansah, Jaime Seidu, Martinez Boadi, Helen Konadu.

**Client/partner logos present in repository:** Moove, Lexta Ghana, Uber, ICGC, Stone Consulting & Management, TAG. The home page visually refers to six partner logos; repository contains seven partner assets. **[CONFIRM]** Whether each is a real client/partner, what relationship is approved for disclosure, and image/logo usage permissions. Logos should not be interpreted as endorsements without approval.

These names and reviews are a **source inventory only**; none have been independently authenticated, and no contact was made to the individuals.

## 10. Service-oriented content hierarchy to preserve as research material

*Not a signed-off sitemap; for later planning.*

- Company story: history, founder/leadership, environmental goals, reasons to trust EcoCare.
- Service catalog: EcoClean, Eco-Laundry, EcoFumes, carpet, upholstery, with related sub-services.
- Service descriptions: customer problem, method (verified), scope/limitations, location, customer preparation, arrival/delivery, quote path.
- Proof: portfolio, before/after assets, testimonials, partnerships only when consented and supported.
- Customer contact: phone, WhatsApp if officially approved, email, location and lead form; later booking scope to be agreed.
- Policies: privacy, terms/cancellation, payment/refund and safety-related disclosures appropriate to services.

## 11. Questions to resolve with client **later, before planning sign-off**

**Identity and legal:** exact registered name, registration details/updated legal reference, principal names/roles, which surname is correct for Margaret, CCAG status, licences/credentials for pest treatment.

**Contact:** confirm primary phone/WhatsApp, official email inbox, address/GhanaPost GPS, service zones, weekend hours and whether emergency/24-hour enquiries are genuinely handled.

**Services:** current five core service categories, dropped/added offers, package names, minimum order, quote-based vs published prices, service delivery process, pickup/delivery, SLA, areas outside Accra, chemical preparation and safety.

**Trust:** real staff/vehicle/equipment photos, approved client logo list, permission for testimonials, real before/after projects and permission to use images.

**Operations:** whether booking should request a quote or reserve a slot, office assignment/approval process, customer confirmation and notification responsibilities.

**Marketing:** active 30% discount, brochure PDF (if real), desired contact CTA, real social profiles, existing analytics/Google Business Profile and search keywords.

**Technical/ownership:** old and proposed custom domain availability, expiration/recovery eligibility, who controls registrar/DNS/Vercel/GitHub, working email, and whether the old source assets/licenses can transfer.

**Commercial (developer-client relationship; not website content):** user reports an approximately GHS 100 unpaid balance from the previous job and that the old domain was not renewed. Do not assume exact invoice amount or status without reconciliation. Keep custom-domain purchase/annual renewals separate from the new development fee and make payment/handover ownership explicit in a new agreement. The new project's agreed upfront payment was 50%; this document does not constitute an invoice or payment agreement.

## 12. Reuse rules for the new project

| Content class | Recommendation |
| --- | --- |
| Service categories / broad business offering | **Retain as draft source information**, confirm current offering |
| Company history, contact and leadership | **Verify with client** before publishing |
| Mission, vision, original taglines | **Retain as reference**, rewrite carefully only after brand approval |
| Photos, logos, testimonials, partner names | **Quarantine until rights and factual permission verified** |
| KPI counters, health/environmental claims, discount | **Do not publish as facts without substantiation** |
| Static PHP booking/contact backend | **Do not copy as-is**; needs properly tested server-side design |
| Template pages/vendor assets | **Reassess license, functionality, relevance and performance** |
| Legal pages | **Use as input only**, not as approved legal final copy |
| Page URLs | Preserve old URLs for redirect mapping only when actual public traffic exists and migration is commissioned |

## 13. Source links by category

**Website:**
- Home: https://ecocare-website.vercel.app/
- About: https://ecocare-website.vercel.app/about-us.html
- Services: https://ecocare-website.vercel.app/service-grid.html
- Laundry: https://ecocare-website.vercel.app/service-details.html
- Cleaning: https://ecocare-website.vercel.app/cleaning-details.html
- Fumigation: https://ecocare-website.vercel.app/fumigation-details.html
- Carpet: https://ecocare-website.vercel.app/capet-details.html
- Upholstery: https://ecocare-website.vercel.app/Upholstery-details.html
- Gallery/Projects: https://ecocare-website.vercel.app/categories.html
- Contact: https://ecocare-website.vercel.app/contact-us.html
- General booking: https://ecocare-website.vercel.app/booking.html
- Laundry booking: https://ecocare-website.vercel.app/booking-laundry.html
- Fumigation booking: https://ecocare-website.vercel.app/booking-fumigation.html
- Upholstery booking: https://ecocare-website.vercel.app/booking-upholstery.html
- Carpet booking: https://ecocare-website.vercel.app/booking-capet.html
- Privacy: https://ecocare-website.vercel.app/privacy-policy.html
- Terms: https://ecocare-website.vercel.app/terms-condition.html

**Relevant source-code file examples:**
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/index.html
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/booking.html
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/appointment.php
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/Laundry-booking.php
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/booking-upholstery.html
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/upholstery-booking.php
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/carpet-booking.php
- https://github.com/PhilipTheBackendDeveloper/ecocare-website/blob/main/contact.php

**Background compliance/technology reading:**
- Ghana Data Protection Commission: https://dpc.gov.gh/compliance/
- DPC portal: https://app.dpc.gov.gh/
- Community PHP runtime for Vercel (not official): https://github.com/vercel-community/php

## 14. Research conclusion

The old EcoCare website is a substantial **content reference**: identity, five main service families, detailed sub-services, business vision, customer acquisition flow, contact details, testimonials and imagery. It is **not** a validated production specification or a trustworthy source for every marketing claim. In particular, form handlers, old template fragments, naming inconsistencies, legal copy, static availability and unapproved promotional assets should not be carried into the new build unchanged.

## 15. Official Owner Promotional Flyer Audit (November 2026)

**Source:** Official EcoCare promotional flyer provided directly by Daddy (business owner).  
**Status:** `[CLIENT-CONFIRMED]` for core service names and telephone contacts; `[CONFIRM]` for visual brand migration and unverified promotional claims.

### 15.1. Confirmed Service Offerings
The promotional flyer officially confirms the following specific service offerings:
1. **Polytank Cleaning:** Storage water tank washing, sediment removal, and hygienic sanitation.
2. **Laundry for Curtains, Duvets and Bedspreads:** Specialized residential linen care, bulky drapery and bedding wash/press alongside standard garment laundry.
3. **Sofa Cleaning and Fabric Care:** Living room sofa sets, fabric suites, cushions, and upholstery preservation.
4. **Carpet Deep Cleaning:** Heavy-traffic carpet and rug soil extraction.
5. **Car Detailing and Cleaning (Both Interior and Exterior):** Full mobile automotive cleaning covering exterior hand wash/paint detailing AND interior seat shampooing/carpet extraction.
6. **Professional Dusting Cleaning:** Previously confirmed by owner; fine particulate capture for ceilings, fans, vents, and seasonal Harmattan dust.

### 15.2. Confirmed Contact Channels
- **Primary Phone:** `+233 24 901 4253`
- **Secondary Phone:** `+233 24 380 7100`
- Both numbers are authentic EcoCare communication lines. Primary status remains with `+233 24 901 4253`.

### 15.3. Visual Brand & Color Scheme Observation
- The promotional flyer features a **gold-and-navy** visual palette.
- The website currently uses the green leaf identity (`img/large-logo.png`, `img/logo-dark.png`).
- **Owner Decision Required:** Preserve the green website logo and color accents until Daddy formally authorizes a rebrand to gold-and-navy.

### 15.4. Unverified Claims vs. Factual Scope
- **Pickup & Delivery:** Framed as available across Greater Accra, but operational turnaround and regional transit availability must be confirmed per booking rather than advertised as universal/unconditional.
- **Product Safety:** Avoid absolute marketing superlatives ("100% chemical-free", "zero risk to all living things"). Use factual descriptions: "eco-conscious, fabric-safe, plant-derived detergents" and "regulated formulations applied according to safety protocols".
- **Pricing:** No fixed rates or discounts published without explicit written confirmation from Daddy.
