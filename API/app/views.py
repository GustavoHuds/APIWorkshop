from django.shortcuts import render
from rest_framework import viewsets
from .models import Applist, Pessoa
from .serializers import AppListSerializer, PessoaSerializer

class AppListViewset(viewsets.ModelViewSet):
    queryset = Applist.objects.all()
    serializer_class = AppListSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer