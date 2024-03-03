from django.urls import path
from apps.task.views import (
    get_all_tasks,
    create_new_task,
    update_task,
    delete_task,
    add_comment,
    task_info,
    reply_comment_view



)

app_name = "task"

urlpatterns = [
    path('task/<int:task_id>/', task_info, name='task-info'),
    path('task/<int:task_id>/add_comment/', add_comment, name='add_comment'),
    path('comment/reply/<int:comment_id>/', reply_comment_view, name='reply_comment'),
    path("", get_all_tasks, name='all-tasks'),
    path("create/", create_new_task, name='create-task'),
    path("<int:task_id>/update/", update_task, name='update-task'),
    path("<int:task_id>.delete/", delete_task, name='delete-task'),

]