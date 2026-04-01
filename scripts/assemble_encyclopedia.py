"""
ASSEMBLE_ENCYCLOPEDIA.PY
Purpose: Dynamically parses 12 Markdown Lore files into a single, high-fidelity PDF Compendium.
Aesthetic: Liminal Brutalism / Corporate Horror
"""

import os
import sys
import re
import logging
from fpdf import FPDF

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

LORE_DIR = r"c:\Users\neo31\Mailstorm\docs\lore"
OUTPUT_FILE = r"c:\Users\neo31\Mailstorm\releases\Mailstorm_Encyclopedia.pdf"

if not os.path.exists(LORE_DIR):
    logging.error(f"FATAL: Lore directory not found at {LORE_DIR}")
    sys.exit(1)

LORE_ORDER = [
    "universe_architecture.md",
    "THE_CORE_MECHANICS.md",
    "THE_CHRONICLE.md",
    "THE_FACTIONS.md",
    "THE_HIERARCHY.md",
    "THE_CONTRACT.md",
    "THE_DAILY_GRIND.md",
    "THE_ROUTE_TOPOLOGY.md",
    "THE_WORKPLACE.md",
    "THE_FORBIDDEN_FORMS.md",
    "THE_BESTIARY.md",
    "characters.md"
]

def load_and_strip_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    in_frontmatter = False
    content = []
    frontmatter_count = 0
    
    for line in lines:
        if line.strip() == "---":
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
                continue
            elif frontmatter_count == 2:
                in_frontmatter = False
                continue
        if not in_frontmatter:
            content.append(line)
            
    return "".join(content)

def draw_title_page(pdf):
    pdf.add_page()
    pdf.set_fill_color(0, 0, 0)
    pdf.rect(0, 0, 210, 297, "F")
    
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 36)
    pdf.set_y(120)
    pdf.cell(0, 15, "THE ABYSSAL STANDARD", align="C", ln=1)
    
    pdf.set_font("helvetica", "", 18)
    pdf.cell(0, 15, "MASTER COMPENDIUM", align="C", ln=1)
    
    pdf.set_y(260)
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(0, 10, "SYSTEMATIC LORE DIRECTORY v1.0", align="C", ln=1)

def parse_markdown(pdf, text, toc_map=None, is_pass_1=False):
    lines = text.split('\n')
    in_table = False
    
    for line in lines:
        stripped = line.strip()
        
        if not stripped:
            pdf.ln(4)
            in_table = False
            continue
            
        if stripped.startswith('|') and stripped.endswith('|'):
            in_table = True
            if '|---' in stripped or '|:---' in stripped:
                continue
                
            cells = [cell.strip() for cell in stripped.split('|')[1:-1]]
            if len(cells) == 0: continue
            col_width = 190 / len(cells)
            
            pdf.set_font("helvetica", "B" if pdf.get_y() < 60 and "Term" in cells else "", 9)
            pdf.set_text_color(20, 20, 20)
            
            for cell in cells:
                clean_cell = cell.replace('**', '')
                try:
                    pdf.cell(col_width, 8, clean_cell, border=1)
                except:
                    pdf.cell(col_width, 8, clean_cell.encode('latin-1','ignore').decode('latin-1'), border=1)
            pdf.ln(8)
            continue
            
        in_table = False
        
        if stripped.startswith('# '):
            heading = stripped[2:].replace('**', '')
            if pdf.page_no() > 3 or (pdf.page_no() > 1 and not is_pass_1): 
                pdf.add_page()
            elif is_pass_1:
                pdf.add_page()
                
            if toc_map is not None and is_pass_1:
                toc_map.append((1, heading[:160], pdf.page_no()))
                
            pdf.set_font("helvetica", "B", 26)
            pdf.set_text_color(0, 0, 0)
            try: pdf.cell(0, 15, heading, ln=1)
            except: pdf.cell(0, 15, heading.encode('latin-1','ignore').decode('latin-1'), ln=1)
            pdf.ln(5)
            
        elif stripped.startswith('## '):
            heading = stripped[3:].replace('**', '')
            if pdf.get_y() > 250: pdf.add_page()
            
            if toc_map is not None and is_pass_1:
                toc_map.append((2, heading[:160], pdf.page_no()))
                
            pdf.set_font("helvetica", "B", 18)
            pdf.set_text_color(150, 0, 0) 
            pdf.ln(8)
            try: pdf.cell(0, 10, heading, ln=1)
            except: pdf.cell(0, 10, heading.encode('latin-1','ignore').decode('latin-1'), ln=1)
            pdf.ln(2)
            
        elif stripped.startswith('### ') or stripped.startswith('#### '):
            heading = stripped.lstrip('# ').replace('**', '')
            pdf.set_font("helvetica", "B", 14)
            pdf.set_text_color(0, 0, 0)
            pdf.ln(5)
            try: pdf.cell(0, 8, heading, ln=1)
            except: pdf.cell(0, 8, heading.encode('latin-1','ignore').decode('latin-1'), ln=1)
            
        elif stripped == '---':
            pdf.ln(5)
            y = pdf.get_y()
            pdf.line(10, y, 200, y)
            pdf.ln(5)
            
        elif (stripped.startswith('- ') or stripped.startswith('* ')) and not stripped.startswith('***'):
            pdf.set_font("helvetica", "", 11)
            pdf.set_text_color(20, 20, 20)
            content = stripped.lstrip('-* ')
            pdf.set_x(15)
            pdf.cell(5, 6, chr(149))
            
            chunks = re.split(r'(\*\*.*?\*\*)', content)
            for chunk in chunks:
                if chunk.startswith('**') and chunk.endswith('**'):
                    pdf.set_font("helvetica", "B", 11)
                    try: pdf.write(6, chunk[2:-2])
                    except: pdf.write(6, chunk[2:-2].encode('latin-1','ignore').decode('latin-1'))
                    pdf.set_font("helvetica", "", 11)
                else:
                    try: pdf.write(6, chunk)
                    except: pdf.write(6, chunk.encode('latin-1','ignore').decode('latin-1'))
            pdf.ln(6)
            
        else:
            pdf.set_font("helvetica", "", 11)
            pdf.set_text_color(20, 20, 20)
            if stripped.startswith('> '):
                pdf.set_font("helvetica", "I", 11)
                stripped = stripped[2:]
            
            chunks = re.split(r'(\*\*.*?\*\*)', stripped)
            for chunk in chunks:
                if chunk.startswith('**') and chunk.endswith('**'):
                    pdf.set_font("helvetica", "B", 11)
                    try: pdf.write(6, chunk[2:-2])
                    except: pdf.write(6, chunk[2:-2].encode('latin-1','ignore').decode('latin-1'))
                    pdf.set_font("helvetica", "", 11)
                else:
                    try: pdf.write(6, chunk)
                    except: pdf.write(6, chunk.encode('latin-1','ignore').decode('latin-1'))
            pdf.ln(6)

def build_pdf():
    total_files = len(LORE_ORDER)
    logging.info("Initiating Two-Pass Mailstorm Encyclopedia Compile...")
    
    pdf_virtual = FPDF(format="A4")
    pdf_virtual.set_auto_page_break(True, margin=15)
    toc_map = []
    
    draw_title_page(pdf_virtual)
    pdf_virtual.add_page(); pdf_virtual.add_page() 
    
    for filename in LORE_ORDER:
        path = os.path.join(LORE_DIR, filename)
        if os.path.exists(path):
            raw_text = load_and_strip_frontmatter(path)
            parse_markdown(pdf_virtual, raw_text, toc_map, is_pass_1=True)

    pdf = FPDF(format="A4")
    pdf.set_auto_page_break(True, margin=15)
    pdf.set_title("Mailstorm: Master Compendium")
    pdf.set_author("The Department of Logistics")
    
    draw_title_page(pdf)
    
    pdf.add_page()
    pdf.set_fill_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("helvetica", "B", 24)
    pdf.cell(0, 15, "TABLE OF CONTENTS", ln=1)
    pdf.ln(10)
    
    for level, heading, pagenum in toc_map:
        if level == 1:
            pdf.ln(3)
            pdf.set_font("helvetica", "B", 12)
            try: pdf.cell(160, 8, heading.upper())
            except: pdf.cell(160, 8, heading.upper().encode('latin-1','ignore').decode('latin-1'))
            pdf.cell(20, 8, str(pagenum), align="R", ln=1)
        elif level == 2:
            pdf.set_font("helvetica", "", 10)
            pdf.set_x(15)
            try: pdf.cell(155, 6, heading[:80])
            except: pdf.cell(155, 6, heading[:80].encode('latin-1','ignore').decode('latin-1'))
            pdf.cell(20, 6, str(pagenum), align="R", ln=1)
    
    for idx, filename in enumerate(LORE_ORDER):
        pct = int(((idx + 1) / total_files) * 10)
        bar = "#" * pct + "-" * (10 - pct)
        try:
            sys.stdout.write(f"\r  [{bar}] {((idx+1)/total_files)*100:.0f}% | {idx+1}/{total_files} completed")
            sys.stdout.flush()
        except:
            pass
        
        path = os.path.join(LORE_DIR, filename)
        if os.path.exists(path):
            raw_text = load_and_strip_frontmatter(path)
            parse_markdown(pdf, raw_text, toc_map=None, is_pass_1=False)
            
    print("\n")
    
    pdf.output(OUTPUT_FILE)
    logging.info(f"Encyclopedia successfully forged at: {OUTPUT_FILE}")

if __name__ == "__main__":
    build_pdf()
