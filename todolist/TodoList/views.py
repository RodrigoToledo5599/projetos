from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls.base import reverse_lazy
from .models import *

class TaskList(ListView):
    model = Task
    template_name="TodoList/tasks.html"
    context_object_name="tasks"

class TaskDetail(DetailView):
    model = Task
    template_name="TodoList/task.html"
    context_object_name="task"

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')