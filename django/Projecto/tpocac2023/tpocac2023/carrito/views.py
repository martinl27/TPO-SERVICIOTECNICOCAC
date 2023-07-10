from django.shortcuts import render
from .models import Carrito

# Create your views here.

def carrito(request):
    carritos = Carrito.objects.all()
    return render(request, "carrito/carrito.html", {'carritos': carritos})
