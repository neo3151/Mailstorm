"""Prepare Episode 2 assets for the web viewer."""
import os
from PIL import Image, ImageDraw, ImageFont

ARCHIVE = r"C:\Users\neo31\.gemini\antigravity\brain\d01fdf8d-e4ea-4465-a618-0d2ad8e90864"
WEB_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\episode_2"
PDF_SRC = r"C:\Users\neo31\Mailstorm\releases\Mailstorm_Ep2_Abyssal_Edition.pdf"

PANELS = [
    ("01_cover.jpg", "ep2_cover_table2_bloodline_hazard_orange_1775017771799.png", None),
    ("02_assignment.jpg", "ep2_panel_01_chuck_route_card_assignment_1775017796158.png", ("TL", "ROUTE 19. SOLO ASSIGNMENT. NO BACKUP AUTHORIZED.")),
    ("03_shadow_grin.jpg", "ep2_panel_02_chucks_shadow_grinning_1775017812732.png", ("BR", "CHUCK'S SHADOW GRINS. IT FEEDS ON FRESH INITIATES.")),
    ("04_llv_depart.jpg", "ep2_panel_03_llv_departure_route19_1775017835507.png", ("TL", "THE LLV GROANS TO LIFE. IT HAS OUTLIVED SIX CARRIERS.")),
    ("05_bone_burn.jpg", "ep2_panel_04_bone_burn_veins_glowing_1775017853408.png", ("BR", "TABLE 2 CURSE ACTIVATES. BONE-MARROW BURN. MANA COST: STEEP.")),
    ("06_xray.jpg", "ep2_panel_05_kip_skeleton_xray_green_mana_1775017871179.png", ("TL", "FLUORESCENT GREEN IN THE VEINS. THE BODY PAYS THE CONTRACT.")),
    ("07_satchel.jpg", "ep2_panel_06_satchel_crushing_weight_1775017889177.png", ("BR", "THE SATCHEL WEIGHS MORE THAN PHYSICS ALLOWS.")),
    ("08_swarm.jpg", "ep2_panel_07_redplum_swarm_mailbox_eruption_1775017913640.png", ("TL", "REDPLUM CURSE DETECTED. SENTIENT ADVERTISEMENT BATS.")),
    ("09_heather.jpg", "ep2_panel_08_heather_arrival_llv_confident_1775017930254.png", ("BR", "NEW ASSET: HEATHER. LEVEL 25. DIGITAL AEGIS EQUIPPED.")),
    ("10_aegis.jpg", "ep2_panel_09_digital_aegis_shield_manifest_1775017947231.png", ("TL", "THE DIGITAL AEGIS MANIFESTS. DOCUMENTATION NULLIFIES ALL.")),
    ("11_shatter.jpg", "ep2_panel_10_bats_shatter_against_shield_1775017965095.png", ("BR", "SHATTER-CRACK. THE SWARM DISINTEGRATES.")),
    ("12_awe.jpg", "ep2_panel_11_kip_ground_awe_heather_standing_1775017983185.png", ("TL", "THE INITIATE WITNESSES TRUE BUREAU-KINESIS.")),
    ("13_sunset.jpg", "ep2_panel_12_last_delivery_sunset_mailbox_1775018000660.png", ("BR", "THE LAST DELIVERY. THE SUN BLEEDS ORANGE.")),
    ("14_hands.jpg", "ep2_panel_13_kips_cracked_hands_closeup_1775018018861.png", ("TL", "THE TABLE 2 CURSE EXTRACTS ITS TOLL. IT ALWAYS DOES.")),
    ("15_resolution.jpg", "ep2_panel_14_heather_leaning_llv_sunset_resolution_1775018040241.png", ("BR", "THE ROUTE IS CLEAR. AMAZON SUNDAY APPROACHES.")),
]

def draw_caption(img, placement, text):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = max(28, int(h * 0.025))
    try: font = ImageFont.truetype("arial.ttf", font_size)
    except: font = ImageFont.load_default()
    pad = 20; max_text_w = int(w * 0.40)
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
    box_w, box_h = int(actual_max_w)+pad*2, len(lines)*line_h+pad*2
    if placement == "TL": x, y = int(w*0.03), int(h*0.03)
    else: x, y = int(w-box_w-w*0.03), int(h-box_h-h*0.03)
    draw.rectangle([x,y,x+box_w,y+box_h], fill="#FFFF00", outline="#000000", width=4)
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#000000", font=font)
    return img

def main():
    import shutil
    os.makedirs(WEB_DIR, exist_ok=True)
    total = len(PANELS) + 1
    for i, (out_name, src_name, caption) in enumerate(PANELS):
        pct = int(100*(i+1)/total)
        bar = "█"*(pct//5) + "░"*(20-pct//5)
        src = os.path.join(ARCHIVE, src_name)
        dst = os.path.join(WEB_DIR, out_name)
        if not os.path.exists(src):
            print(f"  [{bar}] {pct:3d}% | ⚠ Missing: {src_name}"); continue
        img = Image.open(src).convert("RGB")
        if caption: img = draw_caption(img, caption[0], caption[1])
        img.save(dst, quality=90); img.close()
        print(f"  [{bar}] {pct:3d}% | {out_name}")
    if os.path.exists(PDF_SRC):
        shutil.copy2(PDF_SRC, os.path.join(WEB_DIR, "Mailstorm_Ep2_Abyssal_Edition.pdf"))
        print(f"  [████████████████████] 100% | PDF copied")
    print("\n--- EP2 WEB ASSETS READY ---")

if __name__ == "__main__": main()
