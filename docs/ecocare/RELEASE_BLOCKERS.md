# EcoCare Website — Release Blockers & Pre-Launch Checklist

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Active – Requires client resolution before full public launch

---

## 🚦 Gate Status Overview

| ID | Description | Severity | Owner | Status |
|---|---|---|---|---|
| RB-01 | Form backend not functional | 🔴 HIGH | Dev / Client | OPEN |
| RB-02 | Testimonials on HOLD | 🟡 MEDIUM | Client | HOLD |
| RB-03 | Legal docs in DRAFT | 🟡 MEDIUM | Lawyer / Client | DRAFT |
| RB-04 | Hero slider stock images | 🟢 LOW | Client (photos) | PENDING ASSETS |
| RB-05 | Domain & email DNS setup | 🟡 MEDIUM | Client | PENDING |
| RB-06 | Vercel deployment configuration | 🟢 LOW | Dev | READY |

---

## RB-01 — Form Submission Backend (HIGH)

**Problem:** `vendor/php/form-process.php` was not scraped by HTTrack from the original RadiusTheme demo server. Forms in `calculate-form.html` and `contact.html` currently operate with client-side validation and honest success messaging with phone/email CTA fallback.

**Impact:** Users filling the online form do not automatically submit data to EcoCare's inbox.

**Resolution Options (in priority order):**
1. **Recommended (Free/Easy):** Integrate [Formspree](https://formspree.io/) — replace `<form id="ecocare-booking-form">` action with `https://formspree.io/f/{YOUR_FORM_ID}`. No server required.
2. **Alternative:** Use [EmailJS](https://www.emailjs.com/) for direct Gmail delivery without backend.
3. **Self-hosted:** Provide or build a PHP/Node.js serverless endpoint that emails submissions to `ecocaregh1on1@gmail.com`.

**Current Fallback:** Forms display a clear call-to-action directing users to `+233 24 901 4253`.

---

## RB-02 — Customer Testimonials (MEDIUM)

**Problem:** 8 customer reviews (Nana Esi, Raymond Okyere, Peter Darko, Derek Agyapong, etc.) appeared on the old EcoCare website. They are marked `[HOLD]` in `docs/ecocare/CONTENT_APPROVAL_TODO.md` (see CA-09).

**Resolution Required:** Client to confirm:
- Review authenticity and permission to republish
- Whether star ratings, designations, and profile images are correct
- Whether any reviewers must be anonymized

**Current State:** No testimonials published on live site.

---

## RB-03 — Privacy Policy & Terms of Service (MEDIUM)

**Problem:** `privacy-policy.html` and `terms-condition.html` are published as DRAFT documents with a visible legal review banner.

**Resolution Required:** EcoCare Cleaning Services Limited legal counsel or management to review and formally approve both documents before the banner is removed.

---

## RB-04 — Hero Slider & Service Images (LOW)

**Problem:** `index.html` hero uses `img/slider/slide1-1.jpg` (copied from `banner-02.jpg` owned by EcoCare). Service detail pages use Clenix template stock service photos (`img/service/service1.jpg` through `service11.jpg`).

**Resolution Required:**
- Client to provide authentic EcoCare job-site photography for service pages.
- Replace `img/service/service1.jpg` through `service5.jpg` with authentic photos.
- Verify usage rights for all images before formal launch.

---

## RB-05 — Domain & Email DNS Configuration (MEDIUM)

**Problem:** `info@ecocaregh.com` is not yet verified (domain renewal/MX configuration pending, see CA-01). The site currently uses `ecocaregh1on1@gmail.com` everywhere.

**Resolution Required:**
- Client to renew `ecocaregh.com` domain registration.
- Configure MX records for email hosting.
- Once verified, update `EMAIL_PRIMARY` in `scripts/template_core.py` and rebuild pages.

---

## RB-06 — Vercel Deployment (LOW)

**Status:** ✅ `vercel.json` is configured with clean URL rewrites. Ready to deploy.

**To deploy:**
```bash
npm install -g vercel
vercel --prod
```

All routes in `/` → `index.html`, `/about` → `about1.html`, etc., are pre-mapped.

---

## ✅ Items Resolved (Not Blockers)

| Item | Resolution |
|---|---|
| HTTrack 52 comment blocks | Removed from all 26 HTML files |
| Cloudflare tracking beacon | Removed from all 26 HTML files |
| `popper.html` scraped file (99KB) | Deleted; `require()` corrected in JS |
| Demo Google Maps API key | Replaced with verified iframe embed |
| Clenix copyright/brand in pages | Patched across all 31 HTML files |
| `noindex` on 13 deprecated demo pages | Added |
| Demo USD prices ($49/$99/$199) | Replaced with GHS custom-scoping packages |
| Fake staff cutout models | Not used in any public page |
| Fabricated stats ("2583+ Clients") | Removed; replaced with real service highlights |
| EcoCare logo/favicon deployment | `img/logo-dark.png`, `img/favicon.png` active |

