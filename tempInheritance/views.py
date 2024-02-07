from django.shortcuts import render

# Create your views here.

def homeTemplate(request):
    return render(request, 'tempInheritance/home.html')

def productTemplate(request):
    return render(request, 'tempInheritance/product.html')

