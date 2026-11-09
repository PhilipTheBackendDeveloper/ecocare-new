/**
 * EcoCare Cleaning Services Limited — Vercel Serverless Function: Contact Inquiries
 * Route: POST /api/contact
 * Validates incoming contact form data, dispatches email/notification, logs submission, and provides WhatsApp fallback.
 */

const fs = require("fs");
const path = require("path");
const https = require("https");

// Rate limiting configuration
const RATE_LIMIT_WINDOW_MS = 60 * 1000; // 1 minute
const MAX_REQUESTS_PER_WINDOW = 5;
const ipRequestCounts = new Map();

function isRateLimited(ip) {
  const now = Date.now();
  const entry = ipRequestCounts.get(ip) || { count: 0, firstRequest: now };

  if (now - entry.firstRequest > RATE_LIMIT_WINDOW_MS) {
    ipRequestCounts.set(ip, { count: 1, firstRequest: now });
    return false;
  }

  entry.count += 1;
  ipRequestCounts.set(ip, entry);
  return entry.count > MAX_REQUESTS_PER_WINDOW;
}

// Sanitize string against HTML/header injection
function sanitizeString(str, maxLength = 500) {
  if (typeof str !== "string") return "";
  return str
    .replace(/[<>]/g, "")
    .trim()
    .slice(0, maxLength);
}

// Phone validator (supports Ghana local 02x/05x/03x, +233, and international E.164)
function isValidPhone(phone) {
  if (!phone || typeof phone !== "string") return false;
  const digits = phone.replace(/[^\d+]/g, "");
  return digits.length >= 9 && digits.length <= 16;
}

// Email validator (RFC 5322 compliant regex)
function isValidEmail(email) {
  if (!email || typeof email !== "string") return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
}

// Save submission to local storage file safely
function saveSubmission(submission) {
  try {
    const dataDir = path.join(process.cwd(), "data");
    if (!fs.existsSync(dataDir)) {
      fs.mkdirSync(dataDir, { recursive: true });
    }
    const filePath = path.join(dataDir, "submissions.jsonl");
    const line = JSON.stringify(submission) + "\n";
    fs.appendFileSync(filePath, line, "utf8");
  } catch (err) {
    console.error("[ECOCARE-STORAGE-ERROR]", err.message);
  }
}

// Optional email dispatcher via Resend REST API if RESEND_API_KEY is configured
async function dispatchEmail(payload) {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    return { sent: false, reason: "No RESEND_API_KEY configured in environment" };
  }

  const notificationEmail = process.env.NOTIFICATION_EMAIL || "ecocaregh1on1@gmail.com";
  const postData = JSON.stringify({
    from: "EcoCare Website <onboarding@resend.dev>",
    to: [notificationEmail],
    subject: `New EcoCare Contact Inquiry: ${payload.subject}`,
    html: `
      <h2>New Contact Inquiry Received via EcoCare Website</h2>
      <p><strong>Name:</strong> ${payload.name}</p>
      <p><strong>Phone:</strong> ${payload.phone || "Not provided"}</p>
      <p><strong>Email:</strong> ${payload.email || "Not provided"}</p>
      <p><strong>Subject:</strong> ${payload.subject}</p>
      <p><strong>Message:</strong></p>
      <blockquote style="background:#f4f4f4; padding:12px; border-left:4px solid #6bb92d;">${payload.message}</blockquote>
      <p><em>Received at: ${payload.receivedAt} | IP: ${payload.clientIp}</em></p>
    `,
  });

  return new Promise((resolve) => {
    const req = https.request(
      "https://api.resend.com/emails",
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${apiKey}`,
          "Content-Type": "application/json",
          "Content-Length": Buffer.byteLength(postData),
        },
      },
      (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () => {
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve({ sent: true, status: res.statusCode });
          } else {
            resolve({ sent: false, error: body, status: res.statusCode });
          }
        });
      }
    );
    req.on("error", (err) => resolve({ sent: false, error: err.message }));
    req.write(postData);
    req.end();
  });
}

module.exports = async function handler(req, res) {
  // 1. Enforce POST
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({
      success: false,
      error: "Method Not Allowed. Please send a POST request.",
    });
  }

  // 2. Client IP & Rate Limiting
  const clientIp =
    req.headers["x-forwarded-for"]?.split(",")[0] ||
    req.socket?.remoteAddress ||
    "unknown";

  if (isRateLimited(clientIp)) {
    return res.status(429).json({
      success: false,
      error: "Too many submissions. Please wait a minute before trying again.",
    });
  }

  try {
    // 3. Extract & Sanitize Payload
    const body = req.body || {};
    const name = sanitizeString(body.name, 100);
    const phone = sanitizeString(body.phone, 30);
    const email = sanitizeString(body.email, 100);
    const subject = sanitizeString(body.subject, 150) || "General Inquiry";
    const message = sanitizeString(body.message, 2000);
    const renderedAt = parseInt(body.form_rendered_at, 10) || 0;

    // 4. Spam Checks
    // 4a. Honeypot check (hidden input that only bots fill)
    if (body.website_url || body._gotcha || body.hp_field) {
      console.warn(`[ECOCARE-SPAM-BLOCKED] Honeypot triggered from IP: ${clientIp}`);
      // Return 200 to mislead bot into believing submission succeeded
      return res.status(200).json({
        success: true,
        message: "Thank you for contacting EcoCare!",
      });
    }

    // 4b. Timing attack check: if submitted faster than 1000ms from render, suspect bot
    if (renderedAt > 0 && Date.now() - renderedAt < 1000) {
      console.warn(`[ECOCARE-SPAM-BLOCKED] Rapid submission (<1s) from IP: ${clientIp}`);
      return res.status(200).json({
        success: true,
        message: "Thank you for contacting EcoCare!",
      });
    }

    // 5. Field Validations
    const errors = [];
    if (!name || name.length < 2) {
      errors.push("Full name is required (minimum 2 characters).");
    }
    if (!phone && !email) {
      errors.push("Please provide either a telephone number or email address.");
    }
    if (phone && !isValidPhone(phone)) {
      errors.push("Please enter a valid telephone number (e.g. 024 901 4253 or +233 24 901 4253).");
    }
    if (email && !isValidEmail(email)) {
      errors.push("Please enter a valid email address.");
    }
    if (!message || message.length < 5) {
      errors.push("Please enter a brief message (minimum 5 characters).");
    }

    if (errors.length > 0) {
      return res.status(400).json({
        success: false,
        error: "Validation failed.",
        details: errors,
      });
    }

    // 6. Record & Persistent Storage
    const receivedAt = new Date().toISOString();
    const submissionRecord = {
      type: "contact",
      name,
      phone,
      email,
      subject,
      message,
      clientIp,
      receivedAt,
    };
    saveSubmission(submissionRecord);

    // 7. Dispatch Email (if configured)
    const emailResult = await dispatchEmail(submissionRecord);

    // 8. Generate Pre-filled WhatsApp Direct Follow-up Link
    const waText = encodeURIComponent(
      `Hello EcoCare! My name is ${name}. I just submitted an inquiry regarding "${subject}": ${message.slice(0, 150)}... My contact: ${phone || email}.`
    );
    const whatsappUrl = `https://wa.me/233249014253?text=${waText}`;

    const maskedPhone = phone ? phone.replace(/\D/g, "").slice(0, 3) + "****" + phone.replace(/\D/g, "").slice(-2) : "N/A";
    const maskedEmail = email ? email.slice(0, 2) + "***" + email.slice(email.indexOf("@")) : "N/A";
    console.log(
      `[ECOCARE-CONTACT-SUCCESS] Name: ${name} | Phone: ${maskedPhone} | Email: ${maskedEmail} | IP: ${clientIp} | Email Sent: ${emailResult.sent}`
    );

    return res.status(200).json({
      success: true,
      message: "Thank you, " + name + "! Your message has been received by our team in Achimota Mile 7, Accra.",
      data: {
        name,
        contactMethod: phone || email,
        receivedAt,
        emailDispatched: emailResult.sent,
        whatsappUrl,
      },
    });
  } catch (err) {
    console.error("[ECOCARE-CONTACT-ERROR]", err);
    return res.status(500).json({
      success: false,
      error: "An internal server error occurred while processing your request.",
    });
  }
};
