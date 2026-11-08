/**
 * EcoCare Cleaning Services Limited — Vercel Serverless Function: Quote Requests
 * Route: POST /api/quote
 * Validates incoming quote/booking calculator data and dispatches notification safely.
 */

const RATE_LIMIT_WINDOW_MS = 60 * 1000;
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

function sanitizeString(str, maxLength = 500) {
  if (typeof str !== "string") return "";
  return str
    .replace(/[<>]/g, "")
    .trim()
    .slice(0, maxLength);
}

function isValidPhone(phone) {
  if (!phone || typeof phone !== "string") return false;
  const digits = phone.replace(/[^\d+]/g, "");
  return digits.length >= 9 && digits.length <= 16;
}

function isValidEmail(email) {
  if (!email || typeof email !== "string") return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
}

const ALLOWED_SERVICES = [
  "residential",
  "commercial",
  "post-construction",
  "laundry",
  "pest-control",
  "carpet",
  "upholstery",
  "floor",
  "window",
  "event",
];

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({
      success: false,
      error: "Method Not Allowed. Please send a POST request.",
    });
  }

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
    const body = req.body || {};
    const name = sanitizeString(body.name, 100);
    const phone = sanitizeString(body.phone, 30);
    const email = sanitizeString(body.email, 100);
    const location = sanitizeString(body.location, 150);
    const service = sanitizeString(body.service, 50).toLowerCase();
    const propertyType = sanitizeString(body.property_type, 50) || "unspecified";
    const size = sanitizeString(body.size, 50) || "unspecified";
    const preferredDate = sanitizeString(body.preferred_date, 30);
    const notes = sanitizeString(body.notes, 2000);

    // Honeypot spam check
    if (body.website_url || body._gotcha) {
      return res.status(200).json({ success: true, message: "Thank you for requesting a quote!" });
    }

    const errors = [];
    if (!name || name.length < 2) {
      errors.push("Full name is required (minimum 2 characters).");
    }
    if (!phone || !isValidPhone(phone)) {
      errors.push("A valid telephone number is required (e.g. 024 901 4253 or +233 24 901 4253).");
    }
    if (email && !isValidEmail(email)) {
      errors.push("Please enter a valid email address.");
    }
    if (!location || location.length < 2) {
      errors.push("Your location in Greater Accra is required.");
    }
    if (!service || (!ALLOWED_SERVICES.includes(service) && service.length < 3)) {
      errors.push("Please select a valid service from the options provided.");
    }

    if (errors.length > 0) {
      return res.status(400).json({
        success: false,
        error: "Validation failed.",
        details: errors,
      });
    }

    const maskedPhone = phone.replace(/(\d{3})\d+(\d{2})/, "$1****$2");
    console.log(
      `[ECOCARE-QUOTE] Name: ${name} | Phone: ${maskedPhone} | Service: ${service} | Location: ${location} | IP: ${clientIp}`
    );

    return res.status(200).json({
      success: true,
      message: "Your service quote request has been received by EcoCare.",
      data: {
        name,
        service,
        location,
        phoneReceived: true,
        receivedAt: new Date().toISOString(),
      },
    });
  } catch (err) {
    console.error("[ECOCARE-QUOTE-ERROR]", err);
    return res.status(500).json({
      success: false,
      error: "An internal server error occurred while processing your request.",
    });
  }
};

