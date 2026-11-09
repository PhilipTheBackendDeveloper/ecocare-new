# EcoCare Website — Release Blockers & Pre-Launch Checklist

**Document Version:** 1.1  
**Date:** 9 November 2026  
**Status:** In Progress – Technical blockers resolved; owner business authorizations pending

---

## 🚦 Gate Status Overview

| ID | Description | Severity | Owner | Status | Evidence / Notes |
|---|---|---|---|---|---|
| RB-01 | Form backend & spam protection | 🔴 HIGH | Dev | ✅ RESOLVED | Dual Node serverless (`/api`) + PHP fallback (`vendor/php/`); 10/10 automated tests pass |
| RB-02 | Testimonials consent & attribution | 🟡 MEDIUM | Client | ⏸️ PENDING / ATTRIBUTED | Archived reviews displayed with explicit pending disclosure under Ghana DPA (Act 843) |
| RB-03 | Legal docs ratification | 🟡 MEDIUM | Lawyer / Client | ⏸️ DRAFT NOTICED | Published with prominent legal draft disclaimer notice |
| RB-04 | Hero video background & photography | 🟢 LOW | Dev / Client | ✅ HERO VIDEO LIVE / ASSETS PENDING | Modern video background (`video-background.mp4` & `video-background1.mp4`) with sleek mobile glassmorphism UI live on `index.html`; service card photos pending field capture |
| RB-05 | Custom domain DNS & corporate email | 🟡 MEDIUM | Client | PENDING RENEWAL | Active inbox `ecocaregh1on1@gmail.com` deployed cleanly site-wide |
| RB-06 | Vercel clean URL deployment | 🟢 LOW | Dev | ✅ READY | `vercel.json` verified with 15 clean URL routes |
| RB-07 | Pest control safety & EPA compliance | 🔴 HIGH | Dev / Client | ✅ REMEDIATED / PENDING LICENSE | Mandatory 2–4 hr vacate advisory inserted; EPA license number pending client confirmation |

---

## Detailed Blockers Ledger

### RB-01 — Form Submission Backend & Spam Protection (RESOLVED ✅)

- **Problem:** Clenix demo lacked backend endpoints (`vendor/php/form-process.php`), and previous form scripts simulated submission without actual delivery or anti-spam filtering.
- **Resolution Implemented:**
  1. **Node.js / Vercel Serverless Functions:** Built `api/contact.js` and `api/quote.js` with field sanitization, RFC 5322 email validation, and Ghanaian phone number parsing.
  2. **PHP Endpoints:** Created `vendor/php/form-process.php` and `vendor/php/quote-process.php` for standard Apache / cPanel / Shared hosting environments.
  3. **Multi-Layer Spam Protection:**
     - Invisible honeypot field (`name="website_url"`) automatically catches and disarms automated bots without tip-off.
     - Rapid submission timer check flags and discards submissions occurring faster than 1 second from page render.
     - IP rate limiting restricts submissions to a maximum of 5 requests per minute per IP address.
  4. **Email Dispatching & Persistent Local Storage:**
     - Native email delivery integrated via Resend REST API / SMTP when API keys are supplied in `.env`.
     - Submissions are persistently stored to `data/submissions.jsonl` with ISO timestamps and client IP logging so that zero customer inquiries are lost even before client email setup.
  5. **Instant WhatsApp Dispatch Pre-fill:**
     - On successful submission, customers receive an interactive, accessible green alert with an instant one-click link to notify EcoCare dispatch directly via WhatsApp (`+233 24 901 4253`).
- **Test Evidence:**
  - Automated test runner: `node scripts/test_form_backend.js` -> **10/10 PASS** (Valid Ghana phone, email, honeypot spam trap, timing attack, invalid phone rejection, rate limiting 429, persistent file logging).

---

### RB-02 — Customer Testimonials (PENDING / ATTRIBUTED ⏸️)

- **Problem:** Historical reviews (Nana Esi, Raymond Okyere, Peter Darko) were published on the previous EcoCare website. Their republication requires formal re-verification under Ghana's Data Protection Act, 2012 (Act 843).
- **Resolution Implemented:**
  - The native Clenix testimonial carousel on `index.html` has been preserved to maintain the purchased theme's aesthetic.
  - A prominent, transparent disclosure banner has been inserted directly beneath the carousel:
    > *"Customer testimonials shown reflect historical feedback from EcoCare's previous website. Formal re-verification & consent renewal is logged as pending in accordance with Ghana's Data Protection Act, 2012 (Act 843)."*
  - Logged in `docs/ecocare/CONTENT_APPROVAL_TODO.md` (CA-09) pending owner outreach to named clients.

---

### RB-03 — Privacy Policy & Terms of Service (DRAFT NOTICED ⏸️)

- **Problem:** Full legal terms of service and privacy documentation require formal review by qualified legal counsel in Ghana.
- **Resolution Implemented:**
  - Both `privacy-policy.html` and `terms-condition.html` feature a permanent, visible warning banner (`.ecocare-draft-notice`):
    > *"Draft Notice: This document reflects standard operational data handling practices for EcoCare Cleaning Services Limited under Ghana's Data Protection Act, 2012 (Act 843). Formal legal ratification is pending."*
  - Footer navigation links explicitly label both pages as `(Draft)`.

---

### RB-04 — Hero Video Background & Service Photography (HERO VIDEO LIVE ✅ / ASSETS PENDING 🟢)

- **Problem:** Clenix template slider was static with stock images, and service cards use theme illustrations/photos.
- **Resolution Implemented:**
  1. **Modern Hero Video Engine:** Upgraded `index.html` hero to an ambient background video using `video-background.mp4` and `video-background1.mp4`.
  2. **Interactive Scene Switcher:** Added Clip 1 / Clip 2 selector with cinematic crossfade and auto-cycling.
  3. **Mobile Glassmorphism UI:** Features frosted glass card (`backdrop-filter: blur(18px)`), live pulsing status radar, tactile full-width CTA buttons, and high contrast over video motion.
  4. **Brand Assets Active:** EcoCare's authentic logo (`img/logo-dark.png`), icon (`img/mobile-logo.png`), favicon (`img/favicon.png`), and CEO portrait (`img/figure/aboutme.png`) are deployed site-wide.
  5. Replacement of internal service card images with custom field photography remains open for the client upon camera capture.

---

### RB-05 — Domain & Corporate Email DNS (PENDING RENEWAL 🟡)

- **Problem:** `info@ecocaregh.com` domain registration is expired or awaiting MX record configuration.
- **Resolution Implemented:**
  - The verified and monitored active inbox `ecocaregh1on1@gmail.com` is deployed across all 18 canonical pages.
  - Form endpoints default to `ecocaregh1on1@gmail.com`. Once the custom domain MX is verified, updating `NOTIFICATION_EMAIL` in `.env` redirects all notifications automatically without code changes.

---

### RB-06 — Vercel Deployment Configuration (READY ✅)

- **Status:** Complete and verified.
- `vercel.json` provides 15 clean URL rewrite routes (`/`, `/about`, `/services`, `/cleaning`, `/laundry`, `/pest-control`, `/carpet-cleaning`, `/upholstery-cleaning`, `/packages`, `/projects`, `/faq`, `/contact`, `/request-quote`, `/privacy-policy`, `/terms`).
- Verified via `python3 scripts/verify_responsive_and_routes.py` (105/105 checks pass).

---

### RB-07 — Pest Control Safety & EPA Regulatory Compliance (REMEDIATED ✅ / PENDING LICENSE)

- **Problem:** Historical website copy claimed pest control treatments were "harsh chemical-free" and "safe for pets and families without restrictions", which violates Ghana Environmental Protection Agency (EPA) safety protocols for pesticide application.
- **Resolution Implemented:**
  1. **Mandatory Safety Advisory Callout:** Inserted an eye-catching safety alert box on `pest-control.html` detailing:
     - Mandatory food, utensil, and pet dish airtight sealing.
     - Mandatory **2 to 4-hour** premises vacate and re-entry window for all occupants and domestic animals.
     - 30-minute post-return natural ventilation protocol.
     - On-site client review of Material Safety Data Sheets (MSDS) prior to chemical application.
  2. **Applicator Credentials Disclaimer:** Replaced claims of "licensed technicians" with "trained pest management applicators operating in accordance with Ghana Environmental Protection Agency (EPA) public health guidelines".
  3. **Client Action Required:** Client to confirm their specific Ghana EPA / MoFA commercial pest control applicator license registration number for public publication.

---

## Pre-Launch Verification Summary

| Test Suite | Script | Total Checks | Result |
|---|---|---|---|
| Automated QA & Anti-Regression | `python3 scripts/qa_check.py` | 116 | **116 PASS / 0 FAIL** |
| Form Backend & Spam Protection | `node scripts/test_form_backend.js` | 10 | **10 PASS / 0 FAIL** |
| Responsive & Vercel Route Audit | `python3 scripts/verify_responsive_and_routes.py` | 105 | **105 PASS / 0 FAIL** |
