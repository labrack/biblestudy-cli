# rich_ui.py

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def welcome_screen():
    console.rule("[bold blue]📖 Welcome to the Bible Study CLI 📖", style="blue")
    console.print("\nEnter a Bible reference (e.g., [bold]John 3:16[/bold]) or a snippet of scripture.\n")

def select_translation():
    console.print("[bold green]Which translation would you like to use?[/bold green]")
    console.print("[1] NIV\n[2] KJV\n[3] NKJV\n[4] NLT\n[5] CSB")
    choice = Prompt.ask("\nEnter the number for your translation", choices=["1", "2", "3", "4", "5"])
    translation_map = {
        "1": "NIV",
        "2": "KJV",
        "3": "NKJV",
        "4": "NLT",
        "5": "CSB"
    }
    return translation_map[choice]

def main_menu():
    console.rule("[bold green]What would you like to do?[/bold green]")
    console.print("[1] ✏️  Simplify")
    console.print("[2] 🗣️  Modern English")
    console.print("[3] 🏺 Background")
    console.print("[4] 🔗 Cross-References")
    console.print("[5] 🔍 Keyword Focus")
    console.print("[6] 🛠️ Life Application")
    console.print("[0] 🚪 Exit")
    choice = Prompt.ask("\nChoose an option (0-6)", choices=["0", "1", "2", "3", "4", "5", "6"])
    return choice

def show_verse(reference, verse_text):
    console.rule(f"[bold cyan]📜 {reference}[/bold cyan]")
    console.print(Panel(verse_text.strip(), expand=False))

def show_interpretation(title, content):
    console.rule(f"[bold magenta]{title}[/bold magenta]")
    console.print(Panel(content.strip(), expand=False))

def prompt_save():
    save_choice = Prompt.ask("\nWould you like to save this result to your notes?", choices=["y", "n"])
    return save_choice.lower() == "y"

def goodbye_message():
    console.rule("[bold red]👋 Goodbye! Thanks for using the Bible Study CLI[/bold red]")

def error_message(msg):
    console.print(f"[bold red]Error:[/bold red] {msg}")