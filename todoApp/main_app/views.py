from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TaskCreateForm, TaskUpdateForm
from .models import Task
from django.db.models import Q


def home(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, f'Task Added Successfully')
            return redirect('main_app:home')
    else:
        form = TaskCreateForm(label_suffix='')

    tasks = Task.objects.all()

    query = request.GET.get('q')

    if query:
        query = query.strip()
        tasks = tasks.filter(Q(name__icontains=query))
    else:
        tasks = tasks

    task_left = tasks.filter(completed='False').count()
    task_completed = tasks.filter(completed='True').count()

    context = {'form': form, 'tasks': tasks, 'task_left': task_left, 'task_completed': task_completed}
    return render(request, 'main_app/home.html', context)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task, label_suffix='')
        if form.is_valid():
            form.save()
            messages.success(request, f'Task Updated Successfully')
            return redirect('main_app:home')
    else:
        form = TaskUpdateForm(instance=task, label_suffix='')
    context = {'form': form}
    return render(request, 'main_app/update_task.html', context)


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted")
        return redirect('main_app:home')
    context = {'task': task}
    return render(request, 'main_app/delete_task.html', context)
