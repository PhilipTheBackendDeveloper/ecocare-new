# EcoCare Cleaning Services — Master Content Mapping Specification (`CONTENT_MAPPING.md`)

**Document Version:** 1.0  
**Date:** 8 November 2026  
**Status:** Canonical Content Mapping Specification  

---

## 1. Content Categories & Mapping Matrix

Every piece of information from `ECOCARE_CONTENT_DATA.json` and `ECOCARE_MASTER_KNOWLEDGE_BASE.md` is mapped to an exact page, component, and HTML selector, with its editorial disposition noted:

### 1.1 Corporate Identity & Leadership

| Knowledge Base Item | Source Data | Disposition | Destination Page | Target Selector / Component | Rendered Implementation Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Brand Name** | "EcoCare Cleaning Services Limited" | **APPROVED** | Global (all pages) | `<title>`, navbar brand, footer | "EcoCare Cleaning Services Limited" & "EcoCare" |
| **Tagline 1** | "Protect the Environment, Live Better, Prolong Life." | **APPROVED** | Homepage, About, Footer | Hero subtext, footer company overview | Heritage brand slogan preserved faithfully |
| **Tagline 2** | "You got dirt? We got Clean." | **APPROVED** | Homepage, Services banner | `.slider-sub-text`, service callout | Retained as punchy operational tagline |
| **Incorporation** | Claimed Sept 19, 2014 (Ghanaian Companies Code 1963) | **QUALIFIED** | `about1.html` | `.about-box-layout1 .item-subtitle` | Framed as corporate milestone: "Delivering professional residential and commercial cleaning across Ghana since 2014." |
| **Founder / CEO** | Eric Nana Acquah (CEO & Founder) | **APPROVED** | `about1.html`, `team1.html` | `.team-box-layout1`, About narrative | Featured as Chief Executive Officer & Founder |
| **Co-Founder** | Margaret Owusua (Boakye vs. Acquah) | **HELD (CA-02)**| `about1.html` | General Management Team | Disputed surname omitted; featured under executive team role |

---

### 1.2 Contact & Digital Channels

| Knowledge Base Item | Source Data | Disposition | Destination Page | Target Selector / Component | Rendered Implementation Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Physical Address**| "Achimota Mile 7, Accra, Ghana" | **APPROVED** | Global Header, Footer, `contact.html` | `#header-topbar`, `.footer-box-layout1`, `.contact-info` | Displayed with Ghana location marker |
| **Phone Line 1** | `+233 24 901 4253` | **APPROVED** | Global Topbar, Header CTA, Footer, `contact.html` | `<a href="tel:+233249014253">` | Click-to-call link formatted with no spaces in `href` |
| **Phone Line 2** | `+233 24 380 7100` | **APPROVED** | Global Topbar, `contact.html` | `<a href="tel:+233243807100">` | Secondary active operational phone |
| **Primary Email** | `ecocaregh1on1@gmail.com` | **APPROVED** | Global Topbar, Footer, `contact.html` | `<a href="mailto:ecocaregh1on1@gmail.com">` | Verified active Google Workspace / Gmail |
| **Branded Email** | `info@ecocaregh.com` | **HELD (CA-01)**| None (omitted from links) | Internal reference | Omitted from clickable links until domain renewal & MX verification |
| **Facebook** | `facebook.com/profile.php?id=100006412849415` | **APPROVED** | Header, Footer, `contact.html` | `.social-icon a[href*="facebook"]` | Linked directly to official profile |
| **TikTok** | `tiktok.com/@ecocarecompanylimited` | **APPROVED** | Header, Footer, `contact.html` | `.social-icon a[href*="tiktok"]` | Linked to official company account |
| **YouTube** | `youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA` | **APPROVED** | Header, Footer, `contact.html` | `.social-icon a[href*="youtube"]` | Linked to official channel |
| **Google Maps** | Lat 5.6278, Long -0.2441 (EcoCare Laundry Mile 7) | **APPROVED** | `contact.html` | `.google-map-area` | Responsive iframe embed (replaces demo API key) |

---

### 1.3 Five Core Service Families

| Service Family | Brand Label | Destination Route | Dedicated Page Sections | Subservices Included |
| :--- | :--- | :--- | :--- | :--- |
| **1. Cleaning** | `EcoClean` | `single-service1.html` (`cleaning.html`) | Hero, Overview, 6 Subservice Cards, Equipment & Hygiene Process, Sibling Services Sidebar, Quote CTA | Home/House Cleaning, Office Cleaning, Commercial Cleaning, Industrial Cleaning, Post-Construction, Move-in/Move-out, Window & High Glass, Tile/Marble Polishing, Event Clean-Up |
| **2. Laundry** | `Eco-Laundry`| `single-service2.html` (`laundry.html`) | Hero, Garment Care Protocols, Pickup & Delivery scheduling notice, Parameters Sidebar, Quote CTA | Washing & Ironing, Delicate Fabric Care, Dry Cleaning, Linen & Bedding Services, Commercial Uniform Laundry |
| **3. Fumigation** | `EcoFumes` | `pest-control.html` | Hero, Pest Species Guide, Commercial/Residential Protocols, Safety & Evacuation Checklist, Inquiry Form | Termite Treatments, Cockroach Eradication, Rodent Extermination, Mosquito & Bed Bug Fogging, Preventive Warehouse Treatments |
| **4. Carpet Care** | `EcoCare Carpet`| `carpet-cleaning.html`| Hero, Deep Extraction Walkthrough, Stain & Odor Treatment, Fiber Care Advice, Package Options | Deep Hot-Water Extraction, Spot & Stain Pretreatment, Encapsulation Dry Cleaning, Deodorization, High-Traffic Commercial Maintenance |
| **5. Upholstery** | `EcoCare Upholstery`| `upholstery-cleaning.html`| Hero, Fabric & Leather Treatment, Mattress Hygiene, Sanitization Process, Quote CTA | Sofa & Couch Deep Clean, Dining Chair Fabric Care, Mattress Sanitization & Dust Mite Removal, Leather Conditioning |

---

### 1.4 Twelve Historic Service Listings (Directory Mapping)

| # | Historic Service Listing Label | Target Service Family | Canonical Destination URL | Dedicated Flaticon Icon Class |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Office Cleaning** | Cleaning (`EcoClean`) | `single-service1.html#office` | `.flaticon-vacuum` |
| 2 | **Commercial Cleaning** | Cleaning (`EcoClean`) | `single-service1.html#commercial` | `.flaticon-tower` |
| 3 | **Washing and Ironing** | Laundry (`Eco-Laundry`) | `single-service2.html#washing` | `.flaticon-clean-1` |
| 4 | **Upholstery Cleaning** | Upholstery (`EcoCare`) | `upholstery-cleaning.html` | `.flaticon-clean` |
| 5 | **House Cleaning Services** | Cleaning (`EcoClean`) | `single-service1.html#residential` | `.flaticon-clean-2` |
| 6 | **House & Office Fumigation** | Pest Control (`EcoFumes`) | `pest-control.html` | `.flaticon-clean-3` |
| 7 | **Industrial Cleaning** | Cleaning (`EcoClean`) | `single-service1.html#industrial` | `.flaticon-brush` |
| 8 | **Carpet Cleaning** | Carpet (`EcoCare`) | `carpet-cleaning.html` | `.flaticon-mop` |
| 9 | **Floor Cleaning (Marble, Tiles & Grout)** | Cleaning (`EcoClean`) | `single-service1.html#floor` | `.flaticon-mop` |
| 10 | **General Cleaning** | Cleaning (`EcoClean`) | `single-service1.html#general` | `.flaticon-shower` |
| 11 | **Window and Glass Cleaning** | Cleaning (`EcoClean`) | `single-service1.html#window` | `.flaticon-tower` |
| 12 | **Event Clean-Up Services** | Cleaning (`EcoClean`) | `single-service1.html#event` | `.flaticon-calendar` |

---

### 1.5 Omitted & Held Content Registry

| Item Description | Original Location | Status | Exact Reason for Omission from Public Build |
| :--- | :--- | :--- | :--- |
| **8 Customer Reviews** | Old site homepage / about | **HELD** | Customer identities and testimonials require client verification before publishing (see `CONTENT_APPROVAL_TODO.md` CA-09). |
| **Demo Pricing (\$49, \$99, \$199)** | Clenix `pricing-table.html` | **REMOVED** | Replaced with non-fixed scope packages and custom quote inquiries (see CA-03). |
| **Demo Staff Cutout Models** | Clenix `team1.html` / `img/team/` | **REMOVED** | Clenix cutout stock models must not be presented as EcoCare employees. Replaced with authentic leadership and team overview. |
| **Demo Partner Logos** | Clenix `brand*.png` | **REMOVED** | ThemeForest template logos removed. |
| **Fictional Milestones ("2583+ Clients")** | Clenix `index.html` `.counter` | **REMOVED** | Replaced with verified service highlights (see CA-10). |
| **"100% Baby/Pet Safe" Pest Claims** | Old fumigation page | **REMOVED** | Unverified safety claims omitted in favor of professional safety intervals (see CA-04). |
| **E-Commerce Shop & Blog** | `shop.html`, `blog1.html` | **DEPRECATED** | EcoCare does not operate an approved public online store or editorial blog. Excluded from public navigation. |
| **`popper.html`** | Root directory | **DELETED** | Scraped 99KB WordPress 404 error page removed. |
| **Cloudflare Beacon** | Near `</body>` in HTML pages | **DELETED** | Tracking beacon sending analytics to template author removed. |

