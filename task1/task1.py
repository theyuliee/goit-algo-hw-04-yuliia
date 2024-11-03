from pathlib import Path


def totalsalary(path):
   try:
        with open(path, 'r') as fh:
            lines = fh.readlines()

            total = 0
            for line in lines:
                name, salary = line.split(',')
                total += float(salary.strip())

        average = total / len(lines)

        return total, average
   except FileNotFoundError:
       print(f"Помилка, файл не найдено")
   except ValueError:
       print("Помилка, файл порожній")

print(totalsalary(r'lists.txt'))