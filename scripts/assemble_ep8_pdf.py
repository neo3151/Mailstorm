import os
import sys
import glob
import logging
from PIL import Image, ImageDraw, ImageFont
from fpdf import FPDF

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

OUTPUT_FILE = r"C:\Users\neo31\Mailstorm\releases\Mailstorm_Ep8_Abyssal_Edition.pdf"
ARCHIVE_LOCAL = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
ARCHIVE_SHARED = r"C:\Users\neo31\.gemini\antigravity\brain\d01fdf8d-e4ea-4465-a618-0d2ad8e90864"

def get_latest(archive, prefix):
    files = sorted(glob.glob(os.path.join(archive, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

COVER = get_latest(ARCHIVE_LOCAL, "ep8_cover_hazard_orange")
STORY_PANELS = [
    get_latest(ARCHIVE_LOCAL, "ep8_01_prime_tsunami"),
    get_latest(ARCHIVE_LOCAL, "ep8_02_joust"),
    get_latest(ARCHIVE_LOCAL, "ep8_03_bombardment"),
    get_latest(ARCHIVE_LOCAL, "ep8_04_drift"),
    get_latest(ARCHIVE_LOCAL, "ep8_05_dock_slam"),
]

DOSSIER_HANDLER = get_latest(ARCHIVE_LOCAL, "ep8_dossier_handler")
BLUEPRINT = os.path.join(ARCHIVE_SHARED, "abyssal_mdd_scanner_blueprint_schematic_high_fidelity_v2_1775017416187_1775015074586.png")
BACK_COVER = os.path.join(ARCHIVE_SHARED, "abyssal_ep1_pdf_page_32_back_cover_monolithic_logo_high_fidelity_v2_1775017416194_1775015334526_1775016120479.png")

CAPTIONS = {
    0:  ("TL", "THE ALGORITHM WEAPONIZES VOLUME. THE BREACH ON DOCK 42."),
    1:  ("BR", "THE IRON LIFTERS BREAK THE LINE. KINETIC FORCE DEMANDED."),
    2:  ("TL", "LOCALIZED ORBITAL STRIKE. SOUND BARRIERS SHATTER."),
    3:  ("BR", "PROPANE AND RUBBER JUMPSTART THE TOUR 1 CAVALRY."),
    4:  ("TL", "THE DOCK SLAM. THE BREACH IS SEALED. THE LIFTERS HOLD THE LINE."),
}

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
    if not filepath or not os.path.exists(filepath):
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
    pdf.set_title("Mailstorm: Episode 8 - The Iron Lifters (Abyssal Edition)")
    pdf.set_author("The Department of Logistics")
    total, done = 11, 0
    def prog(label):
        nonlocal done; done += 1
        filled = int(20*done/total)
        print(f"  [{'█'*filled}{'░'*(20-filled)}] {int(100*done/total):3d}% | {done}/{total} | {label}")

    print("--- ASSEMBLING EPISODE 8 ABYSSAL EDITION ---")
    add_img(pdf, COVER); prog("Cover Image")
    black_page(pdf, "KINETIC FORCE IS THE ONLY CURRENCY HERE."); prog("Inside Front")
    black_page(pdf, ""); prog("Title Blank")

    for i, panel in enumerate(STORY_PANELS):
        add_img(pdf, panel, CAPTIONS.get(i))
        prog(f"Panel {i+1:02d}")

    black_page(pdf, "SOUND BARRIERS SHATTER ON THE NIGHT SHIFT."); prog("Epilogue Blank")
    
    add_img(pdf, DOSSIER_HANDLER); prog("Dossier: The Iron Lifter")
    add_img(pdf, BLUEPRINT); prog("Shared Schematic: MDD")
    add_img(pdf, BACK_COVER); prog("Back Cover")

    pdf.output(OUTPUT_FILE)
    print(f"\n--- ASSEMBLY COMPLETE: {OUTPUT_FILE} ---")

if __name__ == "__main__":
    try: assemble()
    except Exception as e:
        import traceback; print(f"Error: {e}"); traceback.print_exc()
