from django.urls import path
from apps.task.views import (
    get_all_tasks,
    create_new_task,
    update_task,
    get_task_info_by_task_id,
    delete_task,
    CommentCreateView,


)

app_name = "task"

urlpatterns = [
    path("", get_all_tasks, name='all-tasks'),
    path("create/", create_new_task, name='create-task'),
    path("<int:task_id>/", get_task_info_by_task_id, name='task-info'),
    path("<int:task_id>/update/", update_task, name='update-task'),
    path("<int:task_id>.delete/", delete_task, name='delete-task'),
    path('task/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
]