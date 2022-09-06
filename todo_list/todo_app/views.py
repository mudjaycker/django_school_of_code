from django.shortcuts import render, redirect
from django.contrib import auth
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

def delete_task(request, pk):
    if request.method == "POST":
        todo = ToDo.objects.get(id=pk)
        todo.delete()
        return redirect("/list-todos/")
    return render(request, template_name="delete_task.html")

def update_task(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == "POST":
        todo.titre = request.POST.get("titre")
        todo.description = request.POST.get("description")
        todo.date_fin = request.POST.get("date-fin")
        todo.save()
        return redirect("/list-todos/")
    return render(request, template_name="update_task.html", context={"todo": todo})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)

        if user:
            auth.login(request, user)
            return redirect("/list-todos/")
        return render(request, template_name="login.html")
