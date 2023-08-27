from django.shortcuts import render, redirect

from .models import Task, Status
from.forms import AddTaskForm


def index(request):
    latest_task_list = Task.objects.order_by("-id")
    status_list = Status.objects.all()
    context = {
        "latest_task_list": latest_task_list,
        "status_list": status_list,
    }
    return render(request, "planner/index.html", context)


def add_task(request):
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddTaskForm()
    context = {
        'form': form
    }
    return render(request, "planner/Add_task.html", context)