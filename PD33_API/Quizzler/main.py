from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import *
import html


question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])
    question_answer = html.unescape(question["correct_answer"])
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


ui = UInterface(quiz_brain=quiz)
ques = quiz.next_question()
ui.change_question(ques)
ui.mainloop()

