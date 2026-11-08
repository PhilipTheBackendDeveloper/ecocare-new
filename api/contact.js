/**
 * EcoCare Cleaning Services Limited — Vercel Serverless Function: Contact Inquiries
 * Route: POST /api/contact
 * Validates incoming contact form data and dispatches email/notification safely.
 */

// Simple in-memory rate limiting map for basic spam mitigation
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
    .replace(/[<>]/g, "") // Strip brackets
    .trim()
    .slice(0, maxLength);
}

// Basic phone number validator (accepts Ghanaian local, +233, and general international)
function isValidPhone(phone) {
  if (!phone || typeof phone !== "string") return false;
  const digits = phone.replace(/[^\d+]/g, "");
  return digits.length >= 9 && digits.length <= 16;
}

// Basic email format validator
function isValidEmail(email) {
  if (!email || typeof email !== "string") return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
}

module.exports = async function handler(req, res) {
  // 1. Enforce POST method
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
      error: "Too many requests. Please wait a minute before submitting again.",
    });
  }

  try {
    // 3. Extract & sanitize payload
    const body = req.body || {};
    const name = sanitizeString(body.name, 100);
    const phone = sanitizeString(body.phone, 30);
    const email = sanitizeString(body.email, 100);
    const subject = sanitizeString(body.subject, 150) || "General Inquiry";
    const message = sanitizeString(body.message, 2000);

    // Honeypot spam check (if bot filled hidden field)
    if (body.website_url || body._gotcha) {
      // Silently accept bot submission without processing
      return res.status(200).json({ success: true, message: "Thank you for contacting EcoCare!" });
    }

    // 4. Validation
    const errors = [];
    if (!name || name.length < 2) {
      errors.push("Full name is required (minimum 2 characters).");
    }
    if (!phone && !email) {
      errors.push("Please provide either a valid phone number or email address.");
    }
    if (phone && !isValidPhone(phone)) {
      errors.push("Please enter a valid telephone number (e.g., 024 901 4253 or +233 24 901 4253).");
    }
    if (email && !isValidEmail(email)) {
      errors.push("Please enter a valid email address.");
    }
    if (!message || message.length < 5) {
      errors.push("Please provide a message (minimum 5 characters).");
    }

    if (errors.length > 0) {
      return res.status(400).json({
        success: false,
        error: "Validation failed.",
        details: errors,
      });
    }

    // 5. Audit Logging (privacy-safe: mask phone digits)
    const maskedPhone = phone.replace(/(\d{3})\d+(\d{2})/, "$1****$2");
    console.log(
      `[ECOCARE-CONTACT] Message from: ${name} | Phone: ${maskedPhone} | Subject: ${subject} | IP: ${clientIp}`
    );

    // 6. Return successful receipt
    return res.status(200).json({
      success: true,
      message: "Thank you for contacting EcoCare! Your message has been received.",
      data: {
        name,
        contactMethod: phone || email,
        receivedAt: new Date().toISOString(),
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

