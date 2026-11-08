# Clenix Cleaning Services Template — Architecture & Component Inventory

**Generated on:** 8 November 2026  
**Project:** EcoCare Cleaning Services Ltd  
**Template Source:** Clenix - Cleaning Company & Services HTML5 Template (RadiusTheme)  
**Document Purpose:** Complete architectural audit, component catalog, asset inventory, and implementation guide for the Clenix template codebase located in the root workspace. Use this alongside `knowledge.md` (EcoCare's business data) to construct and customize the new EcoCare website.

---

## Table of Contents

1. [Executive Summary & Core Tech Stack](#1-executive-summary--core-tech-stack)
2. [Workspace File & Directory Architecture](#2-workspace-file--directory-architecture)
3. [Design System, Color Palette & Typography](#3-design-system-color-palette--typography)
4. [Master Page-by-Page Catalog (26 HTML Screens)](#4-master-page-by-page-catalog-26-html-screens)
   - [4.1 Homepage Variations (4 screens)](#41-homepage-variations-4-screens)
   - [4.2 About Us Pages (2 screens)](#42-about-us-pages-2-screens)
   - [4.3 Service Pages (4 screens)](#43-service-pages-4-screens)
   - [4.4 Projects & Portfolio (2 screens)](#44-projects--portfolio-2-screens)
   - [4.5 Team Pages (3 screens)](#45-team-pages-3-screens)
   - [4.6 Pricing & Booking Forms (2 screens)](#46-pricing--booking-forms-2-screens)
   - [4.7 FAQ Page (1 screen)](#47-faq-page-1-screen)
   - [4.8 Shop & E-Commerce (2 screens)](#48-shop--e-commerce-2-screens)
   - [4.9 Blog & News Pages (3 screens)](#49-blog--news-pages-3-screens)
   - [4.10 Contact Page (1 screen)](#410-contact-page-1-screen)
   - [4.11 Utility Pages (2 screens)](#411-utility-pages-2-screens)
   - [4.12 Extraneous Artifact: `popper.html`](#412-extraneous-artifact-popperhtml)
5. [UI Component Library & Layout Classes](#5-ui-component-library--layout-classes)
   - [5.1 Navigation & Header Styles](#51-navigation--header-styles)
   - [5.2 Box Layout Components (45+ Variants)](#52-box-layout-components-45-variants)
   - [5.3 Sidebar Widgets](#53-sidebar-widgets)
   - [5.4 Button & Action Styles](#54-button--action-styles)
   - [5.5 CSS Helper & Utility Classes](#55-css-helper--utility-classes)
6. [Interactive Features & JavaScript Plugins](#6-interactive-features--javascript-plugins)
7. [Icon Sets & Typography Assets](#7-icon-sets--typography-assets)
   - [7.1 Dedicated Cleaning Flaticon Font](#71-dedicated-cleaning-flaticon-font)
   - [7.2 FontAwesome 5 Free](#72-fontawesome-5-free)
8. [Media & Image Assets Inventory](#8-media--image-assets-inventory)
9. [EcoCare Mapping & Production Readiness Gap Analysis](#9-ecocare-mapping--production-readiness-gap-analysis)

---

## 1. Executive Summary & Core Tech Stack

The Clenix template is a specialized, responsive HTML5/CSS3 corporate website template built specifically for commercial, residential, and industrial cleaning services, janitorial companies, and facility maintenance providers.

### Core Specifications
- **Template Name:** Clenix - Cleaning Company & Cleaning Services HTML Template
- **Author:** RadiusTheme (Version 1.0)
- **CSS Framework:** Bootstrap 4.3.1 (`css/bootstrap.min.css`)
- **Base Reset:** Normalize.css (`css/normalize.css`), modern CSS3 box-sizing
- **Primary Script Core:** jQuery v3.3.1 (`js/jquery-3.3.1.min.js`), Popper.js (`js/popper.min.js`), Modernizr 3.7.1 (`js/modernizr-3.7.1.min.js`)
- **Slider Engines:** Nivo Slider (`vendor/slider/`), Owl Carousel 2 (`vendor/OwlCarousel/`)
- **Key Enhancements:** ElevateZoom (product zoom), Magnific Popup (video lightbox), Isotope & ImagesLoaded (filterable masonry gallery), MeanMenu (responsive mobile menu), Select2 (custom form selects), DateTimePicker (interactive booking calendar), Waypoints & CounterUp (animated metrics counters), Validator (client-side form validation).

---

## 2. Workspace File & Directory Architecture

```
/Users/apple/Developer/work/ecocare/
├── 404.html                     # 404 Error page with illustration & search box
├── about1.html                  # About Us variation 1 (History, Team, Stats, Video CTA)
├── about2.html                  # About Us variation 2 (Pricing, Process Steps, Partners)
├── blog1.html                   # Blog layout 1 (3-column grid)
├── blog2.html                   # Blog layout 2 (Standard listing with right sidebar)
├── calculate-form.html          # Interactive Quote Calculation & Booking Form
├── coming-soon.html             # Maintenance / Launch page with countdown clock
├── contact.html                 # Contact Us page (Google Map, info cards, contact form)
├── faq.html                     # FAQ page (Accordion cards + sidebar inquiry form)
├── index.html                   # Homepage Variation 1 (Comprehensive full-service layout)
├── index2.html                  # Homepage Variation 2 (Process-focused with Brand carousel)
├── index3.html                  # Homepage Variation 3 (Middlebar header + Projects gallery)
├── index4.html                  # Homepage Variation 4 (High-impact residential/commercial)
├── knowledge.md                 # EcoCare Cleaning Services Ltd — Existing Website Knowledge Bank
├── popper.html                  # [ARTIFACT] Scraped WordPress 404 error page (Safe to delete)
├── pricing-table.html           # 3-Tier service pricing packages comparison
├── project1.html                # Portfolio / Project gallery
├── service1.html                # Services layout 1 (Icon-driven grid)
├── service2.html                # Services layout 2 (Card-driven grid with Process section)
├── shop.html                    # E-Commerce store (Grid/List switcher, product filters)
├── single-blog1.html            # Single blog post detail with comments & sidebar
├── single-product.html          # Single store product with ElevateZoom & reviews
├── single-project1.html         # Single case study / project detail page
├── single-service1.html         # Single service detail (Category sidebar + Download brochure)
├── single-service2.html         # Single service detail (Service-info sidebar + Booking widget)
├── single-team.html             # Single staff member profile with progress bars & bio
├── style.css                    # Main template stylesheet (8,200+ lines, fully indexed)
├── team1.html                   # Team layout 1 (Full photo cards with social overlays)
├── team2.html                   # Team layout 2 (Clean circular avatar cards)
├── template-inventory.md        # This document
│
├── css/                         # Stylesheets
│   ├── animate.min.css          # CSS3 animations (fade, bounce, zoom, slide)
│   ├── bootstrap.min.css        # Bootstrap 4.3.1 grid and components
│   ├── fontawesome-all.min.css  # FontAwesome 5 Free font icons
│   ├── jquery.datetimepicker.css# Styling for appointment date/time picker
│   ├── magnific-popup.css       # Lightbox modal styles
│   ├── main.css                 # HTML5 Boilerplate base helpers
│   ├── meanmenu.min.css         # Off-canvas / mobile menu styling
│   ├── normalize.css            # Browser reset
│   └── select2.min.css          # Customized select dropdown styles
│
├── js/                          # JavaScript Libraries and scripts
│   ├── bootstrap.min.js         # Bootstrap UI interactive plugins
│   ├── imagesloaded.pkgd.min.js # Image load detection for masonry grids
│   ├── isotope.pkgd.min.js      # Filterable gallery and grid layout
│   ├── jquery-3.3.1.min.js      # jQuery core library
│   ├── jquery.countdown.min.js  # Countdown timer engine (Coming soon page)
│   ├── jquery.counterup.min.js  # Animated numerical counter
│   ├── jquery.datetimepicker.full.min.js # Date & time picker plugin
│   ├── jquery.elevatezoom.js    # Image zoom lens for products
│   ├── jquery.magnific-popup.min.js # Video & image modal popups
│   ├── jquery.meanmenu.min.js   # Mobile responsive navigation
│   ├── main.js                  # Master template initialization & event binding
│   ├── modernizr-3.7.1.min.js   # Browser feature detection
│   ├── plugins.js               # Console polyfill and helper plugins
│   ├── popper.min.js            # Tooltip & dropdown positioning engine
│   ├── select2.min.js           # Enhanced select inputs
│   ├── validator.min.js         # Form field validation engine
│   └── waypoints.min.js         # Scroll triggers for counter & sticky header
│
├── font/                        # Custom Flaticon cleaning icon font
│   ├── flaticon.css             # Flaticon CSS selectors (`.flaticon-*`)
│   ├── Flaticon.eot, .svg, .ttf, .woff, .woff2 # Font binary assets
│
├── webfonts/                    # FontAwesome 5 Free webfont binaries
│   ├── fa-brands-400.*          # Social and brand icons
│   ├── fa-regular-400.*         # Outlined icons
│   └── fa-solid-900.*           # Solid UI icons
│
├── vendor/                      # Third-party vendor sliders
│   ├── OwlCarousel/             # Carousel component (Testimonials, Brands, Team)
│   │   ├── owl.carousel.min.css
│   │   ├── owl.carousel.min.js
│   │   ├── owl.theme.default.min.css
│   │   └── owl.video.play.png
│   └── slider/                  # Nivo Slider component (Homepage Hero Banners)
│       ├── css/nivo-slider.css  # Nivo Slider transitions & controls
│       ├── js/jquery.nivo.slider.js # Nivo Slider script engine
│       └── home.js              # Slider configuration presets (sliders 1 to 5)
│
└── img/                         # Graphic and photographic assets (145+ files)
    ├── favicon.png              # 16x16 / 32x32 Favicon icon
    ├── logo-dark.png            # Main primary navbar logo (dark blue text)
    ├── logo-dark2.png           # Alternative layout logo
    ├── large-logo.png           # High-resolution footer/brand logo
    ├── preloader.gif            # Animated page load spinner
    ├── brand/                   # 9 partner/certification logo placeholders
    ├── blog/                    # 18 editorial blog photos (thumbnails & large)
    ├── figure/                  # 72 graphic shapes, bubbles, 404 art, banners
    ├── project/                 # 8 project/case study photos
    ├── service/                 # 12 high-resolution service photos
    ├── slider/                  # 9 hero background images (1920x800)
    └── team/                    # 14 staff portraits (cutout PNGs with transparent bg)
```

---

## 3. Design System, Color Palette & Typography

### 3.1 Color Palette

The template uses a modern, high-trust hygiene palette dominated by navy blue, dodger blue, and vibrant yellow:

| Color Role | Hex Code | Utility Class | Usage in Template |
| :--- | :--- | :--- | :--- |
| **Primary Navy** | `#14287b` | `.bg-Primary` | Topbars, headers, footer backgrounds, major headings (`h1`–`h6`), brand accents |
| **Light Primary / Action** | `#287ff9` | `.bg-lightprimary` | Primary action buttons, active menu states, link hovers, active badges |
| **Bright Accent Yellow** | `#fef22e` | `.bg-accent` | Callout buttons ("Book Now", "Read More"), rating stars, discount badges |
| **Dark Body Text** | `#111111` / `#444444` | `.text-dark` | Form inputs, bold paragraphs, sub-headings |
| **Muted Paragraph Text** | `#646464` | default `p` | Standard body copy, descriptions, metadata |
| **Light Neutral Background**| `#f8f8f8` | `.bg-assh` | Alternating section backgrounds, service cards |
| **Soft Cool Background** | `#f9fafc` | `.bg-aash` | Alternate cards, why-choose-us cards |
| **Border Gray** | `#e1e1e1` / `#e8e8e8`| `.border-aash` | Card borders, table dividers, form input strokes |
| **Pure White** | `#ffffff` | `.bg-white` | Card backgrounds, sticky header bar, contrast text |

### 3.2 Typography System

- **Primary Headings Font:** `'Poppins', sans-serif` (Imported weights: 300, 400, 500, 600, 700, 800, 900)
  - `h1`: 46px (Desktop) -> 28px (Mobile), Line height: 48px
  - `h2`: 36px (Desktop) -> 26px (Mobile), Line height: 48px
  - `h3`: 22px (Desktop) -> 20px (Mobile), Line height: 30px
  - `h4`: 20px, `h5`: 18px, `h6`: 16px
- **Body & Paragraph Font:** `'Roboto', sans-serif` (Imported weights: 300, 400, 500, 600, 700, 900)
  - Default size: `16px` (Desktop)
  - Line height: `30px`
  - Font smoothing: `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale;`
- **Responsive Font Scaling:**
  - Standard Desktop (`> 1200px`): `html { font-size: 62.5%; }` (1rem = 10px)
  - Laptops (`992px - 1199px`): `html { font-size: 60%; }`
  - Tablets (`768px - 991px`): `html { font-size: 55%; }`
  - Large Phones (`480px - 767px`): `html { font-size: 50%; }`
  - Small Phones (`< 480px`): `html { font-size: 45%; }`

---

## 4. Master Page-by-Page Catalog (26 HTML Screens)

### 4.1 Homepage Variations (4 screens)

All homepages feature sticky navigation, mobile MeanMenu support, animated scroll-up button, preloader, and a rich multi-row footer.

#### `index.html` (Home 1 — General Cleaning Flagship)
- **Header:** Topbar with contact hours, phone, email, and social icons. Navigation style `menu-layout1` with action button ("Get A Quote").
- **Hero Slider:** `ensign-nivoslider-4` with multi-slide transition, bold headlines, bullet tags, and CTA buttons.
- **Sections:**
  1. *About Us Area:* Two-column story with company credentials and checkmark list (`about-box-layout1`).
  2. *Service Area:* 6-card grid with icon graphics (`service-box-layout1`).
  3. *Call to Action Area:* Full-width navy banner with phone callout (`banner-box-layout1`).
  4. *About Us Feature:* Secondary layout with overlapping images and bullet points (`about-box-layout2`).
  5. *Banner Area:* Promo banner with 30% discount badge.
  6. *Pricing Table Area:* 3-column pricing cards (`pricing-box-layout1`).
  7. *Team Area:* 4-column team member showcase (`team-box-layout1`).
  8. *Progress Area:* 4-metric animated counter (`progress-box-layout1`) with satisfied clients, cleanings, staff, awards.
  9. *Testimonial Area:* Owl Carousel slider (`testimonial-box-layout1`).
  10. *Blog Area:* 3-card news grid with date badges and comment counts (`blog-box-layout1`).

#### `index2.html` (Home 2 — Commercial & Residential Focus)
- **Header:** Topbar with phone, email, and "Estimate" action link + navigation `menu-layout2`.
- **Hero Slider:** Full-width hero banner with custom slide transitions.
- **Sections:**
  1. *Why Choose Us Area:* 3-feature card strip directly below the slider (`why-choose-box-layout1`).
  2. *About Us Area:* Clean typography with circular progress indicators (`about-box-layout3`).
  3. *Service Area:* Service cards with photography backgrounds (`service-box-layout2`).
  4. *Banner Area:* Full-width background photo with video popup play button (`banner-box-layout2`).
  5. *Process Area:* 4-step linear workflow ("Book Online" -> "Get Confirmation" -> "Let's Clean" -> "Relax") (`process-box-layout1`).
  6. *Pricing Table Area:* Clean subscription / service packages.
  7. *Progress Area:* Metrics counter bar.
  8. *Team Area:* Staff showcase.
  9. *Testimonial Area:* Testimonial slider.
  10. *Blog Area:* Latest updates.
  11. *Brand Area:* Client / partner logos carousel (`brand-box-layout1`).

#### `index3.html` (Home 3 — Corporate & Facilities Management)
- **Header:** Header layout with Topbar + **Middlebar** (Logo on left, Phone, Email, Location widgets on right) + Bottom Main Navigation (`menu-layout3`).
- **Hero Slider:** Nivo Slider variation.
- **Sections:**
  1. *Brand Area:* Partner logo carousel right under slider.
  2. *Service Area:* Tabbed or categorized service offering (`service-box-layout3`).
  3. *About Us Area:* Corporate facilities overview (`about-box-layout4`).
  4. *Banner Area:* Emergency cleaning callout.
  5. *Team Area:* Staff grid.
  6. *Progress Area:* Corporate statistics counter.
  7. *Projects Area:* Filterable isotope portfolio gallery (`project-box-layout1`).
  8. *Testimonial Area:* Client quotes.
  9. *Blog Area:* Articles.
  10. *Action Area:* Bottom CTA banner (`action-box-layout1`).

#### `index4.html` (Home 4 — Modern Domestic Cleaners)
- **Header:** Topbar + Navigation `menu-layout1`.
- **Hero Slider:** Nivo Slider variation.
- **Sections:**
  1. *Why Choose Us Area:* 4-card feature layout (`why-choose-box-layout2`).
  2. *Service Area:* Interactive cards (`service-box-layout4`).
  3. *Banner Area:* Promotional callout.
  4. *Team Area:* Staff grid.
  5. *Progress Area:* Numerical milestones.
  6. *About Us Area:* Story section.
  7. *Testimonial Area:* Customer feedback.
  8. *Blog Area:* News articles.
  9. *Action Area:* Final conversion banner.

---

### 4.2 About Us Pages (2 screens)

#### `about1.html` (Company Story, Team, Milestones & Video)
- Breadcrumb header banner (`img/figure/breadcumb.jpg`).
- Company history story block with experience badge ("Doing Business Since 1992").
- Team members carousel with social links.
- Parallax banner with video modal popup (`popup-youtube`).
- 4-step "How It Works" process.
- Conversion Call to Action banner.

#### `about2.html` (Pricing, Workflow & Certifications)
- Breadcrumb banner.
- Two-column About section emphasizing affordable pricing and eco-friendly standards.
- 4-step Process layout (`process-box-layout1`).
- Promotional banner.
- Partner/Accreditation brand logo carousel (`brand-box-layout1`).

---

### 4.3 Service Pages (4 screens)

#### `service1.html` (Service Catalog — Icon Grid)
- 6-service grid featuring dedicated Flaticon icons, service titles, short descriptions, and "Read More" links.
- Services included: Kitchen Cleaning, Office Cleaning, Window Cleaning, Floor Cleaning, Plumbing Service, Car Wash.
- Bottom CTA banner: "Together We'll Explore New Things".

#### `service2.html` (Service Catalog — Photo Cards + Process)
- 6-service grid featuring high-quality photography, price tags, and read-more buttons.
- Integrated 4-step "How It Works" workflow section.
- Bottom CTA banner.

#### `single-service1.html` (Service Detail — Category Navigation Focus)
- Two-column layout (8 cols content, 4 cols sidebar).
- Main Content: Hero service photography, detailed text description, quality assurance bullet points, "Experienced Workers" highlight, embedded FAQ accordion for the specific service.
- Sidebar Widgets:
  - `widget-category`: List of all other services with active link indicator.
  - `widget-download`: PDF brochure download buttons ("Company Presentation", "Service Brochure").
  - `widget-contact-form`: Quick consultation form.
  - `widget-banner`: 30% discount promo banner with phone number.

#### `single-service2.html` (Service Detail — Information Card Focus)
- Main Content: Identical rich content block with quality guarantees and service-level FAQ.
- Sidebar Widgets:
  - `widget-service-info`: Key parameters box (Working Hours: 08:00 - 18:00, Pricing: From \$50, Category: Residential, Location, Phone).
  - `widget-download`: PDF download buttons.
  - `widget-contact-form`: Quick booking form.
  - `widget-banner`: Promo banner.

---

### 4.4 Projects & Portfolio (2 screens)

#### `project1.html` (Project Portfolio Gallery)
- 6-project grid showcasing before/after and completed client jobs: Window Cleaning, Office Cleaning, Floor Cleaning, Bedroom Cleaning, Kitchen, Car Wash.
- Card hover overlays displaying project title, category, and direct link.

#### `single-project1.html` (Project Case Study Detail)
- Hero project photography.
- Detailed case study sections:
  - "Project Description"
  - "Challenges"
  - "Solutions & Execution"
- Sidebar: Project Information widget (Client name, Date, Category, Location, Value, Duration) + promotional discount banner.

---

### 4.5 Team Pages (3 screens)

#### `team1.html` (Staff Grid — Full Portrait Cards)
- 8-member team grid (`team-box-layout1`).
- Cards feature photo, staff name, designation (e.g., "Supervisor", "Cleaner", "Manager"), and hover social icon bar (Facebook, Twitter, LinkedIn, Instagram).

#### `team2.html` (Staff Grid — Circular Avatar Cards)
- 8-member team grid (`team-box-layout2`).
- Minimalist card layout with circular portraits, badges, and clean social icons.

#### `single-team.html` (Staff Member Profile)
- Detailed employee profile layout (`single-team-box-layout1`).
- Left column: Staff photograph, direct phone number, email address, social links.
- Right column: Full biography, experience narrative, and animated skill/competency progress bars (e.g., "Cleaning Expertise: 90%", "Customer Satisfaction: 95%").

---

### 4.6 Pricing & Booking Forms (2 screens)

#### `pricing-table.html` (Service Pricing Plans)
- 3-tier pricing comparison cards:
  - **Basic Plan (\$49):** 1 Bedroom, 1 Bathroom, Living Room, Dusting, Mopping.
  - **Standard Plan (\$99):** 2-3 Bedrooms, 2 Bathrooms, Full Kitchen Deep Clean, Vacuuming.
  - **Premium Plan (\$199):** Full House/Office, All Rooms, Carpet & Upholstery, Window Exterior, Sanitization.
- Feature lists with included/excluded indicators and "Order Now" action buttons.

#### `calculate-form.html` (Interactive Cost Calculation & Booking Form)
- Two-column interactive layout:
  - Left column: "Quick Calculate & Book Your Desired Service" explainer with trust badges ("Customer Focused Reviews", "We Are Committed", "Regular & Monthly Cleaning").
  - Right column: Complete multi-input booking calculator:
    - Service Category (`select.select2`): Residential, Commercial, Plot, Apartment.
    - Property Type (`select.select2`).
    - Approximate Square Footage (`select.select2`): 200, 300, 400, 600 SF.
    - Number of Bedrooms (`select.select2`).
    - Number of Bathrooms (`select.select2`).
    - Frequency (`select.select2`): One-time, Weekly, Bi-weekly, Monthly.
    - Postal / ZIP Code (`input[type="text"]`).
    - Preferred Appointment Date (`input.rt-date` with DateTimePicker).
    - Preferred Appointment Time (`input.rt-time` with DateTimePicker).
    - Client Full Name, Phone Number, Email Address.
    - Full Street Address / Notes (`textarea`).
    - Submit Button: "Book Now" (`button[type="submit"]`).

---

### 4.7 FAQ Page (1 screen)

#### `faq.html` (Frequently Asked Questions)
- Full 9-item collapsible Bootstrap accordion (`#accordion`):
  1. *Do I have to sign a contract?*
  2. *Will I always have the same house cleaner?*
  3. *Do you guarantee your work?*
  4. *How can I make a payment?*
  5. *What is your cancellation policy?*
  6. *Are your cleaning products pet- and eco-friendly?*
  7. *What are your pricing plan rules?*
  8. *I need more help / customized service*
  9. *Can I skip or reschedule bookings?*
- Right sidebar: Dedicated question inquiry form widget (`widget-contact-form`) with user icon, email icon, message box, and send button.

---

### 4.8 Shop & E-Commerce (2 screens)

#### `shop.html` (Cleaning Products Storefront)
- Interactive layout switcher: Grid view vs. List view (`.product-view-trigger`).
- Item sorting dropdown ("Sort by popularity", "Sort by price", "Sort by latest").
- Product card grid featuring:
  - Product image (`img/figure/product*.png`).
  - Star rating review display (`5/5 stars`).
  - Product title (Detergents, Floor Cleaners, Glass Cleaners).
  - Price display (`$25.00`).
  - Hover action buttons: "Add to Cart", "Wishlist", "Quick View".
- Standard numbered pagination bar (`.pagination-layout1`).

#### `single-product.html` (Product Detail & Specifications)
- Product imagery section with active ElevateZoom lens effect (`.zoom_01`).
- Quantity selector with increment/decrement buttons (`.quantity-plus`, `.quantity-minus`).
- "Add to Cart" and "Buy Now" buttons.
- Tabbed specifications panel:
  - Tab 1: Description.
  - Tab 2: Additional Information (Weight, Dimensions, Chemical Composition).
  - Tab 3: Customer Reviews & Star Rating Form.
- "Related Products" carousel at the bottom.

---

### 4.9 Blog & News Pages (3 screens)

#### `blog1.html` (Blog Listing — 3-Column Grid)
- 6-article grid with responsive thumbnail images, publishing dates, author names, category tags, titles, excerpts, and "Read More" links.
- Numbered pagination.

#### `blog2.html` (Blog Listing — Standard List with Sidebar)
- Full-width post cards with rich text snippets.
- Standard WordPress-style sidebar:
  - `widget-search-box`: Search keyword input.
  - `widget-category`: Blog category list with count badges.
  - `widget-recent-post`: 3 thumbnail posts with publication dates.
  - `widget-tag`: Tag cloud pills.
  - `widget-newsletter`: Email newsletter subscription form.

#### `single-blog1.html` (Single Article Detail)
- Hero article image and typography-rich article body.
- Blockquote styling with author attribution.
- Social sharing buttons (Facebook, Twitter, Pinterest, LinkedIn).
- Author Profile Box (`author-box-layout1`) with photo, name, and bio.
- Threaded comments list (Parent and reply comments with avatars).
- Leave A Reply Form (Name, Email, Website, Comment text, Submit button).
- Full blog sidebar.

---

### 4.10 Contact Page (1 screen)

#### `contact.html` (Contact Us & Google Map)
- Full-width interactive Google Map container (`#googleMap`) with custom styled map skin, zoom control, and animated bouncing map marker.
- 3 Contact Info Cards (`contact-box-layout1`):
  1. *Office Address:* Physical street address.
  2. *Phone Numbers:* Primary and secondary phone lines.
  3. *Email Contacts:* Branded and customer support emails.
- Contact Form (`#contact-form`):
  - Full Name (`name="name"`, required).
  - Email Address (`name="email"`, required).
  - Subject Line (`name="subject"`).
  - Message (`name="message"`, required).
  - Submit Button with animated response container (`.form-response`).

---

### 4.11 Utility Pages (2 screens)

#### `coming-soon.html` (Under Construction / Launch Screen)
- Clean, focused landing page without standard header/footer.
- Centered brand logo.
- Animated live countdown clock (`.countdown`): Days, Hours, Minutes, Seconds.
- Email newsletter subscription form to capture leads before launch.
- Social media icon channels.

#### `404.html` (Error Page)
- Friendly 404 error illustration graphic (`img/figure/404.png`).
- Headline: "Sorry! Page Was Not Found".
- Explanatory copy and embedded keyword search box.
- "Back to Home" primary button.

---

### 4.12 Extraneous Artifact: `popper.html`

- **Nature:** An extraneous 99,944-byte HTML file in the workspace root.
- **Cause:** Downloaded by HTTrack when attempting to fetch `popper.js` or `popper.html` from the source demo server; it captured a WordPress 404 page with heavy third-party tracking scripts.
- **Action:** Can be safely deleted from the project root without affecting template functionality (the actual library exists at `js/popper.min.js`).

---

## 5. UI Component Library & Layout Classes

### 5.1 Navigation & Header Styles

- `.header.menu-layout1`: Standard clean header with topbar and right-aligned main navigation.
- `.header.menu-layout2`: Transparent or solid floating navbar with compact navigation links.
- `.header.menu-layout3`: Three-tier corporate layout (Topbar + Middlebar with Logo and contact widgets + Bottom navigation bar).
- `.rt-sticky`: CSS class applied dynamically by `main.js` on window scroll past the header threshold; fixes navbar to the top with a subtle drop shadow.
- `#dropdown`: The primary desktop navigation menu selector (`<nav id="dropdown" class="template-main-menu">`).
- `.meanmenu`: Mobile responsive menu generated automatically by `jquery.meanmenu.min.js` below 992px screen width.
- `.offcanvas-menu-btn` & `#offcanvas-wrap`: Hidden side panel drawer activated via toggle button for mobile or auxiliary site details.

---

### 5.2 Box Layout Components (45+ Variants)

The template follows a modular BEM-like class naming convention for all content blocks:

```
[module]-box-layout[number]
```

| Component Family | Classes Defined in `style.css` | Description & Key Elements |
| :--- | :--- | :--- |
| **About Us** | `about-box-layout1` to `about-box-layout7` | Story intros, checkmarks, side-by-side photo grids, circular progress badges |
| **Services** | `service-box-layout1` to `service-box-layout4` | Grid cards with Flaticon icons, photo cards with price badges, overlay cards |
| **Single Service** | `single-service-box-layout1` | Hero service photo, structured text, checkmark guarantees, FAQ cards |
| **Why Choose Us** | `why-choose-box-layout1` to `why-choose-box-layout4` | Numbered benefit boxes, icon-top cards, accent background strips |
| **Process / Workflow** | `process-box-layout1` | 4-step linear flow with step numbers, arrows, and descriptive text |
| **Pricing Tables** | `pricing-box-layout1` | Plan title, currency badge, monthly fee, bulleted feature list, CTA button |
| **Team Profiles** | `team-box-layout1` to `team-box-layout4` | Portrait photo, name, title, animated social link overlay on hover |
| **Single Team** | `single-team-box-layout1` | Staff biography, direct contact card, animated skill progress bars |
| **Testimonials** | `testimonial-box-layout1` to `testimonial-box-layout3` | Quote icon, client review text, 5-star rating, client name, photo, location |
| **Progress / Stats** | `progress-box-layout1` | Animated numerical digits (`.counter`), metric icon, label text |
| **Projects** | `project-box-layout1`, `single-project-box-layout1` | Portfolio cards with zoom/link overlays; case study problem/solution blocks |
| **Blog Articles** | `blog-box-layout1`, `layout2`, `single-blog-box-layout1` | News cards with date pill, author, title, snippet; full post with comment stream |
| **Brand / Partners** | `brand-box-layout1`, `brand-box-layout2` | Logo image carousel with grayscale to color hover transition |
| **Banners / CTAs** | `banner-box-layout1` to `layout5`, `action-box-layout1`, `layout2` | Full-width emergency call strips, 30% discount promo cards, video CTA blocks |
| **Products (Shop)** | `product-box-layout1` | Store product cards with ratings, pricing, and Add to Cart buttons |
| **Contact Info** | `contact-box-layout1` | Icon badge, channel title, telephone/email/address details |
| **Error Page** | `error-box-layout1` | Large graphic, error message, search bar, home redirect button |

---

### 5.3 Sidebar Widgets

All inner pages support standard widget containers wrapped in `.sidebar-widget-area`:

- `.widget.widget-category`: List of links with arrow icons and count indicators.
- `.widget.widget-service-info`: Structured key-value table (Timing, Cost, Category, Location).
- `.widget.widget-project-info`: Project metadata (Client, Completion Date, Category, Scope).
- `.widget.widget-download`: Styled PDF/document download buttons with file icons.
- `.widget.widget-contact-form`: Compact sidebar lead capture form.
- `.widget.widget-banner`: Visual discount callout banner with instant dial button.
- `.widget.widget-recent-post`: Thumbnail list of top 3 latest blog articles.
- `.widget.widget-tag`: Tag cloud pills with active hover styles.
- `.widget.widget-newsletter`: Email newsletter signup form.
- `.widget.widget-search-box`: Search input with submit icon.

---

### 5.4 Button & Action Styles

| Class | Appearance | Common Usage |
| :--- | :--- | :--- |
| `.btn-fill-md` | Medium rectangular solid button | Header "Get A Quote", General CTAs |
| `.btn-fill-sm` | Compact solid button | Sidebar forms, widget buttons |
| `.btn-fill-xl` | Large prominent button | Hero banner primary actions |
| `.fw-btn-fill` | 100% full-width block button | Form submission buttons ("Book Now", "Send") |
| `.bg-accent.text-primarytext` | Yellow background (`#fef22e`) with navy text | High-converting action buttons |
| `.bg-lightprimary` | Dodger blue background (`#287ff9`) with white text | Secondary action buttons |
| `.play-btn` | Circular pulsing play button with triangle icon | Magnific Popup YouTube video triggers |
| `.scrollup.back-top` | Floating square button on bottom-right | Smooth scroll to top of page |

---

### 5.5 CSS Helper & Utility Classes

- **Background Utilities:** `.bg-Primary` (`#14287b`), `.bg-lightprimary` (`#287ff9`), `.bg-accent` (`#fef22e`), `.bg-assh` (`#f8f8f8`), `.bg-aash` (`#f9fafc`), `.bg-assh-2` (`#f1f1f1`), `.bg-white` (`#ffffff`), `.bg-common` (background cover & center).
- **Attribute Trigger for Backgrounds:** `data-bg-image="path/to/img.jpg"` — automatically applied as a CSS `background-image` via `main.js`.
- **Spacing Utilities:**
  - Section paddings: `.section-padding-12-9` (120px top, 90px bottom), `.section-padding-md`, `.section-padding-lg`.
  - Margins: `.mg-b-20` (margin-bottom 20px), `.mg-b-30` (30px), `.mg-b-40`, `.mg-b-60` (60px), `.mg-b--30` (-30px pull).
  - Gutters: `.gutters-10` (10px grid gutters), `.gutters-20`, `.gutters-5`.
- **Decorative Shapes:** `.section-shape1`, `.section-shape2` (wave and curve divider backgrounds).

---

## 6. Interactive Features & JavaScript Plugins

| Feature / Plugin | Script File | Selector / Trigger | Configuration & Capabilities |
| :--- | :--- | :--- | :--- |
| **Contact Form Validation & AJAX** | `validator.min.js`, `main.js` | `#contact-form` | Validates required inputs, email format. Submits via POST to `vendor/php/form-process.php`. Displays inline status alert (`.form-response`). |
| **Sticky Header** | `main.js` | `body.sticky-header #header-menu` | Monitors scroll offset; adds `.rt-sticky` class when scrolling past topbar. |
| **Mobile Menu** | `jquery.meanmenu.min.js` | `nav#dropdown` | Replaces desktop menu below 992px with toggleable mobile accordion navigation. |
| **Hero Slider 1 to 5** | `jquery.nivo.slider.js`, `vendor/slider/home.js` | `#ensign-nivoslider-1` through `-5` | Configured with slice animations, box animations (`boxRainReverse`, `fold`, `boxRainGrowReverse`), pause time 9000ms, transition speed 1000ms. |
| **Content Carousels** | `owl.carousel.min.js`, `main.js` | `.rc-carousel` | Reads data attributes from HTML tag (`data-loop`, `data-items`, `data-autoplay`, `data-responsive`). Powers Testimonials, Team, and Brands. |
| **Animated Metrics Counter** | `jquery.counterup.min.js`, `waypoints.min.js` | `.counter` | Animates numbers from 0 to target when scrolled into viewport (2000ms duration, 50ms delay). |
| **Video Lightbox Popup** | `jquery.magnific-popup.min.js` | `.popup-youtube` | Opens YouTube / Vimeo video embed in a clean modal overlay with fade animation. |
| **Date & Time Picker** | `jquery.datetimepicker.full.min.js` | `.rt-date`, `.rt-time` | `.rt-date` displays calendar dropdown (`d-m-Y`); `.rt-time` displays hour/minute picker (`H:i`). |
| **Filterable Gallery / Masonry** | `isotope.pkgd.min.js`, `imagesloaded.pkgd.min.js` | `#no-equal-gallery .no-equal-item` | Assembles masonry portfolio grid after images finish loading; supports category filtering. |
| **Product Image Zoom** | `jquery.elevatezoom.js` | `.zoom_01` | Inner lens zoom with crosshair cursor on product detail images; refreshes on tab toggle. |
| **Store Quantity Increment** | `main.js` | `.quantity-plus`, `.quantity-minus` | Increments/decrements numeric value inside `input.quantity-input` (min 1). |
| **Store Layout Switcher** | `main.js` | `.product-view-trigger` | Toggles product listing display between `.product-box-grid` and `.product-box-list`. |
| **Countdown Clock** | `jquery.countdown.min.js` | `.countdown` | Parses target date string (e.g., `YYYY/MM/DD`); updates days, hours, minutes, seconds dynamically. |
| **Custom Select Inputs** | `select2.min.js` | `select.select2` | Transforms standard HTML `<select>` into searchable, styled dropdowns with custom arrow icons. |
| **Google Maps Embed** | `main.js` (Google Maps API) | `#googleMap` | Initializes styled road/water skin, custom pin marker (`img/map-marker.png`), and bounce animation. |
| **Preloader** | `main.js` | `#preloader` | Fades out `.preloader` GIF when page assets complete loading. |
| **Smooth Section Scroll** | `main.js` | `[data-type="section-switch"]` | Smoothly scrolls to target anchor ID on click (1000ms duration). |

---

## 7. Icon Sets & Typography Assets

### 7.1 Dedicated Cleaning Flaticon Font

The template includes a custom-built font (`font/flaticon.css`) offering 23 purpose-built cleaning and hygiene icons:

```css
.flaticon-clean:before          /* Sparkle / hygiene badge */
.flaticon-mop:before            /* Floor mop and bucket */
.flaticon-clean-1:before        /* Spray cleaner bottle */
.flaticon-clean-2:before        /* Cleaning gloves */
.flaticon-clean-3:before        /* Sanitizer / scrub brush */
.flaticon-vacuum:before         /* Vacuum cleaner */
.flaticon-brush:before          /* Broom / brush */
.flaticon-dishwasher:before     /* Dishwashing / kitchen cleaner */
.flaticon-shower:before         /* Bathroom / shower hygiene */
.flaticon-tower:before          /* High-rise building / window cleaning */
.flaticon-car-front:before      /* Automobile cleaning / car wash */
.flaticon-sports-car:before     /* Vehicle detailing */
.flaticon-calendar:before       /* Booking appointment calendar */
.flaticon-phone-call:before     /* Phone support */
.flaticon-mail:before           /* Email support */
.flaticon-maps-and-flags:before /* Physical office location pin */
.flaticon-message:before        /* Chat / feedback speech bubble */
.flaticon-play-arrow:before     /* Video play button */
.flaticon-right-arrow:before    /* Navigation forward arrow */
.flaticon-down-arrow:before     /* Dropdown chevron */
.flaticon-back:before           /* Back arrow */
```

### 7.2 FontAwesome 5 Free

Located in `webfonts/` and styled via `css/fontawesome-all.min.css`:
- **Solid Icons (`fas fa-*`):** Chevrons, checkmarks, stars, shopping carts, quote icons, user avatars, search magnifying glasses, clock icons.
- **Regular Icons (`far fa-*`):** Calendar outlines, clock outlines, comment speech bubbles.
- **Brand Icons (`fab fa-*`):** Facebook, Twitter, LinkedIn, Instagram, Pinterest, YouTube.

---

## 8. Media & Image Assets Inventory

All images reside in `img/` and are organized by functional domain:

### 8.1 Branding & Global
- `img/logo-dark.png` (250x60): Primary logo for white navigation bars.
- `img/logo-dark2.png`: Alternative logo variant for Middlebar layouts.
- `img/large-logo.png`: White/high-contrast logo for the dark navy footer.
- `img/favicon.png`: Cleaning icon favicon.
- `img/preloader.gif`: Page loading spinner animation.
- `img/map-marker.png`: Custom map pin icon for Google Maps.

### 8.2 Hero Sliders (`img/slider/`)
- 9 high-resolution photographic banners (1920x800px):
  - `slide1-1.jpg`, `slide1-3.jpg`: Commercial office cleaners with industrial floor polishers.
  - `slide2-1.jpg`: Residential living room cleaner dusting furniture.
  - `slide3-1.jpg`, `slide3-2.jpg`, `slide3-3.jpg`: Domestic and commercial cleaners in uniforms.
  - `slide4-1.jpg`, `slide4-2.jpg`: Janitors smiling with sanitization supplies.

### 8.3 Services Photography (`img/service/`)
- 12 commercial and domestic service images:
  - `service1.jpg`, `service.jpg`: Kitchen deep cleaning and grease removal.
  - `service2.jpg`: Window and glass squeegee cleaning.
  - `service3.jpg`: Office workstation and conference room vacuuming.
  - `service4.jpg`: Tile, grout, and marble floor scrub polishing.
  - `service5.jpg`: Plumbing and drain hygiene.
  - `service10.jpg`, `service11.jpg`: High-rise window and commercial facility sanitization.

### 8.4 Team Portraits (`img/team/`)
- 14 professional staff portrait cutout images (`team1.png` through `team14.png`) on transparent PNG backgrounds, perfectly formatted for cards with overlapping colorful shapes.

### 8.5 Figures, Banners & Illustrations (`img/figure/`)
- 72 graphic assets including:
  - `breadcumb.jpg` (1920x350): Global inner page header background banner.
  - `banner-figure.png`: Uniformed cleaning worker pointing to discount offer.
  - `404.png`: Illustration of broken mop/vacuum for the error page.
  - `product1.png` to `product9.jpg`: Detergents, cleaning liquids, spray bottles, scrubbers for the shop.
  - `bubble1.png` to `bubble10.png`: Transparent water bubble vectors providing floating background visual interest.

### 8.6 Projects & Case Studies (`img/project/`)
- 8 project photos (`project1.jpg` to `project8.jpg`) featuring completed commercial office, domestic kitchen, and window cleaning jobs.

### 8.7 Partner & Client Logos (`img/brand/`)
- 9 logo placeholders (`brand1.png` to `brand9.png`) for corporate clients, association memberships, and certifications.

---

## 9. EcoCare Mapping & Production Readiness Gap Analysis

This section bridges the gap between this Clenix template inventory and EcoCare's real business data documented in `knowledge.md`.

### 9.1 Mapping EcoCare Services to Clenix Components

| EcoCare Service (from `knowledge.md`) | Recommended Clenix Template Page | Matching Clenix Icon / Asset | Suggested Sidebar Widgets |
| :--- | :--- | :--- | :--- |
| **Residential & Domestic Cleaning** | `single-service1.html` | `.flaticon-clean-1` / `img/service/service.jpg` | Category List, Download Brochure |
| **Office & Commercial Cleaning** | `single-service2.html` | `.flaticon-vacuum` / `img/service/service3.jpg` | Service Info Card, Booking Form |
| **Fumigation & Pest Control (EcoFumes)** | `single-service1.html` | `.flaticon-clean-3` / `img/service/service11.jpg` | Safe Chemicals Guarantee, Info Widget |
| **Carpet & Upholstery Care** | `single-service2.html` | `.flaticon-mop` / `img/service/service4.jpg` | Package Pricing, Quick Calculator |
| **Laundry & Dry Cleaning (Eco-Laundry)** | `single-service1.html` | `.flaticon-dishwasher` / `img/figure/product1.png` | Pickup/Delivery Schedule Widget |
| **Tile, Marble & Floor Polishing** | `single-service2.html` | `.flaticon-brush` / `img/service/service4.jpg` | Before/After Gallery, Info Widget |
| **Window & Glass Cleaning** | `single-service1.html` | `.flaticon-tower` / `img/service/service2.jpg` | High-rise Safety Widget |
| **Post-Construction & Deep Clean** | `single-service2.html` | `.flaticon-clean` / `img/service/service10.jpg` | Estimate Calculator Form |

### 9.2 Mapping Pricing & Booking

- **EcoCare's Old Advertised Packages:**
  1. *Carpet & Upholstery Care Package* -> Map to `pricing-table.html` (Plan 1 / Standard).
  2. *Deep Clean Package* -> Map to `pricing-table.html` (Plan 2 / Premium).
- **EcoCare's Old Booking Chaos:**
  - In `knowledge.md`, the old website had 6 broken forms (`booking.html`, `booking-laundry.html`, `booking-fumigation.html`, `booking-upholstery.html`, `booking-capet.html`) with mismatched camelCase/snake_case PHP handlers.
  - **The Clenix Solution:** Consolidate booking into `calculate-form.html`. Its Select2 dropdowns, date picker, time picker, and address fields can easily capture the service category, service mode (pickup vs. at-home), and appointment preferences in a single unified interface.

### 9.3 Mapping Company Identity & Leadership

- **Leadership Profiles (`team1.html` / `single-team.html`):**
  - **Eric Nana Acquah** — CEO & Founder.
  - **Margaret Owusua Acquah** — Administrative Accountant.
  - Feature their photos and verified designations using `team-box-layout1` or `single-team.html`.
- **Certifications & Associations (`brand/` carousel):**
  - Contract Cleaners Association of Ghana (CCAG) membership logo can replace `img/brand/brand1.png`.
- **Contact Details (Header, Footer, `contact.html`):**
  - Address: Achimota Mile 7, Accra, Ghana.
  - Phone: `+233 24 901 4253` / `+233 24 380 7100`.
  - Email: `info@ecocaregh.com` / `ecocaregh1on1@gmail.com`.

### 9.4 Technical Gaps & Required Actions for Deployment

1. **Missing Backend Form Handler (`vendor/php/form-process.php`):**
   - In `js/main.js` line 16, the contact and booking forms submit to `vendor/php/form-process.php`. This file does not exist in the mirrored template.
   - *Fix:* Create a lightweight, secure PHP handler or replace the AJAX endpoint with a modern serverless form service (e.g. Formspree, Web3Forms, EmailJS, or a Netlify/Vercel serverless function).
2. **Extraneous File Cleanup (`popper.html`):**
   - Delete `popper.html` from the project root to eliminate 99KB of unnecessary third-party tracking scripts.
3. **Google Maps API Key:**
   - In `contact.html` line 524, a demo Google Maps API key is embedded (`AIzaSyBtmXSwv4YmAKtcZyyad9W7D4AC08z0Rb4`). Update this with a valid Google Cloud Maps JavaScript API key centered on Achimota Mile 7, Accra, Ghana.
4. **Cloudflare Beacon Cleanup:**
   - As identified during the HTTrack comment cleanup, all 26 HTML pages contain a captured Cloudflare tracking script at the bottom of the body. These can be removed to improve load times and avoid reporting analytics to the template author's account.
5. **Image Replacement:**
   - Replace placeholder logos (`img/logo-dark.png`, `img/large-logo.png`) with EcoCare's official brand logo and green/eco-friendly cleaning assets.

