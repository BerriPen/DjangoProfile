from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'appProfile/home.html')

def arca(request):
    return render(request, 'appProfile/arcaProf.html')

def lino(request):
    return render(request, 'appProfile/linoProf.html')

def viojan(request):
    return render(request, 'appProfile/viojanProf.html')
