from django.shortcuts import render,redirect
from Quiz.models import Question
from Users.forms import CustomUserLoginForm

def main(request):
    user = request.user
    if request.method == 'GET':
        if user.is_authenticated:
            questions = Question.objects.all()
            context = {
                'questions': questions,
            }
            return render(request, 'Quiz/quiz.html',context)
        else:
            return redirect('Users:login')  
    else:
        Score = 0
        Question.objects.all()
        users_answers = request.POST
        time_taken = int(request.POST.get('time_taken', 0)) 
        for question_id, user_answer in users_answers.items():
            try:
                question = Question.objects.get(id=question_id)
            except Question.DoesNotExist:
                continue
            if user_answer == question.answer:
                Score += 10
        user.score = Score
        user.time_taken = time_taken
        user = user.save()
        print(f"Score = {Score} and time taken = {time_taken}")
        context = {
            'score': Score,
            'time_taken': time_taken,
        }
        return render(request,'Quiz/result.html',context)