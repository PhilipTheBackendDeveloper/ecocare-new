# AI coding-agent prompt — fill purchased ThemeForest template with EcoCare knowledge

You are a careful senior website developer and content implementer. This is a **content-population task**, not permission to invent content, replace the template with a new framework, or deploy unapproved business claims.

## What is available
- `ECOCARE_MASTER_KNOWLEDGE_BASE.md`: business/background/content evidence, draft copy, service descriptions, approval matrix.
- `ECOCARE_CONTENT_DATA.json`: structured data for service families, 12 historic cards, contact, old reviews, gallery paths, proposed copy, risk flags.
- `ECOCARE_SOURCE_AUDIT.json`: uploaded old markup inventory and precise referenced paths.
- The purchased ThemeForest template is in this repository (locate it; no template package was included in the research inputs). Do not confuse old EcoCare markup with the newly purchased theme.

## Before changing code
1. Inspect the repository recursively. Identify exact ThemeForest template name/version, license and documentation, framework (pure HTML, WordPress, Next, etc.), assets, page variants and existing build/deploy configuration. **Do not assume** any framework or directory structure.
2. Inventory every page/component/section and decide which existing theme variant should host each of the five main service families, home/about/projects/contact/policies. Preserve the purchased template's core visual design and working animations.
3. Extract all dummy/template/demo content and identify all hard-coded images, fonts, sample testimonials, pricing and form actions. Record a small implementation matrix mapping current section/selector to proposed EcoCare content.
4. Identify approved EcoCare assets actually present in the repo; missing old HTML image references are not assets. Don't automatically reuse copyrighted images/stock or customer photographs without rights.
5. Create a `CONTENT_APPROVAL_TODO.md` for missing facts and source conflicts. **Don't block independent safe edits** on missing details; use neutral copy and omit unverified widgets.

## Priority order for modifications
A. Branding (approved logo/colours only) -> navigation -> homepage -> services directory -> five service detail pages -> about -> gallery/projects -> contact -> legal placeholders -> metadata/accessibility.
B. Use `editorial_copy` values in JSON as **proposals** and adapt lengths to theme while retaining meaning. Factual names/dates/hours/clients are historical only and require owner sign-off. Preserve old taglines as brand reference until approved.
C. Service types are Cleaning/EcoClean, Laundry/Eco-Laundry, Pest control/EcoFumes, Carpet cleaning, Upholstery cleaning. Use 12 card labels as candidates, correcting obvious typos only in rendered copy. Connect every card to the proper detail/quote path.
D. Do not publish unverified stats (2583+ clients, 80+ team, 2129+ projects), discounts (30%), guaranteed 24/7 support, team/person profiles with unresolved names, customer reviews, client logos, unverified EPA/CCAG badges, absolute eco/safety claims or old legal text. Avoid inventing replacements.
E. Do not use `info@ecocaregh.com` as verified mail destination until domain and inbox are tested. Do not copy old PHP `mail()` handlers into a Vercel static app. A contact form must have real server-side delivery/persistence, privacy and proper success/error behavior. If backend is not in scope, implement direct phone/email links with confirmed contacts, and leave form as a documented TODO—not fake success.
F. Respect service-specific hours as **historical claims**; only expose confirmed values. Do not promise exact prices, response times or available slots without operational confirmation.
G. Page SEO: accurate unique titles/descriptions, headings, OpenGraph, no broken links, semantic HTML, sitemap/canonical where appropriate, Google LocalBusiness schema only using verified fields, alt text, WCAG 2.2-oriented keyboard and contrast support.

## Testing and quality gates
- Start local server using actual template instructions; don't invent npm commands for a static HTML theme.
- Test all routes, responsive layouts and navigation at desktop/tablet/mobile.
- Audit missing assets (404), browser console errors, invalid form actions and placeholder text.
- Confirm no dummy reviews/logo references/metrics/discounts remain live.
- Verify actual contact submission and notifications end-to-end in the deployed-compatible environment, or explicitly mark not implemented and disable it.
- Check mailto/tel/WhatsApp only with confirmed official channels.
- Run available test/build/lint commands, output precise pass/fail results and test gaps.
- Prepare a succinct delivery summary with changed files, maintained template structure, screenshots if available, outstanding business approvals and deployment dependencies.

## Critical constraint
**No hallucinations.** A clean, complete, honest page is better than filling every theme slot with invented benefits, faux team photos, false company metrics or legal claims. Anything not supported by the knowledge base and client approval goes into `CONTENT_APPROVAL_TODO.md`, not public-facing text. Do not deploy or purchase services without explicit authorization.
