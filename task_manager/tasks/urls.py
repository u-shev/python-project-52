from django.urls import path
from .views import TasksView, TaskDetailView, \
    TaskCreateView, TaskUpdateView, TaskDeleteView


urlpatterns = [
    path('', TasksView.as_view(), name='tasks'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task'),
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update_task'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
]
