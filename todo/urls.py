from django.urls import path, include
from . import views

urlpatterns = [
    path('all_tasks', views.all_tasks, name="all_tasks"),
    path('add_task', views.add_task, name='add_task'),
    path('remove_task/<int:id>/', views.remove_task, name='remove_task')
]
