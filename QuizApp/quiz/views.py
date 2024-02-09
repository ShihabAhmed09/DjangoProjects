from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import QuestionForm
from .models import Question, Result, Attempt


def home(request):
    high_score = Result.objects.all().order_by('-score', '-time_taken').first()
    context = {'high_score': high_score}
    return render(request, 'quiz/home.html', context)


@login_required(login_url='login')
def quiz(request):
    attempt, created = Attempt.objects.get_or_create(user=request.user)
    chance = attempt.attempt
    # print(chance)
    if request.method == 'POST':
        questions = Question.objects.all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for question in questions:
            total += 1
            # print(question.answer)
            # print(request.POST.get(question.question))
            if question.answer == request.POST.get(question.question):
                score += 10
                correct += 1
            else:
                wrong += 1
        percent = (score / (total * 10)) * 100
        time = request.POST.get('timer')
        Result.objects.create(user=request.user, score=score, percentage=percent, correct=correct, incorrect=wrong,
                              total=total, time_taken=time)
        return redirect('result')
    else:
        if chance < 3:
            questions = Question.objects.all()
            attempt.attempt = chance + 1
            attempt.save()
            context = {'questions': questions}
            return render(request, 'quiz/quiz.html', context)
        else:
            return render(request, 'quiz/max_attempt_page.html')


@login_required(login_url='login')
def result(request):
    if request.user.is_staff:
        results = Result.objects.all()
        context = {'results': results}
        return render(request, 'quiz/admin_result.html', context)
    else:
        results = Result.objects.filter(user=request.user)
        context = {'results': results}
        return render(request, 'quiz/result.html', context)


@login_required(login_url='login')
def add_question(request):
    if request.user.is_superuser:
        form = QuestionForm()
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Question Added!!!')
                return redirect('question-list')
        context = {'form': form}
        return render(request, 'quiz/add_question.html', context)
    else:
        return redirect('home')


@login_required(login_url='login')
def question_list(request):
    if request.user.is_superuser:
        questions = Question.objects.all()
        context = {'questions': questions}
        return render(request, 'quiz/question_list.html', context)
    else:
        return redirect('home')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully!!!')
                return redirect('login')
        context = {'form': form}
        return render(request, 'quiz/register.html', context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'quiz/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
