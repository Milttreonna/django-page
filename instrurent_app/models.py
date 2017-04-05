from __future__ import unicode_literals

from django.db import models


# http://localhost:8000/instrurent_app/index right
# # Create your models here.
class Instrument(models.Model):
    instrument_choice= models.CharField(max_length=25)
    instrument_quantity= models.IntegerField(default=200)
    instrument_description = models.CharField(max_length= 2000)

    instrument_price= models.FloatField(max_length=None)
    instrument_image=models.CharField(max_length=300)

    def format_price(self):
        instrument_price= round(self.instrument_price,2)
        return instrument_price

    def show_image(self):
        return 'decor/images/' + self.instrument_image

    def __str__(self):
        return self.instrument_choice
    
