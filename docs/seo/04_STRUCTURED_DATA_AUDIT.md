# EcoCare Cleaning Services Limited — Structured Data & Entity Clarity Audit
**Document:** `docs/seo/04_STRUCTURED_DATA_AUDIT.md`  
**Date:** November 9, 2026  
**Status:** Schema Implementation & Compliance Report  
**Vocabulary:** [Schema.org](https://schema.org) (JSON-LD format)  
**Target Entity:** EcoCare Cleaning Services Limited (`#organization`)  

---

## 1. Entity Architecture & Stable Identity

To enable unambiguous entity reconciliation across Google Search, Google Knowledge Graph, Bing, and AI search assistants, EcoCare establishes a single canonical entity `@id`:

```json
"@id": "https://ecocaregh.com/#organization"
```

All subordinate structured data nodes (Services, AboutPage, ContactPage, Breadcrumbs) reference this stable root entity via `@id`, establishing an interconnected knowledge graph without redundant data or disconnected fragments.

---

## 2. Page-by-Page Structured Data Implementation

### A. Homepage (`index.html`) — Core LocalBusiness & Organization
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["LocalBusiness", "CleaningService"],
      "@id": "https://ecocaregh.com/#organization",
      "name": "EcoCare Cleaning Services Limited",
      "legalName": "EcoCare Cleaning Services Limited",
      "url": "https://ecocaregh.com/",
      "logo": "https://ecocaregh.com/img/large-logo.png",
      "image": "https://ecocaregh.com/img/large-logo.png",
      "description": "Professional residential housekeeping, corporate janitorial, doorstep laundry, EcoFumes fumigation, carpet extraction, and upholstery care in Accra, Ghana.",
      "telephone": ["+233249014253", "+233243807100"],
      "email": "ecocaregh1on1@gmail.com",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Achimota Mile 7",
        "addressLocality": "Accra",
        "addressRegion": "Greater Accra",
        "addressCountry": "GH"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 5.627819,
        "longitude": -0.244110
      },
      "openingHoursSpecification": [
        {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
          "opens": "07:00",
          "closes": "18:00"
        }
      ],
      "priceRange": "GHS",
      "areaServed": {
        "@type": "AdministrativeArea",
        "name": "Greater Accra Region, Ghana"
      },
      "founder": {
        "@type": "Person",
        "name": "Eric Nana Acquah",
        "jobTitle": "Chief Executive Officer"
      },
      "foundingDate": "2014-09-19",
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "EcoCare Professional Services",
        "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoClean Residential & Commercial Janitorial", "url": "https://ecocaregh.com/cleaning"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Eco-Laundry Doorstep Wash, Iron & Dry Cleaning", "url": "https://ecocaregh.com/laundry"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoFumes Regulated Pest Control & Fumigation", "url": "https://ecocaregh.com/pest-control"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Carpet Deep Steam Extraction & Stain Treatment", "url": "https://ecocaregh.com/carpet-cleaning"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Upholstery & Leather Furniture Deep Sanitization", "url": "https://ecocaregh.com/upholstery-cleaning"}}
        ]
      },
      "sameAs": [
        "https://www.facebook.com/profile.php?id=100006412849415",
        "https://www.tiktok.com/@ecocarecompanylimited",
        "https://www.youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA"
      ]
    },
    {
      "@type": "WebSite",
      "@id": "https://ecocaregh.com/#website",
      "url": "https://ecocaregh.com/",
      "name": "EcoCare Cleaning Services Limited",
      "publisher": {
        "@id": "https://ecocaregh.com/#organization"
      },
      "inLanguage": "en-GH"
    }
  ]
}
</script>
```

### B. Service Detail Pages — Specialized `Service` Node & BreadcrumbList
Example: EcoClean Janitorial (`single-service1.html` -> `/cleaning`):
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Service",
      "@id": "https://ecocaregh.com/cleaning#service",
      "name": "EcoClean Janitorial & Deep Cleaning Services",
      "serviceType": "Residential Housekeeping & Corporate Janitorial",
      "provider": {
        "@id": "https://ecocaregh.com/#organization"
      },
      "description": "Comprehensive residential cleaning, commercial corporate janitorial, and post-construction scrubbing across Greater Accra.",
      "areaServed": {
        "@type": "AdministrativeArea",
        "name": "Greater Accra Region, Ghana"
      },
      "url": "https://ecocaregh.com/cleaning"
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://ecocaregh.com/cleaning#breadcrumb",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "name": "Home",
          "item": "https://ecocaregh.com/"
        },
        {
          "@type": "ListItem",
          "position": 2,
          "name": "Services",
          "item": "https://ecocaregh.com/services"
        },
        {
          "@type": "ListItem",
          "position": 3,
          "name": "EcoClean",
          "item": "https://ecocaregh.com/cleaning"
        }
      ]
    }
  ]
}
</script>
```

### C. FAQ Page (`faq.html` -> `/faq`) — Validated `FAQPage`
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "FAQPage",
      "@id": "https://ecocaregh.com/faq#faq",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What areas in Accra does EcoCare cover?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "EcoCare operates across Greater Accra, including Achimota, East Legon, Cantonments, Airport Residential Area, Dzorwulu, Osu, Spintex, Ridge, Labone, and Tema."
          }
        },
        {
          "@type": "Question",
          "name": "Does EcoCare provide all cleaning equipment and detergents?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Yes, our uniformed cleaning crews arrive fully equipped with professional industrial vacuum extractors, floor scrubbing machines, microfiber materials, and eco-conscious cleaning agents."
          }
        },
        {
          "@type": "Question",
          "name": "How does EcoCare calculate service estimates?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Estimates are scoped transparently in Ghanaian Cedis (GHS) based on property size, floor count, surface conditions, and required equipment. Custom estimates can be calculated via our online quote tool."
          }
        },
        {
          "@type": "Question",
          "name": "What safety precautions are taken for fumigation and pest control?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "EcoFumes treatments strictly adhere to manufacturer product safety labels and certified operator directives. Technicians provide clear instructions on property preparation and room re-entry."
          }
        }
      ]
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://ecocaregh.com/faq#breadcrumb",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://ecocaregh.com/"},
        {"@type": "ListItem", "position": 2, "name": "FAQ", "item": "https://ecocaregh.com/faq"}
      ]
    }
  ]
}
</script>
```

### D. Contact Page (`contact.html` -> `/contact`) — `ContactPage`
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "ContactPage",
      "@id": "https://ecocaregh.com/contact#contact",
      "url": "https://ecocaregh.com/contact",
      "name": "Contact EcoCare Cleaning Services Limited",
      "mainEntity": {
        "@id": "https://ecocaregh.com/#organization"
      }
    },
    {
      "@type": "BreadcrumbList",
      "@id": "https://ecocaregh.com/contact#breadcrumb",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://ecocaregh.com/"},
        {"@type": "ListItem", "position": 2, "name": "Contact", "item": "https://ecocaregh.com/contact"}
      ]
    }
  ]
}
</script>
```

---

## 3. Strict Truthfulness Guardrails in Schema

To protect domain reputation and avoid Google manual actions:
1. **Zero `aggregateRating` / Review Snippets:** Google Guidelines explicitly forbid marking up self-serving, unverified reviews on a business's own LocalBusiness schema. All `aggregateRating`, `Review`, and star rating properties remain omitted until third-party verified review platforms are authenticated.
2. **Zero Fake `VideoObject` on Ambient Background Video:** The background hero video is purely decorative atmospheric media. It is NOT marked up with misleading `VideoObject` schemas or fabricated upload dates.
3. **Zero Fabricated SearchAction:** The site does not provide an on-site search engine with a `?q=` parameter; therefore, Google `potentialAction: SearchAction` is deliberately excluded.
4. **Zero Invented Currency Pricing:** Services link to transparent quotation booking rather than hardcoded fake price points in schema.

