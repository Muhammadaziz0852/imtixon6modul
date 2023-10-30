from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    template = 'index.html'
    context = {}

    def get(self, requets):
        product = Todo.objects.all()
        self.context.update({'message': product})
        return render(requets, self.template, self.context)


class AddTodoView(View):
    template = 'add_todo.html'
    contex = {}

    def get(self, request):
        return render(request, self.template, self.contex)

    def post(self, request):
        title = request.POST.get('message')
        user_id = request.user
        todos=Todo.objects.create(
            text=title,
            user=user_id
        )
        todos.save()
        return redirect('/')
