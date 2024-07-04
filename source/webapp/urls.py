from django.urls import path

from webapp.views import index, create_task, task_detail, update_task, delete_task, delete_tasks

urlpatterns = [
    path('', index, name='tasks'),
    path('create/', create_task, name='create_task'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/<int:pk>/update/', update_task, name='update_task'),
    path('task/<int:pk>/delete/', delete_task, name='delete_task'),
    path('delete_tasks', delete_tasks, name='delete_tasks'),
]

