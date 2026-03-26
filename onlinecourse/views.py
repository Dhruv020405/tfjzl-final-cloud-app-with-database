from django.shortcuts import render, redirect
from .models import Submission, Choice

def submit(request, course_id):
    if request.method == 'POST':
        selected_choices = request.POST.getlist('choice')
        
        submission = Submission.objects.create(enrollment_id=1)
        submission.choices.set(selected_choices)

        return redirect('show_exam_result', submission_id=submission.id)

def show_exam_result(request, submission_id):
    submission = Submission.objects.get(id=submission_id)
    
    selected_choices = submission.choices.all()
    score = submission.choices.count()

    context = {
        'score': score,
        'choices': selected_choices
    }

    return render(request, 'onlinecourse/result.html', context)