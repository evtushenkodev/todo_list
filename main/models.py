from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created = models.DateField(blank=False)

    def __str__(self):
        return self.Title