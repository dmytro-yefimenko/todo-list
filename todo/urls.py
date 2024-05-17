from django.urls import path

from .views import (
    index,
    TaskCreateView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "todo"
