# api_bible_client.py

import requests
from config_loader import get_bible_api_key

BASE_URL = "https://api.scripture.api.bible/v1/bibles"

# Bible IDs
BIBLE_IDS = {
    "NIV": "de4e12af7f28f599-01",   # New International Version
    "KJV": "06125adad2d5898a-01",   # King James Version
    "NKJV": "c936cc06c7204b2f-02",  # New King James Version
    "NLT": "fae27669d3eec4ca-01",   # New Living Translation
    "CSB": "1c6ca0b2e3b78c14-02"    # Christian Standard Bible
}

# Bible book abbreviations expected by api.bible
BOOK_ABBREVIATIONS = {
    "Genesis": "GEN",
    "Exodus": "EXO",
    "Leviticus": "LEV",
    "Numbers": "NUM",
    "Deuteronomy": "DEU",
    "Joshua": "JOS",
    "Judges": "JDG",
    "Ruth": "RUT",
    "1 Samuel": "1SA",
    "2 Samuel": "2SA",
    "1 Kings": "1KI",
    "2 Kings": "2KI",
    "1 Chronicles": "1CH",
    "2 Chronicles": "2CH",
    "Ezra": "EZR",
    "Nehemiah": "NEH",
    "Esther": "EST",
    "Job": "JOB",
    "Psalms": "PSA",
    "Proverbs": "PRO",
    "Ecclesiastes": "ECC",
    "Song of Solomon": "SNG",
    "Isaiah": "ISA",
    "Jeremiah": "JER",
    "Lamentations": "LAM",
    "Ezekiel": "EZK",
    "Daniel": "DAN",
    "Hosea": "HOS",
    "Joel": "JOL",
    "Amos": "AMO",
    "Obadiah": "OBA",
    "Jonah": "JON",
    "Micah": "MIC",
    "Nahum": "NAM",
    "Habakkuk": "HAB",
    "Zephaniah": "ZEP",
    "Haggai": "HAG",
    "Zechariah": "ZEC",
    "Malachi": "MAL",
    "Matthew": "MAT",
    "Mark": "MRK",
    "Luke": "LUK",
    "John": "JHN",
    "Acts": "ACT",
    "Romans": "ROM",
    "1 Corinthians": "1CO",
    "2 Corinthians": "2CO",
    "Galatians": "GAL",
    "Ephesians": "EPH",
    "Philippians": "PHP",
    "Colossians": "COL",
    "1 Thessalonians": "1TH",
    "2 Thessalonians": "2TH",
    "1 Timothy": "1TI",
    "2 Timothy": "2TI",
    "Titus": "TIT",
    "Philemon": "PHM",
    "Hebrews": "HEB",
    "James": "JAS",
    "1 Peter": "1PE",
    "2 Peter": "2PE",
    "1 John": "1JN",
    "2 John": "2JN",
    "3 John": "3JN",
    "Jude": "JUD",
    "Revelation": "REV"
}

def normalize_reference(reference):
    """Convert human-readable single verse input into API-friendly format."""
    for book, abbreviation in BOOK_ABBREVIATIONS.items():
        if reference.lower().startswith(book.lower()):
            rest = reference[len(book):].strip()
            cleaned = rest.replace(":", ".").replace(" ", "")
            return f"{abbreviation}.{cleaned}"
    raise ValueError("Unrecognized book name in reference.")

def fetch_passage_id(reference, bible_id, api_key):
    """Search for a passage ID given a reference string."""
    url = f"{BASE_URL}/{bible_id}/search"
    headers = {
        "api-key": api_key
    }
    params = {
        "query": reference
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        passages = data.get("data", {}).get("passages", [])
        if passages:
            return passages[0]["id"]
        else:
            raise Exception(f"No passage found for query: {reference}")
    else:
        raise Exception(f"Error searching for passage ID: {response.status_code} {response.text}")

def fetch_verse_text(reference, translation="NIV"):
    """Fetch the verse or passage text given a human-readable reference."""
    api_key = get_bible_api_key()
    bible_id = BIBLE_IDS.get(translation.upper())

    if not bible_id:
        raise ValueError(f"Unsupported translation code: {translation}")

    headers = {
        "api-key": api_key
    }

    reference = " ".join(reference.split())  # Clean extra spaces

    if "-" in reference:
        # Multi-verse passage
        print(f"Searching for passage matching '{reference}'...", end=" ")
        passage_id = fetch_passage_id(reference, bible_id, api_key)
        print(f"found ID: {passage_id}")

        url = f"{BASE_URL}/{bible_id}/passages/{passage_id}"
        params = {
            "content-type": "text",
            "include-notes": "false",
            "include-titles": "true",
            "include-chapter-numbers": "false",
            "include-verse-numbers": "true",
            "include-verse-spans": "false",
            "use-org-id": "false"
        }

        print(f"Fetching passage: {passage_id}...", end=" ")
        response = requests.get(url, headers=headers, params=params)
    else:
        # Single verse
        normalized_ref = normalize_reference(reference)
        url = f"{BASE_URL}/{bible_id}/verses/{normalized_ref}"
        params = {
            "content-type": "text"
        }
        print(f"Fetching verse: {reference}...", end=" ")
        response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        verse_text = data["data"]["content"]
        print("done.")
        return verse_text
    else:
        print("failed.")
        raise Exception(f"Error fetching verse: {response.status_code} {response.text}")
