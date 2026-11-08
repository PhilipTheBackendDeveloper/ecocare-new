#!/usr/bin/env python3
"""
Appends the remaining native Clenix page builders and demo sanitization to scripts/restore_clenix_native.py
"""

ADDITIONS = r'''

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
'''

with open('scripts/restore_clenix_native.py', 'a', encoding='utf-8') as f:
    f.write(ADDITIONS)

print("Additions appended successfully!")
