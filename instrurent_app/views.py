from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Instrument
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your views here.

def index(request):
    return render(request, "rentPage/index.html")

def rent(request):
    instruments=Instrument.objects.all()
    return render(request, "rentPage/rent.html", {'instruments':instruments})

def rent_item(request, id):
    item = Instrument.objects.get(pk=id)
    if item.instrument_quantity > 0:
        item.instrument_quantity -= 1
    item.save()
    return redirect('instrurent:rent')