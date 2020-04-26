from django.shortcuts import render
from .serializers import FilmSerializers, FilmFullSerializers
from rest_framework import viewsets
from .models import Film
from rest_framework.response import Response
# Create your views here.


class FilmViewset(viewsets.ModelViewSet):
    serializer_class = FilmSerializers
    queryset = Film.objects.all()

    def retrieve(self, request, *args, **kwargs):   #def z ctrl plus klik na ModelViewSet na RetriveModelMixin >  vievsets.py > mixins.py
        film = self.get_object()
        serializer = FilmFullSerializers(film)   #tu wklejamy FillFull zeby po kliknieciu GET na element (tj po przejsciu w indeks elementu wyswieltilty sie wszystkie elementy)
        return Response(serializer.data)