from django.shortcuts import render
from .serializers import FilmSerializers
from rest_framework import viewsets
from .models import Film
# Create your views here.


class FilmViewset(viewsets.ModelViewSet):
    serializer_class = FilmSerializers
    queryset = Film.objects.all()