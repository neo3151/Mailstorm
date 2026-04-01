import os
import glob
from PIL import Image

# Setup Directories
ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\199c2678-ad5a-46f7-b609-dafe6434baad"
COMICS_DIR = r"C:\Users\neo31\Mailstorm\web\public\comics"
OUT_PDF = r"C:\Users\neo31\Mailstorm\web\public\downloads\Mailstorm_Vol1_Storybook.pdf"
os.makedirs(r"C:\Users\neo31\Mailstorm\web\public\downloads", exist_ok=True)

# Find Covers (using the new textless front cover)
front_covers = sorted(glob.glob(os.path.join(ARTIFACT_DIR, "vol1_front_cover_notext_*.png")), reverse=True)
back_covers = sorted(glob.glob(os.path.join(ARTIFACT_DIR, "vol1_back_cover_*.png")), reverse=True)

# Episode Data exactly mirroring the Website to prevent legacy files
EPISODE_DATA = {
  1: ["01_cover.jpg","05_monolith.jpg","06_kips_hands.jpg","07_doors.jpg",
      "08_pit.jpg","09_stan.jpg","10_strike.jpg","11_severance.jpg",
      "12_chuck.jpg","13_mdd.jpg","14_crush.jpg","15_nixie.jpg",
      "16_pre_strike.jpg","17_climax.jpg","18_aftermath.jpg",
      "20_dossier_kip.jpg","22_blueprint.jpg"],
  2: ["01_cover.jpg","02_assignment.jpg","03_shadow_grin.jpg",
      "04_llv_depart.jpg","05_bone_burn.jpg","06_xray.jpg",
      "07_satchel.jpg","08_swarm.jpg","09_heather.jpg",
      "10_aegis.jpg","11_shatter.jpg","12_awe.jpg",
      "13_sunset.jpg","14_hands.jpg","15_resolution.jpg"],
  3: ["01_ziggurat.jpg","02_foreign_soil.jpg","03_porch_trap.jpg","04_apathy.jpg","05_dlo.jpg"],
  4: ["01_snare.jpg","02_interrogation.jpg","03_summon.jpg","04_cathedral.jpg","05_spite.jpg"],
  5: ["01_descent.jpg","02_swarm.jpg","03_heather.jpg","04_override.jpg","05_coordinates.jpg"]
}

images_to_compile = []

def load_and_resize(path, target_size=(1024, 1536)):
    im = Image.open(path).convert('RGB')
    if im.size != target_size:
        im = im.resize(target_size, Image.Resampling.LANCZOS)
    return im

print(">>> Compiling Volume 1 Storybook...")

# Add Front Cover (without any text overlays)
if front_covers:
    print("Loading textless Front Cover...")
    fc_img = load_and_resize(front_covers[0])
    images_to_compile.append(fc_img)

# Loop Episodes using exact arrays
for ep_num in range(1, 6):
    print(f"Processing Episode {ep_num}...")
    ep_dir = os.path.join(COMICS_DIR, f"episode_{ep_num}")
    for p_name in EPISODE_DATA[ep_num]:
        p_path = os.path.join(ep_dir, p_name)
        if os.path.exists(p_path):
            images_to_compile.append(load_and_resize(p_path))
        else:
            print(f"  WARNING: Missing {p_path}")

# Add Back Cover
if back_covers:
    print("Loading Back Cover...")
    images_to_compile.append(load_and_resize(back_covers[0]))

# Save PDF
if images_to_compile:
    print(f"Stitching {len(images_to_compile)} pages into PDF...")
    images_to_compile[0].save(
        OUT_PDF, 
        "PDF",
        resolution=100.0, 
        save_all=True, 
        append_images=images_to_compile[1:]
    )
    print(f"SUCCESS! Rendered Volume 1 to: {OUT_PDF}")
else:
    print("ERROR: No images found.")
