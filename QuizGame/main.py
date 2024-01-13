from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quest_ans in question_data:
    question_bank.append(Question(quest_ans['question'], quest_ans['correct_answer']))

newQuiz = QuizBrain(question_bank)

while newQuiz.still_has_question():
    newQuiz.next_question()

print("You completed the quiz")
print(f"Your total score was {newQuiz.score}/{newQuiz.question_number}")
