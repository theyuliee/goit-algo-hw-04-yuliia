from pathlib import Path


def get_cats_info(path) :
    cats_list = []
    try:
        with open(path, 'r+') as fh:
           for line in fh :
                id, name, age = line.strip().split(',')
                cats_dict = {"id": id, "name": name, "age": age}
                cats_list.append(cats_dict)
        return cats_list
    except FileNotFoundError:
        print(f"Помилка, файл не найдено")
    except ValueError:
        print("Помилка, файл порожній")
print(get_cats_info(r'lists2'))