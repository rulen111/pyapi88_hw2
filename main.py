# PYAPI-88 Homework #2. Opening and reading a file, writing to a file. Student Akhmarov Ruslan

# Tasks 1 and 2. Defining functions to read a recipe from file and get a shop list of ingredients
def read_recipe(file, recipes_dict):
    """Takes path to a file to read and recipes dictionary, reads one recipe from file
    and adds it to the recipes dictionary. Returns flag_cont variable
    which indicates whether it is not the end of the file yet."""
    flag_cont = True
    dish_name = file.readline().strip()
    if dish_name == "":
        flag_cont = False

    if flag_cont:
        num_ingred = int(file.readline().strip())
        ingred_line = file.readline().strip().split(" | ")
        ingred_list = []

        for _ in range(num_ingred):
            ingred_list += [ingred_line]
            ingred_line = file.readline().strip().split(" | ")

        recipes_dict[dish_name] = [{'ingredient_name': item[0], 'quantity': int(item[1]), 'measure': item[2]}
                                   for item in ingred_list]

        return flag_cont
    else:
        return flag_cont


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    """Takes cook_book dictionary, list of requested dishes and a person count.
    Returns a dictionary which consists of ingredients' names as keys
    and the amount needed as values."""
    shop_list = {}
    for dish in dishes:
        ingred_list = cook_book[dish]

        for ingred in ingred_list:
            if ingred['ingredient_name'] in shop_list.keys():
                shop_list[ingred['ingredient_name']]['quantity'] += ingred['quantity'] * person_count
            else:
                shop_list[ingred['ingredient_name']] = {'measure': ingred['measure'],
                                                        'quantity': ingred['quantity'] * person_count}

    return shop_list


# Task 3. Defining functions to get the number of lines in a file, sort files by this number and write to a new file
def file_len(fp):
    """Takes filepath, opens this file and returns the number of lines in this file"""
    with open(fp, encoding="UTF-8") as file:
        length = sum([1 for _ in file])

    return length


def sort_files(files_list):
    """Takes a list of files and returns a new list which consists of
    file's name, file's data and the number of lines in this file.
    This new list is sorted by the number of lines in each file."""
    sorted_list = []
    for file in files_list:
        length = file_len(file)
        name = file.split('/')[-1]
        with open(file, encoding="UTF-8") as currf:
            data = currf.read()
        sorted_list.append((name, data, length))

    sorted_list = sorted(sorted_list, key=lambda x: x[2])

    return sorted_list


def write_files(sorted_files_list, fp_to_write):
    """Takes a sorted list of files and a path to write.
    Combines given files, formats data by rules described in task description.
    Writes resulting data to a new file."""
    with open(fp_to_write, 'w', encoding="UTF-8") as out_file:
        for item in sorted_files_list:
            out_file.write(f'{item[0]}\n{item[2]}\n{item[1]}\n')


# Task 1 and 2. Calling defined functions and printing the results of given tasks.
recipes = {}
with open("files/recipes.txt", encoding="UTF-8") as f:
    flag = True
    while flag:
        flag = read_recipe(f, recipes)

print(f'Получившийся после прочтения файла кулинарный словарь:\n{recipes}')
print(f'\nПолучившийся список покупок для Цезаря и Омлета на 3 человек:\n'
      f"{get_shop_list_by_dishes(recipes, ['Салат Цезарь', 'Омлет'], 3)}")

# Task 3. Calling defined functions and printing the results of given task.
files = ["files/1.txt", "files/2.txt", "files/3.txt"]
sorted_files = sort_files(files)
print(f'\nСписок файлов (имя, содержимое и количество строк) после сортировки\n{sorted_files}')
write_files(sorted_files, "files/sorted_files.txt")
