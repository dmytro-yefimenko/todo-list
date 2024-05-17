from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.forms import TaskForm
from todo.models import Tag, Task


def index(request) -> HttpResponse:
    """View function for the home page of the site."""

    tasks_list = Task.objects.all()

    context = {
        "tasks_list": tasks_list
    }

    return render(request, template_name="todo/index.html", context=context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")





