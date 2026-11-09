#!/usr/bin/env python3
"""
EcoCare Cleaning Services Limited — Comprehensive Audit Remediation
1. Fixes calculate-form.html: slots the authentic estimate calculator with all Select2 fields and honeypot.
2. Fixes contact.html: slots the clean contact form with correct field names (subject, not phone) and honeypot.
3. Fixes pest-control.html: adds mandatory EPA-compliant Safety Advisory and tempers applicator claims.
4. Updates index.html: adds transparent testimonial archive disclosure banner under carousel.
5. Injects honeypot spam protection across sidebar forms in service and FAQ pages.
"""

import re
import os

# Verified Constants
PHONE_PRIMARY = "+233 24 901 4253"
PHONE_SECONDARY = "+233 24 380 7100"
PHONE_TEL_PRIMARY = "+233249014253"
PHONE_TEL_SECONDARY = "+233243807100"
EMAIL_PRIMARY = "ecocaregh1on1@gmail.com"
OFFICE_ADDRESS = "Achimota Mile 7, Accra, Ghana"
HOURS_TEXT = "Mon - Sat: 07:00am - 06:00pm"
MAP_IFRAME_SRC = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3970.5870075801395!2d-0.24410990324261828!3d5.627819178441937!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xfdf995df95740cb%3A0xbbcb29ede8158fa1!2sEcoCare%20Laundry!5e0!3m2!1sen!2sgh!4v1735185870106!5m2!1sen!2sgh"


def fix_calculate_form():
    with open("calculate-form.html", "r", encoding="utf-8") as f:
        html = f.read()

    calc_area = """        <!-- Booking Form Area Start Here -->
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
                                        <h3>Biodegradable &amp; Regulated Formulations</h3>
                                        <p>We use eco-conscious, plant-derived detergents and regulated pest-control formulations safe for families, pets, and workplace teams.</p>
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
                                <div style="display:none !important;" aria-hidden="true">
                                    <input type="text" name="website_url" tabindex="-1" autocomplete="off" value="">
                                </div>
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
                                        <input type="email" placeholder="E-mail Address (optional)" class="form-control" name="email" id="form-email">
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
                                <div class="form-response mt-3"></div>
                            </form>
                            <div class="text-center mt-3">
                                <small class="text-muted"><i class="fab fa-whatsapp text-success mr-1"></i> Prefer instant chat? WhatsApp us at <a href="https://wa.me/233249014253" class="text-primary font-weight-bold" target="_blank">+233 24 901 4253</a></small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Booking Form Area End Here -->"""

    html = re.sub(
        r'<!-- Booking Form Area Start Here -->.*?<!-- Booking Form Area End Here -->',
        calc_area,
        html,
        flags=re.DOTALL
    )

    with open("calculate-form.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Remediated calculate-form.html: Slotting complete quote calculator with Select2, honeypot & validation.")


def fix_contact_page():
    with open("contact.html", "r", encoding="utf-8") as f:
        html = f.read()

    contact_section = f"""        <!-- Blog Area Start Here -->
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
                                <div style="display:none !important;" aria-hidden="true">
                                    <input type="text" name="website_url" tabindex="-1" autocomplete="off" value="">
                                </div>
                                <div class="row">
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-user"></i></div>
                                        <input type="text" placeholder="Your Name" class="form-control" name="name" data-error="Name field is required" required>
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="far fa-envelope"></i></div>
                                        <input type="email" placeholder="E-mail Address (optional)" class="form-control" name="email">
                                        <div class="help-block with-errors"></div>
                                    </div>
                                    <div class="col-12 form-group">
                                        <div class="form-icon"><i class="fas fa-phone-volume"></i></div>
                                        <input type="tel" placeholder="Phone Number" class="form-control" name="phone" data-error="Phone field is required" required>
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
                                <div class="form-response mt-3"></div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        <!-- Blog Area End Here -->"""

    html = re.sub(
        r'<!-- Blog Area Start Here -->.*?<!-- Blog Area End Here -->',
        contact_section,
        html,
        flags=re.DOTALL
    )

    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Remediated contact.html: Correct field names, phone validation, honeypot & Google Map embed.")


def fix_pest_control_safety():
    with open("pest-control.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update technician wording from "licensed" to trained EPA guideline applicators
    html = html.replace(
        "Our licensed technicians utilize regulated, approved insecticides, rodenticides, and misting compounds",
        "Our trained pest management applicators operate in accordance with Ghana Environmental Protection Agency (EPA) public health guidelines, utilizing regulated insecticides, rodenticides, and misting compounds"
    )

    # 2. Add Mandatory Pest Control Safety Advisory Box before why-choose
    safety_advisory = """                        <!-- Mandatory Safety Advisory Callout -->
                        <div class="alert alert-warning" style="background-color: #fff8e1; border-left: 4px solid #f59e0b; padding: 18px 20px; margin-bottom: 30px; border-radius: 4px; color: #92400e;">
                            <h5 style="color: #92400e; font-weight: 700; margin-bottom: 8px;"><i class="fas fa-exclamation-triangle mr-2"></i> Mandatory Pest Control Safety Advisory</h5>
                            <p style="margin-bottom: 8px; font-size: 14px; line-height: 22px;">For the safety of your family, staff, and pets, all chemical pest management procedures require strict adherence to standard safety protocols:</p>
                            <ul style="margin-bottom: 0; font-size: 13px; line-height: 22px; padding-left: 20px;">
                                <li><strong>Food &amp; Utensil Protection:</strong> Seal all open foodstuffs, cooking utensils, and drinking water containers in airtight plastic tubs or refrigerators prior to application.</li>
                                <li><strong>Mandatory Vacate &amp; Re-Entry Window:</strong> Occupants, children, and domestic pets must vacate treated premises during application and observe a mandatory <strong>2 to 4-hour</strong> re-entry period.</li>
                                <li><strong>Post-Treatment Ventilation:</strong> Ventilate the property thoroughly by opening all windows and doors for at least 30 minutes upon return.</li>
                                <li><strong>Safety Datasheets:</strong> Product technical specifications and safety instructions are reviewed on-site with clients prior to treatment.</li>
                            </ul>
                        </div>
                        <div class="why-choose-box-layout2">"""

    if "Mandatory Pest Control Safety Advisory" not in html:
        html = html.replace('<div class="why-choose-box-layout2">', safety_advisory, 1)

    # 3. Refine FAQ 2 & 3 answers
    old_faq2 = "Yes. We use EPA-approved public health insecticides formulated for indoor environments. When safety instructions and mandatory 2-4 hour re-entry windows are followed, treatments leave behind odorless, safe residual barriers."
    new_faq2 = "We use regulated public health insecticides formulated for structural environments. These are active chemical formulations that must be respected: when our mandatory food sealing and 2 to 4-hour vacate and ventilation windows are observed, treatments break pest breeding cycles without exposing occupants to direct spray drift."
    html = html.replace(old_faq2, new_faq2)

    with open("pest-control.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Remediated pest-control.html: Inserted Mandatory Safety Advisory callout and tempered applicator credentials.")


def fix_index_testimonials_and_forms():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add Testimonials Disclosure
    disclosure_html = """                </div>
                <div class="col-12 text-center mt-3">
                    <p style="font-size: 13px; color: rgba(255, 255, 255, 0.7); margin-bottom: 0;">
                        <i class="fas fa-info-circle mr-1"></i> Customer testimonials shown reflect historical feedback from EcoCare's previous website. Formal re-verification &amp; consent renewal is logged as pending in accordance with Ghana's Data Protection Act, 2012 (Act 843).
                    </p>
                </div>"""

    if "Customer testimonials shown reflect historical feedback" not in html:
        html = html.replace(
            r'                    </div>' + '\n' + r'                </div>' + '\n' + r'            </div>' + '\n' + r'        </section>' + '\n' + r'        <!-- Testimonial Area End Here -->',
            r'                    </div>' + '\n' + disclosure_html + '\n' + r'            </div>' + '\n' + r'        </section>' + '\n' + r'        <!-- Testimonial Area End Here -->'
        )

    # 2. Add Honeypot to index booking form
    if 'name="website_url"' not in html:
        html = html.replace(
            '<form class="contact-form-box" id="ecocare-booking-form">',
            '<form class="contact-form-box" id="ecocare-booking-form">\n                                <div style="display:none !important;" aria-hidden="true"><input type="text" name="website_url" tabindex="-1" autocomplete="off" value=""></div>'
        )

    # 3. Temper slider guarantee text
    html = html.replace(
        "Quality, safety, and customer satisfaction guaranteed",
        "Dedicated to Quality, Safety &amp; Customer Satisfaction"
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ Remediated index.html: Added testimonial archive disclosure, honeypot, and tempered guarantee copy.")


def inject_honeypot_in_sidebar_forms():
    files = [
        "faq.html", "single-service1.html", "single-service2.html",
        "carpet-cleaning.html", "upholstery-cleaning.html"
    ]
    for fname in files:
        with open(fname, "r", encoding="utf-8") as f:
            content = f.read()
        if 'name="website_url"' not in content:
            content = content.replace(
                '<form class="contact-form-box" id="contact-form">',
                '<form class="contact-form-box" id="contact-form">\n                                <div style="display:none !important;" aria-hidden="true"><input type="text" name="website_url" tabindex="-1" autocomplete="off" value=""></div>'
            )
            with open(fname, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✓ Injected honeypot spam protection into {fname}")


if __name__ == "__main__":
    fix_calculate_form()
    fix_contact_page()
    fix_pest_control_safety()
    fix_index_testimonials_and_forms()
    inject_honeypot_in_sidebar_forms()
    print("All audit remediations applied cleanly!")

