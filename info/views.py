from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'info/infos.html')

def about(request):
    return render(request, 'info/about.html')

def glava(request):
    return render(request, 'info/glava.html')

def priv(request):
    return render(request, 'info/enterlayout.html')
