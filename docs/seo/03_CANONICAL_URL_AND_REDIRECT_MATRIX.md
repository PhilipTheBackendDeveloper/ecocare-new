# EcoCare Cleaning Services Limited — Canonical URL & Redirect Matrix
**Document:** `docs/seo/03_CANONICAL_URL_AND_REDIRECT_MATRIX.md`  
**Date:** November 9, 2026  
**Status:** Canonical Information Architecture Blueprint  
**Primary Host:** `https://ecocaregh.com/` (Apex preferred, HTTPS enforced)  

---

## 1. Domain & Protocol Normalization

To eliminate duplicate content penalties, preserve link equity, and enforce TLS security, the following canonicalization rules apply at the CDN/server layer:

| Inbound Request | Target Canonical URL | HTTP Status | Rule Type |
|---|---|---|---|
| `http://ecocaregh.com/*` | `https://ecocaregh.com/:splat` | 301 Permanent | HTTP -> HTTPS Upgrade |
| `http://www.ecocaregh.com/*` | `https://ecocaregh.com/:splat` | 301 Permanent | WWW -> Apex Unification |
| `https://www.ecocaregh.com/*` | `https://ecocaregh.com/:splat` | 301 Permanent | WWW -> Apex Unification |
| `https://ecocaregh.com/index.html` | `https://ecocaregh.com/` | 301 Permanent | Directory Index Stripping |

---

## 2. Canonical Route Inventory (State B: Full Site Launch)

Every served public page maps to exactly one clean URL. Self-referencing canonical `<link rel="canonical" href="...">` tags are embedded in the `<head>` of every HTML document.

| Canonical Public URL | Source Physical File | Page Identity & Search Intent | Robots Directive | Sitemap Status |
|---|---|---|---|---|
| `https://ecocaregh.com/` | `index.html` | Brand Homepage & Facility Care in Accra | `index, follow` | Included (`priority: 1.0`) |
| `https://ecocaregh.com/about` | `about1.html` | Company History, Leadership & Values | `index, follow` | Included (`priority: 0.8`) |
| `https://ecocaregh.com/services` | `service1.html` | 12 Service Listings Directory | `index, follow` | Included (`priority: 0.9`) |
| `https://ecocaregh.com/cleaning` | `single-service1.html` | EcoClean Residential & Corporate Janitorial | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/laundry` | `single-service2.html` | Eco-Laundry Doorstep Wash & Ironing | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/pest-control` | `pest-control.html` | EcoFumes Fumigation & Regulated Pest Control | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/carpet-cleaning` | `carpet-cleaning.html` | Carpet Deep Steam Extraction & Stain Removal | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/upholstery-cleaning` | `upholstery-cleaning.html` | Sofa Deep Extraction & Leather Conditioning | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/packages` | `pricing-table.html` | Scope-Based Service Packages in GHS | `index, follow` | Included (`priority: 0.8`) |
| `https://ecocaregh.com/request-quote` | `calculate-form.html` | Online Estimate Calculator & Booking Desk | `index, follow` | Included (`priority: 0.85`) |
| `https://ecocaregh.com/faq` | `faq.html` | Operational Customer FAQs & Policies | `index, follow` | Included (`priority: 0.7`) |
| `https://ecocaregh.com/contact` | `contact.html` | Achimota Mile 7 Office, Phones & Direct Desk | `index, follow` | Included (`priority: 0.8`) |
| `https://ecocaregh.com/projects` | `project1.html` | Field Execution Showcase & Photo Gallery | `index, follow` | Included (`priority: 0.7`) |
| `https://ecocaregh.com/projects/commercial-case-study` | `single-project1.html` | Corporate Facility Deep Cleaning Case Study | `index, follow` | Included (`priority: 0.6`) |
| `https://ecocaregh.com/privacy-policy` | `privacy-policy.html` | Ghana Data Protection Act (Act 843) Notice | `index, follow` | Included (`priority: 0.3`) |
| `https://ecocaregh.com/terms` | `terms-condition.html` | Operational Terms & Scope of Work | `index, follow` | Included (`priority: 0.3`) |
| `https://ecocaregh.com/coming-soon` | `coming-soon.html` | Temporary Launch Countdown (State A Root) | `noindex, follow` | Excluded from Full Sitemap |
| `https://ecocaregh.com/404` | `404.html` | Error Recovery Page (Returns HTTP 404) | `noindex, nofollow` | Excluded from Sitemap |

---

## 3. Legacy Extension Redirects (`.html` -> Clean URLs)

To ensure visitors arriving from external backlinks, social bookmarks, or search caches reach the canonical URL seamlessly without duplicate URL indexing:

| Inbound Request Path | Destination Clean URL | HTTP Status |
|---|---|---|
| `/about1.html` | `/about` | 301 Permanent |
| `/service1.html` | `/services` | 301 Permanent |
| `/single-service1.html` | `/cleaning` | 301 Permanent |
| `/single-service2.html` | `/laundry` | 301 Permanent |
| `/pest-control.html` | `/pest-control` | 301 Permanent |
| `/carpet-cleaning.html` | `/carpet-cleaning` | 301 Permanent |
| `/upholstery-cleaning.html` | `/upholstery-cleaning` | 301 Permanent |
| `/pricing-table.html` | `/packages` | 301 Permanent |
| `/calculate-form.html` | `/request-quote` | 301 Permanent |
| `/faq.html` | `/faq` | 301 Permanent |
| `/contact.html` | `/contact` | 301 Permanent |
| `/project1.html` | `/projects` | 301 Permanent |
| `/single-project1.html` | `/projects/commercial-case-study` | 301 Permanent |
| `/privacy-policy.html` | `/privacy-policy` | 301 Permanent |
| `/terms-condition.html` | `/terms` | 301 Permanent |

---

## 4. Deprecated Demo Pages Disposition

The 13 unpopulated ThemeForest demo pages are quarantined and redirected permanently:

| Deprecated Demo File | Destination | Status | Reason |
|---|---|---|---|
| `/index2.html`, `/index3.html`, `/index4.html` | `/` | 301 | Unused template variants |
| `/about2.html` | `/about` | 301 | Duplicate demo About page |
| `/service2.html` | `/services` | 301 | Duplicate demo Services grid |
| `/blog1.html`, `/blog2.html`, `/single-blog1.html` | `/` | 301 | Unapproved demo blog posts |
| `/shop.html`, `/single-product.html` | `/services` | 301 | Non-functional demo webshop |
| `/team1.html`, `/team2.html`, `/single-team.html` | `/about` | 301 | Unapproved demo employee rosters |

---

## 5. Implementation Across Hosting Providers

### Netlify Implementation (`_redirects` & `netlify.toml`)
Netlify processes `_redirects` sequentially:
```text
# Domain Unification
http://ecocaregh.com/*    https://ecocaregh.com/:splat    301!
http://www.ecocaregh.com/* https://ecocaregh.com/:splat   301!
https://www.ecocaregh.com/* https://ecocaregh.com/:splat  301!

# Clean URL Rewrites (Internal 200 mapping)
/about                      /about1.html                 200
/services                   /service1.html               200
/cleaning                   /single-service1.html        200
/laundry                    /single-service2.html        200
/pest-control               /pest-control.html           200
/carpet-cleaning            /carpet-cleaning.html        200
/upholstery-cleaning        /upholstery-cleaning.html    200
/packages                   /pricing-table.html          200
/request-quote              /calculate-form.html         200
/faq                        /faq.html                    200
/contact                    /contact.html                200
/projects                   /project1.html               200
/projects/commercial-case-study /single-project1.html    200
/privacy-policy             /privacy-policy.html         200
/terms                      /terms-condition.html        200

# Legacy .html to Clean 301 Redirects
/index.html                 /                            301
/about1.html                /about                       301
/service1.html              /services                    301
/single-service1.html       /cleaning                    301
/single-service2.html       /laundry                     301
/pricing-table.html         /packages                    301
/calculate-form.html        /request-quote               301
/project1.html              /projects                    301
/single-project1.html       /projects/commercial-case-study 301
/terms-condition.html       /terms                       301

# Deprecated Demo Redirects
/index2.html                /                            301
/index3.html                /                            301
/index4.html                /                            301
/about2.html                /about                       301
/service2.html              /services                    301
/blog1.html                 /                            301
/blog2.html                 /                            301
/single-blog1.html          /                            301
/shop.html                  /services                    301
/single-product.html        /services                    301
/team1.html                 /about                       301
/team2.html                 /about                       301
/single-team.html           /about                       301

# Custom 404 Handler
/*                          /404.html                    404
```

### Vercel Implementation (`vercel.json`)
The existing `vercel.json` already contains `cleanUrls: true` and the corresponding 15 clean URL rewrite definitions, ensuring 100% route parity between preview and production.

