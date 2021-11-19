import random
from words import words


def play_hangman():
    word = random.choice(words)
    word_letters = set(word)
    used_letters = set()
    correctly_guessed = set()
    lives = 10
    while lives > 0 and word_letters != correctly_guessed:
        word_list = [letter if letter in correctly_guessed else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        letter = input("Guess a letter: ")
        if letter in used_letters:
            print("You already used this letter!")
        elif letter in word_letters:
            print("You got closer!")
            correctly_guessed.add(letter)
            used_letters.add(letter)
        elif letter not in (word_letters or used_letters):
            lives -= 1
            print("Wrong guess! Remaining lives: " + str(lives))
            used_letters.add(letter)
    if lives > 0:
        print("You got it right, the word was " + word.upper())
    else:
        print("You lost all lives, the word was " + word.upper())

play_hangman()
