from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pickle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    a = website_input.get()
    b = email_input.get()
    c = password_input.get()
    if a == "":
        messagebox.showinfo(title="Password Writer",Message="Fill all entires")
    # is_ok = messagebox.askokcancel(title="Password Writer",message=f"Website:{a}\nPassword:{c}\nDo you wish to proceed?")
    # if is_ok:
    #     with open("data.dat", "ab") as file:
    #         data_list = [a, b, c]
    #         print(data_list)
    #         pickle.dump(data_list, file)
    #     website_input.delete(0, END)
    #     password_input.delete(0, END)

    # ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(pady=20, padx=20)
window.title("Password Writer")

img = PhotoImage(file="logo.png")
print(type(img))
canvas = Canvas(width=200, height=200)
canvas.create_image(130, 95, image=img)
canvas.grid(row=1, column=2)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=1, sticky=E)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1, sticky=E)
password_label = Label(text="Password:")
password_label.grid(row=4, column=1, sticky=E)

# Inputs
password_input = Entry(width=22)
password_input.grid(row=4, column=2, sticky=W)
website_input = Entry(width=40)
website_input.focus()
website_input.grid(row=2, column=2, columnspan=2, sticky=W)
email_input = Entry(width=40)
email_input.insert(5, "shivamrastogi605@gmail.com")
email_input.grid(row=3, column=2, columnspan=2, sticky=W)

# Buttons
button1 = Button(text="Generate Password", width=13)
button1.grid(row=4, column=3)
button2 = Button(text="Add", width=37, command=save)
button2.grid(row=5, column=2, columnspan=2)

window.mainloop()
