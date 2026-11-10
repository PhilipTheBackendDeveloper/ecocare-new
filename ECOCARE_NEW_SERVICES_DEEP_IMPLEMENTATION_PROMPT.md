# EcoCare — Deep Implementation Prompt: Four Client-Confirmed Service Offerings

**Project:** EcoCare Cleaning Services Limited  
**Repository:** `PhilipTheBackendDeveloper/ecocare-new`  
**Website:** `https://ecocaregh.com/`  
**Current public state:** Seven-day Coming Soon on Netlify  
**Full-site state:** In development, not approved for public release  
**Directive:** Implement thoroughly while preserving the purchased Clenix ThemeForest visual identity.

---

## YOUR ROLE AND NON-NEGOTIABLE MISSION

Act as a senior product engineer, information architect, technical SEO specialist, accessibility engineer, content auditor, QA lead, and pragmatic Ghanaian cleaning-services website strategist.

**New information from the actual client (Daddy / EcoCare management):** EcoCare additionally provides:

1. **Sofa and Carpet Cleaning Solutions**
2. **Polytank Cleaning**
3. **Car Interior Cleaning**
4. **Professional Dusting Cleaning**

These **offering names are client-confirmed**. Specific procedures, equipment, chemicals, certifications, price schedules, service radius, warranties, outcomes, guarantees, photos, and booking turnaround are **not** confirmed by this message. Never infer that business claims already marked `VERIFIED_BY_CLIENT` in older AI-authored documents are genuinely independently approved without appropriate evidence.

Your mission is to audit and implement these offerings comprehensively and logically throughout the existing EcoCare website wherever users would need to find, understand, compare, inquire about, or book them. Do **not** merely add four homepage cards. Inspect the actual repo and build a coherent, maintainable service taxonomy that reflects the original offerings and new client instructions.

**Execute the implementation, not just the plan.** Make safe, reversible changes; test thoroughly; produce a precise evidence-based summary. If a material claim requires client clarification, use safe, plain, limited text and record the open question instead of inventing an answer.

## PHASE 0 — READ, SNAPSHOT, UNDERSTAND

1. Inspect `git status`, current branch, latest commits, and local uncommitted changes. Work in a new feature branch such as `feat/ecocare-four-confirmed-services`. Do not discard or overwrite user changes.
2. Read the complete relevant files, including (when present):
   - `knowledge.md`, `ECOCARE_MASTER_KNOWLEDGE_BASE.md`, `ECOCARE_CONTENT_DATA.json`, `ECOCARE_README.md`.
   - `template-inventory.md`, original Clenix template assets and screenshots/reference pages.
   - `index.html`, `service1.html`, `single-service1.html`, `single-service2.html`, `carpet-cleaning.html`, `upholstery-cleaning.html`, `pest-control.html`, `pricing-table.html`, `calculate-form.html`, `contact.html`, `faq.html`, `about1.html`, `project1.html`, related detail pages, the `404.html`, shared nav/footer markup, and any active page variants.
   - `css/ecocare.css`, `style.css`, shared JS and form logic including `js/ecocare.js`.
   - `data/seo-pages.json`, `scripts/enhance_seo_and_a11y.py`, `robots.txt`, `sitemap.xml`, `_redirects`, `vercel.json`, `netlify.toml`.
   - `docs/ecocare/CONTENT_APPROVAL_TODO.md`, `docs/ecocare/RELEASE_BLOCKERS.md`, all relevant `docs/seo/*` documents, and existing QA scripts.
3. Search every HTML, JS, JSON, Python, config, and documentation file for relevant synonyms and old references: `sofa`, `upholstery`, `carpet`, `rug`, `dusting`, `dust removal`, `car interior`, `vehicle interior`, `auto detailing`, `polytank`, `poly tank`, `water tank`, `water storage tank`, `tank washing`, `12 services`, `5 core services`, `serviceType`, `service`.
4. Create a **before/after service coverage matrix**: previous page/section, current mentions, target user intent, required change, link/slug, content status, photo status, approval status, tests. Identify all duplication, conflicting counts, unsupported statements, and orphan pages.
5. Preserve the current two-state release architecture: `netlify.toml` publishes `dist/coming-soon` and the public domain remains the Coming Soon page. Do not touch DNS or publish the full website. The existing Vercel preview is not an authorization to release content publicly.

## PHASE 1 — RECONCILE SERVICE TAXONOMY (NO DUPLICATION)

The current website already has **five familiar service families**: EcoClean, Eco-Laundry, EcoFumes, Carpet Cleaning, Upholstery Cleaning. Preserve them unless the actual content architecture provides an objectively better arrangement without losing continuity.

Map the four confirmations intelligently:

- **Sofa and Carpet Cleaning Solutions:** An umbrella/pairing of two **existing services**, not automatically two additional invented service categories. Preserve the existing **Carpet Cleaning** and **Upholstery / Sofa Cleaning** dedicated pages (`carpet-cleaning.html`, `upholstery-cleaning.html`). Make sofas discoverable explicitly and cross-link the two. Where a bundled service CTA helps, present “Sofa & Carpet Cleaning Solutions” as a combined enquiry option or short landing-section descriptor, not an unverified fixed-price bundle. Avoid misleading duplicate SEO pages targeting identical text.
- **Polytank Cleaning:** A newly confirmed **Water Storage Tank / Polytank Cleaning** offering. A dedicated page with a clean canonical slug such as `/polytank-cleaning` is recommended if it can contain genuinely useful, verified/neutral content. Otherwise include a clear card plus a viable dedicated service description rather than a blank or thin page. Categorize sensibly within EcoClean / Specialist Cleaning, with clear customer-facing terminology. Do not present it as pest-control fumigation.
- **Car Interior Cleaning:** A newly confirmed **Car Interior Cleaning** offering. Add a discoverable service entry; a dedicated route such as `/car-interior-cleaning` is recommended if there is enough unique useful content. The scope is **interior**, not exterior car wash, polishing, paintwork, mechanical care, or comprehensive auto detailing unless explicitly authorized. Ensure it cannot be confused with upholstery cleaning at the client's premises.
- **Professional Dusting Cleaning:** A confirmed specialized **Professional Dusting / Detailed Dust Removal** service. Include it prominently in EcoClean's existing residential/commercial scope. Decide whether its distinct search intent and available evidence justify a dedicated `/professional-dusting` page. If a dedicated page would be thin or duplicative, prefer a substantial subsection on `/cleaning`, a clear directory card/anchor, and a dedicated quotation option. The user must still be able to locate and request this service directly.

**Do not hardcode “12 services” or any new total until you have determined the true unique offering count after de-duplication.** If there are 12 old cards, review whether they should become 15, 16, or another accurate count based on the actual final data model. Count product offerings, not repeated marketing synonyms.

Document the final chosen taxonomy, route policy, parent/child relationships, distinction between service families and individually bookable offerings, and how each new item maps to existing cards and detail pages.

## PHASE 2 — IMPLEMENT EVERY RELEVANT SITE SURFACE

Audit and update each applicable surface, not only the homepage:

1. **Main homepage (`index.html`):** Existing service gallery/cards, short service descriptions, relevant “Our Services” sections, internal links, service CTA, relevant existing content modules, and possible combined sofa/carpet highlight. Add new offering cards only where necessary and consistent with the native Clenix grid; preserve video hero, overall original look, and content density. Do not clutter the hero.
2. **Full Services directory (`service1.html`):** Include all uniquely advertised services and ensure the four confirmations are easily found by name. Show an appropriate brief customer benefit, an available appropriate image or honest visual fallback, and a working “Learn More” or “Request a Quote” link. Keep responsive grid balanced for 1/2/3/4 column layouts and filters functional, if filters are present. Remove stale “12” counts if inaccurate.
3. **Existing detail pages:** Extend Carpet Cleaning and Upholstery Cleaning pages with client-confirmed sofa/carpet wording and accurate cross-links. Extend EcoClean residential/commercial modules to include professional dusting where appropriate. Do not rewrite or remove existing verified content just to insert new text.
4. **New service detail page(s):** For Polytank and Car Interior (and Professional Dusting only if justified), create pages using the closest **existing Clenix service detail template** and its markup/classes. Include unique H1, concise introduction, services covered (limited to grounded facts), who it is for, what customers can provide for a quote, neutral explanatory workflow when verified, relevant FAQ, related services, a clear CTA, breadcrumb navigation, phone/WhatsApp contact fallback, and appropriate images/assets. No empty sections, fake reviews, fake cost cards, decorative duplication, or dead buttons.
5. **Navigation:** Main desktop nav, sticky menu, mobile MeanMenu, sidebars, “Our Services” nav lists, breadcrumbs, and footer service links. Preserve reasonable nav density; add nested links or service-directory navigation rather than stuffing every service into top-level nav.
6. **Packages/Pricing (`pricing-table.html`):** Clearly convey availability of new offerings and quote-by-scope. Preserve existing package structure. Do not add fabricated prices, fixed tank size brackets, vehicle tiers, discounts, or guaranteed bundles. Ensure quote CTAs route to the relevant form service option.
7. **Quotation and contact (`calculate-form.html`, `contact.html`, `js/ecocare.js`):** Add intuitive selectable options for all new distinct services. Preserve existing form fields and functional/validation rules; if a selected service benefits from conditional inputs, add minimal accessible fields with optionality and clear semantics (e.g., approximate tank capacity if known, whether tank is elevated, general vehicle type if relevant, rooms/areas for dusting, number of sofas/rugs) **only when necessary**. Avoid assuming exact required inputs. Do not break the form backend, Netlify Forms work, or honest submission status. Never send these enquiries to an unavailable Vercel-only endpoint in a Netlify full-site build. Preserve privacy and avoid unnecessarily sensitive details.
8. **FAQ (`faq.html`):** Add helpful concise questions only where answers can be stated reliably; for unknown methods, price, frequency, chemical use, access, turnaround or specific materials, answer that an assessment or confirmation is required. Use genuine visible FAQ content rather than only JSON-LD.
9. **About, Projects, Gallery, Blog-like cards, and other marketing modules:** Update service range references where they are relevant, but do not invent case studies, before/after images, project names, corporate endorsements, or articles. A gallery item requires genuine approved photos and work evidence.
10. **Shared footer/header/copyright, homepage snippets, link labels, alt text:** Ensure consistent naming, spelling, contact info, no broken internal routes, and no leftover ThemeForest placeholders related to these categories.
11. **Coming Soon:** The current live Coming Soon site must be **visually and functionally unchanged** unless explicitly requested later. No need to publish new service pages during State A.

## PHASE 3 — ACCURATE CUSTOMER-FACING CONTENT, NOT HALLUCINATIONS

Write polished, warm, premium, natural Ghanaian English that helps people understand the services without sounding like generic AI marketing. Use clear service outcomes (e.g., dust removal from reachable interior surfaces) without guarantees of disease prevention or complete sterilization. Ensure all text fits the original card heights and mobile constraints. Avoid walls of text.

**Approved high-level service language that may be adapted:**
- “Sofa & Carpet Cleaning Solutions — Ask EcoCare about fabric and carpet cleaning for homes and workplaces. The appropriate treatment depends on material and condition.”
- “Polytank / Water Storage Tank Cleaning — Arrange an assessment for cleaning accessible water storage tanks. Method and scheduling depend on tank condition, access, water use and safety requirements.”
- “Car Interior Cleaning — Enquire about cleaning seating and interior surfaces of your vehicle. Service scope and suitability are confirmed before booking.”
- “Professional Dusting Cleaning — Request detailed dust removal for homes, offices and other appropriate interior spaces, based on surfaces and access.”

These are provisional neutral copy examples, not final official slogans. Refine once matching existing brand tone and confirmed scope.

**Mandatory factual constraints:**
- Do not promise tank drinking-water safety, sterilization, microbiological purity, chlorination, potability, or a “100% bacteria-free” result without verified process and appropriate independent evidence.
- Do not invent tank-entry techniques, confined-space access, specific bleach/detergent concentrations, chemical brands, disinfection dwell times, service durations, annual cleaning frequency, or worker certifications. Where safety is relevant, state work must be assessed and carried out using appropriate procedures and qualified personnel.
- Do not add “engine bay cleaning”, “exterior wash”, “paint polishing”, “ceramic coating”, “full detailing”, or leather restoration to **Car Interior Cleaning** unless the client confirms those subservices.
- Do not promise removal of all allergens, mold, pathogens, bacteria or microscopic particles by professional dusting without evidence. Avoid “hospital-grade” without real support.
- Do not guarantee removal of every carpet stain, prevention of damage to upholstery, or universal compatibility with every material.
- No unsupported prices, bookings guaranteed within X hours, “certified by” claims, warranty, staff counts, customer counts, discounts, before/after results, ratings, or client names.
- Existing “VERIFIED_BY_CLIENT” annotations in AI-authored metadata should be cross-checked against actual approval. This message verifies only that the four offerings are provided, not their detailed operating procedures.
- Keep any open decisions in `docs/ecocare/CONTENT_APPROVAL_TODO.md`, using clear IDs and minimal actionable questions.

For water-tank safety background, consult credible relevant guidance such as Ghana's Water Resources Commission and appropriate water-storage/tank-cleaning standards. Research may inform safe wording but cannot establish which particular procedures EcoCare uses.

## PHASE 4 — IMAGES AND CLENIX VISUAL CONSISTENCY

- Inventory available assets under `img/`, matching official photographs and licensed ThemeForest visuals. Determine which photos are genuinely EcoCare, licensed template stock, or unapproved.
- Avoid presenting a generic photo as a factual EcoCare job. If no suitable authorized image exists, use an honest, visually cohesive branded illustration/neutral fallback or preserve an appropriate licensed template visual without misrepresenting it.
- Optimize correct formats, dimensions, alt text, responsive rendering, loading priority, cropping, and file paths.
- Keep the EcoCare logo and favicon unchanged. Preserve Clenix styles, card components, typography, color system, animations, mobile menus, and visual hierarchy. No Next.js/React migration or unrelated redesign.

## PHASE 5 — SEO, ROUTES, CANONICALS, AND DISCOVERABILITY

Implement SEO for pages that are genuinely useful and publishable, not mechanically generated keyword doorways.

- Inspect `data/seo-pages.json`, manifest-driven `scripts/enhance_seo_and_a11y.py`, and existing idempotent generation tests. Update the **single source of truth**, not disconnected repeated hardcoded tags.
- Give any new page unique title, description, H1, canonical URL, meaningful body text, OG/Twitter tags, appropriate `Service` JSON-LD linked to the existing EcoCare provider `@id`, breadcrumbs, internal links, and accurate image references. Include service locations only where verified.
- Suggested human-readable topics: “Polytank / Water Tank Cleaning in Accra”, “Car Interior Cleaning in Accra”, “Professional Dusting Services in Accra”, “Sofa & Carpet Cleaning in Accra”. Choose actual slugs based on content uniqueness and avoid competing near-duplicates.
- Keep existing `/carpet-cleaning` and `/upholstery-cleaning` authority; canonicalize rather than cloning duplicate pages for “Sofa and Carpet”.
- Update `sitemap.xml` **for State B only**, with all genuinely published canonical routes and accurate `lastmod` values. Do not place new unfinished URLs into `dist/coming-soon/` or the currently live State A sitemap.
- Update root `_redirects`, `vercel.json`, and any other full-site routing for clean URLs, safe 301s of extension URLs where needed, and correct non-200 handling. Test Netlify rule order and direct deep links. Do not create infinite redirects or broaden State A redirects.
- Update structured-data service offerings, site nav, `docs/seo/02_SEO_COPY_MATRIX.md`, URL inventory and SEO QA. Never misrepresent missing actual service photos or invent reviews in schema.
- Do not over-optimize keyword variants, claim SEO rank guarantees, or create multiple thin near-identical “Accra / Achimota / East Legon” doorway pages.

## PHASE 6 — TESTING AND PROOF

**Automated QA:**
1. Validate all links and local assets on newly created/modified HTML pages.
2. Verify each advertised service has a reachable booking/contact path, and all new selectable service values are correctly serialized and accepted in the intended production backend.
3. Verify service counts and categories remain consistent across homepage, directory, FAQ, structured data, and documentation.
4. Validate all new SEO canonical routes, sitemap rules, OG values, JSON-LD syntax/semantics, internal link integrity, redirect behavior and metadata idempotency.
5. Re-run relevant existing suites: `scripts/qa_check.py`, `scripts/verify_responsive_and_routes.py`, `scripts/test_seo_comprehensive.py`, `scripts/test_coming_soon.py`, `scripts/test_form_backend.js`; update assertions to reflect genuine new scope without weakening existing checks.
6. Assert the isolated Coming Soon build remains unchanged or byte-equivalent unless there is an expressly approved reason to alter it. `netlify.toml` must still publish `dist/coming-soon`, and the public domain must not expose the new full-site routes.

**Real visual/browser QA:**
- Test homepage, directory, affected existing details, each new detail, packages, FAQ, quote/contact forms, header/footer/nav, and relevant deep links on widths 360, 375, 390, 430, 768, 1024, 1440 and 1920.
- Check layout overflow, non-truncated text, card heights, dark/light contrast, focus states, mobile menu interactions, image quality, keyboard access, reduced-motion handling and Core Web Vitals regressions.
- Test real form submission only in a safe staging environment with configured backend; differentiate mock tests from confirmed persisted submissions and email notifications.
- Compare representative screenshots of changed pages with original Clenix design, ensuring changes are content-driven rather than a new visual identity.

## PHASE 7 — DOCUMENTATION, SAFETY, AND HANDOFF

Produce/update:
1. `docs/ecocare/NEW_SERVICE_COVERAGE_MATRIX.md` showing each of the four offerings and exactly where it appears, with specific files/routes.
2. `docs/ecocare/CONTENT_APPROVAL_TODO.md` entries for unknown tank-cleaning procedure and safety, vehicle interior scope, dusting surfaces/equipment, photography, any package relationship, prices and coverage.
3. `docs/ecocare/RELEASE_BLOCKERS.md` to identify which implementation issues were resolved and which real-world conditions are still pending (email delivery, legal approvals, source verification, etc.).
4. Relevant SEO manifests, sitemap/redirect documentation, and test reports.
5. A crisp final engineering report of code changes, decisions, duplicate avoidance, newly added vs existing services, verified tests (with commands and outcomes), screenshots if available, and remaining client approvals.

**Execution conditions:**
- Do not change the production Netlify publish directory, domain/DNS, public indexing state, or existing Coming Soon countdown.
- Do not push directly to `main` unless explicitly instructed. Make a reviewed feature branch and commit only relevant changes.
- No blind destructive refactors, new framework, paid integration, external API credentials, or unsupported service claims.
- If there are contradictory old data sources, use this newly confirmed four-service instruction for the **existence** of services but escalate specific conflicting details rather than fabricate them.
- Do not stop after planning. Implement as far as possible safely and report real external blockers clearly.

## REQUIRED FINAL ACCEPTANCE CHECKLIST

- [ ] Sofa and Carpet Cleaning Solutions is properly represented without duplicate carpet/upholstery pages.
- [ ] Polytank Cleaning is discoverable and has useful service information and a working enquiry path.
- [ ] Car Interior Cleaning is discoverable, scoped to interior work, and has a working enquiry path.
- [ ] Professional Dusting Cleaning is clearly represented in EcoClean / service discovery and can be requested directly.
- [ ] All applicable home/service/detail/nav/footer/package/FAQ/contact/quote surfaces are consistent.
- [ ] Existing EcoCare services remain present and accurate; unique offering counts are reconciled.
- [ ] Metadata, canonical routes, full-site sitemap, JSON-LD, link graph, and redirects are coherent.
- [ ] Clenix original visual style, logo, favicon, hero video and responsive interactions are preserved.
- [ ] Unverified promises, prices, water-treatment methods, safety claims and stock-photo misrepresentation are excluded or flagged.
- [ ] Netlify Coming Soon remains public, isolated, and unchanged while full-site work is completed.
- [ ] All runnable tests are executed with documented evidence; no false “100% complete” claim where real-world checks/approvals are missing.

**Start by auditing the repository and generating the coverage matrix, then carry out the actual implementation.**
