import os
from pathlib import Path
from os import system

entries_path = Path("Entries")

def count_entries(path):
    counter = 0
    for txt in Path(path).glob("**/*.txt"):
        counter += 1
    return counter

def start():
    system('cls')
    print('*' * 50)
    print('*' * 5 + " JOURNAL INITIATED " + '*' * 5)
    print('*' * 50)
    print("\n")
    print(f"Total entries: {count_entries(entries_path)}")

    option_menu = 'x'
    while not option_menu.isnumeric() or int(option_menu) not in range(1,7):
        print("Choose an option:")
        print('''
        [1] - Read entry
        [2] - New entry
        [3] - New category
        [4] - Delete entry
        [5] - Delete category
        [6] - Exit''')
        option_menu = input()
    return option_menu

def show_categories(path):
    print("Categories:")
    categories_path = Path(path)
    list_categories = []
    counter = 1

    for folder in categories_path.iterdir():
        folder_str = str(folder.name)
        print(f"[{counter}] - [{folder_str}]")
        list_categories.append(folder)
        counter += 1
    return list_categories

def choose_category(list):
    option_correct = "x"

    while not option_correct.isnumeric() or int(option_correct) not in range(1, len(list + 1)):
        option_correct = input("\nChoose a category: ")

    return list[int(option_correct) - 1]

def show_entries(path):
    print("Entries:")
    all_entries_path = Path(path)
    list_entries = []
    counter = 1

    for entry in all_entries_path.glob('*.txt'):
        entry_str = str(entry.name)
        print(f"[{counter}] - [{entry_str}]")
        list_entries.append(entry)
        counter += 1
    return list_entries

def choose_entry(list):
    option_entry = "x"

    while not option_entry.isnumeric() or int(option_entry) not in range(1, len(list + 1)):
        option_entry = input("\nChoose an entry: ")

    return list[int(option_entry) - 1]

def read_entry(entry):
    print(Path(read_entry(entry)))

def create_entry(path):
    exists = False

    while not exists:
        print("Write the name of your entry: ")
        name_entry = input() + '.txt'
        print("Write your new entry: ")
        content_entry = input()
        path_new = Path(path, name_entry)

        if not os.path.exists(path_new):
            Path.write_text(path_new, content_entry)
            print(f"Your entry {name_entry} was created")
            exists = True
        else:
            print("Entry already exists")

start()

menu = 0

if menu == 1:
    categories = show_categories(entries_path)
    category = choose_category(categories)
    all_entries = show_entries(category)
    single_entry = choose_entry(all_entries)
    read_entry(single_entry)
    pass
elif menu == 2:
    categories = show_categories(entries_path)
    category = choose_category(categories)
    create_entry(category)
    pass
elif menu == 3:
    pass
elif menu == 4:
    categories = show_categories(entries_path)
    category = choose_category(categories)
    all_entries = show_entries(category)
    single_entry = choose_entry(all_entries)
    pass
elif menu == 5:
    categories = show_categories(entries_path)
    category = choose_category(categories)
    pass
elif menu == 6:
    pass