import time
import os
import sys
from prettytable import PrettyTable

# Colors
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

def slow_print(text, delay=0.002):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{CYAN}Initializing JuanDevID Terminal Portfolio...{RESET}")
    loading_stages = [
        "[                    ] 0%",
        "[=====               ] 25%",
        "[==========          ] 50%",
        "[===============     ] 75%",
        "[====================] 100%"
    ]
    for stage in loading_stages:
        print(f"\r{BLUE}{stage}{RESET}", end='')
        time.sleep(0.8)
    print()
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def display_logo():
    logo = f"""
{CYAN}
   ___                  ______         ___________ 
  |_  |                 |  _  \\       |_   _|  _  \\ 
    | |_   _  __ _ _ __ | | | |_____   _| | | | | | 
    | | | | |/ _` | '_ \\| | | / _ \\ \\ / | | | | | | 
/\\__/ | |_| | (_| | | | | |/ |  __/\\ V _| |_| |/ / 
\\____/ \\__,_|\\__,_|_| |_|___/ \\___| \\_/\\___/|___/  
{RESET}
    """
    print(logo)

def header():
    print(f"{BOLD}{BLUE}╔════════════════════════════════════════════════════════╗{RESET}")
    slow_print(f"{BOLD}{CYAN}║  Welcome to JuanDevID's Professional Terminal Portfolio  ║{RESET}", 0.0015)
    print(f"{BOLD}{BLUE}╚════════════════════════════════════════════════════════╝{RESET}\n")
    print(f"Type {CYAN}help{RESET} to see available commands.\n")

def show_help():
    table = PrettyTable()
    table.field_names = [f"{BOLD}{CYAN}Command{RESET}", f"{BOLD}{CYAN}Description{RESET}"]
    table.add_row(["help", "See available commands"])
    table.add_row(["about", "Learn more about JuanDevID"])
    table.add_row(["projects", "View the latest projects"])
    table.add_row(["contact", "Contact information and links"])
    table.add_row(["clear", "Clear the screen and reset terminal"])
    table.add_row(["exit", "Exit the terminal portfolio"])
    table.add_row(["social", "View social media and other networks"])
    
    print(table)

def show_about():
    table = PrettyTable()
    table.field_names = [f"{BOLD}{CYAN}About Me{RESET}", ""]
    table.add_row(["Name", "JuanDevID"])
    table.add_row(["Profession", "Developer | Creative Technologist"])
    table.add_row(["Focus", "Innovative tech solutions with elegant design"])
    table.add_row(["Passion", "Programming, AI, and Future Technologies"])
    
    print(table)

def show_projects():
    table = PrettyTable()
    table.field_names = [f"{BOLD}{CYAN}Project{RESET}", f"{BOLD}{CYAN}Description{RESET}"]
    table.add_row(["Terminal Portfolio CLI", "An interactive terminal-based portfolio for showcasing skills."])
    table.add_row(["AI Chatbots", "Creating AI-powered chatbots for various applications."])
    table.add_row(["Web Development", "Building full-stack web applications with cutting-edge technologies."])
    table.add_row(["Machine Learning", "Exploring ML models and AI tools for real-world applications."])
    
    print(table)

def show_contact():
    table = PrettyTable()
    table.field_names = [f"{BOLD}{CYAN}Contact Info{RESET}", ""]
    table.add_row(["GitHub", "https://github.com/JuanDevID"])
    table.add_row(["Twitter", "https://twitter.com/EOSD_Sakuya"])
    table.add_row(["LinkedIn", "https://linkedin.com/in/juandevid"])
    table.add_row(["Email", "juandevid@example.com"])
    
    print(table)

def show_social():
    table = PrettyTable()
    table.field_names = [f"{BOLD}{CYAN}Social Media{RESET}", ""]
    table.add_row(["GitHub", "https://github.com/JuanDevID"])
    table.add_row(["Twitter", "https://twitter.com/EOSD_Sakuya"])
    table.add_row(["Instagram", "https://instagram.com/JuanDevID"])
    table.add_row(["LinkedIn", "https://linkedin.com/in/juandevid"])
    
    print(table)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    display_logo()
    header()

def main():
    loading_animation()
    display_logo()
    header()

    while True:
        command = input(f"{CYAN}[JuanDevID]$ {RESET}").strip().lower()

        if command == "help":
            show_help()
        elif command == "about":
            show_about()
        elif command == "projects":
            show_projects()
        elif command == "contact":
            show_contact()
        elif command == "social":
            show_social()
        elif command == "clear":
            clear_screen()
        elif command == "exit":
            print(f"{CYAN}Thank you for visiting. Goodbye!{RESET}")
            sys.exit()
        else:
            print(f"{BOLD}{WHITE}Command not found.{RESET} Type {CYAN}help{RESET} to see available commands.")

if __name__ == "__main__":
    main()
