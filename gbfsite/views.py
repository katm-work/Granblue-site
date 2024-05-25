from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'products': ''})

def about(request):
    return render(request, 'about.html', {'products': ''})