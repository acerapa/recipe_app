from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ModifiedUserCreationForm, ModifiedUserLoginForm

import json

# User registration
def registerUser(request):
    form = ModifiedUserCreationForm(request.POST or None)
    context = {
        'form': form 
    }
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('User Saved!')
        else:
            error_messages = json.loads(form.errors.as_json())
            return render(request, 'registration/register.html', {"form": form, "error_messages": error_messages})
    return render(request, 'registration/register.html', context)

# User login
def login(request):
  form = ModifiedUserLoginForm(data=request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        auth_login(request, user)
        print('welcome')
        return redirect(to='welcome')
    else: 
        error_messages = json.loads(form.errors.as_json())
        print(error_messages)
        return render(request, 'pages/auth/login.html', {"form": form, "error_messages": error_messages})
  context = {
    'form': form
  }
  return render(request, 'pages/auth/login.html', context)
