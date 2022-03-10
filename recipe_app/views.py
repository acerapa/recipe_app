from django.shortcuts import render

def welcome(request):
    return render(request, 'layouts\app.html')
