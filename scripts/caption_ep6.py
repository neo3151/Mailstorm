import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
DEST_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\episode_6"

os.makedirs(DEST_DIR, exist_ok=True)

# Find the exact files
def get_latest(prefix):
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

panels = [
    {
        "src": get_latest("ep6_01_edge"),
        "dst": "01_edge.jpg",
        "caption": "You can't walk forever. Eventually, the Article 8 safety grid breaks, and the concrete bleeds out into the Evaluation Sea.",
        "sub": "WELCOME TO THE RURAL ROUTE."
    },
    {
        "src": get_latest("ep6_02_ranger"),
        "dst": "02_ranger.jpg",
        "caption": "Out here, there is no Union Hall shield. The NRLCA operates completely exposed.",
        "sub": "\"Get in the rig, City Boy! The Algorithm is clocking us!\""
    },
    {
        "src": get_latest("ep6_03_sentinel"),
        "dst": "03_sentinel.jpg",
        "caption": "The hazards don't wait on street corners anymore. They grow directly out of the overgrown fields.",
        "sub": "THE MAILBOX SENTINELS DEMAND VOLUME."
    },
    {
        "src": get_latest("ep6_04_blitz"),
        "dst": "04_blitz.jpg",
        "caption": "Their magic isn't endurance—it's sheer, reckless momentum. The Evaluation Blitz.",
        "sub": "\"Brace for impact! I'm popping the Tub-Shield!\""
    },
    {
        "src": get_latest("ep6_05_truce"),
        "dst": "05_truce.jpg",
        "caption": "We survived the blitz. The lone wolves officially acknowledged the NALC.",
        "sub": "THE RURAL ALLIANCE HAS BEEN FORGED."
    }
]

def draw_caption(img, caption, sub):
    w, h = img.size
    
    # Fonts
    font_size = 32
    sub_font_size = 28
    try: 
        font = ImageFont.truetype("arial.ttf", font_size)
        font_sub = ImageFont.truetype("arialbd.ttf", sub_font_size)
    except: 
        font = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        
    pad = 20
    max_text_w = int(w * 0.85)
    
    # Process Caption Lines
    words = caption.split()
    cap_lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip() if current else word
        try: tw = font.getbbox(test)[2] - font.getbbox(test)[0]
        except: tw = len(test) * font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current: cap_lines.append(current)
            current = word
    if current: cap_lines.append(current)

    # Process Sub Lines
    words_sub = sub.split()
    sub_lines = []
    current = ""
    for word in words_sub:
        test = f"{current} {word}".strip() if current else word
        try: tw = font_sub.getbbox(test)[2] - font_sub.getbbox(test)[0]
        except: tw = len(test) * sub_font_size * 0.6
        if tw <= max_text_w:
            current = test
        else:
            if current: sub_lines.append(current)
            current = word
    if current: sub_lines.append(current)
    
    cap_h = len(cap_lines) * (font_size + 10)
    sub_h = len(sub_lines) * (sub_font_size + 10)
    
    total_box_h = pad + cap_h + (pad if sub_lines else 0) + sub_h + pad
    
    # Expand canvas downwards by total_box_h
    new_img = Image.new("RGB", (w, h + total_box_h), "#050505")
    new_img.paste(img, (0, 0))
    draw = ImageDraw.Draw(new_img)
    
    y = h + pad
    
    # Draw Caption
    for line in cap_lines:
        actual_w = font.getbbox(line)[2] - font.getbbox(line)[0]
        x = int(w/2 - actual_w/2)
        draw.text((x, y), line, fill="#d4d0c8", font=font)
        y += font_size + 10
        
    y += 10 # gap
    
    # Draw Sub
    for line in sub_lines:
        actual_w = font_sub.getbbox(line)[2] - font_sub.getbbox(line)[0]
        x = int(w/2 - actual_w/2)
        draw.text((x, y), line, fill="#ff4f00", font=font_sub) # Abyssal Orange
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
                # Calculate progress
                prog = int(((idx + 1) / total) * 10)
                bar = "[" + "█" * prog + "░" * (10 - prog) + f"] {int(((idx+1)/total)*100)}% | {idx+1}/{total} done"
                print(f"{bar} -> Generated {dst_path}")
            except Exception as e:
                print(f"Failed to process {src_path}: {e}")
        else:
            print(f"MISSING OR INVALID SOURCE FOR: {p['dst']}")
