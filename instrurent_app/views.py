from django.shortcuts import render
from django.http import HttpResponse
# from .models import Book
from .models import Inventory
# Create your views here.

# def index(request):
#     books=Book.objects.all()
#     return render(request, "rentPage/index.html", {'books':books})


def index(request):
    instruments=Inventory.objects.all()
    return render(request, "rentPage/index.html", {'instruments':instruments})

def rent(request):
    return render(request, "rentPage/rent.html")
