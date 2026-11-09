# EcoCare Website — Release Blockers & Pre-Launch Checklist

**Document Version:** 1.2  
**Date:** 9 November 2026  
**Status:** In Progress – Technical infrastructure, coming-soon isolation, and truthfulness guardrails completed; client email provider credentials and authorizations pending

---

## 🚦 Gate Status Overview

| ID | Description | Severity | Owner | Status | Evidence / Notes |
|---|---|---|---|---|---|
| RB-01 | Form backend & real email delivery | 🔴 HIGH | Dev / Client | 🔴 OPEN (PENDING CREDENTIALS) | Serverless (`/api`) and PHP handlers tested for sanitization, honeypot, timing attacks, rate limiting, and local storage (10/10 PASS). Real inbox delivery pending client provision of `RESEND_API_KEY` or SMTP credentials. |
| RB-02 | Testimonials consent & attribution | 🟡 MEDIUM | Client | ⏸️ PENDING / ATTRIBUTED | Archived reviews displayed with explicit pending disclosure under Ghana DPA (Act 843). |
| RB-03 | Legal docs ratification | 🟡 MEDIUM | Lawyer / Client | ⏸️ DRAFT NOTICED | Published with prominent legal draft disclaimer notice on privacy and terms pages. |
| RB-04 | Hero video background & photography | 🟢 LOW | Dev / Client | ✅ HERO VIDEO LIVE / ASSETS PENDING | Ambient background video (`video-background.mp4` & `video-background1.mp4`) active behind 100% native Clenix template UI on `index.html`; service card photos pending field capture. |
| RB-05 | Custom domain DNS & corporate email | 🟡 MEDIUM | Client | ⏸️ PENDING RENEWAL | Active monitored inbox `ecocaregh1on1@gmail.com` deployed cleanly site-wide. |
| RB-06 | Vercel clean URL deployment | 🟢 LOW | Dev | ✅ READY | `vercel.json` verified with 15 clean URL routes (105/105 checks pass). |
| RB-07 | Pest control safety & EPA compliance | 🔴 HIGH | Dev / Client | 🟡 REMEDIATED / PENDING LICENSE | Fixed 2–4 hr intervals completely removed; copy strictly requires following product labels and on-site qualified operator instructions. EPA license number pending client confirmation. |
| RB-08 | Standalone Coming Soon publication | 🟢 LOW | Dev | ✅ READY | Self-contained static site created at `deploy/coming-soon/` with official root branding, live countdown, direct WhatsApp / phone / email channels, and zero unfinished links. |

---

## Detailed Blockers Ledger

### RB-01 — Form Submission Backend & Real Email Delivery (OPEN — PENDING CREDENTIALS 🔴)

- **Problem:** Clenix demo lacked backend endpoints (`vendor/php/form-process.php`), and previous form scripts simulated submission without actual delivery or anti-spam filtering.
- **Resolution Implemented:**
  1. **Node.js / Vercel Serverless Functions:** Built `api/contact.js` and `api/quote.js` with field sanitization, RFC 5322 email validation, and Ghanaian phone number parsing.
  2. **PHP Endpoints:** Created `vendor/php/form-process.php` and `vendor/php/quote-process.php` for standard Apache / cPanel / Shared hosting environments.
  3. **Multi-Layer Spam Protection:**
     - Invisible honeypot field (`name="website_url"`) automatically catches and disarms automated bots without tip-off.
     - Rapid submission timer check flags and discards submissions occurring faster than 1 second from page render.
     - IP rate limiting restricts submissions to a maximum of 5 requests per minute per IP address.
  4. **PII Masking & Persistent Local Storage:**
     - Submissions are persistently stored to `data/submissions.jsonl` with ISO timestamps and client IP logging so that zero customer inquiries are lost even before client email setup.
     - Phone numbers and email addresses are masked in server console logs (e.g. `233****53`, `kw***@example.com`) to prevent accidental PII leakage under Ghana's Data Protection Act, 2012 (Act 843).
  5. **Instant WhatsApp Dispatch Pre-fill:**
     - On submission, customers receive an interactive, accessible green alert with an instant one-click link to notify EcoCare dispatch directly via WhatsApp (`+233 24 901 4253`).
- **Open Status Justification:**
  - In accordance with non-negotiable truthfulness rules, passing automated test scripts (`test_form_backend.js`) does NOT constitute proof of live email delivery. Real end-to-end delivery requires `RESEND_API_KEY` or SMTP credentials configured in the live deployment environment (`.env`). Until a test email is received in the client's inbox, RB-01 remains **OPEN**.

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
  1. **Background Video Integration:** Integrated an ambient background video using `video-background.mp4` and `video-background1.mp4` that auto-cycles smoothly and silently in the background with strict mobile autoplay policy compliance.
  2. **Streamlined Minimalist Hero UI:** Retained the authentic headline (*"Protect the Environment, Live Better, Prolong Life"* with emerald accent), punchy single-sentence value proposition, and dual CTA buttons. Removed wordy clutter, floating controls, and extra badge/chip strips for an ultra-sleek, distraction-free aesthetic.
  3. **High Contrast Directional Overlay:** Styled an elegant directional gradient overlay (`.hero-video-bg-overlay`) ensuring 100% text legibility while keeping the ambient background video vivid and clearly visible.
  4. **Original Clenix Bottom Transition:** Retained the native Clenix `.section-bubble` curved transition into the About Us section.
  5. **Mobile Responsiveness:** Clean fluid typography down to `<360px`, balanced vertical spacing, and modern touch-friendly buttons.
  6. **Brand Assets Active:** EcoCare's authentic logo (`img/logo-dark.png`), icon (`img/mobile-logo.png`), favicon (`img/favicon.png`), and CEO portrait (`img/figure/aboutme.png`) are deployed site-wide.
  7. Replacement of internal service card images with custom field photography remains open for the client upon camera capture.

---

### RB-05 — Domain & Corporate Email DNS (PENDING RENEWAL ⏸️)

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

### RB-07 — Pest Control Safety & EPA Regulatory Compliance (REMEDIATED 🟡 / PENDING LICENSE)

- **Problem:** Historical website copy claimed pest control treatments were "harsh chemical-free" and "safe for pets and families without restrictions", and previous remediation introduced an unverified "2 to 4-hour" fixed vacate time.
- **Resolution Implemented:**
  1. **No Invented Fixed Intervals:** Excised all invented "2 to 4-hour" fixed intervals across `pest-control.html`, `index.html`, `faq.html`, and `terms-condition.html`.
  2. **Label & Qualified Operator Instructions:** Replaced with explicit instructions requiring clients to adhere strictly to product label directions and site-specific guidance provided on-site by qualified operators.
  3. **Applicator Credentials Disclaimer:** Replaced claims of "licensed technicians" with "trained pest management applicators operating in accordance with Ghana Environmental Protection Agency (EPA) public health guidelines".
  4. **Client Action Required:** Client to confirm their specific Ghana EPA / MoFA commercial pest control applicator license registration number for public publication.

---

### RB-08 — Standalone Coming Soon Publication (READY ✅)

- **Status:** Complete and verified.
- Created `deploy/coming-soon/` as an isolated, static-only deployment package containing:
  - `index.html` with official EcoCare logo and favicon from root.
  - Live animated countdown timer.
  - Direct verified communication channels (WhatsApp quick connect, phone `+233 24 901 4253`, email `ecocaregh1on1@gmail.com`, and Achimota Mile 7 office address).
  - No broken links or links pointing to unfinished pages.
  - Dedicated `netlify.toml` for 1-command deployment (`cd deploy/coming-soon && netlify deploy`).

---

## Pre-Launch Verification Summary

| Test Suite | Script | Total Checks | Result |
|---|---|---|---|
| Automated QA & Anti-Regression | `python3 scripts/qa_check.py` | 116 | **116 PASS / 0 FAIL** |
| Form Backend & Spam Protection | `node scripts/test_form_backend.js` | 10 | **10 PASS / 0 FAIL** |
| Responsive & Vercel Route Audit | `python3 scripts/verify_responsive_and_routes.py` | 105 | **105 PASS / 0 FAIL** |
