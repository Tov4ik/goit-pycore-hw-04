# Завдання 3

import sys
from pathlib import Path
from colorama import init, Fore, Style
init()

def print_directory_tree(directory, indent=""):
    try:
        for item in sorted(directory.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}/")
                print_directory_tree(item, indent + "    ")
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied]{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print("Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.")
        return
    path_str = sys.argv[1]
    path = Path(path_str)
    if not path.exists():
        print(f"Шлях не існує: {path_str}")
        return
    if not path.is_dir():
        print(f"Це не директорія: {path_str}")
        return
    print(f"\nСтруктура директорії: {path.resolve()}\n")
    print_directory_tree(path)

if __name__ == "__main__":
    main()
