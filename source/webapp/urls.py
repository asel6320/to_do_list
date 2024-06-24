from django.urls import path

from webapp.views import index, create_task, task_detail

urlpatterns = [
    path('', index),
    path('create/', create_task),
    path('task/', task_detail),
]