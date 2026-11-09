# EcoCare Cleaning Services Limited — Search Console, Bing & Operational Handover Runbook
**Document:** `docs/seo/07_SEARCH_CONSOLE_BING_HANDOVER.md`  
**Date:** November 9, 2026  
**Status:** Operator Handover & Webmaster Verification Instructions  
**Domain:** `https://ecocaregh.com/`  

---

## 1. Overview & Operational Principles

This runbook provides step-by-step, actionable instructions for the EcoCare website owner or technical administrator to claim, verify, and operate official search engine webmaster properties.

> [!IMPORTANT]
> In accordance with safety and security guidelines, autonomous coding agents must never attempt to log into private third-party provider accounts, modify live DNS records at Namecheap without authorization, or claim external ownership. The owner executes these exact steps.

---

## 2. Google Search Console (GSC) Setup

Google Search Console is the official tool to monitor indexing status, organic search queries, crawl errors, and Core Web Vitals.

### Step 1: Create a Domain Property
1. Navigate to [Google Search Console](https://search.google.com/search-console).
2. Sign in using the primary company Google Account (`ecocaregh1on1@gmail.com`).
3. Select **Add Property**.
4. In the property type dialog, choose **Domain** (left box), NOT "URL prefix".
5. Enter the apex domain: `ecocaregh.com` (without `https://` or `www`).
6. Click **Continue**.

### Step 2: Add DNS TXT Record at Namecheap
Google will provide a unique DNS TXT verification token (e.g. `google-site-verification=abc123xyz...`).
1. Log in to [Namecheap](https://www.namecheap.com).
2. Go to **Domain List** -> Click **Manage** next to `ecocaregh.com`.
3. Select the **Advanced DNS** tab.
4. In the **Host Records** section, click **Add New Record**:
   - **Type:** `TXT Record`
   - **Host:** `@`
   - **Value:** Paste the exact Google verification string provided.
   - **TTL:** `Automatic` (or `5 min`).
5. Click the green checkmark to save.
6. Return to Google Search Console and click **Verify**. (If verification does not succeed immediately, allow 5–15 minutes for DNS propagation and click Verify again).

### Step 3: Sitemap Submission Timing & Reconciliation
- **During State A (7-Day Coming Soon Countdown):**
  - **Do NOT submit `sitemap.xml` in Google Search Console yet.**
  - Because `coming-soon.html` utilizes `<meta name="robots" content="noindex, follow">` to protect search snippet quality, submitting an XML sitemap containing that URL causes Google Search Console to flag a coverage warning: *"Submitted URL marked 'noindex'"*.
  - Verification of domain ownership in Search Console via DNS TXT can proceed immediately; only the sitemap submission itself is deferred.
- **On State B Launch Day (Full Website Launch):**
  - In the left sidebar, click **Sitemaps** (under Indexing).
  - Under "Add a new sitemap", enter: `sitemap.xml`.
  - Click **Submit**.
  - Status will change to **Success** and indicate 16 discovered canonical URLs.

---

## 3. Bing Webmaster Tools & IndexNow Setup

Bing powers search for Microsoft Bing, Yahoo!, DuckDuckGo, and Windows Search.

### Step 1: Account Import
1. Navigate to [Bing Webmaster Tools](https://www.bing.com/webmasters).
2. Sign in with the company account.
3. Select **Import your sites from GSC** (recommended fastest path).
4. Authorize Google Search Console access; Bing will automatically import `ecocaregh.com`, verify ownership, and import the sitemap.

### Step 2: IndexNow Integration (Optional for Fast Crawling)
IndexNow is an open protocol that immediately informs participating search engines (Bing, Yandex, Seznam) when content is updated.
- An IndexNow API key can be hosted at `https://ecocaregh.com/[key].txt`.
- When pages are updated, an HTTP POST request notifies the IndexNow endpoint.
- *Note:* IndexNow alerts crawlers to changes; it does not guarantee immediate indexing or ranking.

---

## 4. Google Analytics 4 (GA4) / Privacy-First Analytics Setup

To monitor real-world user engagement without violating Ghana's Data Protection Act, 2012 (Act 843):

### Recommended Event Configuration:
1. Create a GA4 Web Stream for `https://ecocaregh.com/`.
2. Configure Enhanced Measurement (Page Views, Outbound Clicks, Form Interactions).
3. Set up **Custom Conversion Events**:
   - `contact_whatsapp_click`: Triggered when visitors click the WhatsApp CTA button.
   - `contact_phone_call`: Triggered when visitors click any `tel:` link.
   - `quote_form_submit`: Triggered upon successful submission of the estimate calculator.
   - `contact_form_submit`: Triggered upon successful submission of the contact desk form.
4. **Data Protection Compliance:**
   - Enable IP Anonymization (standard in GA4).
   - Set Data Retention to 2 or 14 months.
   - Ensure zero PII (names, phone numbers, email addresses) is transmitted in query parameters or custom event parameters.

---

## 5. Maintenance & Monitoring Rhythm

| Frequency | Action Item | Tool |
|---|---|---|
| **Weekly** | Check GSC "Coverage" / "Pages" for 404s, 500s, or crawl anomalies | Google Search Console |
| **Weekly** | Review form submissions in `data/submissions.jsonl` to ensure 0 lost inquiries | Server / Admin |
| **Monthly** | Review top organic queries, click-through rates (CTR), and impressions | Google Search Console |
| **Monthly** | Audit Google Business Profile messages, reviews, and operational hours | Google Business Profile |
| **Quarterly** | Test site-wide links, mobile responsiveness, and core web vitals | Lighthouse / Dev Audit |

