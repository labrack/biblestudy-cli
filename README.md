# biblestudy-cli

[![GitHub Release](https://img.shields.io/github/v/release/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/releases)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![OpenAI API](https://img.shields.io/badge/API-OpenAI-blue.svg)](https://openai.com/)
[![Bible API](https://img.shields.io/badge/API-api.bible-blue.svg)](https://docs.api.bible/)
[![License: MIT](https://img.shields.io/github/license/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/commits/main)


BibleStudy CLI — a text-based Bible study companion for your terminal!

Powered by [api.bible](https://docs.api.bible/) and OpenAI. Concept inspired by [SimplyScripture](https://mysimplyscripture.com/).

**<em>Note: Neither I nor this tool are associated with SimplyScripture in any way, I just like their site and wanted a CLI version of it</em>**

---

## Features

- Detect or input Bible references (e.g., `John 3:16`) or snippets
- Choose your preferred translation: NIV, KJV, NKJV, NLT, CSB
- Retrieve full verse text from `api.bible`
- Study options powered by GPT:
  - Simplify the verse
  - Translate into Modern English
  - Explore Historical Background
  - Find Cross-References
  - Analyze Keyword Focus
  - Apply the verse to daily life
- Save your study notes to text files
- Beautiful CLI interface with `rich`

---

## Requirements

- Python 3.9+
- `requests`, `openai`, `rich`

Install dependencies:

```
pip install -r requirements.txt
```

---

## API Keys Setup

This app requires two API keys:

- `api.bible` (get from [api.bible signup](https://docs.api.bible/))
- `OpenAI` (get from [OpenAI platform](https://platform.openai.com/account/api-keys))

Set environment variables:

```
export BIBLE_API_KEY=your-bible-api-key
export OPENAI_API_KEY=your-openai-api-key
export BIBLESTUDY_NOTES_DIRECTORY=your/notes/path  # optional, default is ./notes
```

Or edit `config.py` directly (not recommended for production).

---

## Running the App

```
python main.py
```

---

## Sample Run

```
📖 Welcome to the Bible Study CLI 📖
Enter a Bible reference (e.g., John 3:16) or a snippet of scripture:
>> For God so loved the world
Which translation?
[1] NIV
[2] KJV
[3] NKJV
[4] NLT
[5] CSB
>> 1

✅ Found in cache: John 3:16
Fetching verse... done.

📜 John 3:16
║ For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life. ║

What would you like to do?
[1] ✏️  Simplify
[2] 🗣️  Modern English
[3] 🗺️ Background
[4] 🔗 Cross-References
[5] 🔍 Keyword Focus
[6] 🛠️ Life Application
[0] 🚪 Exit
```

---

## Saving Notes

All study notes will be saved automatically under the `notes/` directory unless configured otherwise.

---

## GitHub Tips

Make sure you DO NOT commit your `config.py` with real API keys.
Use `.gitignore` provided to stay safe.

---

## Special Notes for Mac Users

- If you see a LibreSSL warning about urllib3 when running BibleStudy CLI, you can safely ignore it.
- To suppress it completely, you can run the app with this command:

  ```bash
  python -W ignore::urllib3.exceptions.NotOpenSSLWarning main.py

---

## Future Ideas for Version 1.1+

- Add fuzzy matching for scripture snippets to improve detection.
- Allow users to browse full chapters and books of the Bible.
- Add offline caching of entire Bible translations.
- Introduce user-configurable custom study prompts.
- Build a "Daily Verse" feature that launches on startup.
- Allow bookmarking and tagging favorite verses.
- Build a TUI (Terminal User Interface) with full navigation using `textual` or `urwid`.
- Support saving notes in Markdown or HTML formats.
- Add a session resume feature if the app is closed mid-study.

---

## License

MIT License.
