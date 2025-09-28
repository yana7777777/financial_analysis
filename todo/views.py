from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from todo import views
from .forms import TodoForm
from .models import Todo
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def home(request):
    return render(request, 'todo/home.html')


# def current_todos(request):
#     todos = Todo.objects.order_by('-date')
#     return render(request, 'todo/currenttodos.html', {"todos": todos})

@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True, is_deleted=False)
    return render(request, 'todo/currenttodos.html', {'todos': todos})


def todo_detail(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'todo/tododetails.html', {'todo': todo})


@login_required
def create_todo(request):
    if request.method == "GET":
        return render(request, 'todo/createtodo.html', {"form": TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/createtodo.html', {"form": TodoForm(), 'error': 'Переданы не верные данные'})


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Неверные данные'})


@login_required
def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)

    if request.method == 'POST':
        todo.completed = True
        todo.save()
        return redirect('currenttodos')  # ВАЖНО: всегда возвращать redirect или HttpResponse

    # Если метод не POST, тоже возвращаем редирект
    return redirect('currenttodos')


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completedtodos.html', {'todos': todos})


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect('currenttodos')


@login_required
def trash_bin(request):
    delete_todos = Todo.objects.filter(user=request.user, is_deleted=True)
    return render(request, 'todo/trashbin.html', {'delete_todos': delete_todos})


@login_required
def soft_delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    todo.is_deleted = True
    todo.save()
    return redirect('currenttodos')


@login_required
def restore_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    todo.is_deleted = False
    todo.save()
    return redirect('trashbin')