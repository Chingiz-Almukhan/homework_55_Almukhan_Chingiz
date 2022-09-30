from django.shortcuts import render, redirect

from todoapp.models import Todo


def delete(request, pk):
    articles = Todo.objects.get(pk=pk)
    articles.delete()
    return redirect('main')


def delete_view(request):
    articles = Todo.objects.all()
    context = {
        'articles': articles,
        'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                     ('ready', 'Сделано')],
    }
    return render(request, 'delete_tasks.html', context)


def multi_delete(request):
    task_id = request.POST.getlist('delete')
    for pk in task_id:
        Todo.objects.get(pk=pk).delete()
    return redirect('main')
