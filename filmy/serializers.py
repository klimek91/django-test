from rest_framework import serializers
from .models import Film

class FilmSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'plakat']


class FilmFullSerializers(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = ['id','tytul','opis','rok', 'plakat']