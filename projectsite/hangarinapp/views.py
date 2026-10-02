from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from hangarinapp.models import Task, SubTask, Category, Priority, Note
from hangarinapp.forms import TaskForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'

class TaskList(ListView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task_list.html'
    paginate_by = 5

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')



