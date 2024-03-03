from django.urls import path, include
from apps.task.views import home_page

app_name = 'router'

urlpatterns = [
    path("", home_page, name='home'),
    path("tasks/", include('apps.task.urls')),
    path("user/", include('apps.user.urls')),

    path("api/", include('apps.api.urls')),
]