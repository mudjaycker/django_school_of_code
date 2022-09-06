from django.urls import path
from . views import *


urlpatterns = [
    path('add-todo/', add_new_todo),
    path('list-todos/', list_todos),
    path('one-task/<int:pk>/', get_one_task),
]