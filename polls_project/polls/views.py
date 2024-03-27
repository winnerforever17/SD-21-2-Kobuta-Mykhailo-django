from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm


def index(request):
    latest_questions = Question.objects.all()
    context = {'latest_questions': latest_questions}
    return render(request, 'index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = QuestionForm()
    return render(request, 'polls/create_question.html', {'form': form})


def update_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('polls:index')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'polls/update_question.html', {'form': form, 'question': question})


def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        question.delete()
        return redirect('polls:index')
    return render(request, 'polls/delete_question.html', {'question': question})
