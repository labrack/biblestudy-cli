# Changelog

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