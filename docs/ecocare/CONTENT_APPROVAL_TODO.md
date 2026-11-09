# EcoCare Cleaning Services — Client Approval & Verification Backlog (`CONTENT_APPROVAL_TODO.md`)

**Document Version:** 1.1  
**Date:** 9 November 2026  
**Status:** Live Action Register  
**Governing Rule:** Independent safe implementation must proceed using neutral, truthful copy without blocking on these items. Unverified items remain in this register and are omitted from live public copy.

---

## 1. High-Priority Items (Immediate Client Decisions Needed)

| Item ID | Issue / Conflict | Discovered In | Severity | Current Implementation Guardrail | Action Required from Client (Daddy / EcoCare) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CA-01** | **Primary Contact Email & Domain Status** | `contact.html`, `ECOCARE_CONTENT_DATA.json` | **RESOLVED FOR DOMAIN / OPEN FOR MAILBOX** | Domain `ecocaregh.com` is registered, active, and live with HTTPS on Netlify. Published email is set to verified Gmail: `ecocaregh1on1@gmail.com`. Branded `info@ecocaregh.com` is omitted from public mail links until mailbox setup is completed. | Set up MX records and email hosting for `info@ecocaregh.com` if desired, or continue utilizing verified `ecocaregh1on1@gmail.com`. |
| **CA-02** | **Disputed Leadership Surname** | `about1.html` vs old team files | **HIGH** | Mention Eric Nana Acquah (CEO & Founder); omit disputed surname for Margaret Owusua (Boakye vs. Acquah) and stock portraits. Use "Our Management & Team" narrative. | Confirm full legal name, current role, and permission to feature profile on public website. |
| **CA-03** | **Official Pricing & Package Rates** | Clenix demo ($49/$99/$199) vs EcoCare no fixed rates | **HIGH** | All demo USD and unverified starting GHS figures removed. Converted into 3 Custom Package Inquiries across `pricing-table.html` and `index.html`: Quote on Scope for Residential, Deep Clean & Post-Build, and Corporate Facility Care. | Confirm whether EcoCare wants fixed starting prices (in GH₵) published, or prefers custom quote inquiries based on property inspection. |
| **CA-04** | **Pest Control Safety & Health Claims** | `pest-control.html`, `faq.html`, `terms-condition.html` | **HIGH** | All claims of "100% harmless to infants/pets" or "chemical-free fumigation" and invented fixed 2 to 4-hour intervals removed. Replaced with strict instructions to follow product labels and on-site qualified operator guidance. | Confirm exact chemical formulations, EPA licensing registration number, and standard re-entry safety intervals according to product labels. |
| **CA-12** | **Netlify Form Email Notification Setup** | `contact.html`, `calculate-form.html`, `netlify.toml` | **HIGH** | Forms migrated to native Netlify Forms with bot-field honeypot, accessible validation, zero container data-loss risk, and immediate WhatsApp fallback. Submissions record in Netlify Forms dashboard without paid APIs. | In Netlify Dashboard under Site configuration > Notifications > Form notifications, add email notification to `ecocaregh1on1@gmail.com`. |

---

## 2. Medium-Priority Items (Operational Confirmations)

| Item ID | Issue / Conflict | Discovered In | Severity | Current Implementation Guardrail | Action Required from Client |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **CA-05** | **Working Hours vs "24/7 Support"** | Homepage vs Service pages | **MEDIUM** | Removed "24/7 Support" banner. Stated standard operations: Monday – Saturday (07:00 – 18:00), Sunday by appointment for emergency/commercial requests. | Confirm exact business hours for customer service, office reception, and laundry pickup/drop-off. |
| **CA-06** | **Laundry Pickup & Delivery Coverage** | `single-service2.html` (Eco-Laundry) | **MEDIUM** | Framed pickup and delivery as available across Greater Accra subject to scheduling and location confirmation. | Confirm specific pickup/delivery radius, turnaround timelines (e.g. 24-48 hours), and whether transport fees apply. |
| **CA-07** | **Historical Business Incorporation Claims** | `about1.html` | **MEDIUM** | Framed as historical brand narrative: "Providing professional residential and commercial cleaning services in Ghana since 2014." Avoids repeating legal code citation as active legal claim. | Confirm official Registrar General's Department registration details and certificate spelling if desired on About page. |
| **CA-08** | **CCAG Association Membership** | `knowledge.md` | **MEDIUM** | CCAG logo omitted from brand carousel until current active membership certificate is verified. | Confirm whether EcoCare is currently in good standing with the Contract Cleaners Association of Ghana. |
| **CA-09** | **Customer Testimonials Verification** | 8 Historical reviews in archive | **MEDIUM** | Native Clenix carousel preserved with prominent, transparent legal disclosure stating consent renewal is pending under Ghana DPA (Act 843). | Provide 3–5 real customer testimonials with permission to publish client first name and residential/commercial area. |
| **CA-10** | **Numerical Metrics Counters** | Demo counter: "2583+ clients, 80+ team, 2129+ projects" | **MEDIUM** | Replaced with verified operational features: "5 Core Cleaning Services", "Experienced Cleaning Staff", "Eco-Conscious Methods", "Dedicated Customer Support". | Provide verified operational statistics if client desires numerical milestone counters. |
| **CA-11** | **Physical Office Map Pin & GhanaPost GPS** | `contact.html` | **LOW** | Embedded interactive Google Maps iframe centered on EcoCare Laundry, Achimota Mile 7, Accra, Ghana. | Provide official GhanaPost GPS digital address code (e.g., `GA-XXX-XXXX`) for the Achimota Mile 7 office. |
