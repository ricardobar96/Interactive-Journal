from random import choice

words = ['MOUNTAIN', 'HURRICANE', 'EARTHQUAKE', 'BREAKFAST']

successes = []
failures = []
lives = 7
end_game = false

def random_word(words):
    word = choice(words)
    letters = len(set(word))

    return word, letters