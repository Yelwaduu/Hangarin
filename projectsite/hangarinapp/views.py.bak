from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hangarinapp.models import Task, SubTask, Category, Priority, Note
from hangarinapp.forms import TaskForm, SubtaskForm, PriorityForm, CategoryForm, NoteForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone

class HomePageView(ListView):
    model = Task
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["total_task"] = Task.objects.count()
       context["pending_task"] = Task.objects.filter(status="Pending").count()
       context["completed_task"] = Task.objects.filter(status="Completed").count()
       context["overdue_task"] = Task.objects.filter(
           deadline__lt=timezone.now()).exclude(status="Completed").count()
       return context 

class TaskList(ListView):
    model = Task
    context_object_name = 'Task'
    template_name = 'task_list.html'
    paginate_by = 5
  
    def get_ordering(self):
        allowed = ['title', 'priority__id','category__id']
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return 'title'

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query)|
                Q(status__icontains=query)|
                Q(category__name__icontains=query)|
                Q(priority__name__icontains=query)
            )
        return qs
    

class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

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

    def get_ordering(self):
            allowed = ['title', 'status','parent_task__title']
            sort_by = self.request.GET.get("sort_by")
            if sort_by in allowed:
                return sort_by
            return 'title'
    
    def get_queryset(self):
            qs = super().get_queryset()
            query = self.request.GET.get('q')
    
            if query:
                qs = qs.filter(
                    Q(title__icontains=query)|
                    Q(status__icontains=query)|
                    Q(parent_task__title__icontains=query)|
                    Q(id__icontains=query)
                )
            return qs

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

    def get_ordering(self):
                allowed = ['name',"-name", "id"]
                sort_by = self.request.GET.get("sort_by")
                if sort_by in allowed:
                    return sort_by
                return 'name'
        
    def get_queryset(self):
                qs = super().get_queryset()
                query = self.request.GET.get('q')
        
                if query:
                    qs = qs.filter(
                        Q(name__icontains=query)
                       
                    )
                return qs


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

    def get_ordering(self):
                allowed = ['name','-name','id']
                sort_by = self.request.GET.get("sort_by")
                if sort_by in allowed:
                    return sort_by
                return 'name'
        
    def get_queryset(self):
                qs = super().get_queryset()
                query = self.request.GET.get('q')
        
                if query:
                    qs = qs.filter(
                        Q(name__icontains=query)
                    )
                return qs

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

    def get_ordering(self):
                allowed = ['id', 'task__title']
                sort_by = self.request.GET.get("sort_by")
                if sort_by in allowed:
                    return sort_by
                return 'id'
        
    def get_queryset(self):
                qs = super().get_queryset()
                query = self.request.GET.get('q')
        
                if query:
                    qs = qs.filter(
                        Q(task__title__icontains=query)|
                        Q(id__icontains=query)
                    )
                return qs

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





