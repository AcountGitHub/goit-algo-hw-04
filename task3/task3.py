import sys
from pathlib import Path
from colorama import Fore

'''
Функція приймає шлях до директорії і візуалізує структуру
цієї директорії, виводячи імена всіх піддиректорій та файлів.
Для кращого візуального сприйняття, імена директорій відображаються
червоним кольором, а імена файлів - зеленим.
Також функція приймає аргумент spaces - рядок пробілів,
який використовується для кращого відображення структури директорії
'''

def parse_folder(path, spaces):
    try:
        for element in path.iterdir():
            if element.is_dir():
                print(Fore.RED + f"{spaces}folder: {element.name}")
                parse_folder(element, "  " + spaces)
            elif element.is_file():
                print(Fore.GREEN + f"{spaces}file: {element.name}")
    except FileNotFoundError:
        print(f"Directory {path} not found!")
    except NotADirectoryError:
        print(f"{path} is not a directory!")

if len(sys.argv) > 1:
    parse_folder(Path(sys.argv[1]), "")
    print(Fore.RESET)
else:
    print("Please enter the directory path in the command line arguments")