from django.shortcuts import render

from django.views.generic.list import ListView
from hangarinapp.models import Task, SubTask, Category, Priority, Note

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'
