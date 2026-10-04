"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hangarinapp.views import (HomePageView, TaskList, TaskCreate, TaskUpdate, TaskDelete, 
                               SubtaskList, SubtaskCreate, SubtaskUpdate, SubtaskDelete,
                               PriorityView, PriorityCreate, PriorityUpdate, PriorityDelete,
                               CategoryView, CategoryCreate, CategoryUpdate, CategoryDelete,
                               NoteView, NoteCreate, NoteUpdate, NoteDelete)
from hangarinapp import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    path('task_list', TaskList.as_view(), name='task-list' ),
    path('task_list/add', TaskCreate.as_view(), name='task-add'),
    path('task_list/<pk>', TaskUpdate.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDelete.as_view(), name='task-delete'),
    # ---
    path('subtask_list', SubtaskList.as_view(), name='subtask-list'),
    path('subtask_list/add', SubtaskCreate.as_view(), name='subtask-add'),
    path('subtask_list/<pk>', SubtaskUpdate.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete', SubtaskDelete.as_view(), name='subtask-delete'),
    # ---
    path('priority_list', PriorityView.as_view(), name='priority-list'),
    path('priority_list/add', PriorityCreate.as_view(), name='priority-add'),
    path('priority_list/<pk>', PriorityUpdate.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', PriorityDelete.as_view(), name='priority-delete'),
    # ---
    path('category_list', CategoryView.as_view(), name='category-list'),
    path('category_list/add', CategoryCreate.as_view(), name='category-add'),
    path('category_list/<pk>', CategoryUpdate.as_view(), name='category-update'),
    path('category_list/<pk>/delete', CategoryDelete.as_view(), name='category-delete'),
    # ---
    path('note_list',  NoteView.as_view(), name='note-list'),
    path('note_list/add', NoteCreate.as_view(), name='note-add'),
    path('note_list/<pk>', NoteUpdate.as_view(), name='note-update'),
    path('note_list/<pk>/delete', NoteDelete.as_view(), name='note-delete')


]
