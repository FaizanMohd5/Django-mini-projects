from django.urls import path
from todo import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<int:id>/', views.delete, name='delete_task'),
    path('update/<int:id>/', views.edit, name='edit_task'),
    path('complete/<int:id>/', views.mark_complete, name = 'mark_complete'),
    path('incomplete/<int:id>/', views.mark_incomplete, name='mark_incomplete'),
    path('task/<int:id>/', views.task_detail, name='task_detail'), 
]

