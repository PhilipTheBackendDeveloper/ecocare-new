/**
 * EcoCare Cleaning Services Limited — Automated Form Backend & Submission Test Suite
 * Executes end-to-end unit and integration tests against /api/contact and /api/quote handlers.
 */

const assert = require("assert");
const fs = require("fs");
const path = require("path");

const contactHandler = require("../api/contact");
const quoteHandler = require("../api/quote");

// Mock Request & Response Builder
function createMockReqRes({ method = "POST", body = {}, headers = {}, ip = "127.0.0.1" } = {}) {
  const req = {
    method,
    body,
    headers: {
      "x-forwarded-for": ip,
      ...headers,
    },
    socket: { remoteAddress: ip },
  };

  let statusCode = 200;
  let responseData = null;
  const setHeaders = {};

  const res = {
    setHeader: (k, v) => {
      setHeaders[k] = v;
      return res;
    },
    status: (code) => {
      statusCode = code;
      return res;
    },
    json: (data) => {
      responseData = data;
      return res;
    },
    // Test inspection getters
    getStatusCode: () => statusCode,
    getData: () => responseData,
    getHeader: (k) => setHeaders[k],
  };

  return { req, res };
}

async function runTests() {
  console.log("========================================================================");
  console.log("EcoCare Form Backend & Submission Test Suite");
  console.log("========================================================================\n");

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

  async function asyncTest(name, fn) {
    try {
      await fn();
      console.log(`  ✓ PASS: ${name}`);
      passed++;
    } catch (err) {
      console.error(`  ✗ FAIL: ${name}`);
      console.error(`    Error: ${err.message}`);
      failed++;
    }
  }

  // Ensure clean test storage
  const submissionsFile = path.join(process.cwd(), "data", "submissions.jsonl");
  if (fs.existsSync(submissionsFile)) {
    fs.unlinkSync(submissionsFile);
  }

  console.log("--- CONTACT FORM (/api/contact) TESTS ---");

  await asyncTest("Valid contact submission with Ghana phone (+233 24 901 4253)", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.1",
      body: {
        name: "Kwame Mensah",
        phone: "+233 24 901 4253",
        email: "kwame@example.com",
        subject: "Office Cleaning Inquiry",
        message: "Need regular office cleaning for our Ridge premises.",
        form_rendered_at: Date.now() - 5000,
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 200, "Status must be 200");
    const data = res.getData();
    assert.strictEqual(data.success, true);
    assert.ok(data.data.whatsappUrl.includes("233249014253"), "WhatsApp URL must point to EcoCare number");
  });

  await asyncTest("Valid contact submission with local Ghana phone format (0243807100)", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.2",
      body: {
        name: "Abena Osei",
        phone: "024 380 7100",
        message: "Requesting weekend deep cleaning in Airport Residential.",
        form_rendered_at: Date.now() - 4000,
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 200);
    assert.strictEqual(res.getData().success, true);
  });

  await asyncTest("Spam Honeypot: Bot filling website_url must be caught and disarmed", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.3",
      body: {
        name: "Spam Bot 3000",
        phone: "+1 555 123 4567",
        message: "Buy cheap backlinks now at spam-site.ru",
        website_url: "http://spam-site.ru/buy-links",
        form_rendered_at: Date.now() - 3000,
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 200, "Must return 200 to trick bot");
    // Verify NOT written to real inquiry submissions
    if (fs.existsSync(submissionsFile)) {
      const content = fs.readFileSync(submissionsFile, "utf8");
      assert.ok(!content.includes("Spam Bot 3000"), "Spam submission must not be logged to inquiries");
    }
  });

  await asyncTest("Spam Timing Attack: Submissions faster than 1s must be disarmed", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.4",
      body: {
        name: "Speed Bot",
        phone: "024 901 4253",
        message: "Submitting in 100ms",
        form_rendered_at: Date.now() - 200, // 200ms ago
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 200);
    if (fs.existsSync(submissionsFile)) {
      const content = fs.readFileSync(submissionsFile, "utf8");
      assert.ok(!content.includes("Speed Bot"), "Rapid bot must not be logged to real inquiries");
    }
  });

  await asyncTest("Validation Error: Invalid phone number (<9 digits) must return 400", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.5",
      body: {
        name: "Kofi Annan",
        phone: "12345", // too short
        message: "Hello EcoCare team",
        form_rendered_at: Date.now() - 3000,
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 400);
    assert.strictEqual(res.getData().success, false);
    assert.ok(res.getData().details.some((d) => d.includes("valid telephone number")));
  });

  await asyncTest("Validation Error: Missing name and message must return 400", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.0.6",
      body: {
        phone: "024 901 4253",
      },
    });

    await contactHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 400);
    assert.strictEqual(res.getData().success, false);
  });

  await asyncTest("Rate Limiting: Exceeding 5 submissions per minute must return 429", async () => {
    const testIp = "192.168.1.100";
    let lastStatusCode = 200;

    for (let i = 0; i < 6; i++) {
      const { req, res } = createMockReqRes({
        ip: testIp,
        body: {
          name: `Flooder ${i}`,
          phone: "024 901 4253",
          message: "Flooding request number " + i,
          form_rendered_at: Date.now() - 3000,
        },
      });
      await contactHandler(req, res);
      lastStatusCode = res.getStatusCode();
    }

    assert.strictEqual(lastStatusCode, 429, "6th request from same IP must receive 429 Too Many Requests");
  });

  console.log("\n--- QUOTE CALCULATOR (/api/quote) TESTS ---");

  await asyncTest("Valid quote calculator submission with all scope parameters", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.1.1",
      body: {
        name: "Dr. Ama Poku",
        phone: "+233 24 380 7100",
        email: "ama.poku@gmail.com",
        service: "residential",
        property_type: "residential-house",
        size_sqm: "medium",
        rooms: "3-4",
        bathrooms: "3-4",
        frequency: "one-time",
        location: "East Legon, Accra",
        date: "25/11/2026",
        time: "10:00 AM",
        message: "Four-bedroom home move-in scrub and window cleaning.",
        form_rendered_at: Date.now() - 4000,
      },
    });

    await quoteHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 200);
    const data = res.getData();
    assert.strictEqual(data.success, true);
    assert.strictEqual(data.data.service, "residential");
    assert.ok(data.data.whatsappUrl.includes("East%20Legon"), "WhatsApp URL must contain location");
  });

  await asyncTest("Quote validation error: Missing location in Accra must return 400", async () => {
    const { req, res } = createMockReqRes({
      ip: "10.0.1.2",
      body: {
        name: "Client Without Location",
        phone: "024 901 4253",
        service: "commercial",
        message: "Office clean",
        form_rendered_at: Date.now() - 3000,
      },
    });

    await quoteHandler(req, res);
    assert.strictEqual(res.getStatusCode(), 400);
    assert.ok(res.getData().details.some((d) => d.includes("area or landmark")));
  });

  console.log("\n--- PERSISTENT STORAGE VERIFICATION ---");

  test("Submissions are persisted to data/submissions.jsonl", () => {
    assert.ok(fs.existsSync(submissionsFile), "data/submissions.jsonl must exist on disk");
    const content = fs.readFileSync(submissionsFile, "utf8").trim().split("\n");
    assert.ok(content.length >= 3, `Expected at least 3 logged submissions, got ${content.length}`);

    const firstEntry = JSON.parse(content[0]);
    assert.strictEqual(firstEntry.name, "Kwame Mensah");
    assert.strictEqual(firstEntry.type, "contact");
    assert.ok(firstEntry.receivedAt, "Must record ISO timestamp");

    const quoteEntry = content.find((l) => JSON.parse(l).name === "Dr. Ama Poku");
    assert.ok(quoteEntry, "Quote submission for Dr. Ama Poku must be logged");
    const parsedQuote = JSON.parse(quoteEntry);
    assert.strictEqual(parsedQuote.location, "East Legon, Accra");
  });

  console.log("\n========================================================================");
  console.log(`TEST SUMMARY: ${passed} passed | ${failed} failed`);
  console.log("========================================================================");

  if (failed > 0) {
    process.exit(1);
  }
}

runTests().catch((err) => {
  console.error("Fatal Test Runner Error:", err);
  process.exit(1);
});
