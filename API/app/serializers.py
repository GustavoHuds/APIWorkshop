from rest_framework import serializers
from app.models import Applist, Pessoa

class AppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Applist
        fields = '__all__'

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome']