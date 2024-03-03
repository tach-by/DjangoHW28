from django.contrib import admin
from apps.task.models import (
    Task,
    Status,
    Comment

)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',  'status', 'creator', 'created_at')
    list_filter = ('status', 'creator', 'created_at')
    search_fields = ('title',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'user', 'task')
    list_filter = ('text',)
    search_fields = ('text',)




