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

      // Human-readable labels from form dropdowns
      var serviceEl = form.find('select[name="service"] option:selected');
      var serviceLabel = (serviceEl.length && serviceEl.val() ? serviceEl.text().trim() : "") || payload.service || payload.subject || "Cleaning Services";

      var propertyEl = form.find('select[name="property_type"] option:selected');
      var propertyLabel = (propertyEl.length && propertyEl.val() ? propertyEl.text().trim() : "") || payload.property_type || "";

      var sizeEl = form.find('select[name="size_sqm"] option:selected, select[name="size"] option:selected');
      var sizeLabel = (sizeEl.length && sizeEl.val() ? sizeEl.text().trim() : "") || payload.size_sqm || payload.size || "";

      var roomsEl = form.find('select[name="rooms"] option:selected');
      var roomsLabel = (roomsEl.length && roomsEl.val() ? roomsEl.text().trim() : "") || payload.rooms || "";

      var bathroomsEl = form.find('select[name="bathrooms"] option:selected');
      var bathroomsLabel = (bathroomsEl.length && bathroomsEl.val() ? bathroomsEl.text().trim() : "") || payload.bathrooms || "";

      var frequencyEl = form.find('select[name="frequency"] option:selected');
      var frequencyLabel = (frequencyEl.length && frequencyEl.val() ? frequencyEl.text().trim() : "") || payload.frequency || "";

      var dateVal = (payload.date || payload.preferred_date || "").trim();
      var timeVal = (payload.time || payload.preferred_time || "").trim();

      // Build structured WhatsApp dispatch message with complete details
      var waLines = [];
      if (isQuoteForm) {
        waLines.push("✨ *NEW ECOCARE BOOKING REQUEST* ✨");
        waLines.push("--------------------------------");
        waLines.push("👤 *Customer:* " + nameVal);
        waLines.push("📞 *Phone:* " + phoneVal);
        if (emailVal) waLines.push("✉️ *Email:* " + emailVal);
        waLines.push("");
        waLines.push("🧹 *Service:* " + serviceLabel);
        if (propertyLabel) waLines.push("🏢 *Property:* " + propertyLabel);
        if (sizeLabel) waLines.push("📐 *Size / Scope:* " + sizeLabel);
        if (roomsLabel && roomsLabel.toLowerCase() !== "not applicable") waLines.push("🛏️ *Bedrooms:* " + roomsLabel);
        if (bathroomsLabel && bathroomsLabel.toLowerCase() !== "not applicable") waLines.push("🚿 *Bathrooms:* " + bathroomsLabel);
        if (frequencyLabel) waLines.push("🔄 *Frequency:* " + frequencyLabel);
        if (locationVal) waLines.push("📍 *Location / Area:* " + locationVal);
        if (dateVal) waLines.push("📅 *Preferred Date:* " + dateVal);
        if (timeVal) waLines.push("⏰ *Preferred Time:* " + timeVal);
        if (messageVal) {
          waLines.push("");
          waLines.push("📝 *Notes & Requirements:*");
          waLines.push(messageVal);
        }
        waLines.push("--------------------------------");
        waLines.push("_Sent from EcoCare Ghana Website_");
      } else {
        waLines.push("✨ *NEW ECOCARE INQUIRY* ✨");
        waLines.push("--------------------------------");
        waLines.push("👤 *Customer:* " + nameVal);
        if (phoneVal) waLines.push("📞 *Phone:* " + phoneVal);
        if (emailVal) waLines.push("✉️ *Email:* " + emailVal);
        waLines.push("📋 *Subject:* " + (payload.subject || "General Inquiry"));
        waLines.push("");
        waLines.push("💬 *Message Details:*");
        waLines.push(messageVal);
        waLines.push("--------------------------------");
        waLines.push("_Sent from EcoCare Ghana Website_");
      }

      var waMessageStr = waLines.join("\n");
      var waEncoded = encodeURIComponent(waMessageStr);
      var waUrl1 = "https://wa.me/233249014253?text=" + waEncoded;
      var waUrl2 = "https://wa.me/233243807100?text=" + waEncoded;

      // Direct WhatsApp Dispatch: Trigger directly on user submit event to avoid browser popup blocks
      var openedWa = false;
      try {
        var waWin = window.open(waUrl1, "_blank");
        if (waWin && !waWin.closed) {
          openedWa = true;
        }
      } catch (err) {
        openedWa = false;
      }

      // Function to show verified success message with dual WhatsApp & Phone follow-up buttons
      function showSuccess() {
        formEl.reset();
        submitBtn.prop("disabled", false).html(originalBtnHtml);

        var safeName = $("<div>").text(nameVal).html();
        var safePhone = phoneVal ? $("<div>").text(phoneVal).html() : "";
        var safeEmail = emailVal ? $("<div>").text(emailVal).html() : "";
        var safeService = $("<div>").text(serviceLabel).html();
        var safeLocation = locationVal ? $("<div>").text(locationVal).html() : "";
        var safeDate = dateVal ? $("<div>").text(dateVal + (timeVal ? " at " + timeVal : "")).html() : "";
        var safeNotes = $("<div>").text(messageVal).html();

        var receiptHtml =
          '<div class="ecocare-booking-receipt p-3 p-md-4 mt-3" style="background:#ffffff; border:1.5px solid #28a745; border-radius:10px; box-shadow:0 8px 24px rgba(0,0,0,0.08); text-align:left;">' +
            '<div class="d-flex align-items-center mb-3 pb-2 border-bottom">' +
              '<div style="width:40px; height:40px; border-radius:50%; background:#28a745; color:#fff; display:flex; align-items:center; justify-content:center; font-size:20px; margin-right:12px; flex-shrink:0;">' +
                '<i class="fas fa-check"></i>' +
              '</div>' +
              '<div>' +
                '<h5 class="mb-0 font-weight-bold" style="color:#155724; font-size:17px;">Booking &amp; Estimate Successfully Submitted!</h5>' +
                '<p class="mb-0 text-muted" style="font-size:12.5px;">EcoCare Dispatch Desk &bull; Achimota Mile 7, Accra</p>' +
              '</div>' +
            '</div>' +

            '<div class="alert alert-light border d-flex align-items-center p-2 mb-3" style="background:#f8fdf9; border-color:#c3e6cb !important; font-size:13px; color:#155724;">' +
              '<i class="far fa-envelope-open mr-2 text-success fa-lg"></i>' +
              '<span><strong>Email Notification Dispatched:</strong> A copy has been delivered to <strong>ecocaregh1on1@gmail.com</strong>.</span>' +
            '</div>' +

            '<div class="mb-3">' +
              '<p class="mb-2 font-weight-bold" style="font-size:13.5px; color:#1e293b;">' +
                (openedWa
                  ? '<i class="fab fa-whatsapp text-success mr-1"></i> WhatsApp opened with your pre-filled booking details. If you need to reconnect or reach our second line:'
                  : '<i class="fab fa-whatsapp text-success mr-1"></i> Connect directly on WhatsApp with your complete booking details pre-filled:') +
              '</p>' +
              '<div class="d-flex flex-wrap align-items-center">' +
                '<a href="' + waUrl1 + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm mr-2 mb-2 font-weight-bold text-white shadow-sm" style="background:#25d366; padding:8px 16px; border-radius:6px; font-size:13px; display:inline-flex; align-items:center;">' +
                  '<i class="fab fa-whatsapp mr-1 fa-lg"></i> WhatsApp Line 1 (+233 24 901 4253)' +
                '</a>' +
                '<a href="' + waUrl2 + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm mr-2 mb-2 font-weight-bold text-white shadow-sm" style="background:#128c7e; padding:8px 16px; border-radius:6px; font-size:13px; display:inline-flex; align-items:center;">' +
                  '<i class="fab fa-whatsapp mr-1 fa-lg"></i> WhatsApp Line 2 (+233 24 380 7100)' +
                '</a>' +
              '</div>' +
            '</div>' +

            '<div class="mb-3 pb-2 border-bottom">' +
              '<span class="text-muted d-block mb-2" style="font-size:12px; font-weight:600; text-transform:uppercase; letter-spacing:0.5px;">Or Call Dispatch Directly:</span>' +
              '<div class="d-flex flex-wrap align-items-center">' +
                '<a href="tel:+233249014253" class="btn btn-sm btn-outline-dark mr-2 mb-2 font-weight-bold" style="padding:6px 14px; font-size:12.5px; display:inline-flex; align-items:center;">' +
                  '<i class="fas fa-phone-alt mr-1 text-success"></i> +233 24 901 4253' +
                '</a>' +
                '<a href="tel:+233243807100" class="btn btn-sm btn-outline-dark mr-2 mb-2 font-weight-bold" style="padding:6px 14px; font-size:12.5px; display:inline-flex; align-items:center;">' +
                  '<i class="fas fa-phone-alt mr-1 text-success"></i> +233 24 380 7100' +
                '</a>' +
              '</div>' +
            '</div>' +

            '<div class="p-3" style="background:#f8fafc; border-radius:6px; font-size:12.5px; line-height:1.6; border:1px solid #e2e8f0;">' +
              '<div class="font-weight-bold text-uppercase mb-2 text-secondary" style="font-size:11px; letter-spacing:0.5px;">Booking Details Summary</div>' +
              '<div class="row">' +
                '<div class="col-sm-6 mb-1"><strong>Customer:</strong> ' + safeName + '</div>' +
                '<div class="col-sm-6 mb-1"><strong>Contact:</strong> ' + (safePhone || safeEmail) + '</div>' +
                '<div class="col-sm-6 mb-1"><strong>Service:</strong> ' + safeService + '</div>' +
                (safeLocation ? '<div class="col-sm-6 mb-1"><strong>Location:</strong> ' + safeLocation + '</div>' : '') +
                (safeDate ? '<div class="col-sm-6 mb-1"><strong>Preferred Schedule:</strong> ' + safeDate + '</div>' : '') +
                (propertyLabel ? '<div class="col-sm-6 mb-1"><strong>Property:</strong> ' + propertyLabel + '</div>' : '') +
                (sizeLabel ? '<div class="col-sm-6 mb-1"><strong>Scope / Size:</strong> ' + sizeLabel + '</div>' : '') +
              '</div>' +
              (safeNotes ? '<div class="mt-2 pt-2 border-top text-muted" style="border-color:#e2e8f0 !important;"><strong>Notes:</strong> ' + safeNotes + '</div>' : '') +
            '</div>' +
          '</div>';

        responseBox.html(receiptHtml);
      }

      // Function to handle failure / fallback without falsely claiming success
      function showFallbackError(errMsg) {
        submitBtn.prop("disabled", false).html(originalBtnHtml);

        responseBox.html(
          '<div class="alert alert-warning p-3 mt-3" role="alert" style="border-radius:8px; border:1.5px solid #ffc107; text-align:left;">' +
            '<p class="mb-2 font-weight-bold" style="color:#856404;"><i class="fas fa-exclamation-triangle mr-1"></i> Notice: ' + (errMsg || "We could not connect to the automated mail server.") + '</p>' +
            '<p class="mb-2" style="font-size:13px; color:#664d03;">Your booking details are ready! You can send them directly to EcoCare via WhatsApp or phone for immediate confirmation:</p>' +
            '<div class="d-flex flex-wrap align-items-center mt-2">' +
              '<a href="' + waUrl1 + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm mr-2 mb-2 font-weight-bold text-white shadow-sm" style="background:#25d366; padding:8px 16px; border-radius:6px; font-size:13px; display:inline-flex; align-items:center;">' +
                '<i class="fab fa-whatsapp mr-1 fa-lg"></i> Send on WhatsApp Line 1 (+233 24 901 4253)' +
              '</a>' +
              '<a href="' + waUrl2 + '" target="_blank" rel="noopener noreferrer" class="btn btn-sm mr-2 mb-2 font-weight-bold text-white shadow-sm" style="background:#128c7e; padding:8px 16px; border-radius:6px; font-size:13px; display:inline-flex; align-items:center;">' +
                '<i class="fab fa-whatsapp mr-1 fa-lg"></i> Send on WhatsApp Line 2 (+233 24 380 7100)' +
              '</a>' +
              '<a href="tel:+233249014253" class="btn btn-sm btn-dark mr-2 mb-2 font-weight-bold" style="padding:8px 14px; font-size:13px; display:inline-flex; align-items:center;">' +
                '<i class="fas fa-phone mr-1"></i> Call +233 24 901 4253' +
              '</a>' +
              '<a href="tel:+233243807100" class="btn btn-sm btn-outline-dark mr-2 mb-2 font-weight-bold" style="padding:8px 14px; font-size:13px; display:inline-flex; align-items:center;">' +
                '<i class="fas fa-phone mr-1"></i> Call +233 24 380 7100' +
              '</a>' +
              '<a href="mailto:ecocaregh1on1@gmail.com?subject=EcoCare%20Booking%20Request" class="btn btn-sm btn-outline-secondary mb-2 font-weight-bold" style="padding:8px 14px; font-size:13px; display:inline-flex; align-items:center;">' +
                '<i class="far fa-envelope mr-1"></i> Email: ecocaregh1on1@gmail.com' +
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

      // Dual-Engine Submission: Netlify Forms + Vercel Serverless API Fallback
      var isVercelHost = Boolean(window.location.hostname && window.location.hostname.indexOf("vercel.app") !== -1);
      var apiEndpoint = isQuoteForm ? "/api/quote" : "/api/contact";

      function submitToServerlessApi() {
        $.ajax({
          url: apiEndpoint,
          type: "POST",
          headers: { "Content-Type": "application/json" },
          data: JSON.stringify(payload),
          dataType: "json",
          timeout: 10000,
          success: function (res) {
            showSuccess();
          },
          error: function (xhr, textStatus) {
            var errorMsg = "Could not deliver your request online due to a network connection issue.";
            if (textStatus === "timeout") {
              errorMsg = "The submission request timed out. Please check your internet connection.";
            } else if (xhr && xhr.responseJSON && xhr.responseJSON.error) {
              errorMsg = xhr.responseJSON.error;
            }
            showFallbackError(errorMsg);
          }
        });
      }

      function submitToNetlify(onFail) {
        $.ajax({
          url: form.attr("action") || "/",
          type: "POST",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          data: postData,
          timeout: 12000,
          success: function (res, textStatus, xhr) {
            showSuccess();
          },
          error: function (xhr, textStatus) {
            if (onFail) {
              onFail(xhr, textStatus);
            } else {
              var errorMsg = "Could not deliver your request online due to a network connection issue.";
              if (textStatus === "timeout") {
                errorMsg = "The submission request timed out. Please check your internet connection.";
              }
              showFallbackError(errorMsg);
            }
          }
        });
      }

      if (isVercelHost) {
        // On Vercel preview environments, submit directly to serverless API
        submitToServerlessApi();
      } else {
        // On Netlify / production / local environments, submit via Netlify Form with serverless fallback
        submitToNetlify(function (xhr, textStatus) {
          if (xhr.status === 403 || xhr.status === 404 || xhr.status === 405) {
            submitToServerlessApi();
          } else {
            var errorMsg = "Could not deliver your request online due to a network connection issue.";
            if (textStatus === "timeout") {
              errorMsg = "The submission request timed out. Please check your internet connection.";
            }
            showFallbackError(errorMsg);
          }
        });
      }

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

    // 7. EcoCare Mobile Navigation Drawer Controller (Full-Screen & Body Lock)
    var drawerOpen = false;
    var drawerReveal = null;
    var drawerNav = null;
    var navigatingFromDrawer = false;

    function syncMobileDrawer() {
      var reveal = document.querySelector(".mean-container .meanmenu-reveal");
      var nav = reveal && reveal.parentNode.querySelector(".mean-nav");
      var isOpen = !!(window.innerWidth <= 991 && reveal && nav &&
        reveal.classList.contains("meanclose"));
      if (drawerOpen !== isOpen) {
        $("html, body").toggleClass("mobile-menu-open", isOpen);
        if (isOpen) {
          reveal.focus();
        } else if (!navigatingFromDrawer) {
          var focusTarget = reveal || drawerReveal;
          if (focusTarget && focusTarget.isConnected && $(focusTarget).is(":visible")) {
            focusTarget.focus();
          }
        }
      }
      // Also clear stale locks when a rebuild removes the reveal control.
      if (!isOpen) $("html, body").removeClass("mobile-menu-open");
      drawerOpen = isOpen;
      drawerReveal = reveal;
      drawerNav = nav;
      if (!isOpen) navigatingFromDrawer = false;
    }

    // MeanMenu rebuilds on resize; observe its controls rather than retaining old nodes.
    new MutationObserver(syncMobileDrawer).observe(document.body, {
      subtree: true, childList: true, attributes: true, attributeFilter: ["class"]
    });
    window.addEventListener("resize", syncMobileDrawer);
    syncMobileDrawer();

    $(document).on("keydown", function (event) {
      if (!drawerOpen || !drawerReveal || !drawerNav) return;
      if (event.key === "Escape") {
        event.preventDefault();
        $(drawerReveal).trigger("click");
        syncMobileDrawer();
        return;
      }
      if (event.key !== "Tab") return;
      var focusable = $(drawerNav).find('a[href], button, input, select, textarea, [tabindex]')
        .filter(":visible").filter(function () {
          return !this.disabled && this.tabIndex >= 0;
        }).get();
      focusable.unshift(drawerReveal);
      var current = focusable.indexOf(document.activeElement);
      if (current < 0 || (!event.shiftKey && current === focusable.length - 1) ||
          (event.shiftKey && current === 0)) {
        event.preventDefault();
        focusable[event.shiftKey ? focusable.length - 1 : 0].focus();
      }
    });

    $(document).on("click", ".mean-nav a:not(.mean-expand)", function () {
      navigatingFromDrawer = true;
      if (drawerReveal && drawerReveal.classList.contains("meanclose")) {
        $(drawerReveal).trigger("click");
      }
      syncMobileDrawer();
    });

    // 8. Mobile Liquid Glass Scroll Enhancement
    // Adds .is-scrolled to .mean-bar when user scrolls past 10px on mobile,
    // triggering deeper glass blur, shadow and a subtle tint on the pill.
    (function () {
      var meanBar = null;
      var rafPending = false;

      function updateScrollGlass() {
        rafPending = false;
        if (!meanBar || !meanBar.isConnected) {
          meanBar = document.querySelector(".mean-container .mean-bar");
        }
        if (!meanBar) return;
        var scrollY = window.pageYOffset || document.documentElement.scrollTop;
        if (scrollY > 10) {
          meanBar.classList.add("is-scrolled");
        } else {
          meanBar.classList.remove("is-scrolled");
        }
      }

      function onScroll() {
        if (!rafPending) {
          rafPending = true;
          window.requestAnimationFrame(updateScrollGlass);
        }
      }

      // Only activate on mobile widths
      function attachScrollGlass() {
        if (window.innerWidth <= 991) {
          window.addEventListener("scroll", onScroll, { passive: true });
          updateScrollGlass(); // run once on load
        }
      }

      new MutationObserver(function () {
        if (window.innerWidth <= 991) onScroll();
      }).observe(document.body, { childList: true, subtree: true });

      // Re-evaluate on resize
      window.addEventListener("resize", function () {
        if (window.innerWidth > 991) {
          window.removeEventListener("scroll", onScroll);
          if (meanBar) meanBar.classList.remove("is-scrolled");
        } else {
          window.addEventListener("scroll", onScroll, { passive: true });
          updateScrollGlass();
        }
      });

      if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", attachScrollGlass);
      } else {
        attachScrollGlass();
      }
    })();

    // 12. EcoCare Universal Media Lightbox & Video Modal
    (function () {
      var modalBackdrop = $(
        '<div id="ecocare-media-modal" class="ecocare-media-modal-backdrop" role="dialog" aria-modal="true" aria-hidden="true">' +
        '  <div class="ecocare-media-modal-container">' +
        '    <div class="ecocare-media-modal-header">' +
        '      <h4 class="ecocare-media-modal-title"><i class="fas fa-play-circle text-primary"></i> <span>Media Preview</span></h4>' +
        '      <button type="button" class="ecocare-media-modal-close" aria-label="Close modal">&times;</button>' +
        '    </div>' +
        '    <div class="ecocare-media-modal-body">' +
        '      <video id="ecocare-modal-video" controls playsinline preload="auto" style="display:none;"></video>' +
        '      <img id="ecocare-modal-img" src="" alt="Full view" style="display:none;">' +
        '    </div>' +
        '    <div class="ecocare-media-modal-footer">' +
        '      <div id="ecocare-modal-caption">EcoCare Ghana Field Operations</div>' +
        '    </div>' +
        '  </div>' +
        '</div>'
      ).appendTo("body");

      var modalVideo = modalBackdrop.find("#ecocare-modal-video");
      var modalImg = modalBackdrop.find("#ecocare-modal-img");
      var modalTitle = modalBackdrop.find(".ecocare-media-modal-title span");
      var modalTitleIcon = modalBackdrop.find(".ecocare-media-modal-title i");
      var modalCaption = modalBackdrop.find("#ecocare-modal-caption");

      function openMediaModal(type, src, title, caption) {
        modalTitle.text(title || "EcoCare Field Showcase");
        modalCaption.text(caption || "Authentic field operations across Greater Accra.");

        if (type === "video") {
          modalTitleIcon.attr("class", "fas fa-play-circle text-danger");
          modalImg.hide().attr("src", "");
          modalVideo.show().attr("src", src);
          var videoEl = modalVideo[0];
          videoEl.currentTime = 0;
          var playPromise = videoEl.play();
          if (playPromise !== undefined) {
            playPromise.catch(function () {});
          }
        } else {
          modalTitleIcon.attr("class", "fas fa-image text-primary");
          modalVideo.hide().attr("src", "");
          var videoEl = modalVideo[0];
          if (videoEl) videoEl.pause();
          modalImg.show().attr("src", src).attr("alt", title || "EcoCare Project");
        }

        modalBackdrop.addClass("is-active").attr("aria-hidden", "false");
        $("body").css("overflow", "hidden");
      }

      function closeMediaModal() {
        modalBackdrop.removeClass("is-active").attr("aria-hidden", "true");
        $("body").css("overflow", "");
        var videoEl = modalVideo[0];
        if (videoEl) {
          videoEl.pause();
          modalVideo.attr("src", "");
        }
        modalImg.attr("src", "");
      }

      $(document).on("click", ".ecocare-open-media", function (e) {
        e.preventDefault();
        var btn = $(this);
        var type = btn.data("media-type") || "image";
        var src = btn.data("media-src") || btn.attr("href");
        var title = btn.data("media-title") || btn.attr("title");
        var caption = btn.data("media-caption") || "";
        openMediaModal(type, src, title, caption);
      });

      modalBackdrop.on("click", function (e) {
        if ($(e.target).closest(".ecocare-media-modal-container").length === 0 || $(e.target).hasClass("ecocare-media-modal-close")) {
          closeMediaModal();
        }
      });

      $(document).on("keydown", function (e) {
        if (e.key === "Escape" && modalBackdrop.hasClass("is-active")) {
          closeMediaModal();
        }
      });

      // Video switcher on single-project1.html
      $(document).on("click", ".project-video-thumb-btn", function () {
        var btn = $(this);
        var src = btn.data("video-src");
        var poster = btn.data("video-poster");
        var title = btn.data("video-title");
        var player = $("#case-study-featured-video");
        if (player.length && src) {
          $(".project-video-thumb-btn").removeClass("active");
          btn.addClass("active");
          player.attr("poster", poster || "");
          player.attr("src", src);
          if (title) $("#case-study-video-title").text(title);
          player[0].currentTime = 0;
          player[0].play().catch(function () {});
        }
      });
    })();

  });
})(jQuery);
