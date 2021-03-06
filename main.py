from question_model import Question
from quiz_brain import QuizBrain
import requests
import json

response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()
data = response.json()

print(data)
question_data = json.dumps(data)

question_bank = []
for question in question_data:
    question_text = question["results"]["question"]
    question_answer = question["results"]["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
