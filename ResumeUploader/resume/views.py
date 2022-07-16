from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(View):
    def get(self, request):
        form = ResumeForm(label_suffix='')
        candidates = Resume.objects.all()
        context = {'form': form, 'candidates': candidates}
        return render(request, 'resume/home.html', context)

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES, label_suffix='')
        if form.is_valid():
            # division = form.cleaned_data['division']
            # gender = form.cleaned_data['gender']
            # preferred_job_location = form.cleaned_data['preferred_job_location']
            # print(division)
            # print(gender)
            # print(preferred_job_location)
            form.save()
            messages.success(request, f'Resume Uploaded Successfully')
            return redirect('resume:home')


class CandidateView(LoginRequiredMixin, View):
    def get(self, request, name):
        candidate = Resume.objects.get(name=name)
        context = {'candidate': candidate}
        return render(request, 'resume/candidate_view.html', context)
