from tkinter import *
from tkinter.ttk import *
from Csv_handler import list_place, list_time
import time as t

# Variales used
d_desired_data = "Same Day 00:00"
local_input = ""
desired_output = ""

window = Tk()
window.title("Time Converter")
window.geometry("600x400")
window.config(bg="black")

cur_time = t.gmtime()
cur_hour = cur_time.tm_hour
cur_min = cur_time.tm_min
cur_sec = cur_time.tm_sec
cur_time = f"{cur_hour}:{cur_min}:{cur_sec}"


def move_time_label():
    time_label.after(10, move_time_label)
    cur_time = t.gmtime()
    cur_hour = cur_time.tm_hour
    cur_min = cur_time.tm_min
    cur_sec = cur_time.tm_sec
    cur_time = f"{cur_hour}:{cur_min}:{cur_sec}"
    time_label["text"] = f"Current Time:{cur_time} EST"


time_label = Label(text=f"Current Time:{cur_time} EST", foreground="turquoise", font=('Courier', 10, 'normal'))
time_label.place(x=215, y=80)
move_time_label()

my_label = Label(text="Time Zone Converter", foreground="turquoise", font=('Courier', 30, 'normal'))
my_label.place(x=125, y=100)

input = Entry()
input.insert(END, string="Enter Time(00:00)")
input.config(width=17)
input.place(x=125, y=150)

my_label = Label(text=f"{d_desired_data}", padding=2, width=18)
my_label.place(x=302, y=151)


def listbox_input(event):
    # I had to use this if/else command to ensure that the command does not run when no list item is selected.
    global local_input
    selected_indices = mylist.curselection()
    if selected_indices:
        local_input = mylist.get(selected_indices)
    else:
        local_input = ""


scrollbar = Scrollbar(window)
scrollbar.place(x=278, y=181, height=85, width=14.5)
mylist = Listbox(window, height=5, yscrollcommand=scrollbar.set)
for item in list_place:
    mylist.insert(list_place.index(item), item)
mylist.bind("<<ListboxSelect>>", listbox_input)
mylist.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=mylist.yview)
mylist.place(x=123, y=180, width=155)


def listbox_output(event):
    global desired_output
    selected_indices = mylist2.curselection()
    if selected_indices:
        desired_output = mylist2.get(selected_indices)
    else:
        desired_output = ""


scrollbar = Scrollbar(window)
scrollbar.place(x=457, y=181, height=85)
mylist2 = Listbox(window, height=5, yscrollcommand=scrollbar.set)
for item in list_place:
    mylist2.insert(list_place.index(item), item)
mylist2.bind("<<ListboxSelect>>", listbox_output)
mylist2.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=mylist2.yview)
mylist2.place(x=302, y=180, width=155)


def int_converter(a):
    if a[0] == "+":
        a = a[1:]
        a = a.split(":")
        a = [-int(item) for item in a]
    elif ord(a[0]) == 8722:
        a = a[1:]
        a = a.split(":")
        a = [int(item) for item in a]
    else:
        a = a.split(":")
        a = [int(item) for item in a]
    return a


def normal_converter(a):
    if a[0] == "+":
        a = a[1:]
        a = a.split(":")
        a = [+int(item) for item in a]
    elif ord(a[0]) == 8722:
        a = a[1:]
        a = a.split(":")
        a = [-int(item) for item in a]
    return a


def button_click1():
    global a_time_difference, c_entered_time
    a_time_difference = int_converter(list_time[list_place.index(local_input)])
    c_entered_time = int_converter(input.get())


def button_click2():
    global b_time_difference
    b_time_difference = normal_converter(list_time[list_place.index(desired_output)])


def button_click3():
    d_desired_hour = c_entered_time[0] + b_time_difference[0] + a_time_difference[0]
    d_desired_min = c_entered_time[1] + b_time_difference[1] + a_time_difference[1]
    if d_desired_min > 60:
        d_desired_min -= 60
        d_desired_hour += 1
    elif d_desired_min < 0:
        d_desired_min += 60
        d_desired_hour -= 1
    else:
        d_desired_min = "00"

    if d_desired_hour < 0:
        d_desired_hour += 24
        d_desired_day = "Previous Day "
    elif d_desired_hour > 24:
        d_desired_hour -= 24
        d_desired_day = "Next Day "
    else:
        d_desired_day = "Same Day "
    d_desired_data = d_desired_day + str(d_desired_hour) + ":" + str(d_desired_min)
    my_label["text"] = d_desired_data


my_button = Button(text="Select", command=button_click1)
my_button.place(x=160, y=280)

my_button2 = Button(text="Select", command=button_click2)
my_button2.place(x=335, y=280)

my_button3 = Button(text="Convert Time", command=button_click3, width=10)
my_button3.place(x=225, y=350)
window.mainloop()
