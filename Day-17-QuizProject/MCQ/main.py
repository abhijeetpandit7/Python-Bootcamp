from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# List of Question objects
question_bank = []
for question in question_data:
    question_object = Question(question['question'], question['correct_answer'], question['incorrect_answers'])
    question_bank.append(question_object)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")