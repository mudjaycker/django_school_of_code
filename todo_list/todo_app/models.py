from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def apres_une_semaine():
    return timezone.now() + timezone.timedelta(days=7)
# Create your models here.

class Auteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_phone = models.CharField(max_length=10, unique=True)


class ToDo(models.Model):
    auteur = models.ForeignKey(Auteur, to_field="user" ,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=apres_une_semaine)