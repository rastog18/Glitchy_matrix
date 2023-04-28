import random


def guess_number():
    global list_guess
    while True:
        guess = int(input("\nMake a guess:"))
        if guess in list_guess:
            print("You have already guessed this number.")
        else:
            list_guess.append(guess)
            return guess


def game():
    global chances
    global number
    guess = guess_number()
    if guess == number:
        return f"You got it right, the number was {number}"
    elif guess > number:
        print("Too High")
        chances -= 1
    else:
        print("Too Low")
        chances -= 1
    if chances == 0:
        return "You Loose"


list_guess = []
number = random.randint(2, 99)
print("Welcome to number guessing game!\nI'm thinking of a number between 1 and 100.")
option = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if option == "easy":
    chances = 10
else:
    chances = 5
print(f"You have {chances} attempts remaining to guess the number.")

a = None
while a is None:
    a = game()
print(a)
