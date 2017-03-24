from __future__ import unicode_literals

from django.db import models
from django.template.defaulttags import register

# http://localhost:8000/instrurent_app/index right
# # Create your models here.
class Inventory(models.Model):
    INSTRUMENT_CHOICES=(
    ('clarinet','Clarinet'),
    ('acoustic guitar','Acoustic Guitar'),
    ('banjo','Banjo'),
    ('conga','Conga Set'),
    ('drum','Drum Set'),
    ('electric guitar','Electric Guitar'),
    ('piano','Piano'),
    ('sax','Saxophone'),
    ('trumpet','Trumpet'),
    ('violin','Violin')
    )

    instrument_choice= models.CharField(max_length=25, choices=INSTRUMENT_CHOICES)
    def __str__(self):
        return self.instrument_choice


# #try __init__

#     def __str__(self,name,instrument_choice):
#         # self.name=name 
#         return self.name, self.instrument_choice 
# # class Choice(models.Model):


# #Example  

# class Inventory:
#     def __init__(self , price, quantity, name):
#         self.price=price
#         self.quantity=quantity
#         self.name=name
    
#     def sell(self):
#         self.quantity-=1

# snickers= Inventory(1.60, 2, "Snickers")
# snickers.sell()
# snickers.quantity()

# class Book(models.Model):
#     author=models.CharField(max_length=200)
#     title=models.CharField(max_length=200)
#     price=models.IntegerField()

#     def __str__(self):
#         return self.author


# book=Book("John Greene", "TFIOS")
# book.title()
# book.authors()