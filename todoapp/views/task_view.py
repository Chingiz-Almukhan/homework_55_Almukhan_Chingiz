from django.shortcuts import render

from todoapp.models import Todo


def task_view(request, pk):
    task = Todo.objects.get(pk=pk)
    return render(request, 'task_view.html', context={
        'task': task,
        'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                     ('ready', 'Сделано')],
    })
