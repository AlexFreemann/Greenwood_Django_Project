from django import forms
from listing.models import *

class NewListingForm(forms.ModelForm):

    class Meta:
        model=Listing
        exclude=['listing_link','image_url','is_active','is_main']


