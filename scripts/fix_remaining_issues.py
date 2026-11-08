#!/usr/bin/env python3
"""
Surgically fixes the remaining issues identified by QA check:
1. faq.html: Replaces native FAQ accordion and banner widget using exact comment tags.
2. single-project1.html: Replaces single project layout and widgets using exact comment tags.
3. index.html: Replaces demo CTA banner with EcoCare estimate link.
4. about1.html: Replaces bare href="#" with proper internal links.
5. Demo pages: Robustly sanitizes copyright, agency designation, and email references.
"""

import re
import subprocess
from restore_clenix_native import (
    get_orig,
    clean_common_artifacts,
    replace_header_and_footer,
    replace_page_title,
    FB_URL, TIKTOK_URL, YOUTUBE_URL,
    PHONE_PRIMARY, PHONE_TEL_PRIMARY, PHONE_SECONDARY, PHONE_TEL_SECONDARY,
    EMAIL_PRIMARY, OFFICE_ADDRESS, HOURS_TEXT, MAP_IFRAME_SRC
)

def fix_faq():
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

    faq_section = f"""        <!-- Single Service Area Start Here -->
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
        r'<!-- Single Service Area Start Here -->.*?<!-- Single Service Area End Here -->',
        faq_section,
        html,
        flags=re.DOTALL
    )

    with open("faq.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Fixed native Clenix faq.html!")


def fix_single_project1():
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

    single_proj_section = """        <!-- Single Projects Area Start Here -->
        <section class="section-padding-12">
            <div class="container">
                <div class="row">
                    <div class="col-lg-8">
                        <div class="single-project-box-layout1">
                            <div class="single-project-slider">
                                <div class="rc-carousel nav-control-layout2" data-loop="true" data-items="10" data-margin="10"
                                    data-autoplay="false" data-autoplay-timeout="3000" data-smart-speed="1000" data-dots="false"
                                    data-nav="true" data-nav-speed="false" data-r-x-small="1" data-r-x-small-nav="true"
                                    data-r-x-small-dots="false" data-r-x-medium="1" data-r-x-medium-nav="true" data-r-x-medium-dots="false"
                                    data-r-small="1" data-r-small-nav="true" data-r-small-dots="false" data-r-medium="1"
                                    data-r-medium-nav="true" data-r-medium-dots="false" data-r-large="1" data-r-large-nav="true"
                                    data-r-large-dots="false" data-r-extra-large="1" data-r-extra-large-nav="true"
                                    data-r-extra-large-dots="false">
                                    <div class="slide-item">
                                        <img src="img/project/project7.jpg" alt="Corporate Cleaning Slide 1">
                                    </div>
                                    <div class="slide-item">
                                        <img src="img/project/project8.jpg" alt="Corporate Cleaning Slide 2">
                                    </div>
                                </div>
                            </div>
                            <div class="single-project-info">
                                <div class="item-content">
                                    <h3 class="item-title">Project Overview</h3>
                                    <p>EcoCare was engaged to execute a comprehensive deep clean, high-filtration carpet extraction, and hygienic restroom descaling for a multi-story corporate commercial facility in Accra prior to executive compliance auditing. The facility operates daily with high foot traffic, executive meeting rooms, and dense workstation areas requiring spotless presentation.</p>
                                    <p>Our operations team mobilized specialized industrial cleaning equipment, low-moisture carpet extractors, and plant-derived hospital-grade disinfectants to thoroughly transform the facility overnight without disrupting normal working hours.</p>
                                </div>
                                <div class="item-content">
                                    <h3 class="item-title">Key Challenges</h3>
                                    <p>The engagement presented three critical operational requirements:</p>
                                    <ul class="list-item">
                                        <li><i class="fas fa-check"></i><strong>Strict Overnight Window:</strong> All work completed within 12 hours (7:00 PM - 7:00 AM) before morning staff arrival.</li>
                                        <li><i class="fas fa-check"></i><strong>Zero Odor Impact:</strong> Eco-friendly, low-VOC detergents to avoid respiratory sensitivity among corporate staff.</li>
                                        <li><i class="fas fa-check"></i><strong>Rapid Drying:</strong> Wall-to-wall fitted carpeting across conference suites dry and walk-ready by 7:30 AM.</li>
                                    </ul>
                                </div>
                                <div class="item-content">
                                    <h3 class="item-title">Solutions &amp; Execution</h3>
                                    <p>EcoCare deployed a supervised multi-specialist crew equipped with industrial extraction units and high-velocity air movers:</p>
                                    <ul class="list-item">
                                        <li><i class="fas fa-check"></i>Deep hot-water &amp; encapsulation carpet restoration across 450 sqm of office floor space.</li>
                                        <li><i class="fas fa-check"></i>Sanitary washroom descaling and antibacterial fogging.</li>
                                        <li><i class="fas fa-check"></i>High-touch surface disinfection across workstations, glass partitions &amp; elevators.</li>
                                        <li><i class="fas fa-check"></i>Pre-opening 50-point walkthrough inspection with the client facility manager at 6:45 AM.</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-4 sidebar-break-md sidebar-widget-area">
                        <div class="widget widget-project-info">
                            <div class="heading-layout4">
                                <h3>Project Information</h3>
                            </div>
                            <div class="project-details">
                                <p>Commercial workspace deep sanitization and carpet restoration in Accra.</p>
                                <ul>
                                    <li><span>Category</span>Commercial Janitorial</li>
                                    <li><span>Client</span>Corporate Institution</li>
                                    <li><span>Location</span>Ridge / Airport Hub, Accra</li>
                                    <li><span>Turnaround</span>12-Hour Overnight</li>
                                    <li><span>Status</span>Completed &amp; Certified</li>
                                    <li><span>Rating</span> 
                                        <ul class="item-rating">
                                            <li><i class="fas fa-star"></i></li>
                                            <li><i class="fas fa-star"></i></li>
                                            <li><i class="fas fa-star"></i></li>
                                            <li><i class="fas fa-star"></i></li>
                                            <li><i class="fas fa-star"></i></li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                        <div class="widget widget-recent-post">
                            <div class="heading-layout4">
                                <h4>Service Focus</h4>
                            </div>
                            <ul class="recent-post-list">
                                <li>
                                    <div class="post-date"><i class="far fa-clock"></i> EcoClean Janitorial</div>
                                    <h6 class="item-title"><a href="single-service1.html">Commercial &amp; Residential Care</a></h6>
                                </li>
                                <li>
                                    <div class="post-date"><i class="far fa-clock"></i> Eco-Laundry</div>
                                    <h6 class="item-title"><a href="single-service2.html">Doorstep Laundry &amp; Dry Cleaning</a></h6>
                                </li>
                                <li>
                                    <div class="post-date"><i class="far fa-clock"></i> EcoFumes</div>
                                    <h6 class="item-title"><a href="pest-control.html">Pest Control &amp; Safe Fumigation</a></h6>
                                </li>
                            </ul>
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
        <!-- Single Projects Area End Here -->"""

    html = re.sub(
        r'<!-- Single Projects Area Start Here -->.*?<!-- Single Projects Area End Here -->',
        single_proj_section,
        html,
        flags=re.DOTALL
    )

    with open("single-project1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Fixed native Clenix single-project1.html!")


def fix_index_banner():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Replace the banner Together We'll Explore New Things
    old_banner = r"""        <!-- Banner Area Start Here -->
        <section class="banner-wrap-layout1" data-bg-image="img/figure/banner-bg.jpg">
            <div class="container">
                <div class="row d-flex justify-content-end">
                    <div class="col-xl-6 col-12">
                        <div class="banner-box-layout1">
                            <h2 class="item-title">Together <span>We'll Explore</span> New Things</h2>
                            <a href="#" class="btn-fill-md btn-slide-hover bg-accent text-primarytext">Read More<i class="fas fa-angle-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Banner Area End Here -->"""

    new_banner = """        <!-- Banner Area Start Here -->
        <section class="banner-wrap-layout1" data-bg-image="img/figure/banner-bg.jpg">
            <div class="container">
                <div class="row d-flex justify-content-end">
                    <div class="col-xl-6 col-12">
                        <div class="banner-box-layout1">
                            <h2 class="item-title">Dedicated to <span>Hygienic, Eco-Friendly</span> Living</h2>
                            <a href="calculate-form.html" class="btn-fill-md btn-slide-hover bg-accent text-primarytext">Get an Estimate<i class="fas fa-angle-right"></i></a>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Banner Area End Here -->"""

    html = html.replace(old_banner, new_banner)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Fixed index.html CTA banner link!")


def fix_about1_links():
    with open("about1.html", "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace(
        '<a href="#" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Read More<i class="fas fa-angle-right"></i></a>',
        '<a href="service1.html" class="btn-fill-md bg-accent btn-slide-hover text-primarytext">Explore Services<i class="fas fa-angle-right"></i></a>'
    )
    html = html.replace(
        '<a href="#" class="btn-fill-md btn-slide-hover bg-accent text-primarytext">Get an Estimate<i class="fas fa-angle-right"></i></a>',
        '<a href="calculate-form.html" class="btn-fill-md btn-slide-hover bg-accent text-primarytext">Get an Estimate<i class="fas fa-angle-right"></i></a>'
    )
    with open("about1.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Fixed about1.html buttons!")


def fix_demo_pages_sanitization():
    demo_files = [
        "index2.html", "index3.html", "index4.html",
        "about2.html", "service2.html",
        "shop.html", "single-product.html",
        "blog1.html", "blog2.html", "single-blog1.html",
        "team1.html", "team2.html", "single-team.html"
    ]

    for fname in demo_files:
        with open(fname, "r", encoding="utf-8") as f:
            html = f.read()

        # Robust copyright replacement
        html = re.sub(
            r'Copyright\s+(?:@\s+)?\d{4}\s+clenix\.?\s+All Rights Reserved\.?',
            '&copy; 2026 EcoCare Cleaning Services Limited. Clenix Theme Template Demo.',
            html,
            flags=re.IGNORECASE
        )
        html = html.replace("Copyright 2019 clenix. All Rights Reserved.", "&copy; 2026 EcoCare Cleaning Services Limited. Clenix Theme Template Demo.")

        # Specific demo brands
        if fname == "index4.html":
            html = html.replace("Ceo, Clenix Agency", "Director, EcoCare")
            html = html.replace("Clenix Agency", "EcoCare")
        if fname == "single-team.html":
            html = html.replace("info@clenix.com", "ecocaregh1on1@gmail.com")

        # Strip any other stray clenix / radiustheme from copyright
        html = re.sub(r'clenix', 'EcoCare', html, flags=re.IGNORECASE)
        html = re.sub(r'RadiusTheme', 'EcoCare', html, flags=re.IGNORECASE)

        with open(fname, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✓ Sanitized demo page {fname}")

if __name__ == "__main__":
    fix_faq()
    fix_single_project1()
    fix_index_banner()
    fix_about1_links()
    fix_demo_pages_sanitization()
    print("All fixes applied successfully!")
