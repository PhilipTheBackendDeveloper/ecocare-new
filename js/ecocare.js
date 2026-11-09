/**
 * EcoCare Cleaning Services Limited — Client-Side Controller
 * Handles form validation, spam protection, asynchronous submission to API / PHP,
 * accessible feedback alerts, and instant WhatsApp dispatch integration.
 */
(function ($) {
  "use strict";

  $(document).ready(function () {
    // 1. Stamp all forms with render timestamp for bot timing detection
    var renderTimestamp = Date.now();
    $('form.contact-form-box, form#contact-form, form#ecocare-booking-form').each(function () {
      var form = $(this);
      if (!form.find('input[name="form_rendered_at"]').length) {
        form.append('<input type="hidden" name="form_rendered_at" value="' + renderTimestamp + '">');
      }
      // Ensure invisible honeypot field is present
      if (!form.find('input[name="website_url"]').length) {
        form.append(
          '<div style="display:none !important; position:absolute; left:-9999px;" aria-hidden="true">' +
          '<input type="text" name="website_url" tabindex="-1" autocomplete="off" value="">' +
          '</div>'
        );
      }
    });

    // 2. URL Query Parameter Prefill for Services & Packages
    function getQueryParam(param) {
      var urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    var prefillService = getQueryParam("service") || getQueryParam("plan");
    if (prefillService) {
      var serviceSelect = $('select[name="service"], #booking-service-select, #form-service');
      if (serviceSelect.length) {
        var serviceMap = {
          "cleaning": "residential",
          "residential": "residential",
          "commercial": "commercial",
          "office": "commercial",
          "corporate": "commercial",
          "laundry": "laundry",
          "fumigation": "fumigation",
          "pest": "fumigation",
          "pest-control": "fumigation",
          "carpet": "carpet",
          "upholstery": "upholstery",
          "deep-clean": "post-construction",
          "post-construction": "post-construction"
        };
        var targetVal = serviceMap[prefillService.toLowerCase()] || prefillService;
        serviceSelect.val(targetVal).trigger("change");
      }
    }

    // 3. Helper: Basic Ghana & International Phone Validation
    function isValidPhone(phone) {
      if (!phone) return false;
      var clean = phone.replace(/[^0-9+]/g, "");
      return clean.length >= 9 && clean.length <= 16;
    }

    // 4. Helper: Email Validation
    function isValidEmail(email) {
      if (!email) return false;
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
    }

    // 5. Universal Form Submission Handler
    $(document).on("submit", "form.contact-form-box, form#contact-form, form#ecocare-booking-form", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();

      var form = $(this);
      var responseBox = form.find(".form-response");
      if (!responseBox.length) {
        responseBox = $('<div class="form-response mt-3"></div>').appendTo(form);
      }

      var submitBtn = form.find('button[type="submit"]');
      var originalBtnHtml = submitBtn.html();

      // Collect form fields as key-value pairs
      var formDataArray = form.serializeArray();
      var payload = {};
      $.each(formDataArray, function (i, field) {
        payload[field.name] = field.value;
      });

      // Honeypot check on client side
      if (payload.website_url) {
        // Disarm bot without feedback
        responseBox.html(
          '<div class="alert alert-success" role="alert"><i class="fas fa-check-circle"></i> Thank you! Your request has been received.</div>'
        );
        form[0].reset();
        return false;
      }

      // Determine form type
      var isQuoteForm = Boolean(
        form.attr("id") === "ecocare-booking-form" ||
        form.find('select[name="service"]').length ||
        window.location.pathname.indexOf("calculate-form") !== -1
      );

      var primaryEndpoint = isQuoteForm ? "/api/quote" : "/api/contact";
      var fallbackEndpoint = isQuoteForm ? "vendor/php/quote-process.php" : "vendor/php/form-process.php";

      // Client-Side Validation
      var errors = [];
      var nameVal = (payload.name || "").trim();
      var phoneVal = (payload.phone || "").trim();
      var emailVal = (payload.email || "").trim();
      var messageVal = (payload.message || payload.notes || "").trim();
      var locationVal = (payload.location || "").trim();

      if (nameVal.length < 2) {
        errors.push("Full name is required (minimum 2 characters).");
      }

      if (isQuoteForm) {
        if (!phoneVal || !isValidPhone(phoneVal)) {
          errors.push("A valid telephone number is required (e.g. 024 901 4253 or +233 24 901 4253).");
        }
        if (!locationVal) {
          errors.push("Please provide your area or landmark in Greater Accra.");
        }
        if (messageVal.length < 5) {
          errors.push("Please enter brief details about your service requirements.");
        }
      } else {
        if (!phoneVal && !emailVal) {
          errors.push("Please provide either a telephone number or email address.");
        }
        if (phoneVal && !isValidPhone(phoneVal)) {
          errors.push("Please enter a valid telephone number (e.g. 024 901 4253).");
        }
        if (emailVal && !isValidEmail(emailVal)) {
          errors.push("Please enter a valid email address.");
        }
        if (messageVal.length < 5) {
          errors.push("Please enter your message (minimum 5 characters).");
        }
      }

      if (errors.length > 0) {
        responseBox.html(
          '<div class="alert alert-danger" role="alert" style="border-radius:4px; padding:12px 16px;">' +
          '<strong><i class="fas fa-exclamation-circle mr-1"></i> Please check the required fields:</strong>' +
          '<ul class="mb-0 mt-1 pl-3" style="font-size:13px;">' +
          errors.map(function (err) { return '<li>' + err + '</li>'; }).join('') +
          '</ul>' +
          '</div>'
        );
        return false;
      }

      // Set Loading State
      submitBtn.prop("disabled", true).html('<i class="fas fa-spinner fa-spin mr-1"></i> Submitting Request...');
      responseBox.html(
        '<div class="alert alert-info" role="alert" style="border-radius:4px; padding:10px 14px;">' +
        '<i class="fas fa-info-circle mr-1"></i> Processing your submission with EcoCare dispatch...' +
        '</div>'
      );

      // Function to show success message with WhatsApp follow-up button
      function showSuccess(data) {
        form[0].reset();
        submitBtn.prop("disabled", false).html(originalBtnHtml);

        var waUrl = (data && data.whatsappUrl) || "https://wa.me/233249014253";
        var safeName = $("<div>").text(nameVal).html();
        var safePhone = $("<div>").text(phoneVal || emailVal).html();

        responseBox.html(
          '<div class="alert alert-success" role="alert" style="background:#d4edda; border-color:#c3e6cb; color:#155724; border-radius:4px; padding:16px;">' +
          '<h5 style="color:#155724; font-weight:700; margin-bottom:8px;"><i class="fas fa-check-circle mr-1"></i> Inquiry Received Successfully!</h5>' +
          '<p style="margin-bottom:10px; font-size:14px; line-height:22px;">Thank you, <strong>' + safeName + '</strong>! Our team in Achimota Mile 7, Accra has received your details. We will contact you at <strong>' + safePhone + '</strong> shortly with your tailored scope.</p>' +
          '<div class="mt-2 pt-2 border-top" style="border-color:#c3e6cb !important;">' +
          '<a href="' + waUrl + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm" style="background:#25d366; color:#fff; font-weight:600; padding:6px 14px; border-radius:4px; display:inline-block;">' +
          '<i class="fab fa-whatsapp mr-1"></i> Notify EcoCare Dispatch on WhatsApp' +
          '</a>' +
          '<span class="ml-2 text-muted" style="font-size:12px;">(Optional instant chat)</span>' +
          '</div>' +
          '</div>'
        );
      }

      // Function to handle failure / fallback
      function showFallbackError(errMsg) {
        submitBtn.prop("disabled", false).html(originalBtnHtml);
        var directWaText = encodeURIComponent(
          "Hello EcoCare! My name is " + nameVal + ". I was attempting to submit an inquiry (" + (payload.service || "Cleaning") + ") from your website. My phone is " + phoneVal + "."
        );
        var directWa = "https://wa.me/233249014253?text=" + directWaText;

        responseBox.html(
          '<div class="alert alert-warning" role="alert" style="border-radius:4px; padding:14px;">' +
          '<p class="mb-2"><strong><i class="fas fa-info-circle mr-1"></i> Notice:</strong> ' + (errMsg || "We could not connect to the automated mail server.") + '</p>' +
          '<p class="mb-2" style="font-size:13px;">Your request is important to us. Please connect directly with our dispatch supervisor:</p>' +
          '<a href="' + directWa + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm" style="background:#25d366; color:#fff; font-weight:600;">' +
          '<i class="fab fa-whatsapp mr-1"></i> Click to Send on WhatsApp (+233 24 901 4253)' +
          '</a>' +
          '<span class="ml-2" style="font-size:13px;">or call <a href="tel:+233249014253" style="font-weight:700; color:#333;">+233 24 901 4253</a></span>' +
          '</div>'
        );
      }

      // Execute submission via JSON POST to Node Serverless endpoint
      $.ajax({
        url: primaryEndpoint,
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(payload),
        dataType: "json",
        timeout: 10000,
        success: function (res) {
          if (res && res.success) {
            showSuccess(res.data);
          } else {
            showFallbackError(res.error || (res.details ? res.details.join(", ") : ""));
          }
        },
        error: function (xhr) {
          // If 400 Bad Request, show validation error
          if (xhr.status === 400 && xhr.responseJSON) {
            submitBtn.prop("disabled", false).html(originalBtnHtml);
            var errList = xhr.responseJSON.details || [xhr.responseJSON.error || "Validation failed."];
            responseBox.html(
              '<div class="alert alert-danger" role="alert">' +
              errList.join("<br>") +
              '</div>'
            );
            return;
          }
          // If /api is not hosted (e.g. PHP Apache hosting), attempt fallback to PHP endpoint
          $.ajax({
            url: fallbackEndpoint,
            type: "POST",
            data: form.serialize(),
            dataType: "json",
            timeout: 8000,
            success: function (phpRes) {
              if (phpRes && phpRes.success) {
                showSuccess(phpRes.data);
              } else {
                showFallbackError(phpRes.message || "");
              }
            },
            error: function () {
              showFallbackError("Network or server connection issue.");
            }
          });
        }
      });

      return false;
    });
  });
})(jQuery);
