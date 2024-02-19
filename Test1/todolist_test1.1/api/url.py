from django.urls import path , include
from api import views

urlpatterns = [
    path('todolist/list', views.TodoListList.as_view()),
    path('todolist/create', views.TodoListCreate.as_view()),
    path('todolist/update/<int:pk>', views.TodoListUpdate.as_view()),
    path('todolist/delete/<int:pk>', views.TodoDetailDelete.as_view()) 
]
