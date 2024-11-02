from django.shortcuts import render
from .urls import *


def home(request):
    return render(request, 'home.html')