from django.shortcuts import render
from .models import *


def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/list.html', context)
