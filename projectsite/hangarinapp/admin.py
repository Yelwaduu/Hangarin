from django.contrib import admin
from .models import Priority, Task, SubTask, Category, Note


@admin.register(Priority)
class Priority(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'priority__name', 'category__name')
    search_fields = ('title', 'description')
    list_filter = ('status', 'priority__name', 'category__name')

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title','status','parent_task_name')
    list_select_related = ('parent_task',)

    @admin.display(description='Parent Task', ordering='parent_taks__title')
    def parent_task_name(self, obj):
        return obj.parent_task.title

    search_fields = ('title',)
    list_filter = ('status',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('task__title', 'content', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)
