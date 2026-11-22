# EcoCare Cleaning Services — Route & Redirect Architecture (`ROUTE_REDIRECT_MATRIX.md`)

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Canonical Routing Specification  

---

## 1. Canonical Public Routes

These are the official public-facing routes for the EcoCare website:

| Public Route | Physical HTML File | Page Title / Purpose | Navigation Link |
| :--- | :--- | :--- | :--- |
| `/` | `index.html` | EcoCare Cleaning Services Limited \| Professional Cleaning in Accra, Ghana | Home |
| `/about` | `about1.html` | About EcoCare Cleaning Services \| Our Story, Mission & Standards | About Us |
| `/services` | `service1.html` | All Cleaning Services \| EcoCare Complete Service Directory | Services Directory |
| `/cleaning` | `single-service1.html` | EcoClean \| Residential, Commercial & Deep Cleaning Services | EcoClean |
| `/laundry` | `single-service2.html` | Eco-Laundry \| Washing, Ironing & Delicate Garment Care | Eco-Laundry |
| `/pest-control` | `pest-control.html` | EcoFumes \| Professional Fumigation & Pest Control Services | EcoFumes |
| `/carpet-cleaning`| `carpet-cleaning.html`| Professional Carpet Cleaning & Stain Extraction \| EcoCare | Carpet Cleaning |
| `/upholstery-cleaning`| `upholstery-cleaning.html`| Sofa & Upholstery Cleaning Services \| EcoCare Ghana | Upholstery Care |
| `/packages` | `pricing-table.html` | Service Packages & Estimate Inquiries \| EcoCare | Packages & Estimates |
| `/projects` | `project1.html` | Completed Work & Service Gallery \| EcoCare | Projects Gallery |
| `/faq` | `faq.html` | Frequently Asked Questions \| EcoCare Cleaning Services | FAQ |
| `/contact` | `contact.html` | Contact EcoCare \| Achimota Mile 7, Accra, Ghana | Contact Us |
| `/request-quote`| `calculate-form.html`| Request a Service Quote & Booking Inquiry \| EcoCare | Book Now |
| `/privacy-policy`| `privacy-policy.html`| Privacy Policy (Draft - Pending Legal Review) | Footer Legal |
| `/terms` | `terms-condition.html`| Terms & Conditions (Draft - Pending Legal Review) | Footer Legal |
| `/coming-soon` | `coming-soon.html` | EcoCare Cleaning Services Limited \| Launching Soon | Utility / Maintenance |
| `404` | `404.html` | Page Not Found \| EcoCare Cleaning Services Limited | Error Handler |

---

## 2. Deprecated & Internal Demo Routes (Excluded from Public Navigation)

The following template demo variants are retained in the codebase for internal design/widget reference, but are excluded from public navigation, sitemaps, and search engines:

| Template File | Original Demo Purpose | Public Status | Handling / Redirect Recommendation |
| :--- | :--- | :--- | :--- |
| `index2.html` | Homepage Variant 2 | Unpublished Demo | Canonical points to `index.html`. Add `<meta name="robots" content="noindex, follow">`. |
| `index3.html` | Homepage Variant 3 | Unpublished Demo | Canonical points to `index.html`. Add `<meta name="robots" content="noindex, follow">`. |
| `index4.html` | Homepage Variant 4 | Unpublished Demo | Canonical points to `index.html`. Add `<meta name="robots" content="noindex, follow">`. |
| `about2.html` | About Variant 2 | Unpublished Demo | Canonical points to `about1.html`. Add `<meta name="robots" content="noindex, follow">`. |
| `service2.html` | Service Variant 2 | Unpublished Demo | Canonical points to `service1.html`. Add `<meta name="robots" content="noindex, follow">`. |
| `single-project1.html` | Case Study Variant | Internal Template | Retained for future case studies; not in main nav. |
| `team1.html` | Team Grid Variant 1 | Internal Template | Excluded from main nav pending client-approved staff profiles. |
| `team2.html` | Team Grid Variant 2 | Unpublished Demo | Excluded from main nav. |
| `single-team.html` | Single Profile Variant | Internal Template | Excluded from main nav pending individual approvals. |
| `shop.html` | E-Commerce Catalog | **DEPRECATED** | EcoCare has no e-commerce store. Removed from nav and footer. |
| `single-product.html` | Product Detail | **DEPRECATED** | Removed from nav and footer. |
| `blog1.html` | Blog Grid Variant 1 | **DEPRECATED** | EcoCare has no published articles. Removed from nav and footer. |
| `blog2.html` | Blog List Variant 2 | **DEPRECATED** | Removed from nav and footer. |
| `single-blog1.html` | Single Article Post | **DEPRECATED** | Removed from nav and footer. |
| `popper.html` | Scraped Error Artifact | **DELETED** | File removed from repository. |

---

## 3. Host-Level Clean URL Configuration (Vercel `vercel.json`)

To support clean, extension-free URLs on Vercel or any modern static web host, the following `vercel.json` provides clean route rewrites:

```json
{
  "cleanUrls": true,
  "trailingSlash": false,
  "rewrites": [
    { "source": "/", "destination": "/index.html" },
    { "source": "/about", "destination": "/about1.html" },
    { "source": "/services", "destination": "/service1.html" },
    { "source": "/cleaning", "destination": "/single-service1.html" },
    { "source": "/laundry", "destination": "/single-service2.html" },
    { "source": "/pest-control", "destination": "/pest-control.html" },
    { "source": "/carpet-cleaning", "destination": "/carpet-cleaning.html" },
    { "source": "/upholstery-cleaning", "destination": "/upholstery-cleaning.html" },
    { "source": "/packages", "destination": "/pricing-table.html" },
    { "source": "/projects", "destination": "/project1.html" },
    { "source": "/faq", "destination": "/faq.html" },
    { "source": "/contact", "destination": "/contact.html" },
    { "source": "/request-quote", "destination": "/calculate-form.html" },
    { "source": "/privacy-policy", "destination": "/privacy-policy.html" },
    { "source": "/terms", "destination": "/terms-condition.html" }
  ]
}
```

