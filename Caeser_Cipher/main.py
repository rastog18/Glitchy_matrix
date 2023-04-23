alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
"""we make a list of the text entered. One by one we locate each iteration in the list of alphabet and then we alter 
the text list by updating  +shift value"""


def ceaser():
    text = input("Enter the text:").lower()
    text_list = list(text)
    shift = int(input("Enter the shift number:"))
    while shift > 25:
        shift = shift - 25
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    for i in range(len(text)):
        try:
            e = alphabet.index(text_list[i])
            if direction == 'encode':
                e = e + shift
                if e > 25:
                    e = e - 26
            elif direction == 'decode':
                e = e - shift
                if e < 0:
                    e = 26 + e
            text_list[i] = alphabet[e]
        except ValueError:
            pass
    end_str = ""
    for i in text_list:
        end_str = end_str + i
    print(end_str)


# MAIN
from art import logo
print (logo)
print("To run the coding machine enter 'run', else enter 'break'.")
while True:
    a = input("Enter your choice").lower()
    if a == "run":
        ceaser()
    else:
        break
