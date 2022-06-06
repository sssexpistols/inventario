from django.shortcuts import render, redirect
from .models import *
from .forms import *


def inicio(request):
    return render(request, 'pages/inicio.html')


def nosotros(request):
    return render(request, 'pages/nosotros.html')


def productos(request):
    productos = Product.objects.all()
    return render(request, 'medicines_pages/index.html', {'productos': productos})


def crear(request):
    return render(request, 'medicines_pages/crear.html', {'formulario': formulario})


def editar(request):
    return render(request, 'medicines_pages/editar.html')


def formulario(request):
    return render(request, 'medicines_pages/form.html')


def eliminar(request, medicine_id):
    product = Product.objects.get(medicine_id=medicine_id)
    product.delete()
    return redirect('medicamentos')
