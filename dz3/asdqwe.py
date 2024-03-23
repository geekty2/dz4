import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init()

print(sys.argv)
path = Path(sys.argv[1])

def print_directory_contents(path, indent=''):
    if path.is_dir():
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}/")
                print_directory_contents(item, indent + '   ')
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}")
    else:
        print(f"{Fore.RED}Шлях '{path}' не є директорією.")

directory_path = path
print_directory_contents(directory_path)
