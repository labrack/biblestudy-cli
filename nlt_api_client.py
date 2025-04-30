# nlt_api_client.py

import requests
from bs4 import BeautifulSoup
from config_loader import get_nlt_api_key

BASE_URL = "https://api.nlt.to/api/passages"

def fetch_nlt_text(reference: str) -> str:
    """
    Fetch clean NLT passage text from api.nlt.to,
    preserving verse numbers and stripping footnotes.
    """
    api_key = get_nlt_api_key()

    if not api_key:
        raise Exception("❌ NLT API key is missing. Set NLT_API_KEY in your environment or config.py.")

    params = {
        "ref": reference.replace(" ", ".").replace(":", "."),
        "key": api_key
    }

    print(f"Fetching NLT passage: {reference}...", end=" ")
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200 or "Custom Page Error" in response.text:
        print("failed.")
        raise Exception(f"NLT API Error: {response.status_code} — Check the reference or API key.")

    print("done.")
    soup = BeautifulSoup(response.text, "html.parser")

    all_verses = []

    # Each verse is inside a <verse_export> tag
    for verse_tag in soup.select("verse_export"):
        # Remove footnote anchors and tooltips
        for tag in verse_tag.select("a, .tn"):
            tag.decompose()

        # Extract verse number
        verse_num = verse_tag.select_one(".vn")
        verse_num_text = verse_num.get_text(strip=True) if verse_num else ""

        # Extract verse content (red span)
        red_text = verse_tag.select_one(".red")
        verse_content = red_text.get_text(" ", strip=True) if red_text else ""

        full_line = f"[{verse_num_text}] {verse_content}" if verse_num_text else verse_content
        all_verses.append(full_line)

    return "\n".join(all_verses)