from django.shortcuts import render
from .urls import *
from product.models import Product

def home(request):
    products = Product.objects.all()
    
    context = {
        'products':products,
    }
    return render(request, 'home.html', context)