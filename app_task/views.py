from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def create(request):
    error = ''
    if request.method == 'POST':  # Передаем данные при помощи метода POST
        form = TaskForm(request.POST)  # Получаем данные
        if form.is_valid():  # Если данные корректны то мы их сохраняем в Базу данных
            form.save()
            return redirect('test')  # Переадресуем пользователя на другую страничку в данном случии test
        else:
            error = 'Форма была неверной'

    form = TaskForm
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context)
