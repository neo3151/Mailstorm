"""Prepare Episode 1 assets for the web viewer."""
import os, shutil
from PIL import Image, ImageDraw, ImageFont

ARCHIVE = r"C:\Users\neo31\.gemini\antigravity\brain\d01fdf8d-e4ea-4465-a618-0d2ad8e90864"
WEB_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\episode_1"
PDF_SRC = r"C:\Users\neo31\Mailstorm\releases\Mailstorm_Ep1_Abyssal_Edition.pdf"

PANELS = [
    ("01_cover.jpg", "abyssal_episode_1_hazard_orange_cover_premium_texture_v3_1775017416185_1775015034521.png", None),
    ("05_monolith.jpg", "abyssal_ep1_page_1_panel_1_monolith_wide_1775013447185.png", ("TL", "BRANCH 61. TOMB OF EFFICIENCY. THE MANDATE IS THE ONLY BREATHABLE AIR.")),
    ("06_kips_hands.jpg", "abyssal_ep1_page_1_panel_2_kips_hands_trembling_door_1775013465216.png", ("BR", "CCA INITIATE KIP BAXTER. TABLE 2 STRESS LEVEL: CRITICAL.")),
    ("07_doors.jpg", "abyssal_ep1_page_1_panel_3_doors_open_fluorescent_light_1775013486160.png", ("TL", "THE DOORS ACCEPT NO RETURN POSTAGE. ONLY FORWARD PIVOTS ARE AUTHORIZED.")),
    ("08_pit.jpg", "abyssal_ep1_page_2_panel_1_the_pit_interior_wide_non_euclidean_1775013502076.png", ("TL", "THE SORTING FLOOR. NON-EUCLIDEAN DEPTH. THE CASES STRETCH INTO INFINITY.")),
    ("09_stan.jpg", "abyssal_ep1_page_2_panel_2_stans_vibrating_aura_veteran_carrier_1775013521259.png", ("BR", "CARRIER STAN. TABLE 1 VETERAN. HIS 64-WRAPS VIBRATE AT GRIEVANCE FREQUENCY.")),
    ("10_strike.jpg", "abyssal_ep1_page_2_panel_3_stan_boot_shadow_strike_impact_1775013538296.png", ("TL", "SHADOW SEVERANCE INITIATED. ARTICLE 14, CLAUSE 3: CIVILIAN EGO TERMINATED.")),
    ("11_severance.jpg", "abyssal_ep1_page_2_panel_4_kips_shadow_thrashing_ink_bleeding_horror_anatomy_screaming_kip_1775013560576.png", ("BR", "THE SHADOW THRASHES. THE ABYSS TASTES THE INITIATE FOR THE FIRST TIME.")),
    ("12_chuck.jpg", "abyssal_ep1_page_3_panel_1_chucks_towering_monster_shadow_crate_silhouette_multi_eyed_horror_1775013579067.png", ("TL", "MGR CHUCK. CONTROL-CLASS. HIS SHADOW HAS MORE EYES THAN HIS BUDGET HAS CUTS.")),
    ("13_mdd.jpg", "abyssal_ep1_page_3_panel_2_mdd_beep_stationary_event_alert_polished_v2_1775013663407.png", ("BR", "STATIONARY EVENT DETECTED. THE ALGORITHM DEMANDS MOMENTUM.")),
    ("14_crush.jpg", "abyssal_ep1_page_3_panel_3_gravity_crush_kip_pinned_linoleum_cracking_badge_texture_1775013680343.png", ("TL", "THE WEIGHT OF S.P.M. SCORES. KIP IS PINNED BY THE GRAVITY OF FAILURE.")),
    ("15_nixie.jpg", "abyssal_ep1_page_3_panel_4_nixie_phantom_sludge_emergence_mangled_paper_horror_polished_v2_1775013697449.png", ("BR", "NIXIE PHANTOM EMERGENCE. BORN FROM THE SLUDGE OF UNCLAIMED SOULS.")),
    ("16_pre_strike.jpg", "abyssal_ep1_stan_pre_strike_stance_1571_denial_1775017138708.png", ("TL", "STAN INVOKES 1571 ABSOLUTION. DENIED.")),
    ("17_climax.jpg", "abyssal_episode_1_page_4_splash_stan_strike_1775012700676.png", ("TL", "THE ANCHOR STRIKE. GRIEVANCE MANA AT MAXIMUM LOAD.")),
    ("18_aftermath.jpg", "abyssal_ep1_pdf_page_21_aftermath_llv_graveyard_stan_kip_walking_high_fidelity_1775017416191_1775015334523_1775016063504.png", ("BR", "THE FLOOR IS CLEAR. FOR NOW. WELCOME TO THE ABYSS, INITIATE.")),
    ("20_dossier_kip.jpg", "abyssal_dossier_61094_kip_baxter_redacted_high_fidelity_v2_1775017416186_1775015056679.png", None),
    ("22_blueprint.jpg", "abyssal_mdd_scanner_blueprint_schematic_high_fidelity_v2_1775017416187_1775015074586.png", None),
]

def draw_caption(img, placement, text):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = max(28, int(h * 0.025))
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    pad = 20
    max_text_w = int(w * 0.40)
    words = text.split()
    lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try:
            tw = font.getlength(test)
        except:
            tw = len(test) * font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    line_h = font_size + 10
    actual_max_w = 0
    for line in lines:
        try: lw = font.getlength(line)
        except: lw = len(line) * font_size * 0.6
        if lw > actual_max_w: actual_max_w = lw
    box_w = int(actual_max_w) + pad * 2
    box_h = len(lines) * line_h + pad * 2
    if placement == "TL":
        x, y = int(w * 0.03), int(h * 0.03)
    else:
        x, y = int(w - box_w - w * 0.03), int(h - box_h - h * 0.03)
    draw.rectangle([x, y, x + box_w, y + box_h], fill="#FFFF00", outline="#000000", width=4)
    for i, line in enumerate(lines):
        draw.text((x + pad, y + pad + i * line_h), line, fill="#000000", font=font)
    return img

def main():
    os.makedirs(WEB_DIR, exist_ok=True)
    total = len(PANELS) + 1
    for i, (out_name, src_name, caption) in enumerate(PANELS):
        pct = int(100 * (i + 1) / total)
        bar = "█" * (pct // 5) + "░" * (20 - pct // 5)
        src = os.path.join(ARCHIVE, src_name)
        dst = os.path.join(WEB_DIR, out_name)
        if not os.path.exists(src):
            print(f"  [{bar}] {pct:3d}% | ⚠ Missing: {src_name}")
            continue
        img = Image.open(src).convert("RGB")
        if caption:
            img = draw_caption(img, caption[0], caption[1])
        img.save(dst, quality=90)
        img.close()
        print(f"  [{bar}] {pct:3d}% | {out_name}")

    # Copy PDF for download
    if os.path.exists(PDF_SRC):
        shutil.copy2(PDF_SRC, os.path.join(WEB_DIR, "Mailstorm_Ep1_Abyssal_Edition.pdf"))
        print(f"  [████████████████████] 100% | PDF copied for download")

    print("\n--- WEB ASSETS READY ---")

if __name__ == "__main__":
    main()
