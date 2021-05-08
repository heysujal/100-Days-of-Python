from data import Settings
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

select_questions = Settings()
select_questions.get_questions()
question_data = select_questions.question_list
for question in question_data:
    # appending object of each question and answer into a list
    question_bank.append(Question(question['question'], question['correct_answer']))

# question_bank is now list of objects
brain = QuizBrain(question_bank)
while brain.still_has_questions():
    brain.next_question()

if select_questions.question_list:
    print("You have completed the quiz.")
    print(f"You final score is :{brain.score}/{brain.question_number}")
