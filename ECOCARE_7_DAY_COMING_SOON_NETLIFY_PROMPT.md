# EcoCare — 7-Day Clenix Coming Soon Site & Netlify Launch Prompt

You are a senior frontend engineer, release engineer, and QA engineer with access to my local EcoCare project at `/Users/apple/Developer/work/ecocare` (confirm actual working directory) and GitHub repository `PhilipTheBackendDeveloper/ecocare-new`.

## Goal
Publish **only a standalone Coming Soon website** for EcoCare Cleaning Services Limited at `https://ecocaregh.com`, using the **original purchased Clenix ThemeForest `coming-soon.html` design**, official EcoCare logo/favicon, and a genuine fixed-date seven-day countdown. Do NOT deploy the unfinished full site on that domain yet. Preserve the original `index.html`, all complete website pages, Git history and the existing Vercel preview; make the deployment reversible.

## 1. Inspect and protect
1. Read `coming-soon.html`, `js/main.js`, `js/jquery.countdown.min.js`, `style.css`, `css/ecocare.css`, `vercel.json`, `knowledge.md`, `docs/ecocare/`, and the logo/favicon/image files. Review `git status`, the latest commits and `.gitignore` first. Avoid overwriting uncommitted work.
2. Confirm that `js/main.js` contains the **expired** original Clenix countdown target `2019/10/21`. Replace or isolate this behavior for the temporary landing page; never run two competing timers on the same element.
3. Inspect the original template screenshot/appearance. Keep its existing coming-soon background art, layout, typography, responsive proportions, count-number styling and social links. Use minimal, scoped CSS to fix actual issues; do not redesign the full site or introduce a framework.
4. Confirm logo and favicon are actual EcoCare assets, preferably original `logo.png`, `logo-icon.png` and `favicon-01.png` or verified replacements. Do not use ThemeForest demo logos. If the logo is hard to read on a dark background, create only a lightweight variant or appropriate background with no alteration to its identity.

## 2. Seven-day countdown
1. Default planned deadline: **2026-11-16 14:00 GMT (Africa/Accra)** = `2026-11-16T14:00:00Z`. This is a proposed deadline based on the November 9, 2026 planning date. Make it easy to configure via one documented constant (or a data attribute); if the real deployment happens later, explain that the deadline must be adjusted to seven days after the actual launch, then committed once.
2. Count against a **single fixed UTC timestamp** shared by all visitors. Do not set the target to `Date.now() + seven days` on every page load; never reset on refresh, mobile devices, or on every Git deploy.
3. Show accurate **Days / Hours / Minutes / Seconds**, update once a second, pad hours/minutes/seconds, use accessible labels/announcements without excessive screen-reader chatter. Handle clock skew reasonably, reduced motion and JavaScript-disabled fallback.
4. When time reaches zero, stop at zero and display a neutral launch-status message. **Do not redirect to the incomplete `index.html` or expose the full site automatically.** The actual go-live requires an explicit deployment and client approval.
5. Verify timer code doesn't double-initialize via `js/main.js` and `jquery.countdown.min.js`. Prefer reusing original Clenix styles and plugin where feasible, but correctness and timezone consistency matter more than reusing plugin code.

## 3. Copy, contacts and SEO
1. Heading: `We Are Coming Soon` or `A Better EcoCare Website Is Coming Soon`.
2. Short copy should explain that **the website** is launching soon; avoid implying EcoCare the cleaning company is newly opening or announcing unapproved service divisions.
3. Show EcoCare Cleaning Services Limited, Achimota Mile 7, Accra, Ghana, phone `+233 24 901 4253` (`tel:+233249014253`) and temporary email `ecocaregh1on1@gmail.com`. Do not publish `info@ecocaregh.com` until the mailbox is verified.
4. Add the five established service families as brief informative labels only when they fit the existing Clenix design: EcoClean, Eco-Laundry, EcoFumes, Carpet Cleaning and Upholstery Cleaning. Do not add new elaborate sections, fabricated offers, statistics, customer reviews or a nonfunctional subscription form.
5. Social links must match verified existing EcoCare links and open safely. Every visible CTA/link must work. The logo on this temporary page must point to `/` (Coming Soon), not to the full unpublished `index.html`.
6. Set canonical and OG URLs correctly for the temporary root `https://ecocaregh.com/`; use actual absolute URLs in HTML source, never Markdown-formatted URLs. Temporary `noindex, follow` is appropriate to prevent indexing a placeholder; document removing it when the full site launches. Add basic metadata and correct favicon paths.

## 4. Build isolated site from the original Clenix assets
1. Create a maintainable, repeatable staging/build approach, such as:

```text
repo-root/
  coming-soon.html                 # Original Clenix source page, customized
  scripts/build_coming_soon.py    # Reproducibly generates an isolated deployable site
  dist/coming-soon/               # GENERATED, gitignored; only public deploy output
    index.html                    # Built from coming-soon.html
    css/...                       # Only needed CSS and dependent font files
    js/...                        # Only necessary JS and countdown code
    img/...                       # Official logo, favicon, existing background
    font/...                      # If referenced
    webfonts/...                  # If referenced
  netlify.toml                    # Builds/publishes only dist/coming-soon
```

2. Ensure relative paths resolve after moving `coming-soon.html` to the deployed `/index.html`. Include every referenced font, logo, favicon, background and CSS/JS dependency. Do not expose documentation, `.env`, source maps with secrets, unfinished pages, serverless API files or the full repo in the published directory.
3. Prefer a Python standard-library build script with no new package dependencies; it should validate source assets, clean stale output, copy only needed dependencies, and fail visibly on missing assets. Do not commit generated files unless necessary.
4. Add a Netlify configuration at the repository root equivalent to:

```toml
[build]
  command = "python3 scripts/build_coming_soon.py"
  publish = "dist/coming-soon"
```

5. Preserve `vercel.json` and do not change the current Vercel project or full-site homepage. Ensure the Netlify published root `/` displays the Coming Soon page, not the main `index.html`.

## 5. Local preview and QA
1. Execute the build locally. Preview it using `python3 -m http.server 5500 --directory dist/coming-soon`, then open `http://localhost:5500/`.
2. Perform **real browser visual checks** at desktop 1440px, tablet 768px and mobile 390px (and small 320px if available). Capture screenshots and inspect that logo, background, countdown and footer are readable without horizontal scrolling.
3. Run a link/asset check over the generated site; check for 404s, console errors and JS exceptions. Verify displayed timer matches the fixed UTC target; manually test 7 days, near zero, zero, refresh, and different timezone conditions using a configurable clock/test injection rather than waiting seven days.
4. Verify phone, email, accessibility, focus styles, metadata, favicon, reduced-motion support, and that the page doesn't unexpectedly expose full website routes.
5. If any blocker remains, report it honestly; do not claim production-ready based only on static checks.

## 6. GitHub + Netlify deployment and domain
1. Create a dedicated branch or safe commits for coming-soon changes. Show exactly what changed, run local checks, then commit and push after review. Avoid force pushes and avoid accidentally publishing development pages.
2. Explain the exact Netlify setup on `https://app.netlify.com/`: **Add new project → Import existing project → GitHub → `PhilipTheBackendDeveloper/ecocare-new` → main**, leaving base directory at repository root, applying build command `python3 scripts/build_coming_soon.py`, and publish directory `dist/coming-soon`. Confirm Netlify honors `netlify.toml`. Deploy first to `*.netlify.app` and visually inspect before connecting the domain.
3. On Netlify **Domain management → Add a domain you already own**: add `ecocaregh.com` and `www.ecocaregh.com`. Choose external DNS at Namecheap. In Namecheap **Domain List → Manage → Advanced DNS** configure only the website records Netlify requests. For Netlify's standard network, typical entries are `A @ 75.2.60.5` and `CNAME www <actual-project>.netlify.app`. Follow Netlify's displayed project-specific instructions if different.
4. **Never delete MX, SPF, DKIM, DMARC or unrelated TXT records.** Only remove conflicting A, AAAA, CNAME or URL-redirect host records after inspecting them. Do not change the domain's nameservers unless deliberately choosing Netlify DNS.
5. Verify both the apex and `www` domains, HTTPS certificate, redirect behavior and the live countdown after propagation. The site must not display the full Clenix/EcoCare in-progress website. Do not claim the domain is connected until it resolves and serves the new page.
6. Note that the repository is currently public; do not commit secrets. The Vercel Hobby deployment is not a recommended production host for the commercial EcoCare site. Keep Vercel as temporary development preview and review its plan/use compliance separately.

## 7. Handover, go-live and rollback
1. Write `docs/ecocare/COMING_SOON_DEPLOYMENT.md` containing reproducible build, preview, Git and Netlify steps; domain configuration; countdown target; how to change date; how to redeploy; how to roll back.
2. Document that when the full website is approved, a conscious change to the Netlify build/publish target is needed to switch from Coming Soon to the full project. **Countdown reaching zero alone must never make the full site live**.
3. Provide a final checklist with actual commands executed, successful verification evidence, links (if created), unresolved issues, and any required manual Netlify/Namecheap authorization.
4. Work end-to-end on the local project where you have access. If deployment/account access is unavailable, complete code/build/tests and supply exact manual steps, never pretend deployment occurred.

**Priority: Preserve Clenix visual design; correct fixed seven-day countdown; isolate deployment from unfinished site; full local preview/test; then safe Netlify deployment.**
