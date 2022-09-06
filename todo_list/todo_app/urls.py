from django.urls import path
from . views import *


urlpatterns = [
    path('add-todo/', add_new_todo),
]