# ---------------------------- IMPORTING ------------------------------- #
from tkinter import *
from tkinter.ttk import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#d66158"
GREEN = "#9bdeac"
GREEN2 = "#025464"
YELLOW = "#f7f5dd"
YELLOW2 = "#E8AA42"
FONT_NAME = "Courier"
WORK_MIN = 25*60
SHORT_BREAK_MIN = 5*60
LONG_BREAK_MIN = 20*60
TIMER = "00:00"
reps = 1
fn_time = None


# ---------------------------- TIMER RESET ---------------------------- #
def reset_timer():
    global reps
    window.after_cancel(fn_time)
    canvas.itemconfig(work_name, text="Pomodoro Time", fill=RED)
    canvas.itemconfig(show_timer, text=TIMER)
    canvas.itemconfig(checkpoint1, fill=YELLOW2)
    canvas.itemconfig(checkpoint2, fill=YELLOW2)
    canvas.itemconfig(checkpoint3, fill=YELLOW2)
    canvas.itemconfig(checkpoint4, fill=YELLOW2)
    reps = 1
    my_button1["state"] = "active"


# ------------------------- TIMER MECHANISM ----------------------------#
"""The reason why we can not simply call tim_calculator again again is that, then only the last one will get executed."""


def start_timer():
    global reps
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer = WORK_MIN
        canvas.itemconfig(work_name, text="Work Time", fill="#10A19D")
        time_calculator(timer)
    elif reps == 2:
        canvas.itemconfig(checkpoint1, fill=RED)
        timer = SHORT_BREAK_MIN
        canvas.itemconfig(work_name, text="Break Time", fill=GREEN2)
        time_calculator(timer)
    elif reps == 4:
        canvas.itemconfig(checkpoint2, fill=RED)
        timer = SHORT_BREAK_MIN
        canvas.itemconfig(work_name, text="Break Time", fill=GREEN2)
        time_calculator(timer)
    elif reps == 6:
        canvas.itemconfig(checkpoint3, fill=RED)
        timer = SHORT_BREAK_MIN
        canvas.itemconfig(work_name, text="Break Time", fill=GREEN2)
        time_calculator(timer)
    elif reps == 8:
        canvas.itemconfig(checkpoint4, fill=RED)
        timer = LONG_BREAK_MIN
        canvas.itemconfig(work_name, text="Break Time", fill=RED)
        time_calculator(timer)
    else:
        window.attributes('-topmost', True)
        my_button1["state"] = "active"
        canvas.itemconfig(work_name, text="Times up", fill=YELLOW)
        print("Over")


# ------------------------ COUNTDOWN MECHANISM -------------------------#
"""Window.after is an attribute allowing us to run or perform a task after a given time. It requires can have unlimited  
positional arguments. I ensured that we place the command inside the function itself, so that it runs again and again."""


def time_calculator(count):
    global reps, fn_time
    if count == -1:
        reps += 1
        start_timer()
    else:
        mins = count // 60
        sec = count % 60
        if sec < 10:
            sec = f"0{sec}"
        canvas.itemconfig(show_timer, text=f"{mins}:{sec}")
        count -= 1
        fn_time = window.after(1000, time_calculator, count)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Time")
window.geometry("600x600")

show_time = f"00:00"

img = PhotoImage(file="tv.png")
img2 = PhotoImage(file="tomato2.png")

canvas = Canvas(width=600, height=600)
canvas.create_oval(600, 600, 0, 0, fill=YELLOW2, outline="")
canvas.create_image(100, 125, image=img2)
canvas.create_image(300, 300, image=img)
checkpoint1 = canvas.create_oval(290, 460, 310, 440, fill=YELLOW2, outline="")
checkpoint2 = canvas.create_oval(290, 490, 310, 470, fill=YELLOW2, outline="")
checkpoint3 = canvas.create_oval(290, 520, 310, 500, fill=YELLOW2, outline="")
checkpoint4 = canvas.create_oval(290, 550, 310, 530, fill=YELLOW2, outline="")
show_timer = canvas.create_text(280, 310, text=f"{show_time}", font=(FONT_NAME, 35, "bold"), fill=YELLOW2)
work_name = canvas.create_text(320, 128, text="Pomodoro Time", font=(FONT_NAME, 50, "bold"), fill=RED)
canvas.config(bg="#10A19D")
canvas.place(x=0, y=0)


def button_click():
    my_button1["state"] = "disabled"
    start_timer()


my_button1 = Button(text="Start", command=button_click)
my_button1.place(x=120, y=450)

my_button2 = Button(text="Reset", command=reset_timer)
my_button2.place(x=380, y=450)

mainloop()
