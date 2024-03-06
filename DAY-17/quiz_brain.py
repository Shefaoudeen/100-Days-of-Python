class QuizBrain:

    def __init__(self, list_of_question):
        self.question_no = 0
        self.question_list = list_of_question
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no}: {question.text} (True/False)?: ")
        self.check_answer(answer, question.answer)

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Oops! it's incorrect")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_no}")
        print("\n")
