from django.urls import path
from .views import HomeTemplateView, TodosTemplateView, AddTodosTemplateView, EditTodosTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('todos', TodosTemplateView.as_view(), name='todos'),
    path('add_todos', AddTodosTemplateView.as_view(), name='add_todos'),
    path('edit_todo', EditTodosTemplateView.as_view(), name='edit_todos'),
]