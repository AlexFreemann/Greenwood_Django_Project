from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash)
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import CreateUserForm

from django.conf import settings
# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, )
from django.contrib.sites.shortcuts import get_current_site

from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url
from django.template.response import TemplateResponse

from django.utils.http import is_safe_url, urlsafe_base64_decode

from django.urls import path
from django.conf.urls import include

def registration(request):
    if request.user.is_authenticated:
        # return redirect(path('homepage/', include('homepage.urls')))
        print('ОТправить домой')

    form =CreateUserForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        # form1.save() #чтобы форма исчезла нужно перезаписать переменну ex form=form.save()
        form = form.save()
    return render(request,'account/registration/registration.html',locals())



def login_page(request, template_name='account/login/login.html',
          redirect_field_name='registration',
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)
