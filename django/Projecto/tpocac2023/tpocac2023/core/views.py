from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"core/home.html")
def contacto(request):
    return render(request,"core/contacto.html")
def faq(request):
    return render(request,"core/faq.html")
def indumentaria(request):
    return render(request,"core/indumentaria.html")