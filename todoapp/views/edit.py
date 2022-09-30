from django.shortcuts import render, redirect

from todoapp.forms import TodoForm
from todoapp.models import Todo


def edit(request, pk):
    article = Todo.objects.get(pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial={
            'description': article.description,
            'status': article.status,
            'deadline': article.deadline,
            'more_info': article.more_info

        })
        return render(request, 'edit_task.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            article.description = form.cleaned_data['description']
            article.status = form.cleaned_data["status"]
            article.deadline = form.cleaned_data['deadline']
            article.more_info = form.cleaned_data['more_info']
            print(article.deadline)
            article.save()
            return redirect('main')
        else:
            return render(request, 'edit_task.html', context={'form': form, 'article': article})
