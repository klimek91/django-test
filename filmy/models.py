from django.db import models

# Create your models here.

class Film(models.Model):
    tytul = models.CharField(max_length=40)
    opis = models.TextField()
    rok = models.IntegerField(default=1900)
