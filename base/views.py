# from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'base/list.html'


class DetailList(DetailView):
    model = Task
    context_object_name = 'TasksDetail'
    template_name = 'base/task.html'


class TaskCreate(CreateView):
    model = Task
    template_name = 'base/create_task.html'
    fields = '__all__'
    success_url = reverse_lazy('tasklist')
