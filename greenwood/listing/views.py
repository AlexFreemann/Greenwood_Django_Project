from django.shortcuts import render
from listing.models import Listing
#
def index(request,listing_id):

    listing=Listing.objects.get(id=listing_id)

    return render(request,'listing/listing.html',locals())

# # Create your views here.
