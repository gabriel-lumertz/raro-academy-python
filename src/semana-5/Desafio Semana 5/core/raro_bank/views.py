from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Caixinha

# Create your views here.

def home(request):
    return render(request, 'home.html')

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        objective = request.POST.get('objective')
        value = request.POST.get('value')
        if value == "":
            value = 0

        caixinha = Caixinha(
            name=name,
            objective=objective,
            value=value
        )

        caixinha.save()

        return redirect('listar_caxinha')

    return render(request, 'create.html')

def read(request):

    caixinhas = Caixinha.objects.all()

    contexto = {
        'caixinhas': caixinhas
    }

    return render(request, 'read.html', contexto)

def update(request, id):
    
    caixinha = Caixinha.objects.get(id=id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        objective = request.POST.get('objective')
        value = request.POST.get('value')
        if value == "":
            value = 0

        caixinha.name = name
        caixinha.objective = objective
        caixinha.value = value

        caixinha.save()
        
        return redirect('listar_caxinha')

    return render(request, 'update.html', {'caixinha': caixinha})

def delete(request, id):

    caixinha = Caixinha.objects.get(id=id)
    caixinha.delete()

    return redirect('listar_caxinha')