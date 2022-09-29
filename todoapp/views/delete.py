from django.shortcuts import render, redirect

from todoapp.models import Todo


def delete(request, pk):
    articles = Todo.objects.get(pk=pk)
    articles.delete()
    return redirect('main')
