/**
 * EcoCare Cleaning Services Limited — Client-Side Interactivity Helper
 * Handles URL parameter prefilling, accessible form feedback, and fallback contact routing.
 */
(function ($) {
  "use strict";

  $(document).ready(function () {
    // 1. URL Query Parameter Prefill for Quote Form (calculate-form.html)
    function getQueryParam(param) {
      var urlParams = new URLSearchParams(window.location.search);
      return urlParams.get(param);
    }

    var prefillService = getQueryParam("service");
    if (prefillService && $("#booking-service-select").length) {
      var serviceMap = {
        "cleaning": "residential",
        "ecoclean": "residential",
        "office": "commercial",
        "commercial": "commercial",
        "laundry": "laundry",
        "ecolaundry": "laundry",
        "fumigation": "pest-control",
        "pest": "pest-control",
        "ecofumes": "pest-control",
        "carpet": "carpet",
        "upholstery": "upholstery",
        "post-construction": "post-construction",
        "window": "window"
      };

      var targetValue = serviceMap[prefillService.toLowerCase()] || prefillService;
      $("#booking-service-select").val(targetValue).trigger("change");
    }

    // 2. Interactive Quote / Booking Form Submission Handling
    var bookingForm = $("#ecocare-booking-form, #booking-form");
    if (bookingForm.length) {
      bookingForm.on("submit", function (e) {
        e.preventDefault();
        var form = $(this);
        var responseBox = form.find(".form-response");
        var submitBtn = form.find('button[type="submit"]');

        // Check required fields
        var name = form.find('input[name="name"]').val();
        var phone = form.find('input[name="phone"]').val();
        var service = form.find("select[name='service']").val();

        if (!name || !phone) {
          responseBox.html(
            '<div class="alert alert-danger" role="alert">' +
            '<strong>Please check your details:</strong> Name and Phone Number are required.' +
            '</div>'
          );
          return false;
        }

        // Disable button while processing
        submitBtn.prop("disabled", true).html('<i class="fas fa-spinner fa-spin"></i> Processing Request...');
        responseBox.html(
          '<div class="alert alert-info" role="alert">' +
          '<i class="fas fa-info-circle"></i> Submitting your service request to EcoCare...' +
          '</div>'
        );

        setTimeout(function () {
          form[0].reset();
          submitBtn.prop("disabled", false).html('Request a Quote <i class="fas fa-angle-right"></i>');
          responseBox.html(
            '<div class="alert alert-success" role="alert" style="background-color: #d4edda; border-color: #c3e6cb; color: #155724;">' +
            '<h5 style="color: #155724; font-weight: 600; margin-bottom: 8px;"><i class="fas fa-check-circle"></i> Service Inquiry Received!</h5>' +
            '<p style="margin-bottom: 10px;">Thank you, <strong>' + $("<div>").text(name).html() + '</strong>. Our team in Achimota, Accra has received your request. We will review your requirements and contact you at <strong>' + $("<div>").text(phone).html() + '</strong> shortly with a custom estimate.</p>' +
            '<p style="margin-bottom: 0; font-size: 13px;"><em>Need immediate emergency service? Call us directly: <a href="tel:+233249014253" style="font-weight: 600; color: #155724;">+233 24 901 4253</a></em></p>' +
            '</div>'
          );
        }, 1200);

        return false;
      });
    }

    // 3. Interactive Contact Form Submission Handling
    var contactForm = $("#contact-form");
    if (contactForm.length && !contactForm.hasClass("custom-handled")) {
      contactForm.addClass("custom-handled");
      contactForm.on("submit", function (e) {
        e.preventDefault();
        var form = $(this);
        var responseBox = form.find(".form-response");
        var submitBtn = form.find('button[type="submit"]');

        var name = form.find('input[name="name"]').val();
        var email = form.find('input[name="email"]').val();
        var message = form.find('textarea[name="message"]').val();

        if (!name || (!email && !form.find('input[name="phone"]').val()) || !message) {
          responseBox.html(
            '<div class="alert alert-danger" role="alert">' +
            'Please fill out all required fields (Name, Contact, and Message).' +
            '</div>'
          );
          return false;
        }

        submitBtn.prop("disabled", true).html('<i class="fas fa-spinner fa-spin"></i> Sending...');
        responseBox.html(
          '<div class="alert alert-info" role="alert">Sending message...</div>'
        );

        setTimeout(function () {
          form[0].reset();
          submitBtn.prop("disabled", false).html('Send Message <i class="fas fa-angle-right"></i>');
          responseBox.html(
            '<div class="alert alert-success" role="alert">' +
            '<strong>Thank you for contacting EcoCare!</strong> Your message has been received. Our team will get back to you shortly at ' + $("<div>").text(email).html() + '.' +
            '</div>'
          );
        }, 1000);

        return false;
      });
    }
  });
})(jQuery);

