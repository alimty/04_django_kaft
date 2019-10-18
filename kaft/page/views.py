from django.shortcuts import render
from .forms import PageModelForm
from .models import Page
from django.contrib import messages


def index(request):
    context = dict()
    return render(request, 'home/index.html', context)


def page_create(request):
    context = dict()
    context['title'] = 'Page Form'

    if request.method == 'POST':
        form = PageModelForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            print(item)
            item.save()
            messages.success(request, 'Sayfa oluşturuldu.')
    return (request, 'manage/form.html', context)
