from django.conf.urls import url

from . import views

app_name="instrurent"


urlpatterns = [ 
    url(r'^index$', views.index, name='index'),
    url(r'^rent$', views.rent, name='rent'),
    url(r'^rent_item/(?P<id>[0-9]+)/$', views.rent_item, name='rent_item'),
    
]
