import os
import glob
from fpdf import FPDF

# Configuration
LORE_DIR = r"C:\Users\neo31\Mailstorm\docs\lore"
ARTIFACT_DIR = r"C:\Users\neo31\.gemini\antigravity\brain\02e7ce15-02d4-4e8a-be5c-eb8e8aeb461d"
OUTPUT_FILE = r"C:\Users\neo31\Mailstorm\releases\The_Book_of_Mailstorm_Vol1.pdf"

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
    def header(self):
        # Force every new page to have a dark aesthetic background
        self.set_fill_color(15, 15, 15)
        self.rect(0, 0, 210, 297, "F")
        
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "B", 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f"- {self.page_no()} -", new_x="LMARGIN", new_y="NEXT", align="C")

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
        pdf.set_text_color(255, 100, 0)
        pdf.set_font("helvetica", "B", 26)
        pdf.cell(0, 24, "TABLE OF CONTENTS", new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.set_draw_color(255, 100, 0)
        pdf.line(20, pdf.get_y(), 190, pdf.get_y())
        pdf.ln(10)
        
        pdf.set_font("helvetica", "B", 14)
        pdf.set_text_color(220, 220, 220)
        for entry in toc_data:
            if "PART" in entry["title"]:
                pdf.ln(4)
                pdf.set_font("helvetica", "B", 16)
                pdf.set_text_color(255, 140, 0)
            else:
                pdf.set_font("helvetica", "", 13)
                pdf.set_text_color(200, 200, 200)

            pdf.cell(150, 10, entry["title"])
            pdf.cell(20, 10, str(entry["page"]), new_x="LMARGIN", new_y="NEXT", align="R")
        pdf.ln(10)

    for part in PARTS:
        if pass_num == 1:
            toc_data.append({"title": part["title"], "page": pdf.page_no() + 1})
            
        if part["img"] and pass_num == 2:
            pdf.add_page()
            pdf.image(part["img"], 0, 0, 210, 297)
        
        pdf.add_page()
        
        # Helper to neatly draw text lines
        def safe_draw(pdf, style, size, r, g, b, txt, line_height=7, indent=0):
            pdf.set_font("helvetica", style, size)
            pdf.set_text_color(r, g, b)
            pdf.set_x(15 + indent) # Margin
            
            # Prevent crashes by truncating impossible widths
            words = txt.split(' ')
            safe_words = [w[:45] if len(w) > 45 else w for w in words]
            safe_txt = ' '.join(safe_words)
            
            # W=180 handles page width properly with standard margins
            try:
                pdf.multi_cell(180 - indent, line_height, safe_txt)
            except Exception:
                pass

        for filename in part["files"]:
            filepath = os.path.join(LORE_DIR, filename)
            if not os.path.exists(filepath):
                filepath = os.path.join(ARTIFACT_DIR, filename)
                if not os.path.exists(filepath):
                    continue
            
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            pdf.ln(8)
            for line in lines:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("# "):
                    if pass_num == 1:
                        toc_data.append({"title": "    " + clean_text(line[2:]), "page": pdf.page_no()})
                    pdf.ln(10)
                    safe_draw(pdf, "B", 24, 255, 100, 0, clean_text(line[2:]), 12)
                    pdf.set_draw_color(255, 100, 0)
                    pdf.line(15, pdf.get_y(), 195, pdf.get_y())
                    pdf.ln(6)
                elif line.startswith("## "):
                    pdf.ln(8)
                    safe_draw(pdf, "B", 18, 220, 220, 220, clean_text(line[3:]), 10)
                    pdf.ln(4)
                elif line.startswith("### "):
                    pdf.ln(6)
                    safe_draw(pdf, "B", 14, 255, 150, 50, clean_text(line[4:]), 8)
                    pdf.ln(2)
                elif line.startswith("> [!"):
                    pdf.ln(4)
                    safe_draw(pdf, "B", 14, 255, 50, 50, "--- CLASSIFIED NOTICE ---", 8)
                elif line.startswith(">"):
                    # Sidebar text
                    safe_draw(pdf, "I", 12, 255, 150, 100, clean_text(line[1:]), 8, indent=10)
                    pdf.ln(2)
                elif line.startswith("* "):
                    # Bullet point
                    safe_draw(pdf, "", 12, 200, 200, 200, " • " + clean_text(line[2:]), 6, indent=5)
                    pdf.ln(2)
                else:
                    # Regular paragraph text
                    safe_draw(pdf, "", 12, 220, 220, 220, clean_text(line), 7)
                    pdf.ln(3)
                    
            pdf.add_page() # Break after each markdown doc to keep it clean

def assemble():
    print("Beginning Book of Mailstorm Pass 1 (TOC Calculation)...")
    pdf_dummy = LorePDF()
    pdf_dummy.set_auto_page_break(auto=True, margin=20)
    toc_data = []
    draw_content(pdf_dummy, 1, toc_data)
    
    offset = 2 
    for t in toc_data:
        t["page"] += offset

    print("Beginning Book of Mailstorm Pass 2 (Final Render)...")
    pdf_final = LorePDF()
    pdf_final.set_auto_page_break(auto=True, margin=20)
    
    draw_content(pdf_final, 2, toc_data)
    
    if IMAGES["COVER_BACK"]:
        pdf_final.add_page()
        pdf_final.image(IMAGES["COVER_BACK"], 0, 0, 210, 297)

    pdf_final.output(OUTPUT_FILE)
    print(f"\n[██████████] 100% SUCCESS -> Final Output: {OUTPUT_FILE}")

if __name__ == "__main__":
    assemble()
