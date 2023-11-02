import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Quiz_App.settings")

django.setup()

from Quiz.models import Question

def read_and_add(file_path):
    if not os.path.exists(file_path):
        print(f"Json file not found{file_path}")
        return
    with open(file_path, 'r') as json_file:
        questions = json.load(json_file)['questions']

    print
        
    for question_data in questions:
        question = Question(
            text=question_data['text'],
            op1=question_data['op1'],
            op2=question_data['op2'],
            op3=question_data['op3'],
            op4=question_data['op4'],
            answer=question_data['answer']
        )
        question.save()

if __name__ == '__main__':
    path = 'C:/Users/Administrator/Desktop/WEBPROJECTS/Django-Quizz-App/Quiz_App/questions/questions.json'
    read_and_add(path)
    print("Added questions succesfully")

