rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Input 1 for rock")
print("Input 2 for paper")
print("Input 3 for scissors")

import random
a = int(input("Enter your choice:"))
b = [1,2,3]
c = random.choice(b)
d = [a,c]
print("You Choose:")
e = 0
for i in d:
    if e == 1:
        print("The Computer choose:")
    e+=1
    if i == 1:
        print("rock\n",rock)
    elif i == 2:
        print("paper\n",paper)
    elif i == 3:
        print("scissors\n",scissors)
    else:
        print("Enter a valid no.")
if (a == 1):
    if (c == 1):
        print("A Tie")
    elif (c == 2):
        print("You Loose")
    else:
        print("You Win")
elif (a == 2):
    if (c == 1):
        print("You Win")
    elif (c == 2):
        print("A Tie")
    else:
        print("You Loose")
elif (a == 3):
    if (c == 1):
        print("You Loose")
    elif (c == 2):
        print("A Win")
    else:
        print("A Tie")



