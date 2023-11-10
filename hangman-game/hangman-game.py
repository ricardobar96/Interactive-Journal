from random import choice

words = ['MOUNTAIN', 'HURRICANE', 'EARTHQUAKE', 'BREAKFAST']

successes = []
failures = []
lives = 7
correct = 0
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

    for letter in word:
        if letter in successes:
            solution.append(letter)
        else:
            solution.append('-')

    print(' '.join(solution))

def check_letter(letter, word, lives, correct):
    end = False

    if letter in word:
        successes.append(letter)
        correct += 1
    else:
        failures.append(letter)
        lives -= 1

    if lives == 0:
        end = lose()
    elif correct == letters:
        end = win(word)

    return lives, end, correct

def lose():
    print("YOU LOSE\nTHE WORD WAS " + word)

    return True

def win(word):
    show_word(word)
    print("YOU WIN")

    return True


word, letters = random_word(words)

while not end_game:
    print('\n' + '*' * 20 + '\n')
    show_word(word)
    print('\n')
    print("Failures: " + '-'.join(failures))
    print(f'Lives: {lives}')
    print('\n' + '*' * 20 + '\n')

    letter = ask_letter()
    lives, end, correct = check_letter(letter, word, lives, correct)

    end_game = end