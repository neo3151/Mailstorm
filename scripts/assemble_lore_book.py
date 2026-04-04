import os
import glob
import re
from fpdf import FPDF
from PIL import Image

# Configuration
LORE_DIR = r"C:\Users\neo31\Mailstorm\docs\lore"
ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
OUTPUT_FILE = r"C:\Users\neo31\Mailstorm\releases\The_Book_of_Mailstorm_Vol1.pdf"

# Find latest images
def get_latest(prefix):
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, f"{prefix}_*.png")), reverse=True)
    return files[0] if files else None

IMAGES = {
    "COVER_FRONT": get_latest("book_cover_front"),
    "CH1": get_latest("book_chapter_1"),
    "CH2": get_latest("book_chapter_2"),
    "CH3": get_latest("book_chapter_3"),
    "CH4": get_latest("book_chapter_4"),
    "CH5": get_latest("book_chapter_5"),
    "COVER_BACK": get_latest("book_cover_back"),
    "TEXTURE": get_latest("book_asset_sidebar_texture")
}

PARTS = [
    {"title": "PART I: THE UNIVERSE & HIERARCHY", "img": IMAGES["CH1"], "files": ["universe_architecture.md", "THE_HIERARCHY.md", "THE_ROUTE_TOPOLOGY.md"]},
    {"title": "PART II: THE FACTIONS & THE PEOPLE", "img": IMAGES["CH2"], "files": ["THE_FACTIONS.md", "characters.md"]},
    {"title": "PART III: THE MAGIC & THE LAW", "img": IMAGES["CH3"], "files": ["THE_MASTER_CONTRACT.md", "THE_CORE_MECHANICS.md", "THE_CONTRACT.md", "THE_FORBIDDEN_FORMS.md"]},
    {"title": "PART IV: SURVIVAL & HAZARDS", "img": IMAGES["CH4"], "files": ["THE_METRICS_CAGE.md", "THE_DAILY_GRIND.md", "THE_WORKPLACE.md", "THE_BESTIARY.md"]},
    {"title": "PART V: THE CHRONICLES & THE FUTURE", "img": IMAGES["CH5"], "files": ["THE_CHRONICLE.md", "SEASON_2_BIBLE.md"]}
]

class LorePDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def clean_text(text):
    text = text.replace("**", "").replace("__", "")
    text = text.encode('latin-1', 'replace').decode('latin-1')
    return text

def draw_content(pdf, pass_num, toc_data):
    # Cover
    if IMAGES["COVER_FRONT"]:
        pdf.add_page()
        pdf.image(IMAGES["COVER_FRONT"], 0, 0, 210, 297)

    # TOC
    if pass_num == 2:
        pdf.add_page()
        pdf.set_fill_color(20, 20, 20)
        pdf.rect(0,0,210,297,"F")
        pdf.set_text_color(255, 100, 0)
        pdf.set_font("helvetica", "B", 24)
        pdf.cell(0, 20, "TABLE OF CONTENTS", ln=1, align="C")
        pdf.ln(10)
        pdf.set_font("helvetica", "", 14)
        pdf.set_text_color(220, 220, 220)
        for entry in toc_data:
            pdf.cell(150, 10, entry["title"], ln=0)
            pdf.cell(30, 10, str(entry["page"]), ln=1, align="R")

    for part in PARTS:
        if pass_num == 1:
            toc_data.append({"title": part["title"], "page": pdf.page_no() + 1})
            
        if part["img"] and pass_num == 2:
            pdf.add_page()
            pdf.image(part["img"], 0, 0, 210, 297)
        else:
            pdf.add_page()
            pdf.set_fill_color(0, 0, 0)
            pdf.rect(0,0,210,297,"F")
        
        pdf.add_page()
        for filename in part["files"]:
            filepath = os.path.join(LORE_DIR, filename)
            if not os.path.exists(filepath):
                filepath = os.path.join(ARTIFACT_DIR, filename)
                if not os.path.exists(filepath):
                    continue

            pdf.set_fill_color(20, 20, 20)
            pdf.rect(0,0,210,297,"F")
            
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            pdf.set_text_color(220, 220, 220)
            for line in lines:
                line = line.strip()
                if not line:
                    pdf.ln(4)
                    continue

                if line.startswith("# "):
                    if pass_num == 1:
                        toc_data.append({"title": "    " + clean_text(line[2:]), "page": pdf.page_no()})
                    pdf.set_font("helvetica", "B", 20)
                    pdf.set_text_color(255, 140, 0)
                    pdf.multi_cell(0, 10, clean_text(line[2:]))
                    pdf.ln(4)
                elif line.startswith("## "):
                    pdf.set_font("helvetica", "B", 16)
                    pdf.set_text_color(200, 200, 200)
                    pdf.multi_cell(0, 8, clean_text(line[3:]))
                    pdf.ln(2)
                elif line.startswith("> [!"):
                    pdf.set_font("helvetica", "I", 12)
                    pdf.set_text_color(255, 50, 50)
                    pdf.multi_cell(0, 6, "--- OIG CLASSIFIED FACT ---")
                elif line.startswith(">"):
                    pdf.set_font("helvetica", "I", 11)
                    pdf.set_text_color(255, 200, 100)
                    pdf.multi_cell(0, 6, clean_text(line[1:]))
                else:
                    pdf.set_font("helvetica", "", 11)
                    pdf.set_text_color(180, 180, 180)
                    pdf.multi_cell(0, 6, clean_text(line))

def assemble():
    print("Beginning Book of Mailstorm Pass 1 (TOC Calculation)...")
    pdf_dummy = LorePDF()
    pdf_dummy.set_auto_page_break(auto=True, margin=15)
    toc_data = []
    draw_content(pdf_dummy, 1, toc_data)
    
    offset = 2 # cover + toc page
    for t in toc_data:
        t["page"] += offset

    print("Beginning Book of Mailstorm Pass 2 (Final Render)...")
    pdf_final = LorePDF()
    pdf_final.set_auto_page_break(auto=True, margin=15)
    
    total = 20
    for i in range(total):
        bar = "[" + "█" * (i//2) + "░" * (10 - i//2) + f"] {int(i/total*100)}%"
        print(f"{bar} Assembling PDF Layout...", end='\r')
    
    draw_content(pdf_final, 2, toc_data)
    
    if IMAGES["COVER_BACK"]:
        pdf_final.add_page()
        pdf_final.image(IMAGES["COVER_BACK"], 0, 0, 210, 297)

    pdf_final.output(OUTPUT_FILE)
    print(f"\n[██████████] 100% SUCCESS -> Final Output: {OUTPUT_FILE}")

if __name__ == "__main__":
    assemble()
