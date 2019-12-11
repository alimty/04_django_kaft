from django.shortcuts import render
from .forms import UserModelForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def signup (request):
    context = dict()
    context ['title'] = 'Sign-up Screen'
    context['form'] = UserModelForm(request.POST)
    if request.methode == 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
          item = form.save(commit=False)
          print(item)
          item.save()
          messages.success(request, 'You signed up')
    return render(request, 'user/signup.html', context)

  

