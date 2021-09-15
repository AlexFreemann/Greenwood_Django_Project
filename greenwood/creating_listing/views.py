from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewListingForm



def index(request):

    form =NewListingForm(request.POST, request.FILES or None)
    if request.method =='POST' and form.is_valid():
        print(form.data)
        print(form.cleaned_data)

        # form1.save() #чтобы форма исчезла нужно перезаписать переменну ex form=form.save()
        form = form.save()
        print(form.image_uploaded)
        form.image_url =f'http://127.0.0.1:8009/media/{form.image_uploaded}'
        form.save()



    return render(request,'creating_listing/creating_listing.html',locals())

# Create your views here.
