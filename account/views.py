from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModifiedUserCreationForm, ModifiedUserLoginForm

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
            return render(request, 'registration/register.html', {"form": form})
    return render(request, 'registration/register.html', context)

def login(request):
  form = ModifiedUserLoginForm()
  context = {
    'form': form
  }
  return render(request, 'pages/auth/login.html', context)
