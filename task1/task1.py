from pathlib import Path

file_name = Path('./salary_file.txt')

'''
Функція приймає шлях до текстового файлу, який містить інформацію
про місячні заробітні плати розробників, аналізує файл і повертає
загальну та середню суму заробітної плати всіх розробників
'''

def total_salary(path):
    salary = list()
    total = 0
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            for line in file:
                s = int(line.strip().split(',')[1])
                salary.append(s)
                total += s
    except FileNotFoundError:
        print(f"File {path} not found!")
        salary.append(1)
    return total, total//len(salary)

total, average = total_salary(file_name)
print(f"Загальна сума заробітної плати: {total}, середня заробітна плата: {average}")