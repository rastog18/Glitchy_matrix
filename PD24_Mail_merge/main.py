
with open("./Input/Letters/starting_letter.txt", "r") as file_letter:
    a = file_letter.read()
    print(a)

with open("./Input/Names/invited_names.txt", "r") as file_name:
    name = file_name.readlines()

for j in name:
    j = j.strip()
    with open(f"./Output/ReadyToSend/letter_for_{j}.txt", "w") as file_write:
        letter = a.replace("[name]",f"{j}")
        file_write.write(letter)
