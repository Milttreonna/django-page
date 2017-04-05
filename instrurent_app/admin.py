from django.contrib import admin
# from .models import Book 
from .models import Instrument
from django.contrib.admin import register, ModelAdmin

# Register your models here.
# admin.site.register(Book)
admin.site.register(Instrument)
