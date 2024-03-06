from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

list_of_question = []

for question in question_data:
    list_of_question.append(Question(question['text'], question['answer']))


quiz_brain = QuizBrain(list_of_question)

while quiz_brain.still_has_question() :
    quiz_brain.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_no}")