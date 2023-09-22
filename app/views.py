from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddWordForm


def page_not_found(request, exception):
    return HttpResponse('<h1>Страница не найдена</h1>')

def index(request):
    context = {'title': 'My dictionary'}
    return render(request, 'app/index.html', context=context)

def words_list(request):
    context = {'title': 'List of words'}
    return render(request, 'app/words_list.html', context=context)

def add_word(request):
    if request.method == "POST":
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddWordForm()
    context = {'title': 'Add word', 'form': form}
    return render(request, 'app/add_word.html', context=context)
