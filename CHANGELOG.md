# Changelog

## [1.2.0] – 2025-04-30

### ✨ New Features

- 📖 Added support for the **ESV (English Standard Version)** via [api.esv.org](https://api.esv.org/)
- 🔐 Secure API key integration using `Authorization: Token ...` header
- 🔄 ESV available as option [2] in the translation menu
- 📜 ESV results include properly formatted verse numbers (e.g., `[16]`, `[17]`) for multi-verse passages

### 🧰 Internal Improvements

- Refactored `main.py` to route ESV lookups cleanly through `fetch_esv_text()`
- Added `get_esv_api_key()` in `config_loader.py` for safe fallback loading
- Updated `.env.example` and `config.py.sample` to include `ESV_API_KEY`

---

## [1.1.0] – 2025-04-28

### ✨ New Features

- 🔄 Added full support for the **NLT (New Living Translation)** using [api.nlt.to](https://api.nlt.to)
- 🔠 NLT moved to the default translation option (now option [1])
- 📜 Preserves verse numbers in multi-verse lookups
- 🔧 Added fallback-friendly API routing per translation
- 💾 Support saving study notes as always

### 🛠 Improvements

- Smarter verse parsing (BeautifulSoup) for clean CLI output
- Improved error handling for invalid references or missing API keys
- More readable main menu with “Change Translation” and “Enter New Reference”

### 🧹 Cleanup

- Removed unsupported/deprecated translations (NIV, CSB, NKJV)
- Updated config loader to support NLT API key
- Improved docs, environment handling, and README formatting