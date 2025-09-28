from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True, null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
