#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — SEO, Accessibility (a11y) & Metadata Enhancer
1. Updates <html lang="en"> across all HTML files.
2. Injects OpenGraph & Twitter Cards into <head> for WhatsApp/social sharing previews.
3. Injects Schema.org JSON-LD LocalBusiness structured data on index.html.
4. Adds accessible aria-labels to unlabelled form controls.
5. Generates sitemap.xml and updates robots.txt with active Sitemap directive.
"""

import glob
import os
import re

CANONICAL_PAGES = {
    "index.html": {
        "title": "EcoCare Cleaning Services Limited | Professional Cleaning & Fumigation in Accra, Ghana",
        "description": "Professional residential & commercial janitorial cleaning, doorstep laundry, EcoFumes fumigation, carpet extraction, and upholstery care in Accra, Ghana.",
        "path": "",
        "priority": "1.0",
        "changefreq": "daily"
    },
    "about1.html": {
        "title": "About Us | EcoCare Cleaning Services Limited Ghana",
        "description": "Discover EcoCare's journey since 2014, our sustainable cleaning mission, and leadership by CEO Eric Nana Acquah in Achimota Mile 7, Accra.",
        "path": "about",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "service1.html": {
        "title": "Our Cleaning & Fumigation Services Directory | EcoCare Ghana",
        "description": "Explore all 12 specialized cleaning, laundry, carpet extraction, furniture care, and fumigation services across Greater Accra.",
        "path": "services",
        "priority": "0.9",
        "changefreq": "weekly"
    },
    "single-service1.html": {
        "title": "EcoClean Janitorial & Deep Cleaning Services | EcoCare Ghana",
        "description": "Comprehensive residential cleaning, commercial corporate janitorial, and post-construction scrubbing across Greater Accra.",
        "path": "cleaning",
        "priority": "0.85",
        "changefreq": "weekly"
    },
    "single-service2.html": {
        "title": "Eco-Laundry & Dry Cleaning with Doorstep Delivery | EcoCare Ghana",
        "description": "Scheduled laundry collection, gentle washing, professional ironing, and delicate dry cleaning delivered to your door in Accra.",
        "path": "laundry",
        "priority": "0.85",
        "changefreq": "weekly"
    },
    "pest-control.html": {
        "title": "EcoFumes Pest Control & Fumigation Services | EcoCare Ghana",
        "description": "Targeted eradication for termites, cockroaches, rodents, and bedbugs with mandatory 2-4 hour vacate safety protocols in Accra.",
        "path": "pest-control",
        "priority": "0.85",
        "changefreq": "weekly"
    },
    "carpet-cleaning.html": {
        "title": "Carpet Deep Cleaning & Steam Extraction Services | EcoCare Ghana",
        "description": "Five-stage hot water carpet extraction, heavy stain lifting, and commercial low-moisture cleaning in Accra.",
        "path": "carpet-cleaning",
        "priority": "0.85",
        "changefreq": "weekly"
    },
    "upholstery-cleaning.html": {
        "title": "Upholstery & Furniture Cleaning Services | EcoCare Ghana",
        "description": "Fabric couch deep extraction, delicate leather conditioning, and mattress allergen removal across Greater Accra.",
        "path": "upholstery-cleaning",
        "priority": "0.85",
        "changefreq": "weekly"
    },
    "pricing-table.html": {
        "title": "Affordable Cleaning Plans & Pricing | EcoCare Ghana",
        "description": "Transparent pricing scoping in Ghanaian Cedis (GHS) for residential, deep move-in, and corporate facility care.",
        "path": "packages",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "calculate-form.html": {
        "title": "Request a Free Estimate & Booking | EcoCare Ghana",
        "description": "Interactive estimate calculator and booking request for residential, corporate, laundry, and fumigation services in Accra.",
        "path": "request-quote",
        "priority": "0.85",
        "changefreq": "monthly"
    },
    "faq.html": {
        "title": "Frequently Asked Questions | EcoCare Ghana",
        "description": "Operational answers regarding coverage areas in Greater Accra, pricing in GHS, drying times, and fumigation preparation.",
        "path": "faq",
        "priority": "0.7",
        "changefreq": "monthly"
    },
    "contact.html": {
        "title": "Contact Us | EcoCare Cleaning Services Limited",
        "description": "Connect with our Achimota Mile 7 dispatch office. Phone: +233 24 901 4253 / +233 24 380 7100. Email: ecocaregh1on1@gmail.com.",
        "path": "contact",
        "priority": "0.8",
        "changefreq": "monthly"
    },
    "project1.html": {
        "title": "Our Work & Service Showcase | EcoCare Ghana",
        "description": "Explore field execution highlights across corporate janitorial, carpet restoration, and residential move-in projects in Accra.",
        "path": "projects",
        "priority": "0.7",
        "changefreq": "monthly"
    },
    "single-project1.html": {
        "title": "Commercial Facility Deep Cleaning Case Study | EcoCare Ghana",
        "description": "Case study: Multi-story corporate workspace deep cleaning, carpet steam extraction, and restroom sanitization in Accra.",
        "path": "projects/commercial-case-study",
        "priority": "0.6",
        "changefreq": "monthly"
    },
    "coming-soon.html": {
        "title": "Coming Soon | EcoCare Cleaning Services Limited",
        "description": "EcoCare Cleaning Services Limited upcoming service developments in Accra, Ghana.",
        "path": "coming-soon",
        "priority": "0.3",
        "changefreq": "yearly"
    },
    "404.html": {
        "title": "Page Not Found (404) | EcoCare Cleaning Services Limited",
        "description": "The page you are looking for does not exist. Return to EcoCare homepage.",
        "path": "404",
        "priority": "0.1",
        "changefreq": "yearly"
    },
    "privacy-policy.html": {
        "title": "Privacy Policy | EcoCare Cleaning Services Limited",
        "description": "Privacy policy and client data handling principles under Ghana's Data Protection Act, 2012 (Act 843).",
        "path": "privacy-policy",
        "priority": "0.3",
        "changefreq": "yearly"
    },
    "terms-condition.html": {
        "title": "Terms & Conditions | EcoCare Cleaning Services Limited",
        "description": "Operational service agreements and booking terms for EcoCare Cleaning Services Limited in Accra, Ghana.",
        "path": "terms",
        "priority": "0.3",
        "changefreq": "yearly"
    }
}

BASE_URL = "https://ecocaregh.com"

JSON_LD_SCHEMA = """    <!-- Schema.org JSON-LD Structured Data: LocalBusiness & CleaningService -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": ["LocalBusiness", "CleaningService"],
      "@id": "https://ecocaregh.com/#business",
      "name": "EcoCare Cleaning Services Limited",
      "legalName": "EcoCare Cleaning Services Limited",
      "url": "https://ecocaregh.com/",
      "logo": "https://ecocaregh.com/img/large-logo.png",
      "image": "https://ecocaregh.com/img/large-logo.png",
      "description": "Premier eco-friendly cleaning, doorstep laundry, pest control & fumigation, carpet extraction, and upholstery care in Greater Accra, Ghana.",
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
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "EcoCare Professional Services",
        "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoClean Residential & Commercial Janitorial"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Eco-Laundry Doorstep Wash, Iron & Dry Cleaning"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoFumes Regulated Pest Control & Fumigation"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Carpet Deep Steam Extraction & Stain Treatment"}},
          {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Upholstery & Leather Furniture Deep Sanitization"}}
        ]
      },
      "sameAs": [
        "https://www.facebook.com/profile.php?id=100006412849415",
        "https://www.tiktok.com/@ecocarecompanylimited",
        "https://www.youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA"
      ]
    }
    </script>"""


def fix_html_lang_and_metadata():
    print("Enhancing HTML lang and OpenGraph/Twitter social meta tags...")
    all_html_files = glob.glob("*.html")

    for fpath in all_html_files:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Fix lang="en"
        content = re.sub(r'<html\s+class="([^"]*)"\s+lang="[^"]*"', r'<html class="\1" lang="en"', content)
        content = re.sub(r'<html\s+lang="[^"]*"', r'<html lang="en"', content)

        # 2. Ingest OpenGraph & Twitter tags for canonical pages
        if fpath in CANONICAL_PAGES:
            meta = CANONICAL_PAGES[fpath]
            page_url = f"{BASE_URL}/{meta['path']}" if meta['path'] else f"{BASE_URL}/"

            og_block = f"""    <!-- Canonical & Social Metadata (OpenGraph & Twitter Card) -->
    <link rel="canonical" href="{page_url}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{meta['title']}">
    <meta property="og:description" content="{meta['description']}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:site_name" content="EcoCare Cleaning Services Limited">
    <meta property="og:image" content="{BASE_URL}/img/large-logo.png">
    <meta property="og:locale" content="en_GH">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{meta['title']}">
    <meta name="twitter:description" content="{meta['description']}">
    <meta name="twitter:image" content="{BASE_URL}/img/large-logo.png">"""

            # Remove existing og block if any, then insert right before </head>
            content = re.sub(r'\s*<!-- Canonical & Social Metadata.*?-->\s*(<link rel="canonical".*?<meta name="twitter:image"[^>]*>)?', '', content, flags=re.DOTALL)
            content = content.replace("</head>", f"{og_block}\n</head>")

            # 3. Add JSON-LD to index.html
            if fpath == "index.html" and "application/ld+json" not in content:
                content = content.replace("</head>", f"{JSON_LD_SCHEMA}\n</head>")

        # 4. Form accessibility: ensure inputs have aria-labels if missing
        def add_aria_label(tag_match, label):
            tag = tag_match.group(0)
            if 'aria-label=' in tag:
                return tag
            return tag[:-1] + f' aria-label="{label}">'

        content = re.sub(r'<input[^>]+name="name"[^>]*>', lambda m: add_aria_label(m, "Full Name"), content)
        content = re.sub(r'<input[^>]+name="phone"[^>]*>', lambda m: add_aria_label(m, "Telephone Number"), content)
        content = re.sub(r'<input[^>]+name="email"[^>]*>', lambda m: add_aria_label(m, "Email Address"), content)
        content = re.sub(r'<input[^>]+name="location"[^>]*>', lambda m: add_aria_label(m, "Location / Area in Accra"), content)
        content = re.sub(r'<textarea[^>]+name="message"[^>]*>', lambda m: add_aria_label(m, "Inquiry Message or Service Requirements"), content)
        content = re.sub(r'<select[^>]+name="service"[^>]*>', lambda m: add_aria_label(m, "Select Cleaning Service"), content)
        content = re.sub(r'<select[^>]+name="property_type"[^>]*>', lambda m: add_aria_label(m, "Property Type"), content)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✓ Enhanced {len(all_html_files)} HTML files with lang='en', social metadata, and accessible aria-labels.")


def generate_sitemap():
    print("Generating sitemap.xml...")
    xml_entries = []

    for fpath, meta in CANONICAL_PAGES.items():
        if fpath in ["coming-soon.html", "404.html"]:
            continue
        page_url = f"{BASE_URL}/{meta['path']}" if meta['path'] else f"{BASE_URL}/"
        xml_entries.append(f"""  <url>
    <loc>{page_url}</loc>
    <lastmod>2026-11-09</lastmod>
    <changefreq>{meta['changefreq']}</changefreq>
    <priority>{meta['priority']}</priority>
  </url>""")

    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(xml_entries) + "\n</urlset>\n"

    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"✓ Created sitemap.xml with {len(xml_entries)} verified public routes.")

    # Update robots.txt
    with open("robots.txt", "r", encoding="utf-8") as f:
        rtxt = f.read()

    rtxt = rtxt.replace("# Sitemap: https://ecocaregh.com/sitemap.xml", "Sitemap: https://ecocaregh.com/sitemap.xml")
    if "Sitemap: https://ecocaregh.com/sitemap.xml" not in rtxt:
        rtxt += "\nSitemap: https://ecocaregh.com/sitemap.xml\n"

    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(rtxt)
    print("✓ Updated robots.txt with active Sitemap directive.")


if __name__ == "__main__":
    fix_html_lang_and_metadata()
    generate_sitemap()
    print("All SEO & accessibility enhancements applied successfully!")

