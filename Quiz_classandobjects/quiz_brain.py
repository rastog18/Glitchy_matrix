class Game:
    def __init__(self):
        self.question_no = 0
        self.score_no = 0

    def check(self, ans, real_ans):
        if ans == real_ans:
            self.score_no += 1
            print(f"Correct\nYour current score is {self.score_no}/{self.question_no + 1}\n")

        else:
            print(f"Incorrect\nYour current score is {self.score_no}/{self.question_no + 1}\n")

    def next_question(self, question_bank):
        while len(question_bank) > self.question_no:
            ques = (question_bank[self.question_no]).question
            real_ans = ((question_bank[self.question_no]).answer).lower()
            print("Category:", (question_bank[self.question_no]).category,"\nType:",
                  (question_bank[self.question_no]).type,"\nDifficulty:",
                  (question_bank[self.question_no]).difficulty)
            print(f"Q{self.question_no + 1}:{ques}(True/False):", end="")
            ans = input().lower()
            self.check(ans, real_ans)
            self.question_no += 1
