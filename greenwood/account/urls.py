from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.login_page, name="login"),
]