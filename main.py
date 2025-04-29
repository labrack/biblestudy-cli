# Suppress LibreSSL warnings from urllib3 on older MacOS
import warnings
from urllib3.exceptions import NotOpenSSLWarning

warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

import sys

try:
    from rich_ui import (
        welcome_screen,
        select_translation,
        main_menu,
        show_verse,
        show_interpretation,
        prompt_save,
        goodbye_message,
        error_message
    )
    from cache_manager import get_cached_reference, add_to_cache
    from api_bible_client import fetch_verse_text
    from openai_client import ask_openai
    from notes_manager import save_note
except Exception as e:
    print("\u274c Exception caught during imports!")
    print(f"Error: {e}")
    sys.exit(1)

def main():
    try:
        welcome_screen()

        user_input = input(">> ").strip()
        translation = select_translation()

        reference = get_cached_reference(translation, user_input)

        if reference:
            print(f"✅ Found in cache: {reference}")
        else:
            reference = user_input

        while True:
            try:
                verse_text = fetch_verse_text(reference, translation)
                break
            except Exception as e:
                error_message(f"Error fetching verse: {e}")
                user_input = input("\nPlease enter a new valid Bible reference: ").strip()
                reference = user_input

        show_verse(reference, verse_text)

        while True:
            choice = main_menu()

            if choice == "0":
                goodbye_message()
                break
            elif choice == "7":
                translation = select_translation()
                try:
                    verse_text = fetch_verse_text(reference, translation)
                    show_verse(reference, verse_text)
                except Exception as e:
                    error_message(f"Error switching translation: {e}")
            elif choice == "8":
                user_input = input("\nEnter a new Bible reference: ").strip()
                translation = select_translation()
                reference = get_cached_reference(translation, user_input) or user_input

                try:
                    verse_text = fetch_verse_text(reference, translation)
                    show_verse(reference, verse_text)
                except Exception as e:
                    error_message(f"Error fetching new reference: {e}")
            else:
                action_map = {
                    "1": ("Simplified Explanation", "simplify"),
                    "2": ("Modern English Version", "modern"),
                    "3": ("Historical Background", "background"),
                    "4": ("Cross References", "crossref"),
                    "5": ("Keyword Focus", "keywords"),
                    "6": ("Life Application", "lifeapp")
                }

                action_title, action_key = action_map.get(choice, (None, None))

                if not action_title:
                    error_message("Invalid choice. Please select a valid menu option.")
                    continue

                try:
                    result = ask_openai(action_key, verse_text)
                except Exception as e:
                    error_message(f"Error communicating with AI: {e}")
                    continue

                show_interpretation(action_title, result)

                if prompt_save():
                    try:
                        saved_file = save_note(
                            reference=reference,
                            translation=translation,
                            action_title=action_title,
                            content=result
                        )
                        print(f"✅ Note saved at: {saved_file}")
                    except Exception as e:
                        error_message(f"Error saving note: {e}")

    except Exception as e:
        print("\u274c Crash detected inside main()!")
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\u274c Exception caught inside __main__ startup.")
        print(f"Error: {e}")