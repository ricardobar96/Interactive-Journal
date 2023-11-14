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

start()

menu = 0

if menu == 1:
    pass
elif menu == 2:
    pass
elif menu == 3:
    pass
elif menu == 4:
    pass
elif menu == 5:
    pass
elif menu == 6:
    pass