from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Todos


class HomeTemplateView(View):
    template_name = 'index.html'
    context = {}

    def get(self, request):
        todos = Todos.objects.all()
        self.context.update({'todos': todos})
        return render(request, self.template_name, self.context)

    def post(self, request):
        pass


class TodosTemplateView(View):
    template_name = 'todo.html'
    context = {}

    def get(self, request):
        user = request.user
        todo = Todos.objects.filter(owner_id=user.id)
        self.context.update({'todo': todo})
        return render(request, self.template_name, self.context)

    def post(self, request):
        todo_id = request.POST.get('todo_id')
        Todos.objects.get(pk=todo_id).delete()
        return redirect('/todo')


class AddTodosTemplateView(View):
    template_name = 'add_todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        text = request.POST.get('todo')
        user = request.user
        todo = Todos.objects.create(
            text=text,
            owner=user
        )
        todo.save()
        messages.info(request, 'Todo added successfully')
        return redirect('/add_todos')


class EditTodosTemplateView(View):
    template_name = 'edit_todo.html'
    context = {}

    def get(self, request):
        return render(request, self.template_name, self.context)

    def post(self, request):
        text = request.POST.get('new_text')
        todo_id = request.POST.get('todo')
        user = request.user
        if Todos.objects.filter(owner=user, id=todo_id).exists():
            todo = Todos.objects.update(
                text=text
            )
            todo.save()
            return redirect('/todos')
        return redirect('/')