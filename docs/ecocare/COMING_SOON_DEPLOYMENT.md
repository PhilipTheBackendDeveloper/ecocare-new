# EcoCare — 7-Day Coming Soon Deployment & Handover Guide

**Document Version:** 1.0  
**Date:** 9 November 2026  
**Status:** Ready for Deployment  
**GitHub Repository:** `PhilipTheBackendDeveloper/ecocare-new`  
**Target Domain:** `https://ecocaregh.com`  

---

## 1. Overview & Architecture

To protect client privacy, ensure truthfulness, and allow the EcoCare team to finalize business approvals without public exposure of in-progress pages, this repository includes an **isolated, standalone Coming Soon landing page**.

```
repo-root/
  coming-soon.html                 # Canonical source template with authentic Clenix design
  js/coming-soon-countdown.js      # Robust fixed UTC 7-day countdown controller
  scripts/build_coming_soon.py     # Deterministic Python build script
  dist/coming-soon/                # GENERATED output (gitignored; published to Netlify)
    index.html                     # Deployed at public root /
    css/                           # Minimal scoped stylesheets & Bootstrap
    js/                            # Countdown controller & jQuery
    img/                           # Official EcoCare logo, favicon, background art
    font/ & webfonts/              # Icon fonts (FontAwesome & Flaticon)
    _headers                       # Security headers (X-Frame-Options, nosniff)
    netlify.toml                   # Standalone publish configuration
  netlify.toml                     # Root build config instructing Netlify
```

### Key Safety Guarantees:
1. **Full Site Preserved:** The full website, `index.html`, all 18 canonical pages, images, and `vercel.json` are completely untouched.
2. **Dual-Environment Separation:**
   - **Vercel Preview (`vercel.json`):** Continues serving the full in-progress website preview for internal review.
   - **Netlify (`netlify.toml`):** Publishes ONLY `dist/coming-soon` to the public domain `https://ecocaregh.com`.
3. **Zero Asset Leaks:** The published directory contains no `.env`, no serverless API code, no internal documentation, and no links to unpublished HTML pages.

---

## 2. Seven-Day Fixed Countdown Specification

- **Target Launch Deadline:** **Monday, 16 November 2026 at 14:00:00 GMT (Africa/Accra)**  
  `2026-11-16T14:00:00Z`
- **Timezone Invariance:** Calculated against a fixed UTC millisecond epoch (`1794837600000`). All visitors across Ghana, UK, US, or mobile devices see the exact same synchronized countdown.
- **Refresh Invariant:** Does NOT reset to `Date.now() + 7 days` on page reloads or Git commits.
- **Deadline Behavior (Zero Clamp):**
  When the timer reaches zero, it stops at `00 Days 00 Hours 00 Minutes 00 Seconds` and displays a neutral verification notice:
  > *"The enhanced EcoCare platform is undergoing final launch verification. We will be live momentarily!"*
  **The page strictly NEVER auto-redirects or exposes the unfinished website.** Public go-live requires an explicit human deployment action.

### How to Adjust the Launch Date:
If the public launch schedule changes, update the deadline in **two places**:
1. In `coming-soon.html`:
   ```html
   <div class="countdown" id="launch-countdown" data-deadline="YYYY-MM-DDTHH:MM:SSZ">
   ```
2. In `js/coming-soon-countdown.js`:
   ```javascript
   var DEFAULT_TARGET_UTC = "YYYY-MM-DDTHH:MM:SSZ";
   ```
Then run `python3 scripts/build_coming_soon.py` and commit.

---

## 3. Local Build & Verification Commands

### Step 1: Run the Isolated Build
```bash
python3 scripts/build_coming_soon.py
```
*Expected Output:*
```
✓ Cleaned and prepared dist/coming-soon
✓ Copied 15 core static assets.
✓ Copied FontAwesome webfonts.
✓ Copied Flaticon font assets.
✓ Created Netlify security headers and isolated netlify.toml.
Asset Checks: 14 relative references verified (0 missing)
```

### Step 2: Run the Automated Verification Suite
```bash
python3 scripts/test_coming_soon.py
```
*Validates:*
- Exactly 7 days remaining at planned launch start.
- Mid-week countdown precision.
- Near-zero (5s remaining) calculation.
- Post-deadline zero clamp and announcement trigger.
- Zero leaked internal links or secrets in `dist/coming-soon/`.

### Step 3: Run Full Website QA
```bash
python3 scripts/qa_check.py
```
*Confirms all 116 site-wide QA checks pass with 0 issues.*

---

## 4. Netlify Deployment Setup (Step-by-Step)

1. Log into your Netlify dashboard at [https://app.netlify.com/](https://app.netlify.com/).
2. Click **"Add new site"** → **"Import an existing project"**.
3. Select **GitHub** and authorize access to repository **`PhilipTheBackendDeveloper/ecocare-new`**.
4. Configure Build Settings (Netlify automatically reads `netlify.toml` from the repository):
   - **Branch to deploy:** `main`
   - **Base directory:** *(Leave blank / root)*
   - **Build command:** `python3 scripts/build_coming_soon.py`
   - **Publish directory:** `dist/coming-soon`
5. Click **"Deploy site"**.
6. Netlify will build the standalone Coming Soon landing page and assign a temporary URL (e.g., `ecocare-preview.netlify.app`).
7. Open the preview URL on desktop and mobile to verify:
   - Authentic EcoCare logo and favicon.
   - Clenix background art (`coming-soon.jpg`).
   - Active 7-day countdown updating every second.
   - Direct WhatsApp dispatch link (`+233 24 901 4253`).
   - Direct phone call link (`tel:+233249014253`).

---

## 5. Namecheap External DNS Configuration

Once the Netlify preview is verified, connect your custom domain **`ecocaregh.com`**:

### In Netlify:
1. Navigate to **Site configuration** → **Domain management** → **Domains**.
2. Click **"Add a domain"** and enter `ecocaregh.com`.
3. Confirm adding `ecocaregh.com` and `www.ecocaregh.com`.
4. Choose **"Set up external DNS"** (do NOT use Netlify Nameservers, so you avoid touching existing email MX records).

### In Namecheap:
1. Log into [Namecheap](https://www.namecheap.com/) and go to **Domain List**.
2. Find `ecocaregh.com` and click **"Manage"**.
3. Click the **"Advanced DNS"** tab.
4. **DO NOT DELETE OR TOUCH:**
   - Any MX records (e.g. Gmail / Google Workspace / cPanel mail).
   - Any TXT records containing `v=spf1`, `google-site-verification`, `DKIM`, or `DMARC`.
5. Under **Host Records**, remove any old conflicting `A` or `CNAME` records pointing to parking pages or old servers.
6. Add the following Netlify DNS records:
   - **Type:** `A Record`  
     **Host:** `@`  
     **Value:** `75.2.60.5` *(Netlify's load balancer IP)*  
     **TTL:** `Automatic` (or `1 min` during propagation)
   - **Type:** `CNAME Record`  
     **Host:** `www`  
     **Value:** `<your-site-name>.netlify.app.` *(Your actual Netlify site domain with trailing dot)*  
     **TTL:** `Automatic`

### In Netlify (SSL Certificate):
1. In Netlify Domain management, scroll to **HTTPS** / **SSL/TLS Certificate**.
2. Once DNS propagates (typically 5–30 minutes), click **"Verify DNS configuration"** and **"Provision Certificate"**.
3. Netlify will automatically issue and renew a free Let's Encrypt SSL certificate for both `ecocaregh.com` and `www.ecocaregh.com`.

---

## 6. How to Switch to the Full Website (Go-Live Procedure)

When the EcoCare owner formally approves all remaining items in `docs/ecocare/CONTENT_APPROVAL_TODO.md` and provides email credentials (`RB-01`):

1. Open `netlify.toml` in the repository root.
2. Update the publish directory:
   ```toml
   [build]
     # For static HTML full website:
     publish = "."
   ```
3. Commit and push to `main`:
   ```bash
   git add netlify.toml
   git commit -m "chore(release): switch Netlify production target from coming-soon to full website"
   git push origin main
   ```
4. Netlify will immediately deploy the full 18-page EcoCare website live on `https://ecocaregh.com`.

### Emergency Rollback:
If you ever need to return to the Coming Soon page, simply change `publish = "."` back to `publish = "dist/coming-soon"` in `netlify.toml`, run `python3 scripts/build_coming_soon.py`, and push to `main`.
