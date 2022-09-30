from django.shortcuts import render, redirect

from todoapp.models import Todo
from todoapp.forms import TodoForm


def add_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'add_task.html', context={'form': form,
                                                         'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                                                                      ('ready', 'Сделано')]
                                                         })
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            article = Todo.objects.create(description=form.cleaned_data['description'],
                                          status=form.cleaned_data["status"], deadline=form.cleaned_data['deadline'],
                                          more_info=form.cleaned_data['more_info'])
            return redirect('main')
        else:
            return render(request, 'add_task.html', context={'form': form})
