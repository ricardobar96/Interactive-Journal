from random import choice

words = ['MOUNTAIN', 'HURRICANE', 'EARTHQUAKE', 'BREAKFAST']

successes = []
failures = []
lives = 7
end_game = False

def random_word(words):
    word = choice(words)
    letters = len(set(word))

    return word, letters

def ask_letter():
    letter = ''
    is_valid = False
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while not is_valid:
        letter = input("Choose a letter: ").upper()
        if letter in alphabet and len(letter) == 1:
            is_valid = True
        else:
            print("Please choose a valid letter")

    return letter

def show_word(word):
    solution = []

    for letter in successes:
        solution.append(letter)
    else:
        solution.append('-')

    print(' '.join(solution))
