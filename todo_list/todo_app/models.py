from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def apres_une_semaine():
    return timezone.now() + timezone.timedelta(days=7)
# Create your models here.

class Auteur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)