from django.db import models
from django.contrib.auth.admin import User


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Task(models.Model):
    title = models.CharField(max_length=30, default='Enter title: ')
    description = models.TextField(max_length=100)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.ForeignKey(
        Status,
        on_delete=models.SET(1),
        blank=True,
        null=True
    )

    date_started = models.DateField(help_text="Дата начала")
    deadline = models.DateField(help_text="Дата окончания")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def str(self):
        return f"{self.title[:10]}..."

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')