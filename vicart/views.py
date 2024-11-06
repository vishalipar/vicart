from django.shortcuts import render
from .urls import *
from product.models import Product

def home(request):
    product = Product.objects.all()
    
    context = {
        'product':product,
    }
    return render(request, 'home.html', context)