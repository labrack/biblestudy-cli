# api_bible_client.py

import requests
from config_loader import get_bible_api_key

BASE_URL = "https://api.scripture.api.bible/v1/bibles"

# These are standard Bible IDs used by api.bible for each translation
BIBLE_IDS = {
    "NIV": "de4e12af7f28f599-02",   # New International Version
    "KJV": "06125adad2d5898a-01",   # King James Version
    "NKJV": "c936cc06c7204b2f-02",  # New King James Version
    "NLT": "fae27669d3eec4ca-01",   # New Living Translation
    "CSB": "1c6ca0b2e3b78c14-02"    # Christian Standard Bible
}

def fetch_verse_text(reference, translation):
    """Fetch a verse text given a reference like 'John 3:16' and a translation code (e.g., NIV)."""
    api_key = get_bible_api_key()
    bible_id = BIBLE_IDS.get(translation.upper())

    if not bible_id:
        raise ValueError(f"Unsupported translation code: {translation}")

    headers = {
        "api-key": api_key
    }

    url = f"{BASE_URL}/{bible_id}/verses/{reference.replace(' ', '')}?content-type=text"

    print("Fetching verse...", end=" ")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        verse_text = data['data']['content']
        print("done.")
        return verse_text
    else:
        print("failed.")
        raise Exception(f"Error fetching verse: {response.status_code} {response.text}")