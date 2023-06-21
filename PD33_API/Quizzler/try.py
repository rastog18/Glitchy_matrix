from tkinter import *

THEME_COLOR = "#375362"


# TODO-1 The note here is an explanation: In the program we learn how to use one class in another class. We first import the class, and pass it as a parameter while defining the second class.
class UInterface:
    def __init__(self):
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizler")

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="LOL", font=("Arial", 20, "italic"), fill="black",
                                                     width=275)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.img_right = PhotoImage(file="./images/true.png")
        self.img_wrong = PhotoImage(file="./images/false.png")

        self.button = Button(image=self.img_wrong, highlightthickness=0, borderwidth=0)
        self.button.config(bg=THEME_COLOR, justify=CENTER)
        self.button.grid(column=1, row=3)

        self.button2 = Button(image=self.img_right, highlightthickness=0, borderwidth=0, command=self.tick)
        self.button2.config(bg=THEME_COLOR)
        self.button2.grid(column=2, row=3)
        self.window.mainloop()

    def tick(self):
        self.canvas.config(bg="red")

    # def mainloop(self):
    #     self.window.mainloop()


ui = UInterface()
