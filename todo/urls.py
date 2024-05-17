from django.urls import path

from .views import (
    index,
    TaskCreateView,
    TaskStatusUpdateView,
    TaskUpdateView,
    TaskDeleteView,
)


urlpatterns = [
    path("", index, name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("task/<int:pk>/update-status/", TaskStatusUpdateView.as_view(), name="task-status-update",),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
]

app_name = "todo"
