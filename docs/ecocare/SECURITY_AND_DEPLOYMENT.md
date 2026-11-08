# EcoCare Website — Security & Deployment Guide

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Ready for Review

---

## 1. Architecture Summary

This is a **static multi-page HTML5** website based on the Clenix ThemeForest template by RadiusTheme. There is no server-side CMS, database, or Node.js runtime involved. The page generation toolchain (`scripts/`) runs locally to produce final `.html` files, which are then deployed as pure static assets.

```
Local Build → Static HTML/CSS/JS → Vercel CDN → Public URL
```

---

## 2. Recommended Deployment: Vercel (Free Tier)

`vercel.json` is pre-configured in the project root with clean URL rewrites.

### Quick Deploy Steps
```bash
# Install Vercel CLI (one time)
npm install -g vercel

# Log in
vercel login

# Deploy from project root
cd /Users/apple/Developer/work/ecocare
vercel --prod
```

### Clean URL Mapping (from `vercel.json`)

| Public URL | File |
|---|---|
| `/` | `index.html` |
| `/about` | `about1.html` |
| `/services` | `service1.html` |
| `/cleaning` | `single-service1.html` |
| `/laundry` | `single-service2.html` |
| `/pest-control` | `pest-control.html` |
| `/carpet-cleaning` | `carpet-cleaning.html` |
| `/upholstery-cleaning` | `upholstery-cleaning.html` |
| `/packages` | `pricing-table.html` |
| `/request-quote` | `calculate-form.html` |
| `/projects` | `project1.html` |
| `/faq` | `faq.html` |
| `/contact` | `contact.html` |
| `/privacy-policy` | `privacy-policy.html` |
| `/terms` | `terms-condition.html` |

---

## 3. Alternative Deployment Options

| Host | Method | Cost | Notes |
|---|---|---|---|
| **Vercel** (recommended) | `vercel --prod` | Free | CDN, HTTPS auto, clean URLs |
| **Netlify** | Drag & drop or CLI | Free | Alternative to Vercel |
| **cPanel shared hosting** | FTP upload | Hosting cost | Standard `.htaccess` for clean URLs required |
| **GitHub Pages** | Git push to `gh-pages` | Free | File-based routing, no clean URLs without Jekyll |

---

## 4. Security Checklist

| Item | Status |
|---|---|
| ✅ No exposed server-side API keys | Confirmed — no backend secrets in repo |
| ✅ Demo Google Maps API key removed | Replaced with public-embed iframe |
| ✅ No database credentials | Static site — none applicable |
| ✅ Cloudflare beacon removed | Done (all 26 HTML files) |
| ✅ No HTTrack metadata leakage | Done (all 52 comments removed) |
| ✅ Forms use client-side only validation | No server endpoint exposed |
| ⚠️ Form backend not yet configured | See RB-01 in `RELEASE_BLOCKERS.md` |
| ✅ HTTPS enforced by host | Vercel enforces HTTPS automatically |

---

## 5. Rebuilding Pages After Content Changes

If contact information, services, or business details change, update `scripts/template_core.py` constants, then run:

```bash
# From the project root (/Users/apple/Developer/work/ecocare):
python3 scripts/build_canonical_pages.py
python3 scripts/build_remaining_canonical.py
python3 scripts/qa_check.py
```

All 18 canonical pages will be regenerated and QA-validated automatically.

---

## 6. Form Backend Integration (Future)

**When ready to enable real form submissions:**

### Option A — Formspree (Easiest)
1. Register at [formspree.io](https://formspree.io/)
2. Create a form connected to `ecocaregh1on1@gmail.com`
3. In `calculate-form.html` and `contact.html`, update the `<form>` tag:
   ```html
   <form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
   ```
4. Remove the `ecocare.js` custom submit handler for those forms

### Option B — EmailJS (No backend)
1. Register at [emailjs.com](https://www.emailjs.com/)
2. Connect your Gmail account
3. Add EmailJS SDK and call `emailjs.sendForm()` in `ecocare.js`

---

## 7. Sitemap & Robots.txt (Post-Launch)

After domain is live, create `robots.txt`:
```
User-agent: *
Allow: /

# Block deprecated demo pages from crawling
Disallow: /index2.html
Disallow: /index3.html
Disallow: /index4.html
Disallow: /about2.html
Disallow: /service2.html
Disallow: /shop.html
Disallow: /single-product.html
Disallow: /blog1.html
Disallow: /blog2.html
Disallow: /single-blog1.html
Disallow: /team1.html
Disallow: /team2.html
Disallow: /single-team.html

Sitemap: https://your-domain.com/sitemap.xml
```

Also generate `sitemap.xml` listing only the 15 canonical public pages.

