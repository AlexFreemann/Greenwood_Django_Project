from django.contrib import admin
from .models import *




class ListingAdmin(admin.ModelAdmin):


    class Meta:
        model=Listing

admin.site.register(Listing,ListingAdmin)

