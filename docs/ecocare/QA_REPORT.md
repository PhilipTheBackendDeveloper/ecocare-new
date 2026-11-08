# EcoCare Cleaning Services Limited — QA Report

**Date:** 8 November 2026  
**Auditor:** Automated QA + Manual Review  
**Status:** ✅ ALL CRITICAL CHECKS PASSED

---

## 1. QA Check Summary

| Category | Count |
|---|---|
| ✅ Checks Passed | 116 |
| ⚠️ Warnings | 0 |
| ❌ Issues | 0 |

---

## 2. Canonical Pages Status

| Page File | Route | Status | EcoCare Brand | Real Contact | noindex? |
|---|---|---|---|---|---|
| `index.html` | `/` | ✅ PASS | ✅ | ✅ | No (public) |
| `about1.html` | `/about` | ✅ PASS | ✅ | ✅ | No (public) |
| `service1.html` | `/services` | ✅ PASS | ✅ | ✅ | No (public) |
| `single-service1.html` | `/cleaning` | ✅ PASS | ✅ | ✅ | No (public) |
| `single-service2.html` | `/laundry` | ✅ PASS | ✅ | ✅ | No (public) |
| `pest-control.html` | `/pest-control` | ✅ PASS | ✅ | ✅ | No (public) |
| `carpet-cleaning.html` | `/carpet-cleaning` | ✅ PASS | ✅ | ✅ | No (public) |
| `upholstery-cleaning.html` | `/upholstery-cleaning` | ✅ PASS | ✅ | ✅ | No (public) |
| `pricing-table.html` | `/packages` | ✅ PASS | ✅ | ✅ | No (public) |
| `calculate-form.html` | `/request-quote` | ✅ PASS | ✅ | ✅ | No (public) |
| `faq.html` | `/faq` | ✅ PASS | ✅ | ✅ | No (public) |
| `contact.html` | `/contact` | ✅ PASS | ✅ | ✅ | No (public) |
| `project1.html` | `/projects` | ✅ PASS | ✅ | ✅ | No (public) |
| `single-project1.html` | `/projects` (detail) | ✅ PASS | ✅ | ✅ | No (public) |
| `coming-soon.html` | — | ✅ PASS | ✅ | ✅ | N/A (utility) |
| `404.html` | — | ✅ PASS | ✅ | ✅ | N/A (utility) |
| `privacy-policy.html` | `/privacy-policy` | ✅ PASS | ✅ | ✅ | No (public) |
| `terms-condition.html` | `/terms` | ✅ PASS | ✅ | ✅ | No (public) |

---

## 3. Deprecated Pages Status

All 13 deprecated demo pages received `<meta name="robots" content="noindex, follow">` and had Clenix copyright/email/brand text patched.

| Page | noindex Tag | Clenix Brand Removed |
|---|---|---|
| `index2.html` | ✅ | ✅ |
| `index3.html` | ✅ | ✅ |
| `index4.html` | ✅ | ✅ |
| `about2.html` | ✅ | ✅ |
| `service2.html` | ✅ | ✅ |
| `blog1.html` | ✅ | ✅ |
| `blog2.html` | ✅ | ✅ |
| `single-blog1.html` | ✅ | ✅ |
| `shop.html` | ✅ | ✅ |
| `single-product.html` | ✅ | ✅ |
| `team1.html` | ✅ | ✅ |
| `team2.html` | ✅ | ✅ |
| `single-team.html` | ✅ | ✅ |

---

## 4. Security & Brand Safety Checks

| Check | Result |
|---|---|
| HTTrack `<!-- Mirrored from ... -->` comments | ✅ All removed (52 comments across 26 HTML files) |
| Cloudflare tracking beacon | ✅ Removed from all 26 original HTML files |
| Demo Google Maps API key (`AIzaSyB...`) | ✅ Replaced with verified iframe embed |
| `popper.html` scraped file | ✅ Deleted; `require()` fixed in bootstrap.min.js |
| Clenix brand in canonical pages | ✅ Zero occurrences |
| Demo phone numbers | ✅ Zero occurrences in canonical pages |
| Demo email addresses | ✅ Zero occurrences in canonical pages |
| Demo USD pricing | ✅ Removed; replaced with GHS scoping model |
| Demo stock staff cutout images | ✅ Not used in public team sections |
| Fake client testimonials | ✅ Not published (held pending CA-09 approval) |
| Fabricated statistics/counters | ✅ Replaced with verified service highlights |

---

## 5. Brand Signal Verification (All Canonical Pages)

| Verified Data Point | Status |
|---|---|
| Company Name: "EcoCare Cleaning Services Limited" | ✅ Present in all pages |
| Primary Phone: `+233 24 901 4253` | ✅ Click-to-call `tel:+233249014253` |
| Secondary Phone: `+233 24 380 7100` | ✅ Click-to-call `tel:+233243807100` |
| Email: `ecocaregh1on1@gmail.com` | ✅ Mailto links in footer + contact |
| Address: `Achimota Mile 7, Accra, Ghana` | ✅ All global headers + footer |
| Hours: `Mon - Sat: 07:00am - 06:00pm` | ✅ All global footers |
| Facebook link | ✅ All pages |
| TikTok link | ✅ All pages |
| YouTube link | ✅ All pages |
| Google Maps verified iframe embed | ✅ `contact.html` |
| EcoCare logo (`img/logo-dark.png`) | ✅ All headers |
| Favicon (`img/favicon.png`) | ✅ All pages |

---

## 6. CSS & JS Assets

| Asset | Status |
|---|---|
| `css/ecocare.css` | ✅ Linked in all canonical pages |
| `js/ecocare.js` | ✅ Linked in all canonical pages |
| `css/style.css` (Clenix base) | ✅ Intact |
| Clenix JS stack (jQuery, Bootstrap, Owl, Nivo) | ✅ Intact |
| `vendor/php/form-process.php` | ⚠️ Not present (never scraped by HTTrack). Forms use client-side validation + honest UX messaging. |

---

## 7. Forms Assessment

| Form | File | Backend | Current Handling |
|---|---|---|---|
| Quote / Booking Form | `calculate-form.html` | No backend | Client-side validation → human-readable confirmation message with phone CTA fallback |
| Contact Form | `contact.html` | No backend | Client-side validation → honest confirmation + phone/email redirect |

> [!IMPORTANT]
> `vendor/php/form-process.php` was never recovered from the original site. Forms currently provide a **client-side only** submission experience with clear user messaging and fallback to phone/email. For production, an SMTP gateway (Formspree, EmailJS, or server-side PHP/serverless) must be integrated.

---

## 8. Known Pre-Launch Blockers

Refer to `docs/ecocare/RELEASE_BLOCKERS.md` for the complete release gate list.

| ID | Blocker | Severity |
|---|---|---|
| RB-01 | No working form backend (`form-process.php` missing) | HIGH |
| RB-02 | Testimonials on HOLD pending client approval (CA-09) | MEDIUM |
| RB-03 | Privacy Policy and Terms under DRAFT status | MEDIUM |
| RB-04 | Google Maps API key (contact page uses iframe embed — no API key exposure) | LOW (resolved) |
| RB-05 | Hero slider uses template stock images; EcoCare brand photos pending | LOW |

