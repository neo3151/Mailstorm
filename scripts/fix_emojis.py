import os
import re

LORE_DIR = r"c:\Users\neo31\Mailstorm\docs\lore"
files = [f for f in os.listdir(LORE_DIR) if f.endswith('.md')]

for f in files:
    path = os.path.join(LORE_DIR, f)
    with open(path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    # General corrections
    content = content.replace('Â¢', '¢')
    content = content.replace('Â°', '°')
    
    # characters.md replaces
    content = re.sub(r'## ðŸŸ¢', '## 🟢', content)
    content = re.sub(r'## .*? THE MANAGEMENT INQUISITION', '## 🔴 THE MANAGEMENT INQUISITION', content)
    content = re.sub(r'## .*? THE SUPERNATURAL THIRD-PARTY', '## ⚪ THE SUPERNATURAL THIRD-PARTY', content)
    
    # THE_CHRONICLE.md replaces
    content = re.sub(r'## .*? EPOCH I: THE FOUNDING', '## 🏛️ EPOCH I: THE FOUNDING', content)
    content = re.sub(r'## .*? EPOCH II: THE EXPANSION', '## 🐎 EPOCH II: THE EXPANSION', content)
    content = re.sub(r'## .*? EPOCH III: THE GOLDEN', '## ⚔️ EPOCH III: THE GOLDEN', content)
    content = re.sub(r'## .*? EPOCH IV: THE GREAT POSTAL', '## 🔥 EPOCH IV: THE GREAT POSTAL', content)
    content = re.sub(r'## .*? EPOCH V: THE ALGORITHMIC', '## 💀 EPOCH V: THE ALGORITHMIC', content)
    content = re.sub(r'## .*? EPOCH VI: THE PROPHECY', '## 🔮 EPOCH VI: THE PROPHECY', content)
    
    # THE_WORKPLACE.md replaces
    content = re.sub(r'## .*? LAYER 1: THE SORTING', r'## 📍 LAYER 1: THE SORTING', content)
    content = re.sub(r'## .*? LAYER 2: THE LLV GRAVEYARD', r'## 📍 LAYER 2: THE LLV GRAVEYARD', content)
    content = re.sub(r'## .*? LAYER 3: THE SUPERVISOR', r'## 📍 LAYER 3: THE SUPERVISOR', content)
    content = re.sub(r'## .*? THE DUNGEON MASTER\'S RULES', r'## 📜 THE DUNGEON MASTER\'S RULES', content)

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("All exact mojibake lines have been surgically replaced with their original emojis/characters.")
