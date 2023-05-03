from quiz_data import question_data
from quiz_brain import Game


class Question:
    def __init__(self, text, answer, category, Type, difficulty):
        self.category = category
        self.type = Type
        self.difficulty = difficulty
        self.question = text
        self.answer = answer


question_bank = []
for i in range(len(question_data)):
    Object = "question" + str(i)
    Object = Question(question_data[i]["text"], question_data[i]["answer"], question_data[i]["category"],
                      question_data[i]["type"], question_data[i]["difficulty"])
    question_bank.append(Object)

user = Game()
user.next_question(question_bank)
print(f"\nYou have completed the Quiz\nYour final score was {user.score_no}/{user.question_no}")
