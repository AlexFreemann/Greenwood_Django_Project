from django.shortcuts import render
from listing.models import Listing


def index(request):
    listings = Listing.objects.all()
    return render(request, 'catalog/catalog.html', locals())

