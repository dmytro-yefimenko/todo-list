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


class TaskStatusUpdateView(generic.View):
    model = Task

    def post(self, request, pk) -> HttpResponseRedirect:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()

        return HttpResponseRedirect(reverse("todo:index"))


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete_form.html"
    success_url = reverse_lazy("todo:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags_list"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("todo:tags-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete_form.html"
    success_url = reverse_lazy("todo:tags-list")
