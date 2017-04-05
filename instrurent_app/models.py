from __future__ import unicode_literals

from django.db import models


# http://localhost:8000/instrurent_app/index right
# # Create your models here.
class Instrument(models.Model):
    instrument_choice= models.CharField(max_length=25)
    instrument_quantity= models.IntegerField(default=200)
    instrument_description = models.CharField(max_length= 2000)
    instrument_price= models.FloatField(max_length=None)

    def __str__(self):
        return self.instrument_choice
    
