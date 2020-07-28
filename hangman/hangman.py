#!/usr/bin/env python
# PRACTICE PYTHON script
# Part 1. Pick Word
# Part 2. User guesses letters until they get it right
# Part 3. Limit incorrect guesses and allow repeated games
# http://www.practicepython.org/exercise/2016/09/24/30-pick-word.html

import random

SOWPODS_FILE = "sowpods.txt"

def random_word(filename=SOWPODS_FILE):
    """Returns a random word from a local
    copy of the SOWPODS dictionary downloaded
    from here:

    http://norvig.com/ngrams/sowpods.txt"""

    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    return random.choice(lines).strip()


print "\n --------- Hangman Game ---------"

while True:

    word = random_word().lower()

    print "\nUncover the mystery word by guessing"
    print "the letters it contains."

    found_letters = []
    incorrect_guesses = []
    correct_count = 0

    while correct_count < len(word) and len(incorrect_guesses) < 6:

        print ''.join([a + ' ' if a in found_letters else '_ ' for a in word])

        if incorrect_guesses:
            print "Incorrect guesses:", ", ".join(incorrect_guesses)
        print("{} guesses left".format(6 - len(incorrect_guesses)))

        print "Guess a new letter:"
        while True:
            c = raw_input(">").lower()
            if len(c) != 1:
                print "Enter one letter at a time"
                continue
            if c.isalpha():
                if c in incorrect_guesses or c in found_letters:
                    print "You already tried that."
                else:
                    break
            else:
                print "Must be between a-z."

        if c in word:
            found_letters.append(c)
            correct_count += word.count(c)
        else:
            incorrect_guesses.append(c)

    if correct_count == len(word):
        print word.upper()
        print "Correct.  Well done!"
    else:
        print "Hangman!  You failed to guess the word."
        print "The word is " + word

    print "Play again?"
    c = raw_input("(y/n) >")
    if c.lower().strip() != 'y':
        break
