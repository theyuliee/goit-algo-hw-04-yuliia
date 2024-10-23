from pathlib import Path


def totalsalary(path):
   try:
       with open(path, 'r') as fh:
        lines = fh.readlines()

        total = 0
        for line in lines:
            name, salary = line.split(',')
            total += int(salary.strip())

        average = total / len(lines)

        return f'Загальна сума заробітної плати: {total}',  f'Середня заробітна плата: {average}'
   except FileNotFoundError:
       print(f"Помилка, файл не найдено")
   except ValueError:
       print("Помилка, файл порожній")

print(totalsalary(r'lists.txt'))