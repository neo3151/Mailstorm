import os
import markdown

LORE_DIR = r"c:\Users\neo31\Mailstorm\docs\lore"
OUTPUT_FILE = r"c:\Users\neo31\Mailstorm\web\public\encyclopedia.html"

LORE_ORDER = [
    "universe_architecture.md",
    "THE_CORE_MECHANICS.md",
    "THE_CHRONICLE.md",
    "THE_FACTIONS.md",
    "THE_HIERARCHY.md",
    "THE_MASTER_CONTRACT.md",
    "THE_METRICS_CAGE.md",
    "THE_DAILY_GRIND.md",
    "THE_ROUTE_TOPOLOGY.md",
    "THE_WORKPLACE.md",
    "THE_FORBIDDEN_FORMS.md",
    "THE_BESTIARY.md",
    "characters.md"
]

HTML_WRAPPER = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mailstorm: Master Compendium</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;700&family=Roboto+Condensed:wght@400;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-abyss: #0a0a0a;
            --text-bone: #d4d0c8;
            --accent-hazard: #ff4f00;
            --border-gutter: #1a1a1a;
        }}
        body {{
            background-color: var(--bg-abyss);
            color: var(--text-bone);
            font-family: 'Roboto Condensed', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            font-size: 1.1rem;
        }}
        .container {{
            max-width: 900px;
            padding: 4rem 2.5rem;
            width: 100%;
        }}
        h1, h2, h3 {{
            font-family: 'Oswald', sans-serif;
            color: var(--accent-hazard);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 3.5rem;
            border-bottom: 1px solid var(--border-gutter);
            padding-bottom: 0.5rem;
        }}
        h1 {{ font-size: 3.5rem; text-align: center; border: none; margin-bottom: 4rem; letter-spacing: 4px; line-height: 1.2; text-shadow: 0 0 40px rgba(255,79,0,0.2);}}
        h2 {{ font-size: 2.2rem; margin-top: 5rem; }}
        hr {{ border: 0; height: 1px; background: var(--border-gutter); margin: 4rem 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 2rem 0; background: #111; }}
        th, td {{ border: 1px solid var(--border-gutter); padding: 1rem; text-align: left; }}
        th {{ color: var(--accent-hazard); font-family: 'Oswald', sans-serif; letter-spacing: 2px; }}
        a {{ color: var(--accent-hazard); text-decoration: none; border-bottom: 1px dashed var(--accent-hazard); }}
        a:hover {{ background: var(--accent-hazard); color: #000; }}
        img {{ max-width: 100%; height: auto; }}
        blockquote {{ border-left: 4px solid var(--accent-hazard); padding-left: 1.5rem; margin-left: 0; font-style: italic; color: #888; }}
        ul {{ list-style-type: square; }}
        li {{ margin-bottom: 0.5rem; }}
        .nav-back {{ display: inline-block; margin-bottom: 2rem; color: var(--text-bone); font-family: 'Oswald', sans-serif; letter-spacing: 2px; text-decoration: none; border: 1px solid var(--border-gutter); padding: 0.5rem 1rem; transition: all 0.2s; }}
        .nav-back:hover {{ border-color: var(--accent-hazard); color: var(--accent-hazard); background: transparent; }}
        @media print {{
            body {{ background-color: white; color: black; }}
            h1, h2, h3 {{ color: black; border-color: #ccc; text-shadow: none; }}
            table {{ background: white; }}
            .nav-back {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="nav-back">← RETURN TO PORTAL</a>
        <h1>THE ABYSSAL STANDARD<br><span style="font-size: 1.8rem; color: #555;">MASTER COMPENDIUM</span></h1>
        {content}
    </div>
</body>
</html>"""

import re

def load_and_strip_frontmatter(filepath):
    # Use utf-8-sig to automatically strip the hidden Byte Order Mark 
    # injected by PowerShell's Set-Content, which breaks basic string matching.
    with open(filepath, 'r', encoding='utf-8-sig') as f:
        content = f.read()
    
    # Strip the frontmatter block only if it starts exactly at the beginning of the file
    if content.startswith('---'):
        content = re.sub(r'^---.*?---[\r\n]+', '', content, count=1, flags=re.DOTALL)
            
    return content.strip()

raw_markdown = ""
for filename in LORE_ORDER:
    path = os.path.join(LORE_DIR, filename)
    if os.path.exists(path):
        raw_markdown += load_and_strip_frontmatter(path) + "\n\n---\n\n"

html_content = markdown.markdown(raw_markdown, extensions=['tables'])
final_html = HTML_WRAPPER.format(content=html_content)

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Web Encyclopedia successfully compiled to {OUTPUT_FILE}!")
