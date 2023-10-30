from django.urls import path
from .views import (
     HomeView,
     AddTodoView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', AddTodoView.as_view(), name='add_todo')
]
