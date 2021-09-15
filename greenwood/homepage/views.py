from django.shortcuts import render
from listing.models import Listing
from random import sample

# def index(request):
#
#     return render(request,'homepage/homepage.html',locals())

# Create your views here.



def index(request):
    listings=Listing.objects.filter(is_main=True)
    print(listings)

    return render(request, 'homepage/homepage.html', locals())