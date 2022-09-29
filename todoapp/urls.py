from django.urls import path

from todoapp.views.add import add_view, add
from todoapp.views.base import index_view
from todoapp.views.delete import delete
from todoapp.views.edit import edit, confirm_edit
from todoapp.views.task_view import task_view

urlpatterns = [
    path('', index_view, name='main'),
    path('task/<int:pk>', task_view, name='task'),
    path('add/', add_view, name='add'),
    path("add/add_to_list/", add, name='confirm_add'),
    path('edit/<int:pk>', edit, name='edit'),
    path('edit/confirm/edit/', confirm_edit, name='confirm_edit'),
    path('delete/confirm/<int:pk>', delete, name='delete')
]