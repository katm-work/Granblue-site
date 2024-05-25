from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'products': ''})

def about(request):
    return render(request, 'about.html', {'products': ''})

def forum(request):
    return render(request, 'forum.html', {'products': ''})

def resources(request):
    return render(request, 'resources.html', {'products': ''})