from django.shortcuts import render

# Create your views here.

def index(request):#criando uma visão
    testChave = {
        'curso': 'Desenvolvimento Web Avançado'
    }
    return render(request, 'index.html') #index é geralmente a página principal