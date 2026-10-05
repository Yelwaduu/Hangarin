from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from hangarinapp.models import Task, SubTask, Category, Priority, Note
from hangarinapp.forms import TaskForm, SubtaskForm, PriorityForm, CategoryForm, NoteForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, ListView):
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

class TaskList(LoginRequiredMixin, ListView):
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


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('home')

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

# ---


class SubtaskList(LoginRequiredMixin, ListView):
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

class SubtaskCreate(LoginRequiredMixin, CreateView):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubtaskUpdate(LoginRequiredMixin, UpdateView):
    model = SubTask
    form_class = SubtaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubtaskDelete(LoginRequiredMixin, DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url= reverse_lazy('subtask-list')

# ---

class PriorityView(LoginRequiredMixin, ListView):
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


class PriorityCreate(LoginRequiredMixin, CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdate(LoginRequiredMixin, UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDelete(LoginRequiredMixin, DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

    # ---

class CategoryView(LoginRequiredMixin, ListView):
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

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

# ---

class NoteView(LoginRequiredMixin, ListView):
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

class NoteCreate(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdate(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')





