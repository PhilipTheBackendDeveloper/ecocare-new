/**
 * EcoCare Cleaning Services Limited — Vercel Serverless Function: Quote & Booking Calculator
 * Route: POST /api/quote
 * Validates incoming quote/booking request, logs submission, dispatches notification, and provides WhatsApp follow-up.
 */

const fs = require("fs");
const path = require("path");
const https = require("https");

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

async function dispatchEmail(payload) {
  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    return { sent: false, reason: "No RESEND_API_KEY configured in environment" };
  }

  const notificationEmail = process.env.NOTIFICATION_EMAIL || "ecocaregh1on1@gmail.com";
  const postData = JSON.stringify({
    from: "EcoCare Estimate Calculator <onboarding@resend.dev>",
    to: [notificationEmail],
    subject: `New EcoCare Quote Request: ${payload.service} (${payload.name})`,
    html: `
      <h2>New Quote & Estimate Request Received</h2>
      <p><strong>Customer Name:</strong> ${payload.name}</p>
      <p><strong>Phone:</strong> ${payload.phone}</p>
      <p><strong>Email:</strong> ${payload.email || "Not provided"}</p>
      <p><strong>Service Requested:</strong> ${payload.service}</p>
      <p><strong>Property Type:</strong> ${payload.propertyType}</p>
      <p><strong>Approx Size / Scope:</strong> ${payload.size}</p>
      <p><strong>Bedrooms / Rooms:</strong> ${payload.rooms || "N/A"}</p>
      <p><strong>Bathrooms / Washrooms:</strong> ${payload.bathrooms || "N/A"}</p>
      <p><strong>Frequency:</strong> ${payload.frequency || "One-Time"}</p>
      <p><strong>Location / Landmark:</strong> ${payload.location}</p>
      <p><strong>Preferred Appointment:</strong> ${payload.preferredDate || "Flexible"} at ${payload.preferredTime || "Flexible"}</p>
      <p><strong>Requirements / Notes:</strong></p>
      <blockquote style="background:#f4f4f4; padding:12px; border-left:4px solid #6bb92d;">${payload.notes}</blockquote>
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
      error: "Too many submissions. Please wait a minute before trying again.",
    });
  }

  try {
    const body = req.body || {};
    const name = sanitizeString(body.name, 100);
    const phone = sanitizeString(body.phone, 30);
    const email = sanitizeString(body.email, 100);
    const location = sanitizeString(body.location, 150);
    const service = sanitizeString(body.service, 80) || "General Cleaning";
    const propertyType = sanitizeString(body.property_type, 60) || "Residential";
    const size = sanitizeString(body.size_sqm || body.size, 60) || "Standard";
    const rooms = sanitizeString(body.rooms, 40) || "N/A";
    const bathrooms = sanitizeString(body.bathrooms, 40) || "N/A";
    const frequency = sanitizeString(body.frequency, 40) || "One-Time";
    const preferredDate = sanitizeString(body.date || body.preferred_date, 40);
    const preferredTime = sanitizeString(body.time || body.preferred_time, 40);
    const notes = sanitizeString(body.message || body.notes, 2000);
    const renderedAt = parseInt(body.form_rendered_at, 10) || 0;

    // Honeypot spam check
    if (body.website_url || body._gotcha || body.hp_field) {
      console.warn(`[ECOCARE-SPAM-BLOCKED] Quote Honeypot triggered from IP: ${clientIp}`);
      return res.status(200).json({
        success: true,
        message: "Thank you for requesting an estimate from EcoCare!",
      });
    }

    // Timing check (<1s is automated bot)
    if (renderedAt > 0 && Date.now() - renderedAt < 1000) {
      console.warn(`[ECOCARE-SPAM-BLOCKED] Rapid quote submission (<1s) from IP: ${clientIp}`);
      return res.status(200).json({
        success: true,
        message: "Thank you for requesting an estimate from EcoCare!",
      });
    }

    // Validation
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
      errors.push("Please provide your area or landmark in Greater Accra.");
    }
    if (!notes || notes.length < 5) {
      errors.push("Please provide brief service or property address notes (minimum 5 characters).");
    }

    if (errors.length > 0) {
      return res.status(400).json({
        success: false,
        error: "Validation failed.",
        details: errors,
      });
    }

    const receivedAt = new Date().toISOString();
    const submissionRecord = {
      type: "quote",
      name,
      phone,
      email,
      service,
      propertyType,
      size,
      rooms,
      bathrooms,
      frequency,
      location,
      preferredDate,
      preferredTime,
      notes,
      clientIp,
      receivedAt,
    };
    saveSubmission(submissionRecord);

    const emailResult = await dispatchEmail(submissionRecord);

    // Pre-filled WhatsApp link for instant estimate discussion
    const waText = encodeURIComponent(
      `Hello EcoCare! My name is ${name}. I just requested an estimate on your website for ${service} at ${location}. Property details: ${propertyType}, ${size}. Preferred date: ${preferredDate || "Flexible"}. Notes: ${notes.slice(0, 120)}... Contact: ${phone}.`
    );
    const whatsappUrl = `https://wa.me/233249014253?text=${waText}`;

    const maskedPhone = phone ? phone.replace(/\D/g, "").slice(0, 3) + "****" + phone.replace(/\D/g, "").slice(-2) : "N/A";
    const maskedEmail = email ? email.slice(0, 2) + "***" + email.slice(email.indexOf("@")) : "N/A";
    console.log(
      `[ECOCARE-QUOTE-SUCCESS] Name: ${name} | Service: ${service} | Phone: ${maskedPhone} | Email: ${maskedEmail} | Location: ${location} | IP: ${clientIp} | Email Sent: ${emailResult.sent}`
    );

    return res.status(200).json({
      success: true,
      message: "Thank you, " + name + "! Your quotation request has been received by our Achimota office.",
      data: {
        name,
        service,
        location,
        receivedAt,
        emailDispatched: emailResult.sent,
        whatsappUrl,
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
