from django.urls import path
from . views import *


urlpatterns = [
    path('add-todo/', add_new_todo, name='add_todo'),
    path('list-todos/', list_todos, name="list_todo"),
    path('one-task/<int:pk>/', get_one_task, name="one-task"),
    path('delete-task/<int:pk>/', delete_task, name="delete_task"),
    path('update-task/<int:pk>/', update_task, name="update_task"),
    path('login/', login, name="login"),
    path('enregistrement/', enregistrement, name="enregistrement"),
]