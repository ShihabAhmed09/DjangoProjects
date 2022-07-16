from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Candidates, JobPost
from .forms import ApplyForm, JobPostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def home(request):
    if request.user.is_authenticated:
        candidates = Candidates.objects.filter(company__name=request.user.username)
        context = {'candidates': candidates}
        return render(request, 'jobs/hr.html', context)
    else:
        job_post = JobPost.objects.all()
        context = {'job_post': job_post}
        return render(request, 'jobs/job_seeker.html', context)


@login_required(login_url='login')
def add_job_post(request):
    form = JobPostForm()
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.instance.name = request.user.company
            form.save()
            messages.success(request, 'Job post added!!!')
            return redirect('job-posts', company=request.user)
    context = {'form': form}
    return render(request, 'jobs/add_job_post.html', context)


@login_required(login_url='login')
def job_posts(request, company):
    company = get_object_or_404(Company, name=company)
    job_post = JobPost.objects.filter(name=company)
    context = {'job_post': job_post}
    return render(request, 'jobs/job_posts.html', context)


def apply(request, company, position):
    company = get_object_or_404(Company, name=company)
    # position = get_object_or_404(JobPost, position=position)
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.company = company
            form.instance.position = position
            form.save()
            messages.success(request, 'Applied Successfully!!!')
            return redirect('home')
    context = {'form': form}
    return render(request, 'jobs/apply.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                Company.objects.create(user=user, name=user)
                messages.success(request, 'Account Created Successfully!!!')
                return redirect('login')
        context = {'form': form}
        return render(request, 'jobs/register.html', context)


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
        return render(request, 'jobs/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')
