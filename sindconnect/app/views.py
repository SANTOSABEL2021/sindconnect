from django.shortcuts import render

def home(request):
    pais = 'Gana'
    return render(request, 'home.html', {'pais':pais})

def socios(request):
    return render(request,'socios.html')

def exemplos(request):
    return render(request,'exemplos.html')
