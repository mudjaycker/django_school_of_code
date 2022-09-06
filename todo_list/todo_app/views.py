from django.shortcuts import render
from .models import Auteur, ToDo

# Create your views here.

def add_new_todo(request):
    return render(request, template_name="add_todo.html", context=locals())