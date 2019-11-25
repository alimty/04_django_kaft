from django.shortcuts import render
from .forms import PageModelForm
from .models import Page
from django.contrib import messages


def index(request):
    context = dict()
    context['page'] = Page.objects.filter(status='published')
    return render(request, 'base/base.html', context)


def page_create(request):
    context = dict()
    context['title'] = 'Page Form'
    context['form'] = PageModelForm(request.POST)
    if request.method == 'POST':
        form = PageModelForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            print(item)
            item.save()
            messages.success(request, 'Page is created.')
    return render(request, 'manage/form.html', context)
