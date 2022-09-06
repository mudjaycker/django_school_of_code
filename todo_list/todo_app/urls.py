from django.urls import path
from . views import *


urlpatterns = [
    path('add-todo/', add_new_todo),
    path('list-todos/', list_todos),
    path('one-task/<int:pk>/', get_one_task),
    path('delete-task/<int:pk>/', delete_task),
    path('update-task/<int:pk>/', update_task),
    path('login/', login),
    path('enregistrement/', enregistrement),
]