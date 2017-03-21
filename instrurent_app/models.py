from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Instrument(models.Model):
    INSTRUMENT_CHOICES=(
        ('clarinet','Clarinet'),
        ('acoustic guitar','Acoustic Guitar'),
        ('banjo','Banjo'),
    ('conga','Conga Set'),
    ('drum','Drum Set'),
    ('electric guitar','Electric Guitar'),
    ('piano','Piano'),
    ('sax','saxophone'),
    ('trumpet','Trumpet'),
    ('violin','Violin')
    )

    instrument_choice= models.CharField(max_length="25", choices=INSTRUMENT_CHOICES)