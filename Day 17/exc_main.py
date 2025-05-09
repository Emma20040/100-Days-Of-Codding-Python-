from data import question_data
from question_model import Question
from quize_brain import QuizeBrain

question_bank =[]
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(text= question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizeBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quize")
print(f"your final score is: {quiz.score}/{quiz.question_number}")