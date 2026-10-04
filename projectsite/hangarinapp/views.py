from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hangarinapp.models import Task, SubTask, Category, Priority, Note
from hangarinapp.forms import TaskForm, SubtaskForm, PriorityForm, CategoryForm, NoteForm
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

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    sucesss_url = reverse_lazy('task-list')

class TaskDelete(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

# ---


class SubtaskList(ListView):
    model = SubTask
    context_object_name = 'Subtask'
    template_name = 'subtask_list.html'
    paginate_by = 5

class SubtaskCreate(CreateView):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubtaskUpdate(UpdateView):
    model = SubTask
    form_class = SubtaskForm 
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubtaskDelete(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url= reverse_lazy('subtask-list')

# ---

class PriorityView(ListView):
    model = Priority
    context_object_name = 'Priority'
    template_name = 'priority_list.html'
    paginate_by = 5 

class PriorityCreate(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdate(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDelete(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

    # ---

class CategoryView(ListView):
    model = Category
    context_object_name = 'Category'
    template_name = 'category_list.html'
    paginate_by = 5

class CategoryCreate(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDelete(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

# ---

class NoteView(ListView):
    model = Note
    context_object_name = 'Note'
    template_name = 'note_list.html'
    paginate_by = 5

class NoteCreate(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDelete(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')





