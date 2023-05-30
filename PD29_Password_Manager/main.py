from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pickle
import random
import pyperclip

# Since messagebox is not a class, it is not imported by "*"

init_window = Tk()
init_window.geometry("400x300")
init_window.config(bg="turquoise")
init_window.title("Password Manager")

init_img = PhotoImage(file="logo.png")
init_canvas = Canvas(width=200, height=200, bg="turquoise", highlightthickness=0)
init_canvas.create_image(130, 95, image=init_img)
init_canvas.place(x=70, y=0)

init_label = Label(text="To access the portal enter your password here:")
init_label.place(x=50, y=180)

init_pass = Entry(width=18)
init_pass.insert(0, "Password")
init_pass.focus()
init_pass.place(x=50, y=217)

radio_state = IntVar()
radiobutton1 = Radiobutton(text="Writer", value=1, variable=radio_state,width=9)
radiobutton2 = Radiobutton(text="Reader", value=2, variable=radio_state,width=9)
radiobutton1.place(x=240, y=210)
radiobutton2.place(x=240, y=230)
# init_entry = Entry(width=10)
# init_entry.insert(0, "Reader/Writer")
# init_entry.place(x=237, y=210)


def take_info():
    password = init_pass.get()
    print(password)
    if password == "WELHAM":
        purpose = radio_state.get()
        print(purpose)
        if purpose == 1:
            password_adder()
        elif purpose == 2:
            password_reader()
        else:
            messagebox.showerror(title="Password Manager", message="Select your Purpose Correctly")
    else:
        messagebox.showerror(title="Password Manager",message="Wrong Password")
        pass


init_button = Button(text="Enter", command=take_info, width=20)
init_button.place(x=85, y=255)
messagebox.showinfo(title="Password Manager", message="Double Check the data before you enter your data.")


def password_reader():
    init_canvas.delete("all")
    init_window.destroy()

    window = Tk()
    window.config(pady=20, padx=20)
    window.title("Password Reader")

    with open("data.dat", "rb") as file:
        a = True
        ROW = 1
        while a:
            try:
                data = pickle.load(file)
                website_label = Label(text=f"Website:{data[0]} | Email:{data[1]} | Password:{data[2]}")
                website_label.grid(row=ROW, column=1, sticky=W)
                ROW += 1
                print()
            except EOFError:
                a = False


def password_adder():
    # I tried using messagebox to make the program better, but I found that the messagebox does not run in this function.
    init_canvas.delete("all")
    init_window.destroy()

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_pass():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        nr_letters = random.randint(8,10)
        nr_symbols = random.randint(3,5)
        nr_numbers = random.randint(3,5)

        a = random.sample(letters, nr_letters)
        b = random.sample(symbols, nr_symbols)
        c = random.sample(numbers, nr_numbers)

        new_list = a + b + c
        random.shuffle(new_list)
        passcode = "".join(new_list)
        pyperclip.copy(passcode)
        password_input.insert(0,passcode)
    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save():
        a = website_input.get()
        b = email_input.get()
        c = password_input.get()
        print(a, b, c)
        # is_ok = messagebox.askokcancel(title="Password Writer",message=f"Website:{a}\nPassword:{c}\nDo you wish to proceed?")
        # if is_ok:
        with open("data.dat", "ab") as file:
            data_list = [a, b, c]
            print(data_list)
            pickle.dump(data_list, file)
        website_input.delete(0, END)
        password_input.delete(0, END)

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
    email_input.insert(0, "shivamrastogi605@gmail.com")
    email_input.grid(row=3, column=2, columnspan=2, sticky=W)

    # Buttons

    button1 = Button(text="Generate Password", width=13,command=generate_pass)
    button1.grid(row=4, column=3)
    button2 = Button(text="Add", width=37, command=save)
    button2.grid(row=5, column=2, columnspan=2)

    window.mainloop()


mainloop()
