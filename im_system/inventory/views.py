from django.shortcuts import render, redirect
from .models import *


def index(request):
    return render(request, "index.html")
'''
def laptops(request):
    return render(request, "laptops.html")
'''
def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,

    }
    return render(request , 'laptops.html', context)