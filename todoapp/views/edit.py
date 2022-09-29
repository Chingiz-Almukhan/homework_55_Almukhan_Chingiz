from django.shortcuts import render, redirect

from todoapp.models import Todo


def edit(request, pk):
    articles = Todo.objects.get(pk=pk)
    context = {'article': articles}
    return render(request, 'edit_task.html', context)


def confirm_edit(request):
    pk = request.POST.get('id')
    articles = Todo.objects.get(pk=pk)
    articles.description = request.POST.get('description')
    articles.status = request.POST.get('status')
    articles.deadline = request.POST.get('deadline')
    articles.more_info = request.POST.get('more_info')
    articles.save()
    return redirect('main')
