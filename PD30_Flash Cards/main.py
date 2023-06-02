# ---------------------------- IMPORT/Variable------------------------------- #
from tkinter import *
import random
import pandas
index = None
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FILE MANAGEMENT ------------------------------- #
try:
    file = pandas.read_csv("Words_to_learn.csv")
except FileNotFoundError:
    file = pandas.read_csv("./data/french_words.csv")

file_dict = {value["French"]: value["English"] for (key, value) in file.iterrows()}
keys = list(file_dict.keys())
values = list(file_dict.values())
print(keys,values)


def show_word(index):
    canvas.itemconfig(word_lng, text="English")
    canvas.itemconfig(word_bg, image=img2)
    choice_eng = values[index]
    canvas.itemconfig(word_choice, text=choice_eng)


def change_word_right():
    global index,command,change_word_scheduled
    window.after_cancel(command)
    print(keys[index],values[index])
    keys.remove(keys[index])
    values.remove(values[index])
    new_word_dict = {"French": keys, "English": values}
    data = pandas.DataFrame(new_word_dict)
    data.to_csv("Words_to_learn.csv")
    canvas.itemconfig(word_lng, text="French")
    canvas.itemconfig(word_bg, image=img)
    choice = random.choice(keys)
    index = keys.index(choice)
    print(choice, index)
    canvas.itemconfig(word_choice, text=choice)
    command = window.after(3000, show_word, index)


def change_word_wrong():
    global command,index
    canvas.itemconfig(word_lng, text="French")
    canvas.itemconfig(word_bg, image=img)
    choice = random.choice(keys)
    index = keys.index(choice)
    print(choice,index)
    canvas.itemconfig(word_choice, text=choice)
    command = window.after(3000, show_word, index)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
img = PhotoImage(file="/Users/shivam/PycharmProjects/Udemy/Intermediate/Tkinter/Flash Cards/images/card_front.png")
img2 = PhotoImage(file="/Users/shivam/PycharmProjects/Udemy/Intermediate/Tkinter/Flash Cards/images/card_back.png")
word_bg = canvas.create_image(400, 262, image=img)
word_lng = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill="black")
word_choice = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
change_word_wrong()
canvas.grid(row=1, column=1, columnspan=2)

# Buttons
my_image = PhotoImage(file="./images/right.png")
wrong_button = Button(image=my_image, highlightthickness=0, borderwidth=0, command=change_word_right)
wrong_button.grid(row=2, column=2)

my_image2 = PhotoImage(file="./images/wrong.png")
right_button = Button(image=my_image2, highlightthickness=0, borderwidth=0, command=change_word_wrong)
right_button.grid(row=2, column=1)

mainloop()
