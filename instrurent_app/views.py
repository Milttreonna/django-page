from django.shortcuts import render
from django.http import HttpResponse
# from .models import Book
from .models import Instrument
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.

# def index(request):
#     books=Book.objects.all()
#     return render(request, "rentPage/index.html", {'books':books})


def index(request):
    return render(request, "rentPage/index.html")

def rent(request):
    instruments=Instrument.objects.all()
    return render(request, "rentPage/rent.html", {'instruments':instruments})

