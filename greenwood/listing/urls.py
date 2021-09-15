from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings


from listing import views

urlpatterns = [
    url(r'^listing/(?P<listing_id>\w+)/$', views.index, name='listing'),

]