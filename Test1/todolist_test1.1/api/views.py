from django.shortcuts import render
from api.serializers import TodolistSerializer
from api.models import Todolist
from rest_framework import generics


class TodoListList(generics.ListAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    
class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer

class TodoListUpdate(generics.UpdateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
    
class TodoDetailDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer