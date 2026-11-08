#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Native Clenix Template Restoration Engine
Restores the 100% original Clenix ThemeForest layout, components, markup, and animations
from commit c4ebf6a, surgically slotting authentic EcoCare information into the native slots.
"""

import os
import subprocess
import re

# Verified EcoCare Constants
COMPANY_NAME = "EcoCare Cleaning Services Limited"
PHONE_PRIMARY = "+233 24 901 4253"
PHONE_SECONDARY = "+233 24 380 7100"
PHONE_TEL_PRIMARY = "+233249014253"
PHONE_TEL_SECONDARY = "+233243807100"
EMAIL_PRIMARY = "ecocaregh1on1@gmail.com"
OFFICE_ADDRESS = "Achimota Mile 7, Accra, Ghana"
HOURS_TEXT = "Mon - Sat: 07:00am - 06:00pm"
MAP_IFRAME_SRC = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3970.5870075801395!2d-0.24410990324261828!3d5.627819178441937!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xfdf995df95740cb%3A0xbbcb29ede8158fa1!2sEcoCare%20Laundry!5e0!3m2!1sen!2sgh!4v1735185870106!5m2!1sen!2sgh"

FB_URL = "https://www.facebook.com/profile.php?id=100006412849415"
TIKTOK_URL = "https://www.tiktok.com/@ecocarecompanylimited"
YOUTUBE_URL = "https://www.youtube.com/channel/UCdJfEIsRCxYaOnnmhbs2kcA"

def get_orig(path):
    """Retrieve untouched original template file content from initial commit c4ebf6a."""
    res = subprocess.run(["git", "show", f"c4ebf6a:{path}"], capture_output=True, text=True, check=True)
    return res.stdout

def clean_common_artifacts(html):
    """Strip HTTrack comments, Cloudflare analytics beacons, and inject ecocare helper CSS/JS."""
    # 1. Remove HTTrack comments
    html = re.sub(r'<!-- Mirrored from [^\n]* -->\n?', '', html)
    # 2. Remove Cloudflare beacon
    html = re.sub(r'<script[^>]*static\.cloudflareinsights\.com/beacon\.min\.js[^>]*></script>', '', html)
    # 3. Ensure ecocare.css is linked after style.css
    if 'css/ecocare.css' not in html:
        html = html.replace(
            '<link rel="stylesheet" href="style.css">',
            '<link rel="stylesheet" href="style.css">\n    <!-- EcoCare Brand Constraints -->\n    <link rel="stylesheet" href="css/ecocare.css">'
        )
    # 4. Ensure ecocare.js is included after main.js
    if 'js/ecocare.js' not in html:
        html = html.replace(
            '<script src="js/main.js"></script>',
            '<script src="js/main.js"></script>\n    <!-- EcoCare Interactivity Helper -->\n    <script src="js/ecocare.js"></script>'
        )
    return html

def get_native_header(active_nav="home"):
    def is_act(nav_id):
        return ' class="active"' if active_nav == nav_id else ""

    return f"""        <!-- Header Area Start Here -->
        <header class="header">
            <div id="header-topbar" class="bg-Primary">
                <div class="container">
                    <div class="row d-flex align-items-center">
                        <div class="col-lg-6">
                            <div class="header-topbar-layout1">
                                <ul class="header-top-left">
                                    <li class="social-icon">
                                        <a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a>
                                        <a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a>
                                        <a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a>
                                    </li>
                                    <li class="opening-hour"><i class="far fa-clock"></i>{HOURS_TEXT}</li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-lg-6 d-flex justify-content-end">
                            <div class="header-topbar-layout1">
                                <div class="header-top-right">
                                    <a href="tel:{PHONE_TEL_PRIMARY}" class="text-white mr-3 font-weight-bold" style="font-size: 14px;"><i class="fas fa-phone-alt mr-1"></i> {PHONE_PRIMARY}</a>
                                    <a href="calculate-form.html" class="header-top-btn"><i class="fas fa-calculator mr-1"></i>Get A Quote</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div id="rt-sticky-placeholder"></div>
            <div id="header-menu" class="header-menu menu-layout1">
                <div class="container">
                    <div class="row d-flex align-items-center">
                        <div class="col-xl-2 col-lg-2">
                            <div class="logo-area">
                                <a href="index.html" class="temp-logo">
                                    <img src="img/logo-dark.png" alt="{COMPANY_NAME}" class="img-fluid">
                                </a>
                            </div>
                        </div>
                        <div class="col-lg-7 d-flex justify-content-end position-static">
                            <nav id="dropdown" class="template-main-menu">
                                <ul>
                                   <li{is_act("home")}>
                                        <a href="index.html">Home</a>
                                    </li>
                                    <li{is_act("about")}>
                                        <a href="about1.html">About</a>
                                    </li>
                                    <li{is_act("services")}>
                                        <a href="service1.html">Services</a>
                                        <ul class="dropdown-menu-col-1">
                                            <li><a href="service1.html">All 12 Service Listings</a></li>
                                            <li><a href="single-service1.html">EcoClean (Cleaning)</a></li>
                                            <li><a href="single-service2.html">Eco-Laundry (Garments)</a></li>
                                            <li><a href="pest-control.html">EcoFumes (Pest Control)</a></li>
                                            <li><a href="carpet-cleaning.html">Carpet Deep Cleaning</a></li>
                                            <li><a href="upholstery-cleaning.html">Upholstery &amp; Furniture</a></li>
                                        </ul>
                                    </li>
                                    <li{is_act("packages")}>
                                        <a href="pricing-table.html">Packages</a>
                                    </li>
                                    <li{is_act("projects")}>
                                        <a href="project1.html">Projects</a>
                                    </li>
                                    <li{is_act("faq")}>
                                        <a href="faq.html">FAQ</a>
                                    </li>
                                    <li{is_act("contact")}>
                                        <a href="contact.html">Contact</a>
                                    </li>
                                </ul>
                            </nav>
                        </div>
                        <div class="col-lg-3 d-flex justify-content-end">
                            <div class="header-action-layout1">
                                <ul>
                                    <li class="header-action-number">
                                        <div class="item-icon">
                                            <i class="flaticon-phone-call"></i>
                                        </div>
                                        <div class="item-content">
                                            <div class="item-title">Quick Contact :</div>
                                            <div class="item-number"><a href="tel:{PHONE_TEL_PRIMARY}" style="color: inherit;">{PHONE_PRIMARY}</a></div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <!-- Header Area End Here -->"""

def get_native_footer():
    return f"""        <!-- Footer Area Start Here -->
        <footer class="footer-wrap-layout1 section-shape1">
            <div class="container">
                <div class="footer-top-box">
                    <div class="row">
                        <div class="col-lg-3 col-sm-6 col-12">
                            <div class="footer-box-layout1">
                                <div class="footer-logo mb-3">
                                    <a href="index.html"><img src="img/large-logo.png" alt="{COMPANY_NAME}" class="img-fluid"></a>
                                </div>
                                <p style="color: #dcdcdc; font-size: 14px; line-height: 22px;">
                                    <strong>“Protect the Environment, Live Better, Prolong Life.”</strong><br>
                                    EcoCare Cleaning Services Limited is Ghana's trusted partner for residential cleaning, corporate maintenance, EcoFumes fumigation, Eco-Laundry, carpet deep cleaning, and upholstery care.
                                </p>
                                <div class="footer-social mt-3">
                                    <ul class="social-icon">
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-sm-6 col-12">
                            <div class="footer-box-layout1">
                                <div class="footer-title">
                                    <h4>OUR SERVICES</h4>
                                </div>
                                <div class="footer-menu-box">
                                    <ul class="footer-menu-list">
                                        <li><a href="single-service1.html"><i class="fas fa-angle-right mr-2 text-warning"></i>EcoClean (Cleaning)</a></li>
                                        <li><a href="single-service2.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Eco-Laundry (Garments)</a></li>
                                        <li><a href="pest-control.html"><i class="fas fa-angle-right mr-2 text-warning"></i>EcoFumes (Fumigation)</a></li>
                                        <li><a href="carpet-cleaning.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Carpet Deep Cleaning</a></li>
                                        <li><a href="upholstery-cleaning.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Upholstery &amp; Furniture</a></li>
                                        <li><a href="service1.html"><i class="fas fa-angle-right mr-2 text-warning"></i>All 12 Service Listings</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-sm-6 col-12">
                            <div class="footer-box-layout1">
                                <div class="footer-title">
                                    <h4>QUICK LINKS</h4>
                                </div>
                                <div class="footer-menu-box">
                                    <ul class="footer-menu-list">
                                        <li><a href="index.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Home</a></li>
                                        <li><a href="about1.html"><i class="fas fa-angle-right mr-2 text-warning"></i>About Us</a></li>
                                        <li><a href="pricing-table.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Packages &amp; Estimates</a></li>
                                        <li><a href="calculate-form.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Request a Quote</a></li>
                                        <li><a href="project1.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Projects Gallery</a></li>
                                        <li><a href="faq.html"><i class="fas fa-angle-right mr-2 text-warning"></i>FAQ</a></li>
                                        <li><a href="contact.html"><i class="fas fa-angle-right mr-2 text-warning"></i>Contact Us</a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-sm-6 col-12">
                            <div class="footer-box-layout1">
                                <div class="footer-title">
                                    <h4>HEAD OFFICE</h4>
                                </div>
                                <div class="footer-contact-info" style="color: #dcdcdc; font-size: 14px; line-height: 24px;">
                                    <p style="margin-bottom: 10px;">
                                        <i class="fas fa-map-marker-alt text-warning mr-2"></i> {OFFICE_ADDRESS}
                                    </p>
                                    <p style="margin-bottom: 10px;">
                                        <i class="fas fa-phone-alt text-warning mr-2"></i> <a href="tel:{PHONE_TEL_PRIMARY}" style="color: #ffffff;">{PHONE_PRIMARY}</a><br>
                                        <i class="fas fa-phone-alt text-warning mr-2"></i> <a href="tel:{PHONE_TEL_SECONDARY}" style="color: #ffffff;">{PHONE_SECONDARY}</a>
                                    </p>
                                    <p style="margin-bottom: 10px;">
                                        <i class="fas fa-envelope text-warning mr-2"></i> <a href="mailto:{EMAIL_PRIMARY}" style="color: #ffffff;">{EMAIL_PRIMARY}</a>
                                    </p>
                                    <p style="margin-bottom: 0;">
                                        <i class="far fa-clock text-warning mr-2"></i> {HOURS_TEXT}
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="footer-bottom-box">
                    <div class="row">
                        <div class="col-md-6 col-12">
                            <div class="copyright text-left">
                                &copy; 2026 {COMPANY_NAME}. All Rights Reserved.
                            </div>
                        </div>
                        <div class="col-md-6 col-12 text-right">
                            <div class="footer-bottom-menu">
                                <a href="privacy-policy.html" class="mr-3 text-white-50">Privacy Policy (Draft)</a>
                                <a href="terms-condition.html" class="text-white-50">Terms &amp; Conditions (Draft)</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Footer Area End Here -->"""

def replace_header_and_footer(html, active_nav="home"):
    """Surgically replace the demo header and footer with native Clenix EcoCare header/footer."""
    # Replace Header Area
    html = re.sub(
        r'<!-- Header Area Start Here -->.*?<!-- Header Area End Here -->',
        get_native_header(active_nav),
        html,
        flags=re.DOTALL
    )
    # Replace Footer Area
    html = re.sub(
        r'<!-- Footer Area Start Here -->.*?<!-- Footer Area End Here -->',
        get_native_footer(),
        html,
        flags=re.DOTALL
    )
    return html

def replace_page_title(html, title, description):
    html = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', html)
    html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{description}">', html)
    return html

print("Restoration engine helper loaded.")

# ==============================================================================
# 1. CANONICAL HOMEPAGE: index.html
# ==============================================================================
def build_index():
    html = get_orig("index.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="EcoCare Cleaning Services Limited | Professional Cleaning, Fumigation & Laundry in Accra, Ghana",
        description="EcoCare Cleaning Services Limited provides professional residential, commercial & industrial cleaning, EcoFumes pest control, Eco-Laundry, carpet deep cleaning and upholstery care across Accra, Ghana. Established 2014."
    )
    html = replace_header_and_footer(html, active_nav="home")

    # 1. Nivo Slider Captions
    # Caption 1
    html = html.replace(
        '<div class="slider-sub-text">The Best Cleaning Service Ever!</div>\n                                <h1 class="slider-big-text">Certified Company</h1>\n                                <div class="slider-paragraph">Our best-in-class WordPress solution, \n                                    with additional optimization to make running a WooCommerce online \n                                    store easy. Our prices are clear and straight forward so you can.</div>\n                                <div class="slider-btn-area">\n                                    <a href="#" class="item-btn-fill">Take Our Service\n                                        <i class="fas fa-angle-right"></i>\n                                    </a>\n                                </div>',
        f'<div class="slider-sub-text">EcoCare Cleaning Services Limited</div>\n                                <h1 class="slider-big-text">Protect the Environment, Live Better, Prolong Life</h1>\n                                <div class="slider-paragraph">Accra\'s premier cleaning and hygiene company. Professional domestic housekeeping, corporate janitorial, EcoFumes fumigation, and Eco-Laundry across Greater Accra.</div>\n                                <div class="slider-btn-area">\n                                    <a href="service1.html" class="item-btn-fill">Our Services <i class="fas fa-angle-right"></i></a>\n                                    <a href="calculate-form.html" class="item-btn-fill" style="margin-left: 10px;">Request a Quote <i class="fas fa-calculator"></i></a>\n                                </div>'
    )
    # Caption 2 & 3
    caption_replace_2 = f'<div class="slider-sub-text">Accra, Ghana &bull; Established 2014</div>\n                                <h1 class="slider-big-text">You Got Dirt? We Got Clean.</h1>\n                                <div class="slider-paragraph">From routine office janitorial and high-traffic carpet steam extraction to specialized EcoFumes pest management. Quality, safety, and customer satisfaction guaranteed.</div>\n                                <div class="slider-btn-area">\n                                    <a href="service1.html" class="item-btn-fill">Our Services <i class="fas fa-angle-right"></i></a>\n                                    <a href="calculate-form.html" class="item-btn-fill" style="margin-left: 10px;">Request a Quote <i class="fas fa-calculator"></i></a>\n                                </div>'
    caption_replace_3 = f'<div class="slider-sub-text">Specialized Care &amp; Garment Services</div>\n                                <h1 class="slider-big-text">Eco-Laundry &amp; Fabric Restoration</h1>\n                                <div class="slider-paragraph">Expert wash, fold, steam ironing, and delicate dry cleaning care with scheduled doorstep pickup and delivery across Greater Accra.</div>\n                                <div class="slider-btn-area">\n                                    <a href="single-service2.html" class="item-btn-fill">Eco-Laundry Care <i class="fas fa-angle-right"></i></a>\n                                    <a href="calculate-form.html" class="item-btn-fill" style="margin-left: 10px;">Book Pickup <i class="fas fa-calculator"></i></a>\n                                </div>'

    html = re.sub(
        r'<div id="slider-direction-2".*?<div id="slider-direction-3"',
        f'<div id="slider-direction-2" class="t-cn slider-direction">\n                    <div class="slider-content s-tb slide-2">\n                        <div class="text-left title-container s-tb-c">\n                            <div class="container">\n                                {caption_replace_2}\n                            </div>\n                        </div>\n                    </div>\n                </div>\n                <div id="slider-direction-3"',
        html,
        flags=re.DOTALL
    )

    html = re.sub(
        r'<div id="slider-direction-3".*?</div>\s*</div>\s*<!-- Slider Area End Here -->',
        f'<div id="slider-direction-3" class="t-cn slider-direction">\n                    <div class="slider-content s-tb slide-3">\n                        <div class="text-left title-container s-tb-c">\n                            <div class="container">\n                                {caption_replace_3}\n                            </div>\n                        </div>\n                    </div>\n                </div>\n            </div>  \n        </div>\n        <!-- Slider Area End Here -->',
        html,
        flags=re.DOTALL
    )

    # 2. About Us Area (layout 3 & 4)
    about_replacement = f"""        <!-- About Us Area Start Here -->
        <section class="section-bubble section-padding-md-2">
            <div class="container">
                <div class="row gutters-50 d-flex align-items-center">
                    <div class="col-xl-7">
                        <div class="about-box-layout3">
                            <div class="item-icon shape1">
                                <img src="img/figure/icon-shape1.png" alt="shape">
                            </div>
                            <div class="item-icon shape2">
                                <img src="img/figure/icon-shape2.png" alt="shape">
                            </div>
                            <div class="item-icon shape3">
                                <img src="img/figure/icon-shape3.png" alt="shape">
                            </div>
                            <div class="item-icon shape4">
                                <img src="img/figure/icon-shape4.png" alt="shape">
                            </div>
                            <div class="item-img">
                                <img src="img/figure/figure5.png" alt="EcoCare Professional Cleaning">
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-5">
                        <div class="about-box-layout4">
                            <h2 class="item-title">Making Your Space <span>Healthy &amp; Spotless</span></h2>
                            <p>EcoCare Cleaning Services Limited is Ghana's trusted environmental and facility care provider. Established on September 19, 2014 under the Ghanaian Companies Code, we deliver superior residential and corporate cleaning programs that protect health, enhance comfort, and prolong property life.</p>
                            <div class="service-list">
                                <ul>
                                    <li>Uniformed, vetted and supervised cleaning crews</li>
                                    <li>Eco-conscious, non-toxic sanitizing products</li>
                                    <li>Custom regular, deep scrub, or post-construction visits</li>
                                    <li>Transparent scoping and responsive customer desk in Achimota</li>
                                </ul>
                            </div>
                            <div class="action-area">
                                <a href="calculate-form.html" class="btn-fill-sm bg-accent text-primarytext btn-slide-hover">Book a Service<i class="fas fa-angle-right"></i></a>
                                <div class="phone-number"><i class="flaticon-phone-call"></i><a href="tel:{PHONE_TEL_PRIMARY}" style="color: inherit;">{PHONE_PRIMARY}</a></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- About Us Area End Here -->"""

    html = re.sub(
        r'<!-- About Us Area Start Here -->.*?<!-- About Us Area End Here -->',
        about_replacement,
        html,
        count=1,
        flags=re.DOTALL
    )

    # 3. Services Area (service-box-layout1)
    services_replacement = f"""        <!-- Service Area Start Here -->
        <section class="section-padding-lg bg-common bg-aash" data-bg-image="img/figure/bg-shape1.png">
            <div class="container">
                <div class="heading-layout1">
                    <h2>Cleaning &amp; Environmental Services</h2>
                    <p>Comprehensive hygiene, pest management, and textile restoration solutions for homes and businesses in Accra.</p>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service.jpg" alt="Residential House Cleaning">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="fas fa-home"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-service1.html#residential">Residential House Cleaning</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Bedrooms &amp; Living Areas</li>
                                        <li>Bathrooms Descaling</li>
                                        <li>Kitchen Degreasing</li>
                                        <li>Windows &amp; Glass</li>
                                        <li>Floor Scrubbing</li>
                                        <li>Move-In / Move-Out Clean</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service1.jpg" alt="Commercial Janitorial">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="far fa-building"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-service1.html#office">Commercial &amp; Janitorial</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Corporate Office Suites</li>
                                        <li>Retail &amp; Bank Plazas</li>
                                        <li>Restroom Sanitation</li>
                                        <li>Machine Floor Buffing</li>
                                        <li>Waste Segregation</li>
                                        <li>Supervisor Quality Audits</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service2.jpg" alt="Eco-Laundry">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="flaticon-clean-1"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-service2.html">Eco-Laundry &amp; Garments</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Wash, Dry &amp; Fold</li>
                                        <li>Steam Ironing &amp; Finishing</li>
                                        <li>Delicate Silks &amp; Suits</li>
                                        <li>Duvets &amp; Bedding</li>
                                        <li>Curtain Cleaning</li>
                                        <li>Scheduled Greater Accra Pickup</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service3.jpg" alt="EcoFumes Fumigation">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="flaticon-shield"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="pest-control.html">EcoFumes Pest Control</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Termite Colony Barriers</li>
                                        <li>Cockroach Gel Baiting</li>
                                        <li>Rodent Exclusion Proofing</li>
                                        <li>Mosquito Fogging</li>
                                        <li>Bed Bug Elimination</li>
                                        <li>Warehouse IPM Compliance</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service4.jpg" alt="Carpet Cleaning">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="flaticon-mop"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="carpet-cleaning.html">Carpet Deep Cleaning</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Hot-Water Deep Extraction</li>
                                        <li>Heavy Traffic Lane Revival</li>
                                        <li>Spot &amp; Stain Removal</li>
                                        <li>Low-Moisture Encapsulation</li>
                                        <li>Odor Neutralization</li>
                                        <li>Residential &amp; Commercial</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="service-box-layout1">
                            <div class="item-img">
                                <img src="img/service/service5.jpg" alt="Upholstery Cleaning">
                            </div>
                            <div class="item-middle-content">
                                <div class="item-icon">
                                    <div class="home-icon">
                                        <i class="flaticon-clean"></i>
                                    </div>
                                </div>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="upholstery-cleaning.html">Upholstery Care</a></h3>
                                <div class="serivce-list">
                                    <ul>
                                        <li>Fabric Couches &amp; Sectionals</li>
                                        <li>Leather Care &amp; Conditioning</li>
                                        <li>Dining Chair Fabric Revival</li>
                                        <li>Mattress Dust-Mite Removal</li>
                                        <li>Office Workstation Seating</li>
                                        <li>Vehicle Interior Fabrics</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Service Area End Here -->"""

    html = re.sub(
        r'<!-- Service Area Start Here -->.*?<!-- Service Area End Here -->',
        services_replacement,
        html,
        flags=re.DOTALL
    )

    # 4. Call to Action Strip
    cta_replacement = f"""        <!-- Call To Action Area Start Here -->
        <section class="action-wrap-layout1">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <div class="action-box-layout1">
                            <h2 class="item-title">Need Immediate Professional Cleaning in Accra?</h2>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="action-box-layout1">
                            <div class="item-img bottom-bubble">
                                <img src="img/figure/figure4.png" alt="EcoCare Service">
                            </div>
                            <a href="calculate-form.html" class="btn-fill-md hover-textprimary bg-accent text-primarytext">Get an Estimate<i class="fas fa-angle-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Call To Action Area End Here -->"""

    html = re.sub(
        r'<!-- Call To Action Area Start Here -->.*?<!-- Call To Action Area End Here -->',
        cta_replacement,
        html,
        flags=re.DOTALL
    )

    # 5. In-Page Estimate Request Form (about-box-layout2)
    inpage_form_replacement = f"""        <!-- About Us Area Start Here -->
        <section class="section-padding-md-2 section-bubble">
            <div class="container">
                <div class="row">
                    <div class="col-xl-7 col-lg-6 col-12">
                        <div class="about-box-layout1">
                            <h2 class="item-title">Why Choose EcoCare Cleaning Services?</h2>
                            <div class="item-subtitle">Reliable scheduling, meticulous standards, and transparent service across Greater Accra.</div>
                            <p>We believe that clean, hygienic spaces promote personal wellbeing, corporate productivity, and prolonged physical asset life. Every assignment is supervised and conducted using calibrated equipment and eco-friendly solutions.</p>
                            <div class="list-item">
                                <ul>
                                    <li>
                                        <h3>Customer-Focused Scheduling</h3>
                                        <p>Flexible appointment slots tailored to family routines and after-hours corporate facility operations.</p>
                                    </li>
                                    <li>
                                        <h3>Vetted &amp; Uniformed Specialists</h3>
                                        <p>Trained crew operating under strict safety, integrity, and hygiene protocols.</p>
                                    </li>
                                    <li>
                                        <h3>Transparent Scoping</h3>
                                        <p>Clear, itemized estimates in Ghanaian Cedis with zero hidden fees.</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-5 col-lg-6 col-12">
                        <div class="about-box-layout2">
                            <h3 class="item-title">Request An Estimate</h3>
                            <form class="contact-form-box" id="ecocare-booking-form">
                                <div class="row gutters-10">
                                    <div class="col-12 form-group">
                                        <select class="select2" name="service" required>
                                            <option value="residential">EcoClean: Residential Cleaning</option>
                                            <option value="commercial">EcoClean: Commercial Janitorial</option>
                                            <option value="laundry">Eco-Laundry: Garment &amp; Linen Care</option>
                                            <option value="pest-control">EcoFumes: Fumigation &amp; Pest Control</option>
                                            <option value="carpet">Carpet Deep Cleaning</option>
                                            <option value="upholstery">Upholstery &amp; Furniture</option>
                                            <option value="post-construction">Post-Construction Deep Scrub</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <select class="select2" name="property_type">
                                            <option value="residential">Residential Home</option>
                                            <option value="apartment">Apartment / Flat</option>
                                            <option value="commercial">Office / Commercial</option>
                                            <option value="industrial">Warehouse / Industrial</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <select class="select2" name="frequency">
                                            <option value="one-off">One-Off Deep Clean</option>
                                            <option value="weekly">Weekly Routine</option>
                                            <option value="bi-weekly">Bi-Weekly Care</option>
                                            <option value="monthly">Monthly Contract</option>
                                        </select>
                                    </div>
                                    <div class="col-12 form-group">
                                        <input type="text" placeholder="Location in Accra (e.g. Achimota, East Legon)" class="form-control" name="location" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-md-6 col-12 form-group datetime-picker">
                                        <i class="far fa-calendar-alt"></i>
                                        <input type="text" class="form-control rt-date" placeholder="Preferred Date" name="preferred_date" autocomplete="off" />
                                    </div>
                                    <div class="col-md-6 col-12 form-group datetime-picker">
                                        <i class="far fa-clock"></i>
                                        <input type="text" class="form-control rt-time" placeholder="Preferred Time" name="preferred_time" autocomplete="off" />
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <input type="text" placeholder="Full Name *" class="form-control" name="name" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <input type="tel" placeholder="Phone Number *" class="form-control" name="phone" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <input type="email" placeholder="Email Address" class="form-control" name="email">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group mg-b-20">
                                        <textarea placeholder="Specific requirements or notes..." class="textarea form-control" name="notes" rows="2"></textarea>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <button type="submit" class="fw-btn-fill bg-accent text-primarytext">Request a Quote<i class="fas fa-angle-right"></i></button>
                                    </div>
                                </div>
                                <div class="form-response"></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- About Us Area End Here -->"""

    html = re.sub(
        r'<!-- About Us Area Start Here -->\s*<section class="section-padding-md-2 section-bubble">.*?<!-- About Us Area End Here -->',
        inpage_form_replacement,
        html,
        flags=re.DOTALL
    )

    # 6. Pricing Section (pricing-box-layout1 3 boxes)
    pricing_replacement = f"""        <!-- Pricing Table Area Start Here -->
        <section class="section-padding-xl bg-Primary section-shape2">
            <div class="container">
                <div class="heading-layout1 mg-b-60">
                    <h2 class="text-white">Transparent Service Packages</h2>
                    <p class="text-textprimary">Structured service packages tailored to your property size and frequency in Ghanaian Cedis (GHS).</p>
                </div>
                <div class="row">
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-clean"></i>
                            </div>
                            <h3 class="item-title">Essential Residential</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>Bedrooms &amp; Living Area Dusting</li>
                                    <li><i class="fas fa-check"></i>Floor Vacuuming &amp; Surface Mop</li>
                                    <li><i class="fas fa-check"></i>Kitchen Counters &amp; Sink Sanitization</li>
                                    <li><i class="fas fa-check"></i>Bathroom Scrubbing &amp; Disinfection</li>
                                    <li><i class="fas fa-check"></i>Trash Emptying &amp; Liner Replacement</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency" style="font-size: 26px;">Quote on Scope</div>
                                <div class="item-duration">Routine / Weekly</div>
                            </div>
                            <a href="calculate-form.html?service=residential" class="btn-fill-xl bg-accent text-primarytext">Request Quote</a>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1">
                            <div class="popular-text">Popular Care!</div>
                            <div class="item-icon popular-shape">
                                <i class="flaticon-mop"></i>
                            </div>
                            <h3 class="item-title">Intensive Deep Scrub</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>Everything in Essential Residential</li>
                                    <li><i class="fas fa-check"></i>Kitchen Appliance Degreasing (Ovens)</li>
                                    <li><i class="fas fa-check"></i>Heavy Tile Scale &amp; Grout Descaling</li>
                                    <li><i class="fas fa-check"></i>Baseboard, Door &amp; Window Detailing</li>
                                    <li><i class="fas fa-check"></i>Move-In / Move-Out Readiness</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency" style="font-size: 26px;">Quote on Scope</div>
                                <div class="item-duration">One-Off Intensive</div>
                            </div>
                            <a href="calculate-form.html?service=cleaning" class="btn-fill-xl bg-accent text-primarytext">Request Quote</a>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-tower"></i>
                            </div>
                            <h3 class="item-title">Corporate Facility</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>Dedicated On-Site Day Porters</li>
                                    <li><i class="fas fa-check"></i>Daily Workstation Janitorial</li>
                                    <li><i class="fas fa-check"></i>Restroom Sanitization &amp; Hygiene</li>
                                    <li><i class="fas fa-check"></i>Floor Machine Scrubbing &amp; Buffing</li>
                                    <li><i class="fas fa-check"></i>Monthly Supervisor Quality Audits</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency" style="font-size: 26px;">Custom Retainer</div>
                                <div class="item-duration">Monthly Contract</div>
                            </div>
                            <a href="calculate-form.html?service=commercial" class="btn-fill-xl bg-accent text-primarytext">Inquire Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Pricing Table Area End Here -->"""

    html = re.sub(
        r'<!-- Pricing Table Area Start Here -->.*?<!-- Pricing Table Area End Here -->',
        pricing_replacement,
        html,
        flags=re.DOTALL
    )

    # 7. Team Section (team-box-layout1 3 boxes)
    team_replacement = f"""        <!-- Team Area Start Here -->
        <section class="section-padding-lg-3 section-bubble">
            <div class="container">
                <div class="heading-layout1">
                    <h2>Our Dedicated Leadership &amp; Crew</h2>
                    <p>Experienced professionals directing hygienic operations across Greater Accra.</p>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team1.png" alt="Eric Nana Acquah - CEO & Founder">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Eric Nana Acquah</a></h3>
                                <div class="item-subtitle">Chief Executive Officer &amp; Founder</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team2.png" alt="Facility Operations Team">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Operations Management</a></h3>
                                <div class="item-subtitle">Facility &amp; Janitorial Supervisors</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 d-block d-md-none d-lg-block col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team3.png" alt="Technical Specialists">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Field Technicians</a></h3>
                                <div class="item-subtitle">EcoFumes &amp; Carpet Specialists</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Team Area End Here -->"""

    html = re.sub(
        r'<!-- Team Area Start Here -->.*?<!-- Team Area End Here -->',
        team_replacement,
        html,
        flags=re.DOTALL
    )

    # 8. Progress Area (Counters)
    progress_replacement = f"""        <!-- Progress Area Start Here -->
        <section class="progress-wrap-layout1 section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-xl-6 col-lg-8 col-12">
                        <div class="progress-box-layout1">
                            <h2 class="item-title">All of our Specialists are Fully Trained &amp; Vetted</h2>
                            <div class="item-content">
                                <div class="row">
                                    <div class="col-sm-6">
                                        <div class="counter-item">
                                            <div class="counter count-number" data-num="2014">2014</div>
                                            <div class="count-title">Established Year</div>
                                            <div class="bg-icon"><i class="far fa-calendar-alt"></i></div>
                                        </div>
                                    </div>
                                    <div class="col-sm-6">
                                        <div class="counter-item">
                                            <div class="counter count-number" data-num="5">5</div>
                                            <div class="count-title">Core Service Divisions</div>
                                            <div class="bg-icon"><i class="far fa-thumbs-up"></i></div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Progress Area End Here -->"""

    html = re.sub(
        r'<!-- Progress Area Start Here -->.*?<!-- Progress Area End Here -->',
        progress_replacement,
        html,
        flags=re.DOTALL
    )

    # 9. Testimonial Carousel
    testimonials_replacement = f"""        <!-- Testimonial Area Start Here -->
        <section class="section-padding-md-4 bg-Primary bg-common" data-bg-image="img/figure/bg-shape.png">
            <div class="container">
                <div class="heading-layout2 mg-b-30">
                    <h2 class="text-white">What Clients Say <span>About EcoCare</span></h2>
                </div>
                <div class="rc-carousel nav-control-layout1" data-loop="true" data-items="10" data-margin="30"
                    data-autoplay="false" data-autoplay-timeout="3000" data-smart-speed="1000" data-dots="false"
                    data-nav="true" data-nav-speed="false" data-r-x-small="1" data-r-x-small-nav="true"
                    data-r-x-small-dots="false" data-r-x-medium="1" data-r-x-medium-nav="true" data-r-x-medium-dots="false"
                    data-r-small="1" data-r-small-nav="true" data-r-small-dots="false" data-r-medium="2"
                    data-r-medium-nav="true" data-r-medium-dots="false" data-r-large="3" data-r-large-nav="true"
                    data-r-large-dots="false" data-r-extra-large="3" data-r-extra-large-nav="true"
                    data-r-extra-large-dots="false">
                    <div class="testimonial-box-layout1">
                        <p>I’ve never had my laundry handled so professionally! EcoCare’s team did an amazing job with everything, from washing to folding and ironing.</p>
                        <h3 class="item-title">Nana Esi</h3>
                        <div class="item-subtitle">Doctor, Laundry Client</div>
                        <ul class="item-rating">
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                        </ul>
                    </div>
                    <div class="testimonial-box-layout1">
                        <p>EcoCare made my home look brand new! Their cleaning team was thorough, fast, and detail-oriented. The eco-friendly products gave us peace of mind.</p>
                        <h3 class="item-title">Raymond Okyere</h3>
                        <div class="item-subtitle">Tech Lead, Residential Client</div>
                        <ul class="item-rating">
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                        </ul>
                    </div>
                    <div class="testimonial-box-layout1">
                        <p>I had some worn-out couches I thought were ruined. EcoCare worked wonders! They restored my furniture to near-new condition.</p>
                        <h3 class="item-title">Peter Darko</h3>
                        <div class="item-subtitle">Corporate Executive</div>
                        <ul class="item-rating">
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                            <li><i class="fas fa-star"></i></li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        <!-- Testimonial Area End Here -->"""

    html = re.sub(
        r'<!-- Testimonial Area Start Here -->.*?<!-- Testimonial Area End Here -->',
        testimonials_replacement,
        html,
        flags=re.DOTALL
    )

    # 10. Blog Area
    blog_replacement = f"""        <!-- Blog Area Start Here -->
        <section class="section-padding-lg-4 section-bubble">
            <div class="container">
                <div class="heading-layout1">
                    <h2>Hygiene &amp; Cleaning Insights</h2>
                    <p>Practical guides and recommendations from EcoCare's environmental specialists in Accra.</p>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="blog-box-layout1">
                            <div class="item-img">
                                <a href="carpet-cleaning.html"><img src="img/blog/blog7.jpg" alt="Carpet Cleaning Guide"></a>
                            </div>
                            <div class="item-content">
                                <div class="item-date"><i class="fas fa-calendar-alt"></i>November 2026</div>
                                <h3 class="item-title"><a href="carpet-cleaning.html">Steam Extraction vs. Regular Vacuuming for Carpets</a></h3>
                                <div class="item-author">By EcoCare Specialists</div>
                                <p>Standard vacuuming only cleans surface dust. Discover how pressurized hot-water extraction removes deep abrasive grit and allergens.</p>
                                <div class="entry-meta">
                                    <ul>
                                        <li><a href="carpet-cleaning.html" class="text-primary font-weight-bold">Learn More <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="blog-box-layout1">
                            <div class="item-img">
                                <a href="pest-control.html"><img src="img/blog/blog2.jpg" alt="Pest Control Guide"></a>
                            </div>
                            <div class="item-content">
                                <div class="item-date"><i class="fas fa-calendar-alt"></i>November 2026</div>
                                <h3 class="item-title"><a href="pest-control.html">Preparing Your Premises for Fumigation</a></h3>
                                <div class="item-author">By EcoFumes Lead</div>
                                <p>Essential safety checklist for food storage, vacating during treatment, and honoring the mandatory 2 to 4-hour re-entry safety window.</p>
                                <div class="entry-meta">
                                    <ul>
                                        <li><a href="pest-control.html" class="text-primary font-weight-bold">Learn More <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 d-block d-md-none d-lg-block col-12">
                        <div class="blog-box-layout1">
                            <div class="item-img">
                                <a href="single-service1.html#commercial"><img src="img/blog/blog3.jpg" alt="Commercial Janitorial"></a>
                            </div>
                            <div class="item-content">
                                <div class="item-date"><i class="fas fa-calendar-alt"></i>November 2026</div>
                                <h3 class="item-title"><a href="single-service1.html#commercial">Scheduled Janitorial Care for Commercial Offices</a></h3>
                                <div class="item-author">By Facility Operations</div>
                                <p>How consistent daily maintenance, restroom sanitation, and machine floor scrubbing prevent premature facility wear and elevate client trust.</p>
                                <div class="entry-meta">
                                    <ul>
                                        <li><a href="single-service1.html#commercial" class="text-primary font-weight-bold">Learn More <i class="fas fa-angle-right"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Blog Area End Here -->"""

    html = re.sub(
        r'<!-- Blog Area Start Here -->.*?<!-- Blog Area End Here -->',
        blog_replacement,
        html,
        flags=re.DOTALL
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix index.html with EcoCare data!")

build_index()

# ==============================================================================
# 2. CANONICAL ABOUT US: about1.html
# ==============================================================================
def build_about1():
    html = get_orig("about1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="About Us | EcoCare Cleaning Services Limited Ghana",
        description="Learn about EcoCare Cleaning Services Limited, established in 2014 in Accra, Ghana. Led by CEO Eric Nana Acquah, we deliver sustainable, high-standard residential and commercial cleaning."
    )
    html = replace_header_and_footer(html, active_nav="about")

    # Breadcrumb
    html = re.sub(
        r'<div class="breadcrumbs-area">.*?</div>',
        '<div class="breadcrumbs-area">\n                            <h1>About Us</h1>\n                            <ul>\n                                <li>\n                                    <a href="index.html">Home</a>\n                                </li>\n                                <li>About Us</li>\n                            </ul>\n                        </div>',
        html,
        flags=re.DOTALL
    )

    # About Box 1
    about_story = f"""        <!-- About Us Area Start Here -->
        <section class="section-padding-12-9">
            <div class="container">
                <div class="row">
                    <div class="col-lg-7">
                        <div class="about-box-layout1">
                            <div class="item-tag">Know About Us</div>
                            <h2 class="item-title">Delivering Professional Cleaning Across Ghana Since 2014.</h2>
                            <p>EcoCare Cleaning Services Limited was established on September 19, 2014 under the Ghanaian Companies Code (1963). Based in Achimota Mile 7, Accra, we provide comprehensive environmental care, corporate janitorial solutions, EcoFumes pest eradication, Eco-Laundry, and deep carpet extraction.</p>
                            <p>Led by Chief Executive Officer &amp; Founder Eric Nana Acquah, our mission is captured in our corporate motto: <strong>“Protect the Environment, Live Better, Prolong Life.”</strong> We combine industrial-grade equipment, rigorous quality oversight, and eco-conscious cleaning detergents to safeguard health, comfort, and workplace productivity.</p>
                            <div class="list-item">
                                <ul>
                                    <li>
                                        <h3>Health &amp; Environmental Protection</h3>
                                        <p>Utilizing non-toxic, eco-safe formulations that eliminate pathogens and dirt without contaminating indoor air or endangering occupants.</p>
                                    </li>
                                    <li>
                                        <h3>Vetted, Uniformed &amp; Supervised Teams</h3>
                                        <p>Every assignment is executed by trained personnel working under strict operational supervision and documented quality checklists.</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-5">
                        <div class="about-box-layout6">
                            <div class="item-img">
                                <img src="img/figure/about1.jpg" alt="EcoCare Team at Work">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- About Us Area End Here -->"""

    html = re.sub(
        r'<!-- About Us Area Start Here -->.*?<!-- About Us Area End Here -->',
        about_story,
        html,
        flags=re.DOTALL
    )

    # Why Choose Us (3 boxes)
    why_choose = f"""        <!-- Why Choose Area End Here -->
        <section class="section-padding-12-9 bg-Primary section-shape3">
            <div class="container">
                <div class="row gutters-3">
                    <div class="col-lg-4">
                        <div class="why-choose-box-layout2">
                            <div class="item-icon">
                                <i class="fas fa-check"></i>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title">Vetted Professionals</h3>
                                <p>Carefully screened, trustworthy personnel trained in advanced chemical safety, fabric handling, and equipment operation.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="why-choose-box-layout2">
                            <div class="item-icon">
                                <i class="fas fa-check"></i>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title">Quality Assurance</h3>
                                <p>Supervisory walkthroughs and strict adherence to service-level agreements on every residential or corporate visit.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="why-choose-box-layout2">
                            <div class="item-icon">
                                <i class="fas fa-check"></i>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title">Transparent Scoping</h3>
                                <p>Accurate, itemized quotations based on room count, property square meters, and frequency in Ghanaian Cedis (GHS).</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Why Choose Area End Here -->"""

    html = re.sub(
        r'<!-- Why Choose Area End Here -->\s*<section class="section-padding-12-9 bg-Primary section-shape3">.*?<!-- Why Choose Area End Here -->',
        why_choose,
        html,
        flags=re.DOTALL
    )

    # Process Area (4 steps)
    process = f"""        <!-- Process Area Start Here -->
        <section class="section-padding-md bg-common" data-bg-image="img/figure/bg-shape.png">
            <div class="container">
                <div class="heading-layout1">
                    <h2>Our 4-Step Operational Process</h2>
                    <p>Structured, transparent workflow from your first inquiry to final quality sign-off.</p>
                </div>
                <div class="row">
                    <div class="col-lg-3 col-md-6 col-12">
                        <div class="process-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-call-answer"></i>
                            </div>
                            <div class="item-content">
                                <div class="item-number">01</div>
                                <h3 class="item-title">Inquiry &amp; Scoping</h3>
                                <p>Submit your service request online or call our desk to detail your property size and scope.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12">
                        <div class="process-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-search"></i>
                            </div>
                            <div class="item-content">
                                <div class="item-number">02</div>
                                <h3 class="item-title">Site Assessment</h3>
                                <p>For corporate facilities or deep scrubs, we evaluate surface condition, layout, and scheduling needs.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12">
                        <div class="process-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-mop"></i>
                            </div>
                            <div class="item-content">
                                <div class="item-number">03</div>
                                <h3 class="item-title">Execution</h3>
                                <p>Uniformed crew deploys with commercial extractors, scrubbers, and eco-friendly cleaning detergents.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-md-6 col-12">
                        <div class="process-box-layout1">
                            <div class="item-icon">
                                <i class="flaticon-shield"></i>
                            </div>
                            <div class="item-content">
                                <div class="item-number">04</div>
                                <h3 class="item-title">Quality Inspection</h3>
                                <p>Supervisor audits all focus zones to ensure complete client satisfaction and hygienic compliance.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Process Area End Here -->"""

    html = re.sub(
        r'<!-- Process Area Start Here -->.*?<!-- Process Area End Here -->',
        process,
        html,
        flags=re.DOTALL
    )

    # Team section
    team = f"""        <!-- Team Area Start Here -->
        <section class="section-padding-lg-5">
            <div class="container">
                <div class="heading-layout1">
                    <h2>Our Dedicated Leadership</h2>
                    <p>Meet the experienced leaders guiding EcoCare's environmental and facilities care across Ghana.</p>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team1.png" alt="Eric Nana Acquah - CEO & Founder">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Eric Nana Acquah</a></h3>
                                <div class="item-subtitle">Chief Executive Officer &amp; Founder</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6 col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team2.png" alt="Operations Team">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Operations Management</a></h3>
                                <div class="item-subtitle">Facility &amp; Janitorial Supervisors</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 d-block d-md-none d-lg-block col-12">
                        <div class="team-box-layout1">
                            <div class="item-img">
                                <img src="img/team/team3.png" alt="Specialist Field Crews">
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="about1.html">Field Technicians</a></h3>
                                <div class="item-subtitle">EcoFumes &amp; Carpet Specialists</div>
                                <div class="item-social">
                                    <ul>
                                        <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                        <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                        <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Team Area End Here -->"""

    html = re.sub(
        r'<!-- Team Area Start Here -->.*?<!-- Team Area End Here -->',
        team,
        html,
        flags=re.DOTALL
    )

    # Banner & CTA
    html = re.sub(
        r'<h2 class="item-title text-Primary">Together <span>We\'ll Explore</span> New Things</h2>',
        '<h2 class="item-title text-Primary">Dedicated to a <span>Cleaner, Safer</span> Environment</h2>',
        html
    )
    html = html.replace('Book an Appointment', 'Request a Quote')
    html = re.sub(
        r'<a href="#" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Request a Quote<i class="fas fa-angle-right"></i></a>',
        '<a href="calculate-form.html" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Request a Quote<i class="fas fa-angle-right"></i></a>',
        html
    )

    with open("about1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix about1.html with EcoCare data!")

build_about1()

# ==============================================================================
# 3. CANONICAL SERVICE DIRECTORY: service1.html (All 12 Service Listings)
# ==============================================================================
def build_service1():
    html = get_orig("service1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="All Cleaning & Hygiene Services | EcoCare Cleaning Services Ghana",
        description="Explore all 12 professional cleaning, fumigation, laundry, carpet and upholstery services offered by EcoCare Cleaning Services Limited across Greater Accra."
    )
    html = replace_header_and_footer(html, active_nav="services")

    # Breadcrumbs
    html = re.sub(
        r'<div class="breadcrumbs-area">.*?</div>',
        '<div class="breadcrumbs-area">\n                            <h1>Our Services</h1>\n                            <ul>\n                                <li>\n                                    <a href="index.html">Home</a>\n                                </li>\n                                <li>All 12 Service Listings</li>\n                            </ul>\n                        </div>',
        html,
        flags=re.DOTALL
    )

    twelve_services = [
        {"img": "img/service/service7.jpg", "icon": "flaticon-tower", "title": "Office Cleaning", "link": "single-service1.html#office", "desc": "Nightly and daytime corporate office janitorial programs, desk sanitization, and restroom hygiene management."},
        {"img": "img/service/service1.jpg", "icon": "far fa-building", "title": "Commercial Cleaning", "link": "single-service1.html#commercial", "desc": "Comprehensive facility maintenance for commercial plazas, retail branches, healthcare clinics, and business centers."},
        {"img": "img/service/service2.jpg", "icon": "flaticon-clean-1", "title": "Washing &amp; Ironing", "link": "single-service2.html#washing", "desc": "Wash-and-fold, delicate fabric care, crisp steam pressing, and scheduled doorstep collection across Greater Accra."},
        {"img": "img/service/service5.jpg", "icon": "flaticon-clean", "title": "Upholstery Cleaning", "link": "upholstery-cleaning.html", "desc": "Restorative deep cleaning for living room couches, leather furniture conditioning, dining chairs, and mattress sanitization."},
        {"img": "img/service/service.jpg", "icon": "flaticon-clean-2", "title": "House Cleaning Services", "link": "single-service1.html#residential", "desc": "Thorough residential housekeeping for detached homes and apartments on one-off, weekly, or bi-weekly schedules."},
        {"img": "img/service/service3.jpg", "icon": "flaticon-shield", "title": "House &amp; Office Fumigation", "link": "pest-control.html", "desc": "EcoFumes targeted pest eradication for termites, cockroaches, rodents, and mosquitoes with safe re-entry protocols."},
        {"img": "img/service/service6.jpg", "icon": "flaticon-brush", "title": "Industrial Cleaning", "link": "single-service1.html#industrial", "desc": "Heavy-duty scrubbing, degreasing, and sanitation for manufacturing plants, workshops, and distribution logistics hubs."},
        {"img": "img/service/service4.jpg", "icon": "flaticon-mop", "title": "Carpet Cleaning", "link": "carpet-cleaning.html", "desc": "Industrial hot-water steam extraction, traffic lane stain removal, and low-moisture encapsulation for office carpets."},
        {"img": "img/service/service10.jpg", "icon": "flaticon-mop", "title": "Floor, Marble, Tiles &amp; Grout", "link": "single-service1.html#floor", "desc": "Rotary machine floor scrubbing, tile scale removal, grout deep cleaning, and marble polishing to restore brilliance."},
        {"img": "img/service/service8.jpg", "icon": "flaticon-shower", "title": "General Deep Cleaning", "link": "single-service1.html#general", "desc": "Intensive top-to-bottom scrub and sanitization for move-in, move-out, annual refresh, or newly renovated premises."},
        {"img": "img/service/service11.jpg", "icon": "flaticon-tower", "title": "Window &amp; Glass Cleaning", "link": "single-service1.html#window", "desc": "Interior and exterior glass washing, architectural window detailing, and frame descaling for crystal-clear clarity."},
        {"img": "img/service/service9.jpg", "icon": "far fa-calendar-alt", "title": "Event Clean-Up Services", "link": "single-service1.html#event", "desc": "Pre-event prep, active venue portering, and rapid post-event clearance and waste disposal for private and corporate gatherings."}
    ]

    cards_html = ""
    for s in twelve_services:
        cards_html += f"""                    <div class="col-xl-4 col-md-6 mb-4">
                        <div class="service-box-layout2 white-shadow h-100">
                            <div class="item-img">
                                <img src="{s['img']}" alt="{s['title']}" class="w-100">
                            </div>
                            <div class="item-content">
                                <div class="item-icon">
                                    <div class="icon-bg">
                                        <i class="{s['icon']}"></i>
                                    </div>
                                </div>
                                <h3 class="item-title"><a href="{s['link']}">{s['title']}</a></h3>
                                <div class="hover-content">
                                    <p>{s['desc']}</p>
                                    <a href="{s['link']}" class="btn-fill-xs bg-accent text-primarytext">Read More<i class="fas fa-angle-right"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>\n"""

    service_grid_replacement = f"""        <!-- Service Area Start Here -->
        <section class="section-padding-12-9 bg-assh bg-common" data-bg-image="img/figure/bg-shape1.png">
            <div class="container">
                <div class="heading-layout1 text-center mb-5">
                    <h2>EcoCare Specialized Service Directory</h2>
                    <p class="text-muted" style="max-width: 720px; margin: 0 auto;">Discover all 12 comprehensive cleaning, laundry, fumigation, and restoration services delivered by our vetted, supervised personnel in Accra, Ghana.</p>
                </div>
                <div class="row">
{cards_html}                </div>
            </div>
        </section>
        <!-- Service Area End Here -->"""

    html = re.sub(
        r'<!-- Service Area Start Here -->.*?<!-- Service Area End Here -->',
        service_grid_replacement,
        html,
        flags=re.DOTALL
    )

    # Banner Area
    html = re.sub(
        r'<h2 class="item-title text-Primary">Together <span>We\'ll Explore</span> New Things</h2>',
        '<h2 class="item-title text-Primary">Need a Custom <span>Service Plan</span> for Your Property?</h2>',
        html
    )
    html = re.sub(
        r'<a href="#" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Book an Appointment<i class="fas fa-angle-right"></i></a>',
        '<a href="calculate-form.html" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Request a Free Quote<i class="fas fa-angle-right"></i></a>',
        html
    )

    with open("service1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix service1.html with 12 EcoCare service cards!")

build_service1()

# ==============================================================================
# 4. FIVE DEDICATED SERVICE PAGES (Native Clenix Single-Service Layouts)
# ==============================================================================
def get_service_sidebar_html(active_id="cleaning"):
    services = [
        ("cleaning", "single-service1.html", "EcoClean (Cleaning)"),
        ("laundry", "single-service2.html", "Eco-Laundry (Garments)"),
        ("pest", "pest-control.html", "EcoFumes (Pest Control)"),
        ("carpet", "carpet-cleaning.html", "Carpet Deep Cleaning"),
        ("upholstery", "upholstery-cleaning.html", "Upholstery &amp; Furniture"),
        ("all", "service1.html", "All 12 Service Listings"),
    ]
    links_html = ""
    for sid, url, label in services:
        active_style = ' style="font-weight: 600; color: #14287b;"' if sid == active_id else ''
        icon_class = 'fas fa-angle-right text-warning' if sid == active_id else 'flaticon-right-arrow'
        links_html += f'                                    <li><a href="{url}"{active_style}><i class="{icon_class}"></i>{label}</a></li>\n'

    return f"""                    <div class="col-lg-4 sidebar-break-md sidebar-widget-area">
                        <div class="widget widget-category">
                            <div class="heading-layout4">
                                <h4>Our Services</h4>
                            </div>
                            <div class="category-list">
                                <ul>
{links_html}                                </ul>
                            </div>
                        </div>
                        <div class="widget widget-banner">
                            <div class="item-img">
                                <img src="img/figure/widget-banner.png" alt="EcoCare Assistance">
                            </div>
                            <div class="item-content text-center">
                                <h3 class="item-title font-weight-bold text-white mb-2" style="font-size: 20px;">Need Help Booking?</h3>
                                <p class="text-white-50 small mb-3">Speak directly with our customer desk in Achimota Mile 7.</p>
                                <a href="tel:{PHONE_TEL_PRIMARY}" class="fw-btn-fill bg-accent text-primarytext font-weight-bold">{PHONE_PRIMARY}</a>
                            </div>
                        </div>
                        <div class="widget widget-contact-form">
                            <div class="heading-layout4">
                                <h4>Quick Inquiry</h4>
                            </div>
                            <form class="contact-form-box" id="contact-form">
                                <div class="row">
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-user"></i></div>
                                        <input type="text" placeholder="Your Name *" class="form-control" name="name" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-phone"></i></div>
                                        <input type="tel" placeholder="Phone Number *" class="form-control" name="phone" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-envelope"></i></div>
                                        <input type="email" placeholder="Email Address" class="form-control" name="email">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-edit"></i></div>
                                        <textarea placeholder="Message / Details *" class="textarea form-control" name="message" rows="3" required></textarea>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <button type="submit" class="fw-btn-fill bg-accent text-primarytext">Send Inquiry</button>
                                    </div>
                                </div>
                                <div class="form-response"></div>
                            </form>
                        </div>
                    </div>"""

def build_single_service_page(config):
    html = get_orig("single-service1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(html, title=config["title"], description=config["description"])
    html = replace_header_and_footer(html, active_nav="services")

    # Breadcrumbs
    crumb = f"""<div class="breadcrumbs-area">
                            <h1>{config["crumb_heading"]}</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>
                                    <a href="service1.html">Services</a>
                                </li>
                                <li>{config["crumb_leaf"]}</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    # Main content building
    why_choose_cards = ""
    for wc in config["why_choose"]:
        why_choose_cards += f"""                                        <div class="col-lg-6">
                                            <div class="media">
                                                <div class="item-icon">
                                                    <i class="far fa-check-circle"></i>
                                                </div>
                                                <div class="media-body space-md">
                                                    <h3 class="item-title">{wc["title"]}</h3>
                                                    <p>{wc["desc"]}</p>
                                                </div>
                                            </div>
                                        </div>\n"""

    features_li = "".join([f"                                                    <li>{f}</li>\n" for f in config["features"]])

    info_boxes_html = ""
    for ib in config["info_boxes"]:
        info_boxes_html += f"""                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">{ib["title"]}</div>
                                                <div class="item-subtitle">{ib["val"]}</div>
                                            </div>
                                        </div>\n"""

    faq_cards_html = ""
    for i, faq in enumerate(config["faqs"]):
        c_id = f"faqCol{i+1}"
        h_id = f"faqHead{i+1}"
        is_first = (i == 0)
        show_cls = " show" if is_first else ""
        coll_cls = "" if is_first else " collapsed"
        expanded = "true" if is_first else "false"
        faq_cards_html += f"""                                            <div class="card">
                                                <div class="card-header" id="{h_id}">
                                                    <h5 class="heading-title{coll_cls}" data-toggle="collapse" data-target="#{c_id}" 
                                                        aria-expanded="{expanded}" aria-controls="{c_id}">{faq["q"]}</h5>
                                                </div>
                                                <div id="{c_id}" class="collapse{show_cls}" aria-labelledby="{h_id}" data-parent="#accordion">
                                                    <div class="card-body">
                                                        {faq["a"]}
                                                    </div>
                                                </div>
                                            </div>\n"""

    main_service_section = f"""        <!-- Single Service Area Start Here -->
        <section class="section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="single-service-box-layout1">
                            <div class="main-img">
                                <img src="{config["main_img"]}" alt="{config["heading"]}" class="w-100">
                            </div>
                            <div class="service-content">
                                <h2 class="item-title">{config["heading"]}</h2>
                                <p>{config["p1"]}</p>
                                <p>{config["p2"]}</p>
                                <div class="why-choose">
                                    <div class="row">
{why_choose_cards}                                    </div>
                                </div>
                                <div class="service-more-content">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="item-img">
                                                <img src="{config["more_img"]}" alt="{config["more_title"]}" class="w-100">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="item-content">
                                                <h3 class="item-title">{config["more_title"]}</h3>
                                                <p>{config["more_desc"]}</p>
                                                <ul class="item-feature">
{features_li}                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="service-more-info">
                                    <div class="heading-layout4">
                                        <h3>Service Information</h3>
                                    </div>
                                    <div class="row gutters-20">
{info_boxes_html}                                    </div>
                                </div>
                                <div class="service-faq">
                                    <h3 class="item-title">Frequently Asked Questions</h3>
                                    <div id="accordion" class="accordion">
{faq_cards_html}                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
{get_service_sidebar_html(config["active_sidebar_id"])}
                </div>
            </div>
        </section>
        <!-- Single Service Area End Here -->"""

    html = re.sub(
        r'<!-- Single Service Area Start Here -->.*?<!-- Single Service Area End Here -->',
        main_service_section,
        html,
        flags=re.DOTALL
    )

    with open(config["filename"], "w", encoding="utf-8") as f:
        f.write(html)
    print(f"-> Successfully restored native Clenix {config['filename']}!")

# 1. EcoClean (single-service1.html)
build_single_service_page({
    "filename": "single-service1.html",
    "active_sidebar_id": "cleaning",
    "title": "EcoClean — Residential, Commercial & Deep Cleaning | EcoCare Ghana",
    "description": "EcoClean provides professional domestic housekeeping, corporate office janitorial, post-construction scrubbing, floor machine buffing, and window care in Accra, Ghana.",
    "crumb_heading": "EcoClean: Residential & Commercial",
    "crumb_leaf": "EcoClean",
    "main_img": "img/service/service.jpg",
    "heading": "Comprehensive Domestic, Corporate &amp; Industrial Cleaning",
    "p1": "<strong>EcoClean</strong> is EcoCare's flagship facility and environmental care division. We provide structured, reliable cleaning programs for private homes, corporate headquarters, retail stores, healthcare clinics, and industrial facilities across Greater Accra and Ghana.",
    "p2": "Every assignment is performed by trained, vetted staff using high-grade extraction vacuums, rotary scrubbers, color-coded microfiber towels, and eco-conscious cleaning detergents designed to protect your indoor environment without harsh toxic fumes.",
    "why_choose": [
        {"title": "Uniformed & Supervised", "desc": "All cleaners operate in clean EcoCare uniforms under direct on-site supervisory oversight and documented checklists."},
        {"title": "Commercial Equipment", "desc": "Equipped with rotary single-disc floor scrubbers, industrial wet/dry extractors, and calibrated microfibers."}
    ],
    "more_img": "img/service/service10.jpg",
    "more_title": "EcoClean Core Service Modules",
    "more_desc": "From routine residential care to specialized industrial commissioning, we provide customized scoping across Accra:",
    "features": [
        "Residential Housekeeping (Bedrooms, Kitchen, Bathrooms, Living)",
        "Office & Commercial Janitorial (Desks, Restrooms, High-touch surfaces)",
        "Post-Construction Scrubbing & Debris Clearing",
        "Machine Floor Cleaning (Marble, Granite, Tiles & Grout Polishing)",
        "Window & High Architectural Glass Cleaning"
    ],
    "info_boxes": [
        {"title": "Pricing Model", "val": "Quote on Scope (GHS)"},
        {"title": "Availability", "val": "Mon &ndash; Sat: 07am - 06pm"},
        {"title": "Crew Size", "val": "2 to 8+ Supervised Cleaners"},
        {"title": "Coverage", "val": "Greater Accra &amp; Region"},
        {"title": "Telephone", "val": "+233 24 901 4253"},
        {"title": "E-mail", "val": "ecocaregh1on1@gmail.com"}
    ],
    "faqs": [
        {"q": "Do I need to supply cleaning equipment or detergents?", "a": "No. EcoCare cleaning crews arrive fully equipped with professional industrial vacuums, rotary floor scrubbers, ladders, microfiber systems, and all required eco-conscious cleaning detergents."},
        {"q": "How do you determine pricing for house or office cleaning?", "a": "Pricing depends on your property size, number of bedrooms and bathrooms, current surface condition, and whether you require routine maintenance or an intensive deep scrub. We provide a transparent, no-obligation quote before starting work."},
        {"q": "Do I need to be present during the service?", "a": "While we recommend being present at the start for initial walkthrough instructions and at the end for final inspection, it is not mandatory. Many clients provide access and return upon completion."},
        {"q": "Do you provide recurring office janitorial contracts?", "a": "Yes. We manage daily, bi-weekly, and monthly corporate janitorial agreements for corporate headquarters, embassies, clinics, and commercial plazas across Accra."}
    ]
})

# 2. Eco-Laundry (single-service2.html)
def build_single_service2():
    html = get_orig("single-service2.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Eco-Laundry — Professional Garment Care, Washing & Ironing | EcoCare Ghana",
        description="Eco-Laundry provides meticulous washing, steam ironing, delicate garment care, dry cleaning, and scheduled pickup/delivery across Greater Accra."
    )
    html = replace_header_and_footer(html, active_nav="services")

    # Breadcrumbs
    crumb = f"""<div class="breadcrumbs-area">
                            <h1>Eco-Laundry: Garment &amp; Fabric Care</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>
                                    <a href="service1.html">Services</a>
                                </li>
                                <li>Eco-Laundry</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    # Content replacement
    laundry_content = f"""        <!-- Single Service Area Start Here -->
        <section class="section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8 order-lg-2">
                        <div class="single-service-box-layout1">
                            <h2 class="service-title">Meticulous Laundry, Fabric Preservation &amp; Ironing Care</h2>
                            <p><strong>Eco-Laundry</strong> is EcoCare's dedicated garment and textile care branch headquartered at Achimota Mile 7, Accra. We understand that your clothing and household linens represent personal comfort, professional image, and financial investment. Our laundry facility combines high-capacity commercial washing technology with delicate artisanal finishing to keep every item fresh, sanitized, and impeccably pressed.</p>
                            <div class="main-img">
                                <img src="img/service/service2.jpg" alt="Eco-Laundry Garment Care" class="w-100">
                            </div>
                            <div class="service-content">
                                <p>Whether you require weekly family wash-and-fold services, crisp steam pressing for corporate suits and traditional wear, or bulk linen management for guest houses and hospitality venues, Eco-Laundry guarantees prompt turnaround and fabric-safe cleaning agents.</p>
                                <div class="why-choose">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="media">
                                                <div class="item-icon">
                                                    <i class="far fa-check-circle"></i>
                                                </div>
                                                <div class="media-body space-md">
                                                    <h3 class="item-title">Delicate Fabric Protection</h3>
                                                    <p>Color sorting, fabric-specific temperature cycles, and pH-neutral detergents preserve fiber longevity.</p>
                                                </div>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="media">
                                                <div class="item-icon">
                                                    <i class="far fa-check-circle"></i>
                                                </div>
                                                <div class="media-body space-md">
                                                    <h3 class="item-title">Doorstep Pickup &amp; Delivery</h3>
                                                    <p>Convenient scheduled collection and delivery routes across Greater Accra (Achimota, East Legon, Airport, Spintex).</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="service-more-content">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="item-img">
                                                <img src="img/service/service11.jpg" alt="Garment Pressing" class="w-100">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="item-content">
                                                <h3 class="item-title">Eco-Laundry Core Services</h3>
                                                <p>Comprehensive textile and wardrobe care delivered with speed and care:</p>
                                                <ul class="item-feature">
                                                    <li>Wash, Dry &amp; Fold (Everyday casuals &amp; work wear)</li>
                                                    <li>Steam Ironing &amp; Hand-Finishing</li>
                                                    <li>Delicate Silks &amp; Ceremonial Attire Care</li>
                                                    <li>Heavy Duvets, Comforters &amp; Blankets</li>
                                                    <li>Curtain Drapery Sanitization</li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="service-more-info">
                                    <div class="heading-layout4">
                                        <h3>Service Information</h3>
                                    </div>
                                    <div class="row gutters-20">
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">Turnaround</div>
                                                <div class="item-subtitle">24 &ndash; 48 Hours</div>
                                            </div>
                                        </div>
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">Service Days</div>
                                                <div class="item-subtitle">Mon &ndash; Sat</div>
                                            </div>
                                        </div>
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">Delivery</div>
                                                <div class="item-subtitle">Scheduled Accra</div>
                                            </div>
                                        </div>
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">Hours</div>
                                                <div class="item-subtitle">07:00am - 06:00pm</div>
                                            </div>
                                        </div>
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">Contact</div>
                                                <div class="item-subtitle">{PHONE_PRIMARY}</div>
                                            </div>
                                        </div>
                                        <div class="col-xl-4 col-lg-6 col-md-4 col-sm-6 col-12">
                                            <div class="single-info">
                                                <div class="item-title">E-mail</div>
                                                <div class="item-subtitle">{EMAIL_PRIMARY}</div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="service-faq">
                                    <h3 class="item-title">Frequently Asked Questions</h3>
                                    <div id="accordion" class="accordion">
                                        <div class="card">
                                            <div class="card-header" id="headingOne">
                                                <h5 class="heading-title" data-toggle="collapse" data-target="#collapseOne" 
                                                    aria-expanded="true" aria-controls="collapseOne">What is the standard turnaround time for laundry?</h5>
                                            </div>
                                            <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                                                <div class="card-body">
                                                    Standard wash, dry, and fold orders are ready within 24 to 48 hours. Express same-day or 24-hour expedited services are available upon request when arranged during morning drop-off.
                                                </div>
                                            </div>
                                        </div>
                                        <div class="card">
                                            <div class="card-header" id="headingTwo">
                                                <h5 class="heading-title collapsed" data-toggle="collapse" data-target="#collapseTwo" 
                                                    aria-expanded="false" aria-controls="collapseTwo">Can EcoCare pick up and deliver my clothes?</h5>
                                            </div>
                                            <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                                                <div class="card-body">
                                                    Yes! We provide scheduled pickup and delivery across Greater Accra. Simply call our customer care lines or request a pickup through our online booking form.
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
{get_service_sidebar_html("laundry")}
                </div>
            </div>
        </section>
        <!-- Single Service Area End Here -->"""

    html = re.sub(
        r'<!-- Single Service Area Start Here -->.*?<!-- Single Service Area End Here -->',
        laundry_content,
        html,
        flags=re.DOTALL
    )

    with open("single-service2.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix single-service2.html (Eco-Laundry)!")

build_single_service2()

# 3. EcoFumes (pest-control.html)
build_single_service_page({
    "filename": "pest-control.html",
    "active_sidebar_id": "pest",
    "title": "EcoFumes — Fumigation & Pest Control Services | EcoCare Ghana",
    "description": "EcoFumes delivers targeted fumigation, termite barriers, cockroach eradication, and rodent control for homes, corporate premises, and warehouses in Accra.",
    "crumb_heading": "EcoFumes: Fumigation &amp; Pest Control",
    "crumb_leaf": "EcoFumes",
    "main_img": "img/service/service3.jpg",
    "heading": "Scientific Pest Management &amp; Fumigation Services",
    "p1": "<strong>EcoFumes</strong> is EcoCare's specialized pest eradication and structural fumigation unit. Pests threaten human health, damage valuable physical assets, contaminate food supplies, and violate municipal hygiene regulations. We apply an Integrated Pest Management (IPM) methodology that targets the root causes of infestations rather than just surface symptoms.",
    "p2": "Our licensed technicians utilize regulated, approved insecticides, rodenticides, and misting compounds delivered through ultra-low volume (ULV) cold foggers, thermal fogging units, and precise crack-and-crevice baiting guns across Greater Accra and Ghana.",
    "why_choose": [
        {"title": "Targeted Species IPM", "desc": "Custom treatments specifically calibrated for subterranean termites, German cockroaches, rodents, and mosquitoes."},
        {"title": "Rigorous Safety Protocol", "desc": "Clear pre-treatment instructions and mandatory 2 to 4-hour re-entry safety windows protect occupants and pets."}
    ],
    "more_img": "img/service/service6.jpg",
    "more_title": "Targeted Pest Solutions",
    "more_desc": "Comprehensive chemical barrier and eradication methods for homes and corporate facilities:",
    "features": [
        "Termite Sub-Soil Chemical Barriers & Anti-Termite Drilling",
        "Cockroach Precision Gel Baiting & Residual Spraying",
        "Tamper-Resistant Rodent Bait Stations & Exclusion",
        "Mosquito Outdoor Thermal Fogging & Indoor Misting",
        "Bed Bug Multi-Stage Seam & Baseboard Treatment"
    ],
    "info_boxes": [
        {"title": "Pricing Model", "val": "Quote on Inspection (GHS)"},
        {"title": "Target Pests", "val": "Termites, Roaches, Rodents"},
        {"title": "Re-Entry Window", "val": "2 &ndash; 4 Hours Safety"},
        {"title": "Coverage", "val": "Accra &amp; Regional Sites"},
        {"title": "Telephone", "val": "+233 24 901 4253"},
        {"title": "E-mail", "val": "ecocaregh1on1@gmail.com"}
    ],
    "faqs": [
        {"q": "How often should a residential property or office be fumigated?", "a": "For residential properties, semi-annual (every 6 months) treatments generally provide effective preventive coverage. For commercial food establishments, retail spaces, and warehouses, quarterly maintenance is strongly advised."},
        {"q": "Are the chemicals safe for indoor spaces?", "a": "Yes. We use EPA-approved public health insecticides formulated for indoor environments. When safety instructions and mandatory 2-4 hour re-entry windows are followed, treatments leave behind odorless, safe residual barriers."},
        {"q": "What preparations are required before an EcoFumes visit?", "a": "Occupants should cover or store all food items, cooking utensils, and drinking water containers. Humans and domestic pets must vacate during treatment and observe the mandatory 2 to 4-hour re-entry window."},
        {"q": "Can you handle termite infestations in wooden roofs and door frames?", "a": "Yes. We perform specialized non-repellent termiticide injections that transfer through the termite colony to eliminate the queen and protect structural wood."}
    ]
})

# 4. Carpet Cleaning (carpet-cleaning.html)
build_single_service_page({
    "filename": "carpet-cleaning.html",
    "active_sidebar_id": "carpet",
    "title": "Carpet Cleaning & Restoration Services | EcoCare Ghana",
    "description": "High-power hot water extraction, stain elimination, and low-moisture encapsulation for residential rugs and commercial carpets in Accra.",
    "crumb_heading": "Carpet Deep Cleaning &amp; Restoration",
    "crumb_leaf": "Carpet Cleaning",
    "main_img": "img/service/service4.jpg",
    "heading": "Industrial Carpet Restoration &amp; Deep Fiber Extraction",
    "p1": "Carpets act as giant air filters in homes and commercial facilities, trapping dirt, sand, fine dust particles, allergens, bacteria, and tracked-in pollutants deep within their pile. Standard vacuuming only cleans the top 15% of carpet fibers, leaving abrasive grit at the base that steadily cuts through fibers with foot traffic.",
    "p2": "<strong>EcoCare Carpet Services</strong> employs heavy-duty dual-vacuum extraction machines, high-temperature hot-water injection, and low-moisture encapsulation chemistry to revive heavily soiled carpets, remove stubborn traffic lane stains, and restore indoor air cleanliness across Accra.",
    "why_choose": [
        {"title": "Deep Steam Extraction", "desc": "Pressurized hot water dissolves bonded oils, and high-velocity suction recovers 90% of moisture immediately."},
        {"title": "Low-Moisture Encapsulation", "desc": "Fast-drying polymer chemistry for corporate offices, ready for foot traffic within 1 to 2 hours."}
    ],
    "more_img": "img/service/service10.jpg",
    "more_title": "Our 5-Stage Carpet Process",
    "more_desc": "Systematic restorative care that revitalizes fiber elasticity and color vibrance:",
    "features": [
        "Fiber Assessment & Colorfastness Testing",
        "Industrial High-Suction Dry Vacuuming",
        "Pre-Conditioning & Mechanical Agitation of Stains",
        "Hot-Water Extraction Rinse & Immediate Recovery",
        "Deodorization & Pile Grooming"
    ],
    "info_boxes": [
        {"title": "Pricing Model", "val": "Per Sqm / Dimensions (GHS)"},
        {"title": "Drying Time", "val": "4 &ndash; 8 Hours (Steam)"},
        {"title": "Office Dry Time", "val": "1 &ndash; 2 Hours (Encaps.)"},
        {"title": "Coverage", "val": "Greater Accra Region"},
        {"title": "Telephone", "val": "+233 24 901 4253"},
        {"title": "E-mail", "val": "ecocaregh1on1@gmail.com"}
    ],
    "faqs": [
        {"q": "How long does a carpet take to dry after deep cleaning?", "a": "Typically between 4 to 8 hours depending on ambient indoor ventilation, humidity levels, and air movement. In commercial offices utilizing low-moisture encapsulation, carpets are dry within 1 to 2 hours."},
        {"q": "How is carpet cleaning pricing determined?", "a": "Pricing is calculated based on total square footage (or square meters), rug dimensions, fiber complexity, and the degree of staining or soiling. We provide clear, itemized quotes prior to beginning service."},
        {"q": "Can you remove coffee, ink, and grease stains?", "a": "Yes. Our technicians use specialized pH-balanced spotting agents to break down organic spills, grease, coffee, tea, and pet accidents without causing bleaching or fiber damage."},
        {"q": "Do you clean loose area rugs as well as wall-to-wall carpeting?", "a": "Yes. We clean both fitted wall-to-wall carpets on-site and loose area rugs at your premises with specialized edge-binding protection."}
    ]
})

# 5. Upholstery Cleaning (upholstery-cleaning.html)
build_single_service_page({
    "filename": "upholstery-cleaning.html",
    "active_sidebar_id": "upholstery",
    "title": "Upholstery & Furniture Cleaning Services | EcoCare Ghana",
    "description": "Expert fabric couch cleaning, leather conditioning, mattress allergen sanitization, and dining chair restoration in Accra, Ghana.",
    "crumb_heading": "Upholstery &amp; Furniture Cleaning",
    "crumb_leaf": "Upholstery",
    "main_img": "img/service/service5.jpg",
    "heading": "Deep Fabric Sanitization, Leather Care &amp; Furniture Restoration",
    "p1": "Sofas, armchairs, dining chairs, and office chairs absorb everyday skin oils, perspiration, beverage spills, dust particles, and pet dander. Over time, these residues dull fabric colors, break down protective coatings, and generate subtle unpleasant odors. Mattresses also harbor microscopic dust mites that exacerbate asthma and allergic reactions.",
    "p2": "<strong>EcoCare Upholstery Cleaning</strong> brings specialized mobile upholstery equipment directly to your premises. Using delicate fiber extraction wands, pH-appropriate fabric detergents, and leather conditioning balms, we restore the visual brilliance and hygienic freshness of your furniture without damaging fragile seams or cushion padding.",
    "why_choose": [
        {"title": "Gentle Hand Scrubbing", "desc": "Customized agitation using soft horsehair brushes and fiber-safe emulsifiers lifts dirt without fiber abrasion."},
        {"title": "Mattress Allergen Extraction", "desc": "High-suction vacuum extraction pulls out dead skin cells, perspiration salts, and dust mite colonies."}
    ],
    "more_img": "img/service/service8.jpg",
    "more_title": "Furniture & Textile Specialties",
    "more_desc": "Comprehensive care for residential furniture and high-volume corporate seating:",
    "features": [
        "Fabric Couches, Sofas &amp; Sectionals",
        "Leather Furniture Cleaning &amp; Nutrient Conditioning",
        "Dining Chairs &amp; Fabric Bar Stools",
        "Mattress Deep Sanitization &amp; Allergen Removal",
        "Corporate Task Chairs &amp; Conference Seating"
    ],
    "info_boxes": [
        {"title": "Pricing Model", "val": "Per Seat / Piece (GHS)"},
        {"title": "Drying Time", "val": "4 &ndash; 6 Hours"},
        {"title": "Leather Care", "val": "pH-Balanced Balm"},
        {"title": "Coverage", "val": "Greater Accra Region"},
        {"title": "Telephone", "val": "+233 24 901 4253"},
        {"title": "E-mail", "val": "ecocaregh1on1@gmail.com"}
    ],
    "faqs": [
        {"q": "How long does furniture take to dry after cleaning?", "a": "Our specialized upholstery tools extract the vast majority of rinse fluid, allowing fabrics to dry completely in 4 to 6 hours with normal airflow."},
        {"q": "How do you treat leather furniture?", "a": "We use pH-neutral leather cleansers that dissolve embedded soil from leather pores, followed by rich conditioning creams that replenish natural oils and prevent cracking."},
        {"q": "Can you clean office task chairs in bulk?", "a": "Yes. We regularly handle scheduled weekend or after-hours batch cleaning for corporate workstations and conference rooms across Accra."},
        {"q": "How is upholstery pricing calculated?", "a": "Pricing is based on furniture size (e.g., 3-seater couch, sectional, armchair, or dining chair) and material (fabric vs. leather). We provide a confirmed total before starting."}
    ]
})


# ==============================================================================
# 9. PRICING TABLE: pricing-table.html
# ==============================================================================
def build_pricing_table():
    html = get_orig("pricing-table.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Affordable Cleaning Plans & Pricing | EcoCare Ghana",
        description="Transparent pricing and flexible service packages for residential, commercial, and post-construction cleaning in Accra, Ghana."
    )
    html = replace_header_and_footer(html, active_nav="pricing")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Affordable Cleaning Plans</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Pricing</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    # Pricing table area
    pricing_area = """        <!-- Pricing Table Area Start Here -->
        <section class="section-padding-12-9">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1 border-aash light-hover">
                            <div class="item-icon">
                                <i class="flaticon-clean"></i>
                            </div>
                            <h3 class="item-title">Essential Residential</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>All Surfaces Hand Wiped</li>
                                    <li><i class="fas fa-check"></i>Floors Mopped &amp; Sanitized</li>
                                    <li><i class="fas fa-check"></i>General Dusting &amp; Cobwebs</li>
                                    <li><i class="fas fa-check"></i>Kitchen &amp; Bath Deep Scrub</li>
                                    <li><i class="fas fa-check"></i>Eco-Friendly Detergents</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency">GH&#8373; 350</div>
                                <div class="item-duration">/starting visit</div>
                            </div>
                            <a href="calculate-form.html?plan=residential" class="btn-fill-xl bg-accent text-primarytext">Book Residential</a>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1 border-aash light-hover">
                            <div class="popular-text">Popular Scope!</div>
                            <div class="item-icon popular-shape">
                                <i class="flaticon-mop"></i>
                            </div>
                            <h3 class="item-title">Deep Move-In &amp; Post-Build</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>Paint &amp; Cement Residue Stripping</li>
                                    <li><i class="fas fa-check"></i>High-Level Dust &amp; Glass Clean</li>
                                    <li><i class="fas fa-check"></i>Appliance &amp; Cabinet Detailing</li>
                                    <li><i class="fas fa-check"></i>Restroom Descaling &amp; Sanitizing</li>
                                    <li><i class="fas fa-check"></i>Post-Work Walkthrough Inspection</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency">Custom</div>
                                <div class="item-duration">/quoted on scope</div>
                            </div>
                            <a href="calculate-form.html?plan=deep-clean" class="btn-fill-xl bg-accent text-primarytext">Request Free Quote</a>
                        </div>
                    </div>
                    <div class="col-lg-4">
                        <div class="pricing-box-layout1 border-aash light-hover">
                            <div class="item-icon">
                                <i class="flaticon-clean-2"></i>
                            </div>
                            <h3 class="item-title">Corporate Facility Care</h3>
                            <div class="item-feature">
                                <ul>
                                    <li><i class="fas fa-check"></i>Dedicated Janitorial Deployment</li>
                                    <li><i class="fas fa-check"></i>Daily Trash Removal &amp; Sanitizing</li>
                                    <li><i class="fas fa-check"></i>Restroom Hygiene Supplies</li>
                                    <li><i class="fas fa-check"></i>Carpet &amp; Floor Care</li>
                                    <li><i class="fas fa-check"></i>Flexible After-Hours Schedules</li>
                                </ul>
                            </div>
                            <div class="item-price">
                                <div class="item-currency">Contract</div>
                                <div class="item-duration">/monthly billing</div>
                            </div>
                            <a href="contact.html?plan=corporate" class="btn-fill-xl bg-accent text-primarytext">Enquire Facility Care</a>
                        </div>
                    </div>
                    <div class="col-12 text-center mt-4">
                        <p class="text-muted"><i class="fas fa-info-circle mr-1"></i> All pricing is in Ghanaian Cedis (GHS). Final quotations are confirmed upon site inspection or room-by-room parameter measurement.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Pricing Table Area End Here -->"""

    html = re.sub(
        r'<!-- Pricing Table Area Start Here -->.*?<!-- Pricing Table Area End Here -->',
        pricing_area,
        html,
        flags=re.DOTALL
    )

    # Banner Area
    banner_area = """        <!-- Banner Area Start Here -->
        <section class="banner-wrap-layout2 bg-common" data-bg-image="img/figure/banner-bg1.jpg">
            <div class="container">
                <div class="row d-flex align-items-center">
                    <div class="col-lg-6 col-12">
                        <div class="banner-box-layout4">
                            <h2 class="item-title text-Primary">Need a Tailored Assessment <span>for Your Property?</span></h2>
                            <a href="calculate-form.html" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Book an Inspection<i class="fas fa-angle-right"></i></a>
                        </div>
                    </div>
                    <div class="col-lg-6 col-12">
                        <div class="banner-box-layout5">
                            <div class="item-icon shape1">
                                <img src="img/figure/icon-shape4.png" alt="shape">
                            </div>
                            <div class="item-icon shape2">
                                <img src="img/figure/icon-shape3.png" alt="shape">
                            </div>
                            <div class="item-icon shape3">
                                <img src="img/figure/icon-shape2.png" alt="shape">
                            </div>
                            <div class="item-icon shape4">
                                <img src="img/figure/icon-shape1.png" alt="shape">
                            </div>
                            <div class="item-img">
                                <img src="img/figure/banner-figure.png" alt="figure">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Banner Area End Here -->"""

    html = re.sub(
        r'<!-- Banner Area Start Here -->.*?<!-- Banner Area End Here -->',
        banner_area,
        html,
        flags=re.DOTALL
    )

    with open("pricing-table.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix pricing-table.html!")

build_pricing_table()


# ==============================================================================
# 10. ONLINE BOOKING / ESTIMATE CALCULATOR: calculate-form.html
# ==============================================================================
def build_calculate_form():
    html = get_orig("calculate-form.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Request a Free Estimate & Booking | EcoCare Ghana",
        description="Calculate and request an authentic cleaning, fumigation, laundry, or upholstery care quote from EcoCare in Accra, Ghana."
    )
    html = replace_header_and_footer(html, active_nav="pages")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Online Booking &amp; Estimate</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Booking Form</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    # Calculation Area
    calc_area = """        <!-- Calculation Area Start Here -->
        <section class="section-padding-12-9">
            <div class="container">
                <div class="row">
                    <div class="col-xl-7 col-lg-6 col-12">
                        <div class="about-box-layout1">
                            <h2 class="item-title">Transparent Pricing &amp; Tailored Cleaning Solutions</h2>
                            <div class="item-subtitle">Reliable, eco-friendly cleaning, fumigation, laundry, and upholstery care tailored to your specific premises.</div>
                            <p>Every residential home and corporate facility across Greater Accra has distinct floor layouts, surface materials, and sanitization priorities. EcoCare evaluates your exact property parameters so you pay only for the exact scope of work required.</p>
                            <div class="list-item">
                                <ul>
                                    <li>
                                        <h3>Client-Centric Quality Walkthrough</h3>
                                        <p>Our dedicated supervisors conduct a post-service walkthrough with you to verify complete satisfaction before wrapping up.</p>
                                    </li>
                                    <li>
                                        <h3>Biodegradable &amp; Safe Formulations</h3>
                                        <p>We use eco-conscious, plant-derived detergents and certified pest-control formulations safe for families, pets, and workplace teams.</p>
                                    </li>
                                    <li>
                                        <h3>Flexible Scheduling</h3>
                                        <p>Book one-time deep cleaning, regular weekly maintenance, or scheduled weekend commercial sanitation without disrupting your routine.</p>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-5 col-lg-6 col-12">
                        <div class="about-box-layout2">
                            <h3 class="item-title">Request An Estimate</h3>
                            <form class="contact-form-box" id="contact-form">
                                <div class="row gutters-10">
                                    <div class="col-12 form-group">
                                        <select class="select2" name="service" id="form-service">
                                            <option value="residential">Residential Cleaning (EcoClean)</option>
                                            <option value="commercial">Commercial Janitorial (EcoClean)</option>
                                            <option value="laundry">Eco-Laundry &amp; Dry Cleaning</option>
                                            <option value="fumigation">EcoFumes Pest Control &amp; Fumigation</option>
                                            <option value="carpet">Carpet Deep Cleaning</option>
                                            <option value="upholstery">Upholstery &amp; Furniture Cleaning</option>
                                            <option value="post-construction">Post-Construction Cleaning</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <select class="select2" name="property_type" id="form-property">
                                            <option value="residential-house">Residential House / Compound</option>
                                            <option value="apartment">Apartment / Flat</option>
                                            <option value="office">Corporate Office</option>
                                            <option value="retail">Retail / Showroom</option>
                                            <option value="warehouse">Industrial / Warehouse</option>
                                            <option value="other">Other Facility</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <select class="select2" name="size_sqm" id="form-size">
                                            <option value="small">Small (&lt; 100 sqm)</option>
                                            <option value="medium">Medium (100 - 300 sqm)</option>
                                            <option value="large">Large (300 - 600 sqm)</option>
                                            <option value="corporate">Commercial (600+ sqm)</option>
                                            <option value="per-item">Per Piece (Carpet / Upholstery)</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <select class="select2" name="rooms" id="form-rooms">
                                            <option value="1-2">1 &ndash; 2 Bedrooms / Rooms</option>
                                            <option value="3-4">3 &ndash; 4 Bedrooms / Rooms</option>
                                            <option value="5-plus">5+ Bedrooms / Rooms</option>
                                            <option value="open-office">Open-Plan Office</option>
                                            <option value="na">Not Applicable</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <select class="select2" name="bathrooms" id="form-bathrooms">
                                            <option value="1-2">1 &ndash; 2 Bathrooms</option>
                                            <option value="3-4">3 &ndash; 4 Bathrooms</option>
                                            <option value="5-plus">5+ Restrooms</option>
                                            <option value="na">Not Applicable</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 form-group">
                                        <select class="select2" name="frequency" id="form-frequency">
                                            <option value="one-time">One-Time Deep Clean</option>
                                            <option value="weekly">Weekly Routine</option>
                                            <option value="biweekly">Bi-Weekly Maintenance</option>
                                            <option value="monthly">Monthly Contract</option>
                                        </select>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <input type="text" placeholder="Area / Landmark in Accra" class="form-control" name="location" id="form-location" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-md-6 form-group datetime-picker">
                                        <i class="far fa-calendar-alt"></i>
                                        <input type="text" class="form-control rt-date" placeholder="Preferred Date" name="date" id="form-date" required/>
                                    </div>
                                    <div class="col-md-6 form-group datetime-picker">
                                        <i class="far fa-clock"></i>
                                        <input type="text" class="form-control rt-time" placeholder="Preferred Time" name="time" id="form-time" required/>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <input type="text" placeholder="Your Name" class="form-control" name="name" id="form-name" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-md-6 col-12 form-group">
                                        <input type="tel" placeholder="Phone Number (e.g. 024 901 4253)" class="form-control" name="phone" id="form-phone" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <input type="email" placeholder="E-mail Address" class="form-control" name="email" id="form-email">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group mg-b-20">
                                        <textarea placeholder="Specific Requirements / Address Details" class="textarea form-control" name="message" id="form-message" rows="3" required></textarea>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <button type="submit" class="fw-btn-fill bg-accent text-primarytext">Request Free Estimate<i class="fas fa-angle-right"></i></button>
                                    </div>
                                </div>
                                <div class="form-response"></div>
                            </form>
                            <div class="text-center mt-3">
                                <small class="text-muted"><i class="fab fa-whatsapp text-success mr-1"></i> Prefer instant chat? WhatsApp us at <a href="https://wa.me/233249014253" class="text-primary font-weight-bold" target="_blank">+233 24 901 4253</a></small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Calculation Area End Here -->"""

    html = re.sub(
        r'<!-- Calculation Area Start Here -->.*?<!-- Calculation Area End Here -->',
        calc_area,
        html,
        flags=re.DOTALL
    )

    with open("calculate-form.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix calculate-form.html!")

build_calculate_form()


# ==============================================================================
# 11. FAQ PAGE: faq.html
# ==============================================================================
def build_faq():
    html = get_orig("faq.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Frequently Asked Questions | EcoCare Ghana",
        description="Common questions about EcoCare cleaning services, service areas across Greater Accra, pricing in GHS, drying times, and fumigation preparation."
    )
    html = replace_header_and_footer(html, active_nav="pages")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Frequently Asked Questions</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>FAQ</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    faqs_data = [
        ("headingOne", "collapseOne", "Which areas in Ghana does EcoCare cover?", "EcoCare provides comprehensive cleaning, fumigation, laundry, carpet, and upholstery services across the Greater Accra Region, including Achimota, Legon, Airport Residential, Cantonments, Dzorwulu, Ridge, Osu, Spintex, Tema, Dansoman, and surrounding districts. Contact us for custom arrangements outside Greater Accra.", True),
        ("headingTwo", "collapseTwo", "How can I request a service quotation or consultation?", "You can submit an enquiry through our Online Booking Form, send an email to ecocaregh1on1@gmail.com, or contact our customer support line directly at +233 24 901 4253 / +233 24 380 7100. We will discuss your specific property parameters and provide an itemized quote.", False),
        ("headingThree", "collapseThree", "Are cleaning materials, tools, and equipment provided by EcoCare?", "Yes. Our cleaning crews arrive on-site fully equipped with professional industrial vacuum extractors, floor polishers, microfiber cleaning kits, ladders, and eco-friendly, biodegradable detergents. You do not need to provide cleaning supplies.", False),
        ("headingFour", "collapseFour", "Do I need to be present during the cleaning service?", "While you or an authorized representative should be present at the start to grant access and at completion for the walkthrough inspection, you do not need to remain on-site during the entire cleaning process.", False),
        ("headingFive", "collapseFive", "How is carpet and upholstery pricing calculated?", "Pricing is calculated transparently based on measurable dimensions (square footage or square meters for fitted carpets), piece counts and fabric type (leather vs. fabric seating, sofa size), and the level of deep soiling or spot treatment required. We confirm all costs before beginning work.", False),
        ("headingSix", "collapseSix", "How long do carpets and upholstery take to dry?", "With our high-velocity extraction equipment, standard upholstery dries within 4 to 6 hours, while hot-water extraction carpets dry within 4 to 8 hours under normal indoor ventilation. In commercial settings utilizing low-moisture encapsulation, carpets are dry within 1 to 2 hours.", False),
        ("headingSeven", "collapseSeven", "Can you arrange laundry pickup and doorstep delivery?", "Yes! Eco-Laundry offers scheduled collection and doorstep return across Accra. You can bundle everyday wash-and-fold laundry, delicate dry-cleaned garments, bed linens, and curtains.", False),
        ("headingEight", "collapseEight", "What should I do to prepare my premises for pest control (EcoFumes)?", "Prior to treatment, please clear food items, kitchen utensils, and pet dishes into sealed containers or refrigerators. Cover aquariums and ensure family members and pets vacate the premises during application. Re-entry is safe 2 to 4 hours post-treatment after airing out the space.", False),
        ("headingNine", "collapseNine", "Can I reschedule a booked service?", "Yes. If you need to postpone or adjust your appointment, please contact us at least 24 hours in advance via telephone (+233 24 901 4253) or email so we can reassign our field teams to your preferred alternative date without service interruption.", False),
    ]

    cards_html = ""
    for hid, cid, q, a, is_open in faqs_data:
        collapsed_cls = "" if is_open else " collapsed"
        show_cls = " show" if is_open else ""
        expanded_attr = "true" if is_open else "false"
        cards_html += f"""                                <div class="card">
                                    <div class="card-header" id="{hid}">
                                        <h5 class="heading-title{collapsed_cls}" data-toggle="collapse" data-target="#{cid}" 
                                            aria-expanded="{expanded_attr}" aria-controls="{cid}">{q}</h5>
                                    </div>
                                    <div id="{cid}" class="collapse{show_cls}" aria-labelledby="{hid}" data-parent="#accordion">
                                        <div class="card-body">
                                            {a}
                                        </div>
                                    </div>
                                </div>\n"""

    faq_section = f"""        <!-- Faq Area Start Here -->
        <section class="section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="faq-box-layout1">
                            <div id="accordion" class="accordion">
{cards_html}                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 sidebar-break-md sidebar-widget-area">
                        <div class="widget widget-contact-form">
                            <div class="heading-layout4">
                                <h4>Have Any Questions?</h4>
                            </div>
                            <form class="contact-form-box" id="contact-form">
                                <div class="row">
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-user"></i></div>
                                        <input type="text" placeholder="Name" class="form-control" name="name" data-error="Name field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-envelope"></i></div>
                                        <input type="email" placeholder="E-mail Address" class="form-control" name="email" data-error="email field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-phone-volume"></i></div>
                                        <input type="text" placeholder="Phone" class="form-control" name="phone" data-error="Phone field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-question"></i></div>
                                        <input type="text" placeholder="Subject" class="form-control" name="subject" data-error="Subject field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-comments"></i></div>
                                        <textarea placeholder="Your Question / Message" class="textarea form-control" name="message" id="form-message" rows="4" cols="20" 
                                        data-error="Message field is required" required></textarea>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <button type="submit" class="fw-btn-fill bg-accent text-primarytext">Send Message</button>
                                    </div>
                                </div>
                                <div class="form-response"></div>
                            </form>
                        </div>
                        <div class="widget widget-banner">
                            <div class="item-img">
                                <img src="img/figure/widget-banner.png" alt="banner">
                            </div>
                            <div class="item-content">
                                <h2 class="item-title"><span>Professional</span> Care</h2>
                                <div class="item-subtitle">Transparent Quotes in GHS</div>
                                <a href="calculate-form.html" class="fw-btn-fill bg-accent text-primarytext">Get a Free Quote</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Single Service Area End Here -->"""

    html = re.sub(
        r'<!-- Faq Area Start Here -->.*?<!-- Single Service Area End Here -->',
        faq_section,
        html,
        flags=re.DOTALL
    )

    with open("faq.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix faq.html!")

build_faq()


# ==============================================================================
# 12. CONTACT US: contact.html
# ==============================================================================
def build_contact():
    html = get_orig("contact.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Contact Us | EcoCare Cleaning Services Limited",
        description="Get in touch with EcoCare in Achimota Mile 7, Accra. Telephone: +233 24 901 4253 / +233 24 380 7100. Email: ecocaregh1on1@gmail.com."
    )
    html = replace_header_and_footer(html, active_nav="contact")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Contact Us</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Contact</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    contact_section = f"""        <!-- Contact Us Area Start Here -->
        <section class="section-padding-12-10">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="contact-box-layout1">
                            <div class="google-map-area">
                                <iframe src="{MAP_IFRAME_SRC}" width="100%" height="420" style="border:0; border-radius: 4px;" allowfullscreen="" loading="lazy"></iframe>
                            </div>
                            <div class="contact-info">
                                <div class="media media-none-lg media-none--sm">
                                    <div class="item-icon">
                                        <i class="flaticon-call-answer"></i>
                                    </div>
                                    <div class="media-body space-md">
                                        <h4>Phone:</h4>
                                        <ul>
                                            <li><a href="tel:{PHONE_TEL_PRIMARY}">{PHONE_PRIMARY}</a>,</li>
                                            <li><a href="tel:{PHONE_TEL_SECONDARY}">{PHONE_SECONDARY}</a></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="media media-none-lg media-none--sm">
                                    <div class="item-icon">
                                        <i class="flaticon-message"></i>
                                    </div>
                                    <div class="media-body space-md">
                                        <h4>E-mail:</h4>
                                        <ul>
                                            <li><a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a></li>
                                            <li><span>{HOURS_TEXT}</span></li>
                                        </ul>
                                    </div>
                                </div>
                                <div class="media media-none-lg media-none--sm">
                                    <div class="item-icon">
                                        <i class="flaticon-maps-and-flags"></i>
                                    </div>
                                    <div class="media-body space-md">
                                        <h4>Location:</h4>
                                        <ul>
                                            <li>{OFFICE_ADDRESS}</li>
                                            <li>Greater Accra Region, Ghana</li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 sidebar-break-md sidebar-widget-area">
                        <div class="widget widget-contact-form">
                            <div class="heading-layout4">
                                <h4>Send Us a Message</h4>
                            </div>
                            <form class="contact-form-box" id="contact-form">
                                <div class="row">
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-user"></i></div>
                                        <input type="text" placeholder="Your Name" class="form-control" name="name" data-error="Name field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-envelope"></i></div>
                                        <input type="email" placeholder="E-mail Address" class="form-control" name="email" data-error="email field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-phone-volume"></i></div>
                                        <input type="text" placeholder="Phone Number" class="form-control" name="phone" data-error="Phone field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-question"></i></div>
                                        <input type="text" placeholder="Subject" class="form-control" name="subject" data-error="Subject field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-comments"></i></div>
                                        <textarea placeholder="Message / Service Details" class="textarea form-control" name="message" id="form-message" rows="4" cols="20" 
                                        data-error="Message field is required" required></textarea>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <button type="submit" class="fw-btn-fill bg-accent text-primarytext">Send Message</button>
                                    </div>
                                </div>
                                <div class="form-response"></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Contact Us Area End Here -->"""

    html = re.sub(
        r'<!-- Contact Us Area Start Here -->.*?<!-- Blog Area End Here -->',
        contact_section,
        html,
        flags=re.DOTALL
    )

    # Remove Google Maps script since we use the iframe embed
    html = re.sub(r'<script src="https://maps\.googleapis\.com/maps/api/js[^"]*"></script>\s*', '', html)

    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix contact.html!")

build_contact()


# ==============================================================================
# 13. PROJECTS / SERVICE SHOWCASE: project1.html
# ==============================================================================
def build_project1():
    html = get_orig("project1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Our Work & Service Showcase | EcoCare Ghana",
        description="Explore EcoCare's field execution portfolio across residential deep cleaning, commercial facilities, carpet extraction, upholstery care, and fumigation in Accra."
    )
    html = replace_header_and_footer(html, active_nav="projects")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Our Service Showcase</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Projects &amp; Gallery</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    projects_area = """        <!-- Projects Area Start Here -->
        <section class="section-padding-md-3">
            <div class="container">
                <div class="heading-layout2">
                    <h2>Proven Cleaning Excellence<span>Our Recent Field Work</span></h2>
                </div>
                <div class="row">
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project1.jpg" alt="Residential Deep Scrubbing">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">Residential Move-In Scrub</a></h3>
                                <div class="item-tag">
                                    <a href="single-service1.html">Residential,</a>
                                    <a href="calculate-form.html">Deep Clean</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project2.jpg" alt="Commercial Corporate Janitorial">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">Corporate Office Janitorial</a></h3>
                                <div class="item-tag">
                                    <a href="single-service1.html">Commercial,</a>
                                    <a href="contact.html">Office Facility</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project3.jpg" alt="Wall-to-Wall Carpet Deep Extraction">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">Carpet Deep Steam Extraction</a></h3>
                                <div class="item-tag">
                                    <a href="carpet-cleaning.html">Carpet Care,</a>
                                    <a href="carpet-cleaning.html">Restoration</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project4.jpg" alt="Executive Leather & Fabric Upholstery">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">Leather &amp; Fabric Couch Care</a></h3>
                                <div class="item-tag">
                                    <a href="upholstery-cleaning.html">Upholstery,</a>
                                    <a href="upholstery-cleaning.html">Furniture</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project5.jpg" alt="Post-Construction Clean">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">Post-Construction Detailing</a></h3>
                                <div class="item-tag">
                                    <a href="single-service1.html">Post-Build,</a>
                                    <a href="calculate-form.html">Handover</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 col-md-6">
                        <div class="project-box-layout1">
                            <div class="item-img">
                                <img src="img/project/project6.jpg" alt="EcoFumes Integrated Fumigation">
                                <a href="single-project1.html" class="hover-dot">
                                    <span></span>
                                    <span></span>
                                    <span></span>
                                </a>
                            </div>
                            <div class="item-content">
                                <h3 class="item-title"><a href="single-project1.html">EcoFumes Integrated Fumigation</a></h3>
                                <div class="item-tag">
                                    <a href="pest-control.html">Pest Control,</a>
                                    <a href="pest-control.html">Fumigation</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 text-center mt-4">
                        <p class="text-muted"><i class="fas fa-info-circle mr-1"></i> Showcase items illustrate EcoCare service categories and field execution techniques across Greater Accra.</p>
                    </div>
                </div>
            </div>
        </section>
        <!-- Projects Area End Here -->"""

    html = re.sub(
        r'<!-- Projects Area Start Here -->.*?<!-- Projects Area End Here -->',
        projects_area,
        html,
        flags=re.DOTALL
    )

    with open("project1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix project1.html!")

build_project1()


# ==============================================================================
# 14. SINGLE PROJECT / CASE STUDY: single-project1.html
# ==============================================================================
def build_single_project1():
    html = get_orig("single-project1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Commercial Facility Deep Cleaning Case Study | EcoCare Ghana",
        description="Case study: Multi-story corporate workspace deep cleaning, carpet steam extraction, and restroom sanitization in Accra."
    )
    html = replace_header_and_footer(html, active_nav="projects")

    # Breadcrumbs
    crumb = """<div class="breadcrumbs-area">
                            <h1>Corporate Workspace Deep Cleaning</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>
                                    <a href="project1.html">Projects</a>
                                </li>
                                <li>Case Study</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    single_proj_section = """        <!-- Single Project Area Start Here -->
        <section class="section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="single-project-box-layout1">
                            <div class="single-project-slider">
                                <div class="rc-carousel" data-loop="true" data-items="1" data-margin="30"
                                    data-autoplay="true" data-autoplay-timeout="5000" data-smart-speed="1000"
                                    data-dots="false" data-nav="true" data-nav-speed="false" data-r-x-extra="1"
                                    data-r-x-extra-nav="true" data-r-x-extra-dots="false" data-r-x="1"
                                    data-r-x-nav="true" data-r-x-dots="false" data-r-sm="1"
                                    data-r-sm-nav="true" data-r-sm-dots="false" data-r-md="1"
                                    data-r-md-nav="true" data-r-md-dots="false" data-r-lg="1"
                                    data-r-lg-nav="true" data-r-lg-dots="false">
                                    <div class="item-img">
                                        <img src="img/project/project7.jpg" alt="Corporate Cleaning Slide 1">
                                    </div>
                                    <div class="item-img">
                                        <img src="img/project/project8.jpg" alt="Corporate Cleaning Slide 2">
                                    </div>
                                </div>
                            </div>
                            <div class="single-project-info">
                                <h3 class="item-title">Project Overview</h3>
                                <p>EcoCare was engaged to execute a comprehensive deep clean, high-filtration carpet extraction, and hygienic restroom descaling for a multi-story corporate commercial facility in Accra prior to executive compliance auditing. The facility operates daily with high foot traffic, executive meeting rooms, and dense workstation areas requiring spotless presentation.</p>
                                <p>Our operations team mobilized specialized industrial cleaning equipment, low-moisture carpet extractors, and plant-derived hospital-grade disinfectants to thoroughly transform the facility overnight without disrupting normal working hours.</p>
                                <h3 class="item-title">Key Challenges</h3>
                                <p>The project presented three distinct operational constraints:</p>
                                <ul>
                                    <li><strong>Strict Overnight Window:</strong> All work had to be completed within a 12-hour turnaround between 7:00 PM and 7:00 AM before corporate staff arrived.</li>
                                    <li><strong>Zero Chemical Odors:</strong> Eco-friendly, low-VOC detergents were required to avoid respiratory irritation for occupants the next morning.</li>
                                    <li><strong>Rapid Carpet Drying:</strong> Wall-to-wall fitted carpeting across conference suites needed to be completely dry and walk-ready by 7:30 AM.</li>
                                </ul>
                                <h3 class="item-title">EcoCare Solution &amp; Results</h3>
                                <p>We deployed a dedicated team of supervised cleaning specialists equipped with high-velocity air movers and low-moisture encapsulation extractors. Restrooms underwent deep mineral descaling and sanitary fogging. High-touch touchpoints—including door hardware, banisters, and elevator controls—were sanitized with food-safe disinfectants.</p>
                                <p>A final 50-point walkthrough inspection was conducted with the client facility manager at 6:45 AM, resulting in 100% sign-off approval and successful audit certification.</p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 sidebar-break-md sidebar-widget-area">
                        <div class="widget widget-project-info">
                            <div class="heading-layout4">
                                <h3>Project Information</h3>
                            </div>
                            <div class="project-info-list">
                                <ul>
                                    <li>
                                        <div class="item-icon"><i class="fas fa-user"></i></div>
                                        <div class="item-content">
                                            <h4>Client:</h4>
                                            <div>Corporate Financial Institution</div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="item-icon"><i class="fas fa-tags"></i></div>
                                        <div class="item-content">
                                            <h4>Service:</h4>
                                            <div>Commercial Janitorial &amp; Carpet Deep Extraction</div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="item-icon"><i class="fas fa-layer-group"></i></div>
                                        <div class="item-content">
                                            <h4>Category:</h4>
                                            <div>Commercial Facility Maintenance</div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="item-icon"><i class="far fa-clock"></i></div>
                                        <div class="item-content">
                                            <h4>Turnaround:</h4>
                                            <div>12-Hour Overnight Deployment</div>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="item-icon"><i class="fas fa-map-marker-alt"></i></div>
                                        <div class="item-content">
                                            <h4>Location:</h4>
                                            <div>Ridge / Airport Hub, Accra, Ghana</div>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="widget widget-banner">
                            <div class="item-img">
                                <img src="img/figure/widget-banner.png" alt="banner">
                            </div>
                            <div class="item-content">
                                <h2 class="item-title"><span>Need Corporate</span> Care?</h2>
                                <div class="item-subtitle">Custom Facility Assessment</div>
                                <a href="contact.html?plan=corporate" class="fw-btn-fill bg-accent text-primarytext">Contact Us Today</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Single Project Area End Here -->"""

    html = re.sub(
        r'<!-- Single Service Area Start Here -->.*?<!-- Single Service Area End Here -->',
        single_proj_section,
        html,
        flags=re.DOTALL
    )

    with open("single-project1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix single-project1.html!")

build_single_project1()


# ==============================================================================
# 15. COMING SOON: coming-soon.html
# ==============================================================================
def build_coming_soon():
    html = get_orig("coming-soon.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Coming Soon | EcoCare Cleaning Services Limited",
        description="EcoCare Cleaning Services Limited is expanding exciting new service divisions in Accra, Ghana."
    )
    # Replace logo with authentic EcoCare logo
    html = html.replace('src="img/large-logo.png"', 'src="img/large-logo.png"')
    # Replace social links
    social_block = f"""                                    <div class="comingsoon-social">
                                        <ul>
                                            <li><a href="{FB_URL}" target="_blank" rel="noopener noreferrer" aria-label="Facebook"><i class="fab fa-facebook-f"></i></a></li>
                                            <li><a href="{TIKTOK_URL}" target="_blank" rel="noopener noreferrer" aria-label="TikTok"><i class="fab fa-tiktok"></i></a></li>
                                            <li><a href="{YOUTUBE_URL}" target="_blank" rel="noopener noreferrer" aria-label="YouTube"><i class="fab fa-youtube"></i></a></li>
                                        </ul>
                                    </div>"""
    html = re.sub(r'<div class="comingsoon-social">.*?</div>', social_block, html, flags=re.DOTALL)

    # Copyright and Contact
    copy_block = f"""                                    <div class="comingsoon-copy-right">
                                        <p>&copy; 2026 EcoCare Cleaning Services Limited. All Rights Reserved.</p>
                                        <p style="margin-top: 8px; color: #fff; font-size: 14px;"><i class="fas fa-map-marker-alt" style="color: #6bb92d;"></i> {OFFICE_ADDRESS} &nbsp;|&nbsp; <i class="fas fa-phone" style="color: #6bb92d;"></i> <a href="tel:{PHONE_TEL_PRIMARY}" style="color: #fff;">{PHONE_PRIMARY}</a> &nbsp;|&nbsp; <i class="fas fa-envelope" style="color: #6bb92d;"></i> <a href="mailto:{EMAIL_PRIMARY}" style="color: #fff;">{EMAIL_PRIMARY}</a></p>
                                    </div>"""
    html = re.sub(r'<div class="comingsoon-copy-right">.*?</div>', copy_block, html, flags=re.DOTALL)

    with open("coming-soon.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix coming-soon.html!")

build_coming_soon()


# ==============================================================================
# 16. 404 ERROR PAGE: 404.html
# ==============================================================================
def build_404():
    html = get_orig("404.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Page Not Found (404) | EcoCare Cleaning Services Limited",
        description="The page you are looking for could not be found. Return to EcoCare Cleaning Services Limited homepage."
    )
    html = replace_header_and_footer(html, active_nav="")

    # Fix Go Home link
    html = html.replace('<a href="#" class="item-btn">GO HOME PAGE</a>', '<a href="index.html" class="item-btn">RETURN TO HOME PAGE</a>')

    with open("404.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix 404.html!")

build_404()


# ==============================================================================
# 17. PRIVACY POLICY: privacy-policy.html
# ==============================================================================
def build_privacy_policy():
    html = get_orig("about1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Privacy Policy | EcoCare Cleaning Services Limited",
        description="Privacy policy and data handling principles for EcoCare Cleaning Services Limited, operating in Accra, Ghana."
    )
    html = replace_header_and_footer(html, active_nav="")

    crumb = """<div class="breadcrumbs-area">
                            <h1>Privacy Policy</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Privacy Policy</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    content = f"""        <!-- Privacy Policy Content Area Start Here -->
        <section class="section-padding-12-9">
            <div class="container">
                <div class="row">
                    <div class="col-lg-10 mx-auto">
                        <div class="alert alert-info ecocare-draft-notice" style="background:#f4fbf1; border-left:4px solid #6bb92d; padding:15px; margin-bottom:30px;">
                            <i class="fas fa-info-circle mr-2 text-success"></i> <strong>Draft Policy Notice:</strong> This document reflects standard operational data handling practices for EcoCare Cleaning Services Limited under Ghana's Data Protection Act, 2012 (Act 843). Formal legal ratification is pending.
                        </div>
                        <div class="about-box-layout1">
                            <h2 class="item-title">Our Commitment to Your Privacy</h2>
                            <p>EcoCare Cleaning Services Limited ("EcoCare", "we", "us", or "our") respects the privacy of our residential and commercial clients across Greater Accra. This Privacy Policy outlines what information we collect when you use our website, request a service quote, or engage our cleaning teams.</p>
                            
                            <h3 class="mt-4">1. Information We Collect</h3>
                            <p>To provide accurate estimates and dispatch service teams, we collect:</p>
                            <ul>
                                <li><strong>Contact Details:</strong> Your full name, telephone number(s), and email address.</li>
                                <li><strong>Property &amp; Location Information:</strong> Physical premises address, neighborhood/landmark in Accra, property type, room count, and approximate square footage.</li>
                                <li><strong>Service Preferences:</strong> Cleaning frequencies, specific stain or pest concerns, and preferred appointment dates.</li>
                            </ul>

                            <h3 class="mt-4">2. How We Use Your Information</h3>
                            <p>We process collected details strictly for legitimate operational purposes:</p>
                            <ul>
                                <li>Generating transparent quotations and scope-of-work agreements in Ghanaian Cedis (GHS).</li>
                                <li>Dispatching vetted field crews and supervisors to your property.</li>
                                <li>Communicating service confirmations, reminders, or arrival notices via telephone, SMS, or WhatsApp.</li>
                                <li>Following up after service completion for quality assurance and customer feedback.</li>
                            </ul>

                            <h3 class="mt-4">3. Data Retention &amp; Sharing</h3>
                            <p>We do not sell, rent, or trade your personal information to third parties. Customer contact records are stored securely and accessed only by authorized administrative and dispatch staff. We retain quote records only as long as necessary to fulfill service agreements or comply with statutory accounting requirements in Ghana.</p>

                            <h3 class="mt-4">4. Contact Our Data Representative</h3>
                            <p>If you have questions regarding your data or wish to update or delete your contact records, please contact us:</p>
                            <ul>
                                <li><strong>Email:</strong> <a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a></li>
                                <li><strong>Phone:</strong> <a href="tel:{PHONE_TEL_PRIMARY}">{PHONE_PRIMARY}</a></li>
                                <li><strong>Office:</strong> {OFFICE_ADDRESS}</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Privacy Policy Content Area End Here -->"""

    html = re.sub(
        r'<!-- About Us Area Start Here -->.*?<!-- Call To Action Area End Here -->',
        content,
        html,
        flags=re.DOTALL
    )

    with open("privacy-policy.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix privacy-policy.html!")

build_privacy_policy()


# ==============================================================================
# 18. TERMS & CONDITIONS: terms-condition.html
# ==============================================================================
def build_terms_condition():
    html = get_orig("about1.html")
    html = clean_common_artifacts(html)
    html = replace_page_title(
        html,
        title="Terms & Conditions | EcoCare Cleaning Services Limited",
        description="Terms of service and operational agreements for EcoCare Cleaning Services Limited in Accra, Ghana."
    )
    html = replace_header_and_footer(html, active_nav="")

    crumb = """<div class="breadcrumbs-area">
                            <h1>Terms &amp; Conditions</h1>
                            <ul>
                                <li>
                                    <a href="index.html">Home</a>
                                </li>
                                <li>Terms &amp; Conditions</li>
                            </ul>
                        </div>"""
    html = re.sub(r'<div class="breadcrumbs-area">.*?</div>', crumb, html, flags=re.DOTALL)

    content = f"""        <!-- Terms Content Area Start Here -->
        <section class="section-padding-12-9">
            <div class="container">
                <div class="row">
                    <div class="col-lg-10 mx-auto">
                        <div class="alert alert-info ecocare-draft-notice" style="background:#f4fbf1; border-left:4px solid #6bb92d; padding:15px; margin-bottom:30px;">
                            <i class="fas fa-info-circle mr-2 text-success"></i> <strong>Draft Terms Notice:</strong> These operational terms govern cleaning, laundry, carpet extraction, upholstery care, and fumigation bookings with EcoCare Cleaning Services Limited. Formal legal review is pending.
                        </div>
                        <div class="about-box-layout1">
                            <h2 class="item-title">Terms of Service &amp; Operational Standards</h2>
                            <p>By booking a service appointment or requesting a quotation from EcoCare Cleaning Services Limited, you agree to the following operational terms and conditions:</p>

                            <h3 class="mt-4">1. Quotations, Pricing &amp; Scope Confirmation</h3>
                            <p>All quotes provided via phone, WhatsApp, or our online calculator are preliminary estimates based on client-provided details. Final pricing in Ghanaian Cedis (GHS) is confirmed upon initial on-site walkthrough inspection. Any additional areas or heavy staining identified on-site will be discussed with you before commencing additional work.</p>

                            <h3 class="mt-4">2. Access, Utilities &amp; Safety</h3>
                            <p>Clients agree to provide safe access to the premises at the agreed appointment time, including functional running water and electrical power outlets necessary to operate our commercial extraction and scrubbing equipment. For fumigation (EcoFumes), occupants and pets must vacate the treated premises for the prescribed 2 to 4-hour window.</p>

                            <h3 class="mt-4">3. Quality Walkthrough &amp; Satisfaction Guarantee</h3>
                            <p>At the conclusion of every cleaning service, our crew supervisor invites you or your designated representative to perform a joint walkthrough inspection. Any areas requiring touch-up are addressed immediately on-site prior to supervisor sign-off.</p>

                            <h3 class="mt-4">4. Rescheduling &amp; Cancellations</h3>
                            <p>We understand that unexpected schedule changes happen. Please notify us at least 24 hours in advance if you need to reschedule or postpone your booking so we can reassign field teams without disruption.</p>

                            <h3 class="mt-4">5. Contact Information</h3>
                            <p>For questions regarding our service agreements or to discuss corporate commercial contracts, contact us at <a href="tel:{PHONE_TEL_PRIMARY}">{PHONE_PRIMARY}</a> or <a href="mailto:{EMAIL_PRIMARY}">{EMAIL_PRIMARY}</a>.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Terms Content Area End Here -->"""

    html = re.sub(
        r'<!-- About Us Area Start Here -->.*?<!-- Call To Action Area End Here -->',
        content,
        html,
        flags=re.DOTALL
    )

    with open("terms-condition.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("-> Successfully restored native Clenix terms-condition.html!")

build_terms_condition()


# ==============================================================================
# 19. DEMO PAGES SANITIZATION (13 Pages)
# ==============================================================================
def sanitize_demo_pages():
    demo_files = [
        "index2.html", "index3.html", "index4.html",
        "about2.html", "service2.html",
        "shop.html", "single-product.html",
        "blog1.html", "blog2.html", "single-blog1.html",
        "team1.html", "team2.html", "single-team.html"
    ]

    for fname in demo_files:
        try:
            html = get_orig(fname)
            html = clean_common_artifacts(html)
            # Add noindex to demo pages
            if 'name="robots"' not in html:
                html = html.replace(
                    '<meta name="viewport"',
                    '<meta name="robots" content="noindex, follow">\n    <meta name="viewport"'
                )
            # Patch title
            page_name = fname.replace(".html", "").replace("-", " ").title()
            html = re.sub(r'<title>.*?</title>', f'<title>EcoCare &mdash; {page_name} (Theme Demo)</title>', html)
            # Patch copyright
            html = re.sub(r'Copyright @? \d{4} clenix\. All Rights Reserved\.', '&copy; 2026 EcoCare Cleaning Services Limited. Clenix Theme Template Demo.', html)
            # Patch header logo
            html = html.replace('src="img/logo-dark.png"', 'src="img/logo-dark.png"')

            with open(fname, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"-> Sanitized demo reference page: {fname}")
        except Exception as e:
            print(f"-> Error sanitizing {fname}: {e}")

sanitize_demo_pages()
print("All canonical and demo pages restored and sanitized!")
