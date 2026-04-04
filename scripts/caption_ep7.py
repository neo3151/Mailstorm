import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont

ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
DEST_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics\episode_7"

os.makedirs(DEST_DIR, exist_ok=True)

# Find the exact files
def get_latest(prefix):
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

panels = [
    {
        "src": get_latest("ep7_01_incubation"),
        "dst": "01_incubation.jpg",
        "caption": "You carry the weight long enough, and the concrete starts to whisper. It promises you a clipboard. It promises you'll never have to walk in the rain again.",
        "sub": "THE COST IS MERELY YOUR ALLEGIANCE."
    },
    {
        "src": get_latest("ep7_02_host_chosen_safe"),
        "dst": "02_host_chosen.jpg",
        "caption": "The 204b Parasite does not kill the host. It merely digests the solidarity, making room for Pure Metrics.",
        "sub": "\"UNAUTHORIZED STATIONARY EVENT DETECTED.\""
    },
    {
        "src": get_latest("ep7_03_guest_star"),
        "dst": "03_guest_star.jpg",
        "caption": "The Algorithm demands constant movement. But the Old Guard knows exactly how to freeze the clock.",
        "sub": "THE CHAIRMAN HAS TAKEN HIS SEAT."
    },
    {
        "src": get_latest("ep7_04_metric_assault"),
        "dst": "04_metric_assault.jpg",
        "caption": "The 204b Parasite feeds on fear and movement. It cannot process a man perfectly willing to sit in the cold forever.",
        "sub": "\"I am once again asking you to respect the Master Contract.\""
    },
    {
        "src": get_latest("ep7_05_aftermath"),
        "dst": "05_aftermath.jpg",
        "caption": "The Supervisor's metrics were shattered by the Filibuster. The Parasite retreated to the shadows, starved of authority.",
        "sub": "THE 1% CANNOT BREAK THE STEWARD."
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
