from django.shortcuts import render
from places.models import Place
# Create your views here.


def ukplaces(request,placeslug):
    template = 'place.html'
    places = Place.objects.filter(active=2,district__state__slug=placeslug).order_by('-id')
    return render(request,template,locals())



def placesdetails(request,placeslug):
    template = 'placedetail.html'
    place_obj = Place.objects.get(slug=placeslug)
    return render(request,template,locals())