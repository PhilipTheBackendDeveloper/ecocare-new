/**
 * EcoCare Cleaning Services Limited — Client-Side Controller
 * Handles native Netlify Forms validation, spam protection, asynchronous submission,
 * accessible feedback alerts, and instant WhatsApp dispatch integration.
 */
(function ($) {
  "use strict";

  $(document).ready(function () {
    // 1. Stamp all forms with render timestamp for bot timing detection
    var renderTimestamp = Date.now();
    $('form.contact-form-box, form#contact-form, form#quote-calculator-form, form#ecocare-booking-form, form#quick-inquiry-form').each(function () {
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
          "sofa-cleaning": "upholstery",
          "sofa-carpet": "sofa-carpet",
          "sofa": "sofa-carpet",
          "polytank": "polytank",
          "water-tank": "polytank",
          "tank": "polytank",
          "car-detailing": "car-detailing",
          "detailing": "car-detailing",
          "car-interior": "car-detailing",
          "car": "car-detailing",
          "vehicle": "car-detailing",
          "curtains": "laundry",
          "duvets": "laundry",
          "bedspreads": "laundry",
          "dusting": "dusting",
          "dust": "dusting",
          "deep-clean": "post-construction",
          "post-construction": "post-construction"
        };
        var targetVal = serviceMap[prefillService.toLowerCase()] || prefillService;
        serviceSelect.val(targetVal).trigger("change");
      }
    }

    // 3. Helper: Ghana & International Phone Validation
    // Supports 10-digit Ghana local format (02x, 05x, 03x), +233, and international E.164
    function isValidPhone(phone) {
      if (!phone) return false;
      var clean = phone.replace(/[^0-9+]/g, "");
      return clean.length >= 9 && clean.length <= 16;
    }

    // 4. Helper: Email Validation (RFC 5322 regex)
    function isValidEmail(email) {
      if (!email) return false;
      return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.trim());
    }

    // 5. Universal Netlify Form Submission Handler
    $(document).on("submit", "form.contact-form-box, form#contact-form, form#quote-calculator-form, form#ecocare-booking-form, form#quick-inquiry-form", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();

      var form = $(this);
      var formEl = form[0];
      var responseBox = form.find(".form-response");
      if (!responseBox.length) {
        responseBox = $('<div class="form-response mt-3" role="status" aria-live="polite"></div>').appendTo(form);
      }

      var submitBtn = form.find('button[type="submit"]');
      var originalBtnHtml = submitBtn.html();

      // Collect form fields as key-value pairs
      var formDataArray = form.serializeArray();
      var payload = {};
      $.each(formDataArray, function (i, field) {
        payload[field.name] = field.value;
      });

      // Multi-layer Bot Protection: Honeypots
      if (payload.website_url || payload["bot-field"]) {
        // Disarm bot silently without tipping off crawler
        responseBox.html(
          '<div class="alert alert-success" role="alert"><i class="fas fa-check-circle"></i> Thank you! Your request has been received.</div>'
        );
        formEl.reset();
        return false;
      }

      // Multi-layer Bot Protection: Rapid Timing Attack (< 1s from render)
      var renderedAt = parseInt(form.find('input[name="form_rendered_at"]').val(), 10);
      if (renderedAt && Date.now() - renderedAt < 1000) {
        responseBox.html(
          '<div class="alert alert-warning" role="alert"><i class="fas fa-clock mr-1"></i> Please take a moment to review your details before submitting.</div>'
        );
        return false;
      }

      // Determine form name and identity
      var formName = form.attr("name") || form.find('input[name="form-name"]').val();
      var isQuoteForm = Boolean(
        formName === "quote-calculator" ||
        form.attr("id") === "ecocare-booking-form" ||
        form.attr("id") === "quote-calculator-form" ||
        form.find('select[name="service"]').length ||
        window.location.pathname.indexOf("calculate-form") !== -1
      );

      if (!formName) {
        formName = isQuoteForm ? "quote-calculator" : "contact";
      }

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

      // Set Loading State and debounce submit button
      submitBtn.prop("disabled", true).html('<i class="fas fa-spinner fa-spin mr-1"></i> Submitting Request...');
      responseBox.html(
        '<div class="alert alert-info" role="alert" style="border-radius:4px; padding:10px 14px;">' +
        '<i class="fas fa-info-circle mr-1"></i> Submitting your inquiry to EcoCare dispatch...' +
        '</div>'
      );

      // Function to show verified success message with WhatsApp follow-up button
      function showSuccess() {
        formEl.reset();
        submitBtn.prop("disabled", false).html(originalBtnHtml);

        var serviceLabel = payload.service || payload.subject || "Cleaning Services";
        var waText = encodeURIComponent(
          "Hello EcoCare! I just submitted an inquiry on your website.\n" +
          "Name: " + nameVal + "\n" +
          "Contact: " + (phoneVal || emailVal) + "\n" +
          "Service: " + serviceLabel + "\n" +
          (locationVal ? "Location: " + locationVal + "\n" : "") +
          "Details: " + messageVal
        );
        var waUrl = "https://wa.me/233249014253?text=" + waText;
        var safeName = $("<div>").text(nameVal).html();
        var safeContact = $("<div>").text(phoneVal || emailVal).html();

        responseBox.html(
          '<div class="alert alert-success" role="alert" style="background:#d4edda; border-color:#c3e6cb; color:#155724; border-radius:4px; padding:16px;">' +
          '<h5 style="color:#155724; font-weight:700; margin-bottom:8px;"><i class="fas fa-check-circle mr-1"></i> Inquiry Received Successfully!</h5>' +
          '<p style="margin-bottom:10px; font-size:14px; line-height:22px;">' +
          'Thank you, <strong>' + safeName + '</strong>! Your inquiry has been delivered directly to EcoCare Cleaning Services Limited. Our dispatch desk in Achimota Mile 7 will review your scope and contact you at <strong>' + safeContact + '</strong> shortly.' +
          '</p>' +
          '<div class="mt-2 pt-2 border-top" style="border-color:#c3e6cb !important;">' +
          '<a href="' + waUrl + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm" style="background:#25d366; color:#fff; font-weight:600; padding:6px 14px; border-radius:4px; display:inline-block;">' +
          '<i class="fab fa-whatsapp mr-1"></i> Connect With Dispatch on WhatsApp' +
          '</a>' +
          '<span class="ml-2 text-muted" style="font-size:12px;">(Optional instant chat)</span>' +
          '</div>' +
          '</div>'
        );
      }

      // Function to handle failure / fallback without falsely claiming success
      function showFallbackError(errMsg) {
        submitBtn.prop("disabled", false).html(originalBtnHtml);
        var serviceLabel = payload.service || payload.subject || "Cleaning Services";
        var directWaText = encodeURIComponent(
          "Hello EcoCare! My name is " + nameVal + ". I attempted to submit an inquiry (" + serviceLabel + ") via your website but encountered a connection issue.\n" +
          "Phone: " + phoneVal + "\n" +
          (locationVal ? "Location: " + locationVal + "\n" : "") +
          "Details: " + messageVal
        );
        var directWa = "https://wa.me/233249014253?text=" + directWaText;

        responseBox.html(
          '<div class="alert alert-warning" role="alert" style="border-radius:4px; padding:14px;">' +
          '<p class="mb-2"><strong><i class="fas fa-exclamation-triangle mr-1"></i> Notice:</strong> ' + (errMsg || "We could not connect to the automated mail server.") + '</p>' +
          '<p class="mb-2" style="font-size:13px;">Your request is important to us! Please connect directly with our dispatch team via:</p>' +
          '<div class="d-flex flex-wrap align-items-center mt-2">' +
          '<a href="' + directWa + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm mr-2 mb-2" style="background:#25d366; color:#fff; font-weight:600;">' +
          '<i class="fab fa-whatsapp mr-1"></i> Send on WhatsApp (+233 24 901 4253)' +
          '</a>' +
          '<a href="tel:+233249014253" class="btn btn-sm btn-dark mr-2 mb-2 font-weight-bold">' +
          '<i class="fas fa-phone mr-1"></i> Call +233 24 901 4253' +
          '</a>' +
          '<a href="mailto:ecocaregh1on1@gmail.com?subject=EcoCare%20Website%20Inquiry" class="btn btn-sm btn-outline-secondary mb-2">' +
          '<i class="far fa-envelope mr-1"></i> Email Dispatch' +
          '</a>' +
          '</div>' +
          '</div>'
        );
      }

      // Build Netlify-compatible x-www-form-urlencoded payload
      var postData = form.serialize();
      if (postData.indexOf("form-name=") === -1) {
        postData = "form-name=" + encodeURIComponent(formName) + "&" + postData;
      }

      // Submit via AJAX POST to current path or root /
      $.ajax({
        url: form.attr("action") || "/",
        type: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        data: postData,
        timeout: 12000,
        success: function (res, textStatus, xhr) {
          // In Netlify, successful form submission returns 2xx HTTP status
          showSuccess();
        },
        error: function (xhr, textStatus) {
          // Never claim success on error
          var errorMsg = "Could not deliver your request online due to a network connection issue.";
          if (textStatus === "timeout") {
            errorMsg = "The submission request timed out. Please check your internet connection.";
          }
          showFallbackError(errorMsg);
        }
      });

      return false;
    });

    // 6. EcoCare Hero Video Background Controller & Mobile Autoplay Assurance
    var heroVideo = document.getElementById("hero-bg-video");
    if (heroVideo) {
      // Ensure strict mobile autoplay policy compliance
      heroVideo.muted = true;
      heroVideo.defaultMuted = true;
      heroVideo.playsInline = true;
      heroVideo.setAttribute("playsinline", "");
      heroVideo.setAttribute("webkit-playsinline", "");

      // Safe autoplay trigger
      var playPromise = heroVideo.play();
      if (playPromise !== undefined) {
        playPromise.catch(function () {
          // If browser policy deferred playback, kick off on very first tap or touch
          $(document).one("touchstart click scroll", function () {
            if (heroVideo.paused) {
              heroVideo.play().catch(function () {});
            }
          });
        });
      }

      // Smooth playlist auto-cycling between background video clips
      var playlist = ["video-background.mp4", "video-background1.mp4"];
      var currentIdx = 0;
      heroVideo.addEventListener("ended", function () {
        currentIdx = (currentIdx + 1) % playlist.length;
        heroVideo.src = playlist[currentIdx];
        heroVideo.load();
        heroVideo.play().catch(function () {});
      });
    }
  });
})(jQuery);
