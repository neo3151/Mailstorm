import os
import shutil
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
DEST_DIR = r"c:\Users\neo31\Mailstorm\web\public\comics\episode_3"

os.makedirs(DEST_DIR, exist_ok=True)

panels = [
    {
        "src": "ep3_01_ziggurat_1775050669843.png",
        "dst": "01_ziggurat.jpg",
        "caption": "ROUTE 42 IS VACANT. THE ALGORITHM KNOWS THE TERRAIN.",
        "pos": "TL"
    },
    {
        "src": "ep3_02_foreign_soil_1775050684256.png",
        "dst": "02_foreign_soil.jpg",
        "caption": "FOREIGN SOIL DEBUFF. THE STREET WARPS AND STRETCHES INTO INFINITY.",
        "pos": "BR"
    },
    {
        "src": "ep3_03_porch_trap_1775050699924.png",
        "dst": "03_porch_trap.jpg",
        "caption": "THE SCREEN DOOR GAMBIT. RAW CONCRETE SEALS THE WAY OUT.",
        "pos": "BL"
    },
    {
        "src": "ep3_04_apathy_1775050714216.png",
        "dst": "04_apathy.jpg",
        "caption": "CUSTOMER ARMOR ENGAGED. TOTAL APATHY SHATTERS THE ILLUSION.",
        "pos": "TR"
    },
    {
        "src": "ep3_05_dlo_1775050730369.png",
        "dst": "05_dlo.jpg",
        "caption": "THE DROP IS MADE. BUT AN UNREGISTERED DEAD LETTER ESCAPES THE PIVOT.",
        "pos": "BR"
    }
]

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
    elif placement == "TR": x, y = int(w-box_w-w*0.03), int(h*0.03)
    elif placement == "BL": x, y = int(w*0.03), int(h-box_h-h*0.03)
    else: x, y = int(w-box_w-w*0.03), int(h-box_h-h*0.03) # BR
    
    draw.rectangle([x,y,x+box_w,y+box_h], fill="#FFFF00", outline="#000000", width=4)
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#000000", font=font)
    return img

for p in panels:
    src_path = os.path.join(SRC_DIR, p["src"])
    dst_path = os.path.join(DEST_DIR, p["dst"])
    if os.path.exists(src_path):
        img = Image.open(src_path).convert("RGB")
        img = draw_caption(img, p["pos"], p["caption"])
        img.save(dst_path, quality=95)
        print(f"Generated {dst_path}")
    else:
        print(f"MISSING: {src_path}")
