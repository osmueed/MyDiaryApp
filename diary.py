import json
import os
from datetime import datetime

FILE_NAME = 'diary.json'

def load_entries():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_entry(text):
    entries = load_entries()
    entry = {
        "date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "text": text
    }
    entries.append(entry)
    with open(FILE_NAME, 'w') as file:
        json.dump(entries, file, indent=4)

def show_entries():
    entries = load_entries()
    if not entries:
        print("No diary entries yet.")
    else:
        for entry in entries:
            print(f"[{entry['date']}]: {entry['text']}")
            print("-" * 40)
