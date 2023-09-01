from django.shortcuts import render, redirect

from .models import Task
from.forms import AddTaskForm, ChangeTaskStatus


def index(request):
    latest_task_list = Task.objects.order_by("-id")
    context = {
        "latest_task_list": latest_task_list,
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
    return render(request, "planner/addTask.html", context)


def view_task(request, task_id):
    latest_task_list = Task.objects.filter(pk=task_id)
    form = ChangeTaskStatus()
    context = {
        "latest_task_list": latest_task_list,
        "form": form,
    }
    return render(request, "planner/task.html", context)
