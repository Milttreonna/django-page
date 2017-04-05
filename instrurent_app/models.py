from __future__ import unicode_literals

from django.db import models


# http://localhost:8000/instrurent_app/index right
# # Create your models here.
class Instrument(models.Model):
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
    instrument_quantity= models.IntegerField(max_length=200)

    def __str__(self):
        return self.instrument_choice

