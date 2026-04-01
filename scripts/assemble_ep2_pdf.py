import os
import sys
import logging
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OUTPUT_FILE = r"C:\Users\neo31\Mailstorm\releases\Mailstorm_Ep2_Abyssal_Edition.pdf"
ARCHIVE = r"C:\Users\neo31\.gemini\antigravity\brain\d01fdf8d-e4ea-4465-a618-0d2ad8e90864"

if not os.path.exists(ARCHIVE):
    logging.error(f"FATAL: Archive directory not found: {ARCHIVE}")
    sys.exit(1)

CAPTIONS = {
    0:  ("TL", "ROUTE 19. SOLO ASSIGNMENT. NO BACKUP AUTHORIZED. THE ALGORITHM PROVIDES."),
    1:  ("BR", "CHUCK'S SHADOW GRINS. IT FEEDS ON THE SCENT OF FRESH INITIATES."),
    2:  ("TL", "THE LLV GROANS TO LIFE. IT HAS OUTLIVED SIX CARRIERS BEFORE KIP."),
    3:  ("BR", "THE TABLE 2 CURSE ACTIVATES. BONE-MARROW BURN DETECTED. MANA COST: STEEP."),
    4:  ("TL", "FLUORESCENT GREEN IN THE VEINS. THE BODY PAYS WHAT THE CONTRACT DEMANDS."),
    5:  ("BR", "THE SATCHEL WEIGHS MORE THAN PHYSICS ALLOWS. DPS IS HEAVY ON ROUTE 19."),
    6:  ("TL", "REDPLUM CURSE DETECTED. SENTIENT ADVERTISEMENT BATS. THREAT LEVEL: MODERATE."),
    7:  ("BR", "NEW ASSET: HEATHER. LEVEL 25. CLASSIFICATION: APATHY QUEEN. DIGITAL AEGIS EQUIPPED."),
    8:  ("TL", "THE DIGITAL AEGIS MANIFESTS. DOCUMENTATION NULLIFIES CORPORATE LOGIC-LOOPS."),
    9:  ("BR", "SHATTER-CRACK. THE SWARM DISINTEGRATES. MANAGEMENT CANNOT SURVIVE THE CAMERA."),
    10: ("TL", "KIP ON THE GROUND. THE INITIATE WITNESSES TRUE BUREAU-KINESIS."),
    11: ("BR", "THE LAST DELIVERY. THE SUN BLEEDS ORANGE OVER ROUTE 19."),
    12: ("TL", "KIP'S HANDS CRACK. THE TABLE 2 CURSE EXTRACTS ITS TOLL. IT ALWAYS DOES."),
    13: ("BR", "THE ROUTE IS CLEAR. FOR NOW. AMAZON SUNDAY APPROACHES."),
}

COVER = "ep2_cover_table2_bloodline_hazard_orange_1775017771799.png"
STORY_PANELS = [
    "ep2_panel_01_chuck_route_card_assignment_1775017796158.png",
    "ep2_panel_02_chucks_shadow_grinning_1775017812732.png",
    "ep2_panel_03_llv_departure_route19_1775017835507.png",
    "ep2_panel_04_bone_burn_veins_glowing_1775017853408.png",
    "ep2_panel_05_kip_skeleton_xray_green_mana_1775017871179.png",
    "ep2_panel_06_satchel_crushing_weight_1775017889177.png",
    "ep2_panel_07_redplum_swarm_mailbox_eruption_1775017913640.png",
    "ep2_panel_08_heather_arrival_llv_confident_1775017930254.png",
    "ep2_panel_09_digital_aegis_shield_manifest_1775017947231.png",
    "ep2_panel_10_bats_shatter_against_shield_1775017965095.png",
    "ep2_panel_11_kip_ground_awe_heather_standing_1775017983185.png",
    "ep2_panel_12_last_delivery_sunset_mailbox_1775018000660.png",
    "ep2_panel_13_kips_cracked_hands_closeup_1775018018861.png",
    "ep2_panel_14_heather_leaning_llv_sunset_resolution_1775018040241.png",
]

# Reuse EP1 addendum assets
DOSSIER_KIP = "abyssal_dossier_61094_kip_baxter_redacted_high_fidelity_v2_1775017416186_1775015056679.png"
BLUEPRINT = "abyssal_mdd_scanner_blueprint_schematic_high_fidelity_v2_1775017416187_1775015074586.png"
BACK_COVER = "abyssal_ep1_pdf_page_32_back_cover_monolithic_logo_high_fidelity_v2_1775017416194_1775015334526_1775016120479.png"

def p(name): return os.path.join(ARCHIVE, name)

def draw_caption(img, placement, text):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = max(28, int(h * 0.025))
    try: font = ImageFont.truetype("arial.ttf", font_size)
    except: font = ImageFont.load_default()
    pad = 20
    max_text_w = int(w * 0.40)
    words, lines, current = text.split(), [], ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try: tw = font.getlength(test)
        except: tw = len(test) * font_size * 0.6
        if tw <= max_text_w: current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    line_h = font_size + 10
    actual_max_w = max((font.getlength(l) for l in lines), default=100)
    box_w, box_h = int(actual_max_w) + pad*2, len(lines)*line_h + pad*2
    if placement == "TL": x, y = int(w*0.03), int(h*0.03)
    else: x, y = int(w-box_w-w*0.03), int(h-box_h-h*0.03)
    draw.rectangle([x,y,x+box_w,y+box_h], fill="#FFFF00", outline="#000000", width=4)
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#000000", font=font)
    return img

def add_img(pdf, filepath, caption=None):
    if not os.path.exists(filepath):
        pdf.add_page(); pdf.set_fill_color(0,0,0); pdf.rect(0,0,210,297,"F"); return
    img = Image.open(filepath).convert("RGB")
    iw, ih = img.size
    if caption: img = draw_caption(img, caption[0], caption[1])
    tmp = filepath + ".tmp.jpg"; img.save(tmp, quality=95); img.close()
    if iw/ih > 1.2: pdf.add_page(orientation="L"); pdf.image(tmp,0,0,297,210)
    else: pdf.add_page(orientation="P"); pdf.image(tmp,0,0,210,297)
    os.remove(tmp)

def black_page(pdf, text=""):
    pdf.add_page(); pdf.set_fill_color(0,0,0); pdf.rect(0,0,210,297,"F")
    if text:
        pdf.set_text_color(255,255,255); pdf.set_font('helvetica','B',14)
        pdf.set_y(140); pdf.cell(0,10,text,align='C')

def assemble():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.set_title("Mailstorm: Episode 2 - Table 2 Bloodline (Abyssal Edition)")
    pdf.set_author("The Department of Logistics")
    total, done = 20, 0
    def prog(label):
        nonlocal done; done += 1
        filled = int(20*done/total)
        print(f"  [{'█'*filled}{'░'*(20-filled)}] {int(100*done/total):3d}% | {done}/{total} | {label}")

    print("--- ASSEMBLING EP2 ABYSSAL EDITION ---")
    add_img(pdf, p(COVER)); prog("Cover")
    black_page(pdf, "THE TABLE 2 CURSE IS YOUR INHERITANCE."); prog("Inside Front")
    black_page(pdf, ""); prog("Title Page")  # Could add programmatic TOC later

    for i, panel in enumerate(STORY_PANELS):
        add_img(pdf, p(panel), CAPTIONS.get(i))
        prog(f"Panel {i+1:02d}")

    black_page(pdf, "THE ROUTE IS CLEAR. AMAZON SUNDAY APPROACHES."); prog("Epilogue")
    add_img(pdf, p(BACK_COVER)); prog("Back Cover")

    pdf.output(OUTPUT_FILE)
    print(f"\n--- ASSEMBLY COMPLETE: {OUTPUT_FILE} ---")

if __name__ == "__main__":
    try: assemble()
    except Exception as e:
        import traceback; print(f"Error: {e}"); traceback.print_exc()
