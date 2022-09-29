from django.shortcuts import render

from todoapp.models import Todo


def index_view(request):
    articles = Todo.objects.all()
    context = {
        'articles': articles,
        'statuses': [('new', 'Новая'), ('in process', 'В процессе'),
                     ('ready', 'Сделано')],
    }
    return render(request, 'main_page.html', context)
