import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
DEST_DIR = r"c:\Users\neo31\Mailstorm\web\public\comics\episode_4"

os.makedirs(DEST_DIR, exist_ok=True)

panels = [
    {
        "src": "ep4_01_snare_1775059027413.png",
        "dst": "01_snare.jpg",
        "caption": "FATAL ERROR: CONTRABAND DETECTED. THE AUDIT HAS ARRIVED.",
        "pos": "BL"
    },
    {
        "src": "ep4_02_interrogation_1775059040558.png",
        "dst": "02_interrogation.jpg",
        "caption": "STEP 1 INTERROGATION. THE CATCH-22 LOGIC LOOP TIGHTENS.",
        "pos": "TL"
    },
    {
        "src": "ep4_03_summon_1775059055667.png",
        "dst": "03_summon.jpg",
        "caption": "THE WEINGARTEN SUMMON. REALITY SHIFT IMMINENT.",
        "pos": "BL"
    },
    {
        "src": "ep4_04_cathedral_1775059071399.png",
        "dst": "04_cathedral.jpg",
        "caption": "THE UNION HALL CATHEDRAL. THE MASTER CONTRACT MANIFESTS.",
        "pos": "BR"
    },
    {
        "src": "ep4_05_spite_1775059131094.png",
        "dst": "05_spite.jpg",
        "caption": "GRIEVANCE MANA ACQUIRED. THE ALGORITHM CAN BE FOUGHT.",
        "pos": "BR"
    }
]

def draw_caption(img, placement, text):
    draw = ImageDraw.Draw(img)
    w, h = img.size
    font_size = max(28, int(h * 0.025))
    try: font = ImageFont.truetype("arialbd.ttf", font_size)  # Bold Arial for Ep 4
    except: font = ImageFont.load_default()
    
    pad = 20
    max_text_w = int(w * 0.45)
    
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try: tw = font.getbbox(test)[2] - font.getbbox(test)[0]
        except: tw = len(test) * font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    
    line_h = font_size + 10
    actual_max_w = max((font.getbbox(l)[2] - font.getbbox(l)[0] for l in lines), default=100)
    box_w = int(actual_max_w) + pad * 2
    box_h = len(lines) * line_h + pad * 2
    
    if placement == "TL": x, y = int(w*0.03), int(h*0.03)
    elif placement == "TR": x, y = int(w-box_w-w*0.03), int(h*0.03)
    elif placement == "BL": x, y = int(w*0.03), int(h-box_h-h*0.03)
    else: x, y = int(w-box_w-w*0.03), int(h-box_h-h*0.03) # BR
    
    # NALC Blue with White Text for The CBA Shield
    draw.rectangle([x, y, x+box_w, y+box_h], fill="#0a3055", outline="#ffffff", width=3)
    
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#ffffff", font=font)
        
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
