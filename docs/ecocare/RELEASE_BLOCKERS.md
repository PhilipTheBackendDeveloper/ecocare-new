# EcoCare Website — Release Blockers & Pre-Launch Checklist

**Document Version:** 1.3  
**Date:** 9 November 2026  
**Status:** In Progress – Technical infrastructure, Netlify Forms migration, coming-soon isolation, and truthfulness guardrails completed; live Netlify Form notification inbox delivery and client content approvals pending

---

## 🚦 Gate Status Overview

| ID | Description | Severity | Owner | Status | Evidence / Notes |
|---|---|---|---|---|---|
| RB-01 | Form backend & real email delivery | 🔴 HIGH | Dev / Client | 🟡 MIGRATED TO NETLIFY FORMS / PENDING INBOX TEST | Native Netlify Forms with `bot-field` honeypot, timing defenses, and URL-encoded submission implemented across all canonical pages. 14/14 automated tests pass. Real inbox delivery requires configuring Netlify Form notifications to `ecocaregh1on1@gmail.com` in Netlify dashboard and sending a live test submission. |
| RB-02 | Testimonials consent & attribution | 🟡 MEDIUM | Client | ⏸️ PENDING / ATTRIBUTED | Archived reviews displayed with explicit pending disclosure under Ghana DPA (Act 843). |
| RB-03 | Legal docs ratification | 🟡 MEDIUM | Lawyer / Client | ⏸️ DRAFT NOTICED | Published with prominent legal draft disclaimer notice on privacy and terms pages. |
| RB-04 | Hero video background & photography | 🟢 LOW | Dev / Client | ✅ HERO VIDEO LIVE / ASSETS PENDING | Ambient background video (`video-background.mp4` & `video-background1.mp4`) active behind 100% native Clenix template UI on `index.html`; service card photos pending field capture. |
| RB-05 | Custom domain DNS & corporate email | 🟢 LOW | Dev / Client | ✅ DOMAIN & HTTPS LIVE ON NETLIFY | `ecocaregh.com` is registered, active, and securely serving with HTTPS and apex redirects on Netlify. Corporate `info@ecocaregh.com` remains pending mailbox setup; active monitored inbox `ecocaregh1on1@gmail.com` deployed site-wide. |
| RB-06 | Vercel clean URL deployment | 🟢 LOW | Dev | ✅ READY | `vercel.json` verified with 15 clean URL routes and `X-Robots-Tag: noindex, nofollow` (105/105 checks pass). |
| RB-07 | Pest control safety & EPA compliance | 🔴 HIGH | Dev / Client | 🟡 REMEDIATED / PENDING LICENSE | Fixed 2–4 hr intervals completely removed; copy strictly requires following product labels and on-site qualified operator instructions. EPA license number pending client confirmation. |
| RB-08 | Standalone Coming Soon publication | 🟢 LOW | Dev | ✅ LIVE ON NETLIFY | Standalone 7-day countdown site is live on Netlify at `https://ecocaregh.com`. Full website remains preserved and staged in `dist/staging/`. |

---

## Detailed Blockers Ledger

### RB-01 — Form Submission Backend & Real Email Delivery (MIGRATED TO NETLIFY FORMS / PENDING INBOX TEST 🟡)

- **Problem:** Clenix demo lacked backend endpoints (`vendor/php/form-process.php`), and previous serverless `/api` implementations relied on ephemeral local filesystem storage (`data/submissions.jsonl`) which is wiped on serverless container restarts and non-functional on Netlify static hosting.
- **Resolution Implemented:**
  1. **Native Netlify Forms Infrastructure:** Migrated all forms across `contact.html`, `calculate-form.html`, `index.html`, and service page quick inquiry sidebars to native Netlify Forms (`data-netlify="true"`, `data-netlify-honeypot="bot-field"`).
  2. **Zero Data-Loss Storage:** Submissions are stored persistently in the Netlify Forms dashboard, providing permanent audit logs and exportable CSVs independent of any container lifecycle.
  3. **Zero Third-Party Cost & Credential Free:** Eliminates the need for paid API services (e.g. Resend) or exposed SMTP credentials in `.env`.
  4. **Multi-Layer Spam Protection:**
     - Netlify built-in server-side honeypot (`name="bot-field"`).
     - Invisible client-side honeypot (`name="website_url"`).
     - Rapid submission timer check flagging submissions occurring faster than 1 second from page render.
     - Form submit debounce and button disabling.
  5. **Truthful Feedback & Immediate WhatsApp / Phone Fallback:**
     - The frontend controller (`js/ecocare.js`) strictly verifies HTTP 2xx from Netlify before rendering a success alert.
     - On network or server error, it **never** falsely claims "message received"; instead, it surfaces a prominent notice with one-click pre-filled WhatsApp link (`+233 24 901 4253`), direct phone call link, and direct email link (`ecocaregh1on1@gmail.com`).
  6. **Automated Verification:** Verified via `node scripts/test_netlify_forms.js` (14/14 tests pass).
- **Open Status Justification:**
  - Automated tests prove that HTML attributes, honeypots, phone/email validation, and URL-encoded serialization are 100% correct.
  - However, in accordance with our truthfulness rules, passing test scripts does NOT constitute proof of live email inbox delivery.
  - To achieve live email delivery, the site administrator must enable Form Notifications in the Netlify Dashboard (pointing to `ecocaregh1on1@gmail.com`), deploy the staging/full site, and submit a verified test form. Until an email is confirmed delivered to `ecocaregh1on1@gmail.com`, RB-01 remains **PENDING INBOX TEST**.

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

- **Status:** Complete, tested, and verified.
- **Dedicated Build System:** Created `scripts/build_coming_soon.py` which compiles `coming-soon.html` into `dist/coming-soon/` with 0 missing assets.
- **Fixed 7-Day Countdown:** `js/coming-soon-countdown.js` targets fixed UTC timestamp `2026-11-16T14:00:00Z` (November 16, 2026, 14:00 GMT / Accra time). Invariant across refreshes and timezones; stops cleanly at zero with neutral announcement; strictly never exposes in-progress pages.
- **Branding & Visuals:** Original Clenix coming soon art (`coming-soon.jpg`) with authentic EcoCare logo (`img/large-logo.png`), favicon (`img/favicon.png`), 5 service family chips, direct WhatsApp dispatch CTA (`+233 24 901 4253`), and phone/email.
- **Netlify & Vercel Dual Strategy:** Root `netlify.toml` automatically builds and publishes `dist/coming-soon` to `https://ecocaregh.com`, keeping the Vercel full-site preview intact. Complete deployment documentation written at `docs/ecocare/COMING_SOON_DEPLOYMENT.md`.

---

## Pre-Launch Verification Summary

| Test Suite | Script | Total Checks | Result |
|---|---|---|---|
| Automated QA & Anti-Regression | `python3 scripts/qa_check.py` | 116 | **116 PASS / 0 FAIL** |
| Form Backend & Spam Protection | `node scripts/test_form_backend.js` | 10 | **10 PASS / 0 FAIL** |
| Multi-Screen Responsive & Routes | `python3 scripts/verify_responsive_and_routes.py` | 105 | **105 PASS / 0 FAIL** |
| Standalone Coming Soon & Countdown | `python3 scripts/test_coming_soon.py` | 12 | **12 PASS / 0 FAIL** |
| Responsive & Vercel Route Audit | `python3 scripts/verify_responsive_and_routes.py` | 105 | **105 PASS / 0 FAIL** |
