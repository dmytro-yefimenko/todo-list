from django.db import models
from django.urls import reverse


class Task(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def get_absolute_url(self):
        return reverse("todo:task-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-is_done", "-created"]


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
