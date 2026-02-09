from django.urls import path
from . import views


urlpatterns = [
    #task urls
    path('create/', views.create_task, name='create_task'),
    path('details/', views.taskdetails, name='taskdetails'),
    path('delete/<int:id>/', views.taskdelete, name='taskdelete'),
    path('update/<int:id>/', views.taskupdate, name='taskupdate'),

    #category urls
    path('category/create/', views.create_category, name='create_category'),

    #admin urls
    path('admindashboard/', views.admindashboard, name='taskopen'),
    
]