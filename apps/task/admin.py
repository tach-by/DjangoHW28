from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
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


@admin.register(Comment)
class CommentAdminPage(DraggableMPTTAdmin):
    """
    Админ-панель модели комментариев
    """
    list_display = ('tree_actions', 'indented_title', 'task', 'creator', 'time_create', 'status')
    mptt_level_indent = 2
    list_display_links = ('task',)
    list_filter = ('time_create', 'time_update', 'creator')
    list_editable = ('status',)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)




