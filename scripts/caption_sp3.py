import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
DEST_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\specials\sp3"

os.makedirs(DEST_DIR, exist_ok=True)

def get_latest(prefix):
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

panels = [
    {
        "src": get_latest("sp3_01_the_ascent"),
        "dst": "01_the_ascent.jpg",
        "caption": "High above the frozen trenches, the air is perfectly climate-controlled.",
        "sub": "THE UPPER MANAGEMENT STRATOSPHERE."
    },
    {
        "src": get_latest("sp3_02_the_ballroom"),
        "dst": "02_the_ballroom.jpg",
        "caption": "The District Managers gather to celebrate the quarterly metrics.",
        "sub": "DECADENCE FORGED FROM STOLEN WAGES."
    },
    {
        "src": get_latest("sp3_03_the_bishops"),
        "dst": "03_the_bishops.jpg",
        "caption": "The Algorithm's clerics observe quietly. They do not drink. They only calculate.",
        "sub": "METRICS MADE MANIFEST."
    },
    {
        "src": get_latest("sp3_04_the_toast"),
        "dst": "04_the_toast.jpg",
        "caption": "The toast of the 'Distilled Undeliverables.' The liquefied life essence of crushed route evaluations.",
        "sub": "SIP THE GRIEVANCE MANA. TASTE THE APATHY."
    },
    {
        "src": get_latest("sp3_05_the_contract_shredder"),
        "dst": "05_the_contract_shredder.jpg",
        "caption": "The ritual completes. A thousand carrier evaluations are sacrificed to sustain their immortality.",
        "sub": "PRAY YOU NEVER RECEIVE AN INVITATION."
    }
]

def draw_caption(img, caption, sub):
    w, h = img.size
    font_size = 32
    sub_font_size = 28
    try: 
        font = ImageFont.truetype("arial.ttf", font_size)
    except: font = ImageFont.load_default()
    try:
        font_sub = ImageFont.truetype("arialbd.ttf", sub_font_size)
    except:
        font_sub = ImageFont.load_default()
        
    pad = 20
    max_text_w = int(w * 0.85)
    
    words = caption.split()
    cap_lines, current = [], ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try: tw = font.getbbox(test)[2] - font.getbbox(test)[0]
        except: tw = len(test) * font_size * 0.6
        if tw <= max_text_w: current = test
        else:
            if current: cap_lines.append(current)
            current = word
    if current: cap_lines.append(current)

    words_sub = sub.split()
    sub_lines, current = [], ""
    for word in words_sub:
        test = f"{current} {word}".strip() if current else word
        try: tw = font_sub.getbbox(test)[2] - font_sub.getbbox(test)[0]
        except: tw = len(test) * sub_font_size * 0.6
        if tw <= max_text_w: current = test
        else:
            if current: sub_lines.append(current)
            current = word
    if current: sub_lines.append(current)
    
    cap_h = len(cap_lines) * (font_size + 10)
    sub_h = len(sub_lines) * (sub_font_size + 10)
    total_box_h = pad + cap_h + (pad if sub_lines else 0) + sub_h + pad
    
    new_img = Image.new("RGB", (w, h + total_box_h), "#050505")
    new_img.paste(img, (0, 0))
    draw = ImageDraw.Draw(new_img)
    
    y = h + pad
    for line in cap_lines:
        try: actual_w = font.getbbox(line)[2] - font.getbbox(line)[0]
        except: actual_w = len(line) * font_size * 0.6
        draw.text((w/2 - actual_w/2, y), line, fill="#d4d0c8", font=font)
        y += font_size + 10
    y += 10
    for line in sub_lines:
        try: actual_w = font_sub.getbbox(line)[2] - font_sub.getbbox(line)[0]
        except: actual_w = len(line) * sub_font_size * 0.6
        draw.text((w/2 - actual_w/2, y), line, fill="#ff00ff", font=font_sub) # magenta color for specials
        y += sub_font_size + 10
    return new_img

if __name__ == "__main__":
    total = len(panels)
    for idx, p in enumerate(panels):
        src_path = p["src"]
        dst_path = os.path.join(DEST_DIR, p["dst"])
        if src_path and os.path.exists(src_path):
            try:
                img = Image.open(src_path).convert("RGB")
                img = draw_caption(img, p["caption"], p["sub"])
                img.save(dst_path, quality=95)
                prog = int(((idx + 1) / total) * 10)
                bar = "[" + "█" * prog + "░" * (10 - prog) + f"] {int(((idx+1)/total)*100)}% | {idx+1}/{total} done"
                print(f"{bar} -> Generated {dst_path}")
            except Exception as e:
                print(f"Failed to process {src_path}: {e}")
        else:
            print(f"MISSING OR INVALID SOURCE FOR: {p['dst']}")
