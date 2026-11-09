# EcoCare Cleaning Services Limited — Netlify Forms & Staging Architecture Guide

**Document Version:** 1.0  
**Date:** 9 November 2026  
**Status:** Active Engineering Guide  
**Target Environment:** Netlify Static Hosting & Staging Previews (`https://ecocaregh.com`)

---

## 1. Executive Summary & Why Netlify Forms

Previous iterations of the EcoCare form architecture relied on Node.js serverless functions (`api/contact.js`, `api/quote.js`) that attempted to append incoming inquiries to a local file (`data/submissions.jsonl`) on disk.

### Critical Deficiencies of the Legacy Approach:
1. **Serverless Ephemeral Filesystem (Data-Loss Risk):** In serverless and edge hosting environments, filesystem writes are ephemeral. Every container shutdown or redeployment completely wipes local files, leading to permanent loss of customer leads.
2. **Unsupported on Static Hosting:** On standard static hosting, `/api` endpoints 404. Attempting to fall back to `vendor/php/` fails because modern Jamstack/static hosts do not execute PHP.
3. **Third-Party Dependency & Fragility:** Serverless email dispatch required external API keys (e.g. Resend, SendGrid) which introduced subscription fees, API rate limits, and failure modes when keys expire or are not configured.

### The Solution: Native Netlify Forms
Netlify Forms provides built-in, zero-maintenance, zero-cost form handling designed specifically for static HTML sites:
- **Permanent Dashboard Storage:** All submissions are stored indefinitely in the Netlify Forms dashboard, accessible anytime, filterable, and exportable to CSV.
- **Zero Third-Party APIs or Credentials:** No API keys or SMTP servers needed.
- **Native Spam Filtering:** Built-in server-side honeypots and machine-learning Akismet spam filtering.
- **Native Email Notifications:** Out-of-the-box email alerts delivered directly to `ecocaregh1on1@gmail.com`.

---

## 2. Form Architecture & Mappings

The website consolidates all customer touchpoints into **two primary forms** in the Netlify Dashboard:

### Form 1: `contact`
- **Primary Page:** `contact.html` (Send Us a Message)
- **Secondary Locations:** Sidebar "Quick Inquiry" widgets on `single-service1.html`, `single-service2.html`, `pest-control.html`, `carpet-cleaning.html`, `upholstery-cleaning.html`, and `faq.html`.
- **Fields:**
  - `form-name` = `"contact"` (Hidden)
  - `bot-field` (Netlify honeypot, hidden from humans)
  - `name` (Full Name, required)
  - `phone` (Telephone Number, required)
  - `email` (Email Address, optional)
  - `subject` (Inquiry Topic / Service)
  - `message` (Service Details, required)

### Form 2: `quote-calculator`
- **Primary Page:** `calculate-form.html` (Request An Estimate)
- **Secondary Location:** `index.html` (Homepage Quick Estimate Calculator)
- **Fields:**
  - `form-name` = `"quote-calculator"` (Hidden)
  - `bot-field` (Netlify honeypot, hidden from humans)
  - `service` (EcoClean Residential, Commercial Janitorial, Eco-Laundry, EcoFumes Fumigation, Carpet Deep Clean, Upholstery Care, Post-Construction)
  - `property_type` (Residential, Apartment, Office, Industrial)
  - `frequency` (One-Off, Weekly, Bi-Weekly, Monthly)
  - `size_sqm` / `rooms` / `bathrooms` (Scope indicators)
  - `location` (Area / Landmark in Greater Accra, required)
  - `date` / `time` (Preferred schedule)
  - `name` (Full Name, required)
  - `phone` (Telephone Number, required)
  - `email` (Email Address, optional)
  - `message` / `notes` (Specific Requirements)

---

## 3. Client-Side Submission Controller (`js/ecocare.js`)

The client-side controller handles submission smoothly via asynchronous JavaScript without reloading the page, while preserving full fallback for JavaScript-disabled environments.

### Multi-Layer Defenses:
1. **Server Honeypot:** Netlify's `bot-field` input catches automated crawlers.
2. **Client Honeypot:** `website_url` input catches bots filling all text fields.
3. **Rapid Timing Attack Guard:** Submissions occurring faster than 1 second from page render are flagged and prevented.
4. **Button Debounce:** Submit buttons are immediately disabled and display a spinner `<i class="fas fa-spinner fa-spin"></i>` to prevent accidental multi-submissions.
5. **Ghanaian & International Phone Validation:** Validates 10-digit Ghana local numbers (`024`, `055`, `020`, `030`, etc.), Ghanaian international format (`+233 24 901 4253`), and E.164 formats (9 to 16 digits).

### Verified Truthful Feedback:
- **Success Case (HTTP 2xx):**
  Only when Netlify genuinely accepts the submission with HTTP 200 does the form display:
  > *"Thank you, [Name]! Your inquiry has been delivered directly to EcoCare Cleaning Services Limited. Our dispatch desk in Achimota Mile 7 will review your scope and contact you at [Phone] shortly."*
  Includes an optional one-click green button: **Connect With Dispatch on WhatsApp (+233 24 901 4253)** pre-filled with the customer's exact scope.
- **Error / Offline Case (Non-2xx or Network Failure):**
  The controller **never** falsely claims "message received". It displays a clear, helpful warning:
  > *"Notice: We could not deliver your request online due to a network connection issue."*
  Immediately offers 3 direct communication channels:
  1. Click to send pre-filled message on WhatsApp (`+233 24 901 4253`)
  2. Call dispatch directly (`tel:+233249014253`)
  3. Send direct email to `mailto:ecocaregh1on1@gmail.com`

---

## 4. How to Enable Email Notifications in Netlify Dashboard

To receive real-time email alerts whenever a customer submits an inquiry:

1. Log into your [Netlify Dashboard](https://app.netlify.com/).
2. Select your site: **`ecocaregh`** (or the corresponding site name).
3. In the left navigation, click **Site configuration** > **Notifications** (or **Site settings** > **Forms** > **Form notifications**).
4. Click **Add notification** and choose **Email notification**.
5. Configure the notification modal:
   - **Event:** `New form submission`
   - **Form:** Select `Any form` (or create separate notifications for `contact` and `quote-calculator`).
   - **Email to notify:** `ecocaregh1on1@gmail.com`
6. Click **Save**.
7. Netlify will now automatically email `ecocaregh1on1@gmail.com` with the full submitted details, timestamp, and IP address whenever any customer submits either form.

---

## 5. Safe Full-Site Staging Architecture

The public production website (`https://ecocaregh.com`) is currently serving the isolated 7-Day Coming Soon countdown. To preview the complete EcoCare website without altering production DNS or exposing the full site:

### A. Netlify Context Routing (`netlify.toml`)
```toml
[build]
  command = "python3 scripts/build_coming_soon.py"
  publish = "dist/coming-soon"

# Production Context: Strictly Coming Soon landing page
[context.production]
  command = "python3 scripts/build_coming_soon.py"
  publish = "dist/coming-soon"

# Deploy Previews (Pull Requests against main): Builds complete staging site
[context.deploy-preview]
  command = "python3 scripts/build_staging.py"
  publish = "dist/staging"

# Branch Deploys (feature branches): Builds complete staging site
[context.branch-deploy]
  command = "python3 scripts/build_staging.py"
  publish = "dist/staging"
```

### B. What Staging Builds (`scripts/build_staging.py`)
- **Includes:** All 17 canonical HTML pages, stylesheets, scripts, logos, video background, and Netlify form configurations.
- **Excludes:** All 12 unapproved demo templates (`index2.html`, `blog1.html`, `shop.html`, etc.), documentation, test scripts, local data files, and secrets.
- **Indexing Barriers:**
  - `dist/staging/_headers`: Injects `X-Robots-Tag: noindex, nofollow` on all routes `/*`.
  - `dist/staging/robots.txt`: Injects `User-agent: * \n Disallow: /`.

### C. Local Staging Preview Command
You can build and preview the complete staging site locally in any browser by running:
```bash
python3 scripts/build_staging.py --serve 8080
```
Then navigate to `http://localhost:8080/` in your browser. All clean URLs, forms, and video hero will function identically to the production build.
