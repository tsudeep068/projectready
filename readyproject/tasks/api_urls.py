from django.urls import path
from .views import TaskListAPI
from . import views

urlpatterns = [
    path('tasks/', views.TaskListAPI, name='task_list_api'),
    path('categories/', views.CategoryListAPI, name='category_list_api'),
    path('total_tasks/', views.totaltasks, name='total_tasks_api'),
    path('totalcat/', views.totalcategories, name='total_categories_api'),
    path('delete_task/<int:id>/', views.delete_all_tasks, name='delete_task_api'),
]
