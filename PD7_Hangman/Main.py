# Importing from secondary file.

from Hangman_art import logo
from Hangman_art import word_list
from Hangman_art import stages
import random

# Choosing a random word
chosen_word = random.choice(word_list)
chosen_word_list = list(chosen_word)
len = len(chosen_word_list)
display = []
for i in range(len):
    display.append("_")

# MAIN
print("The word strucutre is",display)
print(logo)
chances_you_get = 6
f = []
while True:
    g = False
    guess = input("Enter your Guess Alphabet:").lower()
    # Checking if the person has already entered the word or not.
    for i in f:
        if i == guess:
            g = True
            print("You have already guessed this letter. Choose another alphabet.")
    if g == False:
        f.append(guess)
    else:
        continue
    c = 0
    d = 0
    e = 0
    for i in chosen_word_list:
        if i == guess:
            display[c] = i
            for j in display:  # Checking if the word is formed.
                if j != "_":
                    e += 1
        else:
            d += 1

        c += 1
    if e == len:
        print("You have guesssed the word:", chosen_word)
        break

    if d == len:
        chances_you_get -= 1
        print(stages[chances_you_get])
        if chances_you_get == 0:
            print("You have been Hangmanned, the word was:", chosen_word)
            break
    print(display)
