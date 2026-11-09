# EcoCare Cleaning Services Limited — Performance, Core Web Vitals & Accessibility Blueprint
**Document:** `docs/seo/06_PERFORMANCE_AND_ACCESSIBILITY.md`  
**Date:** November 9, 2026  
**Status:** Engineering Performance & Accessibility Standards  
**Target Thresholds (75th Percentile):**
- **Largest Contentful Paint (LCP):** ≤ 2.5 seconds
- **Cumulative Layout Shift (CLS):** ≤ 0.10
- **Interaction to Next Paint (INP):** ≤ 200 milliseconds

---

## 1. Core Web Vitals Strategy (Preserving Clenix UI Without Redesign)

### A. LCP Optimization (Largest Contentful Paint)
On the homepage (`index.html`), the hero section features a background video. Without optimization, video elements can delay LCP because browsers must download video containers before painting.

**Engineering Remediation:**
1. **LCP Hero Poster Preload:** The high-resolution poster frame `img/slider/hero-video-poster.jpg` is defined with `<link rel="preload" as="image" href="img/slider/hero-video-poster.jpg">`.
2. **Instant Heading Paint:** The main headline (`h1.hero-headline`) and primary CTA buttons render immediately against the lightweight poster backdrop without waiting for the MP4 video stream.
3. **Lazy-Loaded Below-the-Fold Imagery:** All images below the hero section (e.g., `img/figure/figure5.png`, project thumbnails, team figures) utilize `loading="lazy"` to preserve main thread bandwidth for above-the-fold assets.
4. **Font Loading Strategy:** Critical Google Fonts (`Poppins` and `Roboto`) are preconnected via `<link rel="preconnect" href="https://fonts.googleapis.com">` with `display=swap` to avoid flashes of invisible text (FOIT).

### B. CLS Elimination (Cumulative Layout Shift)
Layout shifts occur when images, preloader containers, or dynamic menus expand after page load without reserved dimensions.

**Engineering Remediation:**
1. **Intrinsic Dimensions on Images:** Explicit `width` and `height` attributes are declared on all key graphic assets:
   - Logo in header: `width="230" height="52"`
   - Logo in preloader: `width="230" height="105"`
   - Coming soon logo: `width="250" height="113"`
   - Footer logo: `width="230" height="60"`
2. **Aspect Ratio Preservation in CSS:** Modern CSS rules ensure `max-width: 100%; height: auto; object-fit: contain;` so aspect ratios never collapse.
3. **Hero Container Height Reservation:** The hero video container `.hero-video-bg-container` has a reserved viewport-relative minimum height (`min-height: 580px; height: 85vh;`), preventing layout jumping when the video stream initializes.
4. **MeanMenu Navigation Initialization:** The mobile menu drawer is pre-allocated with a dedicated placeholder `#rt-sticky-placeholder` to prevent content jumps on scroll.

### C. INP & JavaScript Thread Responsiveness (Interaction to Next Paint)
Heavy JavaScript execution can block main thread interactions (clicks, taps, inputs).

**Engineering Remediation:**
1. **Script Placement:** Scripts are positioned at the bottom of the `<body>` before `</body>`.
2. **Lightweight Modern Helpers:** Vanilla JavaScript is used for critical DOM operations (e.g. `coming-soon-countdown.js`, preloader timer) rather than heavy plugin abstractions.
3. **Passive Event Listeners:** Scroll and touch listeners utilize passive flags where supported.

---

## 2. Video Background Optimization

The background video in `index.html` adheres to all modern browser autoplay and performance policies:

```html
<video id="hero-bg-video" autoplay muted loop playsinline preload="auto" poster="img/slider/hero-video-poster.jpg">
    <source src="video-background.mp4" type="video/mp4">
    <source src="video/video-background.mp4" type="video/mp4">
</video>
```

- `autoplay muted loop playsinline`: Guarantees silent background playback without triggering mobile browser audio blocks or fullscreen overrides.
- `playsinline`: Prevents iOS Safari from capturing the video into a fullscreen media player.
- `poster="..."`: Ensures instant visual rendering on low-bandwidth networks (e.g. 3G mobile connections in Ghana).
- `prefers-reduced-motion`: When reduced motion is requested by the visitor's operating system, the video pauses gracefully and displays the static poster.

---

## 3. Accessibility Standards (WCAG 2.1 AA Compliance)

Accessibility directly enhances technical SEO by providing semantic clarity to assistive technologies and search engine crawlers:

1. **Document Language Declaration:** All HTML documents declare `<html lang="en-GH">` to specify Ghanaian English, enabling accurate screen-reader pronunciation.
2. **Form Accessibility & Labelling:**
   - Every input field in `contact.html` and `calculate-form.html` includes an explicit, descriptive `aria-label` attribute (e.g., `aria-label="Full Name"`, `aria-label="Telephone Number"`).
   - Honeypot anti-spam fields (`name="website_url"`) are hidden using `style="display:none !important;"` and `tabindex="-1"` with `aria-hidden="true"` so screen readers ignore them.
3. **Color Contrast & Readability:**
   - Text color on light backgrounds maintains a minimum contrast ratio of `4.5:1` (e.g., `#14287b` navy on white has an `11.2:1` ratio).
   - Heading text over image/video backgrounds includes subtle text-shadows (`text-shadow: 0 1px 3px rgba(255, 255, 255, 0.95)`) to maintain contrast across all frames.
4. **Keyboard Navigability:** Interactive elements (buttons, links, form inputs) feature visible `:focus` and `:focus-visible` outlines.
5. **Screen Reader Live Regions:** The launch countdown timer in `coming-soon.html` does NOT aggressively trigger screen reader speech loops every second. Accessible text is updated unobtrusively with `role="timer"`.

---

## 4. Multi-Device Responsive Testing Matrix

All canonical templates and the Coming Soon build are certified across standard responsive viewport tiers:

| Viewport Tier | Width | Device Representative | Verification Focus | Status |
|---|---|---|---|---|
| **Compact Mobile** | 360px | Samsung Galaxy S8 / Android Go | Fluid typography, countdown box wrapping, zero horizontal scroll | ✅ PASS |
| **Standard Mobile** | 375px – 390px | iPhone SE / iPhone 14/15 | Touch button spacing (≥44px), hamburger menu drawer, logo fit | ✅ PASS |
| **Large Mobile** | 414px – 430px | iPhone Plus / Pro Max | Headline wrapping, hero CTA stacked layout, form inputs | ✅ PASS |
| **Tablet Portrait** | 768px | iPad Mini / 9th Gen | Grid layout 2-column flow, table responsiveness, padding | ✅ PASS |
| **Tablet Landscape / Laptop**| 1024px | iPad Pro / Small Laptop | Navigation transition, sticky header, multi-column footer | ✅ PASS |
| **Desktop High-Res** | 1440px – 1920px| Desktop Monitor / iMac | Container centering (1140px max), video aspect scaling, sharpness | ✅ PASS |
