from django.shortcuts import render,redirect
from Quiz.models import Question

def main(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('Users:login')
    if request.method == 'POST':
        Score = 0
        time_taken = int(request.POST.get('time_taken', 0))
        users_answers = request.POST.copy()  # Create a copy of the POST data
        # Remove the CSRF token from the copied data
        if 'csrfmiddlewaretoken' in users_answers:
            del users_answers['csrfmiddlewaretoken']
        count = 0
        for question in Question.objects.all():
            count += 1
            question_id = str(question.id)
            user_answer = users_answers.get('question_' + question_id)  # Get the selected answer

            if user_answer == question.answer:
                Score += 10
        user.score = Score
        user.time_taken = time_taken
        user.save()
        Total = count*10
        Accuracy = (Score/Total)*100
        print(f"Score = {Score} and time taken = {time_taken}s")
        context = {
            'score': Score,
            'time_taken': time_taken,
            'total': Total,
            'accuracy': Accuracy,
        }
        return render(request, 'Quiz/result.html', context)
    else:
        questions = Question.objects.all()
        context = {
            'questions': questions,
        }
        return render(request, 'Quiz/quiz.html', context)

    


