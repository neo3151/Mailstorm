import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
DEST_DIR = r"c:\Users\neo31\Mailstorm\web\public\comics\episode_5"

os.makedirs(DEST_DIR, exist_ok=True)

panels = [
    {
        "src": "ep5_01_descent_1775060681635.png",
        "dst": "01_descent.jpg",
        "caption": "THE DEEP BASEMENT. THE DEAD LETTER OFFICE CATACOMBS.",
        "pos": "BL"
    },
    {
        "src": "ep5_02_swarm_1775060697314.png",
        "dst": "02_swarm.jpg",
        "caption": "THE UNDELIVERABLES. RAGE CALCIFIED INTO A SWARM OF CARDBOARD.",
        "pos": "BC"
    },
    {
        "src": "ep5_03_heather_1775060711080.png",
        "dst": "03_heather.jpg",
        "caption": "MACHINE COMMUNION. APWU CLERKS IMPOSE ORDER ON CHAOS.",
        "pos": "BL"
    },
    {
        "src": "ep5_04_override_1775060726596.png",
        "dst": "04_override.jpg",
        "caption": "IMDAS OVERRIDE INITIATED. BRUTE COM-FORCE APPLIED TO THE WAX.",
        "pos": "BR"
    },
    {
        "src": "ep5_05_coordinates_1775060740559.png",
        "dst": "05_coordinates.jpg",
        "caption": "THE SOLIDARITY MANDATE UNLOCKED. DESTINATION SET. THE ENDGAME BEGINS.",
        "pos": "BC"
    }
]

def draw_caption(img, placement, text):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = max(28, int(h * 0.025))
    try: font = ImageFont.truetype("arialbd.ttf", font_size)
    except: font = ImageFont.load_default()
    
    pad = 20
    max_text_w = int(w * 0.55)
    
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try: tw = font.getlength(test)
        except: tw = len(test) * font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    
    line_h = font_size + 10
    actual_max_w = max((font.getlength(l) for l in lines), default=100)
    box_w = int(actual_max_w) + pad * 2
    box_h = len(lines) * line_h + pad * 2
    
    if placement == "TL": x, y = int(w*0.03), int(h*0.03)
    elif placement == "TR": x, y = int(w-box_w-w*0.03), int(h*0.03)
    elif placement == "BL": x, y = int(w*0.03), int(h-box_h-h*0.03)
    elif placement == "BC": x, y = int(w/2 - box_w/2), int(h-box_h-h*0.03)
    else: x, y = int(w-box_w-w*0.03), int(h-box_h-h*0.03) # BR
    
    # APWU Black with Neon Green Text (Cyberpunk Terminal Style)
    draw.rectangle([x, y, x+box_w, y+box_h], fill="#000000", outline="#00ff00", width=4)
    
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#00ff00", font=font)
        
    return img

if __name__ == "__main__":
    total = len(panels)
    for idx, p in enumerate(panels):
        src_path = os.path.join(SRC_DIR, p["src"])
        dst_path = os.path.join(DEST_DIR, p["dst"])
        if os.path.exists(src_path):
            try:
                img = Image.open(src_path).convert("RGB")
                img = draw_caption(img, p["pos"], p["caption"])
                img.save(dst_path, quality=95)
                # Calculate progress
                prog = int(((idx + 1) / total) * 10)
                bar = "[" + "█" * prog + "░" * (10 - prog) + f"] {int(((idx+1)/total)*100)}% | {idx+1}/{total} done"
                print(f"{bar} -> Generated {dst_path}")
            except Exception as e:
                print(f"Failed to process {src_path}: {e}")
        else:
            print(f"MISSING: {src_path}")
