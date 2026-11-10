#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Single-Source-of-Truth SEO & Accessibility Engine
Refactored to be 100% idempotent, reading metadata and schema specifications strictly from data/seo-pages.json.
Enforces:
  1. lang="en-GH" across all HTML pages.
  2. Non-duplicated OpenGraph & Twitter metadata with absolute URLs.
  3. Structured Data JSON-LD (LocalBusiness, WebSite, Service, FAQPage, BreadcrumbList).
  4. Form control accessibility (aria-label).
  5. State B Canonical sitemap.xml and robots.txt generation.
"""

import json
import os
import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = ROOT_DIR / "data" / "seo-pages.json"

def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def build_schema_json_ld(page_key, page_meta, manifest):
    base_url = manifest["base_url"]
    org_id = f"{base_url}/#organization"
    schema_type = page_meta.get("schema_type", "WebPage")
    graph = []

    # Homepage: LocalBusiness & WebSite
    if page_key == "index.html":
        company = manifest["company_contact"]
        local_business = {
            "@type": ["LocalBusiness", "CleaningService"],
            "@id": org_id,
            "name": manifest["site_name"],
            "legalName": manifest["legal_name"],
            "url": f"{base_url}/",
            "logo": manifest["default_og_image"],
            "image": manifest["default_og_image"],
            "description": page_meta["description"],
            "telephone": [company["phone_primary"], company["phone_secondary"]],
            "email": company["email"],
            "address": {
                "@type": "PostalAddress",
                "streetAddress": company["address_street"],
                "addressLocality": company["address_locality"],
                "addressRegion": company["address_region"],
                "addressCountry": company["address_country"]
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": company["geo_lat"],
                "longitude": company["geo_lng"]
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
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoClean Residential & Commercial Janitorial", "url": f"{base_url}/cleaning"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Eco-Laundry Doorstep Wash, Iron & Dry Cleaning", "url": f"{base_url}/laundry"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "EcoFumes Regulated Pest Control & Fumigation", "url": f"{base_url}/pest-control"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Carpet Deep Steam Extraction & Stain Treatment", "url": f"{base_url}/carpet-cleaning"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Upholstery & Leather Furniture Deep Sanitization", "url": f"{base_url}/upholstery-cleaning"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Polytank & Water Storage Tank Hygienic Cleaning", "url": f"{base_url}/polytank-cleaning"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Mobile Car Detailing & Cleaning (Interior & Exterior)", "url": f"{base_url}/car-interior-cleaning"}},
                    {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Professional Electrostatic Microfiber Dusting Services", "url": f"{base_url}/professional-dusting"}}
                ]
            },
            "sameAs": manifest["social_links"]
        }
        website = {
            "@type": "WebSite",
            "@id": f"{base_url}/#website",
            "url": f"{base_url}/",
            "name": manifest["site_name"],
            "publisher": {"@id": org_id},
            "inLanguage": manifest["default_lang"]
        }
        graph.extend([local_business, website])

    # Service Detail Pages
    elif schema_type == "Service":
        service_node = {
            "@type": "Service",
            "@id": f"{page_meta['canonical_url']}#service",
            "name": page_meta["title"].split(" | ")[0],
            "serviceType": page_meta.get("service_type", "Professional Cleaning"),
            "provider": {"@id": org_id},
            "description": page_meta["description"],
            "areaServed": {
                "@type": "AdministrativeArea",
                "name": "Greater Accra Region, Ghana"
            },
            "url": page_meta["canonical_url"]
        }
        graph.append(service_node)

    # FAQ Page
    elif schema_type == "FAQPage":
        faq_node = {
            "@type": "FAQPage",
            "@id": f"{page_meta['canonical_url']}#faq",
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
        }
        graph.append(faq_node)

    # About Page
    elif schema_type == "AboutPage":
        about_node = {
            "@type": "AboutPage",
            "@id": f"{page_meta['canonical_url']}#about",
            "url": page_meta["canonical_url"],
            "name": page_meta["title"],
            "mainEntity": {"@id": org_id}
        }
        graph.append(about_node)

    # Contact Page
    elif schema_type == "ContactPage":
        contact_node = {
            "@type": "ContactPage",
            "@id": f"{page_meta['canonical_url']}#contact",
            "url": page_meta["canonical_url"],
            "name": page_meta["title"],
            "mainEntity": {"@id": org_id}
        }
        graph.append(contact_node)

    # Add BreadcrumbList if breadcrumbs defined
    if page_meta.get("breadcrumb"):
        items = []
        for idx, bc in enumerate(page_meta["breadcrumb"], start=1):
            items.append({
                "@type": "ListItem",
                "position": idx,
                "name": bc["name"],
                "item": bc["url"]
            })
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{page_meta['canonical_url']}#breadcrumb",
            "itemListElement": items
        })

    if not graph:
        return ""

    schema_obj = {
        "@context": "https://schema.org",
        "@graph": graph
    }
    json_str = json.dumps(schema_obj, indent=2, ensure_ascii=False)
    return f"""    <!-- Schema.org JSON-LD Structured Data -->
    <script type="application/ld+json">
{json_str}
    </script>"""

def sanitize_and_enhance_html():
    manifest = load_manifest()
    pages = manifest["pages"]
    base_url = manifest["base_url"]
    site_name = manifest["site_name"]
    lang = manifest["default_lang"]
    default_img = manifest["default_og_image"]

    all_html_files = list(ROOT_DIR.glob("*.html"))
    enhanced_count = 0

    for file_path in all_html_files:
        f_name = file_path.name
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Enforce lang="en-GH"
        content = re.sub(r'<html\s+class="([^"]*)"\s+lang="[^"]*"', rf'<html class="\1" lang="{lang}"', content)
        content = re.sub(r'<html\s+lang="[^"]*"', rf'<html lang="{lang}"', content)

        # 2. Canonical pages enhancement
        if f_name in pages:
            meta = pages[f_name]
            page_url = meta["canonical_url"]
            title = meta["title"]
            desc = meta["description"]
            robots_val = meta.get("robots", "index, follow")

            # Clean out any old/previous metadata blocks (ensuring 100% idempotency)
            content = re.sub(r'\s*<!--\s*Canonical & Social Metadata.*?-->\s*(<link rel="canonical"[^>]*>)?(\s*<meta property="og:[^>]*>|\s*<meta name="twitter:[^>]*>)*', '', content, flags=re.DOTALL)
            content = re.sub(r'\s*<!--\s*Schema\.org JSON-LD Structured Data.*?-->\s*<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'\s*<link rel="canonical"[^>]*>', '', content)
            content = re.sub(r'\s*<meta property="og:[^>]*>', '', content)
            content = re.sub(r'\s*<meta name="twitter:[^>]*>', '', content)
            content = re.sub(r'\s*<meta name="robots"[^>]*>', '', content)

            # Update or insert <title>
            if "<title>" in content:
                content = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', content, count=1)
            else:
                content = content.replace("<head>", f"<head>\n    <title>{title}</title>", 1)

            # Update or insert <meta name="description">
            if '<meta name="description"' in content:
                content = re.sub(r'<meta\s+name="description"\s+content="[^"]*"[^>]*>', f'<meta name="description" content="{desc}">', content, count=1)
            else:
                content = content.replace("</title>", f'</title>\n    <meta name="description" content="{desc}">', 1)

            # Assemble clean Canonical & Social Block
            meta_block = f"""    <meta name="robots" content="{robots_val}">
    <!-- Canonical & Social Metadata (OpenGraph & Twitter Card) -->
    <link rel="canonical" href="{page_url}">
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:site_name" content="{site_name}">
    <meta property="og:image" content="{default_img}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:image:alt" content="{site_name} Branding">
    <meta property="og:locale" content="{lang}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{default_img}">
    <meta name="twitter:image:alt" content="{site_name} Branding">"""

            # Build Schema.org JSON-LD
            schema_block = build_schema_json_ld(f_name, meta, manifest)
            full_head_addition = meta_block
            if schema_block:
                full_head_addition += f"\n{schema_block}"

            content = content.replace("</head>", f"{full_head_addition}\n</head>")

        # 3. Form Accessibility (aria-label)
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

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        enhanced_count += 1

    print(f"✓ Processed and verified {enhanced_count} HTML files with manifest-driven SEO, lang='{lang}', and schema.")

def generate_full_site_sitemap_and_robots():
    manifest = load_manifest()
    pages = manifest["pages"]
    base_url = manifest["base_url"]

    sitemap_entries = []
    for f_name, meta in pages.items():
        if meta.get("in_sitemap", False):
            sitemap_entries.append(f"""  <url>
    <loc>{meta['canonical_url']}</loc>
    <lastmod>2026-11-09</lastmod>
    <changefreq>{meta.get('changefreq', 'weekly')}</changefreq>
    <priority>{meta.get('priority', '0.8')}</priority>
  </url>""")

    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
""" + "\n".join(sitemap_entries) + "\n</urlset>\n"

    sitemap_file = ROOT_DIR / "sitemap.xml"
    with open(sitemap_file, "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print(f"✓ Generated canonical sitemap.xml with {len(sitemap_entries)} verified indexable routes.")

    # Update root robots.txt
    robots_file = ROOT_DIR / "robots.txt"
    robots_content = f"""User-agent: *
Allow: /

# Canonical Sitemap
Sitemap: {base_url}/sitemap.xml
"""
    with open(robots_file, "w", encoding="utf-8") as f:
        f.write(robots_content)
    print(f"✓ Generated root robots.txt pointing to {base_url}/sitemap.xml.")

if __name__ == "__main__":
    sanitize_and_enhance_html()
    generate_full_site_sitemap_and_robots()
    print("EcoCare SEO & Accessibility optimization complete!")
