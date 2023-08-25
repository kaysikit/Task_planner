from django.http import Http404
from django.shortcuts import render

from .models import Task


def index(request):
    latest_task_list = Task.objects.order_by("start_date")
    context = {"latest_task_list": latest_task_list}
    return render(request, "planner/index.html", context)


def add_task(request):
    return render(request, "planner/Add_task.html")