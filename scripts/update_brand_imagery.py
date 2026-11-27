#!/usr/bin/env python3
"""
scripts/update_brand_imagery.py
Comprehensive replacement of all non-Black / stock imagery across the EcoCare website
with authentic Black Ghanaian EcoCare cleaning specialists wearing official EcoCare attire with logo.
"""

import os
import re
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_path(rel_path):
    return os.path.join(BASE_DIR, rel_path)

def make_figure5():
    """
    Updates img/figure/figure5.png by cleanly replacing the photos inside
    the two tilted polaroid frames while preserving 100% of the frames,
    shadows, and background circular illustrations.
    """
    fig5_path = get_path("img/figure/figure5.png")
    fig5 = Image.open(fig5_path).convert("RGBA")
    w, h = fig5.size
    pix = fig5.load()

    # 1. Create masks for top inner photo and bottom inner photo
    mask_top = Image.new("L", (w, h), 0)
    mask_bottom = Image.new("L", (w, h), 0)
    top_pix = mask_top.load()
    bottom_pix = mask_bottom.load()

    for y in range(120, 390):
        for x in range(120, 440):
            r, g, b, a = pix[x, y]
            if a > 240 and not (r > 240 and g > 240 and b > 240):
                top_pix[x, y] = 255

    for y in range(300, 620):
        for x in range(250, 580):
            r, g, b, a = pix[x, y]
            if a > 240 and not (r > 240 and g > 240 and b > 240):
                bottom_pix[x, y] = 255

    mask_top_smooth = mask_top.filter(ImageFilter.GaussianBlur(1.0))
    mask_bottom_smooth = mask_bottom.filter(ImageFilter.GaussianBlur(1.0))

    # 2. Source photo for top frame: EcoCare team photo
    team_img = Image.open(get_path("img/team/ecocare-team.jpg")).convert("RGBA")
    crop_top = team_img.crop((320, 40, 736, 520))
    crop_top = crop_top.resize((360, 300), Image.Resampling.LANCZOS)
    crop_top_rot = crop_top.rotate(-18, expand=True, resample=Image.Resampling.BICUBIC)

    canvas_top = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    cx = 275 - crop_top_rot.width // 2
    cy = 250 - crop_top_rot.height // 2
    canvas_top.paste(crop_top_rot, (cx, cy), crop_top_rot)

    # 3. Source photo for bottom frame: EcoCare field technician in uniform
    tech_img = Image.open(get_path("img/projects/sofa-technician-prep.jpg")).convert("RGBA")
    crop_bottom = tech_img.crop((80, 100, 680, 800))
    crop_bottom = crop_bottom.resize((360, 330), Image.Resampling.LANCZOS)
    crop_bottom_rot = crop_bottom.rotate(15, expand=True, resample=Image.Resampling.BICUBIC)

    canvas_bottom = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    bx = 410 - crop_bottom_rot.width // 2
    by = 460 - crop_bottom_rot.height // 2
    canvas_bottom.paste(crop_bottom_rot, (bx, by), crop_bottom_rot)

    # 4. Composite
    result = fig5.copy()
    result.paste(canvas_top, (0, 0), mask_top_smooth)
    result.paste(canvas_bottom, (0, 0), mask_bottom_smooth)
    result.save(fig5_path, "PNG", optimize=True)
    print(f"-> Updated {fig5_path}")

def make_about1():
    """
    Updates img/figure/about1.jpg (469x596) with the authentic Black Ghanaian
    female EcoCare cleaning supervisor in emerald green polo shirt with EcoCare logo.
    """
    about1_path = get_path("img/figure/about1.jpg")
    team_img = Image.open(get_path("img/team/ecocare-team.jpg")).convert("RGBA")
    
    # Crop the female supervisor standing on the right
    # Coordinate: x in [480, 736], y in [40, 660]
    woman = team_img.crop((485, 40, 736, 650))
    
    # Target size: 469 x 596
    target_w, target_h = 469, 596
    
    # Create background canvas: luxury modern clean interior with soft subtle gradient
    bg = Image.new("RGBA", (target_w, target_h), (245, 248, 252, 255))
    draw = ImageDraw.Draw(bg)
    # Subtle elegant gradient
    for y in range(target_h):
        r = int(245 - 20 * (y / target_h))
        g = int(248 - 15 * (y / target_h))
        b = int(252 - 10 * (y / target_h))
        draw.line([(0, y), (target_w, y)], fill=(r, g, b, 255))
        
    # Scale woman to fit nicely
    scale = (target_h - 40) / woman.height
    new_w = int(woman.width * scale)
    new_h = int(woman.height * scale)
    woman_scaled = woman.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Enhance slightly
    enhancer = ImageEnhance.Sharpness(woman_scaled)
    woman_scaled = enhancer.enhance(1.2)
    
    # Paste centered horizontally, aligned to bottom
    paste_x = (target_w - new_w) // 2
    paste_y = target_h - new_h
    bg.paste(woman_scaled, (paste_x, paste_y), woman_scaled)
    
    # Save as high quality JPEG
    bg.convert("RGB").save(about1_path, "JPEG", quality=95)
    print(f"-> Updated {about1_path} (469x596)")

def make_figure4():
    """
    Updates img/figure/figure4.png (279x273) cutout with the authentic smiling
    Black Ghanaian female EcoCare specialist in green polo shirt.
    """
    fig4_path = get_path("img/figure/figure4.png")
    team_img = Image.open(get_path("img/team/ecocare-team.jpg")).convert("RGBA")
    
    # Crop the female specialist standing on the right
    woman = team_img.crop((495, 45, 735, 620))
    
    # Create transparent canvas 279 x 273
    target_w, target_h = 279, 273
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale to fill height
    scale = target_h / woman.height
    new_w = int(woman.width * scale)
    new_h = target_h
    woman_scaled = woman.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Enhance
    woman_scaled = ImageEnhance.Sharpness(woman_scaled).enhance(1.2)
    woman_scaled = ImageEnhance.Color(woman_scaled).enhance(1.1)
    
    # Paste centered horizontally
    paste_x = (target_w - new_w) // 2
    canvas.paste(woman_scaled, (paste_x, 0), woman_scaled)
    
    canvas.save(fig4_path, "PNG", optimize=True)
    print(f"-> Updated {fig4_path} (279x273)")

def make_banne_img1():
    """
    Updates img/figure/banne-img1.png (880x700) cutout for .progress-wrap-layout1
    with the authentic Black Ghanaian EcoCare technician in uniform.
    """
    banne_path = get_path("img/figure/banne-img1.png")
    tech_img = Image.open(get_path("img/projects/sofa-technician-prep.jpg")).convert("RGBA")
    
    target_w, target_h = 880, 700
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    
    # Scale technician to fit
    tech_crop = tech_img.crop((60, 50, 700, 950))
    scale = target_h / tech_crop.height
    new_w = int(tech_crop.width * scale)
    new_h = target_h
    tech_scaled = tech_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # Enhance
    tech_scaled = ImageEnhance.Sharpness(tech_scaled).enhance(1.15)
    
    # Paste on the right side of the canvas (Clenix layout has image on right side)
    paste_x = target_w - new_w - 40
    canvas.paste(tech_scaled, (paste_x, 0), tech_scaled)
    
    canvas.save(banne_path, "PNG", optimize=True)
    print(f"-> Updated {banne_path} (880x700)")

def make_banner_bg():
    """
    Updates img/figure/banner-bg.jpg (1920x525) and banner-bg1.jpg (1920x522)
    with a wide panoramic banner: authentic field cleaning operations on the left,
    and a rich brand gradient overlay on the right for text readability.
    """
    target_w, target_h = 1920, 525
    canvas = Image.new("RGBA", (target_w, target_h), (18, 40, 76, 255))
    
    # Load authentic field image
    sofa_img = Image.open(get_path("img/projects/sofa-restored-patio.jpg")).convert("RGBA")
    tech_img = Image.open(get_path("img/projects/sofa-technician-prep.jpg")).convert("RGBA")
    
    # Resize and place field images on left side
    sofa_scaled = sofa_img.resize((1000, 525), Image.Resampling.LANCZOS)
    canvas.paste(sofa_scaled, (0, 0))
    
    tech_crop = tech_img.crop((50, 40, 720, 900))
    tech_scaled = tech_crop.resize((480, 525), Image.Resampling.LANCZOS)
    canvas.paste(tech_scaled, (500, 0), tech_scaled)
    
    # Create smooth dark blue to emerald gradient overlay
    # Full gradient from x=400 to 1920 to keep right side crystal clear for text
    overlay = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    for x in range(target_w):
        if x < 400:
            alpha = int(80 * (x / 400))
        elif x < 900:
            alpha = int(80 + 150 * ((x - 400) / 500))
        else:
            alpha = 245
        # Rich deep EcoCare navy blue #132440
        draw.line([(x, 0), (x, target_h)], fill=(19, 36, 64, alpha))
        
    canvas = Image.alpha_composite(canvas, overlay)
    
    # Save banner-bg.jpg
    b1_path = get_path("img/figure/banner-bg.jpg")
    canvas.convert("RGB").save(b1_path, "JPEG", quality=92)
    print(f"-> Updated {b1_path} (1920x525)")
    
    # Save banner-bg1.jpg (1920x522)
    b2_path = get_path("img/figure/banner-bg1.jpg")
    canvas.resize((1920, 522), Image.Resampling.LANCZOS).convert("RGB").save(b2_path, "JPEG", quality=92)
    print(f"-> Updated {b2_path} (1920x522)")

def make_widget_and_banner_figure():
    """
    Updates widget-banner.png (370x307) and banner-figure.png (448x473)
    with the authentic Black Ghanaian EcoCare specialist in green uniform.
    """
    team_img = Image.open(get_path("img/team/ecocare-team.jpg")).convert("RGBA")
    woman = team_img.crop((495, 45, 735, 620))
    
    # 1. widget-banner.png (370x307)
    wb_path = get_path("img/figure/widget-banner.png")
    wb_canvas = Image.new("RGBA", (370, 307), (0, 0, 0, 0))
    scale_wb = 307 / woman.height
    wb_w = int(woman.width * scale_wb)
    wb_woman = woman.resize((wb_w, 307), Image.Resampling.LANCZOS)
    wb_canvas.paste(wb_woman, ((370 - wb_w) // 2, 0), wb_woman)
    wb_canvas.save(wb_path, "PNG", optimize=True)
    print(f"-> Updated {wb_path} (370x307)")
    
    # 2. banner-figure.png (448x473)
    bf_path = get_path("img/figure/banner-figure.png")
    bf_canvas = Image.new("RGBA", (448, 473), (0, 0, 0, 0))
    scale_bf = 473 / woman.height
    bf_w = int(woman.width * scale_bf)
    bf_woman = woman.resize((bf_w, 473), Image.Resampling.LANCZOS)
    bf_canvas.paste(bf_woman, ((448 - bf_w) // 2, 0), bf_woman)
    bf_canvas.save(bf_path, "PNG", optimize=True)
    print(f"-> Updated {bf_path} (448x473)")

def make_blog_images():
    """
    Updates blog7.jpg, blog2.jpg, blog3.jpg (520x370) with authentic field photography.
    """
    target_w, target_h = 520, 370
    
    # blog7.jpg: Carpet Deep Cleaning -> carpet wand extraction
    b7_path = get_path("img/blog/blog7.jpg")
    im7 = Image.open(get_path("img/projects/carpet-wand-extraction.jpg")).convert("RGB")
    # Center crop to 520x370
    crop7 = ImageOps.fit(im7, (target_w, target_h), Image.Resampling.LANCZOS)
    crop7.save(b7_path, "JPEG", quality=92)
    print(f"-> Updated {b7_path} (520x370)")
    
    # blog2.jpg: Pre-Move Deep Scrubbing -> sofa technician prep
    b2_path = get_path("img/blog/blog2.jpg")
    im2 = Image.open(get_path("img/projects/sofa-technician-prep.jpg")).convert("RGB")
    crop2 = ImageOps.fit(im2, (target_w, target_h), Image.Resampling.LANCZOS)
    crop2.save(b2_path, "JPEG", quality=92)
    print(f"-> Updated {b2_path} (520x370)")
    
    # blog3.jpg: Eco-Friendly Fumigation & Sanitation -> mattress rotary scrub
    b3_path = get_path("img/blog/blog3.jpg")
    im3 = Image.open(get_path("img/projects/mattress-rotary-scrub.jpg")).convert("RGB")
    crop3 = ImageOps.fit(im3, (target_w, target_h), Image.Resampling.LANCZOS)
    crop3.save(b3_path, "JPEG", quality=92)
    print(f"-> Updated {b3_path} (520x370)")

def make_service_images():
    """
    Updates residential-cleaning.jpg and general-deep-cleaning.jpg (736x981)
    with authentic EcoCare field photos.
    """
    target_w, target_h = 736, 981
    
    # residential-cleaning.jpg
    res_path = get_path("img/services/residential-cleaning.jpg")
    im_patio = Image.open(get_path("img/projects/sofa-restored-patio.jpg")).convert("RGB")
    res_crop = ImageOps.fit(im_patio, (target_w, target_h), Image.Resampling.LANCZOS)
    res_crop.save(res_path, "JPEG", quality=92)
    print(f"-> Updated {res_path} (736x981)")
    
    # general-deep-cleaning.jpg
    gen_path = get_path("img/services/general-deep-cleaning.jpg")
    res_crop.save(gen_path, "JPEG", quality=92)
    print(f"-> Updated {gen_path} (736x981)")
    
    # commercial-cleaning.jpg (736x1104)
    comm_path = get_path("img/services/commercial-cleaning.jpg")
    im_rec = Image.open(get_path("img/projects/office-reception-delivery.jpg")).convert("RGB")
    comm_crop = ImageOps.fit(im_rec, (736, 1104), Image.Resampling.LANCZOS)
    comm_crop.save(comm_path, "JPEG", quality=92)
    print(f"-> Updated {comm_path} (736x1104)")
    
    # commercial-janitorial.jpg (736x736)
    jan_path = get_path("img/services/commercial-janitorial.jpg")
    im_suite = Image.open(get_path("img/projects/executive-leather-suite.jpg")).convert("RGB")
    jan_crop = ImageOps.fit(im_suite, (736, 736), Image.Resampling.LANCZOS)
    jan_crop.save(jan_path, "JPEG", quality=92)
    print(f"-> Updated {jan_path} (736x736)")

def fix_process_icons():
    """
    Fixes Step 01 icon in about1.html so that 'Inquiry & Scoping' has a visible phone icon.
    """
    about1_path = get_path("about1.html")
    with open(about1_path, "r", encoding="utf-8") as f:
        html = f.read()
        
    old_icon = '<i class="flaticon-call-answer"></i>'
    new_icon = '<i class="fas fa-phone-alt"></i>'
    if old_icon in html:
        html = html.replace(old_icon, new_icon)
        with open(about1_path, "w", encoding="utf-8") as f:
            f.write(html)
        print("-> Fixed Step 01 icon in about1.html to <i class=\"fas fa-phone-alt\"></i>")
    else:
        print("-> Step 01 icon already updated or not found in about1.html")

def run_all():
    print("=== STARTING BRAND IMAGERY & ICON UPDATE ===")
    make_figure5()
    make_about1()
    make_figure4()
    make_banne_img1()
    make_banner_bg()
    make_widget_and_banner_figure()
    make_blog_images()
    make_service_images()
    fix_process_icons()
    print("=== BRAND IMAGERY & ICON UPDATE COMPLETED SUCCESSFULLY ===")

if __name__ == "__main__":
    run_all()
