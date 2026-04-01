import os

LORE_DIR = r"c:\Users\neo31\Mailstorm\docs\lore"
files = [f for f in os.listdir(LORE_DIR) if f.endswith('.md')]

replacements = {
    'â€™': '’',
    'â€”': '—',
    'â€œ': '“',
    'â€"': '”',
    'â€': '”',
    'BÃ©ton': 'Béton',
    'Ã©': 'é'
}

for f in files:
    path = os.path.join(LORE_DIR, f)
    with open(path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    for bad, good in replacements.items():
        content = content.replace(bad, good)
        
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Mojibake characters sanitized.")
