# Functions
def sum(list):
    a = False
    c = 0
    sum = 0
    for i in list:
        if (i == "A"):
            i = 11
            c += 1
            a = True
        sum = sum + i
    while c > 0:
        c = c - 1
        if (sum > 21) and (a == True):
            sum = sum - 10
    return sum


def check(l1, l2):
    y_sum = sum(l1)
    d_sum = sum(l2)
    if (y_sum <= 21) and (d_sum <= 21):
        if y_sum > d_sum:
            return ("You Win 😃")
        elif y_sum == d_sum:
            return ("Draw 🙃")
        else:
            return ("You Loose 😤")
    else:
        if y_sum > 21:
            return ("You Loose 😤")
        if d_sum > 21:
            return ("You Win 😃")


def game():
    import random

    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    y_deck = []
    d_deck = []
    for i in range(2):
        y_deck.append(random.choice(cards))
        d_deck.append(random.choice(cards))
    y_sum = sum(y_deck)
    d_sum = sum(d_deck)

    print(f"Your cards are {y_deck} and your score is {y_sum}.")
    print("Computer's first card is:", d_deck[0])

    while d_sum < 17:
        d_deck.append(random.choice(cards))
        d_sum = sum(d_deck)

    while True:
        decision = input("Type 'y' to get another card, and 'n' to pass")
        if decision == "y":
            y_deck.append(random.choice(cards))
            print(y_deck)
            y_sum = sum(y_deck)
            if y_sum == 21:
                print("Impressive Mate! A Black Jack it is.😎")
            elif y_sum >21:
                print("You have been BUSTED!")
                verdict = "You Loose"
                break
        else:
            verdict = check(y_deck, d_deck)
            break
    print(f"Your Cards were{y_deck}, current score = {y_sum}")
    print(f"Dealer's cards were {d_deck}, current score = {d_sum}")
    print(verdict)

from Black_jack_art import logo
print(logo)

while True:
    decide = input("Do you want to play a game of Black Jack ? Type 'y' or 'n':")
    if decide == "y":
        game()
    else:
        break
