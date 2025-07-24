import re
import os

# --- Configuration ---
UNUSED_KEYS_FILE = 'a.txt'
ORIGINAL_BIB_FILE = 'main.bib'
CLEANED_BIB_FILE = 'main_cleaned.bib'

# --- 1. Read the list of unused citation keys ---
unused_keys = set()
try:
    with open(UNUSED_KEYS_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            # Check if the line contains an unused key marker
            if line.strip().startswith('=> '):
                # Extract the key by splitting the line and taking the last word
                key = line.strip().split()[-1]
                unused_keys.add(key)
    print(f"✔️ Found {len(unused_keys)} unused citation keys in '{UNUSED_KEYS_FILE}'.")
except FileNotFoundError:
    print(f"❌ Error: '{UNUSED_KEYS_FILE}' not found. Make sure you've run checkcites first.")
    exit()

# --- 2. Read the original .bib file ---
try:
    with open(ORIGINAL_BIB_FILE, 'r', encoding='utf-8') as f:
        bib_content = f.read()
except FileNotFoundError:
    print(f"❌ Error: The file '{ORIGINAL_BIB_FILE}' was not found.")
    exit()

# --- 3. Filter out the unused entries ---
bib_parts = bib_content.split('@')
header = bib_parts[0]
entries = bib_parts[1:]

kept_entries = []
removed_count = 0

for entry_str in entries:
    # Use regex to find the citation key
    match = re.search(r'^\s*\w+\s*\{\s*([^,]+)', entry_str)
    
    if match:
        key = match.group(1).strip()
        # If the key is NOT in our unused list, we keep the entry.
        if key not in unused_keys:
            kept_entries.append('@' + entry_str)
        else:
            removed_count += 1
            # print(f"Removing: {key}") # Uncomment to see which keys are removed
    else:
        # Keep malformed entries or comments to be safe.
        kept_entries.append('@' + entry_str)

# --- 4. Write the cleaned .bib file ---
with open(CLEANED_BIB_FILE, 'w', encoding='utf-8') as f:
    f.write(header)
    f.write("".join(kept_entries))

print(f"✅ Success! Removed {removed_count} unused entries.")
print(f"✨ Your clean bibliography has been saved to '{CLEANED_BIB_FILE}'.")