import os
import re

LORE_DIR = r"c:\Users\neo31\Mailstorm\docs\lore"
files = [f for f in os.listdir(LORE_DIR) if f.endswith('.md')]

for f in files:
    path = os.path.join(LORE_DIR, f)
    # Use utf-8-sig to bypass any residual BOM on read
    with open(path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # 1. Clean the garbled characters from headings using regex
    # It targets any garbage string of 1 to 5 chars between ## and I. or IV. etc
    # e.g., "## dY?>,? I. THE " -> "## I. THE "
    content = re.sub(r'##\s+[^a-zA-Z0-9_\-\"\'\(]+([A-Z0-9IVX]+\.)', r'## \1', content)
    content = re.sub(r'#\s+[^a-zA-Z0-9_\-\"\'\(]+([A-Z0-9IVX]+\.)', r'# \1', content)
    
    # Target any remaining explicit known corrupted substrings globally just in case
    content = content.replace('ÐŸ’¡', '')
    content = content.replace('dY?>,?', '')
    
    # 2. Re-save it back properly
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print(f"Sanitized {{len(files)}} lore files.")
