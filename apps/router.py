from django.urls import path, include


app_name = 'router'

urlpatterns = [

    path("tasks/", include('apps.task.urls')),
    path("user/", include('apps.user.urls'))
]