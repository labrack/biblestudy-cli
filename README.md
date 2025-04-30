# biblestudy-cli

[![GitHub Release](https://img.shields.io/github/v/release/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/releases)
[![Last Commit](https://img.shields.io/github/last-commit/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/commits/main)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/github/license/labrack/biblestudy-cli)](https://github.com/labrack/biblestudy-cli/blob/main/LICENSE)

[![OpenAI API](https://img.shields.io/badge/API-OpenAI-lightblue.svg)](https://openai.com/)
[![Bible API](https://img.shields.io/badge/API-api.bible-lightblue.svg)](https://docs.api.bible/)
[![NLT API](https://img.shields.io/badge/API-api.nlt.to-lightblue.svg)](https://api.nlt.to/)
[![ESV API](https://img.shields.io/badge/API-api.esv.org-lightblue.svg)](https://api.esv.org/)

BibleStudy CLI — a text-based Bible study companion for your terminal.

Powered by [api.bible](https://docs.api.bible/), [api.nlt.to](https://api.nlt.to), and OpenAI.  
Inspired by [SimplyScripture](https://mysimplyscripture.com/).

> **Note:** Neither I nor this tool are affiliated with SimplyScripture — I just like their concept and wanted a CLI version.

---

## ✨ Features

- Input or detect Bible references (e.g., `John 3:16`)
- Choose from the following translations:
  - ✅ NLT (New Living Translation) — via `api.nlt.to`
  - ✅ ESV (English Standard Version) — via `api.esv.org`
  - ✅ FBV (Free Bible Version)
  - ✅ KJV (King James Version)
  - ✅ ASV (American Standard Version)
  - ✅ WEB (World English Bible)
- Retrieve verse content and:
  - ✏️ Simplify it
  - 🗣️ Translate into modern speech
  - 🏺 Reveal historical background
  - 🔗 Cross-reference other scriptures
  - 🔍 Highlight key terms
  - 🛠️ Apply to daily life
- Save study notes automatically
- Works in any terminal — beautiful output powered by `rich`

---

## 🚀 Requirements

- Python 3.9+
- `requests`, `openai`, `rich`, `beautifulsoup4`

Install dependencies:

pip install -r requirements.txt

---

## 🔐 API Keys Setup

You'll need:

- **OpenAI API key** ([Get one here](https://platform.openai.com/account/api-keys))
- **api.bible key** ([Sign up here](https://docs.api.bible/))
- **NLT API key** ([Request access here](https://api.nlt.to/))
- **ESV API key** (Request access here](https://api.esv.org))

Set environment variables:

export OPENAI_API_KEY=your-openai-key
export BIBLE_API_KEY=your-api-bible-key
export NLT_API_KEY=your-nlt-api-key
export ESV_API_KEY=your-esv-api-key
export BIBLESTUDY_NOTES_DIRECTORY=./notes  # optional override

Or use `config.py` locally (not recommended for production).

---

## ▶️ Running the App

python main.py

---

## 💬 Sample Run
```
📖 Welcome to the Bible Study CLI 📖

Enter a Bible reference (e.g., John 3:16) or a snippet of scripture.

>> John 3:16

Which translation would you like to use?
[1] NLT (New Living Translation)
[2] ESV (English Standard Version)
[2] FBV (Free Bible Version)
[3] KJV (King James Version)
[4] ASV (American Standard Version)
[5] WEB (World English Bible)

Enter the number for your translation [1/2/3/4/5]: 1

Fetching NLT passage: John 3:16... done.

📜 John 3:16
╭────────────────────────────────────────────────────────────────────────────╮
│ For God loved the world so much that he gave his one and only Son, so     │
│ that everyone who believes in him will not perish but have eternal life.  │
╰────────────────────────────────────────────────────────────────────────────╯

What would you like to do?
[1] ✏️  Simplify
[2] 🗣️  Modern English
[3] 🏺 Background
[4] 🔗 Cross-References
[5] 🔍 Keyword Focus
[6] 🛠️ Life Application
[7] 🔄 Change Translation for Current Reference
[8] ➕ Enter a New Bible Reference
[0] 🚪 Exit
```
---

## 💾 Saving Notes

Your study results are saved to the `notes/` folder by default.  
You can change the location with the `BIBLESTUDY_NOTES_DIRECTORY` environment variable.

---

## 💡 Tips for Development

- Don't commit your real API keys — use the provided `.gitignore` to ignore `config.py`
- Use `.env.example` as a template for local testing
- Notes are plain `.txt` files and easy to back up

---

## 🍎 Mac-Specific Notes

If you see a warning like this:

NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently using LibreSSL

✅ You can safely ignore it, or pin `urllib3<2` in your requirements to avoid it.

---

## 🔮 Future Ideas for Version 1.2+

- Add fuzzy search for snippets (e.g. "love is patient")
- Support full chapter navigation
- Offline caching for entire books
- Daily verse feature
- Save notes in Markdown format
- Session resume after crash
- UI upgrade using `textual` or `urwid`

---

## 📜 License

MIT License — use freely and contribute back!
