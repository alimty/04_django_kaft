from django.shortcuts import render, redirect
from .forms import UserModelForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup (request):
    context = dict()
    context ['title'] = 'Sign-up Screen'
    context['form'] = UserModelForm(request.POST)
    if request.method== 'POST':
        form = UserModelForm(request.POST)
        if form.is_valid():
          item = form.save(commit=False)
          print(item)
          item.save()
          messages.success(request, 'You signed up')
    return render(request, 'user/signup.html', context)


def user_login(request):
  context=dict()
  context["title"]= "Kullanici Girisi"
  if request.method== "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(f"Kullanici adi:{username} sifre:{password}")
    if username and password is not None:
      user = authenticate(
        username=username,
        password=password
      )
      if user is not None:
        login(request, user)
        context['was_logged'] = True
        return render(request, 'base/base.html', context)
    messages.warning(request, 'Kullanici adi ve sifre hatali')
  return render(request, 'user/login.html',  context)

def user_logout(request):
  print("logout edildi")
  logout(request)
  context=dict()
  context['was_logged'] = None
  return render(request, 'base/base.html', context)

