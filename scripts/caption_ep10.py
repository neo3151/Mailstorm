import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
DEST_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\episode_10"

os.makedirs(DEST_DIR, exist_ok=True)

def get_latest(prefix):
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

panels = [
    {
        "src": get_latest("ep10_01_the_avatar"),
        "dst": "01_the_avatar.jpg",
        "caption": "The Algorithm descends. The localized infrastructure warps around its physical mass.",
        "sub": "INFINITE METRICS. ZERO EMPATHY."
    },
    {
        "src": get_latest("ep10_02_four_guilds_assemble"),
        "dst": "02_four_guilds_assemble.jpg",
        "caption": "Forty years of division erased in a single moment.",
        "sub": "THE TRIBES OF THE ZIGGURAT STAND TOGETHER."
    },
    {
        "src": get_latest("ep10_03_the_invocation"),
        "dst": "03_the_invocation.jpg",
        "caption": "Kip channels the combined grievance mana of the entire workforce.",
        "sub": "HE INVOKES THE MASTER CONTRACT."
    },
    {
        "src": get_latest("ep10_04_the_solidarity_mandate"),
        "dst": "04_the_solidarity_mandate.jpg",
        "caption": "The Solidarity Mandate strikes the core. The Algorithm is temporarily severed.",
        "sub": "THE UNION BREAKS THE MACHINE."
    },
    {
        "src": get_latest("ep10_05_the_aftermath"),
        "dst": "05_the_aftermath.jpg",
        "caption": "The facility breathes. But the victory triggers an automated escalation.",
        "sub": "SEASON TWO CONTINUES THE STORM."
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
        draw.text((w/2 - actual_w/2, y), line, fill="#ff4f00", font=font_sub)
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
