"""
Bild-Suche für Karussell-Posts
Nutzt Unsplash Free (ohne API-Key): lädt Bilder manuell herunter.
Alternativ: Pexels als Backup.

Nutzung:
    python3 fetch_images.py "calm woman nature beige" 01
    → Gibt 5 Unsplash-URLs aus + speichert in posts/post_01/input/unsplash/
"""

import sys
import os
import urllib.request
import json

def get_unsplash_urls(query, count=5):
    """Gibt Unsplash-Such-URLs aus (ohne API-Key)."""
    print(f"\n{'='*50}")
    print(f"UNSPLASH SUCHE: {query}")
    print(f"{'='*50}\n")
    print("Ohne API-Key: Bitte manuell auf Unsplash suchen.")
    print(f"Link: https://unsplash.com/s/photos/{query.replace(' ', '-')}\n")
    print(f"Lade {count} passende Bilder herunter und lege sie in den input/unsplash/ Ordner.\n")
    print("Empfohlene Suchbegriffe für Theresa Ross:")
    print("  - calm woman nature beige")
    print("  - soft morning light")
    print("  - hands tea linen")
    print("  - woman back nature mist")
    print("  - minimalist texture warm")
    print("  - breathing calm portrait")
    print("  - earth tones still life")
    print()

def get_pexels_urls(query, count=5):
    """Pexels als Backup."""
    print(f"PEXELS BACKUP: https://www.pexels.com/search/{query.replace(' ', '%20')}/\n")

def create_post_dirs(post_number):
    """Erstellt Ordnerstruktur für einen Post."""
    base = f"../posts/post_{post_number:02d}"
    dirs = [
        f"{base}/input/manual",
        f"{base}/input/unsplash",
        f"{base}/output"
    ]
    for d in dirs:
        path = os.path.join(os.path.dirname(__file__), d)
        os.makedirs(path, exist_ok=True)
    print(f"Ordner erstellt: posts/post_{post_number:02d}/")
    return base

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "calm nature beige"
    post_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    create_post_dirs(post_num)
    get_unsplash_urls(query)
    get_pexels_urls(query)
