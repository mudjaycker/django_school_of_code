from django.shortcuts import render, redirect
from .models import Auteur, ToDo

# Create your views here.

def add_new_todo(request):
    if request.method == "POST":
        auteur_id = request.POST.get("auteur")
        auteur_instance = Auteur.objects.get(user=auteur_id)
        titre = request.POST.get("titre")
        description = request.POST.get("description")
        date_fin = request.POST.get("date-fin")
        todo = ToDo(auteur=auteur_instance, titre=titre, description=description, date_fin=date_fin)
        todo.save()
        return redirect("/list-todos/")
    return render(request, template_name="add_todo.html")

def list_todos(request):
    todos = ToDo.objects.all()
    return render(request, template_name="list_todos.html", context=locals())

def get_one_task(request, pk):
    todo = ToDo.objects.get(id=pk)
    return render(request, template_name="one_task.html", context=locals())