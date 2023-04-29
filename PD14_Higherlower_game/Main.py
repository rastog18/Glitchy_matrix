#Replit is a module from replit website.
from art import logo
from art import vs
from game_data import data
from replit import clear
import random


def game(current_score):
    print(logo)
    random.shuffle(data)
    c = 0
    a = True
    while a is True:
        print(f"Compare A: {data[c]['name']},a {data[c]['description']},from {data[c]['country']}.")
        a_follower = data[c]['follower_count']
        c += 1
        print(vs)
        print(f"Against B: {data[c]['name']},a {data[c]['description']},from {data[c]['country']}.")
        b_follower = data[c]['follower_count']
        print(a_follower,b_follower)
        decision = input("Who has more followers? Type 'A' or 'B':")
        if a_follower > b_follower:
            if decision == "A":
                current_score += 1
                a = True
                clear()
                print(logo)
                print("You're right! Current Score:", current_score)
            else:
                a = False
                clear()
                print(logo)
                print("Sorry that's wrong. Final Score:", current_score)
        else:
            if decision == "B":
                current_score += 1
                a = True
                clear()
                print(logo)
                print("You're right! Current Score:", current_score)
            else:
                a = False
                clear()
                print(logo)
                print("Sorry that's wrong. Final Score:", current_score)


# Main
current_score = 0
game(current_score)
