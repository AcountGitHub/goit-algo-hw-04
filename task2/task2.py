from pathlib import Path

file_name = Path('./cats_file.txt')

'''
Функція приймає шлях до текстового файлу, який містить інформацію про котів,
читає файл та повертає список словників з інформацією про кожного кота
'''

def get_cats_info(path):
    cats_info = list()
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            for line in file:
                info = line.strip().split(',')
                cats_info.append({"id": info[0], "name": info[1], "age": info[2]})
    except FileNotFoundError:
        print(f"File {path} not found!")
    return cats_info

cats_info = get_cats_info(file_name)
print(cats_info)