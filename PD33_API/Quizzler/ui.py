from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


# TODO-1 The note here is an explanation: In the program we learn how to use one class in another class. We first import the class, and pass it as a parameter while defining the second class.
class UInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.window.title("Quizler")

        self.label = Label(text=f"Score:{self.quiz.score}", bg=THEME_COLOR)
        self.label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.config(bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="LOL", font=("Arial", 20, "italic"), fill="black",
                                                     width=275)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

        self.img_right = PhotoImage(file="./images/true.png")
        self.img_wrong = PhotoImage(file="./images/false.png")

        self.button = Button(image=self.img_wrong, highlightthickness=0, borderwidth=0, command=self.cross)
        self.button.config(bg=THEME_COLOR, justify=CENTER)
        self.button.grid(column=1, row=3)

        self.button2 = Button(image=self.img_right, highlightthickness=0, borderwidth=0, command=self.tick)
        self.button2.config(bg=THEME_COLOR)
        self.button2.grid(column=2, row=3)

    def change_question(self, ques):
        self.canvas.itemconfig(self.question_text, text=ques)

    def tick(self):
        if self.quiz.question_number < 10:
            self.quiz.check_answer(user_answer="True")
            self.label.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
            self.change_screen_color()

        elif self.quiz.question_number == 10:
            self.quiz.check_answer(user_answer="True")
            self.canvas.config(bg="yellow")
            self.label.config(text="")
            self.canvas.itemconfig(self.question_text,text=f"Score:{self.quiz.score}/{self.quiz.question_number}",fill="red")
            self.button.config(state=DISABLED)
            self.button2.config(state=DISABLED)

    def cross(self):
        if self.quiz.question_number < 10:
            self.quiz.check_answer(user_answer="False")
            self.label.config(text=f"Score:{self.quiz.score}/{self.quiz.question_number}")
            self.change_screen_color()

        elif self.quiz.question_number == 10:
            self.quiz.check_answer(user_answer="False")
            self.canvas.config(bg="yellow")
            self.label.config(text="")
            self.canvas.itemconfig(self.question_text, text=f"Score:{self.quiz.score}/{self.quiz.question_number}",
                                   fill="red")
            self.button.config(state=DISABLED)
            self.button2.config(state=DISABLED)

    def change_screen_color(self):
        ques1 = self.quiz.next_question()
        if self.quiz.variable_brain == "Right":
            self.canvas.config(bg="green")
        elif self.quiz.variable_brain == "Wrong":
            self.canvas.config(bg="red")
        self.window.after(500,self.change_white,ques1)

    def change_white(self,ques1):
        self.canvas.config(bg="white")
        self.change_question(ques1)

    def mainloop(self):
        self.window.mainloop()
