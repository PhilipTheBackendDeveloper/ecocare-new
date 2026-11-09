# EcoCare Cleaning Services Limited — Baseline & Fact Approval Inventory
**Document:** `docs/seo/00_BASELINE_AND_FACT_APPROVAL.md`  
**Date:** November 9, 2026  
**Repository Branch:** `seo/master-optimization`  
**Base Commit:** `2fdfc0b` (HEAD on `main`: `style(coming-soon): soften background overlay for clear photo visibility while preserving high text contrast`)  
**Current Commit:** `c3b9f56` (`docs: add master SEO and launch optimization prompt specification`)  
**Target Domain:** `https://ecocaregh.com/` (Namecheap DNS -> Netlify)  
**Preview Deployment:** Vercel project `ecocare-new`  

---

## 1. Safety, Snapshot & Git Baseline

### Git Environment Snapshot
- **Branch:** `seo/master-optimization` (isolated feature branch for all SEO, metadata, schema, and QA enhancements).
- **Origin Remote:** `https://github.com/PhilipTheBackendDeveloper/ecocare-new.git`
- **Working Tree:** Clean, zero uncommitted working tree changes prior to this execution.
- **Production Guardrails:**
  - Zero forced resets, zero history deletion.
  - Zero production DNS changes executed without explicit user instruction.
  - Zero unapproved credentials/API keys exposed.
  - Coming Soon state (`dist/coming-soon/`) isolated from full website code.

---

## 2. Inventory of HTML Pages & Code Generators

### A. Canonical Pages (18 Public / Semi-Public Routes)
| Page Filename | Clean Route | Page Purpose & Content Identity | Source of Truth |
|---|---|---|---|
| `coming-soon.html` | `/` (State A) | Standalone 7-Day Launch Countdown, Preloader & Dispatch CTAs | Authored + `build_coming_soon.py` |
| `index.html` | `/` (State B) | EcoCare Primary Brand, Video Hero, 5 Service Families, Testimonials (Pending) | Authored HTML |
| `about1.html` | `/about` | Corporate Heritage (Est. 2014), Leadership (CEO Eric Nana Acquah), Mission | Authored HTML |
| `service1.html` | `/services` | 12 Service Listings across 5 Core Families | Authored HTML |
| `single-service1.html` | `/cleaning` | EcoClean Residential Housekeeping & Commercial Janitorial | Authored HTML |
| `single-service2.html` | `/laundry` | Eco-Laundry Doorstep Garment Care & Dry Cleaning | Authored HTML |
| `pest-control.html` | `/pest-control` | EcoFumes Fumigation & Pest Control (EPA-aligned safety protocols) | Authored HTML |
| `carpet-cleaning.html` | `/carpet-cleaning` | Five-Stage Hot Water Extraction & Commercial Carpet Restoration | Authored HTML |
| `upholstery-cleaning.html` | `/upholstery-cleaning` | Fabric Sofa, Leather Conditioning & Mattress Sanitization | Authored HTML |
| `pricing-table.html` | `/packages` | Scope-Based Packages (Standard, Deep Move-In, Corporate Contract) | Authored HTML |
| `calculate-form.html` | `/request-quote` | Interactive Estimate Calculator & Service Scoping Form | Authored HTML |
| `faq.html` | `/faq` | Operational Inquiries, Pricing Scoping, Greater Accra Coverage | Authored HTML |
| `contact.html` | `/contact` | Achimota Mile 7 Dispatch Office, Telephones, Gmail, Inquiry Form | Authored HTML |
| `project1.html` | `/projects` | Verified Portfolio Showcase (Commercial, Residential, Restorations) | Authored HTML |
| `single-project1.html` | `/projects/commercial-case-study` | Multi-Story Commercial Workspace Deep Cleaning Case Study | Authored HTML |
| `privacy-policy.html` | `/privacy-policy` | Data Handling Notice under Ghana Data Protection Act (Act 843) | Authored HTML |
| `terms-condition.html` | `/terms` | Operational Service Agreement & Scoping Terms | Authored HTML |
| `404.html` | `/404` | Branded HTTP 404 Error Recovery Page | Authored HTML |

### B. Deprecated Demo Pages (13 Non-Public Template Pages)
| Page Filename | Deprecation Status | Target Disposition |
|---|---|---|
| `index2.html`, `index3.html`, `index4.html` | Demo Homepages | Disallowed/Noindex; Excluded from sitemap; 301 redirect to `/` on full launch |
| `about2.html` | Demo About page | Disallowed/Noindex; Excluded from sitemap; 301 redirect to `/about` |
| `service2.html` | Demo Services grid | Disallowed/Noindex; Excluded from sitemap; 301 redirect to `/services` |
| `blog1.html`, `blog2.html`, `single-blog1.html` | Demo Blog templates | Disallowed/Noindex; Excluded from sitemap; return 404 or redirect to `/` |
| `shop.html`, `single-product.html` | Demo E-Commerce | Disallowed/Noindex; Excluded from sitemap; return 404 or redirect to `/` |
| `team1.html`, `team2.html`, `single-team.html` | Demo Team pages | Disallowed/Noindex; Excluded from sitemap; 301 redirect to `/about` |

### C. Code Generators & Script Engine
1. `scripts/build_coming_soon.py`: Generates the isolated `dist/coming-soon/` artifact deployed by Netlify.
2. `scripts/enhance_seo_and_a11y.py`: The existing SEO and metadata enhancement utility. **Refactored to be driven by `data/seo-pages.json` as the immutable single source of truth.**
3. `scripts/qa_check.py`: Quality assurance check enforcing 116 integrity rules.
4. `scripts/test_coming_soon.py`: Validates 12 specific Coming Soon criteria (time-invariance, security, assets).
5. `scripts/verify_responsive_and_routes.py`: Validates 105 mobile and Vercel route configurations.
6. `scripts/test_form_backend.js`: Verifies 10 security, honeypot, rate limiting, and sanitization rules.

---

## 3. Categorization of Business Assertions & Truth Ledger

Every business claim across the website has been audited against `knowledge.md`, `ECOCARE_MASTER_KNOWLEDGE_BASE.md`, and `docs/ecocare/RELEASE_BLOCKERS.md`:

| Category | Item Description | Current Value in Code | Verification Status | Operational Decision / Policy |
|---|---|---|---|---|
| **Identity** | Company Legal Name | EcoCare Cleaning Services Limited | `VERIFIED_BY_CLIENT` | Official registered entity under Ghanaian Companies Code. |
| **Identity** | Founding Date | September 19, 2014 (Commenced Sept 30, 2014) | `VERIFIED_BY_CLIENT` | Used consistently across JSON-LD, About page, and metadata. |
| **Identity** | Leadership | Eric Nana Acquah, CEO | `VERIFIED_BY_CLIENT` | Verified company executive; portrait at `img/figure/aboutme.png`. |
| **Contacts** | Physical Office | Achimota Mile 7, Accra, Ghana | `VERIFIED_BY_CLIENT` | Canonical operating address across footer, contact, and schema. |
| **Contacts** | Primary Phone | `+233 24 901 4253` | `VERIFIED_BY_CLIENT` | Verified active line for calls and WhatsApp dispatch. |
| **Contacts** | Secondary Phone | `+233 24 380 7100` | `VERIFIED_BY_CLIENT` | Verified active corporate line. |
| **Contacts** | Customer Inbox | `ecocaregh1on1@gmail.com` | `VERIFIED_BY_CLIENT` | Active monitored inbox; `info@ecocaregh.com` held until MX verified. |
| **Social** | Facebook | `facebook.com/profile.php?id=100006412849415` | `VERIFIED_BY_CLIENT` | Verified authentic business Facebook profile. |
| **Social** | TikTok | `tiktok.com/@ecocarecompanylimited` | `VERIFIED_BY_CLIENT` | Verified company TikTok profile (vector SVG deployed). |
| **Social** | YouTube | `youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA` | `VERIFIED_BY_CLIENT` | Verified company YouTube channel. |
| **Service Claims** | 5 Service Families | EcoClean, Eco-Laundry, EcoFumes, Carpet, Upholstery | `VERIFIED_BY_CLIENT` | Grounded core offering matching official registration. |
| **Operations** | Service Geography | Greater Accra Region, Ghana | `VERIFIED_BY_CLIENT` | Verified territory (Achimota, East Legon, Cantonments, Osu, etc.). |
| **Operations** | Operating Hours | Mon–Sat: 07:00 – 18:00; Sun: Closed / By Appt | `VERIFIED_BY_CLIENT` | Standard realistic operational desk hours. |
| **Metrics** | "2,583+ Clients, 80+ Staff, 2,129+ Projects" | Demo placeholder counters | `UNVERIFIED/REPLACED` | Replaced with qualitative verified operational features (CA-10). |
| **Availability** | "24/7 Support" banner | Unsubstantiated around-the-clock claim | `UNVERIFIED/REMOVED` | Replaced with real office hours + emergency appointment note (CA-05). |
| **Safety** | "Mandatory 2-4 hour vacate" (Pest Control) | Universal blanket re-entry timing | `UNVERIFIED/REMEDIATED` | Replaced with strict requirement to follow product label and certified technician instructions (RB-07). |
| **Reviews** | Customer Testimonials (Nana Esi, etc.) | Historical feedback from old site | `HOLD / PENDING RE-VERIFICATION` | Rendered with visible Ghana DPA Act 843 re-consent notice; schema `aggregateRating` omitted. |
| **Legal** | Privacy Policy & Terms of Service | Operational drafts | `HOLD / DRAFT NOTICED` | Displayed with prominent draft disclaimers pending client legal counsel sign-off. |
| **Pricing** | Fixed Cedi pricing figures | Vague / ungrounded flat rates | `PROPOSED_COPY` | Shifted to transparent scoping in GHS; custom quote calculator provided. |

---

## 4. Current Deployment & Preview Status

1. **Production Domain (`https://ecocaregh.com/`):**
   - Registrar: Namecheap.
   - Hosted on Netlify under `PhilipTheBackendDeveloper/ecocare-new`.
   - `netlify.toml` targets `dist/coming-soon/` (isolated 7-day Coming Soon build).
2. **Preview Environment:**
   - Hosted on Vercel at `ecocare-new.vercel.app`.
   - `vercel.json` maps 15 clean URLs for internal client review.
   - Guarded with `X-Robots-Tag: noindex, nofollow` on non-production hosts to prevent index leakage.

---

## 5. Phase 0 Audit Conclusion & Next Actions

The baseline repository state is cleanly recorded, all business assertions have been sorted into strict truth categories, and the single source of truth architecture (`data/seo-pages.json`) is ready to be implemented for Phase 1 through Phase 11.

