from django.shortcuts import render, redirect

from todoapp.models import Todo


def add_view(request):
    return render(request, 'add_task.html', context={'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                                                                  ('ready', 'Сделано')]})


def add(request):
    description = request.POST.get('description')
    status = request.POST.get('status')
    deadline = request.POST.get('deadline')
    more_info = request.POST.get('more_info')
    article = Todo.objects.create(description=description, status=status, deadline=deadline, more_info=more_info)
    return redirect('main')
