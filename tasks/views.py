from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()  # в случае со связ формой
        return redirect('/')  # редирект
    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()  # в случае со связ формой
        return redirect('/')  # редирект
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    task = Task.objects.get(pk=pk)
    # form = TaskForm(instance=task)
    if request.method == 'POST':
        task.delete()
        return redirect('/')  # редирект
    context = {'task': task}
    return render(request, 'tasks/delete.html', context)
