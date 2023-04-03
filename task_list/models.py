from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=63, default="Task" )
    created_datetime = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateField(null=True, blank=True)
    deadline_time = models.TimeField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    def __str__(self):
        return self.name

