/**
 * EcoCare Cleaning Services Limited — Standalone Coming Soon Countdown Controller
 * 
 * Target Launch Deadline: Fixed UTC timestamp (Africa/Accra GMT)
 * Default: 2026-11-16T14:00:00Z (7 days from 2026-11-09T14:00:00Z)
 * 
 * Rules:
 * - Shared fixed timestamp for all visitors. Does NOT reset on page reload.
 * - Displays Days, Hours, Minutes, Seconds with zero-padding.
 * - Stops at zero. Surfaces a neutral launch verification banner.
 * - Strictly NEVER auto-redirects or exposes unfinished website pages.
 * - Supports test clock injection via ?test_clock= query param or window.__ECOCARE_TEST_NOW__.
 */
(function () {
  "use strict";

  // Production Target Deadline: Monday, November 16, 2026 at 14:00:00 GMT (Africa/Accra)
  var DEFAULT_TARGET_UTC = "2026-11-16T14:00:00Z";

  function pad(num) {
    return num < 10 ? "0" + num : String(num);
  }

  function getTestTimeOffset() {
    // 1. Check window override
    if (typeof window.__ECOCARE_TEST_NOW__ === "number") {
      return window.__ECOCARE_TEST_NOW__;
    }
    // 2. Check URL query parameters (e.g. ?test_clock=7d, ?test_clock=5s, ?test_clock=0s, ?test_clock=past)
    try {
      var params = new URLSearchParams(window.location.search);
      var testClock = params.get("test_clock");
      if (testClock) {
        var targetMs = Date.parse(DEFAULT_TARGET_UTC);
        if (testClock === "7d") return targetMs - (7 * 86400 * 1000) + 1000;
        if (testClock === "1d") return targetMs - (86400 * 1000);
        if (testClock === "5s") return targetMs - 5000;
        if (testClock === "0s" || testClock === "zero" || testClock === "past") return targetMs + 1000;
        var numericSec = parseInt(testClock, 10);
        if (!isNaN(numericSec)) return targetMs - (numericSec * 1000);
      }
    } catch (e) {
      // Ignore URLSearchParams error in legacy contexts
    }
    return Date.now();
  }

  function initCountdown() {
    var container = document.getElementById("launch-countdown");
    if (!container) return;

    var targetIso = container.getAttribute("data-deadline") || DEFAULT_TARGET_UTC;
    var targetMs = Date.parse(targetIso);

    if (isNaN(targetMs)) {
      targetMs = Date.parse(DEFAULT_TARGET_UTC);
    }

    var statusEl = document.getElementById("countdown-status");
    var timerId = null;

    function render() {
      var nowMs = getTestTimeOffset();
      var remainingSec = Math.max(0, Math.floor((targetMs - nowMs) / 1000));

      if (remainingSec <= 0) {
        // Zero reached: display 00s, stop timer, surface neutral launch announcement
        container.innerHTML =
          '<div class="countdown-section"><div><div class="countdown-number">00</div><div class="countdown-unit">Days</div></div></div>' +
          '<div class="countdown-section"><div><div class="countdown-number">00</div><div class="countdown-unit">Hours</div></div></div>' +
          '<div class="countdown-section"><div><div class="countdown-number">00</div><div class="countdown-unit">Minutes</div></div></div>' +
          '<div class="countdown-section"><div><div class="countdown-number">00</div><div class="countdown-unit">Seconds</div></div></div>';

        if (statusEl) {
          statusEl.innerHTML =
            '<i class="fas fa-check-circle" style="color:#6bb92d; margin-right:8px;"></i>' +
            '<span>The enhanced EcoCare platform is undergoing final launch verification. We will be live momentarily!</span>';
          statusEl.style.display = "block";
        }

        container.setAttribute("aria-label", "Countdown completed: 0 Days, 0 Hours, 0 Minutes, 0 Seconds");

        if (timerId) {
          clearInterval(timerId);
          timerId = null;
        }
        return;
      }

      var days = Math.floor(remainingSec / 86400);
      var hours = Math.floor((remainingSec % 86400) / 3600);
      var minutes = Math.floor((remainingSec % 3600) / 60);
      var seconds = remainingSec % 60;

      var daysUnit = days === 1 ? "Day" : "Days";
      var hoursUnit = hours === 1 ? "Hour" : "Hours";
      var minUnit = "Minutes";
      var secUnit = "Seconds";

      container.innerHTML =
        '<div class="countdown-section"><div><div class="countdown-number">' + pad(days) + '</div><div class="countdown-unit">' + daysUnit + '</div></div></div>' +
        '<div class="countdown-section"><div><div class="countdown-number">' + pad(hours) + '</div><div class="countdown-unit">' + hoursUnit + '</div></div></div>' +
        '<div class="countdown-section"><div><div class="countdown-number">' + pad(minutes) + '</div><div class="countdown-unit">' + minUnit + '</div></div></div>' +
        '<div class="countdown-section"><div><div class="countdown-number">' + pad(seconds) + '</div><div class="countdown-unit">' + secUnit + '</div></div></div>';

      container.setAttribute(
        "aria-label",
        "Launch Countdown: " + days + " " + daysUnit + ", " + hours + " " + hoursUnit + ", " + minutes + " Minutes, " + seconds + " Seconds"
      );
    }

    // Initial render
    render();

    // Schedule 1-second interval
    timerId = setInterval(render, 1000);
  }

  function initPreloader() {
    var preloader = document.getElementById("preloader");
    if (!preloader) return;

    var preloaderStart = Date.now();
    var dissolveStartMs = 1550; // Dissolve begins at 1.55s
    var isDissolving = false;

    function triggerDissolve() {
      if (isDissolving) return;
      isDissolving = true;
      var elapsed = Date.now() - preloaderStart;
      var wait = Math.max(0, dissolveStartMs - elapsed);

      setTimeout(function () {
        preloader.classList.add("preloader-dissolving");
        setTimeout(function () {
          if (preloader.parentNode) {
            preloader.parentNode.removeChild(preloader);
          }
        }, 450); // 1550ms + 450ms = 2000ms total
      }, wait);
    }

    if (document.readyState === "complete") {
      triggerDissolve();
    } else {
      window.addEventListener("load", triggerDissolve);
      // Hard timeout fallback
      setTimeout(triggerDissolve, 2500);
    }
  }

  // Safe DOM ready bootstrap
  function bootstrap() {
    initPreloader();
    initCountdown();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", bootstrap);
  } else {
    bootstrap();
  }
})();

