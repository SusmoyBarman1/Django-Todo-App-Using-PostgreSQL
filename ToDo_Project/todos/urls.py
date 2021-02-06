from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('insert_todo/', views.insert_todo, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item')
]
