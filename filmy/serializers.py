from rest_framework import serializers
from .models import Film

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id','tytul','opis','rok']