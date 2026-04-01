import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
DEST_DIR = r"c:\Users\neo31\Mailstorm\web\public\comics\specials\sp2"

os.makedirs(DEST_DIR, exist_ok=True)

panels = [
    {
        "src": "sp2_01_swarm_1775071784789.png",
        "dst": "01_swarm.jpg",
        "caption": "PRIME DAY DEBUFF ACTIVATED. THE VOLUME HAS BECOME SENTIENT.",
        "pos": "BC"
    },
    {
        "src": "sp2_02_breach_1775071800738.png",
        "dst": "02_breach.jpg",
        "caption": "NO SCAN FOR THIS STOP. SURVIVAL IS THE ONLY METRIC.",
        "pos": "BC"
    },
    {
        "src": "sp2_03_dogspray_1775071814858.png",
        "dst": "03_dogspray.jpg",
        "caption": "STANDARD ISSUE DEFENSIVE INCENDIARY DEPLOYED.",
        "pos": "BC"
    },
    {
        "src": "sp2_04_tubshield_1775071830207.png",
        "dst": "04_tubshield.jpg",
        "caption": "HEAVY BLUNT TRAUMA SUSTAINED. THE PARCEL MUST BE ENDED.",
        "pos": "BC"
    },
    {
        "src": "sp2_05_survivor_1775071843374.png",
        "dst": "05_survivor.jpg",
        "caption": "THE ROUTE REMAINS OPEN. THE ENDLESS CARNAGE CONTINUES TUESDAY.",
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
    max_text_w = int(w * 0.70)
    
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
    
    # Expand canvas downwards by box_h
    # Grindhouse theme: pure black background
    new_img = Image.new("RGB", (w, h + box_h), "#000000")
    new_img.paste(img, (0, 0))
    draw = ImageDraw.Draw(new_img)
    
    # Center text in the new bottom strip
    x = int(w/2 - box_w/2)
    y = h
    
    # Grindhouse text: Hazard Yellow overlay text on the black banner
    for i, line in enumerate(lines):
        draw.text((x+pad, y+pad+i*line_h), line, fill="#ffcc00", font=font)
        
    return new_img

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
