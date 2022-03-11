from django.shortcuts import render
from django.http import HttpResponse
from .forms import ModifiedUserCreationForm

def welcome(request):
    return render(request, 'pages/index.html')

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
