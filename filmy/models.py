from django.db import models

# Create your models here.

class Film(models.Model):
    tytul = models.CharField(max_length=40)
    opis = models.TextField()
    rok = models.IntegerField(default=1900)
    plakat = models.ImageField(upload_to='plakaty',default=None)

    def __str__(self):
        return self.tytul