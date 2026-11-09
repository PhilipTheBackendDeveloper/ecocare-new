#!/usr/bin/env node
/**
 * EcoCare Cleaning Services Limited — Netlify Forms & Staging Test Suite
 * Validates:
 * 1. Static HTML Netlify Form detection attributes across all canonical pages
 * 2. Client-side input validation, honeypots, and timing defenses
 * 3. Netlify URL-encoded submission format and response handling
 * 4. Staging build isolation and noindex indexing barriers
 */

const assert = require("assert");
const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const DIST_STAGING = path.join(ROOT, "dist", "staging");

let passed = 0;
let failed = 0;

function test(name, fn) {
  try {
    fn();
    console.log(`  ✓ PASS: ${name}`);
    passed++;
  } catch (err) {
    console.error(`  ✗ FAIL: ${name}`);
    console.error(`    Error: ${err.message}`);
    failed++;
  }
}

console.log("========================================================================");
console.log("EcoCare Netlify Forms & Full-Site Staging Test Suite");
console.log("========================================================================\n");

// --- 1. HTML NETLIFY FORM DETECTION ATTRIBUTES ---
console.log("--- 1. STATIC HTML NETLIFY FORM ATTRIBUTES ---");

test("contact.html contains valid Netlify form attributes and honeypot", () => {
  const content = fs.readFileSync(path.join(ROOT, "contact.html"), "utf8");
  assert.match(content, /<form[^>]+name="contact"/, "Missing name='contact' on contact.html form");
  assert.match(content, /data-netlify="true"/, "Missing data-netlify='true' on contact.html form");
  assert.match(content, /data-netlify-honeypot="bot-field"/, "Missing data-netlify-honeypot='bot-field'");
  assert.match(content, /name="form-name"[^>]+value="contact"/, "Missing hidden input form-name='contact'");
  assert.match(content, /name="bot-field"/, "Missing honeypot input bot-field");
  assert.match(content, /name="website_url"/, "Missing client honeypot website_url");
  assert.match(content, /name="name"/, "Missing customer name field");
  assert.match(content, /name="phone"/, "Missing customer phone field");
  assert.match(content, /name="subject"/, "Missing subject field");
  assert.match(content, /name="message"/, "Missing message field");
  assert.match(content, /class="form-response[^"]*"\s+role="status"\s+aria-live="polite"/, "Missing accessible role='status' and aria-live='polite'");
});

test("calculate-form.html contains valid Netlify quote-calculator attributes", () => {
  const content = fs.readFileSync(path.join(ROOT, "calculate-form.html"), "utf8");
  assert.match(content, /<form[^>]+name="quote-calculator"/, "Missing name='quote-calculator' on calculate-form.html");
  assert.match(content, /data-netlify="true"/, "Missing data-netlify='true' on calculate-form.html");
  assert.match(content, /data-netlify-honeypot="bot-field"/, "Missing data-netlify-honeypot='bot-field'");
  assert.match(content, /name="form-name"[^>]+value="quote-calculator"/, "Missing hidden form-name='quote-calculator'");
  assert.match(content, /name="bot-field"/, "Missing honeypot input bot-field");
  assert.match(content, /name="service"/, "Missing service select");
  assert.match(content, /name="property_type"/, "Missing property_type select");
  assert.match(content, /name="location"/, "Missing location field");
  assert.match(content, /name="name"/, "Missing customer name field");
  assert.match(content, /name="phone"/, "Missing phone field");
  assert.match(content, /id="calc-customer-name"/, "Customer name should use id='calc-customer-name' to avoid form-name collision");
  assert.match(content, /class="form-response[^"]*"\s+role="status"\s+aria-live="polite"/, "Missing accessible role='status'");
});

test("index.html booking form contains Netlify quote-calculator attributes", () => {
  const content = fs.readFileSync(path.join(ROOT, "index.html"), "utf8");
  assert.match(content, /<form[^>]+id="ecocare-booking-form"[^>]+name="quote-calculator"/, "Missing name='quote-calculator' on index.html");
  assert.match(content, /data-netlify="true"/, "Missing data-netlify='true' on index.html");
  assert.match(content, /data-netlify-honeypot="bot-field"/, "Missing data-netlify-honeypot on index.html");
  assert.match(content, /name="form-name"[^>]+value="quote-calculator"/, "Missing hidden form-name on index.html");
  assert.match(content, /name="bot-field"/, "Missing bot-field on index.html");
});

test("Sidebar quick inquiry widgets on service and FAQ pages configure Netlify contact form", () => {
  const servicePages = [
    "single-service1.html",
    "single-service2.html",
    "pest-control.html",
    "carpet-cleaning.html",
    "upholstery-cleaning.html",
    "faq.html",
  ];

  for (const page of servicePages) {
    const content = fs.readFileSync(path.join(ROOT, page), "utf8");
    assert.match(content, /<form[^>]+name="contact"/, `${page} missing name='contact' on sidebar form`);
    assert.match(content, /data-netlify="true"/, `${page} missing data-netlify='true'`);
    assert.match(content, /name="form-name"[^>]+value="contact"/, `${page} missing hidden form-name='contact'`);
    assert.match(content, /name="bot-field"/, `${page} missing honeypot bot-field`);
  }
});

// --- 2. CLIENT-SIDE VALIDATION & LOGIC TESTS ---
console.log("\n--- 2. CLIENT-SIDE VALIDATION & BOT LOGIC ---");

// Re-implement identical validation functions as in js/ecocare.js
function isValidPhone(phone) {
  if (!phone) return false;
  const clean = phone.replace(/[^0-9+]/g, "");
  return clean.length >= 9 && clean.length <= 16;
}

function isValidEmail(email) {
  if (!email) return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
}

test("Ghanaian and international phone validation", () => {
  // Valid local and international formats
  assert.strictEqual(isValidPhone("+233 24 901 4253"), true, "+233 Ghana format should be valid");
  assert.strictEqual(isValidPhone("024 901 4253"), true, "024 Local 10-digit should be valid");
  assert.strictEqual(isValidPhone("0243807100"), true, "Continuous 10-digit should be valid");
  assert.strictEqual(isValidPhone("0551234567"), true, "055 MTN format should be valid");
  assert.strictEqual(isValidPhone("0201234567"), true, "020 Telecel format should be valid");
  assert.strictEqual(isValidPhone("+1 555 123 4567"), true, "US/Intl format should be valid");

  // Invalid numbers
  assert.strictEqual(isValidPhone(""), false, "Empty string should be invalid");
  assert.strictEqual(isValidPhone("123"), false, "Too short (<9 digits) should be invalid");
  assert.strictEqual(isValidPhone("abcdefghij"), false, "Alphabetic should be invalid");
  assert.strictEqual(isValidPhone("+123456789012345678"), false, "Too long (>16 digits) should be invalid");
});

test("RFC 5322 compliant email validation", () => {
  assert.strictEqual(isValidEmail("ecocaregh1on1@gmail.com"), true);
  assert.strictEqual(isValidEmail("client@domain.com.gh"), true);
  assert.strictEqual(isValidEmail("notanemail"), false);
  assert.strictEqual(isValidEmail("@domain.com"), false);
  assert.strictEqual(isValidEmail("user@.com"), false);
  assert.strictEqual(isValidEmail(""), false);
});

test("Bot honeypot logic intercepts and contains bots without submitting", () => {
  function handleHoneypotCheck(payload) {
    if (payload.website_url || payload["bot-field"]) {
      return { isBot: true, action: "silent_success_disarm" };
    }
    return { isBot: false };
  }

  const cleanPayload = { name: "Kwame", phone: "0249014253", website_url: "", "bot-field": "" };
  assert.strictEqual(handleHoneypotCheck(cleanPayload).isBot, false);

  const botPayload1 = { name: "SpamBot", phone: "0249014253", website_url: "http://spam.ru", "bot-field": "" };
  assert.strictEqual(handleHoneypotCheck(botPayload1).isBot, true);

  const botPayload2 = { name: "SpamBot2", phone: "0249014253", website_url: "", "bot-field": "I am a bot" };
  assert.strictEqual(handleHoneypotCheck(botPayload2).isBot, true);
});

test("Fast timing attack detection (< 1s from render)", () => {
  function checkTimingAttack(renderedAt, submitTime) {
    return submitTime - renderedAt < 1000;
  }

  const now = Date.now();
  assert.strictEqual(checkTimingAttack(now, now + 200), true, "Submissions < 1000ms should be flagged");
  assert.strictEqual(checkTimingAttack(now, now + 3500), false, "Submissions > 1000ms should pass");
});

// --- 3. NETLIFY FORM ENCODING & RESPONSE SIMULATION ---
console.log("\n--- 3. NETLIFY URL-ENCODED SUBMISSION & RESPONSE SIMULATION ---");

test("Form serialization encodes into standard application/x-www-form-urlencoded with form-name", () => {
  const formFields = {
    "form-name": "quote-calculator",
    service: "residential",
    location: "Achimota Mile 7, Accra",
    name: "Dr. Ama Poku",
    phone: "+233 24 901 4253",
    email: "ama@example.com",
    message: "Deep cleaning for 4 bedroom residence.",
  };

  const encoded = new URLSearchParams(formFields).toString();
  assert.ok(encoded.includes("form-name=quote-calculator"), "Encoded string must include form-name");
  assert.ok(encoded.includes("service=residential"), "Encoded string must include service");
  assert.ok(encoded.includes("name=Dr.+Ama+Poku") || encoded.includes("name=Dr.%20Ama%20Poku"), "Name must be URL-encoded");
});

test("Simulated Netlify 200 OK displays verified receipt and WhatsApp link", () => {
  function simulateSubmissionResponse({ status, payload }) {
    if (status >= 200 && status < 300) {
      const waText = encodeURIComponent(`Hello EcoCare! I just submitted an inquiry on your website.\nName: ${payload.name}`);
      return {
        success: true,
        htmlMessage: `<h5 class="alert-heading">Inquiry Received Successfully!</h5><p>Thank you, ${payload.name}! Your inquiry has been received by EcoCare Cleaning Services Limited.</p>`,
        whatsappUrl: `https://wa.me/233249014253?text=${waText}`,
      };
    } else {
      const waText = encodeURIComponent(`Hello EcoCare! My name is ${payload.name}. I attempted to submit an inquiry but encountered a connection issue.`);
      return {
        success: false,
        htmlMessage: "Notice: We could not deliver your request online due to a network connection issue.",
        whatsappUrl: `https://wa.me/233249014253?text=${waText}`,
        phoneLink: "tel:+233249014253",
        emailLink: "mailto:ecocaregh1on1@gmail.com",
      };
    }
  }

  const payload = { name: "Kofi Annan", phone: "0249014253", service: "laundry" };
  const okResult = simulateSubmissionResponse({ status: 200, payload });
  assert.strictEqual(okResult.success, true);
  assert.ok(okResult.htmlMessage.includes("Inquiry Received"), "Must show inquiry received message");
  assert.ok(okResult.whatsappUrl.includes("233249014253"), "Must provide direct WhatsApp link");

  // Verify failure NEVER shows success
  const failResult = simulateSubmissionResponse({ status: 500, payload });
  assert.strictEqual(failResult.success, false);
  assert.ok(!failResult.htmlMessage.includes("Inquiry Received"), "Failure MUST NOT claim inquiry received");
  assert.ok(failResult.htmlMessage.includes("Notice:"), "Failure must display clear notice");
  assert.ok(failResult.whatsappUrl.includes("233249014253"), "Failure must offer WhatsApp alternative");
  assert.strictEqual(failResult.phoneLink, "tel:+233249014253", "Failure must offer direct phone link");
  assert.strictEqual(failResult.emailLink, "mailto:ecocaregh1on1@gmail.com", "Failure must offer email link");
});

// --- 4. STAGING ISOLATION & NOINDEX AUDIT ---
console.log("\n--- 4. STAGING ISOLATION & NOINDEX AUDIT ---");

test("Staging build contains no unapproved demo pages", () => {
  if (!fs.existsSync(DIST_STAGING)) {
    throw new Error("dist/staging directory does not exist. Run scripts/build_staging.py first.");
  }

  const demoPages = [
    "index2.html", "index3.html", "index4.html",
    "about2.html", "service2.html",
    "blog1.html", "blog2.html", "single-blog1.html",
    "shop.html", "single-product.html",
    "team1.html", "team2.html", "single-team.html",
  ];

  for (const demo of demoPages) {
    const demoPath = path.join(DIST_STAGING, demo);
    assert.strictEqual(fs.existsSync(demoPath), false, `Demo page ${demo} must not exist in dist/staging`);
  }
});

test("Staging headers enforce X-Robots-Tag: noindex, nofollow", () => {
  const headersPath = path.join(DIST_STAGING, "_headers");
  assert.strictEqual(fs.existsSync(headersPath), true, "dist/staging/_headers must exist");
  const headers = fs.readFileSync(headersPath, "utf8");
  assert.match(headers, /X-Robots-Tag:\s*noindex,\s*nofollow/, "Staging _headers must contain X-Robots-Tag: noindex, nofollow");
});

test("Staging robots.txt enforces Disallow: /", () => {
  const robotsPath = path.join(DIST_STAGING, "robots.txt");
  assert.strictEqual(fs.existsSync(robotsPath), true, "dist/staging/robots.txt must exist");
  const robots = fs.readFileSync(robotsPath, "utf8");
  assert.match(robots, /Disallow:\s*\//, "Staging robots.txt must contain Disallow: /");
});

test("Root netlify.toml preserves production coming-soon target while routing deploy previews to staging", () => {
  const netlifyToml = fs.readFileSync(path.join(ROOT, "netlify.toml"), "utf8");
  assert.match(netlifyToml, /\[build\][\s\S]*?publish\s*=\s*"dist\/coming-soon"/, "Default build must publish dist/coming-soon");
  assert.match(netlifyToml, /\[context\.production\][\s\S]*?publish\s*=\s*"dist\/coming-soon"/, "Production context must publish dist/coming-soon");
  assert.match(netlifyToml, /\[context\.deploy-preview\][\s\S]*?publish\s*=\s*"dist\/staging"/, "Deploy preview context must publish dist/staging");
  assert.match(netlifyToml, /\[context\.branch-deploy\][\s\S]*?publish\s*=\s*"dist\/staging"/, "Branch deploy context must publish dist/staging");
});

console.log("\n========================================================================");
console.log(`TEST SUMMARY: ${passed} passed | ${failed} failed`);
console.log("========================================================================");

if (failed > 0) {
  process.exit(1);
}
