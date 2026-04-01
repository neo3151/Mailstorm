import os
import sys
import logging
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# CONFIGURATION
OUTPUT_FILE = r"C:\Users\neo31\Mailstorm\releases\Mailstorm_Ep1_Abyssal_Edition.pdf"
ARCHIVE_PATH = r"C:\Users\neo31\.gemini\antigravity\brain\d01fdf8d-e4ea-4465-a618-0d2ad8e90864"

if not os.path.exists(ARCHIVE_PATH):
    logging.error(f"FATAL: Archive directory not found: {ARCHIVE_PATH}")
    sys.exit(1)

# CAPTION DATA: (panel_index, placement, text)
# placement: "TL" = Top-Left, "BR" = Bottom-Right
CAPTIONS = {
    0:  ("TL", "BRANCH 61. TOMB OF EFFICIENCY. THE MANDATE IS THE ONLY BREATHABLE AIR."),
    1:  ("BR", "CCA INITIATE KIP BAXTER. TABLE 2 STRESS LEVEL: CRITICAL. TREMOR INDEX: RISING."),
    2:  ("TL", "THE DOORS ACCEPT NO RETURN POSTAGE. ONLY FORWARD PIVOTS ARE AUTHORIZED."),
    3:  ("TL", "THE SORTING FLOOR. NON-EUCLIDEAN DEPTH. THE CASES STRETCH INTO INFINITY."),
    4:  ("BR", "CARRIER STAN. TABLE 1 VETERAN. HIS 64-WRAPS VIBRATE AT GRIEVANCE FREQUENCY."),
    5:  ("TL", "SHADOW SEVERANCE INITIATED. ARTICLE 14, CLAUSE 3: CIVILIAN EGO TERMINATED."),
    6:  ("BR", "THE SHADOW THRASHES. THE ABYSS TASTES THE INITIATE FOR THE FIRST TIME."),
    7:  ("TL", "MGR CHUCK. CONTROL-CLASS. HIS SHADOW HAS MORE EYES THAN HIS BUDGET HAS CUTS."),
    8:  ("BR", "STATIONARY EVENT DETECTED. THE ALGORITHM DEMANDS MOMENTUM. ALWAYS MOMENTUM."),
    9:  ("TL", "THE WEIGHT OF S.P.M. SCORES. KIP IS PINNED BY THE GRAVITY OF FAILURE."),
    10: ("BR", "NIXIE PHANTOM EMERGENCE. BORN FROM THE SLUDGE OF UNCLAIMED SOULS."),
}

SPLASH_CAPTION = ("TL", "THE ANCHOR STRIKE. GRIEVANCE MANA AT MAXIMUM LOAD.")
AFTERMATH_CAPTION = ("BR", "THE FLOOR IS CLEAR. FOR NOW. WELCOME TO THE ABYSS, INITIATE.")

# STORY PANELS (in order)
STORY_PANELS = [
    "abyssal_ep1_page_1_panel_1_monolith_wide_1775013447185.png",
    "abyssal_ep1_page_1_panel_2_kips_hands_trembling_door_1775013465216.png",
    "abyssal_ep1_page_1_panel_3_doors_open_fluorescent_light_1775013486160.png",
    "abyssal_ep1_page_2_panel_1_the_pit_interior_wide_non_euclidean_1775013502076.png",
    "abyssal_ep1_page_2_panel_2_stans_vibrating_aura_veteran_carrier_1775013521259.png",
    "abyssal_ep1_page_2_panel_3_stan_boot_shadow_strike_impact_1775013538296.png",
    "abyssal_ep1_page_2_panel_4_kips_shadow_thrashing_ink_bleeding_horror_anatomy_screaming_kip_1775013560576.png",
    "abyssal_ep1_page_3_panel_1_chucks_towering_monster_shadow_crate_silhouette_multi_eyed_horror_1775013579067.png",
    "abyssal_ep1_page_3_panel_2_mdd_beep_stationary_event_alert_polished_v2_1775013663407.png",
    "abyssal_ep1_page_3_panel_3_gravity_crush_kip_pinned_linoleum_cracking_badge_texture_1775013680343.png",
    "abyssal_ep1_page_3_panel_4_nixie_phantom_sludge_emergence_mangled_paper_horror_polished_v2_1775013697449.png",
]

# SPECIAL PAGES
COVER = "abyssal_episode_1_hazard_orange_cover_premium_texture_v3_1775017416185_1775015034521.png"
TOC = "abyssal_ep1_pdf_page_3_toc_background_no_text_clean_1775017028042.png"
FOREWORD = "abyssal_ep1_pdf_page_4_postmaster_foreword_silhouette_v2_1775017416190_1775015334522_1775016046652.png"
PRE_STRIKE = "abyssal_ep1_stan_pre_strike_stance_1571_denial_1775017138708.png"
SPLASH = "abyssal_episode_1_page_4_splash_stan_strike_1775012700676.png"
AFTERMATH = "abyssal_ep1_pdf_page_21_aftermath_llv_graveyard_stan_kip_walking_high_fidelity_1775017416191_1775015334523_1775016063504.png"
DOSSIER_KIP = "abyssal_dossier_61094_kip_baxter_redacted_high_fidelity_v2_1775017416186_1775015056679.png"
DOSSIER_CHUCK = "chucks_multieyed_shadow_polished_line_art_no_text_final_v2_1775012303079.png"
BLUEPRINT_MDD = "abyssal_mdd_scanner_blueprint_schematic_high_fidelity_v2_1775017416187_1775015074586.png"
BLUEPRINT_FLOOR = "abyssal_sorting_floor_concept_1775010362396.png"
ARTICLE_14 = "abyssal_ep1_pdf_page_29_article_14_shield_of_just_cause_schematic_v2_1775017416192_1775015334524_1775016081555.png"
GALLERY = "abyssal_gallery_of_spite_evolution_composite_high_fidelity_v2_1775017416188_1775015216669.png"
CREDITS = "abyssal_ep1_pdf_page_31_credits_archive_seal_industrial_stamp_v2_1775017416193_1775015334525_1775016102316.png"
BACK_COVER = "abyssal_ep1_pdf_page_32_back_cover_monolithic_logo_high_fidelity_v2_1775017416194_1775015334526_1775016120479.png"

def build_toc_page(img):
    """Burn correct TOC typography onto a clean background image."""
    draw = ImageDraw.Draw(img)
    w, h = img.size
    fs_title = max(48, int(h * 0.045))
    fs_section = max(30, int(h * 0.028))
    fs_small = max(22, int(h * 0.020))
    try:
        font_title = ImageFont.truetype("arialbd.ttf", fs_title)
        font_section = ImageFont.truetype("arial.ttf", fs_section)
        font_small = ImageFont.truetype("ariali.ttf", fs_small)
    except:
        font_title = font_section = font_small = ImageFont.load_default()

    cx = w // 2
    y = int(h * 0.08)

    # Title
    draw.text((cx, y), "DEPARTMENT OF LOGISTICS", fill="#000000", font=font_title, anchor="mt")
    y += fs_title + 10
    draw.text((cx, y), "EMPLOYEE CONTRACT & ASSIGNMENT TABLE", fill="#333333", font=font_small, anchor="mt")
    y += fs_small + 30

    # Divider
    draw.line([(int(w*0.15), y), (int(w*0.85), y)], fill="#000000", width=3)
    y += 40

    # Sections
    sections = [
        ("ARTICLE 1.1", "THE THRESHOLD", "P. 05"),
        ("ARTICLE 2.1", "THE AWAKENING", "P. 08"),
        ("ARTICLE 3.1", "THE ALGORITHM'S GAZE", "P. 12"),
        ("ARTICLE 4.1", "THE ANCHOR STRIKE", "P. 16"),
        ("ARTICLE 5.1", "THE AFTERMATH", "P. 18"),
        ("ADDENDUM A", "EMPLOYEE DOSSIERS", "P. 20"),
        ("ADDENDUM B", "TECHNICAL SCHEMATICS", "P. 22"),
        ("ADDENDUM C", "ARTICLE 14: SHIELD OF JUST CAUSE", "P. 23"),
        ("ADDENDUM D", "CREDITS & ARCHIVE SEAL", "P. 24"),
    ]
    left = int(w * 0.12)
    right = int(w * 0.88)
    for ref, title, page in sections:
        draw.text((left, y), ref, fill="#990000", font=font_small)
        draw.text((left + int(w * 0.18), y), title, fill="#000000", font=font_section)
        draw.text((right, y), page, fill="#555555", font=font_small, anchor="rt")
        y += fs_section + 20

    # Footer
    y = int(h * 0.88)
    draw.line([(int(w*0.15), y), (int(w*0.85), y)], fill="#000000", width=3)
    y += 20
    draw.text((cx, y), "AUTHORIZED SIGNATURES REQUIRED BELOW", fill="#555555", font=font_small, anchor="mt")
    y += fs_small + 30
    draw.line([(int(w*0.15), y), (int(w*0.45), y)], fill="#990000", width=2)
    draw.line([(int(w*0.55), y), (int(w*0.85), y)], fill="#990000", width=2)
    y += 10
    draw.text((int(w*0.30), y), "KIP BAXTER", fill="#990000", font=font_small, anchor="mt")
    draw.text((int(w*0.70), y), "STAN [CLASSIFIED]", fill="#990000", font=font_small, anchor="mt")

    return img


def draw_caption(img, placement, text):
    """Burn a yellow caption box onto a PIL Image, sized to fit the text."""
    draw = ImageDraw.Draw(img)
    w, h = img.size

    # Font setup
    font_size = max(28, int(h * 0.025))
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()

    pad = 20
    max_text_w = int(w * 0.40)

    # Pixel-accurate word wrap using font.getlength()
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try:
            tw = font.getlength(test)
        except:
            tw = len(test) * font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    # Measure actual box dimensions from rendered lines
    line_h = font_size + 10
    actual_max_w = 0
    for line in lines:
        try:
            lw = font.getlength(line)
        except:
            lw = len(line) * font_size * 0.6
        if lw > actual_max_w:
            actual_max_w = lw

    box_w = int(actual_max_w) + pad * 2
    box_h = len(lines) * line_h + pad * 2

    # Position
    if placement == "TL":
        x, y = int(w * 0.03), int(h * 0.03)
    else:
        x = int(w - box_w - w * 0.03)
        y = int(h - box_h - h * 0.03)

    # Draw yellow box with black border
    draw.rectangle([x, y, x + box_w, y + box_h], fill="#FFFF00", outline="#000000", width=4)

    # Draw each line of text inside the box
    for i, line in enumerate(lines):
        draw.text((x + pad, y + pad + i * line_h), line, fill="#000000", font=font)

    return img


def add_image_page(pdf, filepath, caption_data=None):
    """Add an image page to the PDF, optionally burning a caption onto it."""
    if not os.path.exists(filepath):
        print(f"  ⚠ Not found: {os.path.basename(filepath)}")
        pdf.add_page()
        pdf.set_fill_color(0, 0, 0)
        pdf.rect(0, 0, 210, 297, "F")
        return

    img = Image.open(filepath).convert("RGB")
    img_w, img_h = img.size

    if caption_data:
        placement, text = caption_data
        img = draw_caption(img, placement, text)

    # Save temp captioned image
    temp = filepath + ".captioned.jpg"
    img.save(temp, quality=95)
    img.close()

    aspect = img_w / img_h

    if aspect > 1.2:
        pdf.add_page(orientation="L")
        pdf.image(temp, x=0, y=0, w=297, h=210)
    else:
        pdf.add_page(orientation="P")
        pdf.image(temp, x=0, y=0, w=210, h=297)

    os.remove(temp)


def add_black_page(pdf, text=""):
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, "F")
    if text:
        pdf.set_text_color(255, 255, 255)
        pdf.set_font('helvetica', 'B', 14)
        pdf.set_y(140)
        pdf.cell(0, 10, text, align='C')


def p(name):
    return os.path.join(ARCHIVE_PATH, name)


def assemble():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.set_title("Mailstorm: Episode 1 - The Shadow Day (Abyssal Edition)")
    pdf.set_author("The Department of Logistics")
    pdf.set_creator("Abyssal Foundry v1.0")

    total = 26
    done = 0

    def progress(label):
        nonlocal done
        done += 1
        bar_len = 20
        filled = int(bar_len * done / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        pct = int(100 * done / total)
        print(f"  [{bar}] {pct:3d}% | {done}/{total} | {label}")

    print("--- ASSEMBLING ABYSSAL EDITION (WITH CAPTIONS) ---")

    # P1: Cover
    add_image_page(pdf, p(COVER)); progress("Cover")
    # P2: Inside Front
    add_black_page(pdf, "THE MANDATE IS ABSOLUTE."); progress("Inside Front")
    # P3: TOC (programmatic text overlay)
    toc_img = Image.open(p(TOC)).convert("RGB")
    toc_img = build_toc_page(toc_img)
    toc_temp = p(TOC) + ".toc.jpg"
    toc_w, toc_h = toc_img.size
    toc_img.save(toc_temp, quality=95)
    toc_img.close()
    pdf.add_page(orientation="P")
    pdf.image(toc_temp, x=0, y=0, w=210, h=297)
    os.remove(toc_temp)
    progress("Table of Contents")
    # P4: Foreword
    add_image_page(pdf, p(FOREWORD)); progress("Foreword")

    # P5-P15: Story Panels with Captions
    for i, panel_file in enumerate(STORY_PANELS):
        caption = CAPTIONS.get(i)
        add_image_page(pdf, p(panel_file), caption)
        progress(f"Panel {i+1:02d}")

    # P16: Pre-Strike (unique panel)
    add_image_page(pdf, p(PRE_STRIKE), ("TL", "STAN INVOKES 1571 ABSOLUTION. DENIED.")); progress("Pre-Strike Stance")
    # P17: The Climax Splash
    add_image_page(pdf, p(SPLASH), SPLASH_CAPTION); progress("Splash Climax")

    # P19: Aftermath
    add_image_page(pdf, p(AFTERMATH), AFTERMATH_CAPTION); progress("Aftermath")

    # P20: Epilogue
    add_black_page(pdf, "THE SHADOW DAY IS NEVER OVER. THE CYCLE CONTINUES."); progress("Epilogue")

    # P21-P26: Addendum
    add_image_page(pdf, p(DOSSIER_KIP)); progress("Dossier: Kip")
    add_image_page(pdf, p(DOSSIER_CHUCK)); progress("Dossier: Chuck")
    add_image_page(pdf, p(BLUEPRINT_MDD)); progress("Blueprint: MDD")
    add_image_page(pdf, p(ARTICLE_14)); progress("Article 14")
    add_image_page(pdf, p(CREDITS)); progress("Credits")
    add_image_page(pdf, p(BACK_COVER)); progress("Back Cover")

    pdf.output(OUTPUT_FILE)
    print(f"\n--- ASSEMBLY COMPLETE: {OUTPUT_FILE} ---")
    print(f"--- {total} pages compiled. ---")


if __name__ == "__main__":
    try:
        assemble()
    except ImportError as e:
        print(f"Missing library: {e}")
        print("Run: pip install fpdf2 Pillow")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
