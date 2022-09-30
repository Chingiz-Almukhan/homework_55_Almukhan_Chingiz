from django.urls import path

from todoapp.views.add import add_view
from todoapp.views.base import index_view
from todoapp.views.delete import delete, delete_view, multi_delete
from todoapp.views.edit import edit
from todoapp.views.task_view import task_view

urlpatterns = [
    path('', index_view, name='main'),
    path('task/<int:pk>', task_view, name='task'),
    path('add/', add_view, name='add'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/confirm/<int:pk>', delete, name='delete'),
    path('multi/', delete_view, name='delete_view'),
    path('multi/delete', multi_delete, name='multi_delete')
]