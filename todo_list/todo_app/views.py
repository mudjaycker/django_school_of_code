from django.shortcuts import render
from .models import Auteur, ToDo

# Create your views here.

def add_new_todo(request):
    if request.method == "POST":
        auteur = request.POST.get("auteur")
        titre = request.POST.get("titre")
        description = request.POST.get("description")
        date_fin = request.POST.get("date_fin")
        print(f"auteur = {auteur}, titre = {titre},  description = {description}, date_fin = {date_fin}")
        print("datas = ", request.POST)
    return render(request, template_name="add_todo.html")