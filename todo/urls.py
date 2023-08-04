from django.urls import path
from . import views
urlpatterns = [
    path('',views.TodoFormShowView.as_view(), name='todoform'),
    path('todo_update/<int:pk>',views.todoUpdateView.as_view(), name='todoupdate'),
    path('todo_del/<int:pk>',views.todoDeleteView.as_view(), name='tododelete')
]
