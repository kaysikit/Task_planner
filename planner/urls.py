from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add_task/", views.add_task, name="add_task"),
    path("task/<int:task_id>", views.view_task, name="view_task"),
    path("ready/", views.view_ready_task, name="ready_task"),
]
