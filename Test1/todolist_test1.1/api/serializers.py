from rest_framework import serializers
from api.models import Todolist

class TodolistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todolist
        fields = '__all__'